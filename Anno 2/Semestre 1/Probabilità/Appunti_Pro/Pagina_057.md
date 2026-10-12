<!-- Pagina 57 -->

$$
= \int_0^{\alpha x^\beta} e^{-u} du = 1 - e^{-\alpha x^\beta}
$$

Avendo:

$$
F_X(x; \alpha, \beta) = \begin{cases}
0, & x \le 0 \\
1 - e^{-\alpha x^\beta}, & x > 0
\end{cases}
$$

- Con passaggi analoghi si ottiene:

$$
E(X) = \frac{\Gamma\left(1 + \frac{1}{\beta}\right)}{\alpha^{1/\beta}}
$$

- TASSO DI GUASTO

$X$ V.C. DI DURATA (QUALSIASI)

$$
Z(x) = \frac{f_X(x)}{1 - F_X(x)}, \quad x > 0
$$

$$
1 - F_X(x) = \int_x^\infty f_X(t) dt \quad \text{AFFIDABILITÀ}
$$

La definizione di $Z(x)$ deriva dalla

$$
P(x < X < x + \varepsilon \mid X > x) = \frac{F_X(x + \varepsilon) - F_X(x)}{1 - F_X(x)} \quad \text{per } \varepsilon > 0
$$