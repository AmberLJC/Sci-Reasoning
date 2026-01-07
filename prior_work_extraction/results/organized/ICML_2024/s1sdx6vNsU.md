# Prior Work Analysis Report

## Target Paper
**Title:** s1sdx6vNsU
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

---

## Synthesis

The paper’s core contribution—showing that LoRA training in the NTK regime has no spurious local minima once the adapter rank r scales as √N and that the resulting low-rank solution generalizes—sits at the intersection of three lines of prior work. First, LoRA itself (Hu et al.) provides the low-rank parameterization whose expressivity and trainability are under scrutiny. Second, the NTK framework (Jacot et al.) linearizes training around initialization so that fine-tuning reduces to kernel regression with fixed features; in this linearized setting, imposing LoRA is equivalent to optimizing a factorized low-rank parameter matrix, introducing specific nonconvexity. Third, a rich literature on nonconvex low-rank factorization (Boumal–Voroninski–Bandeira; Ge–Lee–Ma; Bhojanapalli–Neyshabur–Srebro) shows that when the factorization rank exceeds a threshold proportional to the square root of the number of constraints, the landscape becomes benign—local minima are global and gradient methods succeed. The paper directly leverages this blueprint to establish a sharp r ≳ √N threshold that removes spurious local minima for LoRA in the NTK regime, and it complements this with an existence argument that full fine-tuning admits low-rank solutions of rank ≲ √N. Finally, insights on implicit regularization in matrix factorization (Gunasekar et al.) connect the optimization trajectory to low-norm, low-rank solutions, underpinning the paper’s generalization claim for the LoRA-found solution.

---
*Generated: 2026-01-07T00:02:04.899954*
