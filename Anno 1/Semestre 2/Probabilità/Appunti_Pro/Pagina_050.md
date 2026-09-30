<!-- Pagina 50 -->

Nota: talvolta la distribuzione viene parametrizzata in $\lambda = \dfrac{1}{\beta}$ (TASSO, $\lambda$, PARAMETRO DI SCALA, $\beta$). 
($\text{\`e}$ del tutto equivalente), $X \sim \mathcal{E}(\lambda)$

- F. di RIPARTIZIONE:

$$
F_X(x; \beta) = \left\lbrace 
\begin{array}{ll}
0 & x \le 0 \\
1 - e^{-\dfrac{x}{\beta}}, & x > 0
\end{array}
\right.
$$

$$
E(X) = \beta
$$

$$
V(X) = \beta^2
$$

Integrale per parti

- Percentili: $0 < \alpha < 1$

$$
1 - e^{-\alpha/\beta} = \alpha
$$

$$
\implies x_\alpha = -\left[ \log(1-\alpha) \right] \beta
$$