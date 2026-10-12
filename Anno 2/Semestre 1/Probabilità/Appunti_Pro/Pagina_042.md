<!-- Pagina 42 -->

- L'approssimazione è ritenuta buona se
$$
\begin{matrix}
\left\lbrace 
\begin{matrix}
n p \ge 5 \\
n(1-p) \ge 5
\end{matrix}
\right.
\end{matrix}
$$

- Correzione di continuità (cc):
$$
\begin{matrix}
\left\lbrace 
\begin{matrix}
P(X \le n) = \Phi \left( \frac{n + 0.5 - n p}{\sqrt{n p(1-p)}} \right) \\
P(X < n) = \Phi \left( \frac{n - 0.5 - n p}{\sqrt{n p(1-p)}} \right)
\end{matrix}
\right.
\end{matrix}
$$

- POISSON $x_1, x_2, \dots, x_n$ iid, $x_i \sim P(\lambda)$

$$
\sum_{i=1}^n X_i \sim P(n\lambda) \text{ ma anche}
$$

$$
\sum_{i=1}^n X_i \stackrel{a}{\sim} \mathcal{N}(n\lambda, n\lambda)
$$

Quindi: se
$$
X \sim P(\lambda) \implies X \stackrel{a}{\sim} \mathcal{N}(\lambda, \lambda)
$$

L'approssimazione è ritenuta buona se $\lambda \ge 10$; anche qui possiamo applicare una cc di $0.5$