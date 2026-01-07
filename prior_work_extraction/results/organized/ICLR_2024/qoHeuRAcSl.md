# Prior Work Analysis Report

## Target Paper

**Title:** Grounding Language Plans in Demonstrations Through Counterfactual Perturbations

**Conference:** ICLR 2024 (spotlight)

**Authors:** Yanwei Wang, Tsun-Hsuan Wang, Jiayuan Mao, Michael Hagenow, Julie Shah

**Keywords:** Grounding LLM, Learning Mode Abstractions for Manipulation, Learning from Demonstration, Robotics, Task and Motion Planning

**Abstract:** 
> Grounding the common-sense reasoning of Large Language Models in physical domains remains a pivotal yet unsolved problem for embodied AI. Whereas prior works have focused on leveraging LLMs directly for planning in symbolic spaces, this work uses LLMs to guide the search of task structures and constraints implicit in multi-step demonstrations. Specifically, we borrow from manipulation planning literature the concept of mode families, which group robot configurations by specific motion constraint...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Sampling-Based Methods for Factored Task and Motion Planning** (2018)
- *Authors:* Caelan R. Garrett et al.
- *Direct Connection:* This work formalizes modes and mode families that group continuous robot configurations under shared discrete constraints, the exact abstraction this paper adopts to bridge language-level structure and low-level trajectories.

**Explanation-Based Learning: An Alternative View** (1986)
- *Authors:* Gerald DeJong and Raymond Mooney
- *Direct Connection:* The EBL principle of using domain constraints to explain why examples succeed or fail is instantiated here by training a differentiable model on counterfactual success/failure pairs to infer constraints that predict feasible trajectories.

### 💡 Inspiration

**Hindsight Experience Replay** (2017)
- *Authors:* Marcin Andrychowicz et al.
- *Direct Connection:* HER’s central idea of replay-based counterfactual relabeling directly inspires this paper’s synthetic perturbations of demonstrations to create paired successes and failures that supervise learning of task constraints.

### 🔍 Gap Identification

**Do As I Can, Not As I Say: Grounding Language in Robotic Affordances** (2022)
- *Authors:* Michael Ahn et al.
- *Direct Connection:* This work uses LLMs for high-level planning grounded by predefined skill affordances, highlighting the limitation that motivates this paper’s shift to discovering latent task constraints from demonstrations rather than relying on fixed skill sets.

**Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents** (2022)
- *Authors:* Huang et al.
- *Direct Connection:* By performing direct symbolic planning with LLMs, this paper illustrates weak physical grounding of plans, motivating the present work to use LLMs only to guide hypothesis search while grounding through demonstration-derived mode constraints.

### 🔗 Related Problem

**Logic-Geometric Programming: An Optimization-based Approach to Combined Task and Motion Planning** (2018)
- *Authors:* Marc Toussaint
- *Direct Connection:* By modeling manipulation as sequences of mode switches with explicit kinematic/physical constraints, this paper provides the concrete notion of constraint-governed segments that motivates representing demonstrations via mode-family structure.

---

## Synthesis: How Prior Work Led to This Paper

Work on task and motion planning established the notion that manipulation can be decomposed into modes—discrete contact/attachment structures with associated continuous constraint manifolds—and that families of such modes compactly group configurations sharing the same constraint template. In particular, sampling-based factored TAMP formalized modes and mode families as the backbone for search over constrained motion segments, while logic-geometric programming operationalized planning as sequences of mode switches governed by explicit geometric and kinematic constraints. Separately, hindsight experience replay showed that counterfactual relabeling of rollouts can transform failures into informative supervision signals by constructing alternative goal-consistent views of the same experience. Concurrently, language-enabled robotics explored using LLMs as planners: zero-shot planners demonstrated that LLMs can produce symbolic action sequences, and SayCan grounded LLM choices in affordance estimates over predefined skills—both effective but limited in discovering task-specific constraints from data. Finally, explanation-based learning articulated how examples can be generalized by explaining successes and failures with a domain theory of constraints. Together these strands expose a gap and a path forward: use LLMs not to output full plans, but to guide hypothesis search over latent task structure; represent that structure with mode-family abstractions that tie directly to physical constraints; and generate supervision by replaying demonstrations with synthetic perturbations to produce counterfactual successes and failures. By framing learning as explanation-based inference of constraints from these pairs, an end-to-end differentiable model can predict which trajectories satisfy the inferred mode-family constraints, thereby grounding language plans in physically executable behavior.

---

*Analysis generated on: 2026-01-06T09:16:42.857382*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
