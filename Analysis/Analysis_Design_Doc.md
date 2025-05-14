# 🧪 LLaVA Prompt Evaluation – Analysis Design Doc

This document outlines the two types of analyses to be conducted:

- **Part I – Rigorous, Benchmark-Supported Analyses**  
  Backed by structured data across models, prompts, and tasks.

- **Part II – Exploratory & Observational Analyses**  
  Emerging patterns worth discussing or investigating further, but not all are backed by full benchmarks.

---

## ✅ Part I. Rigorous, Benchmark-Based Analyses

### 1. Patterns in the "Best" Prompts
**Goal:** Identify if there are structural consistencies among top-performing prompts.  
**Instructions:**
- For each task, list the best-performing prompt per model.
- Group and compare best prompts by type (Stepwise, Explanation-first, etc.).
- Analyze:
  - Which types appear most frequently?
  - Any shared structural features (e.g., numbered steps, logical transitions)?
- Output: A table + short thematic summary of prompt patterns.

---

### 2. Prompt Generality Across Models
**Goal:** Check whether top prompts for OneVision also perform well on other models.  
**Instructions:**
- Take all OneVision-best prompts (one per task).
- Reuse these prompts on the same tasks for LLaVA-Med and GPT-4o.
- Compare score deltas across models for each prompt.
- Output: Table or heatmap showing prompt transferability across models.

---

### 3. Which CoT Style Works Best (Model-wise and Overall)
**Goal:** Compare Stepwise, Explanation-first, and Visual-first CoT strategies.  
**Instructions:**
- For each model, average scores for prompts within each CoT family.
- Visualize:
  - Which CoT structure yields the highest mean accuracy?
  - Are results consistent across models?
- Output: Bar chart or table of CoT performance per model.

---

## 🧩 Part II. Exploratory, Emergent Analyses

### 4. Prompt Robustness Across Tasks
**Goal:** Identify CoT types that generalize across task types.  
**Instructions:**
- For each task, determine which CoT category had the best performance.
- Count wins per CoT style across tasks.
- Output: Heatmap or matrix of CoT-style effectiveness by task.

---

### 5. Failure Mode Analysis
**Goal:** Understand how different prompts fail.  
**Instructions:**
- Manually examine incorrect generations.
- Tag common error types:
  - ❌ Wrong chemical concept
  - ❌ Vague/no reasoning
  - ❌ Hallucinated facts
  - ❌ Copied prompt
- Tally and compare failure types per CoT.
- Output: Table or pie chart of failure distribution.

---

### 6. Confidence vs Accuracy Trends
**Goal:** Explore whether models sound confident even when wrong.  
**Instructions:**
- If GPT-4o scores include confidence, plot confidence vs correctness.
- Alternatively, rate confidence manually (e.g., high/medium/low).
- Compare across CoT types and models.
- Output: Scatter plot or grouped bar chart of confidence vs accuracy.

---

### 7. Model Sensitivity to CoT Prompting
**Goal:** Measure performance gain from baseline to best CoT per model.  
**Instructions:**
- For each model and task:
  - Compute delta = Best CoT score – Baseline score.
- Output: Heatmap showing "CoT gain" across models and tasks.

---

### 8. Prompt Length or Complexity Effects
**Goal:** Determine if longer/more detailed prompts correlate with performance.  
**Instructions:**
- Measure word or token length of each prompt.
- Plot length vs accuracy per prompt.
- Optionally split by CoT type.
- Output: Scatter plot or line chart of length vs score.

---

## 📌 Suggested Report Structure

### Results (Backed by Data)
- Part I.1 – Patterns in Best Prompts
- Part I.2 – Prompt Generality
- Part I.3 – Best CoT Structure (Model-wise + Overall)

### Discussion (Observational Trends)
- Part II.4 – Prompt Robustness
- Part II.5 – Failure Mode Patterns
- Part II.6 – Confidence vs Accuracy
- Part II.7 – Model Sensitivity to CoT
- Part II.8 – Prompt Length & Complexity
