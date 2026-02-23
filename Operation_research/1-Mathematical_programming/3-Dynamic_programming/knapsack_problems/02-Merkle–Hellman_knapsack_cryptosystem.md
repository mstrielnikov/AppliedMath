# Merkle–Hellman Knapsack Cryptosystem

A legacy public-key cryptosystem based on the Knapsack problem. While initially promising, it is now considered **insecure** due to attacks exploiting the specific structure of its keys.

## 1. System Formalization

The security relies on transforming an "easy" knapsack problem (Superincreasing) into a "hard" one (General) using a modular transformation. This transformation acts as the **trapdoor**.

*   **Hard Knapsack**: General Subset Sum problem (NP-complete). Given random $a_i$, finding binary $x_i$ such that $\sum x_i a_i = S$ is computationally difficult.
*   **Easy Knapsack**: Superincreasing Knapsack. Solvable in polynomial time $O(n)$.
*   **Trapdoor**: The pair $(r, q)$ that converts the superincreasing sequence to a pseudo-random one.

### 1.1 Key Generation

**1. Private Key (The "Easy" Knapsack)**
Construct a superincreasing sequence $W = (w_1, w_2, \dots, w_n)$.
*   **Superincreasing Condition**: Each element is strictly greater than the sum of all preceding elements.
    $$w_k > \sum_{i=1}^{k-1} w_i \quad \text{for } k=2, \dots, n$$

**2. Modular Parameters**
Choose a modulus $q$ and multiplier $r$ such that:
*   $q > \sum_{i=1}^n w_i$ (to prevent modular wrapping of sums).
*   $\gcd(r, q) = 1$ (to ensure existence of inverse $r^{-1}$).

**3. Public Key (The "Hard" Knapsack)**
Compute the sequence $\beta = (b_1, b_2, \dots, b_n)$ where:
$$b_i = r \cdot w_i \pmod q$$

The public key is $\beta$. The private key is $(W, q, r)$.

### 1.2 Encryption

To encrypt an $n$-bit binary message $m = (m_1, m_2, \dots, m_n)$:
Compute ciphertext $C$ as the subset sum of the public key:
$$C = \sum_{i=1}^n m_i b_i$$

### 1.3 Decryption

1.  **Transform Ciphertext**: The receiver uses the private inverse $r^{-1}$ to map the "hard" ciphertext $C$ back to the "easy" sum $C'$.
    $$C' = C \cdot r^{-1} \pmod q$$
    *Proof*: $C \cdot r^{-1} = (\sum m_i r w_i) r^{-1} = \sum m_i w_i \pmod q$. Since $q$ is larger than the total sum, the modular equality implies equality in $\mathbb{Z}$.

2.  **Solve Superincreasing Knapsack (Greedy Algorithm)**:
    Since $W$ is superincreasing, there is a unique solution for $C'$ solvable by taking the largest elements first.
    *   Iterate from $i = n$ down to $1$:
        *   If $C' \ge w_i$, then set $m_i = 1$ and $C' \leftarrow C' - w_i$.
        *   Else set $m_i = 0$.

## 2. Cryptoanalysis (Shamir's Attack)

Shamir (1982) showed that the Merkle-Hellman system can be broken using **Lattice Reduction**. The attack does not solve the NP-complete knapsack problem but rather exploits the specific structure of the public key to recover the private key (or an equivalent one).

### 2.1 Intuition
The public key elements $b_i$ are not random; they are linear transformations of small, superincreasing numbers $w_i$.
$$ b_i = r w_i - k_i q \quad \implies \quad \frac{b_i}{q} \approx \frac{k_i}{r^{-1} \pmod q} $$
This relationship represents a specific type of **Simultaneous Diophantine Approximation**. A lattice constructed from $b_i$ will contain a vector associated with the private key that is significantly shorter than vectors in a random lattice.

### 2.2 LLL Attack (Reconstructing the Trapdoor)

**Input (Lattice Basis)**:
Typical construction for finding the trapdoor parameters involves a lattice basis matrix $\mathbf{B}$ formed by the public key elements. A simplified variant (ignoring scaling factors) is:
$$
\mathbf{B} = \begin{pmatrix}
1 & 0 & \dots & 0 & b_1 \\
0 & 1 & \dots & 0 & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 1 & b_n \\
0 & 0 & \dots & 0 & K \cdot q \\ 
\end{pmatrix}
$$
*(Note: Attacks often guess $q$ or work with approximations)*

**Output (LLL Reduction)**:
The **Lenstra-Lenstra-Lovász (LLL)** algorithm takes this basis and returns a "reduced" basis containing short vectors.
*   One of these short vectors corresponds to the relation $b_i u - k_i q = w_i$ where $w_i$ are small.
*   Specifically, LLL finds parameters that reveal the superincreasing structure (or a sequence close enough to it).

Once the ratio $u/q'$ (approximation of $r/q$) is found, the attacker can transform the public key $\beta$ back into a superincreasing sequence and decrypt messages just like the legitimate receiver.

---

## 3. Context & Related Problems

*   **[Subset Sum Problem](01-subset_sum_problem.md)**: The underlying hard problem that forms the basis of this cryptosystem.
*   **[Knapsack Problem](00-knapsack_problem.md)**: The general optimization problem class.

---

## References
1.  **Wikipedia**: [Merkle–Hellman knapsack cryptosystem](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem)
2.  **Shamir, A.** (1982). "A Polynomial Time Algorithm for Breaking the Basic Merkle-Hellman Cryptosystem".
3.  **LLL Algorithm**: Lenstra, Lenstra, and Lovász (1982).
