# 05. Polynomial Commitments

<table>
  <tr>
    <th>title</th>
    <th>tags</th>
  </tr>
  <tr>
    <td>05. Polynomial Commitments</td>
    <td>
      <table>
        <tr>
          <th>zk-meme</th>
          <th>basic</th>
          <th>quick_read</th>
          <td>Polynomial_Commitments</td>
        </tr>
      </table>
    </td>
  </tr>
</table>

[Github](https://github.com/ETAAcademy)｜[Twitter](https://twitter.com/ETAAcademy)｜[ETA-ZK-Meme](https://github.com/ETAAcademy/ETAAcademy-ZK-Meme)

Authors: [Eta](https://twitter.com/pwhattie), looking forward to your joining

## Polynomial Commitments

Polynomial commitment, `c = commit(x)`, is a cryptographic scheme that allows a prover to commit to a polynomial $f(X)$ in such a way that they can later prove that they know the value of $f(X)$ at a given point $x$ without revealing the entire polynomial.

**Hash**

The most basic construction of a polynomial commitment is to simply hash the coefficients of the polynomial. For example, if $f(X) = a_0 + a_1X + a_2X^2 + \cdots + a_nX^n$, then the commitment $C$ is:

$$
C = SHA256(a_0 || a_1 || a_2 || ... || a_n)
$$

**Petersen Commitment**

Another construction is the Petersen commitment, using a set of randomly chosen bases to compute an ECC point:

$$
C = a_0 G_0 + a_1 G_1 + \cdots + a_n G_n
$$

**KZG Commitment**

One of the most efficient construction is the KZG commitment, using a set of bases with internal algebraic structure $(G, \chi G, \chi^2G, \ldots, \chi^{d-1}G, H, \chi H)$. The KZG commitment to a polynomial $f(X)$ is:

$$
C_{f(X)} = a_0 G_0 + a_1  G_1 + \cdots + a_{n-1} G_{n-1}
= a_0  G + a_1 \chi G + \cdots + a_{n-1}\chi^{n-1} G
= f(\chi) G
$$

where $\chi$ is a random provided by a trusted third party, known as the trapdoor, which is destroyed after the setup phase. There is a bilinear pairing $e\in \mathbb{G}_1\times\mathbb{G}_2\to \mathbb{G}_T$, with $G\in \mathbb{G}_1$ and $H\in \mathbb{G}_2.$

## Optimization Round One🍄: Polynomial Remainder Theorem

KZG is a powerful tool for proving knowledge of a polynomial without revealing the polynomial itself. However, they can be computationally expensive, especially when proving the value of the polynomial at a point. The polynomial remainder theorem can be used to optimize KZG polynomial commitments and reduce the computational cost of proving polynomial values.

**Polynomial Remainder Theorem**

To make KZG polynomial commitments more succinct, we can use the Polynomial Remainder Theorem:

$$
f(X) = q(X) \cdot (X - \zeta) + y
$$

The prover provides the commitment to the polynomial q(X), $C_q,$ to prove $f(\zeta) = y$. The verifier checks whether $[q(\chi)]$ satisfies the divisibility:

$$
(f(X)-y) \cdot 1 \overset{?}{=} q(X) \cdot (X - \zeta)
$$

Using Groth's notation, where $[1]_1 \triangleq G$ and $[1]_2 \triangleq H$ are generators of two groups, we can express the verification equation as:

$$
e(C\_{f(X)} - y[1]_1, [1]_2) \overset{?}{=} e(C\_{q(X)}, [\chi]_2 - \zeta [1]_2)
$$

To reduce the expensive operations on \(\mathbb{G}2\), we can simplify to:

$$
f(X) + \zeta \cdot q(X) - y = q(X) \cdot X
$$

Hence:

$$
e(C\_{f(X)} + \zeta\cdot C\_{q(X)} -y\cdot[1]_1,\ [1]_2)\overset{?}{=} e(C\_{q(X)},\  [\chi]_2)
$$

This equation is equivalent to the original equation, but it reduces the number of operations in $\mathbb{G}\_2$.

## Batch Verification of Multiple Polynomial Commitments

One approach to batch verification is to use random linearization. Multiple polynomials can be combined into a larger polynomial using random numbers, allowing batch verification by opening at a single point:

**Combining Two Polynomials**:

- Given two polynomials $f_1(X)$ and $f_2(X)$, we can form a new polynomial $g(X) = f_1(X) + \nu \cdot f_2(X),$ where $\nu$ is a random number.
- Similarly, $q(X) = q_1(X) + \nu \cdot q_2(X)$ leads to $[q(\chi)]\_1 = \pi = \pi_1 + \nu \cdot \pi_2.$
- The commitment for the new polynomial g is $C_g = C_1 + \nu \cdot C_2.$
- The value of the polynomial at a single point $X = \zeta$ can be computed as $y_g = y_1 + \nu \cdot y_2.$
- The verifier checks the relation:

$$
  e(C - y \cdot G_0, H_0) \overset{?}{=} e(\pi, H_1 - x \cdot H_0)
$$

**Combining Multiple Polynomials**:

- For a more complex case, consider the polynomial constraint $f_1(X) f_2(X) + h_1(X) h_2(X) h_3(X) + g(X) = 0.$
- The straightforward approach involves the prover opening the commitments at $X = \zeta$ and sending the evaluations and corresponding proofs for each polynomial:

$$
(f_1(\zeta),\pi_{f_1}),(f_2(\zeta),\pi_{f_2}),(h_1(\zeta),\pi_{h_1}),(h_2(\zeta),\pi_{h_2}),(h_3(\zeta),\pi_{h_3}),(g(\zeta),\pi_{g})
$$

- The verifier then checks all six evaluation proofs and verifies the polynomial constraint:

$$
f_1(\zeta)f_2(\zeta) + h_1(\zeta)h_2(\zeta)h_3(\zeta) + g(\zeta) \overset{?}{=} 0
$$

## Optimization Round Two 🍄🏰: Reducing the Number of Openings

we will further optimize the process by reducing the number of openings required.

Consider a simple polynomial constraint of the form:

- The prover first opens $\bar{f} = f(\zeta)$ and sends the proof $\pi_{f(\zeta)}.$
- Introduce an auxiliary polynomial $L(X) = \bar{f} \cdot g(X) - h(X),$ then open $L(X)$ at $X = \zeta.$

In this optimized scheme, the prover needs to open only twice. The first opening is $\bar{f},$ and the second opening is for the constant 0, which does not need to be sent to the verifier. Thus, the prover only needs to send two evaluation proofs. Using the aggregation method from the previous section, with a challenge number 𝜈, the prover can aggregate the two polynomial commitments and only needs to send one evaluation proof.

**Complex Polynomial Constraint**

Similarly, consider a more complex polynomial constraint involving six polynomials:

$$
f_1(X) f_2(X) + h_1(X) h_2(X) h_3(X) + g(X) = 0
$$

This constraint can be optimized by introducing an auxiliary polynomial:

$$
L(X) = \bar{f}_1 ⋅ f_2(X) + \bar{h}_1 \bar{h}_2 ⋅ h_3(X) + g(X)
$$

The verifier sends a random number $\nu$, and the prover computes the commitment of the folded polynomial:

$$
[F]_1 = [L]_1 + \nu ⋅ [f_1(\chi)]_1 + \nu^2 [h_1(\chi)]_1 + \nu^3 [h_2(\chi)]_1
$$

and the value of the folded polynomial at $X = \zeta$:

$$
E = \nu ⋅ \bar{f}_1 + \nu^2 ⋅ \bar{h}_1 + \nu^3 ⋅ \bar{h}_2
$$

The verifier checks the following bilinear mapping equation:

$$
e([F]_1 - [E]_1 + \zeta [q(\chi)]_1, [1]_2) \overset{?}{=} e([q(\chi)]_1, [\chi]_2)
$$

This optimized protocol reduces the prover's workload to sending only three openings and one evaluation proof, compared to the original six openings and six evaluation proofs, thus significantly reducing the communication overhead (i.e., the proof size).

### Conclusion

Polynomial commitments are a powerful tool for proving knowledge of polynomials in a cryptographically secure way. They have a wide range of applications in cryptography and are likely to become even more important in the future as applications such as zk-SNARKs and zk-rollups become more widely adopted.
