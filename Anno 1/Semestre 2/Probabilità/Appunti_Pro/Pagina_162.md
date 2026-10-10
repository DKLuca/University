<!-- Pagina 162 -->

(11) VERIFICA D'IPOTESI PER UNA PROPORZIONE (1)

$X_1, X_2, \dots, X_n \quad C.C.S.$

$X_i \sim \text{Bernoulli } (p)$

$$
\left\lbrace 
\begin{aligned}
H_0: &\quad p = p_0 \\
H_1: &\quad p \neq p_0
\end{aligned}
\right.
$$
$\hookrightarrow$ oppure $H_1$ UNILATERALE

Sotto $H_0$: 
$$
n \hat{p} = \sum_{i=1}^n X_i \sim B(n, p_0)
$$
$$
TLC \quad \hat{p} \stackrel{a}{\sim} N\left(p_0, \frac{p_0(1-p_0)}{n}\right)
$$

STATISTICA TEST: di solito si usa la v.c. standardizzata

$$
Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} \stackrel{a}{\sim} N(0,1)
$$
Sotto $H_0$