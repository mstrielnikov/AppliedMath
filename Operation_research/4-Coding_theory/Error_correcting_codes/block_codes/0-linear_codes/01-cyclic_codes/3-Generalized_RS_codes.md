# Generalized Reed-Solomon (GRS) Codes

Generalized Reed-Solomon (GRS) codes extend the powerful properties of standard Reed-Solomon codes to arbitrary evaluation points. While they lose the strict cyclic structure, they retain the **Maximum Distance Separable (MDS)** property and serve as the foundation for modern code-based cryptography.

---

## 1. Definition and Construction

Unlike classical RS codes that require evaluation at roots of unity (forming a cyclic group), GRS codes allow evaluations at **any** distinct points in the field, with optional column scaling.

### 1.1 The Definition
A GRS code $\mathcal{C}_{GRS}(n, k, \vec{\alpha}, \vec{v})$ over $\mathbb{F}_q$ is defined by:
- **Evaluation Points**: $\vec{\alpha} = (\alpha_1, \dots, \alpha_n)$, where all $\alpha_i \in \mathbb{F}_q$ are distinct.
- **Column Multipliers**: $\vec{v} = (v_1, \dots, v_n)$, where all $v_i \in \mathbb{F}_q \setminus \{0\}$.

A vector $c = (c_1, \dots, c_n)$ is a codeword if there exists a polynomial $f(x)$ of degree $< k$ such that:
$$c_i = v_i f(\alpha_i) \quad \text{for } i=1, \dots, n$$
Standard RS codes are the special case where $\alpha_i = \gamma^{i-1}$ (powers of a primitive root) and $v_i = 1$ (or specific values for the cyclic view).

### 1.2 Matrix Representation
The Generator Matrix is a **Weighted Vandermonde Matrix**:
$$G = \begin{pmatrix} v_1 & v_2 & \dots & v_n \\ v_1 \alpha_1 & v_2 \alpha_2 & \dots & v_n \alpha_n \\ \vdots & \vdots & \ddots & \vdots \\ v_1 \alpha_1^{k-1} & v_2 \alpha_2^{k-1} & \dots & v_n \alpha_n^{k-1} \end{pmatrix}$$
This matrix always has rank $k$ because the determinant of any $k \times k$ submatrix involves a Vandermonde determinant of distinct points $\alpha_i$, which is non-zero.

---

## 2. Properties and Analogies

| Feature | Classical BCH / RS | Generalized RS (GRS) |
| :--- | :--- | :--- |
| **Domain** | Primitive Roots of Unity | Arbitrary Distinct Points |
| **Structure** | Cyclic (Ideal in $R_n$) | Linear (Subspace of $\mathbb{F}_q^n$) |
| **Distance** | MDS ($d = n - k + 1$) | MDS ($d = n - k + 1$) |
| **Duality** | Dual is also Cyclic | The Dual of a GRS is a GRS code |
| **Decoding** | Berlekamp-Massey / Euclidean | Generalized Berlekamp-Massey |

### 2.1 The MDS Property refined
The GRS construction is the most general way to produce MDS codes over large fields. The proof relies solely on the fact that a non-zero polynomial of degree $< k$ has at most $k-1$ zeros. The multipliers $v_i$ do not affect zero locations, so the weight distribution is preserved.

---

## 3. Connection to Algebra: Chinese Remainder Theorem

The construction of GRS codes is structurally identical to the **Chinese Remainder Theorem (CRT)** for polynomials.

### 3.1 The Evaluation Map as CRT
The construction of GRS codes is structurally identical to the **Chinese Remainder Theorem (CRT)** for polynomials.
Consider the ring of polynomials $\mathbb{F}_q[x]$. Evaluation at $\alpha_i$ is equivalent to reduction modulo $(x - \alpha_i)$. The evaluation map:
$$\Phi: f(x) \mapsto (f(\alpha_1), \dots, f(\alpha_n))$$
is actually the CRT isomorphism:
$$\mathbb{F}_q[x] / \langle \prod (x - \alpha_i) \rangle \xrightarrow{\cong} \bigoplus_{i=1}^n \mathbb{F}_q[x] / \langle x - \alpha_i \rangle \cong \mathbb{F}_q^n$$
Since $\deg(f) < k \leq n$, the polynomial is uniquely identified by its residues. This perspective allows GRS decoding to be viewed as a **CRT Reconstruction** problem (or "Robust CRT" when errors are present).

## 4. Advanced Structural Insights (from Literature)

Recent research (e.g., *Quintin, Barbier, Chabot*) generalizes GRS codes beyond fields to commutative and even noncommutative rings.

### 4.1 Generalization over Rings
A GRS code can be defined over a ring $A$ if the evaluation points $x_1, \dots, x_n$ belong to the **center** $Z(A)$ and satisfy the **commutative subtractive** property ($x_i - x_j \in A^\times$ for $i \neq j$).
- **Significance**: This allows construction of codes over modular rings like $\mathbb{Z}_{p^r}$, enabling **lifting decoding** schemes where a solution modulo $p$ is lifted to modulo $p^r$.

### 4.2 Key Theorems
1.  **Duality**: The dual of a GRS code is **always** a GRS code.
    $$GRS_k(\vec{\alpha}, \vec{v})^\perp = GRS_{n-k}(\vec{\alpha}, \vec{v}')$$
    where $\vec{v}'$ is a uniquely determined weight vector.
2.  **Schur Product**: The component-wise product of two GRS codes is a GRS code.
    $$GRS_{k_1} \ast GRS_{k_2} = GRS_{k_1+k_2-1}$$
    **Application**: This property is used in the **distinguisher** for the Sidelnikov-Shestakov attack, as random linear codes do not possess this property.

---

## 5. Cryptographic Applications

GRS codes are central to **Code-Based Cryptography**, particularly in the **McEliece Cryptosystem**, which relies on the hardness of decoding a distinct linear code.

### 4.1 McEliece and GRS Insecurity
The original McEliece proposal uses a hidden code $\mathcal{C}$ masked by scrambling matrices $S$ and $P$ ($G_{pub} = S G P$).
- **Naive GRS**: If the hidden code is a raw GRS code, the scheme is **insecure**. The **Sidelnikov-Shestakov attack** (1992) exploits the rigid Vandermonde structure to recover $(\vec{\alpha}, \vec{v})$ in polynomial time.
- **The Fix (Goppa Codes)**: Secure McEliece uses **Binary Goppa Codes**. These are **subfield subcodes** of GRS codes. By restricting the code to binary vectors ($ \mathcal{C}_{Goppa} = \mathcal{C}_{GRS} \cap \mathbb{F}_2^n $), the algebraic structure is "hidden" enough to resist structural attacks while still admitting efficient decoding.

### 4.2 Binary Cases and Alternant Codes
Since GRS codes are defined over $\mathbb{F}_{q^m}$, they are not directly useful for binary transmission unless we modify them.
- **Alternant Codes**: The restriction of a GRS code over $\mathbb{F}_{q^m}$ to the base field $\mathbb{F}_q$.
- **Binary Image**: Mapping each extension field element to $m$ bits. This preserves linearity but usually breaks the MDS property.

---

## 5. Application: Secret Sharing
The most famous application of GRS codes is **Shamir's Secret Sharing**.
-   The vector of shares $(y_1, \dots, y_n)$ corresponds exactly to a GRS codeword with random evaluation points.
-   For a deep dive into the **Byzantine Tolerance** of this scheme and its **Syndrome Decoding** (Welch-Berlekamp), see the dedicated conspectus:
    -   **[Polynomial Secret Sharing & Byzantine Tolerance](7-Polynomial_secret_sharing.md)**

## References
- MacWilliams, F. J., & Sloane, N. J. A. (1977). *The Theory of Error-Correcting Codes*.
- Bernstein, D. J., et al. (2008). *Post-Quantum Cryptography*. (Chapter on Code-Based Cryptography).
- Sidelnikov, V. M., & Shestakov, S. O. (1992). *On insecurity of cryptosystems based on generalized Reed-Solomon codes*.
- Wikipedia contributors. *Generalized Reed-Solomon code, Goppa code, McEliece cryptosystem*.
