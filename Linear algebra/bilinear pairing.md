# Definition
Pairing is a bilinear map from the Cartesian product of two modules which results into third module.
## As bilinear map
Let $M, N, L$ are modules over field $\mathbb{F}$ than pairing $e: M \times N \to L$ satisfies:
1. $\forall m \in M, n \in N, r \in \mathbb{F}: e(r+m,n) = e(m,r+n) = r*e(m,n)$
2. $\forall m \in M, n \in N, r \in \mathbb{F}: e(r*m,n) = e(m,r*n) = e(m,n)^{r}$
3. $\forall m_{1,2} \in M, n_{1,2} \in N, r \in R: e(m_1 + m_2,n) = e(m_1,n) * e(m_2,n)$ and $e(m,n_1 + n_2) = e(m,n_1) * e(m,n_2)$
## As linear map
Let $M, N, L$ are modules over field $R$ than pairing may be represented as tensor product: $M \otimes_R N \to L$
## As morphism
A pairing of modules $M, N, L$ over field $R$ could be considered as the following map:
$\Phi: M \to Hom_{R}(N,L) \Longleftrightarrow \forall m \in M, n \in N: \Phi(m)(n) = e(m,n)$. We can see that right part of equivalence matches the first definition (as a bilinear map).
# Properties
1. A pairing $e(M, N)$ is called **perfect** if the corresponding map is an isomorphism of modules $M$ and $N$.
2. $\forall m \in M, n \in N: e(-m,n) = e(m,-n) = e(m,n)^{-1}$
3. A pairing is called **non-degenerate on the right** when the following condition implies for any $m$: $\forall n \in N: e(m,n)=0 \to n = 0$, similarly $e$ is called **non-degenerate on the left** if for any fixed $n$ holds $\forall m \in M: e(m,n)=0 \to m = 0$
4. Pairing is non-degenerative if: $e(M, N) \neq 0$ 
5. if $M = N$ the pairing $e(M,N)$ is called symmetric pairing.
6. A pairing is called **alternating** if $𝑁=𝑀$ and $\forall m \in M: e(m,n)=0$. In particular, this implies $e(m+n,m+n)=0$, while bilinearity shows $e(m+n,m+n)=e(m,m)*e(m,n)*e(n,m)*e(n,n)=e(m,n)*e(n,m)$. Thus, for an alternating pairing, $e(m,n)=-e(n,m)$
## Lemma. 1
Put $G_1$ and $G_2$ as modules, $G_1 = G_2$ and both $G_1$ and $G_2$ are cyclic groups, then pairing $e(G_1, G_2)$ is commutative: $e(G_1, G_2) = e(G_2, G_1)$.
Let $G_1$ and $G_2$ cyclic groups of prime order $p$. Then groups has generators $g_1$ and $g_2$ respectively: $\langle g_1\rangle = \{ G_1 \}$ and $\langle g_2\rangle = \{ G_2 \}$. In other words $G_1 = \{ mg_{1} \mid \forall m \in [ 1; \#G_1 ) \}$  and $G_2 = \{ ng_{2} \mid \forall n \in [ 1; \#G_2 ) \}$. So by using bilinearity property: $e(G_1, G_2) = e(mg_{1}, ng_{2}) = e(g_{1}, g_{2})^{mn} = e(ng_{1}, mg_{2}) = e(G_2, G_1)$
## Lemma. 2
Show that $e(u,v) = 1$ then  $u=1$ or $v=1$.
Put $u \in G_{1}$ and $v \in G_{2}$ are prime order groups with the same prime characteristics $p$.
Then $u = gx$ and $v = hy$ where $x, y \in \mathbb{Z}_p$. Then $e(u,v) = e(gx, hy) = (g, h)^{xy} = 1 \Longleftrightarrow 1 = e(g,h)^{0}$. Since
$$e(g,h) \neq 1 \Longrightarrow xy = 0 \Longrightarrow \left[ 
    \begin{array}{l}
        x = 0 &\\
        y = 0 
    \end{array} 
\right.
$$
## Consequences. 1
1. $e(ga, h) e(gb, h) = e(g, h)^{a} * e(g, h)^{b} = e(g, h)^{a+b}$
2. $e(g, ha) e(gb, h) = e(g, h)^{a} * e(g, h)^{b} = e(g, h)^{a+b}$
3. $e(ga, -hb) * e(u, v) * e(g, h)^{c} = e(g, h)^{-ab} * e(g, h)^{c} * e(u,v) = e(g, h)^{c-ab} e(u,v)$
4. $\prod_{i=1}^{n} e(g,h^{a_{i}})^{b_{i}} = \prod_{i=1}^{n} e(g,h)^{a_{i}b_{i}} = e(g,h)^{\sum_{i=1}^{n} {a_{i}b_{i}}}$
## Consequences. 2 (lemma 1 + Consequences 1)
Put $G_{1}$ and $G_{2}$ are prime order groups with the same prime characteristics $p$. Then $G_1 = \langle g_1 \rangle \Rightarrow \forall u \in G_1: u = gx$ where $x \in \mathbb{Z}_{p}$. Similarly $\forall v,w \in G_{2}: v=hy, w=hz$ where $y,z \in \mathbb{Z}_{p}$.
So following expressions could be reduced:
1. $e(u,v)*e(u,w) = e(gx, hy)*e(gx, hz) = e(g, h)^{x+y} * e(g, h)^{x+z} = e(g, h)^{x(y+z)} = e(u, vw)$
2. $\prod_{i=1}^{n} e(u^{a}, v_{i}^{b})^{\frac{c_{i}}{ab}} = \prod_{i=1}^{n} e(u, v_{i})^{ab\frac{c_{i}}{ab}} = \prod_{i=1}^{n} e(u, v_{i})^{c_{i}} = e(u,\prod_{i=1}^{n} v_{i}^{c_{i}} )$
# Examples
## Scalar product
Any scalar product on vector space of reals $R^n, n \in \mathbb{N}$
## Determinant map
The determinant map of $n \times n$ matrices $M^{n \times n}$: $e(M_{1}^{n \times n}, M_{2}^{n \times n}) : det(M_{1}^{n \times n}) \times det(M_{2}^{n \times n}) = det_{n \times n}(M_{1} \times M_{2})$
## Matrix product
## Parings of prime order groups
## Pairings on elliptical curves
1. Weil pairing
2. Tate (Tate-Lichtenbaum) pairing
3. Eta paring
4. Ate paring
## Hopf pairing
# Further reading
1. [Wikipedia: Pairings](https://en.wikipedia.org/wiki/Pairing)
# Links
[[bilinear map]]
[[module]]
[[homomorphism]]
[[isomorphism]]
[[scalar product]]
[[tensor product]]
[[bilinear form]]
[[Weil pairing]]
[[Tate pairing]]