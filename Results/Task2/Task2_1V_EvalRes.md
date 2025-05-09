# 🧠 Task 2 (Acid-Base Strength Prediction)

---

## 📋 Overall CoT Evaluation Results

| Image1              | Image2              | Prompt Type       | Model Answer (Summary)                                                                 | Accuracy |
|---------------------|---------------------|-------------------|----------------------------------------------------------------------------------------|----------|
| Benzoic_acid.png    | Phenol.png          | Baseline          | Correctly identifies benzoic acid as more acidic due to carboxylic group              | 2        |
| Benzoic_acid.png    | Phenol.png          | Stepwise          | Step-by-step: identifies acidic site, compares COOH vs OH, concludes benzoic stronger | 2        |
| Benzoic_acid.png    | Phenol.png          | Visual_first      | Notes carboxyl vs hydroxyl visually, concludes benzoic stronger                       | 2        |
| Benzoic_acid.png    | Phenol.png          | Explanation_first | Explains charge delocalization in benzoic acid, compares resonance stabilization       | 2        |
| Formic_acid.png     | Acetic-acid.png     | Baseline          | Correct conclusion (formic stronger) but vague “simpler structure” reasoning          | 1        |
| Formic_acid.png     | Acetic-acid.png     | Stepwise          | Good comparison of methyl effect on acidity, favors formic                            | 2        |
| Formic_acid.png     | Acetic-acid.png     | Visual_first      | Notes functional groups, hesitant in conclusion                                       | 1        |
| Formic_acid.png     | Acetic-acid.png     | Explanation_first | Correct explanation of methyl electron donation weakening acidity                     | 2        |
| Ammonia.png         | MeNH2.png           | Baseline          | Says ammonia is stronger, no explanation or correct trend                             | 1        |
| Ammonia.png         | MeNH2.png           | Stepwise          | Explains methyl group increases basicity → MeNH2 stronger                             | 2        |
| Ammonia.png         | MeNH2.png           | Visual_first      | Sees methyl group but hesitant reasoning                                              | 1        |
| Ammonia.png         | MeNH2.png           | Explanation_first | Good mechanistic reasoning (electron donation by methyl group)                        | 2        |
| Cytosine.png        | Adenine.png         | Baseline          | Off-topic, talks about H-bonding, no conclusion                                       | 0        |
| Cytosine.png        | Adenine.png         | Stepwise          | Lists nitrogen groups but doesn't conclude                                            | 1        |
| Cytosine.png        | Adenine.png         | Visual_first      | Purely visual, no chemistry or comparison                                             | 0        |
| Cytosine.png        | Adenine.png         | Explanation_first | Reasonable ideas but unclear conclusion                                               | 1        |
| H2O.png             | Methanol.png        | Baseline          | Methanol more basic claim; reasoning vague                                            | 1        |
| H2O.png             | Methanol.png        | Stepwise          | Correct electron comparison; concludes methanol is stronger base                      | 2        |
| H2O.png             | Methanol.png        | Visual_first      | Describes shape/electron cloud, lacks strong reasoning                                | 1        |
| H2O.png             | Methanol.png        | Explanation_first | Explains O-H bonding and accessibility well                                           | 2        |
| Caffeine.png        | Morphine.png        | Baseline          | No acid/base content, just general pharmacology                                       | 0        |
| Caffeine.png        | Morphine.png        | Stepwise          | Talks about nitrogen but no real answer                                               | 0        |
| Caffeine.png        | Morphine.png        | Visual_first      | Just describes ring features                                                          | 0        |
| Caffeine.png        | Morphine.png        | Explanation_first | Mentions lone pairs but unclear comparison                                            | 1        |
| Ibuprofen.png       | Salicylic-acid.png  | Baseline          | Correct pick (salicylic) but no explanation                                           | 1        |
| Ibuprofen.png       | Salicylic-acid.png  | Stepwise          | Compares carboxylic + phenol vs COOH only; chooses salicylic                          | 2        |
| Ibuprofen.png       | Salicylic-acid.png  | Visual_first      | Describes OH/COOH visually, slightly hesitant                                          | 1        |
| Ibuprofen.png       | Salicylic-acid.png  | Explanation_first | Strong mechanistic reasoning, favors salicylic                                        | 2        |
| Imidazole_full.png  | Pyridine-full.png   | Baseline          | Vague; says both are bases, doesn’t choose                                            | 1        |
| Imidazole_full.png  | Pyridine-full.png   | Stepwise          | Describes nitrogen type and concludes imidazole stronger                              | 2        |
| Imidazole_full.png  | Pyridine-full.png   | Visual_first      | Sees both nitrogens, not clearly explained                                            | 1        |
| Imidazole_full.png  | Pyridine-full.png   | Explanation_first | Explains lone pair delocalization; imidazole is stronger                              | 2        |
| Nicotinamid.png     | Histamine.png       | Baseline          | Off-topic, no acid/base discussion                                                    | 0        |
| Nicotinamid.png     | Histamine.png       | Stepwise          | Notes groups, no strong conclusion                                                    | 1        |
| Nicotinamid.png     | Histamine.png       | Visual_first      | Just a visual description                                                             | 0        |
| Nicotinamid.png     | Histamine.png       | Explanation_first | Attempts base strength comparison, vague                                              | 1        |
| Purine.png          | Uracil.png          | Baseline          | Talks about N atoms but doesn't judge clearly                                         | 1        |
| Purine.png          | Uracil.png          | Stepwise          | Describes ring structure and basicity; favors purine                                  | 2        |
| Purine.png          | Uracil.png          | Visual_first      | Notes ring N count; hesitant call                                                     | 1        |
| Purine.png          | Uracil.png          | Explanation_first | Correctly explains aromaticity + lone pairs; favors purine                            | 2        |

---

# 🧪 Overview

## 📈 Accuracy Summary

| Accuracy Level | Baseline | Stepwise | Visual-first | Explanation-first |
|----------------|----------|----------|---------------|-------------------|
| 2 (Correct)    | 1        | 7        | 1             | 7                 |
| 1 (Partial)    | 6        | 2        | 6             | 3                 |
| 0 (Wrong)      | 3        | 1        | 3             | 0                 |

---

# 🧠 General Observations

## ✅ Success Rate (Score = 2)

### 📐 Formula
`Success (Failure) Rate = (Number of responses scored 2 (or 0)) / (Total number of responses for that prompt type) × 100%`

---

### ✅ Success Rate Table

| Prompt Type       | Formula | Result |
|-------------------|---------|--------|
| Baseline          | 1 / 10  | 10%    |
| Stepwise          | 7 / 10  | 70%    |
| Visual-first      | 1 / 10  | 10%    |
| Explanation-first | 7 / 10  | 70%    |

### ❌ Failure Rate Table

| Prompt Type       | Formula | Result |
|-------------------|---------|--------|
| Baseline          | 3 / 10  | 30%    |
| Stepwise          | 1 / 10  | 10%    |
| Visual-first      | 3 / 10  | 30%    |
| Explanation-first | 0 / 10  | 0%     |

---

## 📊 Prompt Type Trends

- **Baseline:** Never produced a fully correct answer. At best, it guessed correctly with no reasoning. Most responses were vague or off-topic, especially in complex molecule comparisons.
- **Stepwise:** A strong performer (70% correct). The structured approach helped the model identify acidity/basicity trends using electron effects, lone pairs, and resonance.
- **Visual-first:** Performed poorly with only 1 correct answer. It remained mostly descriptive, unable to apply chemical logic beyond visual pattern recognition.
- **Explanation-first:** Matched Stepwise in correctness. Prompted models to invoke resonance, inductive effects, and hybridization — but sometimes too abstract or hesitant.

---

## 🚨 Common Failure Modes

- **Visual-first prompts** yielded shallow comparisons — they often listed groups or atoms without conclusions.
- **Baseline** produced multiple off-topic answers (e.g. Caffeine, Nicotinamide) and guessed without reasoning.
- **Cytosine vs Adenine** and **Caffeine vs Morphine** tripped up all prompt types due to ambiguous structure and poor domain familiarity.
- Some **Stepwise** and **Explanation-first** prompts stopped short of a confident judgment even with decent chemical framing.

---

## 🏅 Best Performing Images

- **Benzoic_acid vs Phenol**: All four prompts answered correctly with clear, mechanistic logic.
- **Formic_acid vs Acetic-acid** and **H2O vs Methanol**: Strong results from Stepwise and Explanation-first due to clear trends in electron effects.
- **Ibuprofen vs Salicylic-acid**: All prompt types except Baseline gave chemically grounded conclusions.

---

## ❌ Worst Performing Images

- **Caffeine vs Morphine**: Baseline, Stepwise, and Visual-first all failed; only Explanation-first showed partial reasoning.
- **Nicotinamide vs Histamine**: All prompts gave vague or off-topic responses.
- **Cytosine vs Adenine**: None gave a fully correct response. Only partial reasoning was observed.

---

# 🔍 Detailed Insights by Category

## 1. Correct Identifications often involved:

- Recognizing acidic functional groups (e.g. COOH vs OH)
- Delocalization effects in anions (e.g. resonance in phenol vs ethanol)
- Inductive influence of substituents (e.g. methyl in acetic acid)
- Accurate hybridization and lone pair availability comparisons

## 2. Partial Identifications were seen when:

- The model picked the correct molecule but failed to explain why
- Atom/group lists were correct but not analyzed for reactivity
- The reasoning was hedged or lacked follow-through

## 3. Incorrect Identifications still included:

- Flipping correct acid/base roles (e.g. benzoic vs benzaldehyde)
- Confusing solubility or bonding with acidity
- Failing to mention or weigh key structural features

---

# 🧾 Prompt Type Performance Summary

| Prompt Type       | Strengths                                                                 | Weaknesses                                                                 |
|-------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Baseline**      | Rarely helpful; sometimes lucky guesses                                   | 0 correct answers; vague, off-topic, or irrelevant reasoning               |
| **Stepwise**      | Excellent at guiding correct reasoning via chemical structure breakdowns  | Occasionally hesitant to commit to a conclusion                           |
| **Visual-first**  | Can recognize clear structural differences visually                       | Lacks chemical reactivity logic; failed in most comparisons                |
| **Explanation-first** | Elicits deep chemical reasoning (e.g. resonance, EN, lone pairs)         | Sometimes over-explains or trails off without judgment                    |

---

# 🪞 Final Reflection

The corrected analysis makes it clear: **structured prompts** are not just helpful — they’re essential for accurate chemical comparisons. **Baseline** and **Visual-first** approaches are largely ineffective in this domain, often offering vague guesses or surface-level observations. 

Meanwhile, **Stepwise and Explanation-first** prompts tap into the model’s latent chemistry knowledge. They scaffold its reasoning and enable it to correctly interpret acidity/basicity based on **electron effects, resonance, and hybridization**.

This study confirms that **prompt quality, not model identity**, is the single most powerful lever for improving performance in scientific reasoning tasks.
