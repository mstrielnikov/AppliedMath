$BF_{n}$ - set of all [[Boolean function]]s over n-bits inputs

$$
x \in V_{n}, n \in \mathbb{N}
$$
$$
x = (x_1, x_2, ..., x_n)
$$
$$
f \in BF_n
$$
$$
f(x_1, x_2, ..., x_n) \equiv f(x)
$$

# Sub function $f'$ of Boolean function $f$

$f'$ is given by assigning constant values for the first $k$ variables within $x$-vector
$$
f' \in BF_{n-k}
$$
Let $f_0,f_1$ are sub functions such that:
$$
f_0(x_2,...,x_n) = f(0, x_2,...,x_n)
$$
$$
f_1(x_2,...,x_n) = f(1, x_2,...,x_n)
$$

 **Theorem A.** Shannon (or Boole's) expansion (decomposition)
$$
\forall f \in BF_n: f(x_1,...,x_n) = x_1f_1(x_2,...,x_n) \vee \bar{x_1}f_0(x_2,...,x_n)
$$

So  $T_f = (T_{f_0}, T_{f_1})$

**Consequence A.1**
Let $a, b \in \{ 0, 1 \}$ , then define $a^b$ such that:
$$
a^b =
\begin{cases}
a,b = 1
\\
\bar{a}, b=0
\end{cases}
$$$$
\Rightarrow
f(x_1, x_2, ...,x_n) = \bigvee_{a_1,a_2,...,a_n \in \{0,1\}} x_{1}^{a_{1}}x_{2}^{a_{2}}...x_{k}^{a_{k}}f(a_{1},a_{2},...,a_{k}, x_{k+1},...,x_{n})
$$
**Consequence A.2**
Let $x, u \in \ V_n$ , then
$$
x^u = x_{1}^{u_{1}}x_{2}^{u_{2}}...x_{n}^{u_{n}}
$$

**Consequence A.3**.
$$
f(x)= x^u = x_{1}^{u_{1}}x_{2}^{u_{2}}...x_{n}^{u_{n}} \Rightarrow f(x) = \bigvee _{u \in V_{n}} f(u)x^{u} 
$$$f(x)$ there often called Perfect disjunctive normal form of $f$.

# Shannon (or Boole's) expansion (decomposition)

**Consequence 1.2.1**.
$$
x \in V_3
$$
$$
a^{(b)} =
\begin{cases}
a,b = 1
\\
{1}, b=0
\end{cases}
$$
$$
x^{101} = x_1\bar{x_2}x_3
$$
$$
x^{000} = \bar{x_1}\bar{x_2}\bar{x_3}
$$
**Example 1.2.2**.
$$
x \in V_3
$$
$$
x^{(101)} = x_1x_3
$$
$$
x^{(000)} = 1
$$