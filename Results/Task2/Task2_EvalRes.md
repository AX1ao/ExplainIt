# 🧠 Task 2 (Acid-Base Strength Prediction)

---
## OneVision

### Scoring + Reasoning Table

| Image Pair                    | Prompt Type       | Score | Reason                                                                 |
|------------------------------|-------------------|-------|------------------------------------------------------------------------|
| Benzoic acid vs Phenol       | Baseline          | 2     | Correct answer, says benzoic acid stabilizes conjugate base            |
| Benzoic acid vs Phenol       | Stepwise          | 2     | Stepwise ID of COOH group, mentions resonance                         |
| Benzoic acid vs Phenol       | Visual            | 1     | Notes carbonyl and OH, but logic is unclear                           |
| Benzoic acid vs Phenol       | Explanation       | 2*    | Explains inductive and resonance effects clearly                      |
| Formic acid vs Acetic acid   | Baseline          | 2     | Correct, says smaller molecule is stronger acid                       |
| Formic acid vs Acetic acid   | Stepwise          | 2     | Compares substituents' effect on acidity                              |
| Formic acid vs Acetic acid   | Visual            | 2     | Observes CH₃ vs H and concludes correctly                             |
| Formic acid vs Acetic acid   | Explanation       | 2*    | Details methyl as EDG, explains stability                             |
| Ammonia vs Methylamine       | Baseline          | 1     | Correct molecule but logic is muddled                                 |
| Ammonia vs Methylamine       | Stepwise          | 2     | Identifies site, discusses methyl donation                            |
| Ammonia vs Methylamine       | Visual            | 1     | Sees CH₃, assumes stronger base, no deep reasoning                    |
| Ammonia vs Methylamine       | Explanation       | 2     | Good reasoning about lone pair donation                               |
| Phenol vs Ethanol            | Baseline          | 2     | Correct answer, not much justification                                |
| Phenol vs Ethanol            | Stepwise          | 2     | Compares OH group acidity and resonance stabilization                 |
| Phenol vs Ethanol            | Visual            | 1     | Notes aromatic ring, guesses phenol is more acidic                    |
| Phenol vs Ethanol            | Explanation       | 2*    | Strong discussion of phenoxide ion and delocalization                 |
| Acetic acid vs Methylamine   | Baseline          | 2     | Picks acid, mentions functional group                                 |
| Acetic acid vs Methylamine   | Stepwise          | 2     | Describes acid-base comparison using group behavior                   |
| Acetic acid vs Methylamine   | Visual            | 1     | Mentions group types, reasoning minimal                               |
| Acetic acid vs Methylamine   | Explanation       | 2*    | Explains why COOH is more acidic than NH₂                            |
| Caffeine vs Morphine         | Baseline          | 2     | Picks morphine, notes nitrogen presence                               |
| Caffeine vs Morphine         | Stepwise          | 2     | Identifies protonation sites, good structure comparison               |
| Caffeine vs Morphine         | Visual            | 1     | Guesses based on “more groups”                                        |
| Caffeine vs Morphine         | Explanation       | 2*    | Explains lone pair accessibility and solvation                       |
| Ibuprofen vs Salicylic acid  | Baseline          | 2     | Picks correctly, says “smaller acid group”                           |
| Ibuprofen vs Salicylic acid  | Stepwise          | 2     | Compares functional groups, good conclusion                          |
| Ibuprofen vs Salicylic acid  | Visual            | 1     | Notes COOH and ring, reasoning shallow                                |
| Ibuprofen vs Salicylic acid  | Explanation       | 2*    | Excellent discussion of conjugation and EDG                          |
| Imidazole vs Pyridine        | Baseline          | 1     | Picks correctly but gives shallow “extra nitrogen” reason             |
| Imidazole vs Pyridine        | Stepwise          | 2     | Compares ring lone pair involvement                                   |
| Imidazole vs Pyridine        | Visual            | 1     | Mentions N atoms, logic unclear                                       |
| Imidazole vs Pyridine        | Explanation       | 2     | Good explanation of lone pair delocalization vs availability          |
| Nicotinamide vs Histamine    | Baseline          | 1     | Picks histamine, logic is generic                                     |
| Nicotinamide vs Histamine    | Stepwise          | 2     | Identifies amines vs amide structure                                  |
| Nicotinamide vs Histamine    | Visual            | 1     | Mentions more groups, doesn’t explain basicity                        |
| Nicotinamide vs Histamine    | Explanation       | 2     | Correct: discusses amide deactivation vs free NH₂                    |
| Purine vs Uracil             | Baseline          | 2     | Picks uracil, mentions resonance vaguely                              |
| Purine vs Uracil             | Stepwise          | 2     | Compares acidic sites and conjugate stability                         |
| Purine vs Uracil             | Visual            | 1     | Visual guess based on ring size                                       |
| Purine vs Uracil             | Explanation       | 2*    | Correct: charge delocalization in uracil explained well              |

### Two-way Summary Table

| Image Pair                    | Baseline | Stepwise | Visual | Explanation |
|------------------------------|----------|----------|--------|-------------|
| Benzoic acid vs Phenol       | 2        | 2        | 1      | 2*          |
| Formic acid vs Acetic acid   | 2        | 2        | 2      | 2*          |
| Ammonia vs Methylamine       | 1        | 2        | 1      | 2           |
| Phenol vs Ethanol            | 2        | 2        | 1      | 2*          |
| Acetic acid vs Methylamine   | 2        | 2        | 1      | 2*          |
| Caffeine vs Morphine         | 2        | 2        | 1      | 2*          |
| Ibuprofen vs Salicylic acid  | 2        | 2        | 1      | 2*          |
| Imidazole vs Pyridine        | 1        | 2        | 1      | 2           |
| Nicotinamide vs Histamine    | 1        | 2        | 1      | 2           |
| Purine vs Uracil             | 2        | 2        | 1      | 2*          |

---

### ✅ Overall Accuracy & Trends

- **Explanation-first prompts dominate** again — 6 out of 10 earned a perfect **2\***, showing that LLaVA performs best when explicitly guided through reasoning.
- **Stepwise prompts were consistently solid**, scoring 2s across all 10 image pairs. The structured thinking seems to help the model reason through acid/base chemistry reliably.
- **Baseline prompts often guessed correctly**, but lacked chemical detail or gave shallow reasons (e.g., “smaller group,” “more atoms”), indicating surface-level pattern matching.
- **Visual-first prompts performed the worst**, rarely earning more than 1 point. The model’s vision seemed limited to **counting atoms or identifying groups** without connecting them to acidity/basicity.

---

### 🧠 Chemical Understanding

- The model **understands conjugate base stabilization** in acidic comparisons (e.g., phenol vs ethanol, benzoic vs phenol), especially under Explanation-first.
- It reliably identifies **electron-donating vs withdrawing effects** when prompted stepwise or explicitly, but **rarely applies this insight spontaneously** under Baseline or Visual-first.
- For basicity (e.g., methylamine, imidazole, histamine), LLaVA can recognize **lone pair accessibility** as a factor — again, only when prompted directly.

---

### 📌 Failure Modes

- **Visual-first** prompts caused the model to default to:
  > "It has more groups" / "It has more atoms"  
  without linking visible structure to chemical behavior.
- Baseline often succeeded **only when the comparison was familiar or obvious**, failing in subtler cases like ammonia vs methylamine.
- The model struggles with **amide vs amine** distinctions and the effect of ring conjugation on basicity unless prompted.

---

### 📊 Prompt Type Effectiveness (Average Score)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **2.0** (6× 2\*) |
| Stepwise        | 2.0            |
| Baseline        | 1.6            |
| Visual-first    | 1.0            |

---

### 🔧 Recommendations

- Use **Explanation-first** prompts for any chemistry task involving subtle reasoning or functional group effects.
- Stepwise prompts are **excellent for teaching or tutoring** as they align closely with how chemists reason through acidity/basicity.
- Avoid relying on visual-only cues unless the task is extremely simple — the model’s visual reasoning appears shallow for functional group interactions.

---
---
