Let $V_{1}, V_{2} \subset \mathbb{R}$ are linear subspaces of $\mathbb{R}$ and $v_{1} \in V_{1}$, $v_{2} \in V_{2}$.
# Intersection of vector spaces
Let $W$ is another vector spaces given by $W = V_{1} \cap V_{2}$ then $u,w \in W: v = u + w \in W$. Obviously $W \in \mathbb{R}$.
# Addition of vector spaces
Addition for two vector spaces $V_{1}, V_{2}$ could be defined as sums for all possible linear combinations $v_{1}, v_{2}$ from both vector spaces:  $V_{1} + V_{2} = \{ v_{1}+v_{2} \mid v_{1} \in V_1, v_{2} \in V_{2} \} \Longleftrightarrow V_{1} + V_{2} = span(\{V_{1},V_{2}\})$ 
# Union of vector spaces
Suppose we have vector spaces $V_{1}, V_{2} \supset \mathbb{R}^{3}$ such that $dim(V_{1})=dim(V_{2})=2$. Then $v_{1} \in V_{1}$ and $v_{2} \in V_{2}$  are 2-d vectors.
**Lemma**. Sum of vectors in different vector spaces are no belongs to union of these vector spaces: $v_{1} \in V_{1}, v_{2} \in V_{2}: \overline{v} = v_{1} + v_{2} \notin V_{1} \cup V_{2}$. Suppose $V = V_{1} \cap V_{2} \neq 0 \Rightarrow V \in \mathbb{R}$. Then arbitrary chosen $v \in V$ is a dot with $dim(v)=1$. Then we can construct vectors $\overline{vv_{1}} \in V_{1}$ and $\overline{vv_{2}} \in V_{2}$ with common source $v \in V$. By parallelogram law for vector addition, $\overrightarrow{vv} = \overrightarrow{vv_{1}} + \overrightarrow{vv_{2}}$ will be out of $V_{1}$ or $V_{2}$ but will be situated in subspace $\overline{V_{1} \cap V_{2}} \subset \mathbb{R}^3$. The same result is also obvious from definition of addition for vector spaces.
# Connection between dimensions of subspaces
Let $U$ is linear space and $V,W \subset U$ then sum of dimensions for $V,W$: $$dim(V) + dim(W) = dim(V+W) + dim(V \cap W)$$**Lemma.** Sum of subspaces' dimensions. 
Let $\{ u_{1}, u_{2}, ..., u_{k} \}$ is basis for $V \cap W$ and $k=dim(V \cap W)$. Then basis for $V$ is $\{ v_{1}, v_{2}, ..., v_{l}, u_{1}, u_{2}, ..., u_{k} \}$, where $\{ v_{1}, v_{2}, ..., v_{l} \} \notin V \cap W$ are remaining $l$ complement basis vectors from $V$ and linearly independent with basis vectors of intersection $V \cap W$ such that $dim(V) = k + l$.
We can construct basis for subspace $W$ by completion for basis of intersection $V \cap W$ with $m$ linearly independent vectors $w \in W$ which not belongs to the intersection $\{ w_{1}, w_{2}, ..., w_{m} \} \notin V \cap W$. So, basis for $W$ is $\{ w_{1}, w_{2}, ..., w_{m}, u_{1}, u_{2}, ..., u_{k} \}$. Then $dim(W)=k + m$.
Construct basis for $V+W$.  Basis vectors $w \in W$ and $v \in V$ should be selected to hold the foloving condition $span(v_{1}, v_{2}, ..., v_{l}) \cap span(w_{1}, w_{2}, ..., w_{m}) \neq 0$. So, basis for $V+W$ will be $\{ w_{1}, w_{2}, ..., w_{m}, v_{1}, u_{1}, u_{2}, ..., u_{k}, v_{2}, ..., v_{l} \}$. Then we have $dim(V+W)= m + l + k$.
At the end we got: $dim(V) + dim(W) = k + l + m + k$
# Example 1. Find dimension of intersection of given subspaces and basis of subspaces' sum
Given $V, W \subset \mathbb{R}^{4}$. 
$$V = span\{
\begin{pmatrix}  
1 \\  
2 \\
1 \\
-2 
\end{pmatrix},

\begin{pmatrix}  
2 \\  
3 \\
1 \\
0 
\end{pmatrix},

\begin{pmatrix}  
1 \\  
2 \\
2 \\
-3 
\end{pmatrix}
\},

W = span\{
\begin{pmatrix}  
1 \\  
1 \\
1 \\
1 
\end{pmatrix},

\begin{pmatrix}  
1 \\  
0 \\
1 \\
-1 
\end{pmatrix},

\begin{pmatrix}  
1 \\  
3 \\
0 \\
4 
\end{pmatrix}
\},
$$
$$
V \sim 
\begin{pmatrix}  
1 & 2 & 1 & -2\\  
2 & 3 & 1 & 0 \\
1 & 2 & 2 & -3 \\
\end{pmatrix}
\sim
\begin{pmatrix}  
1 & 2 & 1 & -2\\  
0 & -1 & -1 & 4 \\
0 & 0 & 1 & -1 \\
\end{pmatrix}
\Rightarrow dim(V)=3
$$
$$
W \sim 
\begin{pmatrix}  
1 & 1 & 1 & 1 \\  
1 & 0 & 1 & -1 \\
1 & 3 & 0 & -4 \\
\end{pmatrix}
\sim
\begin{pmatrix}  
1 & 2 & 1 & -2\\  
0 & -1 & 0 & -2 \\
0 & 2 & -1 & 3 \\
\end{pmatrix}
\sim
\begin{pmatrix}  
1 & 2 & 1 & -2\\  
0 & -1 & 0 & -2 \\
0 & 0 & -1 & -1 \\
\end{pmatrix}
\Rightarrow dim(W) = 3
$$
$$
W + V \sim 
\begin{pmatrix}  
1 & 2 & 1 & -2 \\  
2 & 3 & 1 & 0 \\
1 & 2 & 2 & -3 \\
1 & 1 & 1 & 1 \\  
1 & 0 & 1 & -1 \\
1 & 3 & 0 & -4 \\
\end{pmatrix}
\sim
\begin{pmatrix}  
1 & 2 & 1 & -2\\  
0 & -1 & -1 & 4 \\
0 & 0 & 1 & -1 \\
1 & 2 & 1 & -2\\  
0 & -1 & 0 & -2 \\
0 & 0 & -1 & -1 \\
\end{pmatrix}
\sim
\begin{pmatrix}  
1 & 2 & 1 & -2\\  
0 & -1 & -1 & 4 \\
0 & 0 & 1 & -1 \\
0 & 0 & 0 & 0 \\  
0 & -1 & 0 & -2 \\
0 & 0 & 0 & -2 \\
\end{pmatrix}
\sim
\begin{pmatrix}  
1 & 0 & 0 & 0 \\  
0 & -1 & -1 & 4 \\
0 & 0 & 1 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & 0 & -2 \\
\end{pmatrix}
\sim
\begin{pmatrix}  
1 & 0 & 0 & 0 \\  
0 & 0 & -1 & 0 \\
0 & 0 & 1 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & 0 & -2 \\
\end{pmatrix}
\sim
\begin{pmatrix}  
1 & 0 & 0 & 0 \\  
0 & -1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & -2 \\
\end{pmatrix}
\Rightarrow dim(V+W) = 4
$$
$$dim(V \cap W) = dim(V) + dim(W) - dim(V + W) = 3 + 3 - 4$$
So, basis for $V+W$:
$$B_{V+W} = \{
\begin{pmatrix}  
1 \\  
2 \\
1 \\
-2  
\end{pmatrix},
\begin{pmatrix}  
0 \\  
-1 \\
-1 \\
4 
\end{pmatrix},
\begin{pmatrix}  
0 \\  
0 \\
1 \\
-1 
\end{pmatrix}
\}$$
# Example 2. Basis for intersection of subspaces
Given $V, W \subset \mathbb{R}^{3}$. 
$$V = span\{
\begin{pmatrix}  
1 \\  
2 \\
1  
\end{pmatrix},

\begin{pmatrix}  
1 \\  
1 \\
-1
\end{pmatrix},

\begin{pmatrix}  
1 \\  
3 \\
3 \\
\end{pmatrix}
\},

W = span\{
\begin{pmatrix}  
2 \\  
3 \\
-1 \\ 
\end{pmatrix},

\begin{pmatrix}  
1 \\ 
2 \\
2 \\
\end{pmatrix},

\begin{pmatrix}  
1 \\  
1 \\
-3 \\
\end{pmatrix}
\}
$$
$$V \sim \begin{pmatrix}
1 & 2 & 1\\  
1 & 1 & -1 \\
1 & 3 & 3\\
\end{pmatrix}
\sim \begin{pmatrix}
0 & 1 & 2 \\  
1 & 1 & -1 \\
0 & 2 & 4 \\
\end{pmatrix}
\sim \begin{pmatrix}
0 & 1 & 2 \\  
1 & 1 & -1 \\
0 & 0 & 0 \\
\end{pmatrix} 
\Rightarrow \dim(V) = 2
$$
$$W \sim \begin{pmatrix}
2 & 3 & -1\\  
1 & 2 & 2 \\
1 & 1 & -3\\
\end{pmatrix}
\sim \begin{pmatrix}
2 & 3 & -1 \\  
2 & 3 & -1 \\
1 & 1 & -3 \\
\end{pmatrix}
\sim \begin{pmatrix}
2 & 3 & -1 \\  
0 & 0 & 0 \\
1 & 1 & -3 \\
\end{pmatrix} 
\sim \begin{pmatrix}
2 & 3 & -1 \\  
1 & 1 & -3 \\
\end{pmatrix} 
\Rightarrow \dim(V) = 2
$$

So, basis for $V \cap W$ should have representation both in $V$ and $W$:
$$
span(V \cap W) = V_{1}\alpha_{1} + V_{2}\alpha_{2} + V_{3}\alpha_{3} = W_{1}\beta_{1} + W_{2}\beta_{2} + W_{3}\beta_{3}
$$
$$
V \cap W \sim \begin{pmatrix}
1 & 2 & 1 \\  
1 & 1 & -1 \\
1 & 1 & -3 \\
2 & 3 & -1 \\  
\end{pmatrix}
\sim \begin{pmatrix}
1 & 2 & 1 \\  
1 & 1 & -1 \\
0 & 0 & -2 \\
2 & 3 & -1 \\  
\end{pmatrix}
\sim \begin{pmatrix}
1 & 2 & 0 \\  
1 & 1 & 0 \\
0 & 0 & -2 \\
2 & 3 & 0 \\  
\end{pmatrix}
\sim \begin{pmatrix}
0 & 1 & 0 \\  
1 & 1 & 0 \\
0 & 0 & -2 \\
0 & 1 & 0 \\  
\end{pmatrix}
\sim \begin{pmatrix}
1 & 1 & 0 \\
0 & 0 & -2 \\
0 & 1 & 0 \\  
\end{pmatrix}
\Rightarrow dim(V \cap W)
$$
So, basis for $V + W$ will be:
$$B_{V + W} = \{
\begin{pmatrix}  
1 \\  
2 \\
1  
\end{pmatrix},
\begin{pmatrix}  
1 \\  
1 \\
-1  
\end{pmatrix},
\begin{pmatrix}  
2 \\  
3 \\
-1  
\end{pmatrix} \}
$$
Basis for $V$ and $W$ will be:
$$
B_{V} = 
span\{
\begin{pmatrix}  
1 \\  
2 \\
1  
\end{pmatrix},

\begin{pmatrix}  
1 \\  
1 \\
-1
\end{pmatrix}
\},

B_{W} = \{
\begin{pmatrix}  
2 \\  
3 \\
-1  
\end{pmatrix},

\begin{pmatrix}  
1 \\  
1 \\
-3
\end{pmatrix}
\}
$$
Basis for $V \cap W$ will be:
$$
U = 
\alpha_{1}
\begin{pmatrix}  
1 \\  
2 \\
1  
\end{pmatrix} +
\alpha_{2}
\begin{pmatrix}  
1 \\  
1 \\
-1
\end{pmatrix} =

\beta_{1}
\begin{pmatrix}  
2 \\  
3 \\
-1  
\end{pmatrix} +

\beta_{2}
\begin{pmatrix}  
1 \\  
1 \\
-3
\end{pmatrix}
$$
$$
\begin{cases}
\alpha_{1} + \alpha_{1} - 2\beta_{1} - \beta_{2} = 0 \\
2\alpha_{1} + \alpha_{1} - 3\beta_{1} - \beta_{2} = 0 \\
\alpha_{1} - \alpha_{1} + \beta_{1} + 3\beta_{2} = 0 \\
\end{cases}
$$
So, 
$$
\begin{pmatrix}
1 & 1 & -2 & -1 \\  
2 & 1 & -3 & -1\\
1 & -1 & 1 & 3 \\
\end{pmatrix}
\sim \begin{pmatrix}
1 & 1 & -2 & -1 \\  
0 & -1 & 1 & 1\\
0 & -2 & 3 & 4 \\
\end{pmatrix}
\sim \begin{pmatrix}
1 & 1 & -2 & -1 \\  
0 & -1 & 1 & 1\\
0 & 0 & 1 & 2 \\
\end{pmatrix}
\sim \begin{pmatrix}
1 & 0 & 0 & 2 \\  
0 & -1 & 0 & -1 \\
0 & 0 & 1 & 2 \\
\end{pmatrix}
$$
Then let $\beta_{2} = -t, \alpha_{1} = 2t, \alpha_{2}=t, \beta_{1}=2t$
$$
V \cap W = \{ u = 
\begin{pmatrix}  
3 \\  
5 \\
1  
\end{pmatrix} t, t \in \mathbb{R}, B_{u} = \begin{pmatrix}  
3 \\  
5 \\
1  
\end{pmatrix}
\}
$$