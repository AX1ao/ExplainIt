# 🧠 Task 2 (Acid-Base Strength Prediction)

---

## 📋 Overall CoT Evaluation Results

## 🧪 Task 3 Full Evaluation Table (All 40 Results)

| Image1            | Image2              | Prompt Type       | Score | Reason                                                                 |
|-------------------|---------------------|-------------------|-------|------------------------------------------------------------------------|
| Ammonia.png       | Methanol.png        | Baseline          | 1     | Correct pick, but vague justification                                 |
| Ammonia.png       | Methanol.png        | Stepwise          | 2     | Good lone pair + EN comparison                                        |
| Ammonia.png       | Methanol.png        | Visual-first      | 1     | Identifies atoms, but conclusion is unclear                           |
| Ammonia.png       | Methanol.png        | Explanation-first | 2     | Explains N vs O lone pair donation well                               |
| MeNH2.png         | Aniline.png         | Baseline          | 1     | Correct pick, but lacks resonance explanation                         |
| MeNH2.png         | Aniline.png         | Stepwise          | 2     | Good discussion of conjugation in aniline                             |
| MeNH2.png         | Aniline.png         | Visual-first      | 1     | Structural only; no reactivity comparison                             |
| MeNH2.png         | Aniline.png         | Explanation-first | 2     | Well-explained difference in lone pair availability                   |
| Imidazole.png     | Pyridine.png        | Baseline          | 1     | Picks imidazole but gives vague reasons                               |
| Imidazole.png     | Pyridine.png        | Stepwise          | 2     | Discusses N positioning and basicity correctly                        |
| Imidazole.png     | Pyridine.png        | Visual-first      | 1     | Visual comparison only, no reasoning                                  |
| Imidazole.png     | Pyridine.png        | Explanation-first | 2     | Explains delocalization and N lone pair behavior                      |
| Ethanol.png       | Phenol.png          | Baseline          | 1     | Picks ethanol, but shallow reasoning                                  |
| Ethanol.png       | Phenol.png          | Stepwise          | 2     | Explains resonance in phenol and favors ethanol                       |
| Ethanol.png       | Phenol.png          | Visual-first      | 1     | Mentions atoms, weak logic                                            |
| Ethanol.png       | Phenol.png          | Explanation-first | 2     | Solid justification about lone pair access                            |
| Pyrrole.png       | Pyridine.png        | Baseline          | 0     | Incorrect: says pyridine is more nucleophilic                         |
| Pyrrole.png       | Pyridine.png        | Stepwise          | 1     | Vague lone pair talk, doesn't resolve conclusion                      |
| Pyrrole.png       | Pyridine.png        | Visual-first      | 0     | Describes shape, gives no judgment                                    |
| Pyrrole.png       | Pyridine.png        | Explanation-first | 1     | Mentions lone pair role, but no clear conclusion                      |
| Cytosine.png      | Uracil.png          | Baseline          | 1     | Picks cytosine, doesn't explain well                                  |
| Cytosine.png      | Uracil.png          | Stepwise          | 2     | Great atom-level comparison                                           |
| Cytosine.png      | Uracil.png          | Visual-first      | 1     | Lists atoms/groups, avoids answering                                  |
| Cytosine.png      | Uracil.png          | Explanation-first | 2     | Explains lone pair availability and resonance                         |
| Histamine.png     | Imidazole.png       | Baseline          | 1     | Correct pick, shallow reasoning                                       |
| Histamine.png     | Imidazole.png       | Stepwise          | 2     | Compares reactive N locations well                                    |
| Histamine.png     | Imidazole.png       | Visual-first      | 1     | Describes both groups but avoids call                                 |
| Histamine.png     | Imidazole.png       | Explanation-first | 2     | Discusses amine vs aromatic behavior well                             |
| Benzaldehyde.png  | Benzoic_acid.png    | Baseline          | 0     | Incorrect; benzoic acid less nucleophilic                             |
| Benzaldehyde.png  | Benzoic_acid.png    | Stepwise          | 1     | Identifies groups but avoids judgment                                 |
| Benzaldehyde.png  | Benzoic_acid.png    | Visual-first      | 0     | Pure description, no reasoning                                        |
| Benzaldehyde.png  | Benzoic_acid.png    | Explanation-first | 1     | Weak reasoning, no strong conclusion                                  |
| Nicotinamid.png   | Purine.png          | Baseline          | 0     | Picks purine without valid reasoning                                  |
| Nicotinamid.png   | Purine.png          | Stepwise          | 1     | Somewhat reasonable but lacks clarity                                 |
| Nicotinamid.png   | Purine.png          | Visual-first      | 0     | Only describes atoms, no call made                                    |
| Nicotinamid.png   | Purine.png          | Explanation-first | 1     | Attempts discussion, lacks depth or clarity                           |
| Furan.png         | Thiophene.png       | Baseline          | 1     | Picks furan (correct), gives no good reason                           |
| Furan.png         | Thiophene.png       | Stepwise          | 2     | Discusses electronegativity and delocalization                        |
| Furan.png         | Thiophene.png       | Visual-first      | 1     | Notes O vs S difference, no real explanation                          |
| Furan.png         | Thiophene.png       | Explanation-first | 2     | Strong justification using atomic properties                          |

---

# 🧪 Overview

## 📈 Accuracy Summary

| Accuracy Level | Baseline | Stepwise | Visual-first | Explanation-first |
|----------------|----------|----------|---------------|-------------------|
| 2 (Correct)    | 0        | 7        | 0             | 7                 |
| 1 (Partial)    | 7        | 3        | 7             | 3                 |
| 0 (Wrong)      | 3        | 0        | 3             | 0                 |

---

# 🧠 General Observations

### 📐 Formula
`Success (Failure) Rate = (Number of responses scored 2 (or 0)) / (Total number of responses for that prompt type) × 100%`

---

### ✅ Success Rate Table

| Prompt Type       | Formula | Result |
|-------------------|---------|--------|
| Baseline          | 0 / 10  | 0%     |
| Stepwise          | 7 / 10  | 70%    |
| Visual-first      | 0 / 10  | 0%     |
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

- **Baseline:** Never got a fully correct answer. Most responses were surface-level guesses without chemical reasoning. Only useful when the correct answer happened to be obvious.
- **Stepwise:** Among the top performers with 70% accuracy. These prompts led the model to structure its analysis, often identifying correct trends in lone pair localization and hybridization.
- **Visual-first:** Failed to produce a single fully correct answer. Even with obvious visual contrasts, the model stuck to neutral or hesitant language. Lacked any chemical insight.
- **Explanation-first:** Matched Stepwise in correctness (7/10). Helped trigger discussions about resonance and delocalization, but occasionally veered into vague or verbose responses.

---

## 🚨 Common Failure Modes

- **Visual-first** prompts consistently produced vague, observational content with no real conclusion.
- **Baseline** prompts showed a strong tendency to guess, sometimes aligning with the correct answer, but lacked reliable chemical logic.
- **Electron-withdrawing group effects** were misunderstood or ignored — notably in benzoic acid vs benzaldehyde.
- Some **partially correct Stepwise and Explanation-first** responses over-described structures without concluding which was more nucleophilic.

---

## 🏅 Best Performing Images

- **Ammonia vs Methanol** and **MeNH₂ vs Aniline**: Clear-cut differences allowed Stepwise and Explanation-first to excel.
- **Furan vs Thiophene**: Strong contrast in heteroatom electronegativity was correctly used by Stepwise and Explanation-first.
- **Histamine vs Imidazole**: Nucleophilic N site in histamine was consistently identified by both strong prompt types.

---

## ❌ Worst Performing Images

- **Benzaldehyde vs Benzoic acid**: Baseline and Visual-first both failed. Few models explained carbonyl nucleophilicity or carboxyl suppression.
- **Nicotinamide vs Purine**: All prompt types were hesitant or incorrect. Complex structure confused reasoning.
- **Pyrrole vs Pyridine**: Baseline made an incorrect call; Visual-first and Explanation-first both hesitated despite clear trends in lone pair delocalization.

---

# 🔍 Detailed Insights by Category

## 1. Correct Identifications often involved:

- Step-by-step breakdown of reactive centers (e.g. lone pair availability, hybridization)
- Recognition of resonance suppression (e.g. in aniline, phenol)
- Electronegative atom comparisons (e.g. O vs S, N vs O)
- Clear comparisons of sp² vs sp³ lone pair geometry

## 2. Partial Identifications were seen when:

- The model made a correct guess but failed to explain why
- It described structural features (e.g. atom types) without interpretation
- It hedged its language (“might be more reactive” or “likely”)

## 3. Incorrect Identifications still included:

- Choosing less nucleophilic species due to resonance misunderstanding
- Assuming more atoms = more reactive (e.g. histamine logic in Baseline)
- Using vague or irrelevant criteria (e.g. "simpler" or "bulkier")

---

# 🧾 Prompt Type Performance Summary

| Prompt Type       | Strengths                                                                 | Weaknesses                                                                 |
|-------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Baseline**      | Sometimes aligns with simple comparisons                                  | No correct answers; lacks chemical reasoning; guesses blindly              |
| **Stepwise**      | Strong at guiding structured chemical logic (hybridization, resonance)    | Sometimes over-literal; partials happen when no clear conclusion is made   |
| **Visual-first**  | Identifies obvious visual differences (atoms/groups)                      | 0 correct answers; lacks reactivity logic; only visual features            |
| **Explanation-first** | Triggers deep reasoning (resonance, lone pairs, conjugation)             | Occasionally verbose or too abstract for unfamiliar molecules              |

---

# 🪞 Final Reflection

In nucleophilicity comparisons, models can only succeed when the prompt scaffolds **chemical reasoning** — not just recognition. The complete failure of Visual-first and Baseline to produce correct answers highlights the **inadequacy of unstructured or shallow prompts**.

Meanwhile, both **Stepwise and Explanation-first** successfully triggered discussions about lone pair localization, resonance suppression, and heteroatom effects — which are central to predicting nucleophilic strength.

Ultimately, this task reaffirms that **prompt structure is not cosmetic** — it fundamentally alters how models think.
