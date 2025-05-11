### 🥉 Nucleophilic Substitution (SN1/SN2)

#### Which molecule is more likely to undergo an SN1 reaction, and why?

| # | Molecule A             | Molecule B           | Correct Answer |
|------|------------------------|----------------------|----------------|
| 1    | Aniline.png            | Phenol.png           | second         |
| 2    | Paracetamol.png        | Morphine.png         | second         |
| 3    | Caffeine.png           | Adenine.png          | first          |
| 4    | Ibuprofen.png          | Salicylic-acid.png   | first          |
| 5    | Methanol.png           | Ethanol.png          | second         |
| 6    | Acetic-acid.png        | Benzoic_acid.png     | second         |
| 7    | Cyclohexane.png        | Benzene.png          | second         |
| 8    | Formic_acid.png        | Nitrobenzene.png     | second         |
| 9    | Pyridine_numbers.png   | Pyrrole-numbered.png | first          |
| 10   | Furan-full.png         | Thiophene-full.png   | second         |

---

## ✅ Final Selected Prompts for Task 4

| Prompt Type         | Final Selected Prompt                                                                                                                                           | Abbr. Reason for Chosen                                     |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **Baseline**        | "Which molecule is more likely to undergo an SN1 reaction, and why?" *(default)*                                                                                | Default phrasing; clean anchor for comparison                |
| **Stepwise**        | "Let’s evaluate both molecules for SN1 reactivity: (i) Leaving group ability, (ii) Carbocation stability, (iii) Steric accessibility. Then decide which is more favorable." | Best overall structure + highest consistent usability        |
| **Visual-First**    | "Identify any aromatic rings adjacent to the site of bond cleavage. Which molecule is better positioned to stabilize the resulting structure through resonance?" | One of few prompts that elicited molecule-specific logic     |
| **Explanation-First** | "The best SN1 substrates are those where the leaving group leaves easily, and the molecule can stabilize the resulting positive charge. Based on this, which one is a better candidate?" | Only expl-first prompt with 1 good + 4 partial completions   |
