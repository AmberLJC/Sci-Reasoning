# Prior Work Analysis Report

## Target Paper
**Title:** 53iSXb1m8w
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem** (1989)
- *Authors:* Michael McCloskey et al.
- *Connection:* Introduced the core phenomenon of catastrophic forgetting in sequential learning, which this paper identifies as the principal mechanism undermining RL fine-tuning when pre-trained capabilities are not revisited.

**Policy Distillation** (2015)
- *Authors:* Andrei A. Rusu et al.
- *Connection:* Establishes KL-based imitation of a teacher policy; the paper leverages this idea by distilling from the pre-trained policy during fine-tuning to explicitly retain pre-trained capabilities.

### 🔍 Gap Identification

**Progressive Neural Networks** (2016)
- *Authors:* Andrei A. Rusu et al.
- *Connection:* Demonstrates catastrophic forgetting in multi-task RL and addresses it via architectural isolation; the present paper pinpoints the same forgetting as the root cause of failed fine-tuning and shows it can be mitigated without added capacity.

### 🔧 Extension

**Overcoming Catastrophic Forgetting in Neural Networks** (2017)
- *Authors:* James Kirkpatrick et al.
- *Connection:* Provides the Fisher-based parameter-importance regularization (EWC) that the paper directly applies during RL fine-tuning to constrain drift from the pre-trained solution and mitigate forgetting on unvisited state subspaces.

**Learning without Forgetting** (2016)
- *Authors:* Zhizhong Li et al.
- *Connection:* Introduces distillation to a previous model as a knowledge-retention loss; the paper adopts an LwF-style KL/distillation from the pre-trained policy to preserve behavior on states not encountered early in fine-tuning.

**Continual Learning Through Synaptic Intelligence** (2017)
- *Authors:* Friedemann Zenke et al.
- *Connection:* Proposes path-integral–based parameter importance; the paper evaluates this class of synaptic-importance regularizers as a direct forgetting-mitigation mechanism for RL fine-tuning.

### 🔗 Related Problem

**Actor-Mimic: Deep Multitask and Transfer Reinforcement Learning** (2016)
- *Authors:* Emilio Parisotto et al.
- *Connection:* Uses distillation for RL transfer and highlights instability when naively fine-tuning across tasks; this work builds on that insight by framing fine-tuning failures as forgetting and enforcing retention of the pre-trained policy.

---

## Synthesis

The paper’s central insight—that failures in RL fine-tuning stem from catastrophic forgetting of pre-trained capabilities—rests on a lineage that begins with the foundational identification of catastrophic interference in sequential learning by McCloskey and Cohen. Translating that phenomenon into modern deep learning, Kirkpatrick et al.’s EWC and Zenke et al.’s Synaptic Intelligence established principled ways to quantify parameter importance and regularize updates to prevent forgetting. Li and Hoiem’s Learning without Forgetting and Rusu et al.’s Policy Distillation provided the complementary paradigm of knowledge distillation to a prior model, offering a direct and practical mechanism to preserve behavior while adapting to new objectives. In RL specifically, Rusu et al.’s Progressive Neural Networks highlighted how naive fine-tuning leads to forgetting and proposed architectural isolation to avoid interference—clearly surfacing the gap that forgetting, not merely optimization difficulty, is the culprit. Parisotto et al.’s Actor-Mimic further showed that distillation can enable transfer across RL tasks but that stability during adaptation is fragile without explicit retention pressures. Building on these threads, the current paper reframes RL fine-tuning as a forgetting-mitigation problem exacerbated by partial state visitation. It then directly deploys the above retention techniques—EWC/SI regularization and LwF-style distillation—to constrain drift from the pre-trained policy, demonstrating on NetHack and Montezuma’s Revenge that preserving behavior on unvisited subspaces is the key to unlocking the anticipated transfer gains.

---
*Generated: 2026-01-06T23:09:26.410018*
