# Prior Work Analysis Report

## Target Paper
**Title:** QpKWFLtZKi
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

EME’s core contribution is to rethink how novelty is measured for intrinsic rewards by focusing on an effective metric over adjacent states that is both dynamics-aware and scalable without episodic count scaling. This builds directly on two major lines of prior work. First, latent-space discrepancy methods such as ICM introduced measuring novelty via L1/L2 distances or prediction errors between successive states, and RIDE refined this by rewarding feature change while tempering it with episodic counts to avoid dithering. NGU and neural density approaches like Ostrovski et al. extended the count-based perspective with episodic and density-based novelty, proving effective on hard-exploration tasks but incurring significant memory/compute overhead and scaling issues. EME explicitly targets these limitations by removing reliance on episodic counts and proposing a more principled metric-based bonus.
The second line is bisimulation theory and practice. Ferns, Panangaden, and Precup established bisimulation metrics as the right notion of state similarity that respects transitions and rewards, suggesting a theoretically grounded metric for exploration. Practical deep variants (e.g., DeepMDP) attempted to learn such representations, but approximation gaps often reduced effectiveness in challenging domains. EME leverages the bisimulation intuition—novelty should reflect dynamics and rewards—while addressing the practical shortcomings of prior approximations. By unifying the strengths of discrepancy-based bonuses and bisimulation-aware representation learning, and by discarding episodic count scaling, EME delivers a scalable, effective exploration bonus tailored to hard-exploration settings.

---
*Generated: 2026-01-06T23:33:35.564917*
