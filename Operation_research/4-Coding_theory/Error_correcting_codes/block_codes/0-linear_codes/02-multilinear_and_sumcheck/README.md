# Multilinear Extensions, Sum-Check, and Secret Sharing

A conspectus on **multilinear polynomials** as the algebraic backbone of modern interactive proof systems and information-theoretically secure cryptography. The topics build from the core mathematical object (the multilinear extension) through the central algorithmic primitive (the Sum-Check Protocol) to applications in secret sharing and polynomial commitment schemes.

## Index

| # | Topic | Description |
|---|-------|-------------|
| 0 | [Multilinear Extensions](./0-multilinear_extensions.md) | Multilinear polynomials, Lagrange basis on the Boolean hypercube, uniqueness of MLE, evaluation algorithms |
| 1 | [Sum-Check Protocol](./1-sumcheck_protocol.md) | Interactive proof for hypercube sums, completeness, soundness, GKR generalization, zero-knowledge variant |
| 2 | [Multilinear Secret Sharing](./2-multilinear_secret_sharing.md) | MLE-based threshold secret sharing, packed batch schemes, verifiable MLSS, Byzantine tolerance |
| 3 | [Multilinear PCS and SNARKs](./3-multilinear_PCS_and_proofs.md) | Hyrax, PST/KZG multilinear, Dory commitment schemes, Spartan-style SNARK construction |
| 4 | [Sum-Check for Matrix Operations](./4-sumcheck_matrix_ops.md) | MatVec, MatMul, bilinear forms, GKR for deep products, batching, sparse matrices — all at $O(\log n)$ verifier cost |

## Topics Covered

- **Algebraic Foundations**: Multilinear polynomials, Möbius inversion, tensor products, Lagrange basis on $\{0,1\}^\ell$
- **Interactive Proofs**: Sum-Check Protocol, round-by-round soundness, GKR layered circuit proofs
- **Secret Sharing**: $(t,n)$-threshold multilinear schemes, packed/batch sharing, information-theoretic privacy proofs
- **Cryptographic Primitives**: Polynomial commitment schemes (Pedersen/DL-based, pairing-based, FRI-based), SNARK constructions
- **Linear Algebra Verification**: Sum-Check for MatVec, MatMul, bilinear forms, GKR-based deep matrix products, sparse and batched variants
- **Connections**: MLE ↔ RS codes, Sum-Check ↔ IP = PSPACE, MLSS ↔ MPC, PCS ↔ SNARKs

## Prerequisite Knowledge

| Concept | Covered In |
|---------|-----------|
| Finite fields $\mathbb{F}_q$ | [Cyclic Codes §0](../01-cyclic_codes/0-cyclic_codes.md) |
| Polynomial interpolation and evaluation | [Reed-Solomon §2](../01-cyclic_codes/2-Reed-Solomon_codes.md) |
| Schwartz-Zippel Lemma | [Schwartz-Zippel §5](../01-cyclic_codes/5-Schwartz_Zippel_Lemma.md) |
| Shamir Secret Sharing (univariate) | [Polynomial SS §7](../01-cyclic_codes/7-Polynomial_secret_sharing.md) |
| Polynomial Proximity / Low-Degree Testing | [Proximity §6](../01-cyclic_codes/6-Polynomial_Proximity.md) |
