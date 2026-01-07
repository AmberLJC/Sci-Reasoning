# Prior Work Analysis Report

## Target Paper
**Title:** qDAAMmGsGw
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Learning to Branch in Mixed Integer Programming** (2019)
- *Authors:* Maxime Gasse et al.
- *Connection:* Introduced the variable–constraint bipartite graph representation and learned embeddings for MILPs, which ACM-MILP leverages to define a latent space over constraints and their interrelations for adaptive selection and grouping.

**Modularity and community detection in bipartite networks** (2007)
- *Authors:* Michael J. Barber
- *Connection:* Provided the theoretical basis for detecting communities in bipartite graphs, which ACM-MILP applies to the constraint–variable bipartite structure to identify coherent constraint groups.

### 💡 Inspiration

**Generating SAT instances with community structure** (2016)
- *Authors:* Jordi Giráldez-Cru et al.
- *Connection:* Demonstrated that preserving and controlling community structure is key to hardness and realism in generated instances, directly inspiring ACM-MILP’s use of community detection to group strongly related constraints for collective modifications.

### 🔍 Gap Identification

**Machine Learning for Combinatorial Optimization: A Methodological Tour d’Horizon** (2021)
- *Authors:* Yoshua Bengio et al.
- *Connection:* Explicitly highlighted data scarcity and distribution shift issues in ML for CO/MILP, motivating ACM-MILP’s goal of hardness-preserving, structure-aware instance generation rather than simplistic random perturbations.

### 🔧 Extension

**Fast unfolding of communities in large networks** (2008)
- *Authors:* Vincent D. Blondel et al.
- *Connection:* Supplied a practical modularity-based community detection algorithm (Louvain) that ACM-MILP adapts to efficiently discover strongly related constraint groups for collective modification.

### 🔗 Related Problem

**Learning to Branch in Mixed Integer Programming** (2016)
- *Authors:* Elias B. Khalil et al.
- *Connection:* Established the precedent of exploiting problem structure and features in MILPs for learning, motivating ACM-MILP’s explicit modeling of constraint dependencies rather than random, structure-agnostic edits.

---

## Synthesis

ACM-MILP’s core innovation—adapting constraint modifications using a learned latent space while preserving constraint interrelations via community detection—rests on two direct pillars: learned structural representations of MILPs and the centrality of community structure for instance hardness. On the MILP side, Gasse et al. (2019) provided the variable–constraint bipartite graph view and learned embeddings that make it natural to embed constraints and reason about their relationships, a foundation ACM-MILP directly uses for probability-based, latent-space-driven constraint selection. Earlier, Khalil et al. (2016) established the value of exploiting problem structure and features in MILPs for learning-guided decisions, underscoring the inadequacy of structure-agnostic random edits that ACM-MILP replaces.

From the instance-generation perspective, Giráldez-Cru and Levy (2016) showed that preserving community structure is crucial to maintaining realism and hardness in generated SAT instances, directly inspiring ACM-MILP’s shift from single-constraint tweaks to community-aware, collective modifications. This is operationalized through community detection on the MILP’s bipartite graph: Barber (2007) provides the bipartite modularity framework and Blondel et al. (2008) the scalable Louvain algorithm, both of which ACM-MILP extends to identify strongly related constraints for grouped edits. Finally, Bengio et al. (2021) articulate the broader gap—data scarcity and distribution shift for ML4CO—providing the motivation for ACM-MILP’s hardness-preserving generation approach that advances beyond random perturbation baselines by explicitly modeling instance structure and interdependencies.

---
*Generated: 2026-01-06T23:09:26.465208*
