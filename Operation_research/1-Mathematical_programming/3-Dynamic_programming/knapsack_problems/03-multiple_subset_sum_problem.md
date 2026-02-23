# Multiple Subset Sum Problem (MSSP)

## 1. Formal Definition

Given a set of items $I = \{1, \dots, n\}$ with weights $w_1, \dots, w_n$ and $m$ bins (knapsacks) with capacities $c_1, \dots, c_m$, the **Multiple Subset Sum Problem** seeks to pack the maximum total weight of items into the bins without exceeding any bin's capacity.

*   **Objective**: Maximize $\sum_{j=1}^m \sum_{i \in S_j} w_i$
*   **Constraint**: $\sum_{i \in S_j} w_i \le c_j$ for all bins $j \in \{1, \dots, m\}$.
*   **Disjointness**: $S_j \cap S_k = \emptyset$ for $j \neq k$.

### Analogy
Instead of filling a single knapsack (single Subset Sum), you are packing **multiple suitcases** for a trip. Each suitcase has a different weight limit. You want to take as much stuff as possible, deciding which item goes into which suitcase.

## 2. Complexity Class

 The MSSP is **Strongly NP-hard**.
*   **Implication**: unlike the single Subset Sum problem, there is no pseudo-polynomial time algorithm (unless P=NP). The complexity depends on the *values* of the inputs in a way that cannot be smoothed out by dynamic programming on the sum.
*   **Reduction**: It generalizes the **3-Partition Problem** (splitting a set into triplets of equal sum), which is strongly NP-complete.
*   **Approximability**: Despite being strongly NP-hard, a **Polynomial Time Approximation Scheme (PTAS)** exists. This means for any error $\epsilon > 0$, we can find a solution within $(1-\epsilon)$ of potential optimal in time polynomial in $n$ (though exponential in $1/\epsilon$). This works because we can enumerate "large" items exactly and fill the remaining space with "small" items greedily.

## 3. Solution Approaches

### 3.1. Greedy Heuristics
Fast, intuitive methods that sort items and assign them one by one.

#### First Fit Decreasing (FFD)
1.  Sort items in descending order of weight.
2.  Place each item into the **first** bin where it fits.
3.  If it fits nowhere, discard it.

<details>
<summary><b>Numeric Example: First Fit (Click to Expand)</b></summary>

**Bin Capacities**: $B_1=10, B_2=10$.
**Items**: $\{8, 7, 5, 2\}$.
1.  **Item 8**: Fits in $B_1$. $B_1$ rem: 2.
2.  **Item 7**: Fits in $B_2$. $B_2$ rem: 3.
3.  **Item 5**: Cannot fit in $B_1$ (2) or $B_2$ (3). Discard.
4.  **Item 2**: Fits in $B_1$ (matches rem 2). $B_1$ rem: 0.

**Total Packed**: $8+7+2 = 17$. (**Optimal**: $\{8, 2\}$ in $B_1$, $\{7\}$ in $B_2$ is not better... wait, $\{5, ... \}$? Actually $\{5, 2\}$ in $B_1$ and $\{8\}$ in $B_2$ implies total 15. The FFD result 17 is optimal here.)
</details>

#### Best Fit Decreasing (BFD)
1.  Sort items in descending order.
2.  Place each item into the bin with the **smallest remaining capacity** that is sufficient (tightest fit).

<details>
<summary><b>Numeric Example: Best Fit (Click to Expand)</b></summary>

**Bin Capacities**: $B_1=9, B_2=9$.
**Items**: $\{5, 4, 3, 3, 3\}$.
1.  **Item 5**: $B_1, B_2$ empty. Put in $B_1$. Rem: $B_1=4, B_2=9$.
2.  **Item 4**: Fits exactly in $B_1$ (best fit). Rem: $B_1=0, B_2=9$.
3.  **Item 3**: Only fits in $B_2$. Rem: $B_1=0, B_2=6$.
4.  **Item 3**: Only fits in $B_2$. Rem: $B_1=0, B_2=3$.
5.  **item 3**: Fits exactly in $B_2$. Rem: $B_1=0, B_2=0$.

**Total Packed**: 18 (Perfect fill).
</details>

### 3.2. Exact Approaches
*   **Meet-in-the-Middle**: For small $m$, can be effective but scales as $O((m+1)^{n/2})$.
*   **Branch and Bound**: Standard for exploring the assignment tree, using linear programming relaxation (Fractional Multi-Knapsack) to bound the profit.

## 4. Connections

*   **[Subset Sum Problem](01-subset_sum_problem.md)**: The basic single-bin version of this problem.
*   **[Knapsack Problem](00-knapsack_problem.md)**: The variation where items have profits different from their weights.
*   **Bin Packing**: The "inverse" problem. In Bin Packing, you fix the items and minimize the bins ($m$). In MSSP, you fix the bins ($m$) and maximize the items.

