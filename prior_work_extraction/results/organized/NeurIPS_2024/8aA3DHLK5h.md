# Prior Work Analysis Report

## Target Paper
**Title:** 8aA3DHLK5h
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

This work fuses approachability theory with the geometry of extensive-form games to produce a stepsize-invariant regret-minimization framework on treeplexes. Blackwell’s 1956 approachability provides the conceptual core: casting no-regret learning as the approachability of a convex set (often a cone). Hart and Mas-Colell’s Regret Matching, itself analyzable via approachability, supplies the model for stepsize-invariant updates on the simplex; the present paper generalizes that invariance to the sequence-form polytope. Von Stengel’s sequence form and the treeplex geometry developed in subsequent work, especially Hoda et al., furnish the representation and distance-generating tools necessary to implement approachability and mirror-style updates over the exponentially structured strategy space of EFGs. The reduction from regret minimization to Nash equilibrium computation in EFGs established by Zinkevich et al. (CFR) is the operational scaffold: the new Blackwell-on-treeplex algorithms plug into self-play to compute equilibria. On the optimization side, the predictive/optimistic online mirror descent framework of Rakhlin and Sridharan underpins the introduction of Predictive Treeplex Blackwell+ (PTB+), delivering O(1/√T) rates in self-play; a stabilized variant achieves state-of-the-art O(1/T), echoing the acceleration seen in optimistic/extragradient methods. Finally, the practical success and stepsize-invariant spirit of RM+ (Tammelin) inform the paper’s plus-style updates in the richer treeplex setting, unifying approachability, regret minimization, and first-order prediction within sequence-form EFGs.

---
*Generated: 2026-01-06T23:39:42.967611*
