<!-- Pagina 59 -->

# La funzione generatrice dei momenti

* Data una v.c. $X$, la sua **funzione generatrice dei momenti** (**f.g.m.**) è la funzione reale con argomento $t \in \mathbb{R}$

$$
m_X(t) = E \left( e^{t X} \right)
$$

ovvero

$$
m_X(t) = \begin{cases}
\sum e^{t x} p_X(x) & \text{se } X \text{ è discreta} \\
\int_{-\infty}^{+\infty} e^{t x} f_X(x)dx & \text{se } X \text{ è continua}
\end{cases}
$$

* La f.g.m. esiste se la sommatoria o l'integrale sono finiti in un intervallo aperto che contiene lo zero, ovvero del tipo $(-t_0, t_0)$, con $t_0 > 0$.