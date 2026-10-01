# CLIP Text Encode (Prompt)

Koduje prompt tekstowy modelem CLIP do postaci embeddingu, który kieruje model dyfuzyjny w stronę generowania konkretnych obrazów.

`CLIP Text Encode (CLIPTextEncode)` działa jak tłumacz: zamienia Twój opis tekstowy na format zrozumiały dla AI. Dzięki temu AI może zinterpretować Twoje polecenie i wygenerować oczekiwany obraz.

Wyobraź sobie rozmowę z artystą, który mówi innym językiem. Model CLIP, wytrenowany na ogromnej liczbie par obraz–tekst, wypełnia tę lukę, zamieniając Twoje opisy na „instrukcje”, za którymi model AI potrafi podążać.

## Wejścia

| Parametr | Opis | Typ danych | Wymagany | Zakres |
| --- | --- | --- | --- | --- |
| `text` | Tekst do zakodowania. Obsługuje wiele linii i prompty dynamiczne. | STRING | Tak | Dowolny tekst |
| `clip` | Model CLIP używany do kodowania tekstu. | CLIP | Tak | Wczytane modele CLIP |

Uwaga: jeśli wejście `clip` jest puste (None) — np. gdy pochodzi z wczytywania checkpointu, który nie zawiera poprawnego modelu CLIP ani kodera tekstu — nod zgłosi błąd.

## Wyjścia

| Nazwa wyjścia | Opis | Typ danych |
| --- | --- | --- |
| `CONDITIONING` | Warunkowanie (conditioning) z zakodowanym tekstem, które kieruje modelem dyfuzyjnym. | CONDITIONING |

## Możliwości promptów

### Modele embedding

Modele embedding pozwalają nadać obrazowi określony efekt artystyczny lub styl. Obsługiwane formaty to `.safetensors`, `.pt` i `.bin`. Aby użyć modelu embedding:

1. Umieść plik w folderze `ComfyUI/models/embeddings`.
2. Odwołaj się do niego w tekście za pomocą `embedding:model_name`.

Przykład: jeśli w folderze `ComfyUI/models/embeddings` masz model `EasyNegative.pt`, możesz go użyć tak:

```
worst quality, embedding:EasyNegative, bad quality
```

**WAŻNE**: używając modeli embedding, sprawdź, czy nazwa pliku się zgadza i czy model pasuje do architektury Twojego modelu. Na przykład embedding stworzony dla SD1.5 nie zadziała poprawnie z modelem SDXL.

### Ustawianie wagi fragmentów promptu

Ważność wybranych części opisu możesz zmieniać nawiasami. Na przykład:

- `(beautiful:1.2)` zwiększa wagę słowa "beautiful".
- `(beautiful:0.8)` zmniejsza wagę słowa "beautiful".
- Same nawiasy `(beautiful)` nadają domyślną wagę 1.1.

Wagi szybko zmienisz skrótem `ctrl + up/down arrow`. Wielkość kroku zmiany wagi ustawisz w ustawieniach.

Jeśli chcesz mieć w prompcie zwykłe nawiasy bez zmiany wagi, poprzedź je ukośnikiem wstecznym, np. `\(word\)`.

### Prompty losowe (wildcard / dynamiczne)

Nawiasy `{}` tworzą prompty dynamiczne. Na przykład `{day|night|morning}` przy każdym przetworzeniu promptu losowo wybierze jedną z opcji.

Jeśli chcesz mieć w prompcie zwykłe nawiasy klamrowe bez losowania, poprzedź je ukośnikiem wstecznym, np. `\{word\}`.

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/en.md)

---
**Odcisk źródła (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
