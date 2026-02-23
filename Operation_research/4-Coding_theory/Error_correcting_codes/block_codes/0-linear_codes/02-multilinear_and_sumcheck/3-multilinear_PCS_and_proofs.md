# Multilinear Polynomial Commitment Schemes

A **Polynomial Commitment Scheme (PCS)** allows a prover to commit to a polynomial and later open it at verifier-chosen points, without revealing the polynomial itself. In the **multilinear** setting the committed object is a multilinear polynomial $\tilde{f}: \mathbb{F}^\ell \to \mathbb{F}$, representing $N = 2^\ell$ field elements. Multilinear PCS are the cryptographic "glue" connecting the Sum-Check Protocol to a succinct non-interactive argument (SNARK).

---

## 1. Polynomial Commitment Schemes: General Definitions

### 1.1 **Definition (Polynomial Commitment Scheme):**
A PCS consists of five algorithms:
- $\mathsf{Setup}(1^\lambda, d) \to \mathsf{ck}$: Generates a commitment key for polynomials of degree $\leq d$.
- $\mathsf{Commit}(\mathsf{ck}, f) \to (\mathsf{cm}, \mathsf{open})$: Commits to polynomial $f$; outputs commitment $\mathsf{cm}$ and opening information $\mathsf{open}$.
- $\mathsf{Open}(\mathsf{ck}, \mathsf{open}, z) \to (v, \pi)$: Produces evaluation $v = f(z)$ and proof $\pi$.
- $\mathsf{Verify}(\mathsf{ck}, \mathsf{cm}, z, v, \pi) \to \{0,1\}$: Checks that $\mathsf{cm}$ commits to a polynomial evaluating to $v$ at $z$.

**Security properties:**
- **Binding:** It is computationally hard to open $\mathsf{cm}$ to two different evaluations at any point.
- **Hiding** (optional): $\mathsf{cm}$ reveals nothing about $f$ (zero-knowledge).
- **Succinctness:**  $|\mathsf{cm}| = O(1)$ and $\mathsf{Verify}$ runs in $o(N)$ time.

### 1.2 Multilinear Setting

For **multilinear** PCS we specialize to $d = 1$ (each variable) and identify $f$ with its $N = 2^\ell$ values. Evaluation proofs are for points $z \in \mathbb{F}^\ell$.

**The fundamental challenge:** A multilinear polynomial has $N$ coefficients. A succinct PCS must compress this into a $O(1)$- or $O(\ell)$-sized commitment.

---

## 2. Inner Product Arguments and Tensor Structure

Many multilinear PCS exploit the **tensor product structure** of multilinear evaluation.

### 2.1 **Claim (Tensor Decomposition of Evaluation):**
Fix $z = (z_1, \dots, z_\ell) \in \mathbb{F}^\ell$. The evaluation of the MLE $\tilde{f}$ at $z$ equals an **inner product**:
$$\tilde{f}(z) = \langle \mathbf{f}, \boldsymbol{\chi}(z) \rangle = \sum_{w \in \{0,1\}^\ell} f(w) \cdot \chi_w(z),$$
where $\mathbf{f} = (f(w))_w \in \mathbb{F}^N$ is the coefficient vector and $\boldsymbol{\chi}(z) = (\chi_w(z))_w \in \mathbb{F}^N$ is the vector of basis polynomial evaluations.

**Key observation:** The vector $\boldsymbol{\chi}(z)$ has a **tensor product structure**:
$$\boldsymbol{\chi}(z) = \bigotimes_{i=1}^\ell (1 - z_i, z_i) \in \mathbb{F}^N.$$
This means $\chi_{(b_1,\dots,b_\ell)}(z) = \prod_{i=1}^\ell (b_i z_i + (1-b_i)(1-z_i))$, as expected.

This tensor structure enables **recursive halving** of the evaluation proof, used in schemes like **Hyrax** and **Dory**.

---

## 3. Hyrax: Pedersen-Based Multilinear PCS

**Hyrax** (Wahby et al., 2018) is a transparent multilinear PCS based on discrete logarithm assumptions, with $O(\sqrt{N})$ proof size.

### 3.1 Setup

Let $\mathbb{G}$ be a prime-order group with generators $\mathbf{g} = (g_0, g_1, \dots, g_{N-1}) \leftarrow \mathbb{G}^N$ chosen uniformly (no trusted setup needed). Arrange the $N$ values of $f$ in a $\sqrt{N} \times \sqrt{N}$ matrix $F$.

### 3.2 Commitment

$$\mathsf{cm} = \left( \mathbf{C}_1, \dots, \mathbf{C}_{\sqrt{N}} \right), \quad \mathbf{C}_i = \prod_{j=0}^{\sqrt{N}-1} g_{i,j}^{f_{ij}} \in \mathbb{G}.$$

Each $\mathbf{C}_i$ is a **Pedersen vector commitment** to row $i$ of $F$. The commitment size is $\sqrt{N}$ group elements.

### 3.3 Evaluation Proof

To prove $\tilde{f}(z) = v$, split $z = (z_L, z_R)$ with $z_L, z_R \in \mathbb{F}^{\ell/2}$. Define:
- $L_j = \chi_{z_R}$ restricted to the $j$-th row, giving a vector $\mathbf{l} = \boldsymbol{\chi}(z_L) \in \mathbb{F}^{\sqrt{N}}$.
- $R_j = \chi_{z_L}$ restricted to the $j$-th column, giving $\mathbf{r} = \boldsymbol{\chi}(z_R) \in \mathbb{F}^{\sqrt{N}}$.

The prover sends the vector $\mathbf{d} = F^T \mathbf{l} \in \mathbb{F}^{\sqrt{N}}$ (an inner product of each column with $\mathbf{l}$) and an inner product argument that $\mathbf{r} \cdot \mathbf{d} = v$. The commitment to $\mathbf{d}$ is verifiable because:
$$\prod_i \mathbf{C}_i^{l_i} = \prod_{i,j} g_{ij}^{f_{ij} l_i} = \prod_j \left(\prod_i g_{ij}^{f_{ij} l_i}\right) = \text{commitment to } \mathbf{d}.$$

**Sizes:** Proof = $O(\sqrt{N})$ group elements. Verifier time = $O(\sqrt{N})$.

---

## 4. PST / KZG Multilinear PCS

The **Papamanthou-Shi-Tamassia (PST)** scheme extends KZG commitments to the multilinear setting using a **structured reference string (SRS)** derived from a trusted setup.

### 4.1 Setup

Sample $\tau_1, \dots, \tau_\ell \xleftarrow{\$} \mathbb{F}$ (trapdoor). Publish:
$$\mathsf{ck} = \left\{ g^{\prod_{i \in S} \tau_i} \right\}_{S \subseteq [\ell]} \in \mathbb{G}^{2^\ell}.$$
These are the **structured powers** of the generators corresponding to each monomial of a multilinear polynomial.

### 4.2 Commitment

$$\mathsf{cm} = g^{\tilde{f}(\tau_1, \dots, \tau_\ell)} = \prod_{S \subseteq [\ell]} \left(g^{\prod_{i \in S} \tau_i}\right)^{\hat{f}(S)}.$$
This is a **single group element**, computed from the Möbius coefficients $\hat{f}(S)$ of $\tilde{f}$.

### 4.3 Evaluation Proof

**Theorem (Quotient Representation):**
For a multilinear polynomial $\tilde{f}$ and a point $z = (z_1, \dots, z_\ell)$, there exist multilinear **quotient polynomials** $q_1, \dots, q_\ell$ such that:
$$\tilde{f}(x) - \tilde{f}(z) = \sum_{i=1}^\ell (x_i - z_i) q_i(x_1, \dots, x_{i-1}).$$

**Proof sketch:**
Apply iterated univariate division: in $x_1$, write $\tilde{f}(x) - \tilde{f}(z_1, x_2, \dots) = (x_1 - z_1) q_1(x_2,\dots,x_\ell)$. Then recurse on $\tilde{f}(z_1, x_2, \dots) - \tilde{f}(z)$ in $x_2$, etc. At each step the quotient is multilinear in the remaining variables. $\square$

The **evaluation proof** consists of $\ell$ commitments $\pi_i = g^{q_i(\tau_1, \dots, \tau_{i-1})}$ (one per variable), each a single group element. Total proof size: $\ell$ group elements.

**Verification** uses a single multi-pairing check:
$$e(\mathsf{cm} / g^v, g) = \prod_{i=1}^\ell e(\pi_i, g^{\tau_i} / g^{z_i}).$$

**Costs:**

| Parameter | PST/KZG Multilinear |
|-----------|---------------------|
| SRS size | $2^\ell = N$ group elements |
| Commitment | $O(N)$ group operations, size $O(1)$ |
| Proof | $O(N)$ operations, size $O(\ell)$ |
| Verification | $O(\ell)$ pairings |

---

## 5. Dory: Transparent Multilinear PCS

**Dory** (Lee, 2021) achieves $O(\sqrt{N})$ proof size and $O(\log N)$ verifier time **without a trusted setup**, using **inner pairing product arguments** over a bilinear group.

### 5.1 Core Idea

Represent the coefficient vector $\mathbf{f}$ as a $\sqrt{N} \times \sqrt{N}$ matrix and the evaluation tensor $\boldsymbol{\chi}(z)$ as an outer product $\mathbf{l} \otimes \mathbf{r}$.

The prover must convince the verifier of the inner product $\langle \mathbf{f}_{\text{rows}}, \mathbf{r} \rangle_{\mathbb{G}}$ using a **pairing-based inner product argument** that halves the problem size at each step.

**Proof size:** $O(\log N)$ after $O(\log N)$ rounds of halving.  
**Verifier time:** $O(\log N)$ pairings.

### 5.2 Comparison Summary

| Scheme | Setup | Commit Size | Proof Size | Verifier Time |
|--------|-------|-------------|------------|---------------|
| Hyrax | Transparent | $O(\sqrt{N})$ | $O(\sqrt{N})$ | $O(\sqrt{N})$ |
| PST/KZG MLE | Trusted ($N$ SRS) | $O(1)$ | $O(\ell)$ | $O(\ell)$ pairings |
| Dory | Transparent | $O(\sqrt{N})$ | $O(\log N)$ | $O(\log N)$ |
| Brakedown | Transparent | $O(\sqrt{N})$ | $O(\sqrt{N})$ | $O(\sqrt{N})$ |
| Virgo (FRI-based) | Transparent | $O(\sqrt{N})$ | $O(\log^2 N)$ | $O(\log^2 N)$ |

---

## 6. Integrating PCS with Sum-Check: A Complete SNARK

The combination of Sum-Check and a multilinear PCS yields a complete SNARK for arithmetic circuits.

### 6.1 **Protocol (Spartan-style SNARK, sketch):**
1. **Witness encoding:** Prover commits to $\mathsf{cm}(\tilde{w})$, the MLE of the witness vector $w$.
2. **R1CS Sum-Check:** The R1CS constraints $Az \circ Bz = Cz$ translate to a sum-check over $\{0,1\}^\ell$:
   $$\sum_{x \in \{0,1\}^\ell} \tilde{A}(\tau, x) \tilde{w}(x) \cdot \tilde{B}(\tau, x) \tilde{w}(x) - \tilde{C}(\tau, x) \tilde{w}(x) = 0,$$
   for a random $\tau \in \mathbb{F}^\ell$ supplied by the verifier.
3. **Reduction to single opening:** Sum-Check reduces to a single evaluation claim $\tilde{w}(r^*) = v$ at a random point $r^*$.
4. **PCS evaluation proof:** Prover provides $(v, \pi)$ from the multilinear PCS.
5. **Verification:** Verifier checks the Sum-Check transcript and then $\mathsf{Verify}(\mathsf{ck}, \mathsf{cm}(\tilde{w}), r^*, v, \pi) = 1$.

**Total verifier work:** Sum-Check cost $O(\ell)$ + PCS verification $O(\ell)$ or $O(\log N)$ depending on scheme.

---

## References

- Wahby, R. S., Tzialla, I., Shelat, A., Thaler, J., & Walfish, M. (2018). *Doubly-efficient zkSNARKs without trusted setup*. IEEE S&P 2018. (Hyrax)
- Papamanthou, C., Shi, E., & Tamassia, R. (2013). *Signatures of correct computation*. TCC 2013. (PST)
- Lee, J. (2021). *Dory: Efficient, transparent arguments for generalised inner products and polynomial commitments*. TCC 2021.
- Setty, S. (2020). *Spartan: Efficient and general-purpose zkSNARKs without trusted setup*. CRYPTO 2020.
- Thaler, J. (2022). *Proofs, Arguments, and Zero-Knowledge* (Chp. 10–13). Georgetown University. [ProofsArgsAndZK.pdf](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf).
- Zhang, T., Xie, X., Zhang, Y., & Song, D. (2021). *Transparent polynomial delegation and its applications to zero knowledge proof*. IEEE S&P 2021. (Virgo)
