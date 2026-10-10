<!-- Pagina 161 -->

$$
R_\alpha = \left\lbrace |t| > t_{0; 1 - \alpha/2} \right\rbrace
$$

- Per $H_1$ unilaterale, $R_\alpha$ è come nel caso per grandi campioni rimpiazzando i percentili della $N(0,1)$ con quelli della $t$

3) DATI APPAIATI

$X_i$ e $Y_i$ RILEVATI SULLA STESSA UNITA (NON INDIPENDENTI)

$$
D_i = X_i - Y_i \quad, i = 1, \dots, n
$$

$$
D_i \sim N(\mu_D, \sigma^2_D) \quad (\text{CASO NORMALE})
$$

$$
T = \frac{\overline{D} - \Delta_0}{\sqrt{\frac{S^2_D}{n}}} \sim t_{n-1} \quad \text{sotto } H_0
$$

Nota:
$$
\begin{cases}
H_0: \mu_X - \mu_Y = \Delta_0 \\
H_1: \mu_X - \mu_Y \neq \Delta_0 \\
\phantom{H_1: \mu_X - \mu_Y} >_{<}
\end{cases}
\longrightarrow
\begin{cases}
H_0: \mu_D = \Delta_0 \\
H_1: \mu_D \neq \Delta_0 \\
\phantom{H_1: \mu_D} >_{<}
\end{cases}
$$