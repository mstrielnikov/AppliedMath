(_Exploring group of 4 elements_)[]

Suppose [[group]] $\langle G, \oplus \rangle$ is a group of order 4 ($char(G) = 4$).
Let $G = \{ 1, a, b, c \}$.

Let explore how group operations are behave. Explore options for $ba$:

1) $\cancel{ba = 1 \Rightarrow a=b^{-1}}$
2) $\cancel{ba = b \Rightarrow a = 1}$
3) $ba = c$
4) $\cancel{ba = a \Rightarrow b = 1}$

From another side we have for $ab$:

1) $\cancel{ab = 1 \Rightarrow a=b^{-1}}$
2) $\cancel{ab = b \Rightarrow a = 1}$
3) $ab = c$
4) $\cancel{ab = a \Rightarrow b = 1}$

Then for $a^{2}$:

1) $\cancel{a^2 = a \Rightarrow a=1}$
2) $a^2 = b$
3) $a^2 = c$
4) $\cancel{a^2 = 1 \Rightarrow a = 1}$

We know that $ab=c=ba$  so $c^2 = (ba)(ab) = ba^{2}b = b^2$. Which makes possible just two options:

1) $b^2 = c^2 = 1$
2) $b^2 = c^2 = a$

So, let's analyse further:

| $b^2 = c^2 = 1$<br> | $b^2 = c^2 = a$ |
| ---- | ---- |
| $\cancel{ac = a \Rightarrow c=1}$ | $\cancel{ac = a \Rightarrow c = 1}$ |
| $\cancel{ac = 1 \Rightarrow a = c}$ | $\cancel{ac = c \Rightarrow a = 1}$ |
| $ac = b = ca$ | $\cancel{ac = 1 \Rightarrow c = a}$ |
| $bc = a = cb$ | $ac = b$ |
|  | $ab = c$ |
|  | $ca = b$ |
|  | $ba = c$ |

Let's build a Cayley table for groups we got.
 
**A**) For $a^2 = b^2 = c^2 = 1$:

|     | $1$ | $a$ | $b$ | $c$ |
| --- | --- | --- | --- | --- |
| $1$ | $1$ | $a$ | $b$ | $c$ |
| a   | $a$ | $1$ | $c$ | $b$ |
| $b$ | $b$ | $c$ | $1$ | $a$ |
| $c$ | $c$ | $b$ | $a$ | $1$ |

We may put: 
$1 = (0,0)$
$a = (1,0)$
$b = (0,1)$
$c = (1,1)$

Then we got a Klein group: $\mathbb{Z}_{2} \times \mathbb{Z}_{2} = \{ (0,0), (0,1), (1,0), (1,1) \}$

Other isomorphisms of a Klein group:

|     | $\mathbb{Z}_{2} \times \mathbb{Z}_{2}$ | $\mathbb{Z}^{\times}_{8}$ | $\mathcal{P}(\{ \alpha, \beta\})$ | $\mathbb{SL_{2}(Z_2)}$                         |
| --- | -------------------------------------- | ------------------------- | --------------------------------- | ---------------------------------------------- |
| $1$ | $(0,0)$                                | $1 mod 8$                 | $\emptyset$                       | $\begin{pmatrix}1 & 0\\\ 0 & 1\end{pmatrix}$   |
| a   | $(0,1)$                                | $3 mod 8$                 | $\{\alpha\}$                      | $\begin{pmatrix}1 & 0\\\ 0 & -1\end{pmatrix}$  |
| $b$ | $(1,0)$                                | $5 mod 8$                 | $\{\beta\}$                       | $\begin{pmatrix}-1 & 0\\\ 0 & 1\end{pmatrix}$  |
| $c$ | $(1,1)$                                | $7 mod8$                  | $\{\alpha, \beta\}$               | $\begin{pmatrix}-1 & 0\\\ 0 & -1\end{pmatrix}$ |

**B**) For $a^2=1, b^2 = c^2 = a$:

|  | $1$ | $a$ | $b$ | $c$ |
| ---- | ---- | ---- | ---- | ---- |
| $1$ | $1$ | $a$ | $b$ | $c$ |
| a | $a$ | $1$ | $c$ | $b$ |
| $b$ | $b$ | $c$ | $a$ | $1$ |
| $c$ | $c$ | $b$ | $1$ | $a$ |

We may put: 
$1 \leftrightarrow 0$
$a \leftrightarrow 1$
$b \leftrightarrow 3$
$c \leftrightarrow 2$

Then got: $\mathbb{Z}_{4} \{ 0, 1, 2, 3 \}$
