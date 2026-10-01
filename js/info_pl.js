// Info PL — podmienia dokumentację nodów (zakładka Info) na polską wersję.
// Przechwytuje pobieranie /docs/<Nod>/<język>.md oraz /extensions/<paczka>/docs/...md,
// wysyła oryginał do /info_pl/translate, a gdy tłumaczenie się nie uda — pokazuje oryginał.
import { app } from "../../scripts/app.js";

const SETTING = "InfoPL.Enabled";
const DOC_RE = /\/docs\/[^?#]+\.md(?:[?#]|$)/;

app.registerExtension({
  name: "info_pl",
  settings: [
    {
      id: SETTING,
      category: ["Info PL", "Dokumentacja", "Włączone"],
      name: "Info nodów po polsku (tłumaczy tylko zwykły tekst, nazwy zostają)",
      type: "boolean",
      defaultValue: true,
    },
  ],
  setup() {
    const originalFetch = window.fetch.bind(window);
    window.fetch = async (input, init) => {
      const url = typeof input === "string" ? input : input?.url ?? String(input);
      const res = await originalFetch(input, init);
      const enabled = app.extensionManager?.setting?.get(SETTING) ?? true;
      if (!enabled || !DOC_RE.test(url) || !res.ok) return res;
      const type = res.headers.get("content-type") ?? "";
      if (type.includes("text/html")) return res; // brak pliku pomocy — zostaw jak jest

      const original = await res.clone().text();
      try {
        const tr = await originalFetch("/info_pl/translate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: original, url }),
        });
        if (!tr.ok) return res;
        return new Response(await tr.text(), {
          status: 200,
          headers: { "Content-Type": "text/markdown; charset=utf-8" },
        });
      } catch (e) {
        console.warn("[Info PL]", e);
        return res;
      }
    };
  },
});
