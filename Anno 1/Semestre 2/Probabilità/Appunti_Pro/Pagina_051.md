<!-- Pagina 51 -->

* RELAZIONE CON IL PROCESSO DI POISSON ($\rightarrow$ file d'attesa) (3)

PROPOSIZIONE: Dato un Processo di Poisson di tasso $\lambda > 0$, il tempo $T$ che intercorre tra 2 arrivi consecutivi è $T \sim \mathcal{E}(\lambda)$

Prova

- Otteniamo $F_T(t)$, verificando che ha la forma tipica della distribuzione esponenziale.

- Se $t \le 0$ ovviamente $P(T \le 0) = 0$
  $\downarrow$
  è un tempo

- Se $t > 0$: per calcolare $P(T \le t)$ introduciamo la v.c. $X$

$$
X = n^\circ \text{ arrivi in } [0, t]
$$

$$
X \sim \mathcal{P}(\lambda t)
$$

$$
P(T > t) = P(X=0) = e^{-\lambda t}, \text{ quindi } P(T \le t) = 1 - e^{-\lambda t}
$$
(PASSAGGIO CHIAVE)