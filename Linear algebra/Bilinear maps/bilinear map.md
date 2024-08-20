# Definition
Bilinear map is a function combining elements of two vector spaces to yield an element of a third vector space and is linear in each of arguments.

Let $V$, $W$, $X$ are vector spaces over the same field $F$. A bilinear map $B$ is a function:
$B: V \times W \to X$, such that $\forall w \in W: v \mapsto B(v, w)$ is linear and $\forall v \in V: w \mapsto B(v, w)$ is a linear map also.

Bilinear map $B$ should satisfy the following conditions:
1. $\forall \lambda F, B(\lambda v, w) = B(v, \lambda w) = \lambda B(v, w)$
2. The map $B$ is additive in both components: if $v_1, v_2 \in V$ and $w_1, w_2 \in W$ then $B(v_1 + v_2, w) = B(v_1, w) + B(v_2, w)$ also $B(v, w_1 + w_2) = B(v, w_1) + B(v, w_2)$

If $V = W$ and $\forall v,w \in V: B(V,W) = B(W,V)$ satisfied, $B$ is symmetric.
# Properties
# Examples
## Matrix multiplication
Matrix multiplication is bilinear map: $M(m, n) \times M(n, p) \to M(m, p)$.
## Cross product in 3d-dimension real space
Cross product in $R^3$ is a bilinear map $R^3 \times R^3 \to R^3$
## Vector space with dual space
## Bilinear form
# LInks
[[map]]
[[vector space]]
[[field]]
[[matrix multiplication]]
[[cross product]]
[[bilinear form]]
[[bilinear pairing]]