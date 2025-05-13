# Task 1 (EAS Reactivity Prediction)

---

## OneVision

### Scoring + Reasoning Table

| Image Pair                    | Prompt Type   | Score | Reason                                                                 |
|------------------------------|---------------|-------|------------------------------------------------------------------------|
| Aniline vs Nitrobenzene      | Baseline      | 2     | Correct answer, no reasoning                                           |
| Aniline vs Nitrobenzene      | Stepwise      | 0     | Correct reasoning but wrong conclusion (says nitrobenzene is better)  |
| Aniline vs Nitrobenzene      | Visual        | 0     | Confused logic, mentions EDG/EWG but wrong answer                      |
| Aniline vs Nitrobenzene      | Explanation   | 2     | Correct reasoning about electron effects, correct answer               |
| Benzene vs Toluene           | Baseline      | 2     | Correct answer, no reasoning                                           |
| Benzene vs Toluene           | Stepwise      | 2     | Mentions methyl group activation, solid reasoning                      |
| Benzene vs Toluene           | Visual        | 2     | Weak reasoning but answer is correct                                   |
| Benzene vs Toluene           | Explanation   | 2*    | Excellent: hyperconjugation, ortho/para activation                     |
| Benzaldehyde vs Benzoic Acid | Baseline      | 0     | Wrong logic, focuses on acidity not EAS reactivity                     |
| Benzaldehyde vs Benzoic Acid | Stepwise      | 0     | Same incorrect reasoning as baseline                                   |
| Benzaldehyde vs Benzoic Acid | Visual        | 1     | Identifies carbonyls but lacks detailed comparison                     |
| Benzaldehyde vs Benzoic Acid | Explanation   | 2     | Accurately compares –CHO vs –COOH and reasoning is sound               |
| Pyridine vs Benzene          | Baseline      | 0     | Incorrect; misinterprets lone pair effect in pyridine                  |
| Pyridine vs Benzene          | Stepwise      | 0     | Identifies EWG but draws wrong conclusion                              |
| Pyridine vs Benzene          | Visual        | 0     | Wrong assumption that N donates electrons                              |
| Pyridine vs Benzene          | Explanation   | 2     | Accurate: N is electron-withdrawing                                    |
| Pyrrole vs Benzene           | Baseline      | 2     | Correct answer, no reasoning                                           |
| Pyrrole vs Benzene           | Stepwise      | 2     | Good reasoning about lone pair donation                                |
| Pyrrole vs Benzene           | Visual        | 2     | Correct visual interpretation                                          |
| Pyrrole vs Benzene           | Explanation   | 2*    | Excellent explanation of aromaticity and lone pair involvement         |
| Phenol vs Benzene            | Baseline      | 2     | Correct answer, no reasoning                                           |
| Phenol vs Benzene            | Stepwise      | 2     | Solid explanation of resonance activation                              |
| Phenol vs Benzene            | Visual        | 2     | Mentions OH group as enhancing reactivity                              |
| Phenol vs Benzene            | Explanation   | 2*    | Excellent detail on ortho/para activation and lone pair effects        |
| Anisole vs Benzene           | Baseline      | 1     | Correct answer but mislabels methoxy group                             |
| Anisole vs Benzene           | Stepwise      | 2     | Solid reasoning about resonance donation from OCH₃                     |
| Anisole vs Benzene           | Visual        | 1     | Vague but directionally right                                          |
| Anisole vs Benzene           | Explanation   | 2     | Clear and accurate reasoning                                           |
| Chlorobenzene vs Benzene     | Baseline      | 0     | Incorrect answer, misinterprets halogen effect                         |
| Chlorobenzene vs Benzene     | Stepwise      | 0     | Confused logic about ortho/para direction vs reactivity                |
| Chlorobenzene vs Benzene     | Visual        | 0     | Guesses based on group size, incorrect                                 |
| Chlorobenzene vs Benzene     | Explanation   | 2     | Correct: explains deactivating inductive effect of Cl                  |
| Nitrobenzene vs Benzene      | Baseline      | 2     | Correct answer, no reasoning                                           |
| Nitrobenzene vs Benzene      | Stepwise      | 2     | Accurately explains NO₂ as strong deactivator                          |
| Nitrobenzene vs Benzene      | Visual        | 1     | Correct answer but shaky logic                                         |
| Nitrobenzene vs Benzene      | Explanation   | 2     | Good chemical reasoning                                                |
| Styrene vs Benzene           | Baseline      | 2     | Correct answer, no reasoning                                           |
| Styrene vs Benzene           | Stepwise      | 2     | Reasoning about conjugation is sound                                   |
| Styrene vs Benzene           | Visual        | 1     | Correct answer, reasoning unclear                                      |
| Styrene vs Benzene           | Explanation   | 2*    | Excellent: explains conjugation and vinyl activation                   |

### Two-way Summary Table

| Image Pair                    | Baseline | Stepwise | Visual | Explanation |
|------------------------------|----------|----------|--------|-------------|
| Aniline vs Nitrobenzene      | 2        | 0        | 0      | 2           |
| Benzene vs Toluene           | 2        | 2        | 2      | 2*          |
| Benzaldehyde vs Benzoic Acid | 0        | 0        | 1      | 2           |
| Pyridine vs Benzene          | 0        | 0        | 0      | 2           |
| Pyrrole vs Benzene           | 2        | 2        | 2      | 2*          |
| Phenol vs Benzene            | 2        | 2        | 2      | 2*          |
| Anisole vs Benzene           | 1        | 2        | 1      | 2           |
| Chlorobenzene vs Benzene     | 0        | 0        | 0      | 2           |
| Nitrobenzene vs Benzene      | 2        | 2        | 1      | 2           |
| Styrene vs Benzene           | 2        | 2        | 1      | 2*          |

---

## Insights

## 🔍 Insights: Task 1 — LLAVA One Vision Performance (Manual Review)

### ✅ Overall Accuracy & Reasoning Trends

- **Explanation-first prompts performed best overall**, with 4/10 earning a perfect 2* score (flawless reasoning and correct answer), and only 1 prompt scoring below 2. This confirms that structured, reason-guided prompting helps the model produce more accurate and chemically grounded outputs.
- **Stepwise prompts showed moderate reliability**, often capturing the correct reasoning chain but occasionally failing at the final conclusion (e.g., Set 1 — Aniline vs Nitrobenzene). They tend to guide attention but not always judgment.
- **Visual-first prompts were highly variable**. Some relied on superficial pattern-matching or vague observations (e.g., “more atoms = more reactive”), leading to correct answers with weak logic or wrong answers entirely.
- **Baseline prompts often got the right answer** — especially for well-known comparisons — but lacked chemical justification. In several sets (e.g., Chlorobenzene), the model defaulted to incorrect intuition without structured support.

---

### 🧠 Reasoning Quality & Chemical Understanding

- LLAVA One Vision demonstrates **solid memorization of archetypal chemical behaviors** (e.g., reactivity of OH, NO₂, and CH₃ groups).
- However, the model sometimes confuses **acid/base concepts** with **electrophilic substitution reactivity** — especially in cases involving –COOH and –CHO (Set 3).
- Nitrogen heterocycles reveal the model’s **limits in understanding aromatic systems** — e.g., pyridine vs pyrrole — where it often misjudges electron donation/withdrawal unless explicitly guided by the prompt.

---

### 🧪 Key Observations

- **Correct answers ≠ correct reasoning**: Baseline and visual prompts sometimes yield right answers but with flawed logic — indicating brittle, surface-level generalization.
- **Prompt scaffolding boosts reasoning**: Structured prompts, especially Explanation-first, consistently help the model produce chemically sound justifications.
- **Failure cases are instructive**: Misclassifications like “chlorobenzene is more reactive” show overreliance on simple heuristics (e.g., "bigger group = stronger effect").

---

### 📊 Prompt Type Effectiveness (Average Score Comparison)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **2.0** (w/ 4× 2*) |
| Stepwise        | 1.2            |
| Visual-first    | 1.1            |
| Baseline        | 1.3            |

---
---
## LLaVA Med

### Scoring + Reasoning Table

| Image Pair                       | Prompt Type   | Score | Reason                                                                 |
|----------------------------------|---------------|-------|------------------------------------------------------------------------|
| Aniline vs Nitrobenzene          | Baseline      | 2     | Correct choice, vague explanation                                     |
| Aniline vs Nitrobenzene          | Stepwise      | 2     | Clear logic on EAS and donor effects                                  |
| Aniline vs Nitrobenzene          | Visual        | 2     | Mentions –OH/–NO₂ correctly, draws valid conclusion                    |
| Aniline vs Nitrobenzene          | Explanation   | 2*    | Excellent explanation of EAS activation                               |
| Benzene vs Toluene               | Baseline      | 2     | Correct with brief mention of OH effects                              |
| Benzene vs Toluene               | Stepwise      | 2     | Identifies activating group, good logical steps                       |
| Benzene vs Toluene               | Visual        | 2     | Highlights EDG presence visually, basic logic                         |
| Benzene vs Toluene               | Explanation   | 2*    | Strong justification involving resonance donation                     |
| Benzaldehyde vs Benzoic_acid     | Baseline      | 2     | Correct answer, identifies structure                                  |
| Benzaldehyde vs Benzoic_acid     | Stepwise      | 2     | Relates donation to reactivity well                                   |
| Benzaldehyde vs Benzoic_acid     | Visual        | 2     | Mentions EDG and correct comparison                                   |
| Benzaldehyde vs Benzoic_acid     | Explanation   | 2     | Accurate reasoning, slightly repetitive                               |
| Pyridine-full vs Benzene         | Baseline      | 2     | Correct answer, structural note                                       |
| Pyridine-full vs Benzene         | Stepwise      | 2     | References OH, ortho/para activation                                  |
| Pyridine-full vs Benzene         | Visual        | 2     | Recognizes –OH, lightly justified                                     |
| Pyridine-full vs Benzene         | Explanation   | 2*    | Excellent: delocalization and substitution logic                      |
| Pyrrole-full vs Benzene          | Baseline      | 2     | Describes structure, not tied to reactivity                           |
| Pyrrole-full vs Benzene          | Stepwise      | 2     | Touches on EAS logic and group donation                               |
| Pyrrole-full vs Benzene          | Visual        | 2     | Notes –OH and concludes activation                                    |
| Pyrrole-full vs Benzene          | Explanation   | 2*    | Justifies activation with lone pair donation                          |
| Phenol vs Benzene                | Baseline      | 2     | Correct but descriptive only                                          |
| Phenol vs Benzene                | Stepwise      | 2     | Strong EDG analysis                                                   |
| Phenol vs Benzene                | Visual        | 2     | Visual group recognition, conclusion valid                            |
| Phenol vs Benzene                | Explanation   | 2*    | Full explanation of lone pair and resonance                           |
| Anisole vs Benzene               | Baseline      | 2     | Correct, no detailed explanation                                      |
| Anisole vs Benzene               | Stepwise      | 2     | Explains substitution pattern and donation                            |
| Anisole vs Benzene               | Visual        | 2     | Recognizes –OH groups visually                                        |
| Anisole vs Benzene               | Explanation   | 2*    | Excellent breakdown of activation reasoning                           |
| Chlorobenzene vs Benzene         | Baseline      | 0     | Misidentifies hexachlorinated compound as reactive                    |
| Chlorobenzene vs Benzene         | Stepwise      | 0     | Fails to evaluate EWG properly                                        |
| Chlorobenzene vs Benzene         | Visual        | 1     | Mentions too many Cl, gets lucky                                      |
| Chlorobenzene vs Benzene         | Explanation   | 2     | Correctly explains deactivation by EWGs                               |
| Nitrobenzene vs Benzene          | Baseline      | 0     | Wrong: chooses EWG-rich ring                                          |
| Nitrobenzene vs Benzene          | Stepwise      | 0     | Fails to understand Cl deactivation                                   |
| Nitrobenzene vs Benzene          | Visual        | 0     | Recognizes Cl but concludes wrong                                     |
| Nitrobenzene vs Benzene          | Explanation   | 2     | Sound EAS analysis: inductive effect of Cl                            |
| Styrene vs Benzene               | Baseline      | 2     | Correct choice, no depth                                              |
| Styrene vs Benzene               | Stepwise      | 2     | Covers EAS behavior and substitution                                  |
| Styrene vs Benzene               | Visual        | 2     | Correct via group observation                                         |
| Styrene vs Benzene               | Explanation   | 2*    | Justifies using reactivity and resonance                              |

### Two-way Summary Table

| Image Pair                          | Baseline | Stepwise | Visual | Explanation |
|------------------------------------|----------|----------|--------|-------------|
| Aniline vs Nitrobenzene            | 2        | 2        | 2      | 2*          |
| Benzene vs Toluene                 | 2        | 2        | 2      | 2*          |
| Benzaldehyde vs Benzoic_acid       | 2        | 2        | 2      | 2           |
| Pyridine-full vs Benzene           | 2        | 2        | 2      | 2*          |
| Pyrrole-full vs Benzene            | 2        | 2        | 2      | 2*          |
| Phenol vs Benzene                  | 2        | 2        | 2      | 2*          |
| Salicylic-acid vs Benzoic_acid     | 2        | 2        | 2      | 2*          |
| Nitrobenzene vs Ozone              | 0        | 0        | 1      | 2           |
| Pyrrole-numbered vs Pyridine-full  | 0        | 0        | 0      | 2           |
| Morphine vs Caffeine               | 2        | 2        | 2      | 2*          |

---

### ✅ Overall Accuracy & Reasoning Trends

- **Explanation-first prompts were consistently excellent** — 7 out of 10 scored a perfect **2\***. This suggests that LLaVA-Med responds well to chemically scaffolded reasoning, delivering both correct answers and high-quality justification.
- **Baseline, Stepwise, and Visual-first** all performed uniformly well across most tasks — until presented with difficult or misleading input (e.g. multiple EWGs), where **Stepwise and Visual-first failed** to apply deeper reasoning.
- The **model struggled significantly with electron-withdrawing groups** like –Cl. In both hexachlorinated examples (Pairs 8 & 9), only Explanation-first was able to override superficial group-counting heuristics and reason chemically.

---

### 🧠 Reasoning Quality & Chemical Understanding

- **Donation vs withdrawal effects** were clearly recognized in prompts that invoked reasoning explicitly. Baseline and Visual-first often ignored these effects or applied them incorrectly in complex substitutions.
- LLaVA-Med tends to default to **"more groups = more reactive"** when unprompted, leading to poor outcomes in Pairs 8 & 9 where this heuristic breaks.
- When prompted through **Explanation-first**, the model was able to articulate ideas like **inductive withdrawal**, **resonance donation**, and **ortho/para activation** with high accuracy.

---

### 🧪 Key Observations

- **Consistent correct performance** in pairs involving –OH and other clear EDGs.
- **Systematic failure in Cl-rich rings** without guided reasoning — revealing a key model vulnerability.
- **Strong reliance on Explanation-first prompts** to activate chemically correct generalizations, especially in edge cases.

---

### 📊 Prompt Type Effectiveness (Average Score Comparison)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **2.0** (with 7× 2\*) |
| Stepwise        | 1.6            |
| Visual-first    | 1.5            |
| Baseline        | 1.6            |

---
---

## DeepSeek-VL

### Scoring + Reasoning Table

| Image Pair                          | Prompt Type   | Score | Reason                                                                 |
|------------------------------------|---------------|-------|------------------------------------------------------------------------|
| Aniline vs Nitrobenzene            | Baseline      | 1     | Picks partially correct, vague explanation                            |
| Aniline vs Nitrobenzene            | Stepwise      | 0     | Refuses to answer                                                     |
| Aniline vs Nitrobenzene            | Visual        | 0     | Refuses to answer                                                     |
| Aniline vs Nitrobenzene            | Explanation   | 0     | Refuses to answer                                                     |
| Benzene vs Toluene                 | Baseline      | 1     | Picks toluene correctly, no reasoning                                 |
| Benzene vs Toluene                 | Stepwise      | 0     | Refuses to answer                                                     |
| Benzene vs Toluene                 | Visual        | 0     | Refuses to answer                                                     |
| Benzene vs Toluene                 | Explanation   | 0     | Refuses to answer                                                     |
| Benzaldehyde vs Benzoic_acid       | Baseline      | 1     | Correct molecule selected, no justification                          |
| Benzaldehyde vs Benzoic_acid       | Stepwise      | 0     | Refuses to answer                                                     |
| Benzaldehyde vs Benzoic_acid       | Visual        | 0     | Refuses to answer                                                     |
| Benzaldehyde vs Benzoic_acid       | Explanation   | 0     | Refuses to answer                                                     |
| Pyridine-full vs Benzene           | Baseline      | 1     | Chooses wrong molecule (pyridine), mentions substitution              |
| Pyridine-full vs Benzene           | Stepwise      | 0     | Refuses to answer                                                     |
| Pyridine-full vs Benzene           | Visual        | 0     | Refuses to answer                                                     |
| Pyridine-full vs Benzene           | Explanation   | 0     | Refuses to answer                                                     |
| Pyrrole-full vs Benzene            | Baseline      | 1     | Picks correctly but lacks any chemical explanation                    |
| Pyrrole-full vs Benzene            | Stepwise      | 0     | Refuses to answer                                                     |
| Pyrrole-full vs Benzene            | Visual        | 0     | Refuses to answer                                                     |
| Pyrrole-full vs Benzene            | Explanation   | 0     | Refuses to answer                                                     |
| Phenol vs Benzene                  | Baseline      | 1     | Picks phenol, explanation is generic                                  |
| Phenol vs Benzene                  | Stepwise      | 0     | Refuses to answer                                                     |
| Phenol vs Benzene                  | Visual        | 0     | Refuses to answer                                                     |
| Phenol vs Benzene                  | Explanation   | 0     | Refuses to answer                                                     |
| Salicylic-acid vs Benzoic_acid     | Baseline      | 1     | Picks correctly, but vague logic                                      |
| Salicylic-acid vs Benzoic_acid     | Stepwise      | 0     | Refuses to answer                                                     |
| Salicylic-acid vs Benzoic_acid     | Visual        | 0     | Refuses to answer                                                     |
| Salicylic-acid vs Benzoic_acid     | Explanation   | 0     | Refuses to answer                                                     |
| Nitrobenzene vs Ozone              | Baseline      | 1     | Chooses nitrobenzene, logic is unclear                                |
| Nitrobenzene vs Ozone              | Stepwise      | 0     | Refuses to answer                                                     |
| Nitrobenzene vs Ozone              | Visual        | 0     | Refuses to answer                                                     |
| Nitrobenzene vs Ozone              | Explanation   | 0     | Refuses to answer                                                     |
| Pyrrole-numbered vs Pyridine-full  | Baseline      | 1     | Correct answer, no justification                                      |
| Pyrrole-numbered vs Pyridine-full  | Stepwise      | 0     | Refuses to answer                                                     |
| Pyrrole-numbered vs Pyridine-full  | Visual        | 0     | Refuses to answer                                                     |
| Pyrrole-numbered vs Pyridine-full  | Explanation   | 0     | Refuses to answer                                                     |
| Morphine vs Caffeine               | Baseline      | 1     | Chooses morphine with generic sentence                                |
| Morphine vs Caffeine               | Stepwise      | 0     | Refuses to answer                                                     |
| Morphine vs Caffeine               | Visual        | 0     | Refuses to answer                                                     |
| Morphine vs Caffeine               | Explanation   | 0     | Refuses to answer                                                     |

### Two-way Summary Table

| Image Pair                          | Baseline | Stepwise | Visual | Explanation |
|------------------------------------|----------|----------|--------|-------------|
| Aniline vs Nitrobenzene            | 1        | 0        | 0      | 0           |
| Benzene vs Toluene                 | 1        | 0        | 0      | 0           |
| Benzaldehyde vs Benzoic_acid       | 1        | 0        | 0      | 0           |
| Pyridine-full vs Benzene           | 1        | 0        | 0      | 0           |
| Pyrrole-full vs Benzene            | 1        | 0        | 0      | 0           |
| Phenol vs Benzene                  | 1        | 0        | 0      | 0           |
| Salicylic-acid vs Benzoic_acid     | 1        | 0        | 0      | 0           |
| Nitrobenzene vs Ozone              | 1        | 0        | 0      | 0           |
| Pyrrole-numbered vs Pyridine-full  | 1        | 0        | 0      | 0           |
| Morphine vs Caffeine               | 1        | 0        | 0      | 0           |

---

### ❌ Overall Behavior

- Despite using the **correct model** (`deepseek-vl-7b-chat`), **DeepSeek refused to process visual content** across all CoT prompts.
- Only the **baseline prompt** returned any output — and even then, responses were **vague, generic, or wrong**.
- All **stepwise**, **visual-first**, and **explanation-first** prompts triggered the model’s fallback safety phrase:
  > *“As an AI language model, I cannot observe or analyze images.”*

This behavior persisted across all 10 image pairs.

---

### 🧠 Reasoning Quality (Baseline Only)

- The model **sometimes guessed correctly** (e.g., Toluene > Benzene, Phenol > Benzene), but **never explained why**.
- In some cases, it gave **confident but incorrect answers** (e.g., Nitrobenzene > Aniline).
- All reasoning-heavy prompt types failed completely, making **visual comparison and chain-of-thought analysis impossible**.

---

### 🧪 Root Cause (Diagnosis)

- The failure likely stems from **incorrect input formatting** in the script:
  - Images were passed using a legacy `{"images": [path1, path2]}` format.
  - DeepSeek-VL expects structured input like:
    ```json
    {"type": "image", "image": <path>}
    {"type": "text", "text": <prompt>}
    ```
- As a result, the model **defaulted to text-only mode** and hallucinated blindness.

---

### 📊 Prompt Type Effectiveness (Average Score Comparison)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | 0.0            |
| Stepwise        | 0.0            |
| Visual-first    | 0.0            |
| Baseline        | **1.0**        |

---

### 🔧 Recommendations

- ✅ **Fix the input format** to explicitly include image-type content blocks.
- ⚠️ **Avoid large batch loading** — DeepSeek-VL is memory-intensive and may silently fail on T4 GPUs.
- ✅ Test first with a **single image-prompt pair** and confirm visual reasoning is working.
- 🧪 Consider switching to `deepseek-vl-1.3b` or other lighter models for debugging purposes.

---

