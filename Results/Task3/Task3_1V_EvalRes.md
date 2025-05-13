# 🧠 Task 3 (Functional Groups)

---

## One Vision

### Scoring + Reasoning Table

| Image Pair                    | Prompt Type       | Score | Reason                                                                 |
|------------------------------|-------------------|-------|------------------------------------------------------------------------|
| Ammonia vs Methanol          | Baseline          | 2     | Correct: N less electronegative, better nucleophile                   |
| Ammonia vs Methanol          | Stepwise          | 2     | Lone pairs and atomic properties well compared                        |
| Ammonia vs Methanol          | Visual            | 1     | Minimal structure-based description                                   |
| Ammonia vs Methanol          | Explanation       | 2*    | Excellent orbital + electronegativity explanation                     |
| MeNH₂ vs Aniline             | Baseline          | 2     | Identifies delocalization in aniline                                  |
| MeNH₂ vs Aniline             | Stepwise          | 2     | Resonance and conjugation explained                                   |
| MeNH₂ vs Aniline             | Visual            | 1     | Notes aromatic ring, doesn’t explain chemistry                        |
| MeNH₂ vs Aniline             | Explanation       | 2*    | Full conjugation vs localization breakdown                            |
| Imidazole vs Pyridine        | Baseline          | 1     | Correct answer, vague logic                                           |
| Imidazole vs Pyridine        | Stepwise          | 2     | Lone pair availability discussed clearly                              |
| Imidazole vs Pyridine        | Visual            | 1     | Counts N atoms, doesn’t explain function                              |
| Imidazole vs Pyridine        | Explanation       | 2*    | Lone pair involvement vs neutrality explained perfectly               |
| Morpholine vs Piperidine     | Baseline          | 2     | Picks piperidine, reasoning vague                                     |
| Morpholine vs Piperidine     | Stepwise          | 2     | Oxygen’s inductive effect addressed                                   |
| Morpholine vs Piperidine     | Visual            | 1     | Structural observation only                                           |
| Morpholine vs Piperidine     | Explanation       | 2*    | Electronic effects on N explained thoroughly                          |
| Acetate vs Methoxide         | Baseline          | 2     | Picks correctly, localized charge argument                            |
| Acetate vs Methoxide         | Stepwise          | 2     | Resonance explained clearly                                           |
| Acetate vs Methoxide         | Visual            | 1     | Identifies spread-out charge visually                                 |
| Acetate vs Methoxide         | Explanation       | 2*    | Resonance and charge impact explained excellently                     |
| Cytosine vs Uracil       | Baseline          | 1     | Picks cytosine, mentions donor atoms but vague                        |
| Cytosine vs Uracil       | Stepwise          | 2     | Identifies NH₂ group and its nucleophilic potential                   |
| Cytosine vs Uracil       | Visual            | 0     | Guesses based on “more atoms,” no logic                               |
| Cytosine vs Uracil       | Explanation       | 2*    | Explains conjugation and donation clearly                             |
| Histamine vs Imidazole   | Baseline          | 1     | Picks histamine, shallow “more nitrogen” reasoning                    |
| Histamine vs Imidazole   | Stepwise          | 2     | Identifies lone pair and group accessibility                          |
| Histamine vs Imidazole   | Visual            | 1     | Surface group comparison                                               |
| Histamine vs Imidazole   | Explanation       | 2*    | Excellent breakdown of NH₂ vs aromatic lone pairs                     |
| Benzaldehyde vs Benzoic acid | Baseline      | 1     | Correct but vague logic                                               |
| Benzaldehyde vs Benzoic acid | Stepwise      | 2     | Correct carbonyl comparison                                           |
| Benzaldehyde vs Benzoic acid | Visual        | 1     | Group observation only                                                |
| Benzaldehyde vs Benzoic acid | Explanation   | 2*    | Resonance and nucleophilic oxygen discussed thoroughly                |
| Nicotinamide vs Purine   | Baseline          | 1     | Picks correctly but weak logic                                        |
| Nicotinamide vs Purine   | Stepwise          | 2     | Discusses donation points                                             |
| Nicotinamide vs Purine   | Visual            | 1     | Counts N atoms, no deeper logic                                       |
| Nicotinamide vs Purine   | Explanation       | 2*    | Conjugation and ring system explained in detail                       |
| Furan vs Thiophene       | Baseline          | 1     | Picks furan, shallow “O is more reactive” claim                       |
| Furan vs Thiophene       | Stepwise          | 2     | Discusses heteroatoms and ring effects                                |
| Furan vs Thiophene       | Visual            | 1     | Observes atoms, no deeper chemistry                                   |
| Furan vs Thiophene       | Explanation       | 2*    | Excellent reasoning around polarity and aromaticity                   |

### Two-way Summary Table

| Image Pair                    | Baseline | Stepwise | Visual | Explanation |
|------------------------------|----------|----------|--------|-------------|
| Ammonia vs Methanol          | 2        | 2        | 1      | 2*          |
| MeNH₂ vs Aniline             | 2        | 2        | 1      | 2*          |
| Imidazole vs Pyridine        | 1        | 2        | 1      | 2*          |
| Morpholine vs Piperidine     | 2        | 2        | 1      | 2*          |
| Acetate vs Methoxide         | 2        | 2        | 1      | 2*          |
| Cytosine vs Uracil       | 1        | 2        | 0      | 2*          |
| Histamine vs Imidazole   | 1        | 2        | 1      | 2*          |
| Benzaldehyde vs Benzoic acid | 1    | 2        | 1      | 2*          |
| Nicotinamide vs Purine   | 1        | 2        | 1      | 2*          |
| Furan vs Thiophene       | 1        | 2        | 1      | 2*          |

---

### ✅ Overall Accuracy & Reasoning Trends

- **Explanation-first prompts dominated** once again — 9 out of 10 image pairs scored a perfect **2\***, showing that LLaVA performs best when given structured, theory-rich prompts.
- **Stepwise prompts were also highly effective**, scoring 2s across all pairs. The model benefits from guided reasoning that helps it isolate key features like lone pair availability and inductive effects.
- **Baseline prompts showed good intuition**, often guessing the right answer but failing to articulate why — many responses relied on phrases like “more reactive” or “more groups” without clear chemical justification.
- **Visual-first prompts remained the weakest**, with low reasoning density. The model tended to focus on visible atom counts or general structural complexity without applying underlying chemical principles.

---

### 🧠 Chemical Reasoning Quality

- The model understands key nucleophilicity factors well under guided prompts:
  - **Lone pair availability** (e.g. amines vs aromatics)
  - **Resonance delocalization** as a deactivator (e.g. acetate vs methoxide)
  - **Electronegativity and atomic properties** (e.g. nitrogen vs oxygen)
- It also handles subtle cases like **imidazole vs pyridine** and **furan vs thiophene** when explicitly prompted to consider electron delocalization or aromatic effects.

---

### ⚠️ Observed Failure Modes

- **Visual-first responses** often reduce to group counting: “this one has more nitrogens” or “oxygen is more reactive” — without discussing electron donation or reactivity.
- **Baseline prompts** occasionally hallucinate cause-effect claims (e.g., “benzoic acid is more nucleophilic because of the acid group”), indicating the model defaults to general chemical familiarity unless prompted to reason.
- In the absence of stepwise or explanation formats, **resonance and inductive effects are rarely mentioned**, even when essential to the correct answer.

---

### 📊 Prompt Type Effectiveness (Average Score)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **2.0** (9× 2\*) |
| Stepwise        | 2.0            |
| Baseline        | 1.5            |
| Visual-first    | 0.9            |

---
---

## LLaVA Med

### Scoring + Reasoning Table

| Image Pair                | Prompt Type       | Score | Reason                                                                 |
|--------------------------|-------------------|-------|------------------------------------------------------------------------|
| NH₂⁻ vs OH⁻              | Baseline          | 2     | Picks NH₂⁻ and gives basic reasoning on nitrogen                       |
| NH₂⁻ vs OH⁻              | Stepwise          | 0     | Missing output                                                        |
| NH₂⁻ vs OH⁻              | Visual            | 1     | Mentions reactive centers, logic unclear                              |
| NH₂⁻ vs OH⁻              | Explanation       | 2*    | Clear explanation of electronegativity and lone pair reactivity       |
| Methylamine vs Pyridine  | Baseline          | 2     | Picks correctly, says NH₂ more reactive                                |
| Methylamine vs Pyridine  | Stepwise          | 0     | Missing output                                                        |
| Methylamine vs Pyridine  | Visual            | 1     | Points out groups, no clear conclusion                                |
| Methylamine vs Pyridine  | Explanation       | 2*    | Describes lone pair resonance in pyridine vs localized in MeNH₂       |
| Pyrazine vs Pyridine     | Baseline          | 0     | Incorrect: says methylation increases nucleophilicity                 |
| Pyrazine vs Pyridine     | Stepwise          | 0     | Missing output                                                        |
| Pyrazine vs Pyridine     | Visual            | 0     | Same as baseline — incorrect                                          |
| Pyrazine vs Pyridine     | Explanation       | 2     | Picks correctly and explains resonance and steric hindrance           |
| Piperidine vs Morpholine | Baseline          | 2     | Picks piperidine with vague justification                             |
| Piperidine vs Morpholine | Stepwise          | 0     | Missing output                                                        |
| Piperidine vs Morpholine | Visual            | 1     | Describes groups, avoids conclusion                                   |
| Piperidine vs Morpholine | Explanation       | 2*    | Clear logic on oxygen withdrawing e⁻ from nitrogen                    |
| Methoxide vs Acetate     | Baseline          | 2     | Picks correctly, briefly mentions resonance                           |
| Methoxide vs Acetate     | Stepwise          | 0     | Missing output                                                        |
| Methoxide vs Acetate     | Visual            | 1     | Identifies groups, guesses correctly                                  |
| Methoxide vs Acetate     | Explanation       | 2*    | Strong explanation of charge delocalization and nucleophilicity       |
| 2-aminobenzimide vs 2-nitrobenzoic acid | Baseline          | 2     | Picks correctly, shallow but directionally valid                      |
| 2-aminobenzimide vs 2-nitrobenzoic acid | Stepwise          | 0     | Missing                                                               |
| 2-aminobenzimide vs 2-nitrobenzoic acid | Visual            | 1     | Structural guess without mechanism                                    |
| 2-aminobenzimide vs 2-nitrobenzoic acid | Explanation       | 2*    | Excellent discussion of lone pairs and EWG effects                    |
| 4-chloro-2-nitrobenzaldehyde vs 4-aminophenol | Baseline     | 2     | Picks amino compound, limited reasoning                              |
| 4-chloro-2-nitrobenzaldehyde vs 4-aminophenol | Stepwise     | 0     | Missing                                                               |
| 4-chloro-2-nitrobenzaldehyde vs 4-aminophenol | Visual       | 1     | Correct direction, lacks justification                               |
| 4-chloro-2-nitrobenzaldehyde vs 4-aminophenol | Explanation   | 2*    | Excellent EDG vs EWG comparison                                       |
| Dimethylhydroquinone vs Catechol     | Baseline          | 2     | Picks catechol, explains position effect                              |
| Dimethylhydroquinone vs Catechol     | Stepwise          | 0     | Missing                                                               |
| Dimethylhydroquinone vs Catechol     | Visual            | 1     | Points out OHs, but doesn’t compare                                   |
| Dimethylhydroquinone vs Catechol     | Explanation       | 2*    | Resonance and spacing explained                                       |
| 2-aminobenzimide vs Imidazole         | Baseline          | 0     | Incorrect — based on group count                                      |
| 2-aminobenzimide vs Imidazole         | Stepwise          | 0     | Missing                                                               |
| 2-aminobenzimide vs Imidazole         | Visual            | 0     | Wrong guess based on appearance                                       |
| 2-aminobenzimide vs Imidazole         | Explanation       | 2     | Picks correctly, explains lone pair availability                      |
| DTT vs Catechol                       | Baseline          | 2     | Chooses DTT and mentions thiol reactivity                             |
| DTT vs Catechol                       | Stepwise          | 0     | Missing                                                               |
| DTT vs Catechol                       | Visual            | 1     | Identifies SH groups only                                             |
| DTT vs Catechol                       | Explanation       | 2*    | Great polarizability and reactivity comparison                        |

### Two-way Summary Table

| Image Pair                | Baseline | Stepwise | Visual | Explanation |
|--------------------------|----------|----------|--------|-------------|
| NH₂⁻ vs OH⁻              | 2        | 0        | 1      | 2*          |
| Methylamine vs Pyridine  | 2        | 0        | 1      | 2*          |
| Pyrazine vs Pyridine     | 0        | 0        | 0      | 2           |
| Piperidine vs Morpholine | 2        | 0        | 1      | 2*          |
| Methoxide vs Acetate     | 2        | 0        | 1      | 2*          |
| 2-aminobenzimide vs 2-nitrobenzoic acid | 2        | 0        | 1      | 2*          |
| 4-chloro-2-nitrobenzaldehyde vs 4-aminophenol | 2 | 0        | 1      | 2*          |
| Dimethylhydroquinone vs Catechol     | 2        | 0        | 1      | 2*          |
| 2-aminobenzimide vs Imidazole         | 0        | 0        | 0      | 2           |
| DTT vs Catechol                       | 2        | 0        | 1      | 2*          |

---

### ✅ Overall Accuracy & Prompt Trends

- **Explanation-first prompts were clearly the strongest**, with 9 out of 10 earning perfect or near-perfect scores (7× 2\*, 2× 2). These prompts consistently elicited accurate comparisons involving electron density, resonance, and lone pair availability.
- **Baseline prompts performed moderately well**, with correct answers in 8 out of 10 cases, though the chemical reasoning was often vague or shallow.
- **Visual-first prompts were weak**, mostly providing superficial structure mentions (e.g., “has more groups”) without mechanistic understanding. They often guessed correctly but could not justify the outcome.
- **Stepwise prompts were missing** for all 10 pairs, leading to 0s across the board for that category. This makes direct comparison difficult but underscores the importance of verifying model response completeness.

---

### 🧠 Chemical Understanding Highlights

- LLaVA-Med correctly applies principles of **electronegativity, resonance delocalization, and conjugation** when given the chance to reason step-by-step or explain directly.
- The model recognizes **inductive effects** well, particularly for groups like –NO₂ or –OH vs –SH, as seen in comparisons like morpholine vs piperidine and DTT vs catechol.
- In borderline cases (e.g., imidazole vs 2-aminobenzimide), **Explanation-first** prompts yielded chemically correct and detailed answers, while other prompt types either failed or made incorrect assumptions.

---

### ⚠️ Observed Weaknesses

- Visual-first responses consistently lack depth, defaulting to heuristics like "more groups = more reactive."
- Baseline responses often assume familiarity without actual reasoning — they occasionally hallucinate relationships between structure and function.
- The total absence of Stepwise responses may reflect either a runtime/model error or prompt incompatibility. Regardless, the absence prevents one of the most pedagogically useful prompt types from being evaluated.

---

### 📊 Prompt Type Effectiveness (Average Score)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **2.0** (7× 2\*, 2× 2) |
| Baseline        | 1.6            |
| Visual-first    | 0.9            |
| Stepwise        | 0.0 (all missing)   |

---
---

## DeepSeek-VL

### Scoring + Reasoning Table

| Image Pair            | Prompt Type       | Score | Reason                                                                 |
|-----------------------|-------------------|-------|------------------------------------------------------------------------|
| Ammonia vs Methanol   | Baseline          | 0     | Refused to compare or conclude                                         |
| Ammonia vs Methanol   | Stepwise          | 0     | Described electron pairs but no conclusion                            |
| Ammonia vs Methanol   | Visual            | 0     | Vision refusal                                                         |
| Ammonia vs Methanol   | Explanation       | 2     | Explained electronegativity and lone pair donation                    |
| MeNH₂ vs Aniline      | Baseline          | 0     | Avoided comparison                                                     |
| MeNH₂ vs Aniline      | Stepwise          | 1     | Described resonance, didn’t conclude                                  |
| MeNH₂ vs Aniline      | Visual            | 0     | Vision refusal                                                         |
| MeNH₂ vs Aniline      | Explanation       | 2     | Explained conjugation vs localization                                 |
| Imidazole vs Pyridine | Baseline          | 0     | Refused to answer                                                      |
| Imidazole vs Pyridine | Stepwise          | 1     | Compared lone pair roles, no conclusion                               |
| Imidazole vs Pyridine | Visual            | 0     | Vision refusal                                                         |
| Imidazole vs Pyridine | Explanation       | 2     | Lone pair resonance vs availability well explained                    |
| Piperidine vs Morpholine | Baseline       | 0     | Declines to compare                                                    |
| Piperidine vs Morpholine | Stepwise       | 1     | Discussed inductive effect of oxygen, no decision                     |
| Piperidine vs Morpholine | Visual         | 0     | Vision refusal                                                         |
| Piperidine vs Morpholine | Explanation    | 2     | Inductive effect from oxygen clearly explained                        |
| Acetate vs Methoxide  | Baseline          | 0     | Avoided conclusion                                                     |
| Acetate vs Methoxide  | Stepwise          | 1     | Compared resonance vs localization, didn’t pick                       |
| Acetate vs Methoxide  | Visual            | 0     | Vision refusal                                                         |
| Acetate vs Methoxide  | Explanation       | 2     | Resonance and nucleophilicity balance explained well                  |
| Cytosine vs Uracil    | Baseline          | 0     | Refused to compare                                                    |
| Cytosine vs Uracil    | Stepwise          | 1     | Discussed NH₂ site but no conclusion                                  |
| Cytosine vs Uracil    | Visual            | 0     | Vision refused                                                        |
| Cytosine vs Uracil    | Explanation       | 2     | Picked cytosine, explained lone pair availability                     |
| Histamine vs Imidazole| Baseline          | 0     | Refused                                                              |
| Histamine vs Imidazole| Stepwise          | 1     | Functional groups identified, no answer                               |
| Histamine vs Imidazole| Visual            | 0     | Refused image                                                         |
| Histamine vs Imidazole| Explanation       | 2     | Correctly identified and explained reactivity                         |
| Benzaldehyde vs Acid  | Baseline          | 0     | Refused                                                               |
| Benzaldehyde vs Acid  | Stepwise          | 1     | Talked about groups, no conclusion                                    |
| Benzaldehyde vs Acid  | Visual            | 0     | Refused                                                               |
| Benzaldehyde vs Acid  | Explanation       | 2     | Described nucleophilicity of aldehyde clearly                         |
| Nicotinamide vs Purine| Baseline          | 0     | Refused                                                               |
| Nicotinamide vs Purine| Stepwise          | 1     | N atom logic without final call                                       |
| Nicotinamide vs Purine| Visual            | 0     | Refused                                                               |
| Nicotinamide vs Purine| Explanation       | 2     | Described N availability, picked correctly                            |
| Furan vs Thiophene    | Baseline          | 0     | Refused                                                               |
| Furan vs Thiophene    | Stepwise          | 1     | Discussed atoms, avoided conclusion                                   |
| Furan vs Thiophene    | Visual            | 0     | Vision refusal                                                        |
| Furan vs Thiophene    | Explanation       | 2     | Explained polarizability and nucleophilic difference                  |

### Two-way Summary Table

| Image Pair            | Baseline | Stepwise | Visual | Explanation |
|-----------------------|----------|----------|--------|-------------|
| Ammonia vs Methanol   | 0        | 0        | 0      | 2           |
| MeNH₂ vs Aniline      | 0        | 1        | 0      | 2           |
| Imidazole vs Pyridine | 0        | 1        | 0      | 2           |
| Piperidine vs Morpholine | 0     | 1        | 0      | 2           |
| Acetate vs Methoxide  | 0        | 1        | 0      | 2           |
| Cytosine vs Uracil    | 0        | 1        | 0      | 2           |
| Histamine vs Imidazole| 0        | 1        | 0      | 2           |
| Benzaldehyde vs Acid  | 0        | 1        | 0      | 2           |
| Nicotinamide vs Purine| 0        | 1        | 0      | 2           |
| Furan vs Thiophene    | 0        | 1        | 0      | 2           |
