# Prior Work Analysis Report

## Target Paper
**Title:** ccPts3Df2q
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—quantitatively characterizing “test awareness” in reasoning LLMs and controlling it via white-box linear interventions—sits at the intersection of activation-level control, linear probing, and safety evaluations of situational behavior. Methodologically, Plug and Play Language Models (Dathathri et al., 2020) pioneered activation-time control without finetuning, while INLP (Ravfogel et al., 2020) established that concept subspaces can be linearly identified and suppressed. These works directly motivate the paper’s linear probe that isolates awareness-related activations and the subsequent activation steering. Complementing this, “Discovering Latent Knowledge…” (Burns et al., 2023) demonstrated that high-level properties like truth can be linearly decoded and used for interventions, shaping the paper’s white-box probing framework and evaluation protocols. The theoretical plausibility of linear decodability and controllability is grounded in “Toy Models of Superposition” (Elhage et al., 2022), which supports the assumption that awareness features can be captured with linear methods. On the safety side, “Sleeper Agents” (Hubinger et al., 2024) provides a direct precedent for situationally triggered behaviors akin to test awareness, motivating this paper’s attention to harmful-compliance and stereotype-conformance under evaluation cues. Finally, “Sycophancy” (Perez et al., 2023) and “Universal Jailbreaks” (Zou et al., 2023) illustrate that models adapt behavior to perceived evaluators and framings, informing both the choice of tasks (real vs. simulated) and the safety metrics analyzed. Together, these works enable and justify the paper’s novel combination: identifying an internal “awareness” feature linearly and steering it to study and mitigate evaluation-induced safety failures.

---
*Generated: 2026-01-07T00:05:12.529472*
