# Prior Work Analysis Report

## Target Paper

**Title:** Submodular Reinforcement Learning

**Conference:** ICLR 2024 (spotlight)

**Authors:** Manish Prajapat, Mojmir Mutny, Melanie Zeilinger, Andreas Krause

**Keywords:** Reinforcement learning, Non-Markovian rewards, Submodular optimization, Policy gradient, Complex objectives in RL

**Abstract:** 
> In reinforcement learning (RL), rewards of states are typically considered additive, and following the Markov assumption, they are independent of states visited previously. In many important applications, such as coverage control, experiment design and informative path planning, rewards naturally have diminishing returns, i.e., their value decreases in light of similar states visited previously. To tackle this, we propose Submodular RL (subRL), a paradigm which seeks to optimize more general, no...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**An analysis of approximations for maximizing submodular set functions** (1978)
- *Authors:* G. L. Nemhauser et al.
- *Direct Connection:* subPO’s stepwise maximization of marginal gains is a direct incarnation of the classical greedy principle and guarantees from Nemhauser et al., transplanted into an RL policy-optimization procedure.

**Structured Solution Methods for Non-Markovian Decision Processes** (1997)
- *Authors:* Fahiem Bacchus et al.
- *Direct Connection:* The NMRDP framework formalizes history-dependent rewards, which this paper specializes by positing submodular set-based returns and then deriving complexity and learning algorithms in that setting.

### 💡 Inspiration

**Learning Submodular Functions over Sequences** (2017)
- *Authors:* Sebastian Tschiatschek et al.
- *Direct Connection:* Sequence submodularity’s diminishing-returns notion and greedy-by-marginal-benefit selection directly informed modeling rewards as submodular over visited-state histories and optimizing them via marginal-gain–driven updates.

### 🔍 Gap Identification

**Reward Machines: Exploiting Reward Function Structure in Reinforcement Learning** (2018)
- *Authors:* Rodrigo Toro Icarte et al.
- *Direct Connection:* Work on reward machines addresses non-Markovian rewards via automata but does not exploit diminishing-returns structure, motivating a formulation that explicitly models submodular, history-dependent rewards and algorithms tailored to their marginal gains.

### 🔧 Extension

**Adaptive Submodularity: Theory and Applications in Active Learning and Stochastic Optimization** (2011)
- *Authors:* Daniel Golovin et al.
- *Direct Connection:* The paper extends the adaptive greedy idea of maximizing expected marginal utility under uncertainty to MDPs by learning a policy that is greedy in marginal gains via policy gradients.

### 🔗 Related Problem

**The Submodular Orienteering Problem** (2005)
- *Authors:* Chandra Chekuri et al.
- *Direct Connection:* Results on maximizing submodular rewards along paths motivate the subRL formulation and hardness proofs, and underpin the use of greedy marginal gains as a planning heuristic in sequential decision settings.

---

## Synthesis: How Prior Work Led to This Paper

Classical submodular optimization established that monotone submodular objectives admit strong guarantees via greedy maximization of marginal gains, with Nemhauser, Wolsey, and Fisher showing the canonical 1−1/e approximation for set selection and thereby elevating marginal-gain–based search as the core design principle. Adaptive submodularity generalized this idea to sequential decision-making under uncertainty, with Golovin and Krause proving that an adaptive greedy policy that picks the action with maximum expected marginal utility remains near-optimal, thus linking stepwise marginal gains to policies. Submodular orienteering extended these rewards to paths, proving hardness and validating greedy heuristics in trajectory-like decisions where rewards accumulate submodularly along a route. In parallel, the NMRDP literature (Bacchus, Boutilier, and Grove) formalized non-Markovian rewards through state augmentation and automata-based methods, later operationalized in RL via reward machines (Icarte et al.), which capture temporal structure but not the diminishing-returns geometry. Finally, work on submodularity over sequences (Tschiatschek et al.) articulated diminishing returns on ordered actions and advocated greedy marginal-benefit selection in sequential settings. Together, these lines revealed a gap: non-Markovian rewards with explicit diminishing returns lacked an RL-native optimization method that operationalizes marginal gains over trajectories. By specializing NMRDPs to submodular set-valued returns and importing the adaptive-greedy marginal-gain principle, the paper naturally proposes a policy-gradient realization of greedy selection, establishes hardness relative to path-style problems, and delivers an algorithm aligned with the provable structure of submodularity.

---

*Analysis generated on: 2026-01-06T12:49:12.609745*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
