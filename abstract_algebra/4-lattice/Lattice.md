# Overview and classification
# Definition

_Lattices studied in abstract algebra and set theory (order theory) both_.
## A. Lattice as a poset
Lattice  $L$ is a [[poset]] where every pair of elements has unique supremum (least upper bound or _join_ $\land$) and unique infinum (greatest lover bound or _meet_ $\vee$).

So, upper sub-lattice of lattice $L$ is defined as: 
$$\forall a,b \in L: \exists ! inf (a,b) \Longleftrightarrow \forall a,b \in L:a \vee b = inf (a,b)$$
Then lower sub-lattice of lattice $L$ is defined as: 
$$\forall a,b \in L: \exists ! sup(a,b) \Longleftrightarrow \forall a,b \in L:a \land b = sup (a,b)$$

Equivalently, [[poset]] $L$ is a lattice only if $L$ is a upper and lower sub-lattice at the same time.

Since, $L$ is [[poset]], then lattice $L$ could be represented as a Hasse diagram. 
## B. Lattice as an algebraic structure
Lattice $L$ defined  as [[algebraic system|algebraic system]] with two binary [[descrete_math/0-set_theory/operation|operations]] $\langle L, \vee, \land \rangle$ (or $\langle L, +, \cdot \rangle$). These operations follows the next properties: 

1) idempotent laws: $a \vee a = a$, $a \wedge a = a$
2) absorption laws:  $a \vee (a \wedge b) = a$, $a \wedge (a \vee b) = a$
3) associativity: $a \vee (b \vee c) = (a \vee b) \vee c$, $a \wedge (b \wedge c) = (a \wedge b) \wedge c$
4) commutativity: $a \vee b = b ∨ a$, $a ∧ b = b ∧ a$

Each sub-lattice $\langle L, \vee \rangle$ and $\langle L, \land \rangle$ are behave as two commutative [[Monoid|monoids]] over the same domain set.
## C. Lattice duality (connection between definitions A and B)
An order-theoretic lattice $L_{\leq}$ gives rise to the two binary operations $\vee$ and $\wedge$. Since the commutative, associative and absorption laws can easily be verified for these operations, they turns into a lattice $\langle L, \vee, \land \rangle$ in the algebraic sense.

The converse is also true. Given an algebraically defined lattice $\langle L, \vee, \land \rangle$, one can define a partial order $\leq$ on $L$ by setting:

$\forall a,b \in L$:
	$a \leq b$, if $a = a \wedge b$
	$a \leq b$, if $b = a \vee b$

The laws of absorption ensure that both definitions are equivalent:
$a = a \wedge b$ implies $b = b \vee (a \wedge b) = ( a \wedge b ) \vee b = a \vee b$

and dualy for the other direction:
$b = a \vee b$ implies $a = a \wedge (a \vee b) = ( a \vee b ) \wedge b = a \wedge b$

#Principle #Duality If set of axiom on a lattices gives some equality, then $\vee$ could be replaced by $\wedge$ and 1 to 0 which results in valid equality also.
# Bounds
## Lattice over bounded posets
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
#Lema #Kuratowski-Zorn If each chain has upper bound in a [[poset]] then poset has max element.

#Kuratowski-Zorn #Consequence #№1  Applying  Kuratowski-Zorn  we could state that every non-empty finite lattice is bounded. 
## Lattice over unbounded poset
#Exception In some sources existence of unbounded lattices are allowed. We are consider to not allow unbounded lattices until we clearly state the opposite.

If existence of bounds unnecessary, then lattice $\langle L, \vee, \land \rangle$ redefines as an algebraic structure where sub-lattices $\langle L, \vee \rangle$ and $\langle L, \land \rangle$ are enough to preserve algebraic properties of a commutative [[halfgroup|halfgroups]].

#Kuratowski-Zorn #Consequence  #№2 If finite unbounded lattices are allowed in given set of axioms then such lattice could be embedded into bounded lattice by adding greatest (least) element: 
$$1 = \bigvee_{a_i \in L, 0 < i < n} a_i $$
$$0 = \bigwedge_{a_i \in L, 0 < i < n} a_i $$
## Lattice over infinite poset
#Exception Depending on purpose, infinite posets could be allowed. We are consider to not allow infinite posets until we clearly state the opposite.

We could extent #Kuratowski-Zorn #Consequence #№2 for infinite poset. Easy to see, that it's not practically possible to define **exact** unique upper (lower) bound for countable set with positively (negatively) infinite numbering of elements. Such situation appears in [[total order]] like $\mathbb{N}$ or $\mathbb{Z}$.

For cases like  $\mathbb{N}$ and $\mathbb{Z}$ (or any isomorphic), bounds could be defined as approximation to far greater element of the set then given subset:
$$\top = \bigvee_{a_i \in \mathbb{Z}, 0 < i \leq \infty } a_i \approx \infty$$
$$\bot \bigwedge_{a_i \in Z, -\infty \leq i \leq 0} a_i \approx -\infty$$
Analogously for upper bound in $\mathbb{N}$ (or $\mathbb{N}_{0})$. Then lower bound could be exactly defined for naturals as $\bot=1$ (or $\bot=0$ depending on number theoretic axiomatic used).

#Exception Such notation doesn't cover [[ordinals]]. In case if ordinals are used then given definition of bounds is still unapplicable without additional clarification. 
# Examples

## 1. Finite total order
 Any total [[order]]. Ex.:  subset of _n_ natural numbers  $\mathbb{N}_\leq$ order or in terms of algebraic structure$\langle \mathbb{N}_{n}, \leq, \ge \rangle$. That case is isomorphic to $\langle \mathbb{N}_{n}, min, max \rangle$, where $\langle \mathbb{N}_{n}, min \rangle$ and $\langle \mathbb{N}_{n}, max \rangle$ are corresponding sub-lattices and [[Monoid|monoids]].
## 2. Poset over divisibility relation
[[poset|Poset]] over divisibility relation $\langle \mathbb{N}, \mid \rangle$ for some number in $\mathbb{N}$ (or $\langle \mathbb{N}, gcd, lcm \rangle$).
![[Pasted image 20240106183926.png]]
## 3. Linguistic order
Linguistic [[order]] $\mathbb{L}_{\le}$ or in terms of algebraic systems $\langle \mathbb{L}, \ge, \le \rangle$.
## 4. Boolean algebras
[[Boolean algebra|Boolean algebras]] over set of n-bit vectors $V_n$ in normal conjunctive (or disjunctive, or algebraic) forms.
## 5. Eulerian poset
Eulerian poset.
## 6. Finite set of integer pairs ordered componentwise.
![[Pasted image 20240106183754.png]]
## 7. Powerset of a set
[[powerset|Powerset]] of _A_ under set inclusion relation $\mathcal{P}(A)_{\subseteq}$ (or meet and join operations): $\langle 2^{A}, \subseteq \rangle$ (or $\langle 2^{A}, \cup, \cap \rangle$)

![[Pasted image 20240106183531.png]]
## 8. Closure of a set
[[closure|Closure]] 
## 9. Collection of all partitions of set ordered by refinement.

![[Pasted image 20240106183628.png]]

## Lattice of subgropus
Lattice of [[subgroup|subgroups]]
Lattice of [[ideal|ideals]].
# Non-Examples

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

# Properties of lattices
## Distributivity
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

## Modularity
Modularity is a weaker property then distributivity. A lattice $\langle L, \vee, \land \rangle$ is modular if: 
$$\forall a,b,c \in L: (a \wedge c) \vee (b \wedge c) = ((a \wedge c) \vee b) \wedge c$$
#Lemma Each distributive lattice is modular.

#Lemma Descartes product of two modular lattices is modular lattice.

#Lemma Sub-spaces of a vector space forms a modular lattice
## Semimodularity

## Completeness

## Conditional completeness

## Complement and pseudo-complement

## Algebraicity

## Classification of lattices according to properties
![[Pasted image 20240107000934.png]]
# Boolean algebra as a special case of lattice

# Morphisms of lattices
# Lattice problems
## Shortest vector problem

[[SVP]]

## Closest vector problem

[[CVP]]



[[SIS]]

# Generalizations of lattices
## Skew lattice
Is a especial non-commutative generalization of a lattice. For a skew lattice $\langle  L, \vee, \wedge \rangle$ only two characteristics of operations are mandatory: associativity and idempotency law. The existence of bounds is not necessary laso. Then sub-lattices $\langle  L, \wedge \rangle$ and $\langle  L, \vee \rangle$ of a skew lattice acts like a halfgroups.
## Continuos lattices

