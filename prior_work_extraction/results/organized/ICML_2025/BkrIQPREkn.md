# Prior Work Analysis Report

## Target Paper
**Title:** BkrIQPREkn
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

AMUN’s core insight is to use adversarial examples of the forget set to reduce model confidence on those samples while preserving accuracy on retained data and unseen test inputs. This builds directly on the machine unlearning problem formulation by Cao and Yang, which framed the need to emulate retraining after deletion but highlighted the computational cost of exact approaches. Subsequent scalable approximate methods, most notably SISA by Bourtoule et al., and selective forgetting via Fisher-based perturbations by Golatkar et al., exposed a persistent efficacy gap: approximate unlearning struggled to match retraining in both accuracy and calibrated confidence on forget/test data. AMUN targets this gap by importing tools and intuitions from adversarial robustness. Goodfellow et al. introduced efficient adversarial example generation, and Madry et al. formalized adversarial training as robust optimization, providing a principled inner maximization to find nearest adversaries that sculpt local decision boundaries. Ilyas et al.’s finding that adversarial examples reflect non-robust yet predictive features offers a conceptual rationale for using adversarial variants as targeted, model-aligned perturbations for unlearning—changing what the model relies on without broad accuracy collapse. Finally, TRADES shows how adversarial training objectives can explicitly manage the trade-off between robustness, accuracy, and confidence via KL-based regularization. By fine-tuning on closest adversarial examples of forget samples, AMUN operationalizes these ideas to selectively suppress confidence where deletion is requested while retaining generalization on the remaining distribution, thereby narrowing the gap to exact unlearning with modest computational overhead.

---
*Generated: 2026-01-07T00:04:09.136118*
