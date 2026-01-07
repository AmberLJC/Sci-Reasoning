# Prior Work Analysis Report

## Target Paper

**Title:** Enhancing Learning with Label Differential Privacy by Vector Approximation

**Conference:** ICLR 2025 (spotlight)

**Authors:** Puning Zhao, Jiafei Wu, Zhe Liu, Li Shen, Zhikun Zhang, Rongfei Fan, Le Sun, Qingming Li

**Keywords:** label differential privacy

**Abstract:** 
> Label differential privacy (DP) is a framework that protects the privacy of labels in training datasets, while the feature vectors are public. Existing approaches protect the privacy of labels by flipping them randomly, and then train a model to make the output approximate the privatized label. However, as the number of classes K increases, stronger randomization is needed, thus the performances of these methods become significantly worse. In this paper, we propose a vector approximation approac...

---

## Key Prior Works (6 papers with direct influence)

### 🏗️ Foundation

**Randomized Response: A Survey Technique for Eliminating Evasive Answer Bias** (1965)
- *Authors:* S.L. Warner
- *Direct Connection:* The scalar label-flipping paradigm used in label-LDP baselines is a direct instantiation of Warner’s randomized response, which this paper departs from by emitting a K-dimensional privatized vector rather than a single flipped label.

### 💡 Inspiration

**RAPPOR: Randomized Aggregatable Privacy-Preserving Ordinal Response** (2014)
- *Authors:* Úlfar Erlingsson et al.
- *Direct Connection:* RAPPOR introduced emitting privatized bit vectors (rather than a single category) under LDP, directly inspiring the idea that vectorized outputs can retain more information than scalar label flips.

**Semi-supervised Knowledge Transfer for Deep Learning from Private Training Data (PATE)** (2017)
- *Authors:* Nicolas Papernot et al.
- *Direct Connection:* PATE established that training on privatized soft-label distributions (probability vectors) preserves more task-relevant information than hard labels, informing the choice to target expectation-aligned label vectors under local label DP.

### 📊 Baseline

**Extremal Mechanisms for Local Differential Privacy** (2016)
- *Authors:* Peter Kairouz et al.
- *Direct Connection:* k-ary randomized response (GRR) from this work is the standard mechanism for privatizing multi-class labels under LDP and suffers utility degradation as K grows, which the proposed vector approximation is designed to overcome.

### 🔧 Extension

**Locally Differentially Private Protocols for Frequency Estimation** (2017)
- *Authors:* Tianhao Wang et al.
- *Direct Connection:* Unary Encoding and Optimized Unary Encoding (OUE) show that K-dimensional privatized vectors yield markedly better accuracy for large-domain categorical estimation, an idea extended here to supervised learning by privatizing labels as vectors whose expectations encode class probabilities.

### 🔗 Related Problem

**Hadamard Response: Estimating Distributions Efficiently under Local Privacy** (2019)
- *Authors:* Jayasree Acharya et al.
- *Direct Connection:* Hadamard Response demonstrates that structured K-dimensional sketches can dramatically improve K-scaling under LDP, motivating the use of structured vector outputs instead of scalar responses for categorical data.

---

## Synthesis: How Prior Work Led to This Paper

Randomized response provides the canonical mechanism for privatizing a categorical value by flipping a single symbol, and k-ary randomized response (GRR) formalizes this for multi-class settings under local differential privacy. While optimal in certain senses, GRR’s variance grows with the alphabet size, making accuracy deteriorate as the number of classes increases. In contrast, RAPPOR pioneered the idea of emitting privatized bit vectors that aggregate more information than a single flip, and later work on unary encoding and optimized unary encoding showed that K-dimensional privatized encodings can substantially improve estimation accuracy for large categorical domains. Hadamard Response further demonstrated that using structured, transformed vector sketches can reduce sample complexity and improve K-scaling in locally private distribution estimation. Parallelly, PATE revealed the value of probability vectors (soft labels) for learning under privacy, indicating that probabilistic targets preserve richer information for training than hard labels, even when privatization noise is present.
Together these results exposed a clear gap: label-LDP training largely relied on scalar flips (GRR-style labels) whose utility collapses with growing K, whereas vectorized LDP encodings and soft-label training both suggest that multi-dimensional privatized signals retain more class information. The present work synthesizes these strands by privatizing each label as a K-dimensional random vector whose expectation matches class-conditional probabilities, marrying the variance advantages of vector LDP encodings with the learning benefits of soft targets. This yields an easy-to-implement, low-overhead mechanism whose error grows much more gently with K, directly addressing the core limitation of GRR-based label privatization.

---

*Analysis generated on: 2026-01-06T13:30:20.030059*

*Pipeline: Prior Work Extraction v2.0 (Direct Lineage Focus)*
