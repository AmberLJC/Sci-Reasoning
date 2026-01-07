# Prior Work Analysis Report

## Target Paper

**Title:** Multi-Robot Motion Planning with Diffusion Models

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yorai Shaoul, Itamar Mishani, Shivam Vats, Jiaoyang Li, Maxim Likhachev

**Keywords:** Multi-Agent Planning, Robotics, Generative Models

**Abstract:** 
> Diffusion models have recently been successfully applied to a wide range of robotics applications for learning complex multi-modal behaviors from data. However, prior works have mostly been confined to single-robot and small-scale environments due to the high sample complexity of learning multi-robot diffusion models. In this paper, we propose a method for generating collision-free multi-robot trajectories that conform to underlying data distributions while using only single-robot data. Our algo...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Planning with Diffusion for Flexible Behavior Synthesis** (2022)
- *Authors:* Michael Janner et al.
- *Direct Connection:* Introduced trajectory-level diffusion modeling for control and planning, which MMD adopts at the single-robot level before adding multi-robot collision handling via search.

**Conflict-Based Search for Optimal Multi-Agent Pathfinding** (2015)
- *Authors:* Guni Sharon et al.
- *Direct Connection:* Established conflict-driven constraint search over individual paths, informing MMD’s high-level strategy to resolve robot-robot collisions as constraints while keeping per-robot motions data-driven.

### 💡 Inspiration

**Decision Diffuser: Offline Reinforcement Learning with Diffusion Models** (2022)
- *Authors:* Anurag Ajay et al.
- *Direct Connection:* Provided conditioning and guidance mechanisms for steering diffusion samples toward goals/constraints, which MMD leverages to condition single-robot diffusions on start/goal while enforcing inter-robot collisions through search.

**Learning Sampling Distributions for Robot Motion Planning** (2018)
- *Authors:* Brent Ichter et al.
- *Direct Connection:* Showed how learned generative models can guide classical planners while search enforces feasibility, a template MMD follows using diffusion-generated motions under search-imposed collision constraints.

### 🔍 Gap Identification

**Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** (2023)
- *Authors:* Xiao Ma Chi et al.
- *Direct Connection:* Established the effectiveness of training diffusion policies from single-robot demonstrations while highlighting the practical limitation to single-robot settings that MMD explicitly overcomes by scaling to multi-robot via search.

### 🔧 Extension

**Subdimensional Expansion for Multi-Robot Path Planning (M*)** (2015)
- *Authors:* Glenn Wagner and Howie Choset
- *Direct Connection:* Introduced the idea of planning independently per robot and coupling only in conflict regions, which MMD extends by replacing per-robot shortest-path planners with learned single-robot diffusion proposals.

**Compositional Visual Generation with Composable Diffusion Models** (2022)
- *Authors:* Mingyang Liu et al.
- *Direct Connection:* Proposed product-of-experts score composition to combine multiple diffusion models, which MMD adapts to compose several environment-specific diffusion models for scalable planning in large spaces.

---

## Synthesis: How Prior Work Led to This Paper

Trajectory diffusion for decision making established that generative models can synthesize feasible, multi-modal behaviors when trained on trajectory data, with Planning with Diffusion showing how to sample and refine trajectories for control. Decision Diffuser further demonstrated how conditioning and guidance could steer diffusion rollouts toward task objectives, and Diffusion Policy validated that single-robot action/trajectory diffusion learned from demonstrations can be robust and sample-efficient in robotics. In parallel, classical multi-robot planning developed principled ways to decouple and recouple agents: M* introduced subdimensional expansion that plans independently and only couples robots near conflicts, while Conflict-Based Search formalized resolving collisions as a high-level constraint search over individual plans. Bridging learning and search, Learning Sampling Distributions for Motion Planning showed learned generative priors can bias planners while search guarantees constraint satisfaction. Finally, Compositional Diffusion demonstrated that multiple diffusion models can be combined via score/product-of-experts composition to represent conjunctions of constraints or concepts.
Taken together, these works revealed a path to scalable multi-robot planning: use single-robot diffusion as powerful data-driven priors, rely on search to enforce hard inter-robot collision constraints without training a joint model, and compose multiple specialized diffusions to cover large, heterogeneous environments. The current paper synthesizes these insights by coupling per-robot diffusion generation with conflict-driven search in the spirit of M* and CBS, and by leveraging composable diffusion to scale across environment partitions—addressing the sample complexity and generalization limits that kept diffusion-based robotics largely confined to single-robot, small-scale settings.

---

*Analysis generated on: 2026-01-06T14:06:17.071063*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
