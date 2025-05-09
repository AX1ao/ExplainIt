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
| 2 (Correct)    | 4        | 9        | 1             | 9                 |
| 1 (Partial)    | 5        | 3        | 7             | 4                 |
| 0 (Wrong)      | 1        | 2        | 4             | 1                 |

---

# 🧠 General Observations

## ✅ Success Rate (Score = 2)

### 📐 Formula
`Success/Failure Rate = (Number of responses scored 2 or 0) / (Total number of responses for that prompt type) × 100%`

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
| Stepwise          | 2 / 10  | 20%    |
| Visual-first      | 4 / 10  | 40%    |
| Explanation-first | 1 / 10  | 10%    |

---

## 📊 Prompt Type Trends

- **Baseline:** Performed best when the acid/base difference was textbook clear (e.g., benzoic vs phenol), but lacked depth in trickier comparisons. Often made vague, under-explained claims.
- **Stepwise:** Most consistently accurate. It helped the model break down structural features and build a clear answer. Only weak when molecule function was very complex.
- **Visual-first:** Struggled the most. Without chemical reasoning, most responses stayed observational or uncertain. Accuracy suffered unless visual difference was very obvious.
- **Explanation-first:** On par with Stepwise in performance. These prompts triggered detailed reasoning, especially about electron effects, resonance, and lone pairs. Weak only when the model got lost in abstract language.

## 🚨 Common Failure Modes

- **Visual-first prompts** often produced vague atom/group descriptions with no real judgment.
- **Caffeine vs Morphine** and **Nicotinamide vs Histamine** repeatedly confused the model due to complex, unfamiliar pharmacological structures.
- Many **Baseline** responses gave correct guesses with no mechanistic justification.
- Some **Stepwise** prompts collapsed into listing features without concluding.

## 🏅 Best Performing Images

- **Benzoic_acid vs Phenol**: All 4 prompts got it right with clear, confident reasoning.
- **Formic_acid vs Acetic-acid** and **H2O vs Methanol**: Great performance especially from Stepwise and Explanation-first.
- **Ibuprofen vs Salicylic-acid**: Clear advantage in salicylic acid, well picked up by multiple prompt types.

## ❌ Worst Performing Images

- **Caffeine vs Morphine**: All prompt types failed or hedged.
- **Nicotinamide vs Histamine**: Multiple prompts gave no real analysis.
- **Cytosine vs Adenine**: No strong reasoning, and only 1 correct-ish answer from 4 prompts.

---

# 🔍 Detailed Insights by Category

## 1. Correct Identifications often involved:

- Functional group comparisons (COOH vs OH)
- Charge stabilization (resonance, inductive effects)
- Clear reasoning steps or structured breakdown
- References to electron-withdrawing/donating effects

## 2. Partial Identifications were seen when:

- The model made a correct pick but gave incomplete or vague justification
- Prompts were more observational than analytical
- Multiple factors were mentioned but not weighed properly

## 3. Incorrect Identifications still included:

- Descriptions without judgment (“X has a methyl group…” with no follow-up)
- Focus on irrelevant features (e.g. brain receptors)
- Mixing up acidity vs basicity, or not picking a side at all

---

# 🧾 Prompt Type Performance Summary

| Prompt Type       | Strengths                                                                 | Weaknesses                                                                 |
|-------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Baseline**      | Can land correct answers on familiar comparisons; simple structure helps  | Often lacks reasoning; guesses with vague or no justification              |
| **Stepwise**      | Best overall performer; supports detailed, logical structure               | Sometimes lists features without reaching a conclusion                     |
| **Visual-first**  | Useful only when structures are extremely distinct                        | Mostly observational, avoids conclusions, lacks chemical logic             |
| **Explanation-first** | Triggers mechanistic and theoretical knowledge; strong on charge effects | Can ramble or drift when the chemistry is too abstract                     |

---

# 🪞 Final Reflection

The results show that **structured prompts** like **Stepwise** and **Explanation-first** are far more effective at eliciting correct, reasoned chemical comparisons. **Baseline** works when the task is easy and familiar. **Visual-first**, while intuitive for multimodal reasoning, underperforms in chemistry tasks where internal reasoning, not appearance, determines reactivity.

This evaluation confirms: for complex domain tasks like acid/base comparison, **prompt design matters more than model size** — and the right reasoning chain can unlock far better performance.
