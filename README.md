# 🧪 Chain-of-Thought Prompting for Chemistry Reasoning in VLMs

This project investigates how different Chain-of-Thought (CoT) prompting structures affect the reasoning abilities of state-of-the-art vision-language models (VLMs) on a suite of chemistry-focused image-based tasks.

---

## 📌 Project Objectives

We systematically evaluate:

- **Model performance across VLMs**, including **LLaVA-OneVision**, **LLaVA-Med (Microsoft)**, and **DeepSeek-VL**, using curated molecule diagrams as input.
- **Prompt structure effectiveness** by comparing three CoT formats—**Stepwise**, **Visual-first**, and **Explanation-first**—against a **baseline (no CoT)** format.
- **Task-specific performance** across five types of chemistry reasoning, from visual recognition to mechanistic inference.
- **Output accuracy and reasoning quality** using a human-rated rubric (0 = incorrect, 1 = partial, 2 = correct), allowing consistent scoring across prompts, tasks, and models.
- **Trends and failure modes**, identifying which CoT formats and models produce reliable scientific reasoning and which fall back on heuristics or hallucinations.

---

## 📦 Deliverables

- **✅ Prompt Set**  
  A curated collection of prompts (baseline and CoT) for five chemistry tasks.

- **✅ Inference Results**  
  Model outputs for each prompt-task-model combination, stored as structured `.csv` files.

- **✅ Graded Dataset**  
  Human-annotated scores (0–2) for all model outputs, including qualitative notes on reasoning.

- **✅ Data Analysis Report**  
  - Accuracy comparisons across models and prompt types  
  - Identification of effective prompt structures  
  - Observations on task complexity and model robustness

- **✅ Findings and Recommendations**  
  Summary discussion on:
  - How CoT prompting influences multimodal scientific reasoning
  - Common reasoning failures and speculation patterns
  - Implications for future prompt design in scientific domains

---

## ⚙️ Setup Overview

### 🔍 Models Evaluated
- `LLaVA-OneVision`  
- `LLaVA-Med` (v1.5 Mistral, biomedical)  
- `DeepSeek-VL` (multilingual vision-language model)

### 🧪 Tasks (for each model)
| Task ID | Task Description |
|---------|------------------|
| Task 0  | Molecule identification |
| Task 1  | EAS (Electrophilic Aromatic Substitution) reactivity |
| Task 2  | Acid/Base strength comparison |
| Task 3  | Nucleophilicity (functional group reactivity) |
| Task 4  | SN1 reaction likelihood |

### 💬 Prompt Structures
- `Baseline` (no CoT)
- `Stepwise`
- `Visual-first`
- `Explanation-first`

### 🧮 Scoring Rubric
| Score | Meaning |
|-------|---------|
| 0     | Incorrect or off-topic answer |
| 1     | Partially correct, incomplete or shallow reasoning |
| 2     | Fully correct with sound reasoning |

---

## 📁 Repository Structure

```
.
├──Analysis/      # store all result evaluations & analysis guideline doc
│   ├── Analysis_Design_Doc.md
│   ├── Task0_1V_EvalRes.md
│   ├── Task1_EvalRes.md
│   ├── Task2_EvalRes.md
│   ├── Task3_EvalRes.md
│   └── Task4_EvalRes.md
├── Dataset/      # stores all images in .png
│   ├── All
│   ├── Task0
│   ├── Task1
│   ├── Task2
│   ├── Task3
│   └── Task4
├── Results/      # stores all results in .csv/.txt/xlsx
│   ├── Task0
│   ├── Task1
│   ├── Task2
│   ├── Task3
│   └── Task4
├── Scripts/      # stores all .py code scripts for finetuning prompts and running tasks on models
│   ├── Task0
│   ├── Task1
│   ├── Task2
│   ├── Task3
│   └── Task4
├── Task_Definitions/    # what each task is about, images used, prompts selected
│   ├── 0_Identify.md
│   ├── 1_EAS.md
│   ├── 2_AcidBase.md
│   ├── 3_FunctionalGroups.md
│   ├── 4_SN1SN2.md
│   ├── meta.csv
│   └── pair_list.csv
├── Img/       # figures
│   ├── ...
├── .gitignore
└── README.md
```
