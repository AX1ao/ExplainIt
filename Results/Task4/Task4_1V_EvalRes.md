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
