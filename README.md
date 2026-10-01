# ComfyUI Info PL

**Dokumentacja nodów ComfyUI po polsku** — zakładka *Info* w panelu noda pokazuje opis po polsku.
Tłumaczony jest tylko zwykły tekst: nazwy parametrów (`ckpt_name`, `MODEL`…), typy danych, kod i linki zostają bez zmian, więc dalej pasują do tego, co widzisz na nodach.

*English below.*

## Jak to działa

1. Otwierasz zakładkę **Info** dowolnego noda.
2. Dodatek bierze oryginalny angielski opis i szuka polskiej wersji:
   - **gotowe tłumaczenia** dołączone do paczki (`translations/pl/`) — działają od razu, bez internetu,
   - **pamięć podręczna** (`cache/`) — wszystko, co zostało już raz przetłumaczone,
   - **tłumaczenie automatyczne** przez [OpenRouter](https://openrouter.ai) — tylko jeśli podasz klucz API. Każdy nod tłumaczy się **raz**, potem wczytuje się z dysku.
3. Jeśli tłumaczenia nie ma i nie da się go zrobić, widzisz zwykły angielski opis — nic się nie psuje.

Gotowe tłumaczenia (v0.1): Load Checkpoint, CLIP Text Encode, KSampler, VAE Encode, VAE Decode, Empty Latent Image, Load Image, Preview Image, Save Image, Blur Image.

## Instalacja

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/<twoj-login>/comfyui-info-pl
```

Uruchom ponownie ComfyUI i odśwież przeglądarkę.

### Tłumaczenie pozostałych nodów (opcjonalnie)

Dodaj klucz OpenRouter — jako zmienną środowiskową albo w pliku `ComfyUI/.env`:

```
OPENROUTER_API_KEY=sk-or-...
```

Domyślny model to `google/gemini-3.1-flash-lite` — przetłumaczenie jednego opisu kosztuje ułamek centa. Inny model ustawisz zmienną `INFO_PL_MODEL`.

### Wyłączanie

**Ustawienia → Info PL → „Info nodów po polsku”**.

## Pomóż przetłumaczyć

Tłumaczenia leżą w `translations/pl/<NazwaNoda>.md`, a w `translations/pl/sources.json` jest skrót SHA-256 angielskiego oryginału, z którego powstały. Dobre tłumaczenie z `cache/` możesz poprawić i dodać przez pull request: skopiuj plik do `translations/pl/<NazwaNoda>.md` i dopisz skrót oryginału do `sources.json`.

Zasada: tłumaczymy zdania i nagłówki; nie ruszamy tekstu w `backtickach`, kodu, linków i typów danych.

## Licencja

GPL-3.0, tak jak [ComfyUI](https://github.com/comfyanonymous/ComfyUI) i oryginalna dokumentacja [Comfy-Org/embedded-docs](https://github.com/Comfy-Org/embedded-docs), z której pochodzą tłumaczenia.

---

## English

**Polish translation of the ComfyUI node documentation** (the *Info* tab in the node panel). Only prose is translated — parameter names in backticks, data types, code blocks and links stay untouched.

- Bundled, hand-checked translations for the most common core nodes work offline.
- Any other node is translated once via OpenRouter (if `OPENROUTER_API_KEY` is set) and cached on disk.
- Falls back to the original English text when no translation is available.
- Toggle in **Settings → Info PL**.

Install: clone into `ComfyUI/custom_nodes` and restart. License: GPL-3.0.
