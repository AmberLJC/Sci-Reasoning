# Prior Work Analysis Report

## Target Paper
**Title:** A3YUPeJTNR
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Prediction Policy Problems** (2015)
- *Authors:* Kleinberg et al.
- *Connection:* This paper formalized the use of predictive risk scores to target scarce interventions under resource constraints; the current work adopts that targeting-as-ranking framework and extends it to a sequential setting where information accrues over time, revealing that later, more accurate signals can perversely worsen population-level ranking loss.

**Sequential Analysis** (1947)
- *Authors:* Wald
- *Connection:* Wald’s framework for sequentially accumulating observations underlies the paper’s model of predictions improving over time, enabling the formal analysis of the planner’s timing decision to act now with noisier signals or wait for more precise ones.

**On the Comparison of Experiments** (1951)
- *Authors:* Blackwell
- *Connection:* Blackwell’s value-of-information ordering motivates the prevailing intuition that more informative signals should improve decisions; the paper pinpoints a setting—information acquisition coupled with intervention timing—where this intuition fails, yielding worse average ranking despite higher individual accuracy.

### 💡 Inspiration

**On Optimum Recognition Error and Reject Trade-off** (1970)
- *Authors:* Chow
- *Connection:* Chow’s reject-option formalizes the explicit trade-off between making an early, potentially error-prone decision and deferring for more information; the present paper reinterprets deferral as waiting to collect additional observations and quantifies its hidden cost on ranking and welfare.

### 🔍 Gap Identification

**Delayed Impact of Fair Machine Learning** (2018)
- *Authors:* Liu et al.
- *Connection:* By showing that predictive allocations can have harmful delayed effects, this work highlights temporal dynamics that static analyses miss; the present paper addresses a specific gap by isolating the timing-of-information acquisition itself as a source of welfare and ranking degradation even without feedback loops.

### 📊 Baseline

**Human Decisions and Machine Predictions** (2018)
- *Authors:* Kleinberg et al.
- *Connection:* As a canonical demonstration of prediction-driven allocation in practice (e.g., bail), it represents the static, score-based targeting baseline whose underlying assumption—that better accuracy improves allocation—this paper directly interrogates by showing that waiting for more accurate predictions can degrade rank-based targeting performance.

### 🔗 Related Problem

**Performative Prediction** (2020)
- *Authors:* Perdomo et al.
- *Connection:* This work formalizes how predictions interact with and change the data-generating process; the current paper complements it by proving that even absent performative effects, the mere timing of prediction (waiting for accuracy) can undermine ranking and optimal allocation.

---

## Synthesis

The paper’s core idea—modeling and quantifying the hidden cost of waiting for more accurate predictions in allocation—sits at the intersection of predictive targeting, sequential decision theory, and the temporal dynamics of deployment. Prediction Policy Problems and Human Decisions and Machine Predictions established the dominant paradigm of using risk scores to rank individuals and allocate scarce resources, implicitly equating higher predictive accuracy with better social welfare. Classical decision theory provides the methodological backbone: Wald’s Sequential Analysis and Chow’s reject-option encode the mechanism by which information accrues over time and decisions can be deferred at a cost, while Blackwell’s comparison of experiments articulates the value-of-information intuition that more informative signals should help. Recent work on the dynamics of algorithmic deployment, notably Delayed Impact of Fair Machine Learning and Performative Prediction, underscores that timing and interactions with the environment can overturn static guarantees. Building directly on these lines, the paper introduces a sequential observation model where predictions refine over time and then analyzes both the induced ranking and the welfare-maximizing allocation under resource constraints. The central contribution is a counterintuitive result: even as individual prediction accuracy improves with time, average ranking loss can worsen, revealing a principled failure mode of the “wait for accuracy” heuristic. This yields new guidance on when to act versus wait, refining the foundational predictive targeting framework by explicitly integrating the economics of timing.

---
*Generated: 2026-01-06T23:09:26.588411*
