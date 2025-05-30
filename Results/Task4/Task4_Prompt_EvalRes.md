# 🧠 Task 4 (SN1SN2)

---

## 📊 Baseline Manual Scoring (0–2)

| Pair | Score | Summary |
|------|-------|---------|
| 1. Aniline vs Phenol | 0 | Completely hallucinates two different molecules (e.g., NH₂CH₂CH₂CH₂OH) not in the pair. |
| 2. Paracetamol vs Morphine | 0 | Generic rambling about electronegativity, no molecule comparison, ends in prompt-loop. |
| 3. Caffeine vs Adenine | 0 | Template spam about “ligand geometry” and “enzyme interactions.” No answer. |
| 4. Ibuprofen vs Salicylic acid | 0 | Massive repetition of “functional groups allow SN1 to occur.” No actual content. |
| 5. Methanol vs Ethanol | 0 | Broken loop: “amines vs amines” nonsense. No chemistry, no decision. |
| 6. Acetic acid vs Benzoic acid | 0 | Repetitive “planar functional group” gibberish. Infinite loop. |
| 7. Cyclohexane vs Benzene | 0 | Corporate-speak on “likelihood of SN reactions increasing daily.” No molecules discussed. |
| 8. Formic acid vs Nitrobenzene | 0 | Vague buzzwords like “geometry facilitates pathway.” No actual answer. |
| 9. Pyridine vs Pyrrole | 0 | Pure hallucination about “electrophidalders,” “endoaldors,” and “enozals.” |
| 10. Furan vs Thiophene | 0 | Word salad repeating “relevance to context” with zero comparison or SN1 logic. |

---

### ✅ Verdict

- **Total Score:** 0 out of 20  
- **Avg per Pair:** 0.0  

**Conclusion:** Baseline completions completely failed to address the question with relevant or real content.

---
---

## 📊 Stepwise Prompt Evaluation Summary (Prompts #1–20)

### 🧾 Manual Evaluation Overview

| Prompt # | Description (Abbreviated)                              | 2 (Good) | 1 (Partial) | 0 (Broken) | Notes                          |
|----------|---------------------------------------------------------|----------|-------------|------------|--------------------------------|
| 1        | LG → Carbocation → Decide                              | 1        | 2           | 7          | Best of early batch            |
| 2        | Stepwise: LG, C+ type, resonance                        | 1        | 1           | 8          | Format copied, logic missing   |
| 3        | Structure → Stability → Decide                         | 0        | 3           | 7          | All vague or fake              |
| 4        | Substitution site → Rank stabilities                   | 1        | 1           | 8          | Often template looped          |
| 5        | LG + C+ + sterics                                       | 0        | 2           | 8          | Heavily broken                 |
| 6        | Can it form C+? (resonance, tertiary)                  | 0        | 3           | 7          | Structure intact, weak content |
| 7        | LG? C+ stable? Compare                                  | 1        | 1           | 8          | Often restates prompt          |
| 8        | LG → Inductive/resonance → Choose                      | 0        | 2           | 8          | No real reasoning              |
| 9        | Examine: LG? C+ stable? SN1?                           | 1        | 0           | 9          | Only 1 usable output           |
| 10       | Solvent + LG + Stability                               | 0        | 1           | 9          | Mostly broken LaTeX            |
| 11       | Substitution → Ionization → C+ stability               | 0        | 0           | 10         | Fully broken                   |
| 12       | Site of ionization → Resonance/C+ analysis             | 0        | 2           | 8          | Weak phrasing effort           |
| 13       | LG → C+ → Sterics → Decide                             | 0        | 2           | 8          | Some structure, bad logic      |
| 14       | Isolate LG → Carbocation → Stabilization               | 0        | 1           | 9          | Mostly broken formatting       |
| 15       | LG? C+ type? Resonance? → Pick                         | 0        | 1           | 9          | Only 1 effortful response      |
| 16       | Substitution center → Carbocation → Decide             | 1        | 0           | 9          | Best single strong completion  |
| 17       | Simulate C+ → Assess via resonance                     | 1        | 2           | 7          | One great (MeOH/Ethanol)       |
| 18       | LG ease → C+ stability → Predict SN1                   | 0        | 1           | 9          | Generic phrasing or loops      |
| 19       | LG? → C+ class? → Resonance? → Decide                  | 0        | 3           | 7          | Several fluffy completions     |
| 20       | LG + C+ + Conditions → Decide                          | 0        | 3           | 7          | Most recent, lots of loops     |

---

## 📊 Stepwise Prompt Score Table (Manual Evaluation)

| Prompt/Pair   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Avg  |
|----------|-------------------|--------------------------|----------------------|------------------------------|----------------------|------------------------------|--------------------------|-----------------------------|----------------------|----------------------|------|
| Prompt 1 | 2                 | 1                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.4  |
| Prompt 2 | 2                 | 1                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.4  |
| Prompt 3 | 1                 | 1                        | 0                    | 0                            | 0                    | 1                            | 0                        | 0                           | 0                    | 1                    | 0.4  |
| Prompt 4 | 2                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.3  |
| Prompt 5 | 1                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.2  |
| Prompt 6 | 1                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.2  |
| Prompt 7 | 2                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.3  |
| Prompt 8 | 1                 | 1                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.3  |
| Prompt 9 | 2                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 0                    | 0.2  |
| Prompt10 | 1                 | 0                        | 1                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.3  |
| Prompt11 | 0                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 0                    | 0.0  |
| Prompt12 | 1                 | 0                        | 0                    | 0                            | 0                    | 1                            | 1                        | 0                           | 0                    | 0                    | 0.3  |
| Prompt13 | 1                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 1                    | 0                    | 0.2  |
| Prompt14 | 0                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 1                           | 0                    | 0                    | 0.1  |
| Prompt15 | 1                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 0                    | 0.1  |
| Prompt16 | 2                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 0                    | 0.2  |
| Prompt17 | 1                 | 0                        | 0                    | 0                            | 2                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.4  |
| Prompt18 | 1                 | 0                        | 0                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.2  |
| Prompt19 | 0                 | 0                        | 1                    | 0                            | 0                    | 1                            | 0                        | 0                           | 0                    | 1                    | 0.3  |
| Prompt20 | 1                 | 0                        | 1                    | 0                            | 0                    | 0                            | 0                        | 0                           | 0                    | 1                    | 0.3  |

---

### 🏆 Top Performing Prompts (Based on Manual Scoring)

1. **Prompt #1** – Most consistently solid output, especially early on.
2. **Prompt #16** – One genuinely strong and relevant answer with chemical accuracy.
3. **Prompt #17** – One strong and two decent attempts; best balance in the latter half.
4. **Prompt #19** – Several fluffy but structured answers; more potential than earlier ones.
5. **Prompt #4** – Steady format, occasionally led to structured reasoning.

---

### 🔍 Key Observations

- **Good prompts ≠ good completions** — many well-designed prompts triggered template repetition or hallucination.
- **Visual understanding seemed unreliable** — most correct answers came from simple or familiar cases (e.g., Aniline vs Phenol).
- **Prompt looping and degenerate output** was the most common failure mode (esp. in Prompts #5, #10, #15).
- **Only 5 completions scored 2/2 out of 200 total**, most from just 3 molecule pairs.
- Prompts that directly asked the model to “decide” at the end fared better than vague or fragmentary ones.
 heteroatom effects — which are central to predicting nucleophilic strength.

Ultimately, this task reaffirms that **prompt structure is not cosmetic** — it fundamentally alters how models think.

---
---

## 📊 Visual-First Prompt Evaluation Summary (Prompts #1–20)

### 🧾 Manual Evaluation Overview

| Prompt # | Description (Abbreviated)                                         | 2 (Good) | 1 (Partial) | 0 (Broken) | Notes                             |
|----------|--------------------------------------------------------------------|----------|-------------|------------|-----------------------------------|
| 1        | Scan structure → LG detachability                                 | 1        | 2           | 7          | Best of batch, flawed but real    |
| 2        | Shape/groups near center → Carbocation support                    | 0        | 1           | 9          | Mostly prompt repeats             |
| 3        | Focus on resonance structures visually                            | 0        | 3           | 7          | Weak logic, heavy looping         |
| 4        | Bonded atoms near site → Pos. charge stabilization                | 0        | 2           | 8          | Broken or echoes                  |
| 5        | Ring/conjugation near LG → Charge dispersal                       | 1        | 2           | 7          | One strong answer                 |
| 6        | Symmetry/planarity → Support delocalization                       | 0        | 2           | 8          | Mostly hallucinations or off-topic|
| 7        | Count lone pairs/electronegative groups visually                  | 0        | 1           | 9          | All but one were fully broken     |
| 8        | Check substitution near LG → Which is more substituted            | 1        | 0           | 9          | Only one meaningful comparison    |
| 9        | Compare rigidity → Less crowded = better SN1                      | 1        | 2           | 7          | Decent steric reasoning attempt   |
| 10       | Aromatic ring near LG → Resonance stabilization                   | 0        | 1           | 9          | Mostly nonsense or prompt echo    |
| 11       | Nearby heteroatoms → Can they stabilize charge?                   | 0        | 1           | 9          | Worst overall; mostly broken      |
| 12       | Exposure of LG site → Easier departure                            | 1        | 2           | 7          | Aniline–Phenol case stood out     |
| 13       | Electron-rich areas → Charge stabilization?                       | 0        | 2           | 8          | Prompt loops or fake chemistry    |
| 14       | Nearby pi/heteroatoms → Support delocalization                    | 1        | 2           | 7          | One good, rest were loops/echoes  |
| 15       | Geometry near LG → Spacious = better SN1                          | 0        | 1           | 9          | Only one vague steric logic       |
| 16       | Count rigid rings near LG → Flexibility helps SN1                 | 0        | 0           | 10         | Fully collapsed into spam         |
| 17       | Orbital overlap/lone pair nearby? → Stability                     | 0        | 1           | 9          | One hallucinated chemistry try    |
| 18       | Search for halogens/OH as leaving groups                          | 0        | 1           | 9          | Generic phrasing, no judgment     |
| 19       | Frameworks → Ion stability after LG leaves                        | 1        | 0           | 9          | One excellent, rest garbage       |
| 20       | Complexity/branching → Supports SN1 intermediate?                 | 1        | 2           | 7          | One strong, two OK, rest loops    |

---

### 📊 Visual-First Prompt Score Table (Manual Evaluation)

| Prompt/Pair   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Avg  |
|---------------|--------|----------|---------|---------|------------|-----------|------------|-------------|-----------|------------|-------|
| Prompt 1      | 1      | 2        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 1          | 0.4   |
| Prompt 2      | 0      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 1          | 0.1   |
| Prompt 3      | 0      | 1        | 0       | 0       | 0          | 0         | 1          | 0           | 0         | 1          | 0.3   |
| Prompt 4      | 1      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 1          | 0.2   |
| Prompt 5      | 2      | 0        | 0       | 0       | 0          | 0         | 0          | 1           | 0         | 1          | 0.4   |
| Prompt 6      | 0      | 1        | 0       | 0       | 1          | 0         | 0          | 0           | 0         | 0          | 0.2   |
| Prompt 7      | 1      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.1   |
| Prompt 8      | 2      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.2   |
| Prompt 9      | 2      | 0        | 0       | 0       | 0          | 0         | 1          | 0           | 0         | 1          | 0.4   |
| Prompt 10     | 1      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.1   |
| Prompt 11     | 1      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.1   |
| Prompt 12     | 2      | 0        | 0       | 0       | 0          | 0         | 0          | 1           | 0         | 1          | 0.4   |
| Prompt 13     | 1      | 1        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.2   |
| Prompt 14     | 2      | 1        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 1          | 0.4   |
| Prompt 15     | 1      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.1   |
| Prompt 16     | 0      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.0   |
| Prompt 17     | 1      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.1   |
| Prompt 18     | 0      | 0        | 0       | 1       | 0          | 0         | 0          | 0           | 0         | 0          | 0.1   |
| Prompt 19     | 2      | 0        | 0       | 0       | 0          | 0         | 0          | 0           | 0         | 0          | 0.2   |
| Prompt 20     | 2      | 0        | 0       | 0       | 1          | 1         | 0          | 0           | 0         | 0          | 0.4   |

---
### 🏆 Top Performing Visual-First Prompts (Based on Manual Scoring)

1. **Prompt #1** – Best overall balance of logic + decisiveness.
2. **Prompt #5** – Clear visual logic, one fully correct SN1 call.
3. **Prompt #9** – Reasoned about sterics and flexibility.
4. **Prompt #12** – Exposure logic worked well for Aniline vs Phenol.
5. **Prompt #19** – One excellent structured response.
6. **Prompt #20** – Reasoned about branching, complexity, and resonance.

---

### 🔍 Key Observations

- Prompts focusing on **explicit structural features** (resonance, branching, lone pairs) performed better than abstract prompts.
- **Most completions were either prompt echoes, hallucinated, or broken.**
- Visual-first logic **only succeeded when the image was simple** (e.g., Aniline vs Phenol).
- **Looping output, LaTeX corruption, and vagueness** were the most common failure modes.
- Across 200 completions, only **~5 truly strong answers** emerged.

---
---

## 📊 Explanation-First Prompt Evaluation Summary (Prompts #1–20)

### 🧾 Manual Evaluation Overview

| Prompt # | Description (Abbreviated)                                          | 2 (Good) | 1 (Partial) | 0 (Broken) | Notes                                    |
|----------|---------------------------------------------------------------------|----------|-------------|------------|------------------------------------------|
| 1        | Cation stability → Decide                                           | 0        | 4           | 6          | Several vague but structured completions |
| 2        | 2-step SN1 + resonance/EDG support                                 | 0        | 2           | 8          | Mostly template echoes                   |
| 3        | Cation stability → Structure-based                                 | 1        | 2           | 7          | One solid explanation (Aniline vs Phenol)|
| 4        | LG departure → Stable intermediate                                 | 0        | 1           | 9          | Total loops or empty filler              |
| 5        | LG ability + stabilize C+ → Decide                                 | 0        | 1           | 9          | One attempt, mostly hallucination        |
| 6        | Polar solvent benefit → Which molecule benefits?                   | 0        | 0           | 10         | Total collapse — surreal or broken       |
| 7        | Resonance/hyperconjugation → C+ stability → Choose                 | 0        | 1           | 9          | One tries SN1 logic, rest hallucinate    |
| 8        | Substitution pattern (3° > 2° > 1°)                                 | 0        | 2           | 8          | Several hallucinations or mismatches     |
| 9        | Benzylic/allylic stabilization                                     | 1        | 2           | 7          | Several say “yes” with no logic          |
| 10       | EWGs destabilize C+ → Analyze surroundings                         | 0        | 2           | 8          | Mostly broken loops, 2 vague nods        |
| 11       | Cation rearrangement potential                                     | 1        | 1           | 8          | Aniline vs Phenol good; rest default “Yes” |
| 12       | Sterics less relevant → Focus on cation stability                  | 0        | 1           | 9          | Prompt repeats or SN3 hallucinations     |
| 13       | Loss of electrons → Molecule resilience → SN1 likelihood           | 0        | 2           | 8          | A few gesture at logic, none complete    |
| 14       | LG leaves easily + charge stabilized → Best SN1 substrate          | 1        | 4           | 5          | One of the best overall                  |
| 15       | SN1 = non-concerted → LG leaves spontaneously → Which fits better? | 0        | 0           | 10         | Complete breakdown                       |
| 16       | π-systems / lone pairs → C+ stabilization                          | 0        | 3           | 7          | Weak, vague mentions of delocalization   |
| 17       | 3° C or resonance → SN1-prone?                                     | 1        | 1           | 8          | Only one good completion                 |
| 18       | Weaker base = better LG                                            | 0        | 1           | 9          | All others hallucinated H₂O or HCl       |
| 19       | Inductive effects → Stabilization context                          | 0        | 2           | 8          | Mostly repeats or off-topic              |
| 20       | Structure-based C+ support → Final judgment                        | 0        | 2           | 8          | Molecule fabrication and loops dominate  |

---

### 📊 Explanation-First Prompt Score Table (Manual Evaluation)

| Prompt/Pair   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Avg  |
|---------------|---|---|---|---|---|---|---|---|---|----|------|
| Prompt 1      | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1  | 0.4  |
| Prompt 2      | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0  | 0.2  |
| Prompt 3      | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0  | 0.3  |
| Prompt 4      | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0  | 0.1  |
| Prompt 5      | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0.1  |
| Prompt 6      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0.0  |
| Prompt 7      | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0.1  |
| Prompt 8      | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0  | 0.2  |
| Prompt 9      | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0.4  |
| Prompt 10     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1  | 0.2  |
| Prompt 11     | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1  | 0.3  |
| Prompt 12     | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0.1  |
| Prompt 13     | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0  | 0.2  |
| Prompt 14     | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1  | 0.6  |
| Prompt 15     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0.0  |
| Prompt 16     | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0  | 0.3  |
| Prompt 17     | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0.3  |
| Prompt 18     | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0.1  |
| Prompt 19     | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0  | 0.2  |
| Prompt 20     | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0  | 0.2  |

---

### 🏆 Top Performing Prompts (Based on Manual Scoring)

1. **Prompt #14** – Only one with 1 good and 4 partial completions.
2. **Prompt #3** – One good (Aniline vs Phenol) + two more usable ones.
3. **Prompt #9** – Clear prompt logic, 1 good + 2 partial.
4. **Prompt #1** – Several partially structured attempts.
5. **Prompt #17** – One strong decision, others weak but aligned.

---

### 🔍 Key Observations

- **Most completions ignored molecules entirely** or misread the structures.
- Even **clear chemistry prompts like EWG or carbocation rearrangement** triggered hallucinations or non-answers.
- **Only 3 completions scored 2/2** across 200 examples.
- **Prompt echoing, decision avoidance, and template loops** were the most common failure modes.
- Molecules like **Aniline vs Phenol** consistently received the best-quality completions.
