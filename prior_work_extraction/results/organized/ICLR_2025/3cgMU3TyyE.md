# Prior Work Analysis Report

## Target Paper

**Title:** Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space

**Conference:** ICLR 2025 (spotlight)

**Authors:** Zhiliang Chen, Xinyuan Niu, Chuan-Sheng Foo, Bryan Kian Hsiang Low

**Keywords:** Multi-turn Conversation Planning, Multi-turn LLM Optimization, MCTS, Semantic Space

**Abstract:** 
> Large language models (LLMs) are used in chatbots or AI assistants to hold conversations with a human user. In such applications, the quality (e.g., user engagement, safety) of a conversation is important and can only be exactly known at the end of the conversation. To maximize its expected quality, conversation planning reasons about the stochastic transitions within a conversation to select the optimal LLM response at each turn. Existing simulation-based conversation planning algorithms typica...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**POMDP-based statistical spoken dialog systems: A review** (2013)
- *Authors:* Steve J. Young et al.
- *Direct Connection:* This survey formalized dialog management as an MDP/POMDP with delayed, end-of-conversation rewards, the exact problem setup SCOPE adopts to plan multi-turn conversational decisions.

### 💡 Inspiration

**Dream to Control: Learning Behaviors by Latent Imagination (Dreamer)** (2019)
- *Authors:* Danijar Hafner et al.
- *Direct Connection:* SCOPE borrows Dreamer’s key insight of simulating future trajectories in a compact latent space to dramatically cut environment interactions, here replacing environment calls with imagined conversational rollouts in embedding space.

### 🔍 Gap Identification

**Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2023)
- *Authors:* Xuezhi Wang et al.
- *Direct Connection:* SCOPE explicitly addresses the computational burden highlighted by self-consistency’s need for many sampled rollouts by learning value estimates in semantic space to avoid majority-vote sampling at every turn.

### 📊 Baseline

**Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (2024)
- *Authors:* Shunyu Yao et al.
- *Direct Connection:* SCOPE directly targets ToT’s inference-time tree search that relies on expensive LLM rollouts at each node by replacing those rollouts with MCTS over a learned semantic transition model.

### 🔧 Extension

**Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (MuZero)** (2020)
- *Authors:* Julian Schrittwieser et al.
- *Direct Connection:* SCOPE adapts MuZero’s core recipe—MCTS over a learned latent dynamics and value model—to conversations by modeling stochastic conversational transitions in a dense semantic space.

### 🔗 Related Problem

**Graph of Thoughts: Solving Elaborate Problems with Large Language Models** (2023)
- *Authors:* Przemyslaw Besta et al.
- *Direct Connection:* SCOPE generalizes GoT’s structured exploration idea by operating in a continuous semantic state space rather than enumerating discrete thought graphs, thereby reducing the number of LLM queries required.

---

## Synthesis: How Prior Work Led to This Paper

Dialog management has long been cast as sequential decision making with delayed rewards, as established by the POMDP formulation for spoken dialog systems, which emphasizes planning under uncertainty and reward arriving only at conversation end. Tree of Thoughts introduced deliberate search over intermediate reasoning steps, expanding a decision tree with LLM-simulated rollouts to select better next actions, while Graph of Thoughts broadened this into graph-structured exploration; both achieved stronger solutions but at the cost of many expensive LLM calls. Self-consistency similarly improved reasoning by sampling multiple complete trajectories and aggregating via majority vote, reinforcing the empirical link between better outcomes and extensive rollouts. In contrast, model-based RL paved an efficient alternative: MuZero learned latent dynamics and value to plan with MCTS without querying the true environment, and Dreamer showed that “imagination” in a compact latent space can substitute for real interactions while preserving planning quality. Together these works revealed that discrete, rollout-heavy search improves decisions but is computationally prohibitive, whereas latent-space world models can enable efficient planning by simulating futures cheaply. Building on this, the present work models conversational transitions directly in a dense semantic space and runs MCTS atop learned dynamics and value, effectively translating ToT-style lookahead into MuZero/Dreamer-style latent planning for multi-turn conversations, thus maintaining decision quality while minimizing LLM queries.

---

*Analysis generated on: 2026-01-06T16:06:18.344479*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
