# Prior Work Analysis Report

## Target Paper

**Title:** The Complexity of Two-Team Polymatrix Games with Independent Adversaries

**Conference:** ICLR 2025 (oral)

**Authors:** Alexandros Hollender, Gilbert Maystre, Sai Ganesh Nagarajan

**Keywords:** algorithmic game theory, Nash equilibrium, minmax optimization

**Abstract:** 
> Adversarial multiplayer games are an important object of study in multiagent learning. In particular, polymatrix zero-sum games are a multiplayer setting where Nash equilibria are known to be efficiently computable. Towards understanding the limits of tractability in polymatrix games, we study the computation of Nash equilibria in such games where each pair of players plays either a zero-sum or a coordination game. We are particularly interested in the setting where players can be grouped into a...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Continuous Local Search** (2011)
- *Authors:* Constantinos Daskalakis and Christos Papadimitriou
- *Direct Connection:* The paper’s CLS framework provides the precise complexity class and proof template that this work leverages to show CLS-hardness for two-team polymatrix games (via reductions to finding stationary points).

**Team-maxmin equilibria of extensive-form games** (1997)
- *Authors:* Bernhard von Stengel and Daphne Koller
- *Direct Connection:* It formalizes team play with identical interests and independent (uncorrelated) strategies, providing the foundational team/independent-adversary model that this paper studies within polymatrix games.

**Graphical Models for Game Theory** (2001)
- *Authors:* Michael Kearns, Michael Littman, and Satinder Singh
- *Direct Connection:* This work introduces the graphical (pairwise) structure for multi-agent interactions that underlies polymatrix games, enabling the edge-wise zero-sum/coordination formulation used here.

### 🔍 Gap Identification

**Three-team polymatrix games are PPAD-complete** (2023)
- *Authors:* John Fearnley et al.
- *Direct Connection:* This result shows hardness for the three-team case and explicitly leaves the two-team complexity open, the precise gap this paper resolves by proving CLS-hardness (and tightness under independent adversaries).

### 🔧 Extension

**End of Potential Line** (2021)
- *Authors:* John Fearnley et al.
- *Direct Connection:* This work introduces the EOPL complete problem and associated reduction toolkit that the present paper directly adapts to encode potential-based continuous search subproblems when proving CLS-hardness.

### 🔗 Related Problem

**Zero-sum polymatrix games are tractable** (2011)
- *Authors:* Costis Daskalakis and Xi Chen (attributed line of work)
- *Direct Connection:* Results in this line establish that equilibria in zero-sum polymatrix games can be computed in polynomial time, forming the key tractable baseline that this paper departs from when mixing zero-sum and coordination edges.

---

## Synthesis: How Prior Work Led to This Paper

Continuous Local Search delineates a complexity class for continuous potential-driven problems and provides a reduction template that captures stationary-point computations; this framework underpins arguments that equilibrium computation can be as hard as finding first-order critical points. End of Potential Line refines this perspective with a canonical complete problem and practical gadgets for encoding potential improvements along discrete paths, offering a versatile engine for CLS-hardness reductions. Team-maxmin equilibria formalize games with teams of identical interests that act independently, clarifying how a team’s inability to correlate constrains feasible strategies and equilibrium notions. Graphical Models for Game Theory introduces the pairwise interaction structure that polymatrix games instantiate, enabling edge-wise decomposition into distinct bilateral interactions. Finally, work establishing the tractability of zero-sum polymatrix games identifies a notable efficient frontier: multi-player settings remain solvable when every edge is antagonistic. Alongside this, hardness for three-team polymatrix games shows where tractability breaks down, explicitly posing the two-team case as an open complexity gap. Together, these works set the stage: the graphical/polymatrix format specifies the model, team-maxmin defines independent teams, and zero-sum tractability marks the baseline, while CLS/EOPL provide the hardness machinery. The remaining gap—two-team games mixing coordination and zero-sum edges, and the special case with independent adversaries—naturally invites a CLS-focused reduction proving hardness yet revealing tight tractability boundaries for the independent-adversary variant.

---

*Analysis generated on: 2026-01-06T15:49:08.211367*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
