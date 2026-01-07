# Prior Work Analysis Report

## Target Paper
**Title:** skb34O7hFp
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Human-level control through deep reinforcement learning** (2015)
- *Authors:* Volodymyr Mnih et al.
- *Connection:* DQN defined the deep RL paradigm and network training setup in which the paper observes the buildup of dormant neurons; ReDo is designed to integrate into such value-based agents without altering the RL objective.

### 💡 Inspiration

**The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks** (2019)
- *Authors:* Jonathan Frankle et al.
- *Connection:* LTH established that (re)initialization can revive performant subnetworks; ReDo leverages this insight by reinitializing identified dormant neurons to restore representational capacity during RL training.

**RePr: Improved Training of Convolutional Filters** (2019)
- *Authors:* Aditya Prakash et al.
- *Connection:* RePr periodically drops and reinitializes underutilized filters to encourage better feature learning; ReDo generalizes this ‘reset’ philosophy beyond CNN filters to neurons in RL networks, guided by a dormancy criterion.

### 📊 Baseline

**Rainbow: Combining Improvements in Deep Reinforcement Learning** (2018)
- *Authors:* Matteo Hessel et al.
- *Connection:* Rainbow serves as a primary high-performance DQN baseline; the paper plugs ReDo into Rainbow and shows that recycling dormant neurons reduces inactivity and improves performance.

### 🔧 Extension

**Rigging the Lottery: Making All Tickets Winners** (2021)
- *Authors:* Utku Evci et al.
- *Connection:* RigL’s prune-and-grow training directly motivates ReDo’s idea of dynamically reallocating capacity; ReDo extends this by recycling at the neuron level using a dormancy signal (rather than weight magnitude/gradients) inside deep RL agents.

### 🔗 Related Problem

**Parameter Efficient Training of Deep Convolutional Neural Networks by Dynamic Sparse Reparameterization** (2019)
- *Authors:* Hesham Mostafa et al.
- *Connection:* Dynamic Sparse Reparameterization showed that periodically redistributing parameters via drop-and-grow improves learning; ReDo adopts the same principle—refreshing underutilized capacity—but triggers resets by detecting dormant neurons during RL training.

**Sparse evolutionary training: Training neural networks with dynamic sparse connectivity** (2018)
- *Authors:* Decebal C. Mocanu et al.
- *Connection:* SET’s prune-and-regrow (rewiring) mechanism inspired ReDo’s periodic ‘refresh’ of unused capacity; ReDo applies a similar evolutionary idea at the neuron granularity to counter neuron inactivity in deep RL.

---

## Synthesis

The core of The Dormant Neuron Phenomenon in Deep Reinforcement Learning is the recognition that deep RL networks progressively accumulate inactive units and that periodically ‘refreshing’ unused capacity can preserve expressivity and improve returns. This idea stands on two converging intellectual threads. First, dynamic sparse training demonstrated that capacity reallocation during training is beneficial: RigL introduced gradient-driven prune-and-grow, while Dynamic Sparse Reparameterization and Sparse Evolutionary Training showed that continual drop-and-grow or rewiring sustains learning by reallocating parameters. ReDo extends this thread by shifting the reallocation unit from connections to neurons and by using a principled dormancy signal (based on neuron inactivity) rather than weight magnitude or gradients, tailored to the dynamics of RL.
Second, prior work on resetting underutilized components showed that reinitialization can revitalize learning. The Lottery Ticket Hypothesis highlighted the power of initialization and (re)born subnetworks, and RePr demonstrated that periodically dropping and reinitializing weakly contributing filters improves feature learning in vision. ReDo generalizes this ‘rejuvenation’ intuition to RL by recycling dormant neurons throughout training.
Finally, the study is grounded in the deep RL setting introduced by DQN and exemplified by the strong Rainbow baseline, which provide the algorithmic context where dormancy emerges and where ReDo is evaluated. Together, these works directly catalyze ReDo’s neuron-level recycling mechanism for maintaining expressivity in deep RL.

---
*Generated: 2026-01-06T23:09:26.578407*
