<!-- Pagina 132 -->

III CASO VARIANZE IGNOTE 3

$\rightarrow$ campioni elevati, rimpizziamo $\sigma_x^2$ e $\sigma_y^2$
con le stime $S_x^2$ e $S_y^2$, senza ulteriori cambiamenti
($n_x \geq 30$, $n_y \geq 30$)

$\rightarrow$ piccoli campioni, V.C. NORMALI con VARIANZE
IGNOTE E NON NECESSARIAMENTE UGUALI: usiamo


$$
T = \frac{(\overline{X} - \overline{Y}) - (\mu_x - \mu_y)}{\sqrt{\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}}} \sim t_{\nu}
$$

$\rightarrow$ RISULTATO APPROSSIMATO, ma l'errore è trascurabile


$$
\nu = \frac{\left(\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}\right)^2}{\left[\frac{\left(\frac{S_x^2}{n_x}\right)^2}{n_x - 1} + \frac{\left(\frac{S_y^2}{n_y}\right)^2}{n_y - 1}\right]}
$$

, ARROTONDATO ALL'INTERO INFERIORE

FORMULA di WELCH / SATTERTHWAITE


$$
IC: \quad \left( \overline{x} - \overline{y} \right) \pm t_{\nu; 1 - \alpha/2} \sqrt{\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}}
$$