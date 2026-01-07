# Prior Work Analysis Report

## Target Paper
**Title:** Mwj57TcHWX
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

DiffTORI’s core contribution—using a differentiable trajectory optimizer as the policy representation and learning both dynamics and cost end-to-end—rests on two converging threads: differentiable optimization and objective-aligned model-based reinforcement learning. On the optimization side, OptNet and subsequent work on differentiable convex optimization layers established implicit differentiation through optimizers as a stable, general-purpose mechanism for embedding optimization inside neural architectures. Differentiable MPC then specialized this idea to control, showing that iLQR/MPC-style trajectory optimizers can be unrolled or implicitly differentiated to train parameters of costs and dynamics from task signals. These advances rely fundamentally on iLQR/DDP, which provides the structured trajectory optimization backbone (linearization/quadratization, backward pass) that makes efficient differentiation feasible.

On the RL side, PILCO and Stochastic Value Gradients demonstrated that learning and exploiting differentiable dynamics to directly optimize expected return addresses the objective mismatch inherent in purely predictive model learning. DiffTORI inherits this principle but channels gradients through the trajectory optimization process itself, aligning learned dynamics and costs with downstream task performance. Finally, Guided Policy Search highlighted the practical synergy between trajectory optimization and policy learning; DiffTORI internalizes this synergy by treating the optimizer as the policy, enabling end-to-end training for both reinforcement and imitation learning while preserving the structure and strong priors of trajectory optimization.

---
*Generated: 2026-01-07T00:02:04.759503*
