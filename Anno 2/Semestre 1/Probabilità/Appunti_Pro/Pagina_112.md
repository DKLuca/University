<!-- Pagina 112 -->

Controllo mediante funzione di ripartizione empirica

In maniera analoga, è possibile utilizzare la funzione di ripartizione empirica, definita come

$$
\widehat{F}_n(x) = \frac{1}{n} \sum_{i=1}^n I_x(y_i) = \frac{\text{Numero di osservazioni } \le x}{n},
$$

dove $I_x(y_i)$ è una opportuna funzione indicatrice

$$
I_x(y_i) = \left\lbrace 
\begin{array}{ll}
1 & \text{se } y_i \le x \\
0 & \text{se } y_i > x
\end{array}
\right.
$$

La funzione di ripartizione empirica stima la vera funzione di ripartizione, quindi il controllo in questo caso si fa confrontandola con la funzione di ripartizione del modello teorico.