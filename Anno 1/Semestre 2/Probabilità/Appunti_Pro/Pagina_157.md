<!-- Pagina 157 -->

(1) CASO $\sigma^2$ IGNOTA (5)

- GRANDI CAMPIONI ($n \geq 30$): rimpiazzo $\sigma^2$ con $S^2$
- PICCOLI CAMPIONI: abbiamo risultati per campioni NORMALI
$$
X_1, X_2, \dots, X_n \text{ ccs } X_i \sim N(\mu, \sigma^2)
$$

$$
\left\lbrace \begin{aligned}
H_0: &\quad \mu = \mu_0 \\
H_1: &\quad \mu \neq \mu_0
\end{aligned} \right.
$$

Sotto $H_0$:
$$
T = \frac{\overline{X} - \mu_0}{\sqrt{\frac{S^2}{n}}} \sim t_{n-1}
$$

$$
R_\alpha = \left\lbrace |t| > t_{n-1; 1-\alpha/2} \right\rbrace
$$

P-VALUE:
$$
p = 2 \left( 1 - F_{t_{n-1}}(|t_{oss}|) \right)
$$