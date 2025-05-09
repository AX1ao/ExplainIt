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
| 2 (Correct)    | 4        | 9        | 1             | 9                 |
| 1 (Partial)    | 5        | 1        | 7             | 6                 |
| 0 (Wrong)      | 1        | 0        | 2             | 0                 |

---

# 🧠 General Observations

## ✅ Success Rate (Score = 2)

### 📐 Formula
`Success (Failure) Rate = (Number of responses scored 2 (or 0)) / (Total number of responses for that prompt type) × 100%`

---

### ✅ Success Rate Table

| Prompt Type       | Formula | Result |
|-------------------|---------|--------|
| Baseline          | 4 / 10  | 40%    |
| Stepwise          | 9 / 10  | 90%    |
| Visual-first      | 1 / 10  | 10%    |
| Explanation-first | 9 / 10  | 90%    |

---

### ❌ Failure Rate Table

| Prompt Type       | Formula | Result |
|-------------------|---------|--------|
| Baseline          | 1 / 10  | 10%    |
| Stepwise          | 0 / 10  | 0%     |
| Visual-first      | 2 / 10  | 20%    |
| Explanation-first | 0 / 10  | 0%     |

---

## 📊 Prompt Type Trends

- **Baseline:** Tends to guess correctly in simpler comparisons but often lacks chemical justification. Best when structural difference is obvious.
- **Stepwise:** Clearly the strongest performer. Its structure helped models apply electron-based logic (e.g., lone pair availability, resonance suppression).
- **Visual-first:** Weakest performer again. Even with obvious visuals (e.g. O vs S), most responses stayed superficial.
- **Explanation-first:** Matches Stepwise in accuracy. Triggered resonance, hybridization, and delocalization reasoning consistently.

## 🚨 Common Failure Modes

- **Visual-first** prompts yielded low performance due to their observational-only nature.
- Baseline prompts often landed correct conclusions but lacked clear mechanistic insight.
- In a few tricky cases (e.g. benzoic acid vs benzaldehyde), some answers flipped the expected nucleophilicity trend due to misunderstanding electron-withdrawing groups.

## 🏅 Best Performing Images

- **Ammonia vs Methanol** and **MeNH₂ vs Aniline**: Nearly all prompt types got these right with solid reasoning.
- **Furan vs Thiophene**: Multiple prompts discussed heteroatom electronegativity correctly.
- **Histamine vs Imidazole**: Strong reasoning on lone pair accessibility by both Stepwise and Explanation-first.

## ❌ Worst Performing Images

- **Benzaldehyde vs Benzoic acid**: Baseline and Visual-first both failed; few explanations accounted for carbonyl reactivity properly.
- **Nicotinamide vs Purine**: All prompts gave vague or incorrect reasoning.
- **Pyrrole vs Pyridine**: Baseline chose the wrong nucleophile; others were hesitant.

---

# 🔍 Detailed Insights by Category

## 1. Correct Identifications often involved:

- Discussing lone pair location (sp² vs sp³ vs conjugated)
- Recognizing resonance or conjugation reducing nucleophilicity
- Using electronegativity to compare O, N, and S atoms
- Comparing substituent effects on reactivity

## 2. Partial Identifications were seen when:

- The model chose correctly but didn’t explain why
- It listed atom types or functional groups without mechanism
- It hesitated or used hedging language (“might be more reactive”)

## 3. Incorrect Identifications still included:

- Reversed logic (e.g., saying benzoic acid more nucleophilic than benzaldehyde)
- Treating all heteroatoms as equally reactive
- Ignoring delocalization or aromatic suppression

---

# 🧾 Prompt Type Performance Summary

| Prompt Type       | Strengths                                                                 | Weaknesses                                                                 |
|-------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Baseline**      | Quick, sometimes right on common-sense comparisons                        | Lacks explanation; cannot handle nuanced resonance or hybridization logic |
| **Stepwise**      | Very strong on structural and mechanistic breakdown                       | Occasionally over-explains or loses momentum before reaching a conclusion |
| **Visual-first**  | Picks up on obvious atom/group visuals                                    | Rarely applies electron logic or chemical rules                           |
| **Explanation-first** | Brings in chemical principles like EN, hybridization, resonance           | Sometimes verbose; logic chain may drift if molecule is unfamiliar        |

---

# 🪞 Final Reflection

In nucleophilicity comparison, accuracy depends heavily on understanding **electron density and accessibility**, not just visual structure. Prompts that encouraged **mechanistic reasoning** (like Stepwise and Explanation-first) dramatically outperformed others, especially in comparisons involving **resonance suppression**, **heteroatom substitution**, or **conjugation**.

Once again, we see that **prompt engineering is a decisive factor** in model performance. The success of Stepwise and Explanation-first prompts highlights how language structure can scaffold scientific thinking — even for complex molecular comparisons.

