<!-- Pagina 160 -->

$$
Z = \frac{\overline{X} - \overline{Y} - \Delta_0}{\sqrt{\frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}}} \stackrel{a}{\sim} N(0, 1) \text{ sotto } H_0
$$

$$
z_{oss} = \frac{\overline{x} - \overline{y} - \Delta_0}{\sqrt{\frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}}} \quad\quad R_\alpha = \lbrace |z| > z_{1-\alpha/2} \rbrace
$$

$$
p = 2 \left( 1 - \Phi(|z_{oss}|) \right)
$$

- Per varianze ignote, ma campioni elevati:
stesse formule utilizzando $s_X^2$ e $s_Y^2$

2) Varianze ignote (e possibilmente diverse)

- Campioni normali (e piccoli)

$$
T = \frac{\overline{X} - \overline{Y} - \Delta_0}{\sqrt{\frac{s_X^2}{n_X} + \frac{s_Y^2}{n_Y}}} \sim t_\nu \text{ sotto } H_0
$$

$\nu = \text{ formula di WELCH / SATTERTHWAITE}$