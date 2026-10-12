<!-- Pagina 106 -->

# Lo stimatore media campionaria

In generale, dato un qualsiasi modello statistico parametrico, la media campionaria $\overline{Y}$ è sempre uno stimatore non distorto e consistente di $\mu = E(Y_i)$, dato che, se $\sigma^2 = V(Y_i)$

$$
E(\overline{Y}) = \mu \, , \qquad V(\overline{Y}) = \frac{\sigma^2}{n} \, .
$$

La consistenza della media campionaria va sotto il nome di **legge dei grandi numeri**. Inoltre, il teorema del limite centrale assicura che la distribuzione di $\overline{Y}$ è approssimativamente normale.

Si noti inoltre che

$$
\sigma_{\overline{Y}} = \frac{\sigma}{\sqrt{n}} \, .
$$

In presenza di outliers, è preferibile utilizzare una media troncata, eliminando una percentuale (piccola) di dati. La media troncata è un esempio di **stimatore robusto**.