# 🧠 Prompting for Chemical Reasoning: A Comparative Study of Chain-of-Thought Structures in Vision-Language Models

---

## 🌟 Overview

This project investigates how **different Chain-of-Thought (CoT) prompt structures** influence reasoning behavior in **vision-language models** when applied to structured scientific images. We focus on a chemically grounded question:

> **“Which compound is more reactive, and why?”**

By comparing models like **GPT-4V** and **BLIP-2**, we aim to understand how CoT structures impact accuracy, reasoning clarity, and cross-model generality in tasks that require multimodal understanding and logical inference.

---

## 🎯 Research Questions

1. **Model-Specific Effectiveness**  
   Which CoT prompt structures improve reasoning and accuracy for each model?

2. **Cross-Model Generality**  
   Are there CoT formats that generalize well across different architectures?

3. **Task-Specific Optimization**  
   Can we identify a single “best” CoT prompt for chemical reactivity reasoning?

---

## 🔍 Task Design

- **Input**: Side-by-side visual representations of molecular structures (e.g., SMILES-based 2D diagrams)
- **Output**: Natural language answer to:  
  > *“Which compound is more reactive? Explain your reasoning.”*

- **Data**: 50 curated image pairs with known reactivity differences (based on functional groups, resonance, etc.)
- **Ground Truth**: Expert-labeled chemical rationale (non-ambiguous)

---

## 🧱 Chain-of-Thought Structures Evaluated

We define and test the following CoT prompt families:

| Structure Type       | Prompt Style Description                                 |
|----------------------|----------------------------------------------------------|
| **Stepwise**         | “Let’s think step by step...”                            |
| **Visual-first**     | “Looking at the molecular structure, we observe...”      |
| **Explanation-first**| “Compound A is more reactive. This is because…”          |
| **Contrastive**      | “Compared to B, compound A has features that…”           |
| **Baseline (no CoT)**| Direct answer with no reasoning guidance                 |

---

## 🧪 Models Tested

- **GPT-4V** (OpenAI)
- **BLIP-2** (Salesforce)
- *(Optional: DeepSeek-VL)*

Each model is evaluated with every CoT prompt across all 50 image pairs.

---

## 📈 Evaluation Metrics

- **Answer Accuracy** (vs. ground truth)
- **Reasoning Quality** (logic, fluency — scored manually or via GPT-judge)
- **Cross-Model Consistency**
- **Failure Modes and Error Categories**

---

## 📊 Expected Deliverables

- 📘 **Per-Model CoT Performance Table**
- 🔄 **Cross-Model Comparison Matrix**
- 🧪 **Recommended Prompt for This Task**
- 💬 **Annotated Justification Examples**
- 🔍 **Failure Analysis Summary**
- 🧠 **Prompting Insights for Future Research**

---

## 💬 Sample Prompt Format (Visual-first)

```text
Question: Which compound is more reactive, and why?

Visual-first Prompt:
Looking at the molecular structure, we observe that Compound A contains a carboxylic acid group while Compound B has an alcohol group. Carboxylic acids are more reactive due to resonance stabilization of their conjugate base. Therefore, Compound A is more reactive.
```
