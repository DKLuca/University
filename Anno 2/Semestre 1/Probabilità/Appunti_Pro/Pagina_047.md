<!-- Pagina 47 -->

per $y > 0$

$$
f_Y(y; \mu, \sigma) = \phi \left( \frac{\log(y) - \mu}{\sigma} \right) \cdot \frac{1}{\sigma} \cdot \frac{1}{y}
$$

ovvero:

$$
f_Y(y; \mu, \sigma) = \left\lbrace \begin{array}{ll} 0, & y \le 0 \\ \frac{1}{\sqrt{2\pi}\sigma y} e^{-\frac{(\log(y)-\mu)^2}{2\sigma^2}}, & y > 0 \end{array} \right.
$$

- Grafici: si veda Fig. 6.29

- ESEMPIO 6.22

$$
X \sim \log N (3.2, 1)
$$

$$
\log(X) \sim N(3.2, 1)
$$

$$
P(X > 8) = P(\log(X) > \log(8))
$$

$$
= 1 - \Phi \left( \frac{\log(8) - 3.2}{1} \right)
$$

$$
= 0.8688
$$