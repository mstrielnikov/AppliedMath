# Knapsack Problem

## 1. Classical Definition (0/1 Knapsack)

Given a set of $n$ items, each with a weight $w_i$ and a value $v_i$, and a maximum capacity $W$, the goal is to determine which items to include in a collection so that the total weight is less than or equal to $W$ and the total value is maximized.

### Matrix Formulation (Integer Linear Programming)

Let $\mathbf{x} \in \{0, 1\}^n$ be a vector of binary variables where $x_i=1$ if the $i$-th item is selected, and $0$ otherwise.
Let $\mathbf{v} \in \mathbb{R}^n$ be the vector of values and $\mathbf{w} \in \mathbb{R}^n$ be the vector of weights.

The problem can be stated as a system of linear equations (maximization):

$$
\begin{aligned}
\text{maximize} \quad & \mathbf{v}^\top \mathbf{x} \\
\text{subject to} \quad & \mathbf{w}^\top \mathbf{x} \le W \\
& \mathbf{x} \in \{0, 1\}^n
\end{aligned}
$$

## 2. Complexity Class

*   **Optimization Problem**: The Knapsack problem is **NP-hard**. There is no known polynomial-time algorithm that can solve it for all cases (unless P=NP).
*   **Decision Problem**: The problem "Can a value of at least $V$ be achieved without exceeding weight $W$?" is **NP-complete**.
*   **Pseudo-Polynomial**: It can be solved in pseudo-polynomial time $O(nW)$ using dynamic programming. This is not polynomial in the input size because the input size is proportional to $\log W$, not $W$ itself.

## 3. Proof of NP-Hardness (Outline)

We show NP-hardness by reduction from the **Subset Sum Problem**, which is known to be NP-complete.

For a detailed proof and formulation of the Subset Sum problem, see the [Subset Sum Conspect](subset_sum.md).

**Reduction Logic**:
Since the Subset Sum problem is a special case of the Knapsack problem where $v_i = w_i$ and $W = K$, any algorithm that solves the general Knapsack problem can also solve the Subset Sum problem. Therefore, Knapsack must be at least as hard as Subset Sum (NP-hard).

## 4. Solution Approaches

### 4.1. Dynamic Programming (Pseudo-Polynomial)

**Standard Recurrence (Weight-based)**
Let $dp[i][w]$ be the maximum value that can be attained with weight less than or equal to $w$ using items up to $i$.
*   **Recurrence**: $dp[i][w] = \max(dp[i-1][w], \quad dp[i-1][w - w_i] + v_i)$ (if $w_i \le w$).
*   **Complexity**: $O(nW)$ time and space. pseudo-polynomial.

### 4.2. Meet-in-the-Middle (Exponential Time)

Useful when $n$ is small (e.g., $n \le 40$) but $W$ is extremely large.

**Algorithm Steps**:
1.  **Divide**: Partition items into two sets $S_1, S_2$ of size $n/2$.
2.  **Generate**: Compute all subset sums/values for both sets. Let $L_1$ and $L_2$ be lists of pairs $(w, v)$.
3.  **Sort & Prune**: Sort $L_2$ by weight. Remove **dominated** states (remove pair $(w, v)$ if $\exists (w', v')$ such that $w' \le w$ and $v' \ge v$). This ensures strictly increasing value for increasing weight.
4.  **Search**: For each $(w_1, v_1) \in L_1$:
    *   Find $(w_2, v_2) \in L_2$ maximizing $v_2$ such that $w_2 \le W - w_1$ using binary search (or two pointers).
    *   Update global max value with $v_1 + v_2$.

**Complexity**: $O(2^{n/2})$. Specifically, sorting takes $O(n \cdot 2^{n/2})$.

### 4.3. Branch and Bound (Exact)

An exact search algorithm that explores a state-space tree (include/exclude item) but prunes branches that cannot exceed the current best solution.

*   **Upper Bound**: At any node, calculate the **relaxation** (Fractional Knapsack) for the remaining items.
*   **Pruning Condition**: If $(\text{current value} + \text{upper bound}) \le \text{best known solution}$, prune this branch.
*   **Strategy**: Often sorts items by $v_i/w_i$ and uses Depth-First Search for memory efficiency.

### 4.4. Greedy Approximation (Heuristic)

A fast, non-optimal approach for large inputs.

1.  Calculate density $r_i = v_i / w_i$ for all items.
2.  Sort items such that $r_1 \ge r_2 \ge \dots \ge r_n$.
3.  Add items in order as long as they fit in the knapsack.
4.  **Approximation Guarantee**: To ensure a bound, compare the greedy result with the single most valuable item that fits. The max of these two is a **1/2-approximation** ($V_{approx} \ge 0.5 \cdot V_{opt}$).

---

## 5. Generalizations via Formalization

### 5.1. Multidimensional Knapsack Problem ($d$-KP)
The items have multiple resource constraints (e.g., weight, volume, budget).
*   **Formalization**:
    $$ \text{Maximize } \mathbf{v}^\top \mathbf{x} $$
    $$ \text{Subject to } \mathbf{A}\mathbf{x} \le \mathbf{b}, \quad \mathbf{x} \in \{0, 1\}^n $$
    Where $\mathbf{A}$ is a $d \times n$ matrix (column $j$ represents resources consumed by item $j$) and $\mathbf{b}$ is the vector of capacities for $d$ dimensions.

### 5.2. Parametric Knapsack Problem (PKP)
The parameters (profits or weights) depend on a scalar parameter $\lambda$.
*   **Affine Profit Case**:
    $$ \text{Maximize } Z(\lambda) = \sum_{i=1}^n (a_i + \lambda b_i) x_i $$
    $$ \text{Subject to } \sum w_i x_i \le W $$
*   **Goal**: Analyze the optimal value function $Z(\lambda)$ or finding ranges of $\lambda$ where solution topology remains constant. This is distinct from the *Linear Fractional Knapsack* problem.

### 5.3. Inverse Parametric Knapsack
Given a desired solution $\mathbf{x}^*$, finding the minimal modification to the problem parameters (e.g., changing $\lambda$ or minimal vector norm perturbation) such that $\mathbf{x}^*$ becomes optimal.

---

## 6. Classification of Variations

The "Knapsack" family is broad. We can classify related problems by their structural changes.

### 6.1. By Weight/Cardinality Constraint
*   **[Subset Sum Problem](01-subset_sum_problem.md)**: Special case where $v_i = w_i$.
*   **Change Making Problem**: Minimize number of items to reach exact sum $W$ (Unbounded Knapsack with $v_i=1$).
*   **Multidimensional Knapsack**: Vector constraints $\mathbf{A}\mathbf{x} \le \mathbf{b}$.

### 6.2. By Objective Structure
*   **[Quadratic Knapsack Problem](04-quadratic_knapsack_problem.md)**: Objective includes interaction terms $P_{ij} x_i x_j$.
*   **Parametric Knapsack**: Objective is a function $f(x, \lambda)$.

### 6.3. By Bin/Container Structure
*   **[Multiple Subset Sum Problem](03-multiple_subset_sum_problem.md)**: Items packed into $m$ bins with different capacities.
*   **Bin Packing Problem**: Fixed items, minimize number of bins $m$.
*   **Multiple Knapsack Problem**: General case with $m$ bins and distinct item profits.

### 6.4. Applications
*   **[Resource Allocation (Cloud/Kubernetes)](05-resource_allocation_problems.md)**: Transition from Hard Constraints (Node Capacity) to Soft Constraints (Price).
*   **[Merkle-Hellman Cryptosystem](02-Merkle–Hellman_knapsack_cryptosystem.md)**: Utilizing the hardness of Subset Sum.

---

## 7. References

1.  **MIT 6.006 Recitation 21**: [PDF](https://courses.csail.mit.edu/6.006/fall11/rec/rec21_knapsack.pdf)
2.  **MIT 18.434 Seminar**: [PDF](https://math.mit.edu/~goemans/18434S06/knapsack-katherine.pdf)
3.  **Wikipedia**: [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)
