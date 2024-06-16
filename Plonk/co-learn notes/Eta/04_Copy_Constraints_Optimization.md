# 04. Copy Constraints and Optimization

<table>
  <tr>
    <th>title</th>
    <th>tags</th>
  </tr>
  <tr>
    <td>04. Copy Constraints and Optimization</td>
    <td>
      <table>
        <tr>
          <th>zk-meme</th>
          <th>basic</th>
          <th>quick_read</th>
          <td>Copy_Constraints_Optimization</td>
        </tr>
      </table>
    </td>
  </tr>
</table>

[Github](https://github.com/ETAAcademy)｜[Twitter](https://twitter.com/ETAAcademy)｜[ETA-ZK-Meme](https://github.com/ETAAcademy/ETAAcademy-ZK-Meme)

Authors: [Eta](https://twitter.com/pwhattie), looking forward to your joining

## Plonk Protocol: Copy Constraints and Position Vector Optimization

### Copy Constraints

The copy constraints in the Plonk protocol ensure that the values of certain variables remain consistent across different columns of the W table. This is necessary for the protocol to correctly verify the computation of a circuit.

**Table W**

$$
\begin{array}{c|c|c|c|}
i & w_a & w_b & w_c  \\
\hline
0 & 0 & 0 & {\color{green}out} \\
1 & {\color{red}x_6} & {\color{blue}x_5} & {\color{green}out} \\
2 & x_1 & x_2 & {\color{red}x_6} \\
3 & x_3 & x_4 & {\color{blue}x_5} \\
\end{array}
$$

**Table of IDs**

$$
\begin{array}{c|c|c|c|}
i & id_{a,i} & id_{b,i} & id_{c,i}  \\
\hline
0 & 0 & 4 & {\color{green}8} \\
1 & {\color{red}1} & {\color{blue}5} & {\color{green}9} \\
2 & 2 & 6 & {\color{red}10} \\
3 & 3 & 7 & {\color{blue}11} \\
\end{array}
$$

**Permutation Vectors**

Introduce permutation vectors $\sigma_a, \sigma_b, \sigma_c:$

$$
\begin{array}{c|c|c|c|}
i & \sigma_{a,i} & \sigma_{b,i} & \sigma_{c,i}  \\
\hline
0 & 0 & 4 & {\color{green}9} \\
1 & {\color{red}10} & {\color{blue}11} & {\color{green}8} \\
2 & 2 & 6 & {\color{red}1} \\
3 & 3 & 7 & {\color{blue}5} \\
\end{array}
$$

**Prover's Process**

The prover uses random numbers $\beta$ and $\gamma$ provided by the verifier to merge and permute vectors, obtaining the multisets $f_i$ and $g_i$, which could be encoded into polynomials:

$$
\begin{split}
f(X)&=\Big(w_a(X)+\beta\cdot {id_a}(X)+\gamma\Big)\Big(w_b(X)+\beta\cdot {id_b}(X)+\gamma\Big)\Big(w_c(X)+\beta\cdot {id_c}(X)+\gamma\Big)\\
g(X)&=\Big(w_a(X)+\beta\cdot {\sigma_a}(X)+\gamma\Big)\Big(w_b(X)+\beta\cdot {\sigma_b}(X)+\gamma\Big)\Big(w_c(X)+\beta\cdot {\sigma_c}(X)+\gamma\Big)\\
\end{split}
$$

**Auxiliary Vector $\vec{z}$**

Construct $\vec{z}$ to represent intermediate steps:

$$
z_0 = 1, \qquad z_{i+1}=z_i\cdot \frac{f_i}{g_i}\\
$$

$$
\begin{array}{|c|c|c|}
i & H_i & z_i\\
\hline
0 & \omega^0=1 & 1\\
1 & \omega^1 & 1\cdot \frac{f_0}{g_0}\\
2 & \omega^2 & \frac{f_0}{g_0}\cdot \frac{f_1}{g_1}\\
3 & \omega^3 & \frac{f_0f_1}{g_0g_1}\cdot \frac{f_2}{g_2}\\
\vdots & & \vdots\\
N-1 & \omega^{N-1} & \frac{f_0f_1\cdots f_{N-3}}{g_0g_1\cdots g_{N-3}}\cdot \frac{f_{N-2}}{g_{N-2}} \\
N & \omega^{N}=1 & \frac{f_0f_1\cdots f_{N-1}}{g_0g_1\cdots g_{N-1}}  = 1
\end{array}
$$

If $\vec{f}$ and $\vec{g}$ are equivalent, $z_N = 1$. This is verified by ensuring:

$$
z(\omega^0) = 1
$$

$$
z(\omega\cdot X)g(X) = z(X)f(X)
$$

where:

- $z_0$ is an initial value of 1
- $z_i$ is the value of the copy constraint at step $i$
- $f_i$ is a polynomial expression representing the value of a variable at step $i$
- $g_i$ is a polynomial expression representing the value of a variable at step $i$
- $X$ is a variable
- $\omega$ is a generator of the multiplicative subgroup $H$

### Position Vector Optimization

The σ vectors only need to use distinct values to mark the permutations, not necessarily increasing natural numbers. If we use H = (1, ω, $ω^2,$ ...), then the polynomial ${id_a}(X)$ will be greatly simplified:

$$
\begin{split}
\vec{id}_a &= (1,\omega,\omega^2,\omega^3)\\
\vec{id}_b &= (k_1,k_1\omega,k_1\omega^2,k_1\omega^3)\\
\vec{id}_c &= (k_2,k_2\omega,k_2\omega^2,k_2\omega^3)\\
\end{split}
$$

where $k_i$ are distinct quadratic non-residues.

$$
id_a(X) = X, \quad id_b(X) = k_1 \cdot X, \quad id_a(X) = k_2 \cdot X
$$

If there are more columns in σ, then we need to choose multiple $k_1, k_2, k_3, ... = g^1, g^2, g^3, ...$ where g is a generator of the multiplicative subgroup T, and $|T|\*2^λ = p-1.$

### Public Inputs

$$
\begin{array}{c|c|c|c|}
i & q_L & q_R & q_M & q_C & q_O \\
\hline
0 & 0 & 0 & 0 & 99 & 1 \\
1 & 0 & 0 & 1 & 0 & 1 \\
2 & 1 & 1 & 0 & 0 & 1 \\
3 & 0 & 0 & 1 & 0 & 1 \\
\end{array}
$$

To prove that a circuit output equals a specific public value (e.g., out=99), the simplest method is to use the $q_C$ column with constraints $q_L = q_R = q_M = 0:$

$q_C(X) - q_O(X)w_c(X) = 0$

This method fixes the public values as constants, requiring recomputation of the $q_C(X)$ polynomial if values change, which is inefficient.

Introduce a new column $\phi$ for public parameters, which allow public input changes without affecting other parts of the circuit. The new arithmetic constraint is:

$q_L(X)w_a(X) + q_R(X)w_b(X) + q_M(X)w_a(X)w_b(X) - q_O(X)w_c(X) + q_C(X) + \phi(X) = 0$

In summary, handling public inputs efficiently in the Plonk protocol involves introducing a dedicated column for public parameters to avoid frequent recalculations of constraint polynomials. Additionally, optimizing position vectors and managing copy constraints with auxiliary vectors and random merging helps ensure the integrity and efficiency of the proof system.
