# Prior Work Analysis Report

## Target Paper
**Title:** cEJ9jNJuJP
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (6 papers)

### 🏗️ Foundation

**Attention, Learn to Solve Routing Problems!** (2019)
- *Authors:* Wouter Kool et al.
- *Connection:* It introduced a high-quality probabilistic policy for routing, widely used to derive edge-probability maps that seed post-hoc search; the ICML’24 paper questions the effectiveness of such learned probabilistic guidance when coupled with search.

**Neural Combinatorial Optimization with Reinforcement Learning** (2016)
- *Authors:* Irwan Bello et al.
- *Connection:* This seminal work established the post-hoc, search-augmented neural paradigm (e.g., active search) for combinatorial optimization that the ICML’24 paper reevaluates in its modern heatmap-guided form.

**Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm** (2017)
- *Authors:* David Silver et al.
- *Connection:* AlphaZero popularized learned-guided Monte Carlo Tree Search; the heatmap-guided MCTS paradigm critiqued by the ICML’24 paper is a direct instantiation of this learned-prior–plus–MCTS template in TSP.

### 💡 Inspiration

**Learning the Traveling Salesman Problem with Graph Neural Networks** (2020)
- *Authors:* Chaitanya K. Joshi et al.
- *Connection:* This work explicitly learns edge-inclusion probabilities (a heatmap over edges) for TSP, establishing the exact heatmap signal that the ICML’24 paper theoretically and empirically interrogates and replaces with a simple non-ML baseline.

### 🔍 Gap Identification

**NeuroLKH: Combining Deep Learning with the Lin–Kernighan–Helsgaun Heuristic for the Traveling Salesman Problem** (2021)
- *Authors:* Jingwen Xin et al.
- *Connection:* By fusing learned edge priors with a hand-crafted powerhouse (LKH), this line exemplifies post-hoc neural guidance of classical search; the ICML’24 paper highlights that such reliance on problem-specific heuristics and learned heatmaps still fails to surpass plain LKH-3 in large-scale TSP.

### 📊 Baseline

**LKH-3: Implementation of the Lin–Kernighan–Helsgaun Heuristic** (2017)
- *Authors:* Keld Helsgaun
- *Connection:* LKH-3 serves as the principal classical baseline the ICML’24 paper uses to demonstrate that heatmap-guided MCTS underperforms a state-of-the-art handcrafted heuristic on large-scale TSP.

---

## Synthesis

The ICML 2024 position paper targets a specific modern recipe for large-scale TSP—learn a heatmap over edges and couple it with a post-hoc search procedure (MCTS)—and asks whether the learned heatmap truly provides actionable guidance beyond classical heuristics. This paradigm has two intellectual roots. First, the neural-CO wave established by Bello et al. seeded the notion of post-hoc search-augmented neural solvers, while Kool et al. made high-quality probabilistic policies practical for routing at scale. Joshi et al. then crystallized the exact artifact under scrutiny—a supervised edge-inclusion probability heatmap—making “edge heatmaps” a standard interface between learning and search. Second, AlphaZero showed how learned priors can drive MCTS effectively, a template that many TSP works instantiated as heatmap-guided tree search. In parallel, NeuroLKH demonstrated how learned edge priors can be injected into a powerful handcrafted solver, epitomizing the broader class of post-hoc, problem-specific neural guidance that the paper argues remains brittle. Against this backdrop, the authors benchmark the heatmap+MCTS paradigm directly against LKH-3 and find it lacking, and further show that a simple non-ML baseline can outperform complex heatmap models. The combined lineage therefore directly motivates their thesis: the community’s reliance on learned edge heatmaps and post-hoc search has outpaced rigorous validation, and future work should pursue theoretically grounded heatmaps and more autonomous, generalizable ML approaches that can genuinely rival LKH-3.

---
*Generated: 2026-01-06T23:09:26.436158*
