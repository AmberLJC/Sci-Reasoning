# Prior Work Analysis Report

## Target Paper
**Title:** c16m2kUTLZ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Provable Defenses via the Convex Outer Adversarial Polytope** (2018)
- *Authors:* Eric Wong et al.
- *Connection:* This work formalized certified robustness as bounding worst-case outputs under perturbations via convex relaxations; our paper critiques the assumption that such real-number bounds translate to guarantees for floating-point deployments.

**Interval Analysis** (1966)
- *Authors:* Ramon E. Moore
- *Connection:* Moore’s interval arithmetic is the theoretical basis for interval and symbolic-interval verifiers; we prove that—even when intervals yield sound real-valued bounds—practical floating-point soundness can still fail.

### 💡 Inspiration

**What Every Computer Scientist Should Know About Floating-Point Arithmetic** (1991)
- *Authors:* David Goldberg
- *Connection:* Goldberg’s exposition of rounding and non-associativity directly motivates our construction of adversarial networks that detect and exploit floating-point execution order and precision to mislead sound-on-paper verifiers.

### 📊 Baseline

**AI2: Safety and Robustness Certification of Neural Networks with Abstract Interpretation** (2018)
- *Authors:* Timon Gehr et al.
- *Connection:* AI2 established interval/abstract-interpretation-based, theoretically sound certification for neural networks—a class of methods our paper proves does not guarantee practical (floating-point) soundness and empirically demonstrates can be misled.

**On the Effectiveness of Interval Bound Propagation for Training Verifiably Robust Models** (2018)
- *Authors:* Srinivas Gowal et al.
- *Connection:* IBP is the canonical interval-analysis variant for DNNs that our theoretical results explicitly target, showing that bounding real-valued outputs via intervals does not ensure bounds for deployed floating-point executions.

**Neurify: Efficient Neural Network Verification** (2018)
- *Authors:* Shiqi Wang et al.
- *Connection:* Neurify’s symbolic-interval approach represents a key interval-based verifier that our paper shows can be defeated by networks exploiting floating-point operation order/precision, highlighting the theoretical–practical soundness gap.

### 🔗 Related Problem

**Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks** (2017)
- *Authors:* Guy Katz et al.
- *Connection:* Reluplex set the standard for exact DNN verification under real arithmetic; our results expose how such guarantees can fail to reflect actual floating-point behavior at deployment time.

---

## Synthesis

The core innovation of this paper is to separate theoretical soundness (bounding a network’s real-valued outputs) from practical soundness (bounding the actual floating-point outputs realized on deployed systems), and to show that today’s ‘sound’ verifiers fail at the latter. This thesis sits squarely on the lineage of interval and relaxation-based verification. AI2 and its abstract-interpretation framework, together with IBP and symbolic-interval methods like Neurify, operationalized interval analysis for neural networks and popularized claims of soundness when computing bounds with floating-point arithmetic. Our results prove that such approaches, although theoretically sound for real-number semantics, do not guarantee practical soundness for IEEE-754 execution and can be systematically deceived.
Convex relaxation methods exemplified by Wong and Kolter’s convex outer adversarial polytope formalized certified robustness as bounding worst-case outputs under perturbations, yet—like exact verifiers such as Reluplex—implicitly reason in real arithmetic. We show that the guarantees derived under these assumptions may not hold for deployed floating-point inference, especially in stochastic or implementation-dependent environments. The conceptual mechanism enabling our counterexamples traces to foundational numerical analysis: Moore’s interval analysis provides the bounding calculus these verifiers rely on, while Goldberg’s classic account of rounding error and non-associativity inspires our adversarial networks that detect and exploit operation ordering and precision. Taken together, these works directly define the problem, supply the dominant methods and benchmarks, and expose (through their assumptions) the precise gap our paper formalizes and empirically validates.

---
*Generated: 2026-01-06T23:07:19.574326*
