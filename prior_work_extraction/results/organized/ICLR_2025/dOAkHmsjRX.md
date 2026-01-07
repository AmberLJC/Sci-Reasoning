# Prior Work Analysis Report

## Target Paper

**Title:** Budgeted Online Continual Learning by Adaptive Layer Freezing and Frequency-based Sampling

**Conference:** ICLR 2025 (spotlight)

**Authors:** Minhyuk Seo, Hyunseo Koh, Jonghyun Choi

**Keywords:** Continual Learning, Lifelong Learning, Efficient Training, Layer Freezing

**Abstract:** 
> The majority of online continual learning (CL) advocates single-epoch training and imposes restrictions on the size of replay memory. However, single-epoch training would incur a different amount of computations per CL algorithm, and the additional storage cost to store logit or model in addition to replay memory is largely ignored in calculating the storage budget. Arguing different computational and storage budgets hinder fair comparison among CL algorithms in practice, we propose to use float...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**On Tiny Episodic Memories in Continual Learning** (2019)
- *Authors:* Arslan Chaudhry et al.
- *Direct Connection:* This work formalized the online, single-epoch replay setting with a fixed-size buffer (typically via reservoir sampling), establishing the problem setup and baseline this paper evaluates under a unified FLOPs/Bytes budget and augments with frequency-based retrieval.

### 💡 Inspiration

**FreezeOut: Accelerate Training by Progressively Freezing Convolutional Layers** (2017)
- *Authors:* Andrew Brock et al.
- *Direct Connection:* FreezeOut showed that progressively freezing layers can cut training FLOPs with little accuracy loss, directly inspiring this paper’s adaptive, batch-informativeness-driven layer freezing tailored to online replay.

### 🔍 Gap Identification

**Learning to Learn without Forgetting by Maximizing Transfer and Minimizing Interference** (2019)
- *Authors:* Matthew Riemer et al.
- *Direct Connection:* By using meta-gradients and multiple inner updates per batch, this method exposed how 'single-epoch' protocols can mask large compute disparities across OCL algorithms, motivating the paper’s FLOPs-based budgeting for fair comparisons.

**Dark Experience for General Continual Learning** (2020)
- *Authors:* Paolo Buzzega et al.
- *Direct Connection:* DER/DER++ improved replay using stored logits, directly highlighting unaccounted auxiliary storage—precisely the memory overhead this paper’s Bytes-budget explicitly counts when comparing OCL methods.

### 📊 Baseline

**Online Continual Learning with Maximally Interfered Retrieval** (2019)
- *Authors:* Rahaf Aljundi et al.
- *Direct Connection:* MIR’s interference-driven buffer retrieval is a primary replay baseline that this paper replaces with a frequency-based sampler to equalize informational exposure under the same total resource budget.

### 🔗 Related Problem

**ER-ACE: Mitigating New-Class Overconfidence in Online Class-Incremental Learning** (2021)
- *Authors:* Lucas Caccia et al.
- *Direct Connection:* ER-ACE pinpointed new-class bias and leveraged class-aware mechanisms in replay, a limitation this paper addresses via frequency-based retrieval that balances exposure without incurring extra compute or memory.

---

## Synthesis: How Prior Work Led to This Paper

Online continual learning coalesced around a single-epoch, class-incremental replay protocol with tiny buffers, crystallized by Chaudhry et al., where reservoir-updated memories underpin simple, strong ER baselines. Riemer et al. then pursued meta-learning with replay to optimize transfer versus interference, but its multiple inner-loop updates per minibatch underscored that nominally similar protocols can hide major compute disparities. Aljundi et al. advanced retrieval with MIR, selecting high-interference samples from the buffer, while Buzzega et al. (DER/DER++) boosted performance by distilling from stored logits—both strategies improved accuracy yet introduced untracked costs, from extra gradient computations to auxiliary memory for logits. ER-ACE identified a complementary pain point: new-class overconfidence in the online regime, motivating class-aware replay treatments to re-balance exposure. Parallel to these CL developments, FreezeOut showed that progressively freezing layers can markedly reduce training FLOPs with limited accuracy loss, although its schedule was not conditioned on stream informativeness or replay dynamics. Together, these strands revealed an unmet need: a fair, unified accounting of computation and memory across OCL methods, and mechanisms that deliver competitive accuracy within a strict resource budget. Building directly on the replay setting, the paper formalizes budgets via FLOPs and Bytes, counters DER-style hidden storage, and replaces interference-centric retrieval with frequency-based sampling to equalize informational exposure. It adapts FreezeOut’s efficiency insight into an online context with batch-informativeness-driven layer freezing, achieving compute savings that respect the new budget while preserving accuracy.

---

*Analysis generated on: 2026-01-06T13:13:04.248571*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
