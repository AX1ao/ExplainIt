# 🧠 Task 4 (SN1SN2)

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

| Prompt/Pair   | Ani/Ph | Para/Mor | Caf/Ade | Ibu/Sal | MeOH/EtOH | Acid/Ben | Cycl/Benz | Form/Nitro | Pyr/Pyrr | Fur/Thio | Avg  |
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

