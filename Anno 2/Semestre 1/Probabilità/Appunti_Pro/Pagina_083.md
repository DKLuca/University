<!-- Pagina 83 -->

A) La v.c. varianza campionaria

Nel caso di variabili i.i.d., con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, ci sono dei risultati anche per **variabile casuale varianza campionaria**

$$
S^2 = \frac{1}{(n - 1)} \sum_{i=1}^{n} (Y_i - \overline{Y})^2
$$

- Se $Y_1, \dots, Y_n$ sono v.c. indipendenti con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, allora

$$
E(S^2) = \sigma^2
$$

$$
V(S^2) = (\sigma^2)^2 \left( \frac{2}{n - 1} + \frac{\kappa}{n} \right),
$$

con $\kappa$ costante che dipende dalla distribuzione ($0$ per $Y_i$ normali, ma non in generale).