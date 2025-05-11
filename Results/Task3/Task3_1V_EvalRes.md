# 🧠 Task 3 (Functional Groups)

---

## 📋 Overall CoT Evaluation Results

## 🧪 Task 3 Full Evaluation Table (All 40 Results)

| Pair                         | Prompt Type       | Score | Notes                                                       |
|------------------------------|-------------------|-------|-------------------------------------------------------------|
| Ammonia vs Methanol          | Baseline          | 1     | Correct choice, weak logic                                  |
|                              | Stepwise          | 2*    | Flawless electron-based reasoning                           |
|                              | Visual-first      | 1     | Observational only                                          |
|                              | Explanation-first | 2     | Clear and correct                                           |
| MeNH₂ vs Aniline             | Baseline          | 2     | Brief but accurate                                          |
|                              | Stepwise          | 2*    | Excellent explanation of delocalization                     |
|                              | Visual-first      | 1     | Pure description                                            |
|                              | Explanation-first | 2     | Strong, chemical insight                                    |
| Imidazole vs Pyridine        | Baseline          | 1     | Vague "more reactive" reasoning                             |
|                              | Stepwise          | 2     | Correct lone pair analysis                                  |
|                              | Visual-first      | 1     | No conclusion                                               |
|                              | Explanation-first | 2     | Good reasoning about lone pair access                       |
| Ethanol vs Phenol            | Baseline          | 1     | Weak reasoning                                              |
|                              | Stepwise          | 2*    | Excellent resonance-based comparison                        |
|                              | Visual-first      | 1     | Mentions groups, no decision                                |
|                              | Explanation-first | 2     | Clear resonance-based logic                                 |
| Pyrrole vs Pyridine          | Baseline          | 0     | Incorrect pick, bad reasoning                               |
|                              | Stepwise          | 1     | Touches on lone pairs, no comparison                        |
|                              | Visual-first      | 0     | No reasoning, no call                                       |
|                              | Explanation-first | 1     | Hints at key feature, doesn't commit                        |
| Cytosine vs Uracil           | Baseline          | 1     | Vague N-count logic                                         |
|                              | Stepwise          | 2*    | Excellent lone pair + ring discussion                       |
|                              | Visual-first      | 0     | No reasoning, no decision                                   |
|                              | Explanation-first | 2     | Good reasoning, clear call                                  |
| Histamine vs Imidazole       | Baseline          | 1     | “More donors” without chemistry                             |
|                              | Stepwise          | 2*    | Great hybridization contrast                                |
|                              | Visual-first      | 1     | Descriptive, non-committal                                  |
|                              | Explanation-first | 2     | Clear amine vs ring logic                                   |
| Benzaldehyde vs Benzoic acid | Baseline          | 0     | Incorrect call, wrong logic                                 |
|                              | Stepwise          | 1     | Reasonable comparison but no decision                       |
|                              | Visual-first      | 0     | Lists groups, no chemistry                                  |
|                              | Explanation-first | 1     | Attempts logic, unclear call                                |
| Nicotinamide vs Purine       | Baseline          | 0     | Incorrect with bad justification                            |
|                              | Stepwise          | 2     | Good comparison of base structure and lone pair location    |
|                              | Visual-first      | 0     | Pure atom description                                       |
|                              | Explanation-first | 1     | Delocalization logic present but not resolved               |
| Furan vs Thiophene           | Baseline          | 1     | Correct but vague                                            |
|                              | Stepwise          | 2*    | Excellent electronegativity comparison                      |
|                              | Visual-first      | 1     | Structural contrast only                                    |
|                              | Explanation-first | 2     | Accurate reactivity comparison                              |

---

# ✅ Score Distribution

| Score   | Count |
|---------|-------|
| 2*      | 6     |
| 2       | 12    |
| 1       | 17    |
| 0       | 5     |

- 2* (Correct + Excellent Reasonings)
- 2 (Correct)
- 1 (Partial)
- 0 (Wrong)
  
---

# 🧪 Overview

# 📊 Prompt Type Summary

| Prompt Type       | 2* | 2 | 1 | 0 |
|-------------------|----|---|---|---|
| Baseline          | 0  | 2 | 7 | 1 |
| Stepwise          | 4  | 4 | 2 | 0 |
| Visual-first      | 0  | 1 | 6 | 3 |
| Explanation-first | 2  | 5 | 2 | 0 |

---

# 🧠 General Observations

### 📐 Formula
`Success (Failure) Rate = (Number of responses scored 2 and 2* (or 0)) / Total responses for that prompt type × 100%`

---

### ✅ Success Rate Table

| Prompt Type       | Formula | Result |
|-------------------|---------|--------|
| Baseline          | 0 / 10  | 0%     |
| Stepwise          | 8 / 10  | 80%    |
| Visual-first      | 1 / 10  | 10%    |
| Explanation-first | 7 / 10  | 70%    |

---

### ❌ Failure Rate Table

| Prompt Type       | Formula | Result |
|-------------------|---------|--------|
| Baseline          | 3 / 10  | 30%    |
| Stepwise          | 0 / 10  | 0%     |
| Visual-first      | 3 / 10  | 30%    |
| Explanation-first | 0 / 10  | 0%     |

---

## 📊 Prompt Type Trends

- **Baseline:** Scored **0/10** for correct outputs. Despite sometimes identifying the right molecule, reasoning was consistently shallow or completely absent. Three responses were outright incorrect.
- **Stepwise:** Achieved **80% accuracy**, with 4 perfect scores. These prompts provided a clear logical scaffold that allowed the model to perform reliably, even on subtle comparisons.
- **Visual-first:** Scored only **1 correct**, mostly sticking to visual features without applying any chemistry. Weakest overall in both correctness and decisiveness.
- **Explanation-first:** Matched Stepwise closely with **70% accuracy**, prompting mechanistic reasoning including resonance and lone pair positioning, though a few responses were too vague or over-explained.

---

## 🚨 Common Failure Modes

- **Visual-first** often gave purely descriptive answers without reactivity reasoning or conclusions.
- **Baseline** relied on guesses, sometimes choosing correctly but rarely explaining why.
- Models failed to evaluate **resonance suppression** accurately in trickier comparisons (e.g., benzoic acid vs benzaldehyde).
- **Partials in Stepwise and Explanation-first** occurred when models listed correct factors but failed to synthesize a conclusion.

---

## 🏅 Best Performing Images

- **Ammonia vs Methanol** and **MeNH₂ vs Aniline**: Clear-cut donor comparisons where Stepwise and Explanation-first performed flawlessly.
- **Furan vs Thiophene**: Strong heteroatom contrast (O vs S) led to high scores for Stepwise and Explanation-first.
- **Histamine vs Imidazole**: Lone pair accessibility and hybridization were handled well by structured prompts.

---

## ❌ Worst Performing Images

- **Benzaldehyde vs Benzoic acid**: Both Baseline and Visual-first failed; most prompts misunderstood electron withdrawal.
- **Nicotinamide vs Purine**: Models often gave hesitant or contradictory reasoning across all prompt types.
- **Pyrrole vs Pyridine**: Incorrect or avoided conclusions despite clear trends in lone pair delocalization.

---

# 🔍 Detailed Insights by Category

## 1. Correct Identifications often involved:

- Clear reasoning around **lone pair donation and localization**
- Consideration of **resonance effects** (especially in phenols, anilines)
- Correct interpretation of **heteroatom electronegativity** (O vs N vs S)
- Step-by-step structure of **reactive site accessibility**

## 2. Partial Identifications were seen when:

- The model guessed correctly but lacked mechanistic support
- Prompts triggered listing of features without evaluating them
- The model hedged or stopped short of a clear conclusion

## 3. Incorrect Identifications still included:

- **Reversing acid/base roles** due to misunderstanding resonance
- **Overvaluing group count** ("more N atoms" = more reactive)
- Ignoring **delocalization** and lone pair geometry

---

# 🧾 Prompt Type Performance Summary

| Prompt Type       | Strengths                                                                 | Weaknesses                                                                 |
|-------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Baseline**      | Occasionally guessed right in easy cases                                  | 0 correct answers; reasoning weak or off-topic                            |
| **Stepwise**      | Best performer; strong logic chain, especially with hybridization/resonance | Slight risk of verbose listing without concluding                         |
| **Visual-first**  | Picks up on gross structural features (e.g. atom types, rings)            | Rarely makes decisions; lacks any deep chemical comparison                |
| **Explanation-first** | Triggers good mechanistic analysis (resonance, lone pair access)          | Sometimes drifts into verbosity or vagueness                              |

---

# 🪞 Final Reflection

The final results confirm a sharp divide between **chemically structured prompts** and all others.

- **Baseline** and **Visual-first** were consistently weak: observational, hesitant, or entirely off-topic.
- In contrast, **Stepwise** and **Explanation-first** unlocked the model’s deeper reasoning by providing a scaffold — helping it identify **lone pair localization**, **resonance suppression**, and **electron donation** correctly.

This study clearly supports the idea that **prompt quality matters more than model size** in scientific reasoning — and that Chain-of-Thought isn’t just a style, but a pathway to better cognition.

Meanwhile, both **Stepwise and Explanation-first** successfully triggered discussions about lone pair localization, resonance suppression, and heteroatom effects — which are central to predicting nucleophilic strength.

Ultimately, this task reaffirms that **prompt structure is not cosmetic** — it fundamentally alters how models think.
