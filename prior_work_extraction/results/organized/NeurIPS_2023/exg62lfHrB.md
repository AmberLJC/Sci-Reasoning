# Prior Work Analysis Report

## Target Paper
**Title:** exg62lfHrB
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

Model Spider tackles the problem of efficiently selecting a suitable pretrained model from a large, heterogeneous zoo by learning a compatibility function between model and task representations. Two foundational ideas motivate this design. First, Taskonomy showed that cross-task transfer patterns form a structured signal that can be learned and generalized, while Task2Vec introduced the notion of embedding tasks into vector spaces for downstream meta-learning. Building on these, Model Spider tokenizes both tasks and PTMs into embeddings and learns a fitness score to rank model candidates without exhaustively evaluating each model.
Transferability metrics such as LEEP and LogME directly shape the problem formulation and baselines for Model Spider: they estimate how well a pretrained representation will transfer to a target with minimal adaptation. However, they still require per-model probing on the target data. Model Spider advances this line by training on a separate set of tasks and their approximate performances to amortize selection, enabling efficient ranking across many PTMs with limited computation.
Empirical insights from “Do Better ImageNet Models Transfer Better?” motivate robust, dataset-aware model selection beyond simple pretraining accuracy, aligning with Model Spider’s emphasis on learned compatibility rather than naive heuristics. Finally, Auto-sklearn’s meta-learning for algorithm selection and RankNet’s pairwise learning-to-rank objective inform Model Spider’s meta-level training and optimization: use historical task–model outcomes to learn embeddings and a ranking loss, then re-rank with PTM-specific semantics to refine final selection.

---
*Generated: 2026-01-06T23:42:48.029988*
