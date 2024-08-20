# 1. Definition

_Lattices studied in abstract algebra and set theory (order theory) both_.
## A. Lattice as a poset
Lattice  $L$ is a [[poset]] where every pair of elements has unique supremum (least upper bound or _join_ $\vee$) and unique infinum (greatest lover bound or _meet_ $\land$).

So, upper sub-lattice of lattice $L$ is defined as: 
$$\forall a,b \in L: \exists ! inf (a,b) \Longleftrightarrow \forall a,b \in L:a \vee b = inf (a,b)$$
Then lower sub-lattice of lattice $L$ is defined as: 
$$\forall a,b \in L: \exists ! sup(a,b) \Longleftrightarrow \forall a,b \in L:a \land b = sup (a,b)$$
Equivalently, [[poset]] $L$ is a lattice only if $L$ is a upper and lower sub-lattice at the same time.

Since, $L$ is [[poset]], then lattice $L$ could be represented as a Hasse diagram. 
## B. Lattice as an algebraic structure
Lattice $L$ defined  as [[algebraic system|algebraic system]] with two binary [[operation|operations]] $\langle L, \land, \vee \rangle$ (or $\langle L, +, \cdot \rangle$). These operations follows the next properties: 
1) idempotent laws: $a \vee a = a$, $a \wedge a = a$
2) absorption laws:  $a \vee (a \wedge b) = a$, $a \wedge (a \vee b) = a$
3) associativity: $a \vee (b \vee c) = (a \vee b) \vee c$, $a \wedge (b \wedge c) = (a \wedge b) \wedge c$
4) commutativity: $a \vee b = b ∨ a$, $a ∧ b = b ∧ a$

Each sub-lattice $\langle L, \vee \rangle$ and $\langle L, \land \rangle$ are behave as two commutative [[Monoid|monoids]] over the same domain set.
### Lema 2.B.1 Dedekind
Absorption law of lattice implies idempotency law.
$\forall x,y: x \vee (x \land y) = x$. Let $y = x \vee x \Longrightarrow  x = x \vee (x \land (x \vee x) ))$.
# 2. Properties
## 2.1 Lattice duality (connection between definitions A and B)
An order-theoretic lattice $L_{\leq}$ gives rise to the two binary operations $\vee$ and $\wedge$. Since the commutative, associative and absorption laws can easily be verified for these operations, they turns into a lattice $\langle L, \land, \vee \rangle$ in the algebraic sense.

The converse is also true. Given an algebraically defined lattice $\langle L, \land, \vee \rangle$, one can define a partial order $\leq$ on $L$ by setting:

$\forall a,b \in L$:
	$a \leq b$, if $a = a \wedge b$
	$a \leq b$, if $b = a \vee b$

The laws of absorption ensure that both definitions are equivalent:
$a = a \wedge b$ implies $b = b \vee (a \wedge b) = ( a \wedge b ) \vee b = a \vee b$

and dually for the other direction:
$b = a \vee b$ implies $a = a \wedge (a \vee b) = ( a \vee b ) \wedge b = a \wedge b$

If we are mention algebraic and poset-like properties of the lattice $L$ both at the same time, than we may combine algebraic operations and set relations in the signature like $\langle L, \land, \vee, \leq \rangle$.
### Theorem 2.1. Property of duality
If set of axiom on a lattices gives some equality, then $\vee$ could be replaced by $\wedge$ and 1 to 0 which results in valid equality also. From other side, if $\langle L, \land, \vee \rangle$ is a lattice then $\langle L, \vee, \land \rangle$ is also (dual) lattice.
## 2.2. Property of isotonicity (Theorem)
For lattice $\langle L, \land, \vee, \leq \rangle$ holds the following property:
$$
\forall x,y,z \in \langle L, \land, \vee, \leq \rangle: y \leq z \Longrightarrow
\left[ 
    \begin{array}{l}
        x \land y \leq x \land z &\\
        x \vee y \leq x \vee z &\\
    \end{array} 
\right.
$$
**Proof**. From one side we have: $y \leq z \Longrightarrow y = y \land z$. From another: $x \land y = x \land (y \land z) \Longrightarrow (x \land x) \land (y \land z) = (x \land y) \land (x \land z) \Longrightarrow x \land y \leq x \land z$
## 2.3. Property of half-distributivity (Theorem)
Lattices are half-distributive respectively to it's operations: $\forall x,y,z \in \langle L, \land, \vee, \leq \rangle$: 
1. $x \land (y \vee z) \geq (x \land y) \vee (x \land z)$
2. $x \vee (y \land z) \leq (x \vee y) \land (x \vee z)$
**Proof**. $x \geq x \land y$, $x \geq x \land z \Longrightarrow x \geq (x \land y) \vee (x \land z)$
$$
\left[ 
    \begin{array}{l}
		y \vee z \geq y \geq x \land y &\\
		y \vee z \geq z \geq x \land z
    \end{array} 
\right.
\Longrightarrow
y \vee z \geq (x \land y) \vee (x \land z)
\Longrightarrow
x \land (y \vee z) \geq (x \land y) \vee (x \land z)
$$
Using property of duality, we obtain $x \vee (y \land z) \leq (x \vee y) \land (x \vee z)$.
## 2.4. Theorem. Inclusion-exclusion formula
Let $\langle L, \land, \vee \rangle$ is a lattice, $\langle G, + \rangle$ and exists map $f: L \to G$ such as $\forall x,y \in L: f(x)+f(y)=f(x \vee y)+f(x \land y)$, then: $f(\bigvee_{i=1}^{n}x_{i})=\sum_{i=1}^{n}f(x_i)-\sum_{1 \leq i \lt j \leq n} f(x_i \land x_j) + \sum_{1 \leq i \lt j \lt k \leq n} f(x_i \land x_j \land x_k)-...+(-1)^{n-1}f(x_{1} \land x_{2} \land ... \land x_{n})$
### Examples:
1. $\langle \mathbb{N}, gcd, lcm \rangle$, $f: \mathbb{N} \to \langle \mathbb{Q}, \cdot \rangle$. Put $f(x)=x$ then $f(x)f(y)=xy=gcd(x,y) \cdot lcm(x,y)=f(x \land y) \cdot f(x \vee y)$
2. $\langle \mathbb{R}, min, max \rangle$, $f: \mathbb{R} \to \langle \mathbb{R}, + \rangle$. Put $f(x)=x$ then $f(x)+f(y)=x+y=min(x,y) + max(x,y)$
# 3. Bounds
## 3.1. Lattice over bounded posets
The [[poset]] $L$ is bounded if greatest element $\top$ in $L$ exists (also 1 or $inf(L)$) and a least element $\bot$ (also 0 or $sup(L))$ which satisfy:
$$\forall x \in L: 0 \leq x \leq 1$$
Hence:
$$\exists! 1 \in L: inf(L)=max(L)$$
$$\exists! 0 \in L: sup(L)=min(L)$$
A lattice may also be defined as an algebraic structure of the form $\langle L, \vee, \land, 0, 1 \rangle$ with consideration of bounds. Hence 0 is an identity element for the join operation $\vee$ (sub-lattice $\langle L, \vee, 0, \rangle$) and 1 is identity element for the meet sub-lattice $\langle L, \land, 1, \rangle$:
$$
\forall x \in L: x \vee 0=x
$$
$$
\forall x \in L: x \land 1=x
$$
### Lema 2.1.1. Kuratowski-Zorn
If each chain has upper bound in a [[poset]] then poset has max element.
### Consequence 2.1.1. Kuratowski-Zorn
Applying  Kuratowski-Zorn  we could state that every non-empty finite lattice is bounded. 
## 3.2. Lattice over unbounded poset
#Exception In some sources existence of unbounded lattices are allowed. We are **consider to not allow unbounded lattices generally** until we clearly state the opposite.

If existence of bounds unnecessary, then lattice $\langle L, \vee, \land \rangle$ redefines as an algebraic structure where sub-lattices $\langle L, \vee \rangle$ and $\langle L, \land \rangle$ are enough to preserve algebraic properties of a commutative [[halfgroup|halfgroups]].

#Kuratowski-Zorn #Consequence  #№2 If finite unbounded lattices are allowed in given set of axioms then such lattice could be embedded into bounded lattice by adding greatest (least) element via induction: 
$$1 = \bigvee_{a_i \in L, 0 < i < n} a_i $$
$$0 = \bigwedge_{a_i \in L, 0 < i < n} a_i $$
## 3.3. Lattice over infinite poset
#Exception Depending on purpose, infinite posets could be allowed. We are **consider to not allow infinite posets** until we clearly state the opposite.

We could extent #Kuratowski-Zorn #Consequence #№2 for infinite poset. Easy to see, that it's not practically possible to define **exact** unique upper (lower) bound for countable set with positively (negatively) infinite numbering of elements. Such situation appears in [[total order]] like $\mathbb{N}$ or $\mathbb{Z}$.

For cases like  $\mathbb{N}$ and $\mathbb{Z}$ (or any isomorphic), bounds could be defined as approximation to far greater element of the set then given subset:
$$\top = \bigvee_{a_i \in \mathbb{Z}, 0 < i \leq \infty } a_i \approx \infty$$
$$\bot \bigwedge_{a_i \in Z, -\infty \leq i \leq 0} a_i \approx -\infty$$
Analogously for upper bound in $\mathbb{N}$ (or $\mathbb{N}_{0})$. Then lower bound could be exactly defined for naturals as $\bot=1$ (or $\bot=0$ depending on number theoretic axiomatic used).

#Exception Such notation doesn't cover [[ordinals]]. In case if ordinals are used then given definition of bounds is still unapplicable without additional clarification. 
# 4. Examples

## 4.1 Finite total order
 Any total [[order]]. Ex.:  subset of _n_ natural numbers  $\mathbb{N}_\leq$ order or in terms of algebraic lattices $\langle \mathbb{N}_{n}, min, max \rangle$, where $\langle \mathbb{N}_{n}, min \rangle$ and $\langle \mathbb{N}_{n}, max \rangle$ are corresponding sub-lattices and [[Monoid|monoids]].
## 4.2 Poset over divisibility relation
[[poset|Poset]] over divisibility relation $\mathbb{N}_{\mid}$ for some number in $\mathbb{N}$ (or $\langle \mathbb{N}, gcd, lcm \rangle$).
![[Pasted image 20240106183926.png]]
## 4.3 Linguistic order
Linguistic [[order]] $\mathbb{L}_{\le}$
## 4.4 Boolean algebras
[[Boolean algebra|Boolean algebras]] over set of n-bit vectors $V_n$ in normal conjunctive (or disjunctive, or algebraic) forms.
## 4.5 Eulerian poset
Eulerian poset.
## 4.6 Finite set of integer pairs ordered componentwise.
![[Pasted image 20240106183754.png]]
## 4.7 Powerset of a set
[[powerset|Powerset]] of _A_ under set inclusion relation $\mathcal{P}(A)_{\subseteq}$ (or meet and join operations): $\langle 2^{A}, \subseteq \rangle$ (or $\langle 2^{A}, \cup, \cap \rangle$)

![[Pasted image 20240106183531.png]]
## 4.8 Closure of a set
[[closure|Closure]] 
## 4.9 Collection of all partitions of set ordered by refinement.

![[Pasted image 20240106183628.png]]

## 4.10 Lattice of subgropus
Let $\langle G, \circ \rangle$ is a group, then $Sub(G)$ is a set of subgroups. By Lagrange's theorem $Sub(G) \neq \emptyset$ and contains at least trivial subgroups. We are going to define operations of intersection and Descartes product over $Sub(g)$ to get lattice $\langle Sub(G), \cap, \times \rangle$. 
### Show that intersection of groups is a non-empty group
Let $G_1,G_2 \subseteq Sub(G)$ are non-trivial groups, $G^{0} \in Sub(G)$ is a trivial group with $|G^0| = 1$. 
Let $gcd(|G_1|,|G_2|)=1$ then by Lagrange's theorem we have: $\#G_1 | \#[G_1 \cap G_2]$, $\#G_2 | \#[G_1 \cap G_2]$, $\#[G_1 \cap G_2] | \#[Sub(G)]$. This leads us to $\#[G_1 \cap G_2] = |G^{0}| \Rightarrow G_1 \cap G_2 \cong G^{0}$. Then pairwise intersection of all possible subgroup pairs (with co-prime orders) returns supremum $\bot$ of semi-lattice $\langle Sup(G), \cap \rangle$: $\bigcap_{i,j = 1, i \neq j}^{i,j=|Sub(G)|} G_{i} \cap G_{j} = \bigcap_{k = 1}^{k=|Sub(G)|} G_{k}^{0} =\{ \emptyset \} = min(\langle Sup(G), \cap \rangle) = \bot$
### Show that Descartes product of groups forms a semi-lattice
Let $G_1,G_2 \subseteq Sub(G)$ are non-trivial groups and $G_{1} \times G_2 = \{ g_{1}g_{2}, g_1 \in G_1, g_2 \in G_2\}$.
## 4.11 Lattice of ideals
## 4.12 Set of functions defined on closed interval
Let $X \subseteq \mathbb{R}$ then $\mathbb{R}^{X}$ is a set of maps in form $X \to \mathbb{R}$. Let $f$ and $g$ are functions defined for some interval within $\mathbb R^{X}$: $f,g \in \mathbb {R}^{X}: h = min\{f,g\} \Longrightarrow \forall x \in \mathbb{R}^{X}: min \{ f(x),g(x) \}$. So we obtain semi-lattice $\langle \mathbb{R}^{X}, min \rangle$ defined for functions in $\mathbb {R}^{X}$ respectively to $min$ operation. Then $\langle \mathbb{R}^{X}, max \rangle$ works similarly. So, $\langle \mathbb{R}^{X}, min, max \rangle$ is a lattice.
## 4.13 Set of subspaces of vector space
Show that set all subspaces for vector space is lattice respectively to intersection and addition  $\langle V, \cap, + \rangle$.
# 5. Non-Examples

1) Descrete [[order]] with at least two uncomparable elements which dones't have meet or join: $\exists a,b \in L: (sup(a,b)=\emptyset) \vee (inf(a,b)=\emptyset)$
![[Pasted image 20240106184212.png]]
2) [[poset|Poset]] is not forming a lattice if upper or lower bound is not exactly defined: $!\nexists a, b \in L: ( a = max(L) = (inf(L)) ) \vee ( b = min(L) = sup(L) )$. Ex.: $\mathbb{N}$ - not defined upper bound; $\mathbb{Z}$ - not defined upper and lower bound.
![[Pasted image 20240106185100.png]]
3) Any [[set]] $A$ with at least two equal elements under some relation $R$. In other words, any  set which not preserve anti-symmetricy for relation on it. Such [[set|sets]] are not [[poset|posets]] by definition.
![[Pasted image 20240106185023.png]]
	According to Hasse diagram above we have $a \le b \le d \le f$ and $a \le c \le e \le f$. 
	Then for joins: $b \vee d = b$ and $b \vee e = b$ $\to$ $e = d = 1 \to$ by principle of duality it holds for meets.
	Analogously: $c \vee d = c$ and $c \vee e = c$ $\to$ $e = d = 1 \to$ by principle of duality it holds for meets.
	 Sum-up: 
		a) equal elements are exists in a given poset, then it's not a lattice.
		b) $inf(b, c)$ and $sup(d,e)$ are not unique, then given poset is not a lattice.

# 6. Classification of lattices according to optional properties
## 6.1 Distributivity
Algebraic operations on a lattice could preserve property of distributivity
$\forall a,b,c \in \langle L, \wedge, \vee\rangle$:
$$a \vee (b \land c) = (a \vee b) \land (a \vee c)$$
$$a \land (b \vee c) = (a \land b) \vee (a \land c)$$
#Lemma If lattice is distributive then $a \vee c = b \vee c$ and $a \wedge c = b \wedge c$ implies $a = b$:
$$ a = a \vee (a \wedge c) = a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c) = (a \vee b) \wedge (b \vee c) = b \vee (a \wedge c) = b \vee (b \wedge c) = b $$
#Lemma Any sub-lattice of a distributive lattice is also distributive lattice (by induction).

#Lemma Descartes product for distributive lattices is distributive lattice.

#Lemma If lattice $A$ is distributive then [[powerset]] $\mathcal{P}(A)$ is also distributive.

#Axiom The only non-distributive lattices with fewer than 6 elements are called $M_{3}$ and $N_{5}$ they are shown in Pictures 10 and 11, respectively. A lattice is distributive if and only if it does not have a sub-lattice isomorphic to $M_3$ or $N_5$. Each distributive lattice is isomorphic to a lattice of sets (with union and intersection as join and meet, respectively).
![[Pasted image 20240106185158.png]]
![[Pasted image 20240106185212.png]]

## 6.2 Modularity
Modularity is a weaker property then distributivity. A lattice $\langle L, \vee, \land \rangle$ is modular if: 
$$\forall a,b,c \in L: (a \wedge c) \vee (b \wedge c) = ((a \wedge c) \vee b) \wedge c$$
#Lemma Each distributive lattice is modular.

#Lemma Descartes product of two modular lattices is modular lattice.

#Lemma Sub-spaces of a vector space forms a modular lattice
## 6.3 Semimodularity

## 6.4 Completeness

## 6.5 Conditional completeness

## 6.6 Complement and pseudo-complement

## 6.7 Algebraicity
# 7. Lattice problems
## Shortest vector problem

[[SVP]]

## Closest vector problem

[[CVP]]



[[SIS]]

# 8. Generalizations of lattices
## 8.1 Skew lattice
Is a especial non-commutative generalization of a lattice. For a skew lattice $\langle  L, \vee, \wedge \rangle$ only two characteristics of operations are mandatory: associativity and idempotency law. The existence of bounds is not necessary laso. Then sub-lattices $\langle  L, \wedge \rangle$ and $\langle  L, \vee \rangle$ of a skew lattice acts like a halfgroups.
## 8.2 Continuos lattices

