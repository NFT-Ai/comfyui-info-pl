# Load Checkpoint

Wczytuje plik checkpointu modelu dyfuzyjnego i dzieli go na trzy główne części: główny model służący do odszumiania latentów, koder tekstu CLIP oraz koder/dekoder obrazu VAE. Nod automatycznie wykrywa wszystkie pliki modeli w folderze `ComfyUI/models/checkpoints` oraz w dodatkowych ścieżkach skonfigurowanych w pliku `extra_model_paths.yaml`.

## Wejścia

| Parametr | Opis | Typ danych | Wymagany | Zakres |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Nazwa checkpointu (modelu) do wczytania. Wybierz nazwę pliku modelu — decyduje ona o tym, jaki model AI zostanie użyty do dalszego generowania obrazów. | COMBO | Tak | Wszystkie pliki modeli znalezione w folderze checkpoints |

**Uwaga:** jeśli dodasz nowe pliki modeli, gdy ComfyUI jest uruchomiony, odśwież przeglądarkę (Ctrl+R), aby zobaczyć je na liście rozwijanej.

## Wyjścia

| Nazwa wyjścia | Opis | Typ danych |
| --- | --- | --- |
| `MODEL` | Model używany do odszumiania latentów. To główny model dyfuzyjny, który generuje obraz. | MODEL |
| `CLIP` | Model CLIP używany do kodowania promptów — zamienia opis tekstowy na informacje zrozumiałe dla AI. | CLIP |
| `VAE` | Model VAE używany do kodowania i dekodowania obrazów do i z przestrzeni latentnej. | VAE |

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/en.md)

---
**Odcisk źródła (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
