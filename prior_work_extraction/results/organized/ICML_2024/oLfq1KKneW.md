# Prior Work Analysis Report

## Target Paper
**Title:** oLfq1KKneW
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Planning chemical syntheses with deep neural networks and symbolic AI** (2018)
- *Authors:* Marcus W. Segler et al.
- *Connection:* Established the modern formulation of retrosynthetic route planning as search guided by learned one-step models, which this paper adopts but augments with a route-level energy to optimize global, user-specified objectives.

**Reward Augmented Maximum Likelihood** (2016)
- *Authors:* Mohammad Norouzi et al.
- *Connection:* Introduces exponentiated-reward reweighting of a model’s distribution, the statistical mechanism the paper leverages by learning an energy (reward) that reshapes route probabilities toward desired global properties.

**Your Classifier is Secretly an Energy Based Model** (2019)
- *Authors:* Will Grathwohl et al.
- *Connection:* Grounds the EBM view that adding an energy term yields a log-linear composition with a base model; the proposed conditional residual EBM directly operationalizes this to compose a learned route-level energy with a probabilistic planner.

### 💡 Inspiration

**Direct Preference Optimization: Your Language Model Is Secretly a Reward Model** (2023)
- *Authors:* Yifan M. Rafailov et al.
- *Connection:* Provides the key preference-learning insight that an aligned policy arises from an exponential tilt of a reference model; the paper instantiates this by learning a conditional residual energy over full synthesis routes to tilt a base route distribution toward preferred criteria.

### 🔍 Gap Identification

**AiZynthFinder: a fast, robust and flexible open-source software for retrosynthetic planning** (2020)
- *Authors:* Anders Genheden et al.
- *Connection:* Represents widely used MCTS-based planners that expand using local scores and hand-crafted heuristics; its lack of principled, learnable control over route-level preferences is a gap directly addressed by the conditional residual EBM.

### 📊 Baseline

**Retro*: Learning Retrosynthetic Planning with Neural Guided A* Search** (2020)
- *Authors:* Chen et al.
- *Connection:* Serves as a primary baseline and target of improvement; unlike Retro*, which relies on heuristics/value functions without explicit preference control, the proposed method learns a residual energy to reweight route probabilities toward desired criteria (cost, yield, steps).

### 🔗 Related Problem

**Plug and Play Language Models: A Simple Approach to Controlled Text Generation** (2020)
- *Authors:* Siddharth Dathathri et al.
- *Connection:* Demonstrates post-hoc control of a base generator via an auxiliary scorer; the paper adopts this control-without-retraining principle by learning an energy over complete routes to steer generation according to preferences.

---

## Synthesis

The paper’s core contribution—controlling retrosynthetic route generation via a conditional residual energy that tilts a base probabilistic planner toward user-specified preferences—emerges from two converging lineages. From synthesis planning, Segler et al. established the modern framework of neural-guided search over retrosynthetic trees, later embodied in practical planners like AiZynthFinder and Retro*. These systems demonstrated the effectiveness of one-step models plus search, but also exposed a gap: route generation is dominated by local policies and handcrafted heuristics, offering little principled control over global objectives such as cost, yield, or step count. From learning-to-align generative models, Norouzi et al.’s Reward Augmented Maximum Likelihood introduced exponentiated-reward reweighting, and Rafailov et al.’s Direct Preference Optimization clarified that alignment can be achieved by an exponential tilt of a reference policy based on preferences. Grathwohl et al. provided the EBM formalism that makes this tilt a learned energy added to the base log-probability. Inspired by plug-and-play control in text generation (Dathathri et al.), the present work keeps the base retrosynthesis model while learning a conditional residual energy over entire routes, trained from preferences/criteria, to reshuffle probability mass toward globally superior syntheses. In doing so, it directly addresses the lack of lookahead-aware, preference-controllable route quality in Retro*/AiZynthFinder-style planners with a principled, learnable energy-based reweighting.

---
*Generated: 2026-01-06T23:09:26.501671*
