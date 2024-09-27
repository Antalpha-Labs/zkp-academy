# 02. Lagrange Interpolation

<table>
  <tr>
    <th>title</th>
    <th>tags</th>
  </tr>
  <tr>
    <td>02. Lagrange Interpolation</td>
    <td>
      <table>
        <tr>
          <th>zk-meme</th>
          <th>basic</th>
          <th>quick_read</th>
          <td>Lagrange_Interpolation</td>
        </tr>
      </table>
    </td>
  </tr>
</table>

[Github](https://github.com/ETAAcademy)｜[Twitter](https://twitter.com/ETAAcademy)｜[ETA-ZK-Meme](https://github.com/ETAAcademy/ETAAcademy-ZK-Meme)

Authors: [Eta](https://twitter.com/pwhattie), looking forward to your joining

## Lagrange Interpolation

Provers can combine multiple constraints into a single polynomial, which reduces communication and simplifies verification for Verifiers.

### Probabilistic Check of Polynomials

1. **Schwartz-Zippel Theorem**: The Verifier provides a random challenge $\zeta \in \mathbb{F}$ for two polynomials $f(\zeta) = g(\zeta)$. If the degree of the polynomials is small compared to the size of the field they're working in (like the number of elements in a set), the chance of $f(X) = g(X)$ getting a wrong answer is less than $\leq \frac{d}{|\mathbb{F}|}$(since a polynomial of degree d is determined by \(d+1\) points).

2. **Vector Verification**: Similar to above, vectors (lists of numbers) can be encoded as polynomials. To verify that three vectors $\vec{a} + \vec{b} = \vec{c}$, the direct method is to encode the vectors into polynomials (using the vector as polynomial coefficients), such as $a(X) = a_0 + a_1X + a_2X^2 + \cdots + a_{n-1}X^{n-1}$. We can create polynomials a(X), b(X), and c(X) from the lists a, b, and c, respectively. If the property $a_i + b_i = c_i$ holds true, then interestingly, adding the polynomials a(X) + b(X) will result in the polynomial c(X), a(X) + b(X) = c(X). By challenging with a random number $\zeta$, If we evaluate both sides of the equation a(ζ) + b(ζ) = c(ζ), then $\vec{a} + \vec{b} = \vec{c}$.

### Lagrange Interpolation and Evaluation Form

Multiplying polynomials can get messy. So, for checking if the element-wise product (think multiplication of corresponding entries) of two vectors equals a third vector, a special kind of polynomial encoding is used called Lagrange interpolation.

- Using Lagrange Interpolation to validate $\vec{a} \circ \vec{b} \overset{?}{=} \vec{c}$, where terms $a_i \cdot b_i$ and $c_i$ do not correspond to the coefficients of $X^i$.
- Instead, we use Lagrange interpolation polynomials Interpolation: $\{L_i(X)\}_{i\in[0,N-1]}$, where $L_i(w_i)=1$, and $L_i(w_j)=0 (j\neq i)$. Then $\vec{a}$ can be encoded as follows:

$$
a(X)=a_0\cdot L_0(X) + a_1\cdot L_1(X)+ a_2\cdot L_2(X) + \cdots + a_{N-1}\cdot L_{N-1}(X)
$$

- The element-wise product of vectors $a_i \cdot b_i = c_i$ resulting in $a(w_i) \cdot b(w_i) = c(w_i)$. Similarly, $\vec{a} \circ \vec{b} = \vec{c}$ translates to functions $a(X) \cdot b(X) = c(X)$ for all $X \in H$.

### Single Challenge Verification

To detect Prover’s cheating with a single challenge, transform the above equality by removing the specific X values (since X should cover a large range like $\mathbb{F}:$

$$
a(X) \cdot b(X) - c(X) = q(X) \cdot z_H(X), \quad \forall X \in \mathbb{F}
$$

Since $f(X) = 0$ for all $X \in H$ and $f(X) = a(X) \cdot b(X) - c(X)$,H is the root set of f(X):

$$
f(X)=(X-w_0)(X-w_1)(X-w_2)\cdots(X-w_{N-1})\cdot q(X)
$$

Thus, f(X) is divisible by the vanishing polynomial $z_H(X) = (X - w_0)(X - w_1) \cdots (X - w_{N-1})$. The Prover computes q(X) and sends it to the Verifier. Since H is a known system parameter, the Verifier can compute $z_H(X)$ and check:

$$a(\zeta) \cdot b(\zeta) - c(\zeta) \overset{?}{=} q(\zeta) \cdot z_H(\zeta)$$

### Optimization: Roots of Unity

There's a clever way to choose the roots of unity to simplify calculations. The subgroup H is formed by the powers of $\omega$:

$$
H = (1, \omega, \omega^2, \ldots, \omega^{N-1})
$$

These elements satisfy certain symmetries, e.g., $\omega = -\omega^{\frac{N}{2} + 1}$ and $\omega^i = -\omega^{\frac{N}{2} + i}$. Summing all roots of unity yields zero:

$$
\sum\_{i=0}^{N-1} \omega^i = 0
$$

In practical, we choose a large finite field with a large powers-of-2 multiplicative subgroup. Due to the symmetry of $\omega^i$, on the subgroup H, we have:

$$
z_H(X) = \prod*{i=0}^{N-1} (X - \omega^i) = X^N - 1
$$

In essence, polynomial encoding and Lagrange interpolation provide a powerful way to compress and verify complex relationships between data, simplifies many calculations and enhances efficiency in verification.
