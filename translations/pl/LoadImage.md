# Load Image

Nod LoadImage wczytuje i wstępnie przygotowuje obrazy ze wskazanej ścieżki. Obsługuje formaty z wieloma klatkami, wykonuje potrzebne przekształcenia, np. obrót na podstawie danych EXIF, normalizuje wartości pikseli i — jeśli obraz ma kanał alfa — tworzy maskę. To podstawowy nod do przygotowania obrazów do dalszej obróbki lub analizy w workflow.

## Wejścia

| Parametr | Opis | Typ danych |
| --- | --- | --- |
| `image` | Parametr 'image' wskazuje obraz do wczytania i przetworzenia. Na jego podstawie ustalana jest ścieżka do pliku, a następnie obraz jest wczytywany, przekształcany i normalizowany. | COMBO[STRING] |

## Wyjścia

| Parametr | Opis | Typ danych |
| --- | --- | --- |
| `image` | Przetworzony obraz z znormalizowanymi wartościami pikseli i zastosowanymi przekształceniami. Gotowy do dalszej obróbki lub analizy. | `IMAGE` |
| `mask` | Opcjonalne wyjście z maską obrazu — przydatne, gdy obraz ma kanał alfa (przezroczystość). | `MASK` |

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/en.md)
