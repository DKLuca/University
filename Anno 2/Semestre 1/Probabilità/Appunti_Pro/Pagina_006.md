<!-- Pagina 6 -->

# VARIANZA E COVARIANZA (1)

$\text{Def}$ $V(X)$ è la VARIANZA di $X$ (o della sua distribuzione):

$$
\sigma_{X}^{2} = V(X) = E \left[ \left( X - \mu_{X} \right)^{2} \right] = \begin{cases} 
\sum_{x} \left( x - \mu_{x} \right)^{2} p_{X}(x) & \text{CASO DISCRETO} \\
\int_{-\infty}^{+\infty} \left( x - \mu_{X} \right)^{2} f_{X}(x) \, dx & \text{CASO CONTINUO}
\end{cases}
$$

Misura la VARIABILITÀ di $X$

- $\sigma_{X} = \sqrt{V(X)}$ è la DEVIAZIONE STANDARD di $X$

- $\text{Nota:}$ FORMULA DI CALCOLO (analoga a quella vista nella statistica descrittiva)

$$
E \left[ \left( X - \mu_{X} \right)^{2} \right] = E \left( X^{2} \right) - \mu_{X}^{2}
$$

$\text{Prova:}$ (caso continuo, caso discreto è analogo)

$$
V(X) = \int_{-\infty}^{+\infty} \left( x^{2} + \mu_{X}^{2} - 2 x \mu_{X} \right) f_{X}(x) \, dx
$$

$$
= \int_{-\infty}^{+\infty} x^{2} f_{X}(x) \, dx + \mu_{X}^{2} \underbrace{\int_{-\infty}^{+\infty} f_{X}(x) \, dx}_{1} - 2\mu_{X} \underbrace{\int_{-\infty}^{+\infty} x f_{X}(x) \, dx}_{\mu_{X}}
$$