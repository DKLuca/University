<!-- Pagina 86 -->

B) Risultati per variabili bernoulliane

Se consideriamo $n$ v.c. bernoulliane $Y_i \sim \text{Bernoulli}(p)$, $i=1,\dots,n$, indipendenti, si ottiene facilmente che

$$
\sum_{i=1}^{n} Y_i \sim Bi(n,p) \,,
$$

Per $n$ elevato è più semplice utilizzare il t.l.c., che permette di **approssimare la binomiale con la normale**.

Al crescere di $n$, la distribuzione di una v.c. binomiale di parametri $n$ e $p$ si "avvicina" sempre di più a quella di una normale con parametri $\mu = np$ e $\sigma^2 = np(1-p)$.

L'approssimazione è ritenuta buona se $np > 5$ e $n(1-p) > 5$ (eventualmente utilizzando **correzioni di continuità** ($\pm 0.5$)), che migliorano l'approssimazione normale per v.c. discrete).