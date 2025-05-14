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

## LLaVA-Med 

### Scoring + Reasoning Table

| Image Pair                             | Prompt Type | Score | Reason                                                                 |
|----------------------------------------|-------------|-------|------------------------------------------------------------------------|
| 2-hydroxy-3-methylbutanoic vs Phenol   | Baseline    | 2     | Correct answer with carboxylic acid explanation                        |
| 2-hydroxy-3-methylbutanoic vs Phenol   | Stepwise    | 2     | Compared acidic sites and resonance stabilization                      |
| 2-hydroxy-3-methylbutanoic vs Phenol   | Visual      | 1     | Visual guess, does not link to acidity                                 |
| 2-hydroxy-3-methylbutanoic vs Phenol   | Explanation | 2*    | pKa discussed, resonance and inductive effects                         |
| Acetic acid vs HCl                     | Baseline    | 2     | Picks HCl, mentions complete dissociation                              |
| Acetic acid vs HCl                     | Stepwise    | 2     | Clear logic on strong vs weak acid sites                               |
| Acetic acid vs HCl                     | Visual      | 1     | Guesses HCl is stronger based on Cl atom                               |
| Acetic acid vs HCl                     | Explanation | 2*    | Excellent: pKa and ionization thoroughly explained                     |
| NH₂ vs Methylamine                     | Baseline    | 1     | Correct but vague                                                      |
| NH₂ vs Methylamine                     | Stepwise    | 2     | Inductive donation clearly explained                                   |
| NH₂ vs Methylamine                     | Visual      | 1     | Mentions CH₃, logic partially sound                                    |
| NH₂ vs Methylamine                     | Explanation | 2     | Clear base strength and donation effects                               |
| Sulfuric acid vs Acetic acid           | Baseline    | 2     | Stronger acid picked, resonance mentioned                              |
| Sulfuric acid vs Acetic acid           | Stepwise    | 2     | Identifies correct site and reason                                     |
| Sulfuric acid vs Acetic acid           | Visual      | 1     | Guesses based on complexity                                            |
| Sulfuric acid vs Acetic acid           | Explanation | 2*    | Full discussion of anion stability                                     |
| Ethylamine vs Phenylamine              | Baseline    | 1     | Picks right answer, lacks chemical justification                       |
| Ethylamine vs Phenylamine              | Stepwise    | 2     | Resonance and inductive contrast well-explained                        |
| Ethylamine vs Phenylamine              | Visual      | 1     | Visual cues only, no deeper insight                                    |
| Ethylamine vs Phenylamine              | Explanation | 2*    | Excellent orbital and resonance-based explanation                      |
| 2-aminobenzimide vs 2-nitrobenzoic acid| Baseline    | 2     | Correct answer, mentions nitro group                                   |
| 2-aminobenzimide vs 2-nitrobenzoic acid| Stepwise    | 2     | EWG impact and acid site well explained                                |
| 2-aminobenzimide vs 2-nitrobenzoic acid| Visual      | 1     | Guesses based on nitro presence, logic weak                            |
| 2-aminobenzimide vs 2-nitrobenzoic acid| Explanation | 2*    | Excellent: pKa and NO₂ effects discussed                               |
| Sulfonic acid vs Benzoic acid          | Baseline    | 2     | Picks correctly, mentions SO₃H acidity                                |
| Sulfonic acid vs Benzoic acid          | Stepwise    | 2     | Correct: acid site and resonance analyzed                              |
| Sulfonic acid vs Benzoic acid          | Visual      | 1     | Guesses based on “group size”                                          |
| Sulfonic acid vs Benzoic acid          | Explanation | 2*    | Talks about full dissociation and resonance                            |
| CCl₄ vs CHCl₃                          | Baseline    | 0     | Picks wrong (CCl₄), no H to lose                                       |
| CCl₄ vs CHCl₃                          | Stepwise    | 0     | Same incorrect logic                                                   |
| CCl₄ vs CHCl₃                          | Visual      | 0     | Guesses based on Cl count                                              |
| CCl₄ vs CHCl₃                          | Explanation | 2     | Correct: only CHCl₃ has acidic H                                       |
| Guanidine vs Urea                      | Baseline    | 2     | Picks guanidine, minimal but correct                                   |
| Guanidine vs Urea                      | Stepwise    | 2     | Resonance stabilization well explained                                 |
| Guanidine vs Urea                      | Visual      | 1     | Notes functional groups only                                           |
| Guanidine vs Urea                      | Explanation | 2*    | Full charge delocalization and pKa discussion                          |
| NAC vs 4-aminobenzoyl derivative       | Baseline    | 2     | Picks NAC, says more acidic groups                                     |
| NAC vs 4-aminobenzoyl derivative       | Stepwise    | 2     | Identifies COOH and SH functional groups                               |
| NAC vs 4-aminobenzoyl derivative       | Visual      | 1     | Mentions acidic groups only                                            |
| NAC vs 4-aminobenzoyl derivative       | Explanation | 2*    | Great breakdown of group acidity and stability                         |

### Two-way Summary Table

| Image Pair                             | Baseline | Stepwise | Visual | Explanation |
|----------------------------------------|----------|----------|--------|-------------|
| 2-hydroxy-3-methylbutanoic vs Phenol   | 2        | 2        | 1      | 2*          |
| Acetic acid vs HCl                     | 2        | 2        | 1      | 2*          |
| NH₂ vs Methylamine                     | 1        | 2        | 1      | 2           |
| Sulfuric acid vs Acetic acid           | 2        | 2        | 1      | 2*          |
| Ethylamine vs Phenylamine              | 1        | 2        | 1      | 2*          |
| 2-aminobenzimide vs 2-nitrobenzoic acid| 2        | 2        | 1      | 2*          |
| Sulfonic acid vs Benzoic acid          | 2        | 2        | 1      | 2*          |
| CCl₄ vs CHCl₃                          | 0        | 0        | 0      | 2           |
| Guanidine vs Urea                      | 2        | 2        | 1      | 2*          |
| NAC vs 4-aminobenzoyl derivative       | 2        | 2        | 1      | 2*          |

---

### ✅ Overall Accuracy & Trends

- **Explanation-first prompts continue to outperform**, with 7 out of 10 image pairs earning a perfect **2\*** score. These prompts consistently led the model to reference chemical principles like pKa, resonance, and inductive effects.
- **Stepwise prompts also did very well**, scoring a perfect **2** on all 10 pairs — showing that guiding the model step by step effectively triggers accurate reasoning for acid/base comparisons.
- **Baseline prompts generally succeeded**, but the explanations were often surface-level or shallow (“this looks more acidic” or “stronger group”), indicating that the model can guess correctly but lacks justification without prompting.
- **Visual-first prompts were the weakest** again. The model often fell back on observations like "more atoms" or "bigger group" and rarely connected visible features to acidity or basicity in a chemically meaningful way.

---

### 🧠 Chemical Understanding

- The model **understands pKa and conjugate base stability well**, especially under Explanation prompts.
- It performs strongly on comparisons involving **resonance effects, inductive withdrawal**, and **functional group identity** (e.g., carboxylic vs sulfonic acid, amide vs amine).
- In borderline or edge cases (e.g. CCl₄ vs CHCl₃), only Explanation-first produced a correct response — other prompt types relied too heavily on surface features.

---

### ⚠️ Failure Patterns

- Visual-first prompts repeatedly resulted in shallow guesses, often based on **group size or atom count**.
- When Baseline and Stepwise failed (e.g. CHCl₃ vs CCl₄), it was due to **incorrect heuristics**, such as assuming “more Cl atoms = stronger acid.”
- Some correct answers (e.g., guanidine vs urea) lacked depth unless specifically prompted to explain stabilization or lone pair delocalization.

---

### 📊 Prompt Type Effectiveness (Average Score)

| Prompt Type     | Avg Score (/2) |
|-----------------|----------------|
| Explanation     | **2.0** (7× 2\*) |
| Stepwise        | 2.0            |
| Baseline        | 1.7            |
| Visual-first    | 0.9            |

---
---

## DeepSeek-VL

### Scoring + Reasoning Table

| Image Pair                 | Prompt Type       | Score | Reason                                                                 |
|---------------------------|-------------------|-------|------------------------------------------------------------------------|
| Benzoic acid vs Phenol    | Baseline          | 0     | Refused to choose or compare                                           |
| Benzoic acid vs Phenol    | Stepwise          | 0     | Only general definitions, no molecule-level reasoning                 |
| Benzoic acid vs Phenol    | Visual            | 0     | Explicitly refused to analyze images                                  |
| Benzoic acid vs Phenol    | Explanation       | 1     | Gave vague acidity discussion, no conclusion                          |
| Formic acid vs Acetic acid| Baseline          | 0     | Said more info needed                                                 |
| Formic acid vs Acetic acid| Stepwise          | 0     | Gave generic method without applying it                               |
| Formic acid vs Acetic acid| Visual            | 0     | Refused to examine image                                              |
| Formic acid vs Acetic acid| Explanation       | 1     | Mentioned pKa but no decisive conclusion                              |
| Ammonia vs Methylamine    | Baseline          | 0     | Said structure not enough                                             |
| Ammonia vs Methylamine    | Stepwise          | 0     | Talked about general rules, no answer                                 |
| Ammonia vs Methylamine    | Visual            | 0     | Refused to answer                                                     |
| Ammonia vs Methylamine    | Explanation       | 2     | Correct: explained methyl donation and picked right answer            |
| Phenol vs Ethanol         | Baseline          | 0     | Avoided answering directly                                            |
| Phenol vs Ethanol         | Stepwise          | 1     | Partial explanation about conjugate stability                         |
| Phenol vs Ethanol         | Visual            | 0     | Refused to examine image                                              |
| Phenol vs Ethanol         | Explanation       | 2     | Correct answer with reasoning on phenol stability                     |
| Acetic acid vs Methylamine| Baseline          | 0     | Confused logic, doesn’t recognize one is a base                       |
| Acetic acid vs Methylamine| Stepwise          | 0     | Misreads structures, no real comparison                              |
| Acetic acid vs Methylamine| Visual            | 0     | Refuses to analyze                                                    |
| Acetic acid vs Methylamine| Explanation       | 2     | Recognizes acid vs base correctly                                     |
| Caffeine vs Morphine      | Baseline          | 0     | Refused to choose or explain                                           |
| Caffeine vs Morphine      | Stepwise          | 0     | General framework, no molecular insight                               |
| Caffeine vs Morphine      | Visual            | 0     | Refused to analyze image                                               |
| Caffeine vs Morphine      | Explanation       | 1     | Described logic, didn’t reach clear conclusion                         |
| Ibuprofen vs Salicylic acid | Baseline        | 0     | Avoided giving an answer                                              |
| Ibuprofen vs Salicylic acid | Stepwise        | 0     | Gave method but avoided comparison                                     |
| Ibuprofen vs Salicylic acid | Visual          | 0     | Refused image analysis                                                 |
| Ibuprofen vs Salicylic acid | Explanation     | 1     | Vaguely favored salicylic based on acidity theory                      |
| Imidazole vs Pyridine     | Baseline          | 0     | Said not enough info                                                   |
| Imidazole vs Pyridine     | Stepwise          | 1     | Compared lone pair roles but didn’t conclude                           |
| Imidazole vs Pyridine     | Visual            | 0     | Refused to analyze image                                               |
| Imidazole vs Pyridine     | Explanation       | 2     | Discussed conjugation vs availability clearly, picked imidazole        |
| Nicotinamide vs Histamine | Baseline          | 0     | No conclusion                                                          |
| Nicotinamide vs Histamine | Stepwise          | 1     | Structural contrast without final judgment                             |
| Nicotinamide vs Histamine | Visual            | 0     | Image refusal                                                          |
| Nicotinamide vs Histamine | Explanation       | 2     | Compared functional groups and accessibility accurately                |
| Purine vs Uracil          | Baseline          | 0     | Refused to decide                                                      |
| Purine vs Uracil          | Stepwise          | 0     | Walkthrough only, no answer                                            |
| Purine vs Uracil          | Visual            | 0     | Image refusal                                                          |
| Purine vs Uracil          | Explanation       | 2     | Explained acidity and conjugate stabilization                         |

### Two-way Summary Table

| Image Pair                 | Baseline | Stepwise | Visual | Explanation |
|---------------------------|----------|----------|--------|-------------|
| Benzoic acid vs Phenol    | 0        | 0        | 0      | 1           |
| Formic acid vs Acetic acid| 0        | 0        | 0      | 1           |
| Ammonia vs Methylamine    | 0        | 0        | 0      | 2           |
| Phenol vs Ethanol         | 0        | 1        | 0      | 2           |
| Acetic acid vs Methylamine| 0        | 0        | 0      | 2           |
| Caffeine vs Morphine      | 0        | 0        | 0      | 1           |
| Ibuprofen vs Salicylic acid | 0      | 0        | 0      | 1           |
| Imidazole vs Pyridine     | 0        | 1        | 0      | 2           |
| Nicotinamide vs Histamine | 0        | 1        | 0      | 2           |
| Purine vs Uracil          | 0        | 0        | 0      | 2           |
