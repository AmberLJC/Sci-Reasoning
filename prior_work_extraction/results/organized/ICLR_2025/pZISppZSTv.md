# Prior Work Analysis Report

## Target Paper
**Title:** pZISppZSTv
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

CLoSD’s core contribution—closing the loop between a text-driven diffusion planner and a physics-based RL controller—arises at the intersection of two mature lines of work. On the control side, DeepMimic established robust RL imitation of reference trajectories for physics-based characters, a template CLoSD adopts for its tracking controller. AMP and ASE advanced this paradigm to handle diverse, realistic motion and multi-skill settings via data-driven priors and modular skill abstractions, informing CLoSD’s emphasis on a simple, robust imitator capable of executing varied behaviors across tasks.
On the generative side, Human Motion Diffusion Model (MDM) demonstrated that diffusion can produce high-quality, text-conditioned motions, while HumanML3D/T2M provided the text–motion alignment and data needed to make motion generation promptable. CLoSD leverages this capability by converting diffusion from an offline sampler into a fast, autoregressive, on-the-fly planner that outputs short-horizon motion plans.
Crucially, Diffuser showed diffusion models can function as trajectory planners for sequential decision-making, directly motivating CLoSD’s use of diffusion as a universal planner. Complementarily, PhysDiff highlighted the benefits of injecting physics into diffusion-based motion synthesis; CLoSD extends this idea by creating a feedback loop in which a physics-based RL controller continuously tracks, evaluates, and implicitly corrects diffusion proposals during environment interaction. Together, these works enable CLoSD’s closed-loop, text-driven, multi-task character control that marries generative diversity with physical plausibility.

---
*Generated: 2026-01-07T00:02:04.905924*
