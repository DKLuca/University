<!-- Pagina 133 -->

- Esistono formule anche per il caso di VARIANZE IGNOTE MA UGUALI

$$
(\overline{x} - \overline{y}) \pm t_{n_x + n_y - 2; 1 - \alpha/2} \ s_p \sqrt{\frac{1}{n_x} + \frac{1}{n_y}}
$$

$$
s^2_p = \frac{(n_x - 1) s^2_x + (n_y - 1) s^2_y}{n_x + n_y - 2} \quad \begin{matrix} \text{STIMA} \\ \text{"POOLED"} \\ \text{DELLA VARIANZA} \end{matrix}
$$

- In pratica, l'IC con la formula di WELCH può essere usato anche se le varianze sono uguali.

ES 9.22

$$
\begin{matrix}
\underline{\text{FARMAC 1}} & \underline{\text{FARMAC 2}} \\
n_x = 14 & n_y = 16 \\
\overline{x} = 17 & \overline{y} = 19 \\
s^2_x = 1.5 & s^2_y = 1.8
\end{matrix}
$$

- IC $95\%$ : il testo calcola $(0.70, 3.30)$, assumendo uguali varianze.

- Formula di Welch: $\nu = 27.9 \implies \nu = 27$

$$
t_{27; \, 0.995} = 2.771
$$