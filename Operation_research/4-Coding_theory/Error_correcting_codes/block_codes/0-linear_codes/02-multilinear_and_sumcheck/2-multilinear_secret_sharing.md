# Multilinear Secret Sharing

This document extends the classical **Shamir Secret Sharing** to the multilinear setting. Instead of a univariate secret polynomial over a threshold, we consider secrets indexed by the Boolean hypercube, share functions derived from multilinear extensions, and packed (batch) schemes that secret-share many secrets simultaneously. These constructions underpin modern **MPC protocols** and **distributed SNARKs**.

---

## 1. Recap: Shamir vs. Multilinear

| Property | Shamir (univariate) | Multilinear |
|----------|---------------------|-------------|
| Secret space | $\mathbb{F}$ (single element) | $\mathbb{F}^{2^\ell}$ (function on $\{0,1\}^\ell$) |
| Polynomial | $f(x)$, degree $< k$ | $\tilde{f}(x_1,\dots,x_\ell)$, multilinear |
| Share of party $i$ | $f(\alpha_i) \in \mathbb{F}$ | $\tilde{f}(r^{(i)}) \in \mathbb{F}$ for random $r^{(i)} \in \mathbb{F}^\ell$ |
| Reconstruction | Lagrange on the line | Multilinear evaluation |
| Dimension of secret | 1 | $2^\ell$ |

---

## 2. Multilinear Secret Sharing: Formal Setup

### 2.1 **Definition (Multilinear Secret Sharing Scheme — Informal):**
A $(t, n)$-multilinear secret sharing scheme (MLSS) shares a function $f: \{0,1\}^\ell \to \mathbb{F}$ (the **secret**) among $n$ parties such that:
1. **$t$-Reconstruction**: Any $t$ parties can jointly recover $f$ completely.
2. **$(t-1)$-Privacy**: Any $t-1$ parties learn nothing about $f$.

The scheme uses the **multilinear extension** $\tilde{f}$ as the underlying polynomial object.

### 2.2 **Definition (Multilinear Secret Sharing Scheme — Formal):**
Let $\mathbb{F}$ be a finite field with $|\mathbb{F}| \geq n + 2^\ell$. Fix:
- $n$ distinct **evaluation points** $\alpha_1, \dots, \alpha_n \in \mathbb{F} \setminus \{0,1\}$ (i.e., not used as Boolean inputs).
- A **threshold** $t \leq n$.
- A **secret** $f: \{0,1\}^\ell \to \mathbb{F}$, represented as its vector of $N = 2^\ell$ values.

**Distribution (Dealer $\mathcal{D}$):**
1. Embed $f$ as the coefficient vector $\mathbf{c} = (f(w))_{w \in \{0,1\}^\ell} \in \mathbb{F}^N$.
2. Choose $t - 1$ uniformly random functions $r_1, \dots, r_{t-1}: \{0,1\}^\ell \to \mathbb{F}$ (the **masking functions**).
3. Construct the **randomized multilinear polynomial** $F: \mathbb{F} \times \mathbb{F}^\ell \to \mathbb{F}$:
   $$F(y, x_1, \dots, x_\ell) := \tilde{f}(x_1, \dots, x_\ell) + \sum_{j=1}^{t-1} y^j \cdot \tilde{r}_j(x_1, \dots, x_\ell).$$
   Here $y$ is the "party index dimension" and $\tilde{r}_j$ is the MLE of $r_j$.
4. **Share of party $P_i$:** The function $F_i: \{0,1\}^\ell \to \mathbb{F}$, defined by $F_i(x) = F(\alpha_i, x)$.

**Reconstruction:** Given shares $F_{i_1}, \dots, F_{i_t}$ from any $t$ parties, apply univariate Lagrange interpolation at each point $x \in \{0,1\}^\ell$ separately:
$$\tilde{f}(x) = F(0, x) = \sum_{j=1}^{t} F_{i_j}(x) \cdot \prod_{m \neq j} \frac{0 - \alpha_{i_m}}{\alpha_{i_j} - \alpha_{i_m}}.$$
The Lagrange coefficients $\lambda_j = \prod_{m \neq j} \frac{-\alpha_{i_m}}{\alpha_{i_j} - \alpha_{i_m}}$ depend only on the parties' indices, not on $x$. So reconstruction is:
$$\tilde{f}(x) = \sum_{j=1}^{t} \lambda_j \cdot F_{i_j}(x), \quad \forall x \in \mathbb{F}^\ell.$$

This can be applied point-by-point for each $x \in \{0,1\}^\ell$ to recover all of $f$.

---

## 3. Security Analysis

### 3.1 **Theorem (Perfect $t$-Privacy):**
In the above scheme, any $t - 1$ shares are **statistically independent** of the secret $f$.

**Proof:**
Fix any set $I \subset [n]$ with $|I| = t - 1$. The shares $\{F_i(x)\}_{i \in I}$ at any fixed $x$ form a univariate polynomial $F(\cdot, x)$ evaluated at $\{\alpha_i\}_{i \in I}$.

Since $F(\cdot, x)$ has degree $t - 1$ in $y$ with the top $t-1$ coefficients $\tilde{r}_j(x)$ chosen uniformly at random, by the standard Shamir privacy argument:
- Any $t-1$ evaluations $F(\alpha_i, x)$ determine $\tilde{r}_1(x), \dots, \tilde{r}_{t-1}(x)$ but leave $F(0, x) = \tilde{f}(x)$ uniformly distributed in $\mathbb{F}$.
- Since this holds for each $x \in \{0,1\}^\ell$ and the masking polynomials $\tilde{r}_j$ are independent, the entire secret function $f$ is information-theoretically hidden. $\square$

### 3.2 **Theorem (Perfect $t$-Reconstruction):**
Given shares from any $t$ parties $\{F_i\}_{i \in I}$, the unique polynomial $F(\cdot, x)$ of degree $\leq t-1$ interpolating $\{(\alpha_i, F_i(x))\}_{i \in I}$ equals the true $F(\cdot, x)$ for all $x$.

**Proof:**
By Lagrange's theorem, $t$ points $(y_1, v_1), \dots, (y_t, v_t)$ with distinct $y_i$ uniquely determine a polynomial of degree $\leq t-1$. Since $F(\cdot, x)$ has degree $t-1$ and the $\alpha_i$ are distinct, $t$ evaluations uniquely recover $F(\cdot, x)$, and setting $y = 0$ gives $\tilde{f}(x) = F(0, x)$. $\square$

### 3.3 Share Size

Each share $F_i$ is a function $\{0,1\}^\ell \to \mathbb{F}$, requiring $N = 2^\ell$ field elements to store. Thus the **share expansion ratio** is:
$$\text{share size} / \text{secret size} = N / N = 1 \text{ (per party)},$$
i.e., each share is the same size as the secret. The total storage across all $n$ parties is $n \cdot N$ (vs. $N$ for the secret). This matches the share expansion of univariate Shamir applied independently to each of the $N$ coordinates.

---

## 4. Packed Multilinear Secret Sharing

**Packed (or batch) secret sharing** amortizes the cost by sharing multiple secrets simultaneously within a single polynomial family.

### 4.1 **Definition (Packed MLSS):**
Let $B \leq t - 1$ be a **batch size**. The dealer holds $B$ secrets $f^{(1)}, \dots, f^{(B)}: \{0,1\}^\ell \to \mathbb{F}$.

Choose $B$ distinct **secret embedding points** $\beta_1, \dots, \beta_B \in \mathbb{F} \setminus \{\alpha_1, \dots, \alpha_n\}$. Construct the polynomial $F: \mathbb{F} \times \mathbb{F}^\ell \to \mathbb{F}$ of degree $t - 1$ in $y$ such that:
$$F(\beta_j, x) = \tilde{f}^{(j)}(x), \quad j = 1, \dots, B,$$
and $F(\alpha_i, x)$ is the share of party $P_i$.

**Construction:** For each fixed $x \in \{0,1\}^\ell$, use Lagrange interpolation to construct a univariate polynomial $p_x$ of degree $t - 1$ satisfying $p_x(\beta_j) = f^{(j)}(x)$ for $j = 1, \dots, B$, with the remaining $t - 1 - B$ degrees of freedom filled by random masking.

**Reconstruction of $f^{(j)}$:** Given $t$ shares, interpolate $F(\cdot, x)$ and evaluate at $\beta_j$.

**Security threshold:** With $B$ secrets embedded and $t$ parties needed for reconstruction, privacy holds for any coalition of $\leq t - B - 1$ parties.

### 4.2 **Theorem (Batch Amortization):**
Packed MLSS with batch size $B$ achieves:
- **Communication per secret:** $N / B$ (amortized), down from $N$.
- **Privacy threshold:** $t - B - 1$ (instead of $t - 1$).
- **Reconstruction threshold:** $t$ (unchanged).

**Tradeoff:** Larger batches $B$ reduce communication cost but also reduce the privacy threshold. This is the same tradeoff as in univariate packed Shamir (also called **Franklin-Yung packing**).

---

## 5. Verifiable Multilinear Secret Sharing

In adversarial settings, parties may submit **incorrect shares**. We extend to **Verifiable MLSS (VMLSS)**.

### 5.1 Commitment-Based Verification

**Method:** The dealer commits to the multilinear polynomial $F$ using a **multilinear polynomial commitment scheme** (e.g., PST/KZG multilinear, or Hyrax).

- **Commit phase:** Dealer broadcasts a commitment $\text{com}(F)$ and, for each party $P_i$, a **share opening proof** $\pi_i$ such that any verifier can check $F(\alpha_i, \cdot) = F_i(\cdot)$ given $\text{com}(F)$.
- **Reconstruction:** Parties reveal their shares and proofs; only shares with valid proofs are used.

**Cost (KZG multilinear, degree $\ell$ in $x$-variables):**
- Commitment: $O(N)$ group operations (one per basis polynomial).
- Share proof: $O(\ell)$ group operations (opening at a point).
- Verification: $O(\ell)$ pairing checks.

### 5.2 Extension: Byzantine Tolerance

Analogous to the univariate case (cf. the coding theory argument for Shamir), VMLSS can correct $e$ Byzantine corruptions if:
$$n \geq t + 2e.$$

**Decoding:** The error-correction problem reduces, for each fixed $x \in \{0,1\}^\ell$, to decoding a Reed-Solomon code:
- The shares $\{(\alpha_i, F_i(x))\}$ form an $(n, t)$-RS codeword corrupted in $e$ positions.
- Apply Berlekamp-Welch or Gao's algorithm to recover $F(\cdot, x)$.
- Evaluate at $y = 0$ (or $y = \beta_j$) to get $\tilde{f}(x)$ (or $\tilde{f}^{(j)}(x)$).

This decoding is performed **pointwise** for each $x \in \{0,1\}^\ell$, giving total decoding complexity $O(N \cdot n^2)$ with naïve decoding or $O(N \cdot n \log^2 n)$ with FFT-based algorithms.

---

## 6. Connection to Linear Secret Sharing Schemes (LSSS)

### 6.1 **Definition (Linear Secret Sharing Scheme — LSSS):**
A secret sharing scheme is **linear** over $\mathbb{F}$ if:
1. The shares of the secret $s \in \mathbb{F}$ are a linear function of $s$ and the randomness.
2. Given a qualified set $A$ of shares, reconstruction is a linear function of the received shares.

**Fact:** Both univariate Shamir and the multilinear scheme above are LSSS (by construction via linear interpolation and linear MLE evaluation).

### 6.2 Monotone Span Programs

Every LSSS corresponds to a **Monotone Span Program (MSP)**. An MSP is a matrix $M \in \mathbb{F}^{m \times d}$ and a labeling $\rho: [m] \to [n]$ such that:
- **Reconstruction:** For any authorized set $A \subseteq [n]$, the vector $e_1$ (first basis vector) is in the row span of $M_A = \{M_i : \rho(i) \in A\}$.
- **Privacy:** For any unauthorized set $B$, $e_1$ is not in the row span of $M_B$.

**Connection to MLE:** For threshold access structures, the MSP matrix $M$ encodes Lagrange coefficients, and for multilinear threshold schemes, $M$ encodes the Vandermonde-like structure in the $y$-variable.

---

## 7. Applications in MPC and Proof Systems

| Application | Role of Multilinear SS |
|-------------|------------------------|
| **MPC over $\mathbb{F}$ (BGW protocol generalization)** | Each wire in an arithmetic circuit carries a shared multilinear function |
| **Distributed SNARK (Ozdemir-Boneh 2022)** | Parties hold shares of the witness extension $\tilde{w}$; jointly run Sum-Check |
| **Homomorphic Threshold Encryption** | Multilinear evaluations serve as the ciphertext space |
| **Multiparty Computation from Multilinear Maps** | Secret sharing on multilinear groups |
| **Private Information Retrieval (PIR)** | $k$-server PIR based on evaluations of MLE on queried index |

---

## References

- Ben-Or, M., Goldwasser, S., & Wigderson, A. (1988). *Completeness theorems for non-cryptographic fault-tolerant distributed computation*. STOC 1988, 1–10.
- Franklin, M., & Yung, M. (1992). *Communication complexity of secure computation*. STOC 1992, 699–710.
- Shamir, A. (1979). *How to share a secret*. Communications of the ACM, 22(11), 612–613.
- Thaler, J. (2022). *Proofs, Arguments, and Zero-Knowledge* (Chp. 3, 14). Georgetown University. [ProofsArgsAndZK.pdf](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf).
- Ozdemir, A., & Boneh, D. (2022). *Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets*. USENIX Security 2022.
- Pedersen, T. P. (1991). *Non-interactive and information-theoretically secure verifiable secret sharing*. CRYPTO 1991, 129–140.
- Beimel, A. (2011). *Secret-sharing schemes: A survey*. Coding and Cryptology, LNCS 6639, 11–46.
