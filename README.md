# 📄 Project Objectives

The goal of this project is to systematically evaluate the impact of Chain-of-Thought (CoT) prompting structures on the performance of state-of-the-art vision-language models in chemistry-focused reasoning tasks. Specifically, we aim to:

- **Compare model performance** across three modern multimodal models — **LLaVA-OneVision**, **Microsoft LLaVA-Med**, and **DeepSeek-VL** — on a curated set of molecule-related image tasks.
- **Assess the effectiveness of CoT prompting** by testing three distinct CoT structures alongside a baseline (no CoT) for each task.
- **Analyze task difficulty and model robustness** by covering five types of chemistry reasoning tasks, ranging from simple molecule identification to complex mechanistic predictions.
- **Quantitatively evaluate outputs** using a standardized scoring rubric (0 = incorrect, 1 = partially correct, 2 = correct), enabling consistent cross-model and cross-task comparisons.
- **Identify trends** in how different models and prompting strategies affect reasoning quality, factual accuracy, and error patterns in chemistry-specific contexts.

# 📄 Expected Deliverables

By the end of the project, we expect to deliver:

- **Prompt Set:**  
  A refined set of baseline and CoT prompts tailored for five molecule-related reasoning tasks.

- **Inference Results:**  
  Model outputs for every combination of model, task, and prompting style, organized systematically.

- **Graded Dataset:**  
  Human-annotated scores (0/1/2) for all outputs, indicating the correctness of each model's reasoning.

- **Data Analysis Report:**  
  - Statistical summaries of model accuracy across different tasks and prompt structures.
  - Comparative analysis identifying which CoT structures (if any) significantly improve model performance.
  - Observations on task difficulty trends and model-specific strengths and weaknesses.

- **Discussion of Findings:**  
  A high-level interpretation of the results, including insights into:
  - The role of CoT prompting in multimodal scientific reasoning.
  - Model-specific behaviors and failure modes.
  - Recommendations for future prompt engineering in chemical and scientific domains.

# ✅ Summary of Setup

## Models:
- LLaVA-OneVision
- Microsoft LLaVA-Med
- DeepSeek-VL

## Tasks (per model):
- **Task 0:** Identify molecule (baseline)
- **Task 1:** EAS (Electrophilic Aromatic Substitution prediction)
- **Task 2:** Acid/Base analysis
- **Task 3:** Functional group identification
- **Task 4:** SN1/SN2 mechanism prediction

## Prompt types:
- Baseline (no CoT)
- 3 CoT styles (Stepwise, Visual-first, Explanation-first)

## Scoring rubric:
- 0 = Wrong
- 1 = Partially correct
- 2 = Fully correct
