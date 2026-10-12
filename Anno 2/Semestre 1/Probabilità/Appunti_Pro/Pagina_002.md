<!-- Pagina 2 -->

ES 4.3

$X =$ tempo vita dispositivo

$$
f_X(x) = \left\lbrace \begin{array}{ll} \frac{20000}{x^3}, & x > 100 \\ 0, & \text{altrove} \end{array} \right.
$$

$$
\left( \int_{100}^{\infty} \frac{20000}{x^3} dx = 20000 \cdot \left(-\frac{1}{2}\right) \left(x^{-2}\right)\Big|_{100}^{\infty} = 1 \right)
$$

$$
E(X) = \int_{100}^{\infty} x \frac{20000}{x^3} dx = 200 \text{ ore}, \begin{array}{l} \text{DURATA} \\ \text{MEDIA} \end{array}
$$

- PROPOSIZIONE

$$
E[g(X)] = \left\lbrace \begin{array}{ll} \sum_{x} g(x) P_X(x) & \text{CASO DISCR.} \\ \int_{-\infty}^{\infty} g(x) f_X(x) dx & \text{CASO CONT.} \end{array} \right.
$$

Nota: che $Y = g(X)$ sia v.c. è immediato dalla definizione di v.c.; il risultato ci permette di evitare di dover calcolare la distribuzione di $Y$ per calcolare $E(Y)$. Deriva dalle proprietà di sommatorie e integrali.