# Prior Work Analysis Report

## Target Paper
**Title:** Ex3oJEKS53
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s central advance is a principled, architecture-agnostic framework for applying K-FAC to modern neural networks that use linear layers with weight sharing, culminating in two variants—expand and reduce—and exactness guarantees for deep linear networks with tying. This builds first on the original K-FAC formulation, which factorizes Fisher/Gauss–Newton blocks into activation and gradient covariances for fully connected layers (Grosse & Martens, 2015). The convolutional extension (Martens & Grosse, 2015) showed how weight sharing in CNNs induces structured Fisher blocks; the present work generalizes that insight beyond convolutions to arbitrary linear weight-tying, formalized as expand versus reduce operations.

Methodologically, the curvature target and exactness arguments rest on the Gauss–Newton/Fisher perspective developed for scalable second-order optimization (Botev et al., 2017) and the broader natural-gradient foundation (Amari, 1998), which justify K-FAC as an efficient approximation to the Fisher geometry even under parameter tying. On the application side, scalable Laplace approximations leveraging K-FAC (Ritter et al., 2018) established that such curvature estimates enable marginal likelihood-based hyperparameter selection; the authors exploit this by using the faster K-FAC-reduce to accelerate evidence optimization in Wide ResNets. Finally, practical large-scale deployments of K-FAC on modern architectures (Osawa et al., 2019) underscored both the potential and the need for a unified treatment of weight sharing, directly motivating the paper’s architecture-general framework and its two computationally distinct K-FAC flavors.

---
*Generated: 2026-01-06T23:33:35.594060*
