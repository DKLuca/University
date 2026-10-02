<!-- Pagina 84 -->

A) Teorema del limite centrale

Teorema Sia $Y_1, Y_2, \dots$ una successione di v.c. indipendenti, ciascuna con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$. Allora, posto $Z_n = \sqrt{n}(\overline{Y} - \mu)/\sigma$, per ogni $z$

$$
\lim_{n \to \infty} P(Z_n \le z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-t^2/2} dt = \Phi(z) \,.
$$

In simboli il teorema del limite centrale (t.l.c.) si denota scrivendo

$$
Z_n = \sqrt{n}\frac{(\overline{Y} - \mu)}{\sigma} \xrightarrow{\mathcal{D}} \mathcal{N}(0, 1) \,,
$$

dove $\xrightarrow{\mathcal{D}}$ si legge "converge in distribuzione".

Una lettura **pratica** del teorema del limite centrale è la seguente:

$$
\overline{Y} \stackrel{a}{\sim} \mathcal{N}\left\lbrace \mu, \frac{\sigma^2}{n} \right\rbrace \,,
$$

dove $\stackrel{a}{\sim}$ significa "distribuita approssimativamente".