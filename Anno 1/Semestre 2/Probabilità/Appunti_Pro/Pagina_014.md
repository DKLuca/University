<!-- Pagina 14 -->

Prova: $V(\underbrace{aX+b}_{Y}) = E \left[ (Y - \mu_Y)^2 \right]$ (4)

$$
= E \left[ (aX+b - a\mu_X - b)^2 \right]
$$

$$
= E \left[ a^2(X-\mu_X)^2 \right] = a^2 V(X)
$$

RIS 7 $a, b \in \mathbb{R}$, $X, Y$ v.c.
$$
V(aX+bY) = a^2 V(X) + b^2 V(Y) + 2ab \operatorname{cov}(X,Y)
$$

Prova: $V(aX+bY) = E \left\lbrace \left[ (aX+bY) - (a\mu_X + b\mu_Y) \right]^2 \right\rbrace$

$$
= E \left\lbrace \left[ a(X-\mu_X) + b(Y-\mu_Y) \right]^2 \right\rbrace
$$

$$
= E \left\lbrace a^2(X-\mu_X)^2 + b^2(Y-\mu_Y)^2 + 2ab(X-\mu_X) \cdot (Y-\mu_Y) \right\rbrace = \rightarrow \text{applico RIS 5}
$$

$$
= a^2 E \left[ (X-\mu_X)^2 \right] + b^2 E \left[ (Y-\mu_Y)^2 \right] + 2ab \cdot E \left[ (X-\mu_X)(Y-\mu_Y) \right] \text{, ovvero il risultato}
$$