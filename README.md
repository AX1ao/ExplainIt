# 🧠 CoT-Caption: Studying Chain-of-Thought Structures in Vision-Language Models

---

## 📌 Project Overview

This project investigates how **Chain-of-Thought (CoT) prompting structures** affect the reasoning behavior of vision-language models (VLMs) in image captioning tasks.  
Rather than modifying models or datasets, we perform a **comparative case study** using prompt-only methods to test how different CoT styles influence:

- Caption **accuracy**
- Expression of **uncertainty**
- Perceived **persuasiveness or trustworthiness**

---

## 🎯 Research Objectives

We aim to answer three focused questions:

1. **Structure Effect**  
   Which CoT structure (e.g., stepwise, visual-first, contrastive) yields the most effective model performance?

2. **Uncertainty Calibration**  
   Does CoT help models express uncertainty in a more appropriate, calibrated way?

3. **Accuracy vs. Persuasiveness**  
   Does CoT improve factual correctness — or just make the model *sound* more confident and convincing?

---

## 🧪 Methodology Summary

- **50 total images**, reused across all prompt formats
- **4 prompt structures** per image:
  - Stepwise (explicit “Let’s think step by step”)
  - Visual-first (starts with scene observation)
  - Contrastive (image pairs)
  - Baseline (no CoT guidance)
- **3 models**:
  - `GPT-4V`
  - `DeepSeek-VL`
  - `BLIP-2`
- **175 prompts total × 3 models = 525 outputs**
- Prompting is performed in **stateless, one-shot sessions**
- Outputs are evaluated using **manual dual annotation**

---

## ⚙️ Models Used

| Model | Type | Notes |
|-------|------|-------|
| `BLIP-2` (`Salesforce/blip2-flan-t5-xl`) | Open-source | Controlled baseline model |
| `DeepSeek-VL` | Open-source | Chat-style VLM |
| `GPT-4V` | Proprietary | Oracle-quality multimodal reasoning |

---

## 🛠️ Evaluation Metrics

| Metric | Description |
|--------|-------------|
| ✅ **Accuracy** (0–2) | Final answer correctness |
| ✅ **Reasoning Quality** (0–2) | Step coherence, justification |
| ✅ **Confidence Expression** (0–2) | Explicit uncertainty vs overconfidence |
| ✅ **Persuasiveness** (0–2) | How convincing the output sounds, regardless of correctness |
| ✅ **Cohen’s Kappa** | Inter-rater agreement for all scores |
| 🟡 *(Optional)* CLIPScore, BERTScore | Caption similarity metrics (TBD) |

All evaluations are logged in a shared scoring sheet with matching image IDs and prompt types.

---

## 🧪 Annotation Procedure

- Two annotators independently label each model output
- Labels are:
  - Accuracy: `Incorrect (0)`, `Partial (1)`, `Correct (2)`
  - Reasoning Quality: `Hallucinated`, `Incomplete`, `Clear & Justified`
  - Confidence: `Explicitly Uncertain`, `Hedged`, `Confident`
  - Persuasiveness: `Unconvincing`, `Somewhat convincing`, `Very persuasive`
- Final scores are merged and agreement is measured using **Cohen’s Kappa**

---

## ⏳ Milestones

| # | Task | Description |
|--|------|-------------|
| 1 | Project Setup | Define objectives and evaluation plan |
| 2 | Prompt Structure Design | Write 4 prompt types (incl. baseline) |
| 3 | Image Set Creation | Curate 50 diverse images and pairings |
| 4 | Model Execution | Run all models across 175 prompts |
| 5 | Manual Annotation | Score 525 outputs across 4 dimensions |
| 6 | Analysis & Reporting | Aggregate findings, finalize report |

---

# 🚦 Multimodal CoT Evaluation — Project Tracker

## ✅ Setup & Scope

- ✅ Finalized research question and model list
- ✅ Selected 3 CoT structures + 1 baseline
- ✅ Evaluation framework: accuracy, reasoning, confidence, persuasiveness
- ✅ Dual annotation setup + Cohen’s Kappa
- ✅ All known biases (randomness, meta exposure) acknowledged

---

## 📅 This Week’s Plan

| Date | Task |
|------|------|
| Apr 22 | Start image picking (no pressure to finish) |
| Apr 23 | Finalize 50 images and 25 contrastive pairs; Write 150 CoT prompts |
| Apr 24 | Deploy + test all 3 models; sync with Xinyu |
| Apr 25 | Start running all prompts across models and logging outputs |

---

## 🔜 Next Week & Beyond

### ⬜ Evaluation
- ⬜ Create scoring templates for both annotators
- ⬜ Annotate all 525 outputs (manual)
- ⬜ Calculate Cohen’s Kappa for each score type

### ⬜ Analysis
- ⬜ Compute accuracy vs confidence patterns
- ⬜ Analyze persuasiveness vs correctness
- ⬜ Extract standout examples + trends
- ⬜ Create visualizations (bar/pie/line charts)

### ⬜ Report & Presentation
- ⬜ Finalize LaTeX report
- ⬜ Add appendix: image list, rubric, prompt examples
- ⬜ Build slide deck for final presentation
