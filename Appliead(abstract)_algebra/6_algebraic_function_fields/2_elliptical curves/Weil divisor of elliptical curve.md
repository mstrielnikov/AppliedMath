# Definition
Weil divisor $Div$ over field of elliptical curve $E$: $Div(E) = \sum_{P \in E} C_{p}(P)$ where $C_{p} \in \mathbb Z$.
Supplier of divisor: $Supp(Div(E)) = \{ \forall P \in E: C_{P} \neq 0 \}$
Degree of divisor: $Deg(E) = \sum_{P \in E} C_{P}$
Addition of divisors: $Div_{1}(E) + Div_{2}(E): \sum_{P \in E} C_{P_{1}} + C_{P_{2}}$
# Theorem
Set of all divisors over field $\mathbb F$ is a free Abelian group produced by points of $E$.
# Examples
1. $Div(E) = 2P + 3[2P] + 7O$, where $C_{p} = 2, C_{2p} = 3, C_{O} = 7$ and $Supp(Div(E) = \{ P, 2P, O \})$
2. $Div(E) = 2[P]$, where $C_p = 1, C_{2p} = 0$ and $Supp(Div(E) = \{ P \})$
3. $Div(E) = [2P]$, where $C_p = 0, C_{2p} = 1$ and and $Supp(Div(E) = \{ 2P \})$
# Main divisor
Let $f$ is real function defined on the points of elliptical curve $E$ with values on closure of $\mathbb F$.
For all $P \in E$ put $ord_{P}(f)$ as order of $P$ which satisfies $f(P) = 0$.
Then main divisor will have the following representation: $Div(f) = \sum_{P \in E} ord_{P}(f)(P)$.
# Divisor equivalence
One divisor $Div_1$ is equivalent to another divisor $Div_2$  is exists $Div(f)$ such that $Div_{2} = Div(f) + Div_1$. In other words: $Div_{1} \sim Div_2 \Longleftrightarrow Div_2 = Div(f) + Div_1$.
It's easy to see that set of all equivalent divisors $Div^{\sim}$ to given $Div_1$ 
# Theorem (Equivalence relation of zero divisors)
Let $Div_{E}$ is the set of all divisors defined for elliptic curve $E$. Then $Div_{E}^{0}$ is the subset of $Div_{E}$ where each of them has degree 0: $Div^0_{E} = \{ \forall Div \in Div_{E} : Deg(Div(E)) = 0 \}$. 
**The statement**. $Div^{0}_{E}/{\sim} \cong E$. 
# Further reading
1. [Wikipedia: Divisor(algebraic geometry)](https://en.wikipedia.org/wiki/Divisor_(algebraic_geometry))
2. [Weil pairings](https://www.youtube.com/watch?v=qFGFT41GXVw&list=PLhCN8H4P5Lvh9YH6Yv8X4w8Y-WIUYOqgp&index=20)
# Links
[[elliptic curves]]
[[Weil pairing]]