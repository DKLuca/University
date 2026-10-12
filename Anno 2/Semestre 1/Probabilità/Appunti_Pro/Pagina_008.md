<!-- Pagina 8 -->

Di nuovo, possiamo considerare il caso continuo o quello discreto, i passaggi sono gli stessi. Qui prendiamo il caso discreto

$$
\operatorname{Cov}(X,Y) = \sum_x \sum_y (x - \mu_x)(y - \mu_y) \, p_{XY}(x,y)
$$

$$
= \sum_x \sum_y x y \, p_{XY}(x,y) - \mu_x \sum_x \sum_y y \, p_{XY}(x,y)
$$

$$
- \mu_y \sum_x x \sum_y p_{XY}(x,y) + \mu_x \cdot \mu_y \sum_x \sum_y p_{XY}(x,y)
$$

$$
= \sum_x \sum_y x y \, p_{XY}(x,y) - 2\mu_x \cdot \mu_y + \mu_x \cdot \mu_y
$$

$\underline{\qquad\qquad\qquad\qquad\qquad\qquad\qquad}$

$\text{Def}$: COEFFICIENTE DI CORRELAZIONE TRA $X$ e $Y$

$$
\rho_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y}, \quad -1 \le \rho_{XY} \le 1
$$

- Se $Y = a + bX \implies \left\lbrace \begin{array}{l} \rho_{XY} = 1 \text{ per } b>0 \\ \rho_{XY} = -1 \text{ per } b<0 \end{array} \right. $

Ha la stessa interpretazione di $\sigma_{XY}$, con il vantaggio di essere privo di unità di misura e standardizzato (tra $-1$ e $1$)