<!-- Pagina 40 -->

10. TEOREMA DEL LIMITE CENTRALE (TLC)

$X_1, X_2, \dots, X_n \quad \boxed{i.i.d.}$

$E(X_i) = \mu, \quad V(X_i) = \sigma^2$

sia $Z_n = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}}$

allora $\lim_{n \to \infty} F_{Z_n}(z) = \Phi(z), \quad \forall z \in \mathbb{R}$

(Prova: anche qui si usa la f.g.m.)

- Interpretazione operativa del risultato:

per $n$ elevato, $Z_n \stackrel{a}{\sim} N(0, 1)$

ovvero

$$
\overline{X} \stackrel{a}{\sim} N\left(\mu, \frac{\sigma^2}{n}\right)
$$

- Si può esprimere per la somma:

$$
\sum_{i=1}^{n} X_i \stackrel{a}{\sim} N(n\mu, n\sigma^2)
$$