# Subset Sum Problem

## 1. Formal Definition

Given a multiset of integers $S = \{a_1, a_2, \dots, a_n\}$ and a target integer $T$, the **Subset Sum Problem** asks whether there exists a non-empty subset $S' \subseteq S$ such that the sum of the elements in $S'$ equals $T$.
$$
\sum_{a \in S'} a = T
$$

### Relation to Partition Problem
The **Partition Problem** is a special case of Subset Sum where the target is exactly half the total sum of the set ($T = \frac{1}{2} \sum S$). It asks if $S$ can be partitioned into two subsets with equal sums.

*   **Reduction (Partition $\to$ Subset Sum)**: Direct instance where $T = \text{Total}/2$.
*   **Reduction (Subset Sum $\to$ Partition)**: To decide if subset of $S$ sums to $T$, construct set $S' = S \cup \{|\sum S - 2T|\}$. A partition of $S'$ exists iff a subset of $S$ sums to $T$.

## 2. Complexity Class & Proof

The Subset Sum problem is **NP-complete**.
-   **In NP**: A certificate (the subset) can be summed in $O(N)$ to verify the target.
-   **NP-Hardness Proof (Outline)**:
    Reduction from **3-SAT**.
    1.  Given a 3-SAT formula with $n$ variables and $k$ clauses.
    2.  Construct large integers (in base 10 or sufficient base) where digits correspond to variables and clauses.
    3.  **Variable Digits**: For variable $x_i$, create numbers $v_i$ (true) and $v'_i$ (false). The $i$-th digit is 1, ensuring only one of $v_i, v'_i$ is chosen (target has 1 at this position).
    4.  **Clause Digits**: For clause $j$, the numbers corresponding to literals in that clause have a 1 at digit position $n+j$.
    5.  **Slack Variables**: Add separate slack numbers to allow clause sums to reach the target (e.g., target digit is 3 or 4 to ensure at least one true literal).
    6.  **Conclusion**: A subset sums to the target digit pattern iff a valid truth assignment satisfies all clauses.

## 3. Algorithms

### 3.1. Exponential Time (Meet-in-the-Middle)
Split $S$ into two halves $S_1, S_2$. Generate all sums for $S_1$ (list $L_1$) and $S_2$ (list $L_2$). For each $x \in L_1$, check if $T-x \in L_2$.
*   **Complexity**: $O(2^{n/2})$.

<details>
<summary><b>Numeric Example (Click to Expand)</b></summary>

**Input**: $S = \{45, 34, 4, 12, 5, 2\}$, $T = 42$.
**Steps**:
1.  **Split**: $S_1 = \{45, 34, 4\}$, $S_2 = \{12, 5, 2\}$.
2.  **Generate Sums**:
    *   $L_1 = \{0, 4, 34, 38, 45, 49, 79, 83\}$ (sorted)
    *   $L_2 = \{0, 2, 5, 7, 12, 14, 17, 19\}$ (sorted)
3.  **Search**: Iterate $x \in L_1$, binary search $T-x$ in $L_2$.
    *   $x=38 \implies \text{Need } 42-38=4$. Not in $L_2$.
    *   $x=34 \implies \text{Need } 42-34=8$. Not in $L_2$.
    *   **Wait**: Check original subsets. Actually, no subset sums to 42.
    *   Let's ensure the example works for $T=41$:
        *   $x=34 \in L_1$. Need $7 \in L_2$. Found ($5+2$).
        *   Result: True. Subset $\{34, 5, 2\}$.
</details>

### 3.2. Pseudo-Polynomial Time (Dynamic Programming)
Let $DP[i][s]$ be true if sum $s$ is achievable using first $i$ items.
*   **Recurrence**: $DP[i][s] = DP[i-1][s] \lor DP[i-1][s - a_i]$
*   **Complexity**: $O(N \cdot T)$.

<details>
<summary><b>Numeric Example (Click to Expand)</b></summary>

**Input**: $S = \{3, 4, 5\}$, $T = 7$.
**DP Table (Boolean array of size T+1)**:

| Item | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **Init** | T | F | F | F | F | F | F | F |
| **+3** | T | F | F | **T** | F | F | F | F |
| **+4** | T | F | F | T | **T** | F | F | **T** |
| **+5** | T | F | F | T | T | **T** | F | T |

**Result**: $DP[7]$ is **True** (formed by $3+4$).
</details>

## 4. Extensions

### 4.1. Handling Negative Numbers
When $S$ contains negative integers, the possible "sum" range shifts.
*   **Range**: $[MinSum, MaxSum]$ instead of $[0, T]$.
*   **DP Adjustment**: Shift array indices by adding offset $O = |MinSum|$.
    *   Index $j$ corresponds to actual sum $j - O$.
    *   Array size becomes $MaxSum - MinSum + 1$.

### 4.2. Applications: Numeric Systems
The Subset Sum problem models how numbers are represented in various systems.

*   **Binary Representation**: Standard Subset Sum where $S = \{2^0, 2^1, \dots, 2^k\}$. Every integer has a unique representation (sum).
*   **Balanced Ternary (Signed Subset Sum)**:
    *   Allow coefficients $x_i \in \{-1, 0, 1\}$.
    *   **Problem**: "Weighting Problem" (Bachet). What ensures every number can be weighed?
    *   **Solution**: $S = \{1, 3, 9, 27, \dots\}$ (Powers of 3).
    *   Example: $2 = 3 - 1$, $7 = 9 - 3 + 1$.

---

---

## 5. Related Problems

*   **[Knapsack Problem](00-knapsack_problem.md)**: The general case where items have distinct values and weights.
*   **[Multiple Subset Sum Problem](03-multiple_subset_sum_problem.md)**: Extension where items are packed into multiple containers.
*   **[Merkle-Hellman Cryptosystem](02-Merkle–Hellman_knapsack_cryptosystem.md)**: A cryptographic application relying on the hardness of Subset Sum.

---

## References
1.  **Wikipedia**: [Subset sum problem](https://en.wikipedia.org/wiki/Subset_sum_problem)
2.  **Dartmouth CS31**: [Lecture Notes (PDF)](https://www.cs.dartmouth.edu/~deepc/LecNotes/cs31/lec9+10.pdf)
