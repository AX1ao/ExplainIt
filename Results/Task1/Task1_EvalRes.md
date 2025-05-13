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
----

