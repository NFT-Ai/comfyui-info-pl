# Blur Image

Nod `ImageBlur` nakłada na obraz rozmycie Gaussa — zmiękcza krawędzie oraz zmniejsza szczegóły i szum. Parametrami ustawiasz siłę i zasięg rozmycia.

## Wejścia

| Pole | Opis | Typ danych |
| --- | --- | --- |
| `image` | Obraz wejściowy do rozmycia. To główny cel efektu. | `IMAGE` |
| `blur_radius` | Promień rozmycia. Większy promień daje mocniejsze rozmycie. | `INT` |
| `sigma` | Zasięg rozmycia. Wyższa wartość sigma oznacza, że rozmycie obejmuje większy obszar wokół każdego piksela. | `FLOAT` |

## Wyjścia

| Pole | Opis | Typ danych |
| --- | --- | --- |
| `image` | Rozmyta wersja obrazu wejściowego; siłę rozmycia wyznaczają parametry wejściowe. | `IMAGE` |

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/en.md)
