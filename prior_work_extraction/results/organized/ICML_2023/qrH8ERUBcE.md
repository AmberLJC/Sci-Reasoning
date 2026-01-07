# Prior Work Analysis Report

## Target Paper
**Title:** qrH8ERUBcE
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning** (1999)
- *Authors:* Richard S. Sutton et al.
- *Connection:* HRMs are operationalized by treating each RM call as an option, relying explicitly on the options framework’s initiation/termination and temporally extended actions to learn each subtask independently.

**Decision-Theoretic Planning with Non-Markovian Rewards** (2006)
- *Authors:* Sylvie Thiébaux et al.
- *Connection:* RMs build on the NMRDP tradition formalizing rewards as history-dependent automata; HRMs inherit and extend this foundation to hierarchical, callable reward machines.

### 💡 Inspiration

**Reinforcement Learning with Hierarchies of Machines** (1998)
- *Authors:* Ronald Parr et al.
- *Connection:* The core idea of empowering an automaton to invoke subroutines mirrors HAMs; HRMs adapt this call/return semantics from hierarchical controllers to the reward-function automaton setting.

**Statecharts: A Visual Formalism for Complex Systems** (1987)
- *Authors:* David Harel
- *Connection:* HRMs import the hierarchical finite-state-machine notion—states that encapsulate nested machines and callable substructures—directly from the Statecharts paradigm.

### 🔍 Gap Identification

**Compositional Reinforcement Learning from Logical Specifications** (2021)
- *Authors:* Nimrod Jothimurugan et al.
- *Connection:* This work showed how flat automata from temporal logic can guide options but lacked hierarchical callable structure; HRMs address this gap by enabling nested RM calls for deeper abstraction.

### 📊 Baseline

**Reward Machines: Exploiting Reward Function Structure in Reinforcement Learning** (2019)
- *Authors:* Rodrigo Toro Icarte et al.
- *Connection:* Hierarchies of Reward Machines directly extends the RM formalism by adding callable submachines; the paper’s empirical baseline and the notion of a flat, automaton-structured reward come from this work.

### 🔗 Related Problem

**Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition** (2000)
- *Authors:* Thomas G. Dietterich
- *Connection:* MAXQ established the efficiency of hierarchical decomposition; HRMs achieve analogous benefits by decomposing the reward specification (via RM calls) rather than the value function directly.

---

## Synthesis

The core innovation in Hierarchies of Reward Machines (HRMs) is to endow the reward-machine formalism with callable submachines, enabling hierarchical abstraction over the reward structure itself. This directly builds on Reward Machines by Toro Icarte et al., which introduced flat automaton-structured rewards and Q-learning schemes over them; HRMs generalize that baseline by permitting nested calls, creating reusable subtask specifications. To exploit these call-based subtasks, HRMs lean on the options framework (Sutton et al.), treating each RM call as an option with its own initiation and termination—making the hierarchical reward decomposition learnable with off-the-shelf option-based RL. The callable-automaton idea is inspired by hierarchical controllers, notably Hierarchical Abstract Machines (Parr & Russell), and by Statecharts (Harel), which pioneered hierarchical finite-state machines with subroutine-like semantics; HRMs adapt these notions specifically to reward-specification automata. Prior compositional RL from logical specifications (Jothimurugan et al.) demonstrated that flat automata can guide option construction but did not provide hierarchical callable structure, a gap HRMs explicitly fill to improve scalability and reuse. Finally, the non-Markovian reward literature (Thiébaux et al.) provides the theoretical foundation for representing history-dependent rewards via automata, a lineage from which RMs—and thus HRMs—directly descend. Together, these works establish the formal, hierarchical, and learning machinery that HRMs integrate and extend.

---
*Generated: 2026-01-06T23:09:26.540976*
