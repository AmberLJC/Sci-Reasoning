# Prior Work Analysis Report

## Target Paper

**Title:** Entity-Centric Reinforcement Learning for Object Manipulation from Pixels

**Conference:** ICLR 2024 (spotlight)

**Authors:** Dan Haramati, Tal Daniel, Aviv Tamar

**Keywords:** deep reinforcement learning, visual reinforcement learning, object-centric, robotic object manipulation, compositional generalization

**Abstract:** 
> Manipulating objects is a hallmark of human intelligence, and an important task in domains such as robotics. In principle, Reinforcement Learning (RL) offers a general approach to learn object manipulation. In practice, however, domains with more than a few objects are difficult for RL agents due to the curse of dimensionality, especially when learning from raw image observations. In this work we propose a structured approach for visual RL that is suitable for representing multiple objects and t...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**An Object-Oriented Representation for Efficient Reinforcement Learning** (2008)
- *Authors:* Carlos Diuk et al.
- *Direct Connection:* This work formalized factoring MDP state into objects with attributes and relations, which the paper instantiates in a deep, pixel-based entity-centric architecture for multi-object manipulation.

**Universal Value Function Approximators** (2015)
- *Authors:* Tom Schaul et al.
- *Direct Connection:* The paper adopts the UVFA formulation of goal-conditioned value/policy learning and extends it by conditioning on structured, entity-level goal representations that include inter-object dependencies.

**Deep Sets** (2017)
- *Authors:* Manzil Zaheer et al.
- *Direct Connection:* Its permutation-invariant set encoder provides the architectural principle used to aggregate variable-size sets of object entities and underpins the paper’s compositional generalization guarantee to more objects.

### 💡 Inspiration

**Relational Deep Reinforcement Learning** (2018)
- *Authors:* Vinicius Zambaldi et al.
- *Direct Connection:* This work introduced attention-based relational reasoning over entity pairs in RL, which the paper adapts to model object–object interactions needed for dependency-aware manipulation from pixels.

**Object-Centric Learning with Slot Attention** (2020)
- *Authors:* Francesco Locatello et al.
- *Direct Connection:* The slot-based mechanism for unsupervised object discovery from images is leveraged to extract a fixed-capacity set of entity tokens that feeds the paper’s entity-centric RL module.

### 🔍 Gap Identification

**Reward Machines: Exploiting Reward Function Structure in Reinforcement Learning** (2019)
- *Authors:* Rodrigo Toro Icarte et al.
- *Direct Connection:* By handling goal dependencies via explicit automata but requiring symbolic structure, this work highlights a gap that the paper fills by learning dependency-aware, entity-conditioned goals directly from pixels.

### 🔗 Related Problem

**Graph Networks as Learnable Physics Engines for Inference and Control** (2018)
- *Authors:* Alvaro Sanchez-Gonzalez et al.
- *Direct Connection:* It demonstrated that message passing over object graphs enables accurate multi-object control, motivating the paper’s entity-graph policy/value design to capture interactions during manipulation.

---

## Synthesis: How Prior Work Led to This Paper

Object-oriented RL established that factoring state into objects with attributes and relations yields sample efficiency and generalization, motivating representations that reason at the entity level. Universal Value Function Approximators framed control as goal-conditioned value learning, enabling policies to generalize across goal spaces via goal inputs. Deep Sets provided a principled way to process variable-size sets with permutation invariance, ensuring architectures can scale to more objects without changing parameters. Relational Deep RL showed that attention over entity pairs lets agents reason about interactions crucial for control, while graph-based physics engines demonstrated that message passing over object graphs enables accurate multi-object prediction and control. Slot Attention introduced a practical route to extract a small set of object slots directly from pixels in a self-supervised manner, yielding entity tokens with which downstream reasoning modules can operate. Reward Machines, in turn, captured goal dependencies through automata, but relied on symbolic task structure and supervision. Taken together, these works suggest a path: parse images into entities, reason relationally over a permutation-invariant set, and condition value/policy on structured goals. The remaining opportunity is to support dependency-structured goals directly from pixels while retaining combinatorial generalization. By combining slot-based entity perception with a Deep Sets–style, relationally enhanced goal-conditioned value/policy, and by grounding dependencies in entity-conditioned goals rather than external automata, the current work naturally extends these foundations to multi-object manipulation that trains on a few objects yet generalizes to many.

---

*Analysis generated on: 2026-01-06T15:27:00.593114*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
