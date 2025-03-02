# Direct sum of linear spaces
Given two vector (or linear) spaces $V_{1}$ and $V_{2}$ such that $V_{1} \cap V_{2} = 0$. Then direct sum of $V_{1}$ and $V_{2}$ is vector space $V$: $V_{1} \oplus V_2 = V$. 

It's easy to see that any sum of kind $V = \sum_{i \leq n }^{n} V_{i}$ such that for each $V_{i}$ holds $\cap_{i \leq n}^{n} V_{i} = 0$ then this sum is partitioning (or decomposition) of $V$: $\oplus_{i \leq n}^{n} V_{i}$.

**Consequence**. $V_{i} \cap (V_{1} \oplus V_{2} \oplus V_{j<i} \oplus V_{j > i}) = 0$

**Lemma.** Each vector space $V$ have single direct sum representation: $\exists! V_{1}, V_{2}: V_{1} \oplus V_{2} = V$.
Suppose $V$ has more the one unique representation by $V'_{1}, V'_{2}$ then:
$$V'_{1} \neq V_{1}, V'_{2} \neq V_{2} \Longrightarrow V = V'_{1} + V'_{2} = V_{1} + V_{2} \Longrightarrow V_{1} - V'_{1} = V_{2} - V'_{2} = 0 \Longrightarrow V_{1} = V'_{1}, V_{2}=V'_{2}$$
Let $n = dim(V)$ and $V = \cup_{i \leq n}^{n} \{ V_{i} \}$ where each $V_{i}$ could represented as vector [[basis]]: $V_{i} = \{ \alpha_{i}V, \alpha_{i} \in \mathbb{R} \}$. Then $V = \sum_{i \leq n}^{n} \alpha_{i}V$ and $V_{i} \cap V_{j \neq i} = 0$, so $V = \oplus_{i \leq n}^{n} \alpha_{i}V$.
As an example, we can pick arbitrary basis in $V^2 \in \mathbb{R}^{2}$ and another basis $V \in \mathbb{R}, V \cap V^{2} = 0 \Rightarrow V \oplus V^{2} = V^{3}, V^{3} \in \mathbb{R}^3$.

Let vector spaces $V \supseteq U$ and $V = U \oplus W$, $dim(V) = n$, $dim(U) = k$ with $W$ is unknown.
Then basis $B_{U}$ of vector space $U$: $B_{U} = \{ U_{1}, U_{2}, ..., U_{k} \}$. $n \geq k$ because $U$ is subset of $V$. We could pick complement vectors to $B_{U}$ from $V$ to get basis of $V$ in way: $$B_{V} = B_{U} \cup B_{W} = \{ U_{1}, U_{2}, ..., U_{k} \} \cup \{ W_{1}, W_{2}, ..., W_{m} \} = \{ U_{1}, U_{2}, ..., U_{k}, W_{1}, W_{2}, ..., W_{m} \}$$
Keep in mind that $U = span(\{ U_{1}, U_{2}, ..., U_{k} \})$ and $W = span(\{ W_{1}, W_{2}, ..., W_{k} \})$ then $U \cap W = 0$. 
Then we have $V = U + W$ and $dim(V) = dim(U) + dim(W)$. So, $W$ is complement to $U$ but $W$ is not necessary unique. But if some basis from $V$ chosen and fixed, then basis representation of $U$ is unique.

# Descartes product of linear spaces
Given vector spaces $V_{1}$, $V_{2}$, $W$ such that $V_{1} \times V_{2} = W$. Then $W$ is a set of basis pairs $v_{1}$ and $v_{2}$ from corresponded vector spaces $V_{1}$ and $V_{2}$: $W = \{ (v_{1}, v_{2}) \mid v_{1} \in V_{1}, v_{2} \in V_{2}  \}$. 
1. Addition will looks like: $(v_{1}, v_{2}) + (u_{1}, u_{2}) = (u_{1} + v_{1}, u_{2} + v_{2}) = (w_{1}, w_{2}) \in W$.
2. Multiply to scalar $\alpha$: $\alpha(u_{1}, u_{2}) = (\alpha u_{1}, \alpha u_{2})$
3. Identity element $I$: $I = (0,0)$

If we put $V'_{1} = \{ (V_{1}, 0) \}$ and $V'_{2} = \{ (0, V_{2}) \}$ then $V'_{1} \oplus V'_{2} = W$. Note that $V'_{1} \subset W$ $V'_{2} \subset W$ and $V'_{1} \cap V'_{2} = (0, 0)$ correspondingly $V'_{1} \cup V'_{2} = W$.
