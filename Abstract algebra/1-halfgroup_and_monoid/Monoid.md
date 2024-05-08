# Definition
Non-empty set $M$ with defined abstract operation $\circ$ on elements of $M$ forms an algebraic system $\langle M, \circ \rangle$ called monoid if the following statements are true:
1. The $\langle M, \circ \rangle$ is **closed** respectively to defined operation: $\forall a,b \in M: a \circ b = c, c \in M$
2. **Asociativity**: $\forall a,b,c \in M: (a \circ b) \circ c = a \circ (b \circ c)$
3. Exists left $e_L$ or right $e_R$ **identity** or both: $\forall a \in M: e_L \circ a = a$ and $\forall a \in M: a \circ e_R = a$.

#Lemma Monoid $M$ has only one identity element:  $\forall x \in M, \exists! e \in M: ex=xe$. Let $e_1, e_2 \in M \Rightarrow e_2 = e_1e_2 = e_1$

#Lemma If both left $a^{-1}_{L}$ and right $a^{-1}_{R}$ inverses of element $a$ are exists then they are equals: $\forall a \in M \exists a^{-1}_{L}, a^{-1}_{R} \Rightarrow a^{-1}_{L} = a^{-1}_{R}$. We have $a^{-1}_{L} a a^{-1}_{R} = (a^{-1}_{L} a) a^{-1}_{R} = a^{-1}_{L} (a a^{-1}_{R})$ which follows from associativity property of monoid.
# Power of the element
Let $n \in \mathbb{N}_0$ and $a^n \in M$. By induction, put base $a^0$, then for $\forall m: a^{m+1} = a^{m}a, m \in [1; n-1]$.

#Theorem $\forall m,n \in \mathbb{N}_0: a^na^m = a^{m+n}$
#Lemma Put $m=0$ as the base of induction: $a^{n}a^0=a^ne=a^{n+0}=a^n$. So, let $a^na^m = a^{m+n}$ then increase $m$ by induction step $m+1$: $a^{n}a^{m+1} = a^n(a^ma)=(a^na^m)a = a^{n+m}a = a^{n+m+1}$
#Consequence Powers of monoid's element are commutative: $a^n a^m = a^ma^n$.
# Orbit of the element
For element $a$ which belongs to monoid $M$ put $\langle a \rangle$ is orbit of element $a$:  $\langle a \rangle = \{ e, a, a^2, a^3, ... \}$. 
# Cyclic monoid
$M$ is a cyclic monoid if exists element $g$ which belongs monoid $M$ and powers of $g$ produces all elements of a cyclic monoid $M$:
$M$ - cyclic monoid $\Leftrightarrow \exists g \in M: M = \langle g \rangle$ then $g$ is generator.

#Theorem All existent cyclic monoids of infinite order are isomorphic to $\langle \mathbb{N}_0, + \rangle$.

If $M$ is a cyclic monoid of finite order $s$: $\exists min(s), s > 0: \exists m < s, g^s=g^m$. Where $m$ is preorder and $n$ is order of generator. Then $s,n,m$ connected by the relation: $n = s - m$. Cyclic monoids may be denoted as $C_{m,n}$.
![[Cyclic monoid structure.canvas]]
#Example: $\langle \mathbb{Z}_{20} \rangle$ with $\langle 2 \rangle = \{ 1, 2, 4, 8, 16, 12 \} \equiv C_{2,4}$
$1 \to  2 \to 4 \to 8 \to 16 \to 12 \to 4 \to ...$

# Examples
## Commutative monoids
Simple seen as monoids are following ones: $\langle \mathbb{N}_0, + \rangle$ , $\langle \mathbb{N}_0, * \rangle$ , $\langle \mathbb{Q}, * \rangle$, $\langle \mathbb{Z}_{n}, * \rangle$,  $\langle \mathbb{M}_{n \times n}(\mathbb{R}), * \rangle$
## Set of all automorphisms
1. Put $X$ as arbitrary set, then following Descartes power  ${X}^{X} = \{ f \mid f : X \to X \}$ is a set of all automorphisms. We may understand composition operation $\circ$ as abstract multiplication on arbitrary maps for $X$ into $X$. These statements produce the structure $\langle {X}^{X}, \circ \rangle$. Let's prove all monoid's properties for $\langle {X}^{X}, \circ \rangle$. Identity map existence. Let $e(x) = x$. Then: $e(f(x)) = f(e(f(x))) = f(x) \Rightarrow f \circ e = e \circ f$ . Additionally we can see that $\langle {X}^{X}, \circ \rangle$ non-commutative at general. Commutativity preserves for $\circ$ just only if given $f$ is injective.
2. The same works for $\langle 2^A, \cup \rangle$.

## Set of symmetry maps
Let's see into subset of ${X}^{X}$ just when $f$ is bijective map. This subset if a set of all symmetry groups of $X$: $Sym(X) \subset X^X$. Also $Sym(X) = \{ f \in X^X \mid f - bijection \}$

## Symmetric difference of sets
$\langle 2^A, \Delta \rangle$ is monoid at least:
1.  $A \Delta B \Delta C = B \Delta C \Delta A = A \Delta C \Delta B$ 
2. $A \Delta E = E \Delta A = A \Rightarrow E = \emptyset$
And $\langle 2^A, \Delta \rangle$ is Abelian group if consider additional properties:
1. Inverse element existance: $A^{-1} \Delta A = A \Delta A^{-1} = \emptyset$ because of $A^{-1} = A$
2. $A \Delta B = B \Delta A$
## Formal gramatics
Suppose $\mathbb{L}$ is set of words with operation of concatenation $|$ is monoid $\langle \mathbb{L}, | \rangle$. 
# Links
[[algebraic system]]
[[halfgroup]]
[[Descartes product]]