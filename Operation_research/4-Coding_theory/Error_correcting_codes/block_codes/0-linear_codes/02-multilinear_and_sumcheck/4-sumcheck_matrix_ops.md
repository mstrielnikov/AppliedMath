# Sum-Check and GKR for Linear Algebra: Matrix and Vector Products

The Sum-Check Protocol (cf. [§1](./1-sumcheck_protocol.md)) applies directly to the verification of **linear algebraic operations**. We show how to reduce the correctness of matrix-vector products, matrix-matrix products, and batched variants to a single or constant number of Sum-Check instances, yielding proof systems with **logarithmic verifier cost** in the matrix dimension.

---

## 1. Encoding Matrices and Vectors as Multilinear Extensions

### 1.1 Dimension Conventions

Throughout this section, let:
- $n = 2^\ell$ — the dimension (powers of 2 for simplicity; general $n$ handled by zero-padding).
- $A \in \mathbb{F}^{n \times n}$, $B \in \mathbb{F}^{n \times n}$, $u \in \mathbb{F}^n$, $v \in \mathbb{F}^n$.
- $\ell$ — the number of Boolean variables needed to index a single dimension.

### 1.2 **Definition (MLE of a Vector):**
A vector $u \in \mathbb{F}^n$ is identified with the function $u: \{0,1\}^\ell \to \mathbb{F}$ by enumerating entries in binary order. Its **multilinear extension** is:
$$\tilde{u}(x) := \sum_{b \in \{0,1\}^\ell} u_b \, \chi_b(x), \quad x \in \mathbb{F}^\ell.$$

### 1.3 **Definition (MLE of a Matrix):**
A matrix $A \in \mathbb{F}^{n \times n}$ is identified with the function $A: \{0,1\}^\ell \times \{0,1\}^\ell \to \mathbb{F}$, mapping $(i, j) \mapsto A_{ij}$. Its MLE is the multilinear polynomial in $2\ell$ variables:
$$\tilde{A}(x, y) := \sum_{(i,j) \in \{0,1\}^{2\ell}} A_{ij} \, \chi_i(x) \chi_j(y), \quad x, y \in \mathbb{F}^\ell.$$

**Tensor structure of $\tilde{A}$:** The MLE of a matrix factors over the basis as a "bilinear form" in the Lagrange basis. Unlike a general bilinear form, $\tilde{A}(x, y)$ is multilinear (degree $\leq 1$) in each of the $2\ell$ variables independently.

---

## 2. Matrix-Vector Product

### 2.1 Claim Formulation

Let $A \in \mathbb{F}^{n \times n}$ and $u \in \mathbb{F}^n$. The prover claims that $v = Au$, i.e., for all $i \in [n]$:
$$v_i = \sum_{j=0}^{n-1} A_{ij} \, u_j.$$

Encoding in MLE language: for all $x \in \{0,1\}^\ell$,
$$\tilde{v}(x) = \sum_{b \in \{0,1\}^\ell} \tilde{A}(x, b) \, \tilde{u}(b).$$
This is a sum of $n$ terms over the Boolean hypercube in $b$, with $x$ fixed.

### 2.2 **Protocol (Sum-Check for Matrix-Vector Product):**

**Setup:** The verifier holds commitments $\mathsf{cm}(\tilde{A}), \mathsf{cm}(\tilde{u}), \mathsf{cm}(\tilde{v})$.

**Step 1 — Reduce to a single point:**  
The verifier samples $\tau \xleftarrow{\$} \mathbb{F}^\ell$ and reduces the claim "for all $x$, $\tilde{v}(x) = \ldots$" to a single evaluation:
$$\tilde{v}(\tau) = \sum_{b \in \{0,1\}^\ell} \tilde{A}(\tau, b) \, \tilde{u}(b).$$
Here $\tilde{v}(\tau)$ is obtained from the PCS opening of $\mathsf{cm}(\tilde{v})$.

**Step 2 — Apply Sum-Check:**  
Define $g: \{0,1\}^\ell \to \mathbb{F}$ by $g(b) = \tilde{A}(\tau, b) \cdot \tilde{u}(b)$.  
The verifier runs Sum-Check on the instance:
$$\sum_{b \in \{0,1\}^\ell} g(b) = \tilde{v}(\tau).$$
This is a sum over $\ell$ variables with $g$ of total degree $\leq 2\ell$ (product of two multilinear polynomials, each of degree $\ell$ in $b$-variables).

**Step 3 — Final check:**  
Sum-Check reduces to a single evaluation of $g$ at a random point $r \in \mathbb{F}^\ell$:
$$g(r) = \tilde{A}(\tau, r) \cdot \tilde{u}(r).$$
The verifier opens $\mathsf{cm}(\tilde{A})$ at $(\tau, r)$ and $\mathsf{cm}(\tilde{u})$ at $r$ to verify this product.

### 2.3 Complexity

| Parameter | Value |
|-----------|-------|
| Rounds | $\ell = \log_2 n$ |
| Prover communication | $O(\ell)$ field elements |
| Verifier computation | $O(\ell)$ field ops + 2 PCS openings |
| Soundness error | $O(\ell / |\mathbb{F}|)$ |
| Prover time (given $A$, $u$) | $O(n^2)$ — dominant cost is computing $g$ at all $b$ |

The verifier cost is **$O(\log n)$** — exponentially less than the $O(n^2)$ work of computing $v = Au$ directly.

---

## 3. Matrix-Matrix Product

### 3.1 Claim Formulation

Let $A, B, C \in \mathbb{F}^{n \times n}$ with $C = AB$. Entry-wise:
$$C_{ik} = \sum_{j=0}^{n-1} A_{ij} B_{jk}.$$
Encoding in MLE: for all $(x, z) \in \{0,1\}^\ell \times \{0,1\}^\ell$:
$$\tilde{C}(x, z) = \sum_{b \in \{0,1\}^\ell} \tilde{A}(x, b) \, \tilde{B}(b, z).$$

### 3.2 **Protocol (Two-Round Sum-Check for MatMul):**

**Step 1 — Random linear combination over output:**  
The verifier samples $\tau_1, \tau_2 \xleftarrow{\$} \mathbb{F}^\ell$ and reduces to:
$$\tilde{C}(\tau_1, \tau_2) = \sum_{b \in \{0,1\}^\ell} \tilde{A}(\tau_1, b) \, \tilde{B}(b, \tau_2).$$
The LHS is obtained from the PCS opening of $\mathsf{cm}(\tilde{C})$.

**Step 2 — Sum-Check over $b$:**  
Define $h(b) = \tilde{A}(\tau_1, b) \cdot \tilde{B}(b, \tau_2)$, a polynomial of individual degree $\leq 2$ in each $b_i$ (degree 2 because each factor is linear in $b$, so their product is quadratic: $d = 2$).

Run Sum-Check:
$$\sum_{b \in \{0,1\}^\ell} h(b) = \tilde{C}(\tau_1, \tau_2).$$
Rounds: $\ell$. Round polynomial degree per variable: $d = 2$.

**Step 3 — Final oracle query:**  
Sum-Check terminates with a random point $r^* \in \mathbb{F}^\ell$ and requires:
$$h(r^*) = \tilde{A}(\tau_1, r^*) \cdot \tilde{B}(r^*, \tau_2).$$
Two PCS openings: $\tilde{A}(\tau_1, r^*)$ and $\tilde{B}(r^*, \tau_2)$.

### 3.3 Soundness Analysis

The polynomial $h$ has total degree $\leq 2\ell$ and individual degree $\leq 2$. Soundness error per round is $d / |\mathbb{F}| = 2 / |\mathbb{F}|$. Over all $\ell$ rounds:
$$\Pr[\mathcal{V} \text{ accepts false } C] \leq \frac{2\ell}{|\mathbb{F}|} + \frac{2\ell}{|\mathbb{F}|} + \Pr[\text{PCS fails}].$$

The factor of $2\ell$ (instead of $\ell$) arises from the quadratic per-variable degree. For $|\mathbb{F}| \geq 2^{128}$, this is negligible.

### 3.4 Complexity

| Parameter | Value |
|-----------|-------|
| Rounds | $\ell = \log_2 n$ |
| Prover communication | $O(\ell)$ field elements (3 coefficients per round) |
| Verifier computation | $O(\ell)$ field ops + 2 PCS openings |
| Prover time | $O(n^2)$ to compute $h$ values across all $b \in \{0,1\}^\ell$ |
| Soundness error | $2\ell / |\mathbb{F}|$ |

This matches the $O(n^2)$ prover cost of the classical $O(n^3)$ matmul (since one factor is already known), with a **logarithmic-cost verifier**.

---

## 4. GKR-Based Protocol for Deep Matrix Products

For a sequence of matrix products $C = A^{(1)} A^{(2)} \cdots A^{(D)}$ (depth $D$), the GKR protocol applies recursively.

### 4.1 Circuit Encoding

Model the computation as a **depth-$D$ layered arithmetic circuit** where:
- Each layer $i$ computes $V^{(i)} \in \mathbb{F}^{n \times n}$ from $V^{(i-1)}$ and $A^{(i)}$.
- Layer $i$ has $n^2$ gates, each computing one entry of $V^{(i)}$ as a sum of $n$ products.

The MLE of layer $i$'s values is $\tilde{V}^{(i)}: \mathbb{F}^{2\ell} \to \mathbb{F}$.

### 4.2 Recursive Reduction (GKR)

For a random point $\tau = (\tau_1, \tau_2) \in \mathbb{F}^{2\ell}$:
$$\tilde{V}^{(i)}(\tau_1, \tau_2) = \sum_{b \in \{0,1\}^\ell} \tilde{V}^{(i-1)}(\tau_1, b) \cdot \tilde{A}^{(i)}(b, \tau_2).$$

Apply Sum-Check to reduce this to a single evaluation of $\tilde{V}^{(i-1)}$ at a new random point. Repeat for layers $i = D, D-1, \dots, 1$.

**Net cost:**
- **Prover:** $O(D \cdot n^2)$ total.
- **Verifier:** $O(D \cdot \ell)$ field ops + $D$ PCS openings (one per matrix $A^{(i)}$).
- **Proof size:** $O(D \cdot \ell)$ field elements.

For $D = O(\log n)$ layers (deep networks, etc.), this is **$O(\log^2 n)$ verifier time** for products of $O(\log n)$ matrices of size $n \times n$.

### 4.3 **Theorem (GKR for Iterated MatMul, informal):**
There exists an interactive proof for the claim $C = \prod_{i=1}^D A^{(i)}$ with:
- Proof length $O(D \log n)$ field elements.
- Verifier time $O(D \log n + D \cdot T_{\text{open}})$, where $T_{\text{open}}$ is the PCS opening verification cost.
- Prover time $O(D \cdot n^2)$.
- Soundness error $O(D \log n / |\mathbb{F}|)$.

---

## 5. Vector Inner Product and Bilinear Forms

### 5.1 Inner Product $\langle u, v \rangle$

The inner product is the degenerate case: $C = u^T v \in \mathbb{F}$ (a scalar). Encoding:
$$\langle u, v \rangle = \sum_{b \in \{0,1\}^\ell} \tilde{u}(b) \, \tilde{v}(b).$$

Sum-Check over $b \in \{0,1\}^\ell$ as before. The round polynomial $s_j$ has individual degree $\leq 2$. Proof size: $O(\ell)$ field elements. Verifier: $O(\ell)$ + 2 PCS openings.

### 5.2 Matrix Quadratic Form $u^T A v$

A **bilinear form** $u^T A v$ for $A \in \mathbb{F}^{n \times n}$, $u, v \in \mathbb{F}^n$:
$$u^T A v = \sum_{i,j \in \{0,1\}^\ell} \tilde{u}(i) \, \tilde{A}(i, j) \, \tilde{v}(j).$$

This is a sum over $2\ell$ Boolean variables. The summand is a product of three multilinear functions (each of degree $\leq 1$ in each variable), giving individual degree $\leq 3$ and total degree $\leq 3\ell$ overall.

**Protocol:** Run a single Sum-Check over the $2\ell$-dimensional hypercube:
$$\sum_{(i,j) \in \{0,1\}^{2\ell}} \tilde{u}(i) \, \tilde{A}(i,j) \, \tilde{v}(j) = u^T A v.$$
Rounds: $2\ell$. Degree per round: $d \leq 3$. Total soundness error: $6\ell / |\mathbb{F}|$. Three PCS openings at the end.

### 5.3 Batch Inner Products: VMATVEC

Given $k$ vectors $u^{(1)}, \dots, u^{(k)}$ and a fixed matrix $A$, prove all $k$ products $v^{(i)} = Au^{(i)}$ simultaneously.

**Method 1 — Independent repetitions:** Run $k$ separate Sum-Check instances. Cost: $k \times O(\ell)$ per operation. But this is the naïve approach.

**Method 2 — Random linear combination (batch):**  
Sample $\rho_1, \dots, \rho_k \xleftarrow{\$} \mathbb{F}$. Define:
$$\bar{u} := \sum_{i=1}^k \rho_i u^{(i)}, \qquad \bar{v} := \sum_{i=1}^k \rho_i v^{(i)}.$$
Verify $\bar{v} = A \bar{u}$ using a **single** Sum-Check. If any $v^{(i)} \neq Au^{(i)}$, the claim $\bar{v} = A\bar{u}$ fails except with probability $\leq k\ell / |\mathbb{F}|$ (by Schwartz-Zippel).

**Cost:** $O(\ell)$ field ops + $O(k)$ to form the combination. Amortized cost per product: $O(\ell / k)$.

---

## 6. Rectangular and Non-Square Matrices

For $A \in \mathbb{F}^{m \times n}$ with $m = 2^{\ell_1}$ and $n = 2^{\ell_2}$, $\ell_1 \neq \ell_2$:

The MLE becomes $\tilde{A}: \mathbb{F}^{\ell_1} \times \mathbb{\mathbb{F}}^{\ell_2} \to \mathbb{F}$.

**Matrix-vector product $v = Au$, $u \in \mathbb{F}^n$:** Sum-Check over $\ell_2$ variables, round polynomial degree $d \leq 2$.

**Matrix-matrix product $C = AB$, $A \in \mathbb{F}^{m \times n}$, $B \in \mathbb{F}^{n \times p}$:** Sum-Check over $\ell_2$ (inner dimension) variables.

| Shape of $C = AB$ | inner dimension | Sum-Check vars | Rounds |
|--------------------|-----------------|----------------|--------|
| $m \times p$ | $n$ | $\ell_2 = \log_2 n$ | $\ell_2$ |
| $n \times n$ (square) | $n$ | $\ell = \log_2 n$ | $\ell$ |
| $1 \times n$ (row) $\times$ $n \times 1$ (col) | $n$ | $\ell$ | $\ell$ |

The number of rounds always depends on the **inner (contracted) dimension**, not the output shape.

---

## 7. Sparse Matrices

### 7.1 Sparsity-Aware Sum-Check

Let $A$ have $s \ll n^2$ nonzero entries. Encode $A$ as a list of $(i, j, A_{ij})$ triples.

The prover cannot evaluate $\tilde{A}(\tau, b)$ for all $b \in \{0,1\}^\ell$ in $O(n^2)$ if $A$ is large but sparse. Instead:

**Sparse MLE evaluation:** Given the list of $s$ nonzero entries, evaluate $\tilde{A}(\tau, b)$ for all $b \in \{0,1\}^\ell$ in $O(s \cdot \ell)$ (instead of $O(n^2)$).

**Proof:** Each nonzero $(i, j, A_{ij})$ contributes $A_{ij} \cdot \chi_i(\tau) \cdot \chi_j(b)$ to $\tilde{A}(\tau, b)$. The factor $\chi_i(\tau)$ is a fixed scalar (compute once per $i$ in $O(\ell)$). Accumulate $s$ such terms for each $b$.

**Total prover time** for the Sum-Check: $O(s \cdot \ell)$ instead of $O(n^2 \log n)$.  
For $s = O(n)$ (sparse), this is $O(n \log n)$ — near-linear in the matrix size.

### 7.2 **Corollary (Sparse MatVec Sum-Check):**
For a sparse matrix $A$ with $s$ nonzeros and vector $u$, there exists a proof system with:
- **Prover time:** $O(s \cdot \ell)$, i.e., $O(s \log n)$.
- **Verifier time:** $O(\ell)$, i.e., $O(\log n)$.
- **Proof size:** $O(\ell)$ field elements.
- **Soundness error:** $O(\ell / |\mathbb{F}|)$.

This is asymptotically optimal: it matches the cost of simply reading the sparse matrix.

---

## 8. Summary: Protocol Comparison

| Operation | Prover Time | Verifier Time | Rounds | $d$ (degree) |
|-----------|------------|---------------|--------|--------------|
| Inner product $\langle u, v \rangle$ | $O(n)$ | $O(\ell)$ | $\ell$ | 2 |
| Matrix-vector $v = Au$ | $O(n^2)$ | $O(\ell)$ | $\ell$ | 2 |
| Bilinear form $u^T A v$ | $O(n^2)$ | $O(\ell)$ | $2\ell$ | 3 |
| Matrix-matrix $C = AB$ | $O(n^2)$ | $O(\ell)$ | $\ell$ | 2 |
| Iterated matmul (depth $D$) | $O(D n^2)$ | $O(D\ell)$ | $D\ell$ | 2 |
| Batch $k$ MatVec (random comb.) | $O(n^2 + kn)$ | $O(\ell)$ | $\ell$ | 2 |
| Sparse MatVec ($s$ nnz) | $O(s\ell)$ | $O(\ell)$ | $\ell$ | 2 |

In every case the verifier achieves **$O(\log n)$** cost — independent of the natural $\Omega(n^2)$ or $\Omega(n^3)$ cost of the operation itself.

---

## References

- Goldwasser, S., Kalai, Y. T., & Rothblum, G. N. (2015). *Delegating Computation: Interactive Proofs for Muggles*. Journal of the ACM, 62(4), Article 27. (GKR)
- Thaler, J. (2013). *Time-optimal interactive proofs for circuit evaluation*. CRYPTO 2013. (Prover-efficient GKR)
- Thaler, J. (2022). *Proofs, Arguments, and Zero-Knowledge* (Chp. 4–6). Georgetown University. [ProofsArgsAndZK.pdf](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf).
- Setty, S. (2020). *Spartan: Efficient and general-purpose zkSNARKs without trusted setup*. CRYPTO 2020.
- Wahby, R. S., Tzialla, I., Shelat, A., Thaler, J., & Walfish, M. (2018). *Doubly-efficient zkSNARKs without trusted setup*. IEEE S&P 2018. (Hyrax + GKR)
- Zhang, Y., Genkin, D., Katz, J., Papadopoulos, D., & Papamanthou, C. (2017). *vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases*. IEEE S&P 2017.
- Bootle, J., Cerulli, A., Chaidos, P., Groth, J., & Petit, C. (2016). *Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting*. EUROCRYPT 2016.
