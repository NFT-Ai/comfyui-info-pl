# Save Image

Nod SaveImage zapisuje obrazy wejściowe jako pliki PNG w folderze wyjściowym ComfyUI. Może osadzać w każdym zapisanym pliku metadane workflow, np. prompt, i zwraca obrazy bez zmian, więc nadal można ich używać w kolejnych nodach.

## Wejścia

| Parametr | Opis | Typ danych | Wymagany | Zakres |
| --- | --- | --- | --- | --- |
| `images` | Obrazy do zapisania. | IMAGE | Tak | - |
| `filename_prefix` | Przedrostek nazwy zapisywanego pliku. Może zawierać znaczniki formatowania, np. `%date:yyyy-MM-dd%` albo `%Empty Latent Image.width%`, aby wstawić wartości z nodów (domyślnie: "ComfyUI"). | STRING | Tak | - |

Nod dostaje też dwa ukryte wejścia, `prompt` i `extra_pnginfo`, które ComfyUI wypełnia automatycznie promptem workflow i dodatkowymi informacjami PNG. Gdy metadane są włączone, te informacje zapisują się jako tekstowe metadane w każdym pliku PNG.

Nazwa każdego zapisanego obrazu składa się z `filename_prefix`, opcjonalnego znacznika `%batch_num%` (zastępowanego pozycją obrazu w paczce) i pięciocyfrowego licznika, np. `ComfyUI_00001_.png`. Obrazy są zapisywane z kompresją PNG na poziomie 4.

## Wyjścia

| Nazwa wyjścia | Opis | Typ danych |
| --- | --- | --- |
| `images` | Oryginalne obrazy wejściowe, zwrócone bez zmian po zapisaniu na dysk. | IMAGE |
| `ui` | Wynik tylko dla interfejsu: lista zapisanych plików (nazwa, podfolder i typ) do pokazania w przeglądarce. | UI_RESULT |

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/en.md)

---
**Odcisk źródła (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
