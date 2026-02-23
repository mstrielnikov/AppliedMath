# BCH Codes: Multiple Error Correction

Bose-Chaudhuri-Hocquenghem (BCH) codes are a powerful class of cyclic codes that generalize the concept of Hamming codes to allow for the correction of multiple errors. They are defined by the roots of their generator polynomials in an extension field.

## 1. Foundations: Algebraic Construction

### 1.1 Finite Field Extension
BCH codes over a base field $\mathbb{F}_q$ (usually $\mathbb{F}_2$) are constructed using an extension field $\mathbb{F}_{q^m}$, where $n = q^m - 1$ is the block length.
- **$\alpha$**: A **primitive element** (or primitive $n$-th root of unity) in $\mathbb{F}_{q^m}$, meaning $\alpha^n = 1$ and all non-zero elements are powers of $\alpha$.
- The code structure is determined by selecting a sequence of powers of $\alpha$ as required roots.

### 1.2 Minimal Polynomials
For any element $\beta \in \mathbb{F}_{q^m}$, its **minimal polynomial** $m_\beta(x)$ is the lowest-degree monic polynomial in $\mathbb{F}_q[x]$ such that $m_\beta(\beta) = 0$.
- For BCH codes, we are interested in $m_{\alpha^i}(x)$.
- All elements in the same **conjugacy class** (orbit under the Frobenius map $z \mapsto z^q$) share the same minimal polynomial.

### 1.3 Generator Polynomial $g(x)$
A BCH code with **designed distance** $\delta$ is a cyclic code whose generator polynomial $g(x)$ is the least common multiple of the minimal polynomials of $\delta-1$ consecutive powers of $\alpha$:
$$g(x) = \text{lcm}\{m_{\alpha^l}(x), m_{\alpha^{l+1}}(x), \dots, m_{\alpha^{l+\delta-2}}(x)\}$$
- **Narrow-sense BCH**: $l=1$.
- **Primitive BCH**: $n = q^m - 1$.

## 2. Parameters and the BCH Bound

### 2.1 Minimum Distance
**Theorem (BCH Bound):** The minimum distance $d$ of a BCH code is at least its designed distance $\delta$:
$$d \geq \delta$$
This guarantees that the code can correct at least $t = \lfloor (\delta-1)/2 \rfloor$ errors.

### 2.2 Dimension and Rate
The dimension $k$ of the code is $n - \deg(g(x))$.
- **The Trade-off**: As the designed distance $\delta$ increases, the number of required roots in $g(x)$ grows, increasing $\deg(g(x))$ and thus **reducing the Code Rate ($R$)**.
- This is the fundamental "cost of reliability" in BCH codes: to correct more errors, one must transmit more parity bits and fewer information bits.

## 3. The Decoding Pipeline

Decoding BCH codes involves an algebraic process to identify error locations $X_i$ and (for non-binary) error magnitudes $Y_i$.

### 3.1 Step 1: Syndrome Evaluation
Calculate symbols $S_1, S_2, \dots, S_{\delta-1}$ by evaluating the received polynomial $R(x)$ at the powers of $\alpha$:
$$S_j = R(\alpha^j) = \sum_{k=0}^{n-1} r_k (\alpha^j)^k$$
If all syndromes are zero, no errors are detected.

### 3.2 Step 2: The Key Equation
The syndromes $S_j$ are related to the **Error Locator Polynomial** $\Lambda(x) = \prod_{i=1}^t (1 - X_i x)$, where $X_i$ are the locations of the errors:
$$\Lambda(x) S(x) \equiv \Omega(x) \pmod{x^{\delta-1}}$$

### 3.3 Step 3: Solving for $\Lambda(x)$
Two primary algorithms exist to find $\Lambda(x)$ from the syndromes:
1.  **Peterson-Gorenstein-Zierler (PGZ)**: Solves a system of $t$ linear equations. Efficient for very small $t$ (e.g., $t \leq 3$).
2.  **Berlekamp-Massey Algorithm**: An iterative algorithm that finds the shortest Linear Feedback Shift Register (LFSR) that generates the syndrome sequence. This is the standard for practical implementations.

### 3.4 Step 4: Finding Roots (Chien Search)
The roots of $\Lambda(x)$ correspond to the inverses of the error locations. Since we are in a finite field, we use **Chien Search**—an exhaustive but hardware-efficient test of all possible locations $\alpha^i$.

### 3.5 Step 5: Error Correction
- **Binary BCH**: Once a root $\alpha^{-i}$ is found, the error at position $i$ is corrected by flipping the bit.
- **q-ary BCH**: Use **Forney’s Algorithm** to calculate specific error values $Y_i$.

## 4. Relationship to Other Codes
- **Hamming Codes**: Binary BCH codes with $\delta=3$ are equivalent to Hamming codes.
- **Reed-Solomon Codes**: These are $q$-ary BCH codes where the extension degree $m=1$ (roots are in the base field).

---

## 5. References
- Couvreur, A. (n.d.). *Lecture Notes on Coding Theory*. École Polytechnique / CNRS. [PDF](https://www.lix.polytechnique.fr/~alain.couvreur/doc_ens/lecture_notes.pdf).
- Guruswami, V. (2004). *BCH Codes and Decoding*. MIT OCW 6.895. [Lecture Notes](https://ocw.mit.edu/courses/6-895-essential-coding-theory-fall-2004/pages/lecture-notes/).
- Wikipedia contributors. (n.d.). *BCH code, Berlekamp–Massey algorithm, Peterson–Gorenstein–Zierler algorithm*. Wikipedia, The Free Encyclopedia.
