# Model Card: Krea 2 Identity LoRA Case Study

## Status

This repository is a portfolio case study. It does not distribute the trained
weights or the source dataset.

## Model description

- **Type:** Low-Rank Adaptation (LoRA)
- **Base model:** Krea 2 Raw
- **Trainer:** ai-toolkit
- **Trigger used during the experiment:** `hania_01`
- **Training set:** 60 captioned still images of one real public figure
- **Training length:** 5,000 steps, completed in two resumable stages
- **LoRA rank / alpha:** 32 / 32

The experiment studied identity consistency and prompt editability across
portrait, upper-body, and full-body compositions.

## Intended use

- Documenting an image-model fine-tuning workflow
- Studying LoRA training, captions, aspect-ratio buckets, and checkpoint
  progression
- Reproducing the technique with an original, licensed, or consented dataset

## Out-of-scope use

Do not use this work to deceive viewers, impersonate the depicted person,
suggest endorsement, harass or defame anyone, create sexualized material, or
evade platform disclosure rules. Do not present generated images as authentic
photographs.

## Training data

The private experiment used 60 varied portrait/editorial images. Native aspect
ratios were retained and each image was resized to approximately the same pixel
budget. Nine monochrome examples were labeled explicitly in their captions.

The source media is not included because its redistribution rights have not
been established. Before publishing any weights or dataset, independently
verify image copyright, consent, privacy/publicity rights, the base-model
license, and the trainer's license.

## Evaluation

Evaluation was qualitative. Six fixed prompts were generated every 250 steps
with the same initial seed and sampling parameters. Review focused on:

- Identity consistency between prompt categories
- Retention of clothing, setting, expression, and composition control
- Color versus monochrome controllability
- Changes between the 2,500-step and 5,000-step checkpoints

No face-recognition benchmark, blinded human study, or demographic fairness
evaluation was performed. The sample gallery therefore demonstrates behavior
but should not be treated as a quantitative model comparison.

## Observed limitations

- Hairstyle was omitted from most captions, reducing hairstyle editability.
- The generated face remained somewhat fuller/rounder than the target in the
  final qualitative review.
- The small, high-variance dataset mixes lighting, grading, distance, and
  editorial styles, which competes with identity learning at rank 32.
- Results may vary with software versions, hardware, prompts, and seeds.
- A real-person likeness model creates elevated risks of confusion, unwanted
  representation, and misuse even when individual outputs look benign.

## Disclosure

All gallery images in this repository are synthetic outputs. The project is
unofficial and is not affiliated with or endorsed by the depicted person.
