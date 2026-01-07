# Prior Work Analysis Report

## Target Paper
**Title:** KGt0F2yjBz
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The key contribution of Angles Don’t Lie is to replace heuristic curricula and uniform sampling in reinforcement fine-tuning with a model-intrinsic geometric signal—angle concentration—shown to correlate with gradient magnitude and thus with learnability. This builds directly on the RLHF/RFT regime popularized by InstructGPT, where PPO is the standard optimizer and uniform prompt sampling induces sample inefficiency. The authors’ idea of prioritizing data via the model’s own signal is a conceptual continuation of Prioritized Experience Replay, which improved RL sample efficiency by sampling proportional to TD-error, a learned signal of utility.
Curriculum and data selection research provides the methodological scaffolding. Self-Paced Learning demonstrated that curricula guided by the learner’s feedback (loss) outperform fixed heuristics, while GLISTER established that gradient/Fisher-informed selection yields efficient training by focusing on examples that most influence generalization. The present work advances this line by identifying a principled, computationally accessible proxy—angular concentration of token representations—that predicts gradient impact and can be used online during RFT.
Finally, representation geometry studies—particularly the discovery of anisotropy and narrow-cone angular structure in contextual embeddings—motivate angle concentration as a meaningful intrinsic statistic. Complementary evidence from example-level training dynamics (e.g., forgetting events) underscores that internal signals can expose example importance. Synthesizing these threads, GAIN-RL injects an angle-informed, gradient-driven scheduler into PPO-based RFT, yielding a theoretically grounded and practically effective route to training-efficient RL for LLMs.

---
*Generated: 2026-01-07T00:21:32.329574*
