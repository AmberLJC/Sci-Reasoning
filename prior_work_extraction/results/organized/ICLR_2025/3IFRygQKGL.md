# Prior Work Analysis Report

## Target Paper

**Title:** OptionZero: Planning with Learned Options

**Conference:** ICLR 2025 (oral)

**Authors:** Po-Wei Huang, Pei-Chiun Peng, Hung Guei, Ti-Rong Wu

**Keywords:** Option, Semi-MDP, MuZero, MCTS, Planning, Reinforcement Learning

**Abstract:** 
> Planning with options -- a sequence of primitive actions -- has been shown effective in reinforcement learning within complex environments. Previous studies have focused on planning with predefined options or learned options through expert demonstration data.
Inspired by MuZero, which learns superhuman heuristics without any human knowledge, we propose a novel approach, named *OptionZero*. OptionZero incorporates an *option network* into MuZero, providing autonomous discovery of options through ...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning** (1999)
- *Authors:* Richard S. Sutton et al.
- *Direct Connection:* OptionZero’s treatment of options and its dynamics modification follow the SMDP option model (initiation, intra-option policy, termination), enabling planning over temporally extended actions as single transitions in search.

**Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm** (2017)
- *Authors:* David Silver et al.
- *Direct Connection:* OptionZero inherits the AlphaZero-style self-play plus MCTS training paradigm and reinterprets actions in the search as learned options instead of only primitive moves.

### 💡 Inspiration

**The Option-Critic Architecture** (2017)
- *Authors:* Pierre-Luc Bacon et al.
- *Direct Connection:* OptionZero adopts the idea of learning option policies and termination functions end-to-end, but repurposes them for use inside MCTS and learns them via self-play signals rather than purely flat control.

**Value Prediction Network** (2017)
- *Authors:* Junhyuk Oh et al.
- *Direct Connection:* OptionZero generalizes VPN’s insight of learning abstract, option-like transition models for planning by embedding option-conditioned transitions into MuZero’s latent dynamics to look ahead farther under fixed simulation budgets.

### 📊 Baseline

**Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model** (2020)
- *Authors:* Julian Schrittwieser et al.
- *Direct Connection:* OptionZero directly builds on MuZero’s self-play training loop and learned policy–value–dynamics architecture, extending it by inserting an option network and modifying the dynamics to model option-conditioned (multi-step) transitions for MCTS.

### 🔗 Related Problem

**Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation** (2016)
- *Authors:* Tejas D. Kulkarni et al.
- *Direct Connection:* This work demonstrated that temporal abstraction improves long-horizon control (e.g., Atari), motivating OptionZero’s use of learned options to reduce branching and extend effective planning depth.

---

## Synthesis: How Prior Work Led to This Paper

MuZero established a powerful template that couples self-play with a learned policy–value–dynamics model, using MCTS to plan without human priors; however, its search operates over primitive actions and is constrained by simulation budgets. The options framework of Sutton, Precup, and Singh introduced semi-MDPs and formal option models—initiation sets, intra-option policies, and terminations—showing that temporally extended actions can be modeled as single transitions for planning. Option-Critic demonstrated that option policies and termination can be learned end-to-end from reward, removing the need for hand-engineered options and suggesting parameterizations suitable for neural learning. Value Prediction Network showed that learning abstract, option-like transition models enables multi-step lookahead in latent space, indicating a route to deeper planning through learned temporally extended dynamics. AlphaZero proved the effectiveness of self-play plus MCTS as a scalable training paradigm for decision-making systems. Hierarchical Deep RL (H-DQN) further evidenced that temporal abstraction can dramatically aid long-horizon tasks like Atari.
Together these works highlight a gap: self-play planning systems lacked temporal abstraction, while hierarchical methods with options rarely integrated with powerful model-based search or required handcrafting/demonstrations. OptionZero synthesizes MuZero’s self-play and MCTS with the SMDP option formalism and Option-Critic style learnable option parameterizations, and brings VPN’s idea of option-conditioned transitions into MuZero’s dynamics. This combination allows search over learned options to go deeper under the same simulation budget, naturally advancing the prior landscape.

---

*Analysis generated on: 2026-01-06T10:08:43.209224*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
