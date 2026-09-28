# Krea 2 Identity LoRA — Fine-Tuning Case Study

This repository documents a rank-32 identity LoRA trained on
[Krea 2 Raw](https://huggingface.co/krea/Krea-2-Raw) with
[ai-toolkit](https://github.com/ostris/ai-toolkit). The goal was to improve
identity consistency across different compositions, clothing, lighting, and
photographic styles while preserving prompt control.

> **Disclosure:** Every image in this repository is AI-generated. The target
> identity is a real public figure. This is an unofficial, non-commercial
> portfolio case study and is not affiliated with or endorsed by the depicted
> person. Training images and model weights are intentionally not included.

## During-training evaluation samples

The following images are intermediate evaluation samples captured during
training. They document the model's progression before the completed-model
results shown in the next section.

The same fixed studio prompt shows how the learned identity developed over the
run:

| Baseline (step 0) | First run (step 2,500) | Resumed run (step 5,000) |
|---|---|---|
| ![Baseline training sample](assets/progression-step-0000.jpg) | ![Training sample at step 2500](assets/progression-step-2500.jpg) | ![Training sample at step 5000](assets/progression-step-5000.jpg) |

Additional evaluation generations captured during training:

| Window portrait | Full-body rooftop scene |
|---|---|
| ![During-training window portrait](assets/final-window-portrait.jpg) | ![During-training rooftop scene](assets/final-rooftop-full-body.jpg) |

| Expression change | Monochrome control |
|---|---|
| ![During-training laughing portrait](assets/final-laughing-portrait.jpg) | ![During-training black-and-white portrait](assets/final-monochrome-portrait.jpg) |

## After-training results

These are the primary results generated after the fine-tuning run was
completed. The first three images are shown with their supplied prompts. The
remaining seven are published without prompt text. A focused version of this
gallery is also available in [Post-Training Generation Samples](POST_TRAINING_SAMPLES.md).

### Prompt 1 — studio portrait

![After-training studio portrait](assets/post-training/captioned/prompt-01.png)

> `hania_01` sits on a wooden chair against a plain warm gray studio
> background, wearing a dark brown high-neck top, soft even studio lighting;
> framed from the waist up, centered.

### Prompt 2 — beverage campaign portrait

![After-training beverage campaign portrait](assets/post-training/captioned/prompt-02.png)

> `hania_01` in a professional Coca-Cola advertising campaign portrait,
> wearing an elegant modest red long-sleeve fashion dress with a high closed
> neckline, fully covered chest, tailored waist and sophisticated contemporary
> styling. She wears small polished gold earrings and a delicate gold necklace.
> Her dark hair is styled in polished soft waves.
>
> Medium close-up composition. `hania_01` holds a cold glass Coca-Cola bottle
> beside her face without covering any facial features. The bottle is covered
> with realistic cold condensation droplets, the red Coca-Cola label facing
> directly toward the camera and clearly readable.
>
> She gives a natural cheerful smile while looking directly into the lens. Her
> expression feels spontaneous, friendly and refreshing rather than overly
> posed.
>
> Bright clean commercial studio environment with a red gradient background,
> subtle sparkling highlights, soft rim light around her hair and shoulders,
> crisp product illumination on the bottle and soft flattering illumination
> across her face.
>
> Leave clean negative space above and beside her for advertising headline
> placement.
>
> High-budget beverage advertising photography, professional product campaign,
> realistic bottle proportions, realistic fingers around the bottle, detailed
> condensation, natural skin texture, crisp facial focus, premium commercial
> photography, photorealistic, vertical 2:3 advertising poster.

### Prompt 3 — cinematic portrait

![After-training cinematic portrait](assets/post-training/captioned/prompt-03.png)

> Close-up portrait of `hania_01` on a cinematic film set, wearing an elegant
> dark green dress, calm emotional expression, slightly parted lips, subtle
> intensity in her eyes, looking just past the camera, soft dramatic key light
> across her face, shallow depth of field, realistic cinematic actress portrait.

### Additional results without prompts

| Sample 1 | Sample 2 | Sample 3 | Sample 4 |
|---|---|---|---|
| ![Uncaptioned after-training sample 1](assets/post-training/uncaptioned/sample-01.png) | ![Uncaptioned after-training sample 2](assets/post-training/uncaptioned/sample-02.png) | ![Uncaptioned after-training sample 3](assets/post-training/uncaptioned/sample-03.png) | ![Uncaptioned after-training sample 4](assets/post-training/uncaptioned/sample-04.png) |

| Sample 5 | Sample 6 | Sample 7 |
|---|---|---|
| ![Uncaptioned after-training sample 5](assets/post-training/uncaptioned/sample-05.png) | ![Uncaptioned after-training sample 6](assets/post-training/uncaptioned/sample-06.png) | ![Uncaptioned after-training sample 7](assets/post-training/uncaptioned/sample-07.png) |

### Coordinated-shoot contact sheets

| Shoot 1 — green dress | Shoot 2 — blue dress |
|---|---|
| ![Green-dress shoot contact sheet](assets/post-training/collages/shoot-01-collage.jpg) | ![Blue-dress shoot contact sheet](assets/post-training/collages/shoot-02-collage.jpg) |

### Advertising / commercial results

These post-training outputs explore beverage, fragrance, jewellery, and
lifestyle campaign compositions. No prompt text is published for these images.
They are unofficial AI-generated concepts and are not commissioned, sponsored,
or endorsed by any brand shown or referenced.

| Campaign concept 1 | Campaign concept 2 | Campaign concept 3 | Campaign concept 4 |
|---|---|---|---|
| ![Advertising result 1](assets/post-training/advertising/ad-01.png) | ![Advertising result 2](assets/post-training/advertising/ad-02.png) | ![Advertising result 3](assets/post-training/advertising/ad-03.png) | ![Advertising result 4](assets/post-training/advertising/ad-04.png) |

| Campaign concept 5 | Campaign concept 6 | Campaign concept 7 |
|---|---|---|
| ![Advertising result 5](assets/post-training/advertising/ad-05.png) | ![Advertising result 6](assets/post-training/advertising/ad-06.png) | ![Advertising result 7](assets/post-training/advertising/ad-07.png) |

## Training setup

| Item | Value |
|---|---|
| Base model | Krea 2 Raw |
| Training method | LoRA |
| LoRA rank / alpha | 32 / 32 |
| Dataset | 60 captioned images |
| Image preparation | Native aspect ratio preserved; approximately 1024² pixel budget |
| Buckets | 4 aspect-ratio buckets |
| Training steps | 5,000 total: 2,500 + resumed run to 5,000 |
| Batch size | 1 |
| Optimizer | AdamW 8-bit |
| Learning rate | `1e-4` |
| Training precision | BF16 |
| Saved precision | FP16 |
| Scheduler | Flow matching, linear timestep sampling |
| Caption dropout | 5% |
| EMA | Disabled |
| Evaluation | Six fixed prompts every 250 steps |
| Final LoRA size | 218 MiB |

The complete, sanitized configuration is in
[`config/train_lora_krea2_identity.example.yaml`](config/train_lora_krea2_identity.example.yaml).

## Method

1. Curated 60 varied portrait and editorial images, including nine monochrome
   examples.
2. Resized each image to a consistent pixel budget without cropping. Preserving
   aspect ratio kept full-body framing intact and allowed ai-toolkit to bucket
   the images.
3. Used natural-language captions beginning with a unique trigger token.
   Controllable properties were described explicitly; the monochrome images,
   for example, included a black-and-white sentence.
4. Trained for 2,500 steps, evaluated fixed prompts, then resumed the same job
   from its saved metadata and optimizer state to 5,000 steps.
5. Compared samples across checkpoints using the same seed and prompt suite.

## Findings

- The 2,500-step checkpoint was under-trained for a 60-image dataset. Extending
  to 5,000 steps substantially improved consistency across prompts.
- Improvement from step 4,000 to 5,000 was smaller than the earlier gain,
  suggesting that further progress would require better data rather than only
  more steps.
- Explicitly captioning monochrome examples kept black-and-white rendering
  promptable instead of binding it to the identity token.
- Preserving aspect ratio prevented destructive crops in full-body images.
- Hairstyle was not consistently captioned in this run, so it became partly
  entangled with the trigger token and is less controllable than clothing,
  setting, or color treatment.

## Reproducing the pipeline

Only train on images you own or are authorized to use.

1. Install ai-toolkit using its upstream instructions.
2. Prepare a captioned dataset. The reusable no-crop resizing utility is in
   [`scripts/prepare_dataset.py`](scripts/prepare_dataset.py).
3. Copy the example YAML into ai-toolkit's `config/` directory.
4. Update the dataset and text-encoder paths in the YAML.
5. Run from the ai-toolkit repository:

   ```bash
   python run.py config/train_lora_krea2_identity.example.yaml
   ```

The base model is not included and may require significant storage and GPU
memory. Hardware requirements depend on the current ai-toolkit and model setup.

## Repository contents

```text
.
├── assets/          # Selected AI-generated evaluation samples
├── config/          # Sanitized ai-toolkit training configuration
├── scripts/         # Reusable dataset preparation utility
├── POST_TRAINING_SAMPLES.md # Prompted and uncaptioned output gallery
├── MODEL_CARD.md    # Scope, limitations, and responsible-use notes
└── README.md
```

## What is intentionally excluded

- Raw training images and captions
- Source videos and downloaded archives
- Checkpoints, optimizer state, and base-model files
- Full logs containing local filesystem paths
- Secrets, credentials, and machine/network information

See [MODEL_CARD.md](MODEL_CARD.md) before considering any weight release or
deployment involving a real person's likeness.
