# Prior Work Analysis Report

## Target Paper
**Title:** wbs1fKLfOe
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Sparsified SGD with Memory** (2018)
- *Authors:* S. U. Stich et al.
- *Connection:* This work introduced the error-feedback (memory) mechanism that provably corrects the bias of sparse/biased compressors; Fed-EF adopts this EF mechanism on clients and extends its analysis to the federated, non-convex, and partially participating setting.

**Error Feedback Fixes SignSGD and other Gradient Compression Schemes** (2019)
- *Authors:* S. P. Karimireddy et al.
- *Connection:* By proving that error feedback eliminates bias and restores convergence for biased compressors (and that naive SignSGD can fail), this paper provides the core theoretical insight that Fed-EF generalizes to federated optimization with client sampling and data heterogeneity.

**Local SGD Converges Fast and Communicates Little** (2019)
- *Authors:* S. U. Stich
- *Connection:* This work formalized local updates with periodic averaging and established linear speedup; Fed-EF shows that, even with biased compression, error feedback preserves the same linear speedup guarantees in federated non-convex optimization with partial participation.

### 🔍 Gap Identification

**FedPAQ: A Communication-Efficient Federated Learning Method with Periodic Averaging and Quantization** (2020)
- *Authors:* A. Reisizadeh et al.
- *Connection:* FedPAQ analyzes quantized FL with client sampling but relies on (effectively) unbiased compression; Fed-EF explicitly addresses the open gap of biased compression in FL by combining it with error feedback and establishing fast non-convex convergence.

**signSGD: Compressed Optimization for Non-Convex Problems** (2018)
- *Authors:* J. Bernstein et al.
- *Connection:* As a canonical biased compression method, signSGD highlights both the appeal and pitfalls of biased gradients; Fed-EF is motivated by these limitations and uses error feedback to remedy the poor convergence of biased compression in federated settings.

### 📊 Baseline

**Communication-Efficient Learning of Deep Networks from Decentralized Data** (2017)
- *Authors:* H. B. McMahan et al.
- *Connection:* Fed-EF is built on the FedAvg-style federated optimization template and explicitly matches the full-precision FedAvg convergence rate under partial participation, making FedAvg the primary baseline this work aims to equal in accuracy with far less communication.

### 🔧 Extension

**EF21: A New, Simpler, Theoretically Better, and Practically Faster Error Feedback** (2021)
- *Authors:* E. Gorbunov et al.
- *Connection:* EF21 offers streamlined EF analyses and improved rates in (centralized/distributed) optimization; the present paper extends EF-style recursions and guarantees to the federated regime, proving full-precision-matching rates and linear speedup under partial participation.

---

## Synthesis

The core innovation of Li and Li is to bring the error-feedback (EF) principle—long known to debias compressed gradients—into the federated learning (FL) setting and to analyze it rigorously for non-convex objectives under partial participation. The FL template and the full-precision benchmark are set by FedAvg (McMahan et al.), whose local-update/periodic-averaging paradigm and random client sampling define the problem the authors aim to match in accuracy while reducing communication. The EF mechanism itself originates from sparsified SGD with memory (Stich et al.), which established how residual accumulation corrects the bias of compressors like Top-k. Karimireddy et al. then provided a unifying theory showing that EF fixes biased schemes, including SignSGD, and clarified why naive biased compression can fail—an insight the present paper transfers to federated optimization with heterogeneous data and client sampling.

Recent EF refinements, such as EF21 (Gorbunov et al.), offered simpler analyses and improved rates in centralized/distributed settings; Li and Li extend this line by proving that EF in FL can match full-precision FedAvg rates and achieve linear speedup with respect to the number of clients. On the FL-compression side, FedPAQ (Reisizadeh et al.) analyzed client-sampled FL with quantization but focused on unbiased compression, leaving a gap for biased compressors. By addressing this gap, and by showing why directly applying biased compression in FL converges poorly while EF restores fast convergence, the paper forges a direct bridge between EF theory and practical, communication-efficient federated training.

---
*Generated: 2026-01-06T23:09:26.519111*
