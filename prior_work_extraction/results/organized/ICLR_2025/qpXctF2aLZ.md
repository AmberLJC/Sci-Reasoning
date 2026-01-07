# Prior Work Analysis Report

## Target Paper
**Title:** qpXctF2aLZ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Proximal Policy Optimization Algorithms** (2017)
- *Authors:* John Schulman et al.
- *Connection:* SYMPOL plugs an axis-aligned, differentiable decision-tree policy into PPO’s clipped surrogate objective, directly leveraging PPO’s on-policy policy-gradient framework to optimize symbolic tree parameters end-to-end.

### 💡 Inspiration

**Reinforced Decision Trees** (2015)
- *Authors:* Mohammad Norouzi et al.
- *Connection:* SYMPOL adopts the core idea of treating internal tree routing as stochastic and training splits with policy gradients, extending this principle from supervised decision-tree training to sequential RL and integrating it with on-policy optimization.

**Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data** (2019)
- *Authors:* Sergei Popov et al.
- *Connection:* SYMPOL draws on the effectiveness of end-to-end gradient training of tree ensembles with soft gating from NODE, adapting the idea to axis-aligned, interpretable trees and optimizing them with policy-gradient signals in RL.

### 🔍 Gap Identification

**Distilling a Neural Network Into a Soft Decision Tree** (2017)
- *Authors:* Nicholas Frosst et al.
- *Connection:* SYMPOL explicitly avoids the two-stage distillation paradigm exemplified by soft decision trees, addressing the information loss from imitating a black-box teacher by directly optimizing the tree with RL returns.

### 📊 Baseline

**Verifiable Reinforcement Learning via Policy Extraction (VIPER)** (2018)
- *Authors:* Osbert Bastani et al.
- *Connection:* VIPER is a primary tree-policy baseline that extracts decision trees from neural policies via imitation, and SYMPOL improves on it by removing the extract-then-imitate step and optimizing the symbolic policy directly on-policy to mitigate information loss.

### 🔧 Extension

**Deep Neural Decision Forests** (2015)
- *Authors:* Peter Kontschieder et al.
- *Connection:* SYMPOL extends soft, differentiable split functions from neural decision forests to an RL setting, adapting them to interpretable, axis-aligned trees trained by policy gradients rather than supervised losses.

### 🔗 Related Problem

**Programmatically Interpretable Reinforcement Learning** (2018)
- *Authors:* Abhinav Verma et al.
- *Connection:* PIRL shares the goal of interpretable policies but relies on non-differentiable program synthesis, a limitation SYMPOL sidesteps by providing a differentiable, gradient-optimized symbolic (tree) policy within standard on-policy RL.

---

## Synthesis

SYMPOL’s core innovation—end-to-end, on-policy optimization of interpretable, axis-aligned decision-tree policies—emerges at the intersection of policy-gradient RL and differentiable decision-tree learning. PPO provides the foundational on-policy learning scaffold and clipped surrogate objective into which SYMPOL embeds a symbolic tree, enabling stable gradient-based updates of split thresholds and leaf action distributions. From the decision-tree side, soft, differentiable routing popularized by Deep Neural Decision Forests and later refined in NODE demonstrates how to parameterize splits for gradient descent; SYMPOL repurposes these ideas for RL objectives while maintaining strict axis alignment for interpretability. Reinforced Decision Trees contributes the crucial insight that tree routing can be treated as a stochastic policy and trained with policy gradients, an idea SYMPOL generalizes from supervised prediction to sequential decision-making with PPO. The paper directly responds to a prominent limitation in interpretable RL: methods like Frosst & Hinton’s soft-tree distillation and VIPER’s policy extraction achieve interpretability but incur information loss by imitating a separate neural teacher. By training the tree policy directly with returns rather than mimicking a black box, SYMPOL eliminates this bottleneck. Finally, compared to program-synthesis approaches such as PIRL—which achieve interpretability via non-differentiable search—SYMPOL preserves interpretability while remaining fully differentiable and compatible with standard on-policy RL pipelines.

---
*Generated: 2026-01-06T23:08:23.927998*
