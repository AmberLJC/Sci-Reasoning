# Prior Work Analysis Report

## Target Paper
**Title:** b7waOsMnq8
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—sharp Gaussian approximations for decentralized federated learning with local SGD, including a Berry–Esseen theorem for the terminal iterate and time-uniform approximations for the full trajectory—rests on two pillars: the local-SGD/federated optimization paradigm and modern probabilistic approximation/bootstrapping tools for dependent processes.

On the algorithmic side, McMahan et al.’s FedAvg introduced local updating with intermittent aggregation, the very structure formalized as local SGD and analyzed by Stich, whose results established fast convergence with limited communication. These works identify the object of inference (local SGD iterates) and baseline convergence properties that this paper advances to distributional guarantees.

On the statistical side, Polyak and Juditsky’s stochastic-approximation CLT for averaged SGD seeded the idea that SGD iterates admit Gaussian limits. To obtain sharp, nonasymptotic guarantees for non-averaged local SGD, the authors draw on martingale Berry–Esseen theory (Haeusler), enabling explicit rates for the final iterate. For trajectory-wide, time-uniform approximations and valid Gaussian multiplier bootstraps, they leverage Gaussian approximation techniques for dependent sequences (Zhang & Wu), naturally modeling SGD’s dependence structure, together with multiplier bootstrap theory and uniform Gaussian approximations over index sets (Chernozhukov–Chetverikov–Kato).

Finally, the application to adversarial attack detection in federated settings is motivated by Byzantine-robust distributed learning (Yin et al.), where detecting malicious behavior is critical; the proposed time-uniform Gaussian approximations justify bootstrap-based tests along the training trajectory, turning robustness goals into principled statistical procedures.

---
*Generated: 2026-01-07T00:21:33.145457*
