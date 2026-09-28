# Post-Training Generation Samples

These images were generated after fine-tuning and are included as qualitative
examples of identity consistency, prompt response, styling, pose variation, and
expression control. They are evaluation outputs, not training images.

The first three samples retain their supplied prompts. The remaining seven are
shown without reconstructed or inferred prompts because no accompanying prompt
text was supplied for them. Embedded generation workflow metadata has been
removed from every published image.

## Captioned samples

### Prompt 1 — warm gray studio portrait

> `hania_01` sits on a wooden chair against a plain warm gray studio
> background, wearing a dark brown high-neck top, soft even studio lighting;
> framed from the waist up, centered.

![Warm gray studio portrait](assets/post-training/captioned/prompt-01.png)

### Prompt 2 — beverage campaign portrait

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

![Beverage campaign portrait](assets/post-training/captioned/prompt-02.png)

### Prompt 3 — cinematic film-set portrait

> Close-up portrait of `hania_01` on a cinematic film set, wearing an elegant
> dark green dress, calm emotional expression, slightly parted lips, subtle
> intensity in her eyes, looking just past the camera, soft dramatic key light
> across her face, shallow depth of field, realistic cinematic actress portrait.

![Cinematic film-set portrait](assets/post-training/captioned/prompt-03.png)

## Additional uncaptioned samples

No prompt text is published for these outputs.

| Sample 1 | Sample 2 |
|---|---|
| ![Uncaptioned sample 1](assets/post-training/uncaptioned/sample-01.png) | ![Uncaptioned sample 2](assets/post-training/uncaptioned/sample-02.png) |

| Sample 3 | Sample 4 |
|---|---|
| ![Uncaptioned sample 3](assets/post-training/uncaptioned/sample-03.png) | ![Uncaptioned sample 4](assets/post-training/uncaptioned/sample-04.png) |

| Sample 5 | Sample 6 |
|---|---|
| ![Uncaptioned sample 5](assets/post-training/uncaptioned/sample-05.png) | ![Uncaptioned sample 6](assets/post-training/uncaptioned/sample-06.png) |

| Sample 7 |
|---|
| ![Uncaptioned sample 7](assets/post-training/uncaptioned/sample-07.png) |

## Coordinated-shoot contact sheets

These contact sheets preserve each source image's complete composition without
cropping. They provide a compact view of consistency across pose and framing.

### Shoot 1 — green dress, 15 outputs

![Shoot 1 contact sheet](assets/post-training/collages/shoot-01-collage.jpg)

### Shoot 2 — blue dress, 12 outputs

![Shoot 2 contact sheet](assets/post-training/collages/shoot-02-collage.jpg)

## Reading the examples

These are qualitative demonstrations rather than a benchmark. They are useful
for checking whether the learned identity remains recognizable across wardrobe,
lighting, composition, expression, and full-body versus close-up framing. A
stronger evaluation would add fixed seeds, multiple generations per prompt, and
side-by-side comparisons against the base model and earlier checkpoints.
