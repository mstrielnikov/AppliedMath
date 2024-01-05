# Definition

_Lattices studied in abstract algebra and set theory both_

## A. Lattices in terms of sets (order theory)
Lattice  $L$ is a [[poset]] where every pair of elements has unique supremum (least upper bound or _join_ $\land$) $\sup L$ and unique infinum (greatest lover bound or _meet_ $\vee$) $\inf L$.

So, upper sub-lattice of lattice $L$ is defined as: 
$$\forall a,b \in L: \exists ! inf (a,b) \Longleftrightarrow \forall a,b \in L:a \land b = inf (a,b)$$
Then lower sub-lattice of lattice $L$ is defined as: 
$$\forall a,b \in L: \exists ! sup(a,b) \Longleftrightarrow \forall a,b \in L:a \vee b = sup (a,b)$$

Equivalently, [[poset]] $L$ is a lattice only if $L$ is a upper and lower sub-lattice at the same time.

Since, $L$ is [[poset]], then lattice $L$ could be represented as a Hasse diagram.

## B. In terms of universal (abstract) algebra
Lattice $L$ defined  as [[abstract_algebra/0-algebra/algebra|algebra]] with two binary [[descrete_math/0-set_theory/operation|operations]] $\langle L, \vee, \land \rangle$ (or $\langle L, +, \cdot \rangle$). These operations follows the next properties: 

1) idempotent laws: $a \vee a = a$, $a \wedge a = a$
2) absorption laws:  $a \vee (a \wedge b) = a$, $a \wedge (a \vee b) = a$
3) associativity: $a \vee (b \vee c) = (a \vee b) \vee c$, $a \wedge (b \wedge c) = (a \wedge b) \wedge c$
4) commutativity: $a \vee b = b ∨ a$, $a ∧ b = b ∧ a$

Each sub-lattice $\langle L, \vee \rangle$ and $\langle L, \land \rangle$ are forming a two commutative [[halfgroup|halfgroups]] over the same domain set.

## C. Connection between definitions A and B
An order-theoretic lattice $L_{\leq}$ gives rise to the two binary operations $\vee$ and $\wedge$. Since the commutative, associative and absorption laws can easily be verified for these operations, they turns into a lattice $\langle L, \vee, \land \rangle$ in the algebraic sense.

The converse is also true. Given an algebraically defined lattice $\langle L, \vee, \land \rangle$, one can define a partial order $\leq$ on $L$ by setting:

$\forall a,b \in L$:
	$a \leq b$, if $a = a \wedge b$
	$a \leq b$, if $b = a \vee b$

The laws of absorption ensure that both definitions are equivalent:

$a = a \wedge b$ implies $b = b \vee (b \wedge a)  b = b \vee ( b \wedge a ) = ( a \wedge b ) \vee b = a \vee b$

and dualy for the other direction.
## Bounds

The set $L$ is bounded if greatest element $\top$ in $L$ exists (also 1 or $inf(L)$) and a least element $\bot$ (also 0 or $sup(L))$ which satisfy:
$$\forall x \in L: 0 \leq x \leq 1$$
Hence:
$$\exists! 1 \in L: inf(L)=max(L)$$
$$\exists! 0 \in L: sup(L)=min(L)$$
A lattice may also be defined as an algebraic structure of the form $\langle L, \vee, \land, 0, 1 \rangle$. Hence 0 is an identity element for the join operation $\vee$ (sub-lattice $\langle L, \vee, 0, \rangle$) and 1 is identity element for the meet sub-lattice $\langle L, \land, 1, \rangle$:
$$
\forall x \in L: x \vee 0=x
$$
$$
\forall x \in L: x \land 1=x
$$

# Examples

1) [[powerset|Powerset]] of _A_ under set inclusion relation $\mathcal{P}(A)_{\subseteq}$ (or meet and join operations): $\langle 2^{A}, \subseteq \rangle$ (or $\langle 2^{A}, \cup, \cap \rangle$).
2) Any total [[order]]. Ex.:  subset of _n_ numbers within $\mathbb{N}$ ordered by relation of strict comparison $\langle \mathbb{N}_{n}, <, > \rangle$ which is equivalent to $\langle \mathbb{N}_{n}, min, max \rangle$.
3) Partial [[order|ordered]] set of $\mathbb{N}$ respectively to divisibility property $\langle \mathbb{N}, \mid \rangle$ (or $\langle \mathbb{N}, gcd, lcm \rangle$).
4) [[poset|Poset]] _A_ with reflexive relation such as $\le$ (or $=$) forms a lattice only if _A_ consists from single element.
5) Eulerian poset.
6) Linguistic [[order]] $\mathbb{L}_{\le}$ or in terms of lattices $\langle \mathbb{L}, \gt, \lt \rangle$.
7) [[Boolean algebra|Boolean algebras]] over set of n-bit vectors $V_n$ in normal conjunctive (or disjunctive, or algebraic) forms.
8) Finite set of integer pairs (vectors) ordered componentwise.
9) Collection of all partitions of any set _A_ ordered by refinement.
10) [[closure]].
11) Lattice of [[subgroup|subgroups]].
12) Lattice of [[ideal|ideals]].
# Non-Examples

1) Partial [[order]] is not forming a lattice if $\exists a,b \in L: (sup(a,b)=\emptyset) \vee (inf(a,b)=\emptyset)$.
2) Any [[poset]] with non-existing exact least or greatest element (unique upper or lower bound): $!\nexists a, b \in L: ( a = max(L) = (inf(L)) ) \vee ( b = min(L) = sup(L) )$. Ex.: $\mathbb{N}, \mathbb{Z}, \mathbb{R}$.
3) Any [[poset]] with at least two equal elements.

# Properties

## Completeness

## Conditional completeness

## Distributivity

## Skewness
## Modularity

## Semimodularity

## Continuity and algebraicity

# Morphisms of lattices

# Lattice problems
## Shortest vector problem

[[SVP]]

## Closest vector problem

[[CVP]]



[[SIS]]
