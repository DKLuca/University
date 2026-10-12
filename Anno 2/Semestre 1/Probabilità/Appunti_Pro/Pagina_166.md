<!-- Pagina 166 -->


TLC:
$$
\hat{p}_X - \hat{p}_Y \stackrel{a}{\sim} N \left( p_X - p_Y, \frac{p_X(1-p_X)}{n_X} + \frac{p_Y(1-p_Y)}{n_Y} \right)
$$


Sotto $H_0$, $p_X = p_Y = p$ e perciò


$$
\sum_{i=1}^{n_X} X_i + \sum_{i=1}^{n_Y} Y_i \sim \text{Bi}(n_X + n_Y, p)
$$


$$
\hat{p} = \frac{\sum_{i=1}^{n} X_i + \sum_{i=1}^{n} Y_i}{n_X + n_Y}
$$


STIMATORE "POOLED" DELLA PROPORZIONE (valido sotto $H_0$)


STATISTICA TEST:
$$
Z = \frac{\hat{p}_X - \hat{p}_Y}{\sqrt{\hat{p}(1-\hat{p}) \left( \frac{1}{n_X} + \frac{1}{n_Y} \right)}}
$$


Sotto $H_0$:
$$
Z \stackrel{a}{\sim} N(0,1)
$$


- Per $R_\alpha$ e P-VALUE: stesse formule del caso di una proporzione