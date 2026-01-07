# Prior Work Analysis Report

## Target Paper
**Title:** iYzyTmd3Jd
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CooHOI’s core idea—decoupling cooperative humanoid manipulation into (1) single-agent human–object skill acquisition from motion priors and (2) subsequent multi-agent coordination via the manipulated object’s shared dynamics—emerges from two converging lines of work. On the single-agent side, DeepMimic established the recipe for learning physically plausible humanoid skills through motion-guided reinforcement learning, while AMP demonstrated how adversarially trained motion priors can scale imitation to complex, contact-rich behaviors. ASE then showed that such learned skills can be encapsulated as reusable, transferable policies, suggesting a clean stage-wise path from mastery of individual capabilities to broader task composition—exactly the scaffold CooHOI uses for its phase-one skill learning and phase-two transfer.
On the multi-agent side, canonical CTDE methods like MADDPG and value-factorization approaches like QMIX highlighted both the promise and the practical limitations of end-to-end multi-agent RL—credit assignment, instability, and sample inefficiency. CooHOI’s design explicitly sidesteps these pitfalls by first perfecting individual controllers and then coordinating them indirectly through the physics of the commonly manipulated object. This object-centric coordination philosophy is grounded in the relational reasoning paradigm introduced by Interaction Networks, which framed dynamics as interactions among entities. Finally, large-scale motion repositories such as AMASS make the first phase viable by providing rich motion priors. Together, these works directly shape CooHOI’s two-phase, object-dynamics–mediated approach to efficient, realistic cooperative human–object manipulation.

---
*Generated: 2026-01-06T23:33:36.286035*
