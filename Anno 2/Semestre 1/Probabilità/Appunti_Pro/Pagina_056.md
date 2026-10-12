<!-- Pagina 56 -->

10 DISTRIBUZIONE WEIBULL

* Come la distribuzione gamma, estende la distr. esponenziale ma è molto più flessibile

$$
X \sim \text{Weibull}(\alpha, \beta)
$$

$$
f_X(x; \alpha, \beta) = \left\lbrace
\begin{array}{ll}
\alpha \beta x^{\beta-1} e^{-\alpha x^\beta}, & x > 0 \\
0, & x \leq 0
\end{array}
\right.
$$

$\alpha > 0$, $\beta > 0$ (parametro di forma)

* Se $\beta = 1$, $X \sim \mathcal{E}(\alpha)$

* $F$ di ripartizione per $x > 0$:

$$
F_X(x; \alpha, \beta) = \int_0^x \alpha \beta t^{\beta-1} e^{-\alpha t^\beta} dt
$$

poniamo 
$$
\begin{array}{l}
u = \alpha t^\beta \\
du = \alpha \beta t^{\beta-1} dt
\end{array}
$$