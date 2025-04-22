# Explain it!
---
# CoT-Caption: Studying Chain-of-Thought Structures in Vision-Language Models

## 📌 Project Overview

This project investigates how **Chain-of-Thought (CoT) reasoning** affects the performance and behavior of modern vision-language models (LLVMs) in image captioning tasks. Rather than training new models, this is a **comparative case study** analyzing how different CoT prompting strategies impact caption **accuracy**, **uncertainty calibration**, and **perceived trustworthiness**.

## 🎯 Research Objectives

We aim to answer three focused questions:

1. **Structure Effect**  
   Which CoT structure (e.g., stepwise, cause-effect, explanation-first) yields the most effective model performance?

2. **Uncertainty Calibration**  
   Does CoT help models express uncertainty in a more appropriate, calibrated way?

3. **Accuracy vs. Persuasiveness**  
   Does CoT improve factual correctness — or just make the model *sound* more confident and convincing?

---

## 🧪 Methodology Summary

- **50 test images** shared across all experiments  
- **3 CoT structures** (prompt templates) per image  
- **3 models**: BLIP-2, DeepSeek-VL, GPT-4V  
- Each [image × prompt] pair = one caption + CoT output  
- Total: **150 outputs/model × 3 models = 450 outputs**
- Evaluation via automated scoring + light human judgment

---

## ⚙️ Models Used

| Model | Type | Notes |
|-------|------|-------|
| `BLIP-2` (`Salesforce/blip2-flan-t5-xl`) | Open-source | Controlled captioning baseline |
| `DeepSeek-VL` | Open-source | Chat-style multimodal reasoning |
| `GPT-4V` | Proprietary | High-quality oracle for contrast |

---

## ⏳ Milestones

| # | Task | Description |
|--|------|-------------|
| 1 | Project Setup | Finalize objectives, scope, and evaluation criteria |
| 2 | Define Prompt Structures & Models | Write CoT prompts and choose inference models |
| 3 | Create Test Set | Curate 50 diverse image cases and define prompt mappings |
| 4 | Run Inference | Generate model outputs for all image × prompt pairs |
| 5 | Score Outputs | Compute CLIP Score, BERTScore, and uncertainty features |
| 6 | Analyze & Report | Summarize findings in final LaTeX report and repo |

---

## 🛠️ Evaluation Metrics

| Metric | Purpose |
|--------|---------|
| **CLIP Score** | Caption-image alignment |
| **BERTScore** | Caption-reference semantic overlap |
| **Uncertainty Expression Tags** | Track hedging (“likely”, “probably”) |
| **Human Preference (optional)** | A/B testing for trustworthiness and clarity |

---

# 🧠 Multimodal CoT Evaluation — Project Tracker

---

## ✅ Setup & Scope Definition

- ✅ Finalized research question & model list (GPT-4V, DeepSeek-VL, BLIP-2)
- ✅ Chose 3 CoT prompt formats (Stepwise, Visual-first, Contrastive)
- ✅ Defined evaluation framework (Accuracy, Reasoning, Confidence)
- ✅ Decided on 50 total images, reused for all formats
- ✅ Dropped Modular and Meta from experiment scope
- ✅ Finalized label system (2 = Good, 1 = Partial, 0 = Bad)
- ✅ Decided on manual dual annotation + Cohen’s Kappa

---

## 📅 This Week’s Goals

### 📅 April 22 (Tue)
- 📅 Start image picking (no pressure to finish)

### 📅 April 23 (Wed)
- 📅 Finalize 50 image selection
- 📅 Create 25 contrastive pairs from 50 images
- 📅 Write 50 Stepwise prompts
- 📅 Write 50 Visual-first prompts
- 📅 Write 25 Contrastive prompts
- 📅 Build `test_cases.csv` with all [image × prompt structure] entries

### 📅 April 24 (Thu)
- 📅 Deploy and test GPT-4V
- 📅 Deploy and test DeepSeek-VL
- 📅 Deploy and test BLIP-2
- 📅 Sync with Xinyu (first full project discussion)

### 📅 April 25 (Fri)
- 📅 Begin running prompts across all models
- 📅 Save outputs to `generated_outputs/`
- 📅 Begin logging progress into `progress_log.md`

---

## ⬜ Next Week & Beyond

### ⬜ Evaluation Phase
- ⬜ Create scoring templates (per rater)
- ⬜ Annotate all 375 outputs (2 raters)
- ⬜ Calculate Cohen’s Kappa per dimension
- ⬜ Merge and finalize final `eval_results.csv`

### ⬜ Analysis & Writeup
- ⬜ Aggregate accuracy + reasoning scores
- ⬜ Select strong/weak example outputs
- ⬜ Create bar/line/pie charts per structure & model
- ⬜ Draft results summary + discussion insights

### ⬜ Final Report Polish
- ⬜ Insert results into report
- ⬜ Write final conclusion
- ⬜ Add appendix: prompts, eval rubric, sample outputs

### ⬜ Presentation Prep
- ⬜ Create slide deck
- ⬜ Design per-structure summary visuals
- ⬜ Rehearse walkthrough with Xinyu

