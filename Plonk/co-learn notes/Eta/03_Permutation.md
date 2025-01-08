# 03. Permutation

<table>
  <tr>
    <th>title</th>
    <th>tags</th>
  </tr>
  <tr>
    <td>03. Permutation</td>
    <td>
      <table>
        <tr>
          <th>zk-meme</th>
          <th>basic</th>
          <th>quick_read</th>
          <td>Permutation</td>
        </tr>
      </table>
    </td>
  </tr>
</table>

[Github](https://github.com/ETAAcademy)｜[Twitter](https://twitter.com/ETAAcademy)｜[ETA-ZK-Meme](https://github.com/ETAAcademy/ETAAcademy-ZK-Meme)

Authors: [Eta](https://twitter.com/pwhattie), looking forward to your joining

## Permutation

A verifier can verify multiple copy constraints within a table $\omega$ using just one random challenge, without even seeing the table itself. For $\omega$, cyclic permutations are performed for the positions that need to be equal, and then the prover demonstrates that the original $\omega$ table is equal to the cyclically permuted $\omega'$ table. **Verifying table equality can be achieved through polynomial encoding and probabilistic checking**

### Cold Start: Grand Product

1. **Product Relation:**
   The product $p = q_0 \cdot q_1 \cdot q_2 \cdot \cdots \cdot q_{n-2}$ is proved by converting a cumulative product calculation into multiple single multiplication. An auxiliary vector $\vec{r}$, acting as an accumulator, is introduced to represent the "intermediate values" after each multiplication, essentially capturing the entire calculation trace of the product process. The leftmost column represents the original vector to be multiplied { $q_i$ }, the middle column { $r_i$ } is the auxiliary variable that stores the intermediate value "before each single multiplication," and the rightmost column shows the value after each multiplication.

   Interestingly, when we shift the "middle column" vector, r , up one row, it becomes almost identical to the "rightmost column," except for the last element.

2. **Polynomial Constraints:**
   When we encode the three columns of the table as polynomials, they satisfy three specific constraints based on Lagrange Basis polynomials:

   - Initial value: $r_0 = 1, r_{n-1} = p$:
     $L_0(X) \cdot (r(X) - 1) = 0,$
     $L_{n-1}(X) \cdot (r(X) - p) = 0, \quad \forall X \in H.$
   - Recursive multiplication relation (removing $\omega^{-1}$ from the set):
     $q(X) \cdot r(X) = r(\omega \cdot X), \quad \forall X \in H \setminus \{\omega^{-1}\}.$

   Simplifying the Constraints:

   - We add a row to the product table, setting $q_{n-1} = 1/p$ (note: p is the product of vector $\vec{q}$. Thus, $r_n = r_0 = 1$. The rightmost column is exactly a cyclic shift of $vec{r}$.
   - The verifier can challenge the following polynomial equation:
     $L_0(X) \cdot (r(X) - 1) + \alpha \cdot (q(X) \cdot r(X) - r(\omega \cdot X)) = h(X) \cdot z_H(X).$
     Here, $\alpha$ is a random challenge number used to combine multiple polynomial constraints, and $h(X)$ represents the quotient polynomial, with $z_H(X) = (X-1)(X-\omega) \cdots (X-\omega^{n-1})$.

$$
\begin{array}{c|c|c}
q_i & r_i & q_i\cdot r_i \\
\hline
q_0 & 1  & r_0\\
q_1 & r_0 & r_1\\
q_2 & r_1 & r_2\\
\vdots & \vdots & \vdots\\
q_{n-2} & r_{n-2} & r_{n-1}\\
q_{n-1}=\frac{1}{p} & r_{n-1} & 1 \\
\end{array}
$$

### Using Grand Product to Prove Multiset Equality:

1. If two polynomials p(X) and q(X) are equal, they must share the same set of roots { $q_i$ }.
   For example: $\prod_{i}(X - q_i) = q(X) = p(X) = \prod_{i}(X - p_i),$ $\\{q_i\\}=_{multiset}\\{p_i\\}$.

   By requesting a random number $\gamma$ from the verifier, the prover can prove that the vectors { $p_i$ } and { $q_i$} are equal in the multiset sense through the following equation:
   $\prod_{i \in [n]}(\gamma - p_i) = \prod_{i \in [n]}(\gamma - q_i)$

2. **Product Proof:**
   As mentioned earlier, the multiplication process is converted into a series of single multiplications using auxiliary vectors. Interestingly, two multiplications can be merged into one, as shown here:
   $\prod_{i \in [n]} \frac{(\gamma - p_i)}{(\gamma - q_i)} = 1.$

### From Multiset Equality to Permutation Proof:

If two vectors $\vec{a}$ and $\vec{b}$ satisfy a permutation $\sigma$, the combined vectors $\vec{a}'$ and $\vec{b}'$ will satisfy the multiset equality relationship. By combining vectors and position values, treating $(a_i, i)$ as one element and $(b_i, \sigma(i))$ as another element, a "permutation proof" can be converted into a "multiset equality." By requesting a random number $\beta$ from the verifier, the tuples can be "folded" into a single value.

$$
\begin{array}{|c|c | c|c|}
a_i & {i} & b_i & \sigma({i}) \\
\hline
a_0 & 0 & b_0=a_1 & 1 \\
a_1 & 1 & b_1=a_0 & 0 \\
a_2 & 2 & b_2=a_3 & 3 \\
a_3 & 3 & b_3=a_2 & 2 \\
\vdots & \vdots & \vdots & \vdots \\
a_{n-1} & n-1 & b_{n-1}=a_n & n \\
a_n & n & b_n=a_{n-1} & n-1 \\
\end{array}
$$

$$
\begin{array}{|c|c|}
a'_i=(a_i, i) & b'_i=({b}_i, \sigma(i)) \\
\hline
(a_0, 0) & (b_0=a_1, 1) \\
(a_1, 1) & (b_1=a_0, 0) \\
\vdots & \vdots \\
(a\_{n-1}, n-1) & (b\_{n-1}=a\_{n}, n) \\
(a\_n, n) & (b\_n=a\_{n-1}, n-1) \\
\end{array}
$$

$$
\begin{array}{|c|c|}
a'_i=(a_i+\beta\cdot i) & b_i'=(b + \beta\cdot \sigma(i)) \\
\hline
(a_0 + \beta\cdot 0) & (b_0 + \beta\cdot 1) \\
(a_1 + \beta\cdot 1) & (b_1 + \beta\cdot 0) \\
\vdots & \vdots \\
(a\_{n-1} + \beta\cdot n-1) & (b\_{n-1} + \beta\cdot n) \\
(a\_n + \beta\cdot n) & (b\_n + \beta\cdot (n-1))\\
\end{array}
$$

The verification process leverages multiset equivalence as a stepping stone to prove the existence of a permutation between two vectors, which relies on random challenges and polynomial encoding to ensure the validity of the proof.
