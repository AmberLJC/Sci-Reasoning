# Prior Work Analysis Report

## Target Paper
**Title:** JFygzwx8SJ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

KVzip sits at the intersection of KV-cache eviction, compression, and practical serving. Early system work such as FlashAttention established IO-aware kernels that make attention efficient but still scale linearly with cache size, while vLLM’s PagedAttention showed that careful KV memory management and sharing are crucial for high-throughput serving. On the algorithmic side, StreamingLLM demonstrated that query-agnostic eviction is feasible by relying on positional/windowing and attention-sink heuristics to sustain long-context decoding, revealing the promise of policies that do not depend on the current query. In parallel, methods like H2O and Scissorhands advanced token-importance–driven KV pruning, typically guided by attention statistics or heuristic saliency, but remained largely query-aware or tightly coupled to per-query signals, limiting cross-query reuse. KV compression efforts such as SnapKV and KVQuant further underscored that shrinking KV memory is possible without prohibitive accuracy loss, yet primarily targeted representation-level approximations or quantization rather than principled content selection. KVzip synthesizes these lines by introducing a model-driven, query-agnostic criterion: measuring each KV pair’s contribution to reconstructing the original context with the underlying LLM. This reconstruction-based importance allows a single compressed KV cache to be reused across diverse queries, delivering 3–4× cache reduction and about 2× lower FlashAttention decoding latency with negligible task degradation, and providing a complementary lever to quantization and system-level paging.

---
*Generated: 2026-01-07T00:21:32.322833*
