# KSampler

KSampler działa tak: przerabia podany wejściowy obraz latentny na podstawie wybranego modelu oraz warunków pozytywnych i negatywnych.
Najpierw dodaje szum do danych obrazu zgodnie z ustawionym **seed** i **denoise strength**, a następnie wprowadza ustawiony **Model** razem z warunkami **positive** i **negative**, aby wygenerować obraz.

## Wejścia

| Nazwa parametru | Opis | Typ danych | Wymagany | Domyślnie | Zakres/opcje |
| --- | --- | --- | --- | --- | --- |
| Model | Model wejściowy używany do odszumiania | checkpoint | Tak | Brak | - |
| seed | Służy do wygenerowania losowego szumu; ten sam "seed" daje identyczne obrazy | Int | Tak | 0 | 0 ~ 18446744073709551615 |
| steps | Liczba kroków odszumiania; więcej kroków to dokładniejszy wynik | Int | Tak | 20 | 1 ~ 10000 |
| cfg | Określa, jak ściśle obraz trzyma się warunków wejściowych; zalecane 6–8 | float | Tak | 8.0 | 0.0 ~ 100.0 |
| sampler_name | Wybór samplera do odszumiania; wpływa na szybkość i styl generowania | Opcja UI | Tak | Brak | Wiele algorytmów |
| scheduler | Określa, jak usuwany jest szum; wpływa na przebieg generowania | Opcja UI | Tak | Brak | Wiele schedulerów |
| Positive | Warunki pozytywne kierujące odszumianiem — to, co ma się pojawić na obrazie | conditioning | Tak | Brak | - |
| Negative | Warunki negatywne kierujące odszumianiem — to, czego nie chcesz na obrazie | conditioning | Tak | Brak | - |
| Latent_Image | Obraz latentny, który będzie odszumiany | Latent | Tak | Brak | - |
| denoise | Określa, ile szumu zostanie usunięte; niższe wartości oznaczają mniejszą zmianę obrazu wejściowego | float | Nie | 1.0 | 0.0 ~ 1.0 |
| control_after_generate | Pozwala zmieniać seed po każdym uruchomieniu | Opcja UI | Nie | Brak | Random/Inc/Dec/Keep |

## Wyjście

| Parametr | Funkcja |
| -------------- | ------------------------------------------ |
| Latent         | Zwraca latent po odszumieniu przez sampler |

## Kod źródłowy

[Zaktualizowano 15 maja 2025]

```Python

def common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=1.0, disable_noise=False, start_step=None, last_step=None, force_full_denoise=False):
    latent_image = latent["samples"]
    latent_image = comfy.sample.fix_empty_latent_channels(model, latent_image)

    if disable_noise:
        noise = torch.zeros(latent_image.size(), dtype=latent_image.dtype, layout=latent_image.layout, device="cpu")
    else:
        batch_inds = latent["batch_index"] if "batch_index" in latent else None
        noise = comfy.sample.prepare_noise(latent_image, seed, batch_inds)

    noise_mask = None
    if "noise_mask" in latent:
        noise_mask = latent["noise_mask"]

    callback = latent_preview.prepare_callback(model, steps)
    disable_pbar = not comfy.utils.PROGRESS_BAR_ENABLED
    samples = comfy.sample.sample(model, noise, steps, cfg, sampler_name, scheduler, positive, negative, latent_image,
                                  denoise=denoise, disable_noise=disable_noise, start_step=start_step, last_step=last_step,
                                  force_full_denoise=force_full_denoise, noise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)
    out = latent.copy()
    out["samples"] = samples
    return (out, )
class KSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", {"tooltip": "The model used for denoising the input latent."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "The random seed used for creating the noise."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "The number of steps used in the denoising process."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "The algorithm used when sampling, this can affect the quality, speed, and style of the generated output."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "The scheduler controls how noise is gradually removed to form the image."}),
                "positive": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to include in the image."}),
                "negative": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to exclude from the image."}),
                "latent_image": ("LATENT", {"tooltip": "The latent image to denoise."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "The amount of denoising applied, lower values will maintain the structure of the initial image allowing for image to image sampling."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("The denoised latent.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "Uses the provided model, positive and negative conditioning to denoise the latent image."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```

> Ta dokumentacja została wygenerowana przez AI. Jeśli znajdziesz błędy lub masz sugestie, zachęcamy do współtworzenia! [Edytuj na GitHubie](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/en.md)
