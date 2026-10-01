# Empty Latent Image

Nod `EmptyLatentImage` tworzy pustą reprezentację w przestrzeni latentnej o podanych wymiarach i wielkości paczki. To punkt wyjścia do generowania lub przerabiania obrazów w przestrzeni latentnej.

## Wejścia

| Parametr | Opis | Typ danych |
| --- | --- | --- |
| `width` | Szerokość tworzonego obrazu latentnego. Bezpośrednio wyznacza wymiary wynikowej reprezentacji latentnej. | `INT` |
| `height` | Wysokość tworzonego obrazu latentnego. Razem z szerokością określa wymiary przestrzeni latentnej. | `INT` |
| `batch_size` | Liczba obrazów latentnych tworzonych w jednej paczce. Pozwala generować kilka obrazów naraz. | `INT` |

## Wyjścia

| Parametr | Opis | Typ danych |
| --- | --- | --- |
| `latent` | Tensor z paczką pustych obrazów latentnych — baza do dalszego generowania lub przerabiania obrazu w przestrzeni latentnej. | `LATENT` |

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/en.md)
