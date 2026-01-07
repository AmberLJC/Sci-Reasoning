# Prior Work Analysis Report

## Target Paper

**Title:** Problem-Parameter-Free Federated Learning

**Conference:** ICLR 2025 (oral)

**Authors:** Wenjing Yan, Kai Zhang, Xiaolu Wang, Xuanyu Cao

**Keywords:** Adaptive federated learning, problem-parameter free, arbitrary data heterogeneity, adaptive stepsize

**Abstract:** 
> Federated learning (FL) has garnered significant attention from academia and industry in recent years due to its advantages in data privacy, scalability, and communication efficiency. However, current FL algorithms face a critical limitation: their performance heavily depends on meticulously tuned hyperparameters, particularly the learning rate or stepsize. This manual tuning process is challenging in federated settings due to data heterogeneity and limited accessibility of local datasets. Conse...

---

## Key Prior Works (7 papers with direct influence)

### 🏗️ Foundation

**Communication-Efficient Learning of Deep Networks from Decentralized Data** (2017)
- *Authors:* H. Brendan McMahan et al.
- *Direct Connection:* Established the federated averaging paradigm and partial participation setting that the new algorithm operates within and seeks to improve upon under nonconvex objectives.

### 💡 Inspiration

**Stochastic Polyak Step-Size for SGD: Almost Sure Convergence** (2021)
- *Authors:* Konstantinos Loizou et al.
- *Direct Connection:* Provided a loss- and gradient-norm–based, problem-parameter-free adaptive stepsize (SPS/SPS+) that directly inspires the paper’s stepsize rule adapted to the federated, nonconvex setting.

**AdaGrad-Norm: Robust Stochastic Optimization to Noise Variance** (2019)
- *Authors:* Rachel Ward et al.
- *Direct Connection:* Showed that normalizing updates by accumulated gradient norms yields learning-rate robustness, a principle the paper leverages in designing a global stepsize that adapts without problem-specific tuning under partial participation.

### 🔍 Gap Identification

**Federated Optimization in Heterogeneous Networks (FedProx)** (2020)
- *Authors:* Tian Li et al.
- *Direct Connection:* Introduced a proximal correction to mitigate client drift under data heterogeneity but remained highly sensitive to the choice of stepsize and proximal coefficient, underscoring the need for problem-parameter-free methods.

**SCAFFOLD: Stochastic Controlled Averaging for Federated Learning** (2020)
- *Authors:* Sai Praneeth Karimireddy et al.
- *Direct Connection:* Addressed client drift via control variates but still required carefully tuned learning rates and algorithmic constants, highlighting the limitation of parameter sensitivity in heterogeneity-robust FL.

### 📊 Baseline

**Adaptive Federated Optimization** (2021)
- *Authors:* Sashank J. Reddi et al.
- *Direct Connection:* Proposed FedAdam/FedYogi, combining server momentum with adaptive preconditioning for FL; the new method retains this momentum+adaptivity template but removes dependence on problem-specific stepsize and momentum parameters.

### 🔗 Related Problem

**SlowMo: Improving Communication-Efficient Distributed SGD** (2020)
- *Authors:* Priya Goyal et al.
- *Direct Connection:* Demonstrated that server-side momentum stabilizes and accelerates local/periodic averaging methods, motivating the paper’s use of momentum but with automatically chosen, parameter-free momentum dynamics.

---

## Synthesis: How Prior Work Led to This Paper

Federated averaging introduced the core distributed learning protocol with local steps and partial participation, setting the stage for nonconvex training over heterogeneous clients. To counteract client drift from heterogeneity, FedProx added a proximal term, yet its success hinged on tuning both the stepsize and proximal coefficient. SCAFFOLD corrected drift using control variates, but similarly required carefully selected learning rates and algorithmic constants to realize its theoretical benefits. Moving toward adaptive optimization, Adaptive Federated Optimization (FedAdam/FedYogi) brought server-side momentum and adaptive preconditioning to FL, improving stability but remaining sensitive to global learning rate and momentum hyperparameters, especially under non-IID data and sporadic client participation. In parallel, the stochastic Polyak step-size (SPS/SPS+) offered a loss- and gradient-norm–based rule that dispenses with problem-specific parameters, while AdaGrad-Norm showed that normalizing by accumulated gradient norms yields robustness to noise without delicate learning-rate schedules. Complementing these, SlowMo established that server momentum can stabilize and accelerate decentralized/local-SGD style training under infrequent synchronization. Together, these works suggest that momentum and adaptive scaling are crucial for robust FL under heterogeneity, but prevailing methods still depend on problem-specific hyperparameters; meanwhile, parameter-free step-size rules exist in centralized stochastic optimization but had not been fused with FL’s aggregation and partial participation. The present work synthesizes these insights by coupling a problem-parameter-free, loss/gradient-norm–driven stepsize with automatically managed momentum at the server, preserving the heterogeneity robustness of adaptive federated optimizers while eliminating reliance on hand-tuned problem parameters and providing convergence guarantees in the nonconvex FL regime.

---

*Analysis generated on: 2026-01-06T18:01:08.979128*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
