# Prior Work Analysis Report

## Target Paper

**Title:** Bayesian Optimization of Antibodies Informed by a Generative Model of Evolving Sequences

**Conference:** ICLR 2025 (spotlight)

**Authors:** Alan Nawzad Amin, Nate Gruver, Yilun Kuang, Yucen Lily Li, Hunter Elliott, Calvin McCarter, Aniruddh Raghu, Peyton Greenside, Andrew Gordon Wilson

**Keywords:** Bayesian optimization, generative model, antibody, biological sequence

**Abstract:** 
> To build effective therapeutics, biologists iteratively mutate antibody sequences to improve binding and stability. Proposed mutations can be informed by previous measurements or by learning from large antibody databases to predict only typical antibodies. Unfortunately, the space of typical antibodies is enormous to search, and experiments often fail to find suitable antibodies on a budget. We introduce Clone-informed Bayesian Optimization (CloneBO), a Bayesian optimization procedure that effic...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Navigating the protein fitness landscape with Gaussian processes** (2013)
- *Authors:* Romero et al.
- *Direct Connection:* This work established the experimental protein engineering framework of Bayesian optimization with Gaussian processes, which CloneBO adopts conceptually while replacing generic priors with a clone-informed generative model to propose mutations.

**partis: rapid and accurate inference of B-cell receptor clonal families** (2016)
- *Authors:* Ralph et al.
- *Direct Connection:* partis formalized and enabled large-scale inference of B-cell clonal families, providing the data structure and methodology that make training a clonal-family–aware generative model (CloneLM) feasible.

### 💡 Inspiration

**Mutation effects predicted from sequence co-variation** (2017)
- *Authors:* Hopf et al.
- *Direct Connection:* EVmutation demonstrated that evolutionary generative models provide strong priors for functional variants, directly inspiring CloneLM’s use of evolutionary signals—here, from clonal family trajectories—to bias mutation proposals toward fitness-improving changes.

### 🔍 Gap Identification

**Machine learning–assisted directed evolution for protein engineering** (2021)
- *Authors:* Wittmann et al.
- *Direct Connection:* By showing that ML-guided directed evolution can squander experimental budget when library design is not sufficiently targeted, this paper motivates CloneBO’s use of a clonal-family–aware generative prior to concentrate proposals on mutations most likely to improve function.

**Population-level inference of immune receptor selection (SONIA)** (2020)
- *Authors:* Sethna et al.
- *Direct Connection:* SONIA modeled repertoire-level generation and selection of BCRs but did not capture within-clone evolutionary trajectories, a limitation CloneBO addresses by learning a generative model explicitly from clonal families to guide optimization.

**AntiBERTa: antibody-specific language modeling for sequence representation** (2021)
- *Authors:* Ruffolo et al.
- *Direct Connection:* Antibody LMs like AntiBERTa showed that ‘naturalness’ priors from repertoire-wide training correlate with function but lack lineage context, motivating CloneBO’s lineage-informed LM to propose somatic-hypermutation–like, affinity-maturation–consistent edits.

### 🔧 Extension

**LaMBO: Language Model Bayesian Optimization for Biological Sequences** (2023)
- *Authors:* Daulton et al.
- *Direct Connection:* LaMBO introduced LM-guided Bayesian optimization over discrete sequences, and CloneBO extends this idea by training the language model on antibody clonal families and integrating it into the BO loop to emulate affinity maturation in the lab.

---

## Synthesis: How Prior Work Led to This Paper

Gaussian-process Bayesian optimization demonstrated that experimental protein engineering can be cast as a sample-efficient search over sequence space, with acquisition-driven proposals guiding lab rounds of mutation and measurement. Machine learning–assisted directed evolution then highlighted how model-guided libraries improve success rates, while also revealing that poorly targeted libraries waste scarce assays. Language-model–driven Bayesian optimization extended BO to discrete biological sequences by using a generative model to structure the proposal space. In parallel, evolutionary generative models such as EVmutation showed that unsupervised evolutionary constraints provide powerful priors for predicting fitness effects of mutations. Within immunology, repertoire models like SONIA captured VDJ generation biases and selection at the population level but did not model the stepwise, within-lineage dynamics of affinity maturation. Tools such as partis defined and inferred clonal families from repertoire sequencing, enabling large-scale datasets of related, evolving antibody sequences. Finally, antibody-specific language models (e.g., AntiBERTa) established that repertoire-trained LMs encode ‘naturalness’ signals correlated with expression and binding, yet they typically ignore lineage and antigen-driven evolutionary context. Together, these works expose a gap: BO for proteins is powerful but untailored to antibody affinity maturation; generative models provide strong priors but either operate on global repertoires or MSAs rather than clonal evolution; and MLDE needs targeted, budget-efficient libraries. The natural next step is to train a generative model directly on clonal families to internalize somatic hypermutation and selection patterns, and to embed that model within a BO loop so mutation proposals emulate immune optimization—thereby focusing experimental effort on lineage-consistent edits most likely to improve binding and developability under tight budgets.

---

*Analysis generated on: 2026-01-06T08:45:46.223143*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
