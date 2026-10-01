# VAE Decode

Nod VAEDecode dekoduje reprezentacje latentne z powrotem na obrazy za pomocą wskazanego modelu VAE (Variational Autoencoder). Służy do tworzenia obrazów ze skompresowanych danych, czyli odtwarzania obrazu z jego zapisu w przestrzeni latentnej.

## Wejścia

| Parametr | Opis | Typ danych |
| --- | --- | --- |
| `samples` | Parametr 'samples' to reprezentacje latentne do zdekodowania na obrazy. Dostarcza skompresowane dane, z których odtwarzany jest obraz. | `LATENT` |
| `vae` | Parametr 'vae' wskazuje model VAE, którym latenty zostaną zdekodowane na obrazy. Decyduje o sposobie dekodowania i jakości odtworzonych obrazów. | VAE |

## Wyjścia

| Parametr | Opis | Typ danych |
| --- | --- | --- |
| `image` | Obraz odtworzony z podanej reprezentacji latentnej przy użyciu wskazanego modelu VAE. | `IMAGE` |

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/en.md)
