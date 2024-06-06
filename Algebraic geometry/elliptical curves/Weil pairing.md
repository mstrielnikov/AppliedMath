# Definition
Let $E$ elliptical curve over Galois field $GF(p^{m})$.
Let $E[r]$ is subgroup $E/GF(p^{n})$ when $n=1$.
The Weil pairing is a map $w_{r}: E[r] \times E[r]\to (GF(p^{m}))^{*}$.
Wail pairing $w$ for $P$ and $Q$  could be calculated $w_{r}(Q,P) = (-1)^{r}\frac{f(Div(Q))}{g(Div(P))}$, where:
1. $supp(Div(Q)) \cap supp(Div(P)) = \emptyset$
2. $Div(P) \sim (P) - O$  and $Div(Q) \sim (Q) - O$ 
3. $Div(f) = rDiv(P)$ and $Div(g) = rDiv(Q)$
# Theorem
Wail pairing $w_{r}$ is a bilinear pairing.
# Miller's theorem
For elliptical curve points $P$ and $Q$ which linearly dependent $P=rQ$, Wail pairing $w_{r}(P,Q)=(-1)^{r}\frac{f_{r,P}(Q)}{f_{r,Q}(P)}$, where $f_{r,P}$ and $f_{r,Q}$ are Weil functions. Each of $f_{r,P}$ and $f_{r,Q}$ could be calculated with Miller's algorithm.
# Miller's algorithm
Additional notation which will be used during the algorithm.
$l_{T,T}$ - real equation of tangent line to E in point $P$.
${V_{[2T]}}$

Input: $n \in \mathbb N$, $P \in E$, 
Output: $f_{n,P}(Div(P))$
1. Find representation of $n$ in binary system $n_{bin} = \sum_{i=1}^{l} n_{i}*2^{i}$, where $l=\lceil log_{2}n \rceil$
2. Initialisation: $T = P, f = 1$
3. for($i = l - 1$; $i \geq 0$; $i-1$) \{
4. $f := f^{2}*\frac{l_{T,T}(Div(P))}{V_{[2T(Div(P))]}}$
5. $T := [2T]$
6. if ($n_i == 1$) \{
7.      $f:=f*\frac{l_{T,T}(Div(P))}{V_{[2T(Div(P))]}}$
8.      $T := T + P \}$
9. 

$f_{r,Q}(P)$

# Further reading
1. [Wikipedia: Weil pairing](https://en.wikipedia.org/wiki/Weil_pairing)
# Links
[[Weil function]]
[[bilinear pairing]]
[[Weil divisor of elliptical curve]]
[[Tate pairing]]