# Prior Work Analysis Report

## Target Paper
**Title:** VKKY3Uv7vi
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

BPQP stands on a clear lineage of research that made optimization layers differentiable and practical. OptNet first demonstrated a QP as a neural layer and backpropagated via KKT-based implicit differentiation, but required solving large KKT linear systems. Barratt and Boyd then provided a rigorous sensitivity analysis for cone programs via KKT systems, which underpins both theory and practice of differentiable convex optimization. Building on this, CVXPY Layers generalized differentiable convex programs using implicit differentiation of KKT systems, but incurred heavy Jacobian/KKT factorization costs, especially with many constraints. In parallel, Gould and colleagues’ Deep Declarative Networks formalized differentiating through argmin layers via KKT/implicit function theory, encouraging specialized implementations tailored to problem structure. Earlier, Domke and Pedregosa showed that one can avoid explicit Jacobian formation and large inverses by solving structured linear systems for implicit gradients—a computational perspective that strongly influenced efficiency-focused designs. Finally, decision-focused learning by Donti et al. highlighted the need for scalable, solver-in-the-loop differentiation on large, constrained problems.
BPQP’s core contribution—recasting the backward pass as a simplified, decoupled QP by exploiting KKT structure—directly extends these foundations. It retains the correctness guarantees of KKT-based implicit differentiation while replacing costly Jacobian/KKT solves with a smaller QP that can be solved efficiently and even decoupled across instances, addressing the scalability and efficiency bottlenecks identified in prior differentiable optimization frameworks.

---
*Generated: 2026-01-06T23:42:49.048507*
