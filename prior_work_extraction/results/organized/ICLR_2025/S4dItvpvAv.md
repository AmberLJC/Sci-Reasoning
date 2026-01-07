# Prior Work Analysis Report

## Target Paper

**Title:** How to Find the Exact Pareto Front for Multi-Objective MDPs?

**Conference:** ICLR 2025 (spotlight)

**Authors:** Yining Li, Peizhong Ju, Ness Shroff

**Keywords:** Multi-objective optimization, Markov decision Process

**Abstract:** 
> Multi-Objective Markov Decision Processes (MO-MDPs) are receiving increasing attention, as real-world decision-making problems often involve conflicting objectives that cannot be addressed by a single-objective MDP. 
The Pareto front identifies the set of policies that cannot be dominated, providing a foundation for finding Pareto optimal solutions that can efficiently adapt to various preferences.
However, finding the Pareto front is a highly challenging problem. Most existing methods either (i...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**A Survey of Multi-Objective Sequential Decision-Making** (2013)
- *Authors:* Diederik M. Roijers et al.
- *Direct Connection:* This survey formalized the MO-MDP problem, distinguished the Pareto Coverage Set (PCS) from the Convex Coverage Set (CCS), and explicitly highlighted that existing methods either traverse a continuous preference space or restrict to deterministic policies—gaps this paper targets with an exact Pareto-front characterization.

**Multiple Objective Infinite-Horizon Discounted Markov Decision Processes** (1982)
- *Authors:* D. J. White
- *Direct Connection:* White’s vector-valued dynamic programming formulation and the connection between linear scalarization and supported efficient solutions provide the theoretical basis that this paper extends to derive the exact structure of the Pareto front.

**Constrained Markov Decision Processes** (1999)
- *Authors:* Eitan Altman
- *Direct Connection:* Altman’s occupancy-measure linear programming view and the sufficiency of stationary randomized policies under discounting underpin this paper’s polyhedral treatment of achievable return sets and the exact Pareto frontier.

**Markov Decision Processes: Discrete Stochastic Dynamic Programming** (1994)
- *Authors:* Martin L. Puterman
- *Direct Connection:* Puterman’s characterization of deterministic stationary policies as extreme points of the occupancy polytope grounds the finite extreme-structure insight that this paper leverages to enumerate all Pareto-extreme solutions and recover the full front.

### 🔍 Gap Identification

**Optimistic Linear Support for Multi-Objective Reinforcement Learning** (2014)
- *Authors:* Diederik M. Roijers et al.
- *Direct Connection:* OLS exemplifies weight-space traversal to approximate the CCS by solving scalarized MDPs, directly motivating this paper’s shift from continuous preference exploration to a finite, exact characterization of the full Pareto front.

**Multi-Objective Reinforcement Learning Using Sets of Pareto Dominating Policies** (2014)
- *Authors:* K. Van Moffaert et al.
- *Direct Connection:* By constructing sets of deterministic Pareto-dominating policies, this work underscored the inability of deterministic-only approaches to recover the full Pareto front, a limitation the current paper overcomes by characterizing and computing the entire frontier including randomized policies.

---

## Synthesis: How Prior Work Led to This Paper

Work on multi-objective sequential decision-making established the formal backbone for vector-valued returns and multi-criteria optimality in MDPs. White showed how vector-valued dynamic programming aligns with scalarizations, clarifying that linear weights recover only supported efficient solutions. Altman’s constrained MDP framework introduced the occupancy-measure linear program and proved that stationary randomized policies suffice under discounting, implying that attainable return sets are polyhedral images of an occupation-measure polytope. Puterman’s classic results tied deterministic stationary policies to extreme points of this polytope, sharpening the geometric structure of policy-induced returns. On the algorithmic side, Roijers’ survey distinguished the Pareto Coverage Set from the Convex Coverage Set and cataloged two dominant strategies: preference-space traversal via scalarization and deterministic set–based methods. OLS instantiated the former, iteratively solving scalarized MDPs to approximate the CCS by exploring continuous weight space. In contrast, Van Moffaert and Nowé advanced the latter by constructing sets of deterministic Pareto-dominating policies, but without a path to the full frontier that includes randomized mixtures. Together these works revealed a precise opportunity: combine the polyhedral, occupancy-measure view (which guarantees convex representability with randomized policies) with the insight that linear scalarization only touches supported points, and then go beyond weight exploration and deterministic sets. The present paper synthesizes these threads to identify a finite, exact structural characterization of the entire Pareto front for MO-MDPs and provides a dynamic-programming-compatible route to compute it without traversing a continuous preference space.

---

*Analysis generated on: 2026-01-06T13:27:54.481287*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
