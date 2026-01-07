# Prior Work Analysis Report

## Target Paper
**Title:** gmmXyAq8TI
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Coop’s central contribution is to treat GPU memory as addressful, not fungible, and to co-optimize tensor allocation with rematerialization so evictions form contiguous, immediately reusable regions. This builds on a lineage of compute–memory tradeoffs. Revolve provides the theoretical basis for checkpointing schedules, while Chen et al. brought rematerialization to deep learning with gradient checkpointing. Later, systems like Checkmate and DTR refined rematerialization—Checkmate by optimizing global schedules under memory budgets and DTR by making online eviction decisions. However, these methods largely assume that any freed memory is equivalent, neglecting the allocator’s address space and the fragmentation it induces.

At the same time, DL frameworks exposed the practical challenge: TensorFlow’s BFC allocator and MXNet’s graph-aware memory planning highlighted how allocation, in-place reuse, and co-sharing govern peak memory and fragmentation. These works showed that where and how a tensor is placed matters, yet they did not integrate this with rematerialization policies. Finally, vDNN’s windowed management of activations illustrated the benefits of structured, locality-aware scheduling for memory, albeit focused on offloading rather than address-aware evictions.

Coop synthesizes these strands: it adopts rematerialization but constrains evictions to a sliding window so freed bytes are contiguous and immediately consumed by the pending allocation, and it further reduces recomputation with in-place reuse and cheap tensor partitioning. By unifying schedule and placement, Coop directly addresses fragmentation—a blind spot in prior rematerialization work.

---
*Generated: 2026-01-06T23:42:49.130256*
