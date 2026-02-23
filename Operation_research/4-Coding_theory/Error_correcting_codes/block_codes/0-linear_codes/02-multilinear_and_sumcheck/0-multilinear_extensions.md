# Multilinear Polynomials and the Multilinear Extension

This conspectus introduces the algebraic foundation for all subsequent topics: the **multilinear extension (MLE)** of a function. A polynomial is *multilinear* if it has degree at most 1 in each variable separately. The MLE is the unique such polynomial that matches a given function on the Boolean hypercube, and it serves as the central object in both the Sum-Check Protocol and multilinear secret sharing.

---

## 1. Multivariate Polynomial Background

### 1.1 Polynomial Rings in Several Variables

Let $\mathbb{F}$ be a finite field and $\ell \in \mathbb{N}$. The **polynomial ring in $\ell$ variables** over $\mathbb{F}$ is:
$$\mathbb{F}[x_1, \dots, x_\ell]$$
Elements are finite $\mathbb{F}$-linear combinations of **monomials** $x_1^{e_1} \cdots x_\ell^{e_\ell}$, $e_i \in \mathbb{N}_0$.

The **total degree** of a monomial is $\sum_{i=1}^\ell e_i$; the **individual degree in $x_i$** is $e_i$.

### 1.2 **Definition (Multilinear Polynomial):** 
A polynomial $\tilde{f} \in \mathbb{F}[x_1, \dots, x_\ell]$ is **multilinear** if for every $i \in [\ell]$ the degree of $\tilde{f}$ in $x_i$ is at most $1$. Equivalently, every monomial that appears has the form
$$\prod_{i \in S} x_i, \quad S \subseteq [\ell].$$
The number of distinct such monomials—and hence the dimension of the vector space of multilinear polynomials over $\mathbb{F}^\ell$—is exactly $2^\ell$.

### 1.3 Lagrange Basis on the Hypercube

Every multilinear polynomial is uniquely determined by its values on the **Boolean hypercube** $\{0,1\}^\ell$. The natural basis for multilinear functions over the hypercube is given by **multilinear Lagrange basis polynomials**:

$$\chi_w(x_1, \dots, x_\ell) := \prod_{i=1}^\ell \bigl( x_i w_i + (1 - x_i)(1 - w_i) \bigr), \quad w \in \{0,1\}^\ell.$$

**Properties of $\chi_w$:**
- **Interpolation:** $\chi_w(v) = \mathbf{1}[v = w]$ for all $v \in \{0,1\}^\ell$.
- **Partition of unity:** $\sum_{w \in \{0,1\}^\ell} \chi_w(x) = 1$ for all $x \in \mathbb{F}^\ell$.
- **Degree:** Each $\chi_w$ is multilinear of total degree exactly $\ell$.

---

## 2. The Multilinear Extension (MLE)

### 2.1 **Definition (Multilinear Extension):**
Let $f: \{0,1\}^\ell \to \mathbb{F}$ be any function. Its **multilinear extension** is the polynomial $\tilde{f}: \mathbb{F}^\ell \to \mathbb{F}$ defined by:
$$\tilde{f}(x_1, \dots, x_\ell) := \sum_{w \in \{0,1\}^\ell} f(w) \cdot \chi_w(x_1, \dots, x_\ell).$$

This is simply Lagrange interpolation over the Boolean hypercube using the basis $\{\chi_w\}$.

### 2.2 **Theorem (Uniqueness of the MLE):**
The multilinear extension $\tilde{f}$ is the **unique** multilinear polynomial that agrees with $f$ on $\{0,1\}^\ell$.

**Proof:**
- **Existence:** The formula above provides a multilinear polynomial (linear combination of multilinear $\chi_w$'s) that agrees with $f$ on every $w \in \{0,1\}^\ell$: $\tilde{f}(w) = \sum_v f(v)\mathbf{1}[v=w] = f(w)$. ✓
- **Uniqueness:** Suppose $g$ and $h$ are both multilinear and agree on $\{0,1\}^\ell$. Then $p = g - h$ is multilinear and vanishes on $\{0,1\}^\ell$. In $x_1$, write $p = x_1 A(x_2, \dots) + B(x_2, \dots)$. Setting $x_1 = 0$ and $x_1 = 1$ yields $B \equiv 0$ and $A \equiv 0$ on $\{0,1\}^{\ell-1}$. By induction on $\ell$, $p \equiv 0$.  $\square$

### 2.3 Explicit Coefficient Representation

Via Möbius inversion on the Boolean lattice, one can expand the MLE in the **multilinear monomial basis**:
$$\tilde{f}(x) = \sum_{S \subseteq [\ell]} \hat{f}(S) \prod_{i \in S} x_i,$$
where the **Möbius coefficients** $\hat{f}(S)$ are given by:
$$\hat{f}(S) = \sum_{T \subseteq S} (-1)^{|S \setminus T|} f(T).$$

**Complexity of Evaluation:**  
Given the $2^\ell$ values $f(w)$, evaluating $\tilde{f}$ at a single point $r \in \mathbb{F}^\ell$ takes $O(2^\ell)$ field operations via the **dynamic-programming sum-product formula**:
$$\tilde{f}(r_1, \dots, r_\ell) = \sum_{w \in \{0,1\}^\ell} f(w) \prod_{i=1}^\ell \bigl( r_i w_i + (1-r_i)(1-w_i) \bigr).$$
This can be computed with $O(\ell \cdot 2^\ell)$ multiplications by processing one coordinate at a time.

---

## 3. Key Properties of the MLE

### 3.1 Linearity
The map $f \mapsto \tilde{f}$ is a **linear** map from $\mathbb{F}^{2^\ell}$ to the space of multilinear polynomials:
$$\widetilde{f + g} = \tilde{f} + \tilde{g}, \qquad \widetilde{\alpha f} = \alpha \tilde{f}.$$

### 3.2 Schwartz-Zippel Bound for Multilinear Polynomials

**Corollary (of Schwartz-Zippel):**
Let $\tilde{f} \not\equiv 0$ be a multilinear polynomial over $\mathbb{F}$ in $\ell$ variables (total degree $\leq \ell$). If $r \in S^\ell$ is chosen uniformly at random:
$$\Pr[\tilde{f}(r) = 0] \leq \frac{\ell}{|S|}.$$

**Consequence for Polynomial Identity Testing:** Two functions $f, g: \{0,1\}^\ell \to \mathbb{F}$ are identical if and only if $\tilde{f} \equiv \tilde{g}$. By the above, for a random $r \in \mathbb{F}^\ell$, $\tilde{f}(r) = \tilde{g}(r)$ with probability at most $\ell / |\mathbb{F}|$ when $f \neq g$. This gives a **one-round probabilistic test** for multilinear identity.

### 3.3 Local Computation via Restriction

For any fixed values $r_1, \dots, r_k \in \mathbb{F}$, the **restriction** of a multilinear polynomial $\tilde{f}$ to $x_1 = r_1, \dots, x_k = r_k$ is again multilinear (in $x_{k+1}, \dots, x_\ell$). This **locality under restriction** is the key mechanism exploited in the Sum-Check Protocol.

### 3.4 Tensor Product Structure

The space of multilinear polynomials on $\mathbb{F}^\ell$ is isomorphic to the **$\ell$-fold tensor product** of the 2-dimensional space spanned by $\{1, x\}$:
$$\text{MLin}(\mathbb{F}^\ell) \cong \mathbb{F}[x_1]/\langle x_1^2 - x_1\rangle \otimes \cdots \otimes \mathbb{F}[x_\ell]/\langle x_\ell^2 - x_\ell\rangle.$$
This allows vectorized simultaneous evaluation which is important for efficient proof systems.

---

## 4. Evaluating the MLE: Algorithms

### 4.1 Bookkeeping Algorithm (Streaming)
**Input:** Values $f: \{0,1\}^\ell \to \mathbb{F}$ stored in a table $T$ of size $N = 2^\ell$; query point $r = (r_1, \dots, r_\ell) \in \mathbb{F}^\ell$.  
**Output:** $\tilde{f}(r)$.

```
For j = 1 to ℓ:
    For each w ∈ {0,1}^(ℓ−j):
        T[w] ← (1 − r_j) · T[0 ∥ w] + r_j · T[1 ∥ w]
Return T[ε]    (the single remaining entry)
```

**Time:** $O(\ell \cdot 2^\ell)$ = $O(N \log N)$.  
**Space:** $O(N)$ (in-place).

This is the canonical algorithm used in practice by verifiable computation systems (Spartan, HyperPlonk, etc.).

### 4.2 Streaming Evaluation for Linear Layers

When $f$ is the witness (satisfying assignment) in a arithmetic circuit, the evaluator (prover) must produce $\tilde{f}(r)$ without storing all $2^\ell$ entries. This leads to the notion of a **witness-efficient prover**, an active research topic in SNARK design.

---

## References

- Thaler, J. (2022). *Proofs, Arguments, and Zero-Knowledge* (Chp. 3: Multilinear Extensions). [bookmarks.cs.utexas.edu/~thaler](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf).
- Lund, C., Fortnow, L., Karloff, H., & Nisan, N. (1992). *Algebraic methods for interactive proof systems*. Journal of the ACM, 39(4), 859–868.
- Goldwasser, S., Kalai, Y. T., & Rothblum, G. N. (2015). *Delegating Computation: Interactive Proofs for Muggles*. Journal of the ACM, 62(4), Article 27.
- Spartan (2020). Setty, S. *Spartan: Efficient and general-purpose zkSNARKs without trusted setup*. CRYPTO 2020.
