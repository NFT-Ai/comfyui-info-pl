# VAE Encode

Ten nod koduje obrazy do reprezentacji w przestrzeni latentnej za pomocą wskazanego modelu VAE. Ukrywa złożoność procesu kodowania i daje prosty sposób na zamianę obrazów w ich reprezentacje latentne.

## Wejścia

| Parametr | Opis | Typ danych |
| --- | --- | --- |
| `pixels` | Parametr 'pixels' to dane obrazu, które mają zostać zakodowane do przestrzeni latentnej. Jest bezpośrednim wejściem procesu kodowania, więc decyduje o wynikowej reprezentacji latentnej. | `IMAGE` |
| `vae` | Parametr 'vae' wskazuje model VAE (Variational Autoencoder), którym obraz zostanie zakodowany do przestrzeni latentnej. Określa mechanizm kodowania i cechy powstałej reprezentacji latentnej. | VAE |

## Wyjścia

| Parametr | Opis | Typ danych |
| --- | --- | --- |
| `latent` | Wynikiem jest reprezentacja obrazu wejściowego w przestrzeni latentnej — jego najważniejsze cechy w skompresowanej postaci. | `LATENT` |

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/en.md)
