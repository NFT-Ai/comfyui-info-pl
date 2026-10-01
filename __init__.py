"""ComfyUI Info PL — zakładka Info (dokumentacja nodów) po polsku.

Frontend (js/info_pl.js) przechwytuje pobieranie plików pomocy *.md i wysyła oryginał tutaj.
Kolejność szukania tłumaczenia:
  1. translations/pl/<Nod>.md — gotowe tłumaczenia z paczki (sprawdzone ręcznie),
  2. cache/<sha256 oryginału>.md — wcześniej przetłumaczone automatycznie,
  3. OpenRouter (LLM) — gdy ustawiony klucz OPENROUTER_API_KEY; wynik trafia do cache.
Tłumaczony jest tylko zwykły tekst: `nazwy w backtickach`, kod, typy danych i linki zostają.
"""
import asyncio
import hashlib
import json
import os
import re
import ssl
import urllib.request
from pathlib import Path

import folder_paths
from aiohttp import web
from server import PromptServer

WEB_DIRECTORY = "./js"
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

HERE = Path(__file__).resolve().parent
BUNDLED = HERE / "translations" / "pl"
SOURCES = json.loads((BUNDLED / "sources.json").read_text()) if (BUNDLED / "sources.json").exists() else {}
CACHE = HERE / "cache"
CACHE.mkdir(exist_ok=True)
MODEL = os.environ.get("INFO_PL_MODEL", "google/gemini-3.1-flash-lite")
DOC_URL = re.compile(r"/docs/(?P<node>[^/?#]+?)(?:/[\w-]+)?\.md")

try:
    import certifi
    SSL = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL = ssl.create_default_context()

PROMPT = """Przetłumacz poniższą dokumentację w Markdown z angielskiego na polski.
Zasady:
- Tłumacz tylko zwykły tekst: zdania, nagłówki, nagłówki kolumn tabel, opisy.
- NIE zmieniaj niczego w `backtickach`, w blokach ``` kodu, w adresach URL ani w nazwach typów danych pisanych WIELKIMI LITERAMI (np. COMBO, MODEL, IMAGE, LATENT, INT, FLOAT, STRING).
- Nazwy parametrów i nodów, które w tabelach nie są w backtickach (np. seed, steps, cfg, denoise), też zostaw bez zmian.
- Zachowaj dokładnie strukturę Markdown: tabele, listy, pogrubienia, linie, liczbę kolumn.
- Używaj naturalnej polszczyzny i terminologii ComfyUI/grafiki (latent, prompt, sampler, checkpoint można zostawić).
- Zwróć wyłącznie przetłumaczony Markdown, bez komentarzy i bez otaczania go blokiem kodu.

"""


def api_key():
    """Klucz z OPENROUTER_API_KEY albo z pliku .env w katalogu głównym ComfyUI."""
    key = os.environ.get("OPENROUTER_API_KEY")
    env_file = Path(folder_paths.base_path) / ".env"
    if not key and env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.strip().startswith("OPENROUTER_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"\'')
    return key or None


def llm_translate(text):
    key = api_key()
    if not key:
        raise RuntimeError("brak OPENROUTER_API_KEY")
    body = {"model": MODEL, "temperature": 0,
            "messages": [{"role": "user", "content": PROMPT + text}]}
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions", data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "X-Title": "ComfyUI Info PL"})
    with urllib.request.urlopen(req, timeout=120, context=SSL) as r:
        out = json.load(r)["choices"][0]["message"]["content"].strip()
    if out.startswith("```"):  # model mimo zakazu owinął wynik w blok kodu
        out = out.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return out


def md(text):
    return web.Response(text=text, content_type="text/markdown")


@PromptServer.instance.routes.post("/info_pl/translate")
async def translate_route(request):
    data = await request.json()
    text, url = data.get("text", ""), data.get("url", "")
    sha = hashlib.sha256(text.encode()).hexdigest()
    m = DOC_URL.search(url)
    bundled = BUNDLED / f"{m['node']}.md" if m else None
    has_bundled = bundled is not None and bundled.exists()

    if has_bundled and SOURCES.get(m["node"]) == sha:
        return md(bundled.read_text())
    cached = CACHE / f"{sha}.md"
    if cached.exists():
        return md(cached.read_text())
    try:
        pl = await asyncio.get_running_loop().run_in_executor(None, llm_translate, text)
    except Exception as e:
        if has_bundled:  # oryginał się zmienił, a nie ma czym przetłumaczyć — starsze tłumaczenie lepsze niż nic
            return md(bundled.read_text())
        print(f"[Info PL] {m['node'] if m else url}: nie przetłumaczono ({e})")
        return web.json_response({"error": str(e)}, status=503)
    cached.write_text(pl)
    return md(pl)
