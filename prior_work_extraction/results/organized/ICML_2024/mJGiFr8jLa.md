# Prior Work Analysis Report

## Target Paper
**Title:** mJGiFr8jLa
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

### 🏗️ Foundation

**Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations** (2019)
- *Authors:* M. Raissi et al.
- *Connection:* Introduced the PINN formulation and popularized Adam/L-BFGS training, providing the exact loss structure and baseline training protocol whose loss landscape and optimizer behavior this paper analyzes and improves.

**Fast exact multiplication by the Hessian** (1994)
- *Authors:* B. Pearlmutter
- *Connection:* Provided the Hessian–vector product technique essential for scalable Newton-CG methods, enabling the practical implementation of NysNewton-CG for large PINNs.

### 💡 Inspiration

**Deep learning via Hessian-free optimization** (2010)
- *Authors:* J. Martens
- *Connection:* Established the Newton-CG/Hessian-free paradigm using curvature–vector products, the algorithmic scaffold that NysNewton-CG adopts and specializes to the PINN setting.

**Using the Nyström method to speed up kernel machines** (2001)
- *Authors:* C. K. I. Williams et al.
- *Connection:* Introduced Nyström low-rank approximations for PSD matrices; the proposed NysNewton-CG leverages this idea to build an efficient curvature approximation/preconditioner for Newton-CG in PINNs.

### 🔍 Gap Identification

**Characterizing possible failure modes in physics-informed neural networks** (2021)
- *Authors:* A. Krishnapriyan et al.
- *Connection:* Documented optimizer sensitivity and training pathologies in PINNs, directly motivating this paper’s loss-conditioning analysis and the search for more robust second-order training methods.

### 📊 Baseline

**On the limited memory BFGS method for large scale optimization** (1989)
- *Authors:* D. C. Liu et al.
- *Connection:* Defines the L-BFGS optimizer that serves as a primary baseline; this paper explains L-BFGS’s limitations under operator-induced ill-conditioning and demonstrates gains from Adam+L-BFGS and NysNewton-CG.

### 🔧 Extension

**Sub-sampled Newton methods I: globally convergent algorithms** (2019)
- *Authors:* F. Roosta-Khorasani et al.
- *Connection:* Provided randomized second-order strategies via approximate curvature, which NysNewton-CG extends by using a Nyström low-rank curvature model tailored to ill-conditioned PINN losses.

---

## Synthesis

The core innovation of this paper is to reveal how differential operators induce ill-conditioning in the PINN loss landscape and to exploit this insight with an efficient second-order optimizer, NysNewton-CG. This trajectory begins with Raissi et al. (2019), which formalized the PINN loss and popularized Adam/L-BFGS training—precisely the setup interrogated here. Reports of optimizer sensitivity and failures in Krishnapriyan et al. (2021) directly exposed gaps that this work addresses by tying failures to operator-driven conditioning and by proposing a principled remedy. Algorithmically, the second-order component builds on the Hessian-free/Newton-CG framework of Martens (2010), which uses curvature–vector products to obtain Newton steps without forming the Hessian. Randomized second-order ideas from Roosta-Khorasani and Mahoney (2019) further inform the design, suggesting that approximate curvature can be both effective and scalable. Williams and Seeger (2001) provide the critical Nyström low-rank approximation used here to construct an efficient curvature model/preconditioner aligned to the structure of the PINN loss. Pearlmutter (1994) underpins the entire approach by enabling fast Hessian–vector products required for Newton-CG. Finally, Liu and Nocedal (1989) supply the L-BFGS baseline that the paper analyzes and surpasses, both empirically and conceptually, by showing why pure first- or quasi-Newton methods struggle on ill-conditioned PINN losses and why a hybrid (Adam+L-BFGS) and the proposed NysNewton-CG yield substantial gains.

---
*Generated: 2026-01-06T23:09:26.450409*
