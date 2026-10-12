<!-- Pagina 135 -->

PROBLEMA: $X_i$ e $Y_i$ (stesso provino) (6)

NON SONO INDIPENDENTI!

Ci aspettiamo $\rho_{X_i, Y_i} > 0$ (e infatti $r_{x, y} > 0$)

Non possiamo usare le formule per campioni indipendenti!

SOLUZIONE: Considero le $n$ DIFFERENZE

$$
D_i = X_i - Y_i, \quad i = 1, 2, \dots, n \quad \text{CCS}
$$

$$
\begin{aligned}
E(D_i) &= \mu_X - \mu_Y = \mu_D \\
V(D_i) &= \sigma_D^2 \quad \text{IGNOTA}
\end{aligned}
$$

$\hookrightarrow$ Uso formula per IC per $\mu$ caso singolo campione, con varianza ignota

$$
\hat{\mu}_D \pm t_{n - 1; 1 - \alpha/2} \sqrt{\frac{S_D^2}{n}}
$$

- Al solito, per $n$ elevato uso $z_{1 - \alpha/2}$, invece di $t_{n - 1; 1 - \alpha/2}$