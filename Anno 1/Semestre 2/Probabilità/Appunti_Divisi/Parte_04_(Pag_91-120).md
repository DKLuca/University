<!-- ===== PAGINA 91 ===== -->

<!-- Pagina 91 -->

# La distribuzione $t$ di Student

Date due v.c. indipendenti, $Z \sim \mathcal{N}(0,1)$ e $X \sim \chi^2_n$, allora
$$Y = \frac{Z}{\sqrt{X/n}},$$

ha distribuzione $t$ di Student con $n$ gradi di libertà, $Y \sim t_n$.
Molto simile alla normale standard, a cui tende rapidamente al crescere di $n$, con $E(Y) = 0$ e $V(Y) = n/(n-2)$.

### Funzione di densità

> **[Nota Grafico: Un grafico cartesiano che mostra la funzione di densità della distribuzione $t$ di Student per diversi valori dei gradi di libertà ($n=5$ in linea continua, $n=10$ in linea tratteggiata, $n=100$ in linea puntinata). L'asse x va da $-6$ a $6$ e l'asse y (etichettato come $f(y)$) va da $0.0$ a $0.4$, mostrando curve simmetriche a campana simili a quella normale standard, ma con code più pesanti per $n$ piccoli.]**

---

*a.a 2024/2025 — R. Bellio* \hfill *26 / 28*



<!-- ===== PAGINA 92 ===== -->

<!-- Pagina 92 -->

# Altri risultati per la distribuzione normale

* Per la varianza campionaria, vale
  $$\frac{\sum_{i=1}^n (Y_i - \overline{Y})^2}{\sigma^2} = \frac{(n-1) S^2}{\sigma^2} \sim \chi_{n-1}^2 \, .$$

* $\overline{Y}$ e $S^2$ sono v.c. indipendenti.

* Media campionaria standardizzata e media campionaria **studentizzata**

  $$\frac{\overline{Y} - \mu}{\sqrt{\frac{\sigma^2}{n}}} \sim \mathcal{N}(0, 1) \, ,$$
  
  $$\frac{\overline{Y} - \mu}{\sqrt{\frac{S^2}{n}}} \sim t_{n-1} \, .$$



<!-- ===== PAGINA 93 ===== -->

<!-- Pagina 93 -->

## Un risultato per due campioni indipendenti

Se $X_1, \dots, X_{n_X}$ e $Y_1, \dots, Y_{n_Y}$ rappresentano due c.c.s. **tra loro indipendenti**, con $X_i \sim \mathcal{N}(\mu_X, \sigma_X^2)$ e $Y_i \sim \mathcal{N}(\mu_Y, \sigma_Y^2)$, allora utilizzando la proprietà che combinazioni lineari di v.c. sono normali si ottiene

$$\overline{X} - \overline{Y} \sim \mathcal{N}\left(\mu_X - \mu_Y, \frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}\right),$$

con il risultato che vale in maniera approssimata (via t.l.c.) nel caso di medie campionarie di campioni non normali.

---

*(a.a 2024/2025 — R. Bellio)* \hfill *(28 / 28)*



<!-- ===== PAGINA 94 ===== -->

<!-- Pagina 94 -->

Stima puntuale e controllo del modello



<!-- ===== PAGINA 95 ===== -->

<!-- Pagina 95 -->

# I problemi dell'inferenza statistica

Utilizzando il campione osservato $y = (y_1, \dots, y_n)$, alla luce del modello statistico parametrico prescelto, si vogliono ricavare informazioni sul parametro ignoto $\theta \in \Theta$. I principali problemi inferenziali sono suddivisibili in tre classi:

* **stima puntuale**: si vuole ottenere, sulla base dei dati del campione $y$, un valore numerico per $\theta$;
* **stima intervallare**: si vuole ottenere, sulla base dei dati del campione $y$, un sottoinsieme di $\Theta$ in cui è plausibilmente incluso $\theta$;
* **verifica di ipotesi**: data una congettura o un'ipotesi su $\theta$, si vuole verificare, sulla base dei dati del campione $y$, se essa è accettabile, cioè in accordo con i dati osservati.



<!-- ===== PAGINA 96 ===== -->

<!-- Pagina 96 -->

# Stima puntuale

Ipotizziamo allora di aver specificato un modello statistico parametrico per i dati del campione, ovvero una distribuzione di probabilità per $Y_i$ che indichiamo genericamente con $p(y_i; \theta)$, funzione di probabilità o di densità.

L'obiettivo della stima puntuale è utilizzare i dati per ottenere un valore plausibile del parametro, ovvero una sua **stima**.

In molti casi, esiste un modo abbastanza intuitivo per ottenere una stima di $\theta$.



<!-- ===== PAGINA 97 ===== -->

<!-- Pagina 97 -->

# Esempio: frazione campionaria di elementi difettosi

Si analizzano $n = 40$ elementi, scelti a caso tra quelli prodotti da un certo macchinario. Il campione osservato è

$$y = (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,$$
$$0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0) \text{,}$$

dove $0$ e $1$ indicano, rispettivamente, se l'oggetto è o non è conforme agli standard di qualità.

In questo caso è naturale assumere $Y_i \sim \text{Bernoulli}(p)$, con $p \in (0, 1)$, perciò nel caso specifico $\theta = p$ e $\Theta = (0, 1)$.

La media campionaria $\overline{y}$, ossia la **frazione campionaria di elementi difettosi**, è una stima naturale di $p$. Con $3$ difettosi su $40$ si ottiene

$$\widehat{p} = \frac{3}{40} = 0.075 \text{.}$$



<!-- ===== PAGINA 98 ===== -->

<!-- Pagina 98 -->

Esempio: peso di scatole di prodotto

Una macchina produce scatole di un certo prodotto di peso nominale $1\text{ Kg.}$, ma in realtà aventi distribuzione $\mathcal{N}(\mu, \sigma^2)$.

Si vuole stimare il peso medio effettivo e la varianza sulla base di un campione casuale semplice di $n = 20$ pezzi.

Dopo l'estrazione del campione si ottiene

$$\bar{y} = 1.007\text{ Kg } , \qquad s = 0.0027\text{ Kg } .$$

Appare naturale porre $\widehat{\mu} = 1.007$ e $\widehat{\sigma}^2 = 0.0027^2 = 7.29 \times 10^{-6}$.

Per valutare la proporzione di scatole comprese nell'intervallo $1 \pm 0.01$, si utilizzano poi le consuete formule per la normale, ovvero

$$\Phi\left(\frac{1.01 - 1.007}{0.0027}\right) - \Phi\left(\frac{0.99 - 1.007}{0.0027}\right) = 0.867 .$$

---
<div style="display: flex; justify-content: space-between; font-size: 0.9em;">
  <span>a.a 2024/2025 — R. Bellio</span>
  <span>5 / 26</span>
</div>



<!-- ===== PAGINA 99 ===== -->

<!-- Pagina 99 -->

# Stime e stimatori

La **stima** di un parametro è definita come un **valore** numerico ottenuto dai dati osservati del campione $y_1, \dots, y_n$.

Si definisce **stimatore** di un parametro di interesse una **variabile casuale** funzione delle v.c. $Y_1, \dots, Y_n$ che generano i valori osservati (quindi lo stimatore è una statistica e la stima ne è il valore osservato con i dati).

In generale, se $\theta$ è parametro di interesse, si denota con $\widehat{\theta}$ sia la stima $\widehat{\theta}(y_1, \dots, y_n)$ che lo stimatore $\widehat{\theta}(Y_1, \dots, Y_n)$, è poi il contesto a rendere chiare a quale delle due ci si riferisce.

Due punti importanti:
* Dato uno stimatore, come posso stabilire se si tratta di un buon stimatore? (**Proprietà di uno stimatore**).
* Come posso reperire un buon stimatore? (**Metodi di stima**)

---
*a.a 2024/2025 — R. Bellio* $\hfill$ *6 / 26*



<!-- ===== PAGINA 100 ===== -->

<!-- Pagina 100 -->

# Proprietà di uno stimatore

Si considera il comportamento dello stimatore al variare del campione, ovvero la vicinanza della sua distribuzione al valore del parametro. Due definizioni:

* $E(\widehat{\theta} - \theta)$ è la **distorsione** di $\widehat{\theta}$;
* $EQM(\widehat{\theta}) = E[(\widehat{\theta} - \theta)^2]$ è l'**errore quadratico medio** di $\widehat{\theta}$.

La loro espressione è una funzione del parametro $\theta$ e della dimensione campionaria $n$.

Si parla allora di:

* **Stimatore non distorto**: ha distorsione nulla, cioè $E(\widehat{\theta}) = \theta$.
* **Stimatore consistente (in media quadratica)**: al crescere della dimensione campionaria

$$EQM(\widehat{\theta}) \to 0\text{.}$$

---

a.a 2024/2025 — R. Bellio $\hfill$ 7 / 26



<!-- ===== PAGINA 101 ===== -->

<!-- Pagina 101 -->

# Consistenza

Mentre la non distorsione è una proprietà desiderabile, la consistenza è un requisito necessario per uno stimatore ragionevole. Vale infatti

$$EQM(\widehat{\theta}) = V(\widehat{\theta}) + (E(\widehat{\theta}) - \theta)^2\text{,}$$
$$= \text{varianza} + (\text{distorsione})^2\text{.}$$

La condizione di consistenza equivale allora a

$$\begin{cases}
\lim_{n \to \infty} E(\widehat{\theta}) = \theta\text{,} \\
\lim_{n \to \infty} V(\widehat{\theta}) = 0\text{.}
\end{cases}$$

In pratica si richiede che lo stimatore sia non distorto (almeno per $n \to \infty$) e che la sua varianza diventi sempre più piccola, ossia la sua distribuzione si concentri sempre più attorno al valore $\theta$.

All'aumentare dell'informazione campionaria, sembra ragionevole richiedere che la conoscenza su $\theta$ diventi sempre più precisa.



<!-- ===== PAGINA 102 ===== -->

<!-- Pagina 102 -->

# Precisione della stima

Per confrontare due (o più) stimatori consistenti di uno stesso parametro, è sufficiente confrontare il loro errore quadratico medio: lo stimatore con $EQM$ minore sarà preferibile.

Se gli stimatori sono non distorti, il confronto si riduce a verificare quale stimatore ha la minor varianza a parità di numerosità del campione (e si parla allora di **stimatore più efficiente** tra quelli considerati).

La radice della varianza di uno stimatore è detta **errore standard** (o talvolta **incertezza**)

$$\sigma_{\widehat{\theta}} = \sqrt{V(\widehat{\theta})},$$

e la sua valutazione con i dati del campione è detta **errore standard stimato** $\widehat{\sigma}_{\widehat{\theta}}$. L'errore standard stimato è generalmente utilizzato come misura della **precisione di stima**, ed è riportato assieme ad essa.

---
*a.a 2024/2025 — R. Bellio* \hfill *9 / 26*



<!-- ===== PAGINA 103 ===== -->

<!-- Pagina 103 -->

# Esempi

* Modello bernoulliano
Se $Y_i \sim \text{Bernoulli}(p)$, uno stimatore di $p$ è la media campionaria, cioè $\widehat{p} = \overline{Y}$. Si ottiene

$$E(\widehat{p}) = p \text{,}$$

$$V(\widehat{p}) = \frac{p(1-p)}{n} \text{.}$$

Lo stimatore è non distorto e consistente, e vale inoltre $\sigma_{\widehat{p}} = \sqrt{p(1-p)/n}$.  
Con $n = 40$ e $\widehat{p} = 0.075$, si ottiene $\widehat{\sigma}_{\widehat{p}} = 0.0416$.

* Modello Poisson
Se $Y_i \sim \mathcal{P}(\lambda)$, uno stimatore di $\lambda$ è di nuovo la media campionaria, $\widehat{\lambda} = \overline{Y}$. Si ottiene

$$E(\widehat{\lambda}) = \lambda \text{,}$$

$$V(\widehat{\lambda}) = \frac{\lambda}{n} \text{.}$$

Lo stimatore è non distorto e consistente.



<!-- ===== PAGINA 104 ===== -->

<!-- Pagina 104 -->

• Modello normale

Se $Y_i \sim \mathcal{N}(\mu, \sigma^2)$, allora $\bar{Y}$ e $S^2$ sono due stimatori per $\mu$ e $\sigma^2$. Si ottiene

$$E(\bar{Y}) = \mu \, , \quad V(\bar{Y}) = \frac{\sigma^2}{n} \, ,$$

$$E(S^2) = \sigma^2 \, , \quad V(S^2) = \frac{2(\sigma^2)^2}{(n-1)} \, .$$

Entrambi gli stimatori sono non distorti e consistenti; il denominatore $(n-1)$ nella definizione di $S^2$ serve proprio ad ottenere la non distorsione.



<!-- ===== PAGINA 105 ===== -->

<!-- Pagina 105 -->

Per lo stimore alternativo (e più intuitivo) per la varianza

$$\widehat{\sigma}^2 = \frac{\sum_{i=1}^{n}(Y_i - \overline{Y})^2}{n}$$

si ottiene

$$E(\widehat{\sigma}^2) = \frac{(n-1)}{n} \sigma^2, \qquad V(\widehat{\sigma}^2) = \frac{(n-1)}{n} \cdot \frac{2(\sigma^2)^2}{n},$$

per cui si tratta comunque di uno stimore consistente.

---
*(a.a 2024/2025 — R. Bellio)* \hfill *(12 / 26)*



<!-- ===== PAGINA 106 ===== -->

<!-- Pagina 106 -->

# Lo stimatore media campionaria

In generale, dato un qualsiasi modello statistico parametrico, la media campionaria $\overline{Y}$ è sempre uno stimatore non distorto e consistente di $\mu = E(Y_i)$, dato che, se $\sigma^2 = V(Y_i)$

$$E(\overline{Y}) = \mu , \quad \quad V(\overline{Y}) = \frac{\sigma^2}{n} .$$

La consistenza della media campionaria va sotto il nome di **legge dei grandi numeri**. Inoltre, il teorema del limite centrale assicura che la distribuzione di $\overline{Y}$ è approssimativamente normale.

Si noti inoltre che

$$\sigma_{\overline{Y}} = \frac{\sigma}{\sqrt{n}} .$$

In presenza di outliers, è preferibile utilizzare una media troncata, eliminando una percentuale (piccola) di dati. La media troncata è un esempio di **stimatore robusto**.



<!-- ===== PAGINA 107 ===== -->

<!-- Pagina 107 -->

# Metodi di stima

Esistono vari metodi di stima. In casi semplici, si utilizza il **metodo dell'analogia**, che ci porta a stimare la media con la media campionaria, la varianza con la varianza campionaria e così via.

Per situazioni generali, esistono vari metodi per reperire stimatori.

Tra gli altri, citiamo il **metodo della massima verosimiglianza**, che per molti versi è quello preferibile, ed è utilizzato nei software statistici per stimare i parametri di distribuzioni quali la Gamma e la Weibull, e per modelli statistici più complessi.

---
*(a.a 2024/2025 — R. Bellio)* \hfill *14 / 26*



<!-- ===== PAGINA 108 ===== -->

<!-- Pagina 108 -->

# Controllo empirico del modello

Alla luce dei dati disponibili $y = (y_1, \dots, y_n)$, per procedere con i metodi dell'inferenza statistica parametrica è necessario specificare un modello per i dati, ovvero una distribuzione di probabilità per le variabili casuali indipendenti $Y_1, \dots, Y_n$.

In certi casi la specificazione (soprattutto per dati continui) può essere non banale, ed è allora necessario procedere ad un **controllo empirico del modello**.

A tal fine, si utilizzano
- Metodi della statistica descrittiva, come l'**istogramma** o la **funzione di ripartizione empirica**.
- I **grafici di probabilità**.

---

<div style="display: flex; justify-content: space-between; font-size: 0.9em;">
  <span>a.a 2024/2025 — R. Bellio</span>
  <span>15 / 26</span>
</div>



<!-- ===== PAGINA 109 ===== -->

<!-- Pagina 109 -->

# Controllo mediante istogramma

L'istogramma nell'ambito inferenziale può essere interpretato come una **stima della funzione di densità**.

* La stima è valida a prescindere da quale sia la vera distribuzione dei dati.
* La stima è migliore per grandi campioni, cioè quando l'informazione campionaria aumenta.

Il controllo si effettua confrontando l'istogramma con la funzione di densità del modello teorico, con i **parametri** del modello teorico rimpiazzati da opportune **stime**.



<!-- ===== PAGINA 110 ===== -->

<!-- Pagina 110 -->

# Esempio: PM (bassa quota)

I dati sembrano avere una distribuzione asimmetrica: un modello adatto sembra essere la distribuzione Gamma, con $\widehat{\alpha} = 2.03$ e $\widehat{\beta} = 1.82$.

### Dati su scala originale

> **[Nota Grafico: Istogramma della densità dei dati in funzione di PM, con asse x da 0 a 12 e asse y da 0.00 a 0.20. È sovrapposta una curva di densità di colore rosso che mostra una distribuzione asimmetrica positiva (Gamma).]**



<!-- ===== PAGINA 111 ===== -->

<!-- Pagina 111 -->

### Esempio: PM (bassa quota)

In alternativa, è possibile effettuare la trasformazione $x_i = \sqrt[4]{y_i}$, e utilizzare un modello normale, con $\mu = \bar{x}$ e $\sigma^2 = s_x^2$.

**Dati trasformati**

> **[Nota Grafico: Istogramma della densità dei dati trasformati in funzione di PM, con sovrapposta una curva di densità normale rossa simmetrica centrata intorno a 1.3]**

---

a.a 2024/2025 — R. Bellio \hfill 18/ 26



<!-- ===== PAGINA 112 ===== -->

<!-- Pagina 112 -->

# Controllo mediante funzione di ripartizione empirica

In maniera analoga, è possibile utilizzare la funzione di ripartizione empirica, definita come

$$\widehat{F}_n(x) = \frac{1}{n}\sum_{i=1}^{n} I_x(y_i) = \frac{\text{Numero di osservazioni} \le x}{n},$$

dove $I_x(y_i)$ è una opportuna funzione indicatrice

$$I_x(y_i) = \begin{cases} 
1 & \text{se } y_i \le x \\ 
0 & \text{se } y_i > x 
\end{cases}$$

La funzione di ripartizione empirica stima la vera funzione di ripartizione, quindi il controllo in questo caso si fa confrontandola con la funzione di ripartizione del modello teorico.



<!-- ===== PAGINA 113 ===== -->

<!-- Pagina 113 -->

# Grafici di probabilità

I **grafici di probabilità** (o **carte di probabilità**) consentono di confrontare la distribuzione ipotizzata per i dati (teorica) con i dati campionari. Sono la tecnica più comunemente utilizzata.

Se $F(\cdot)$ indica la funzione di ripartizione teorica, i grafici sono dei diagrammi di dispersione delle coppie $\left( F(y_i), \widehat{F}_n(y_i) \right)$, oppure (equivalentemente) delle coppie $\left( F^{-1}(y_i), \widehat{F}_n^{-1}(y_i) \right)$, $i = 1, \dots, n$.

Anche in questo caso, occorre rimpiazzare i parametri del modello teorico con le stime ottenute dai dati.

Se il modello teorico è corretto, i punti tenderanno ad essere allineati lungo una linea retta.



<!-- ===== PAGINA 114 ===== -->

<!-- Pagina 114 -->

# Grafici di probabilità normali

I grafici di probabilità si possono costruire per tutte le distribuzioni continue, però i più utilizzati sono i **grafici delle probabilità normali**, che consentono di confrontare i dati con il modello teorico normale.

Si ottengono mediante un algoritmo in 3 passi

1. Considero $n$ valori equispaziati tra $0$ e $1$

$$p_i = \frac{i - 0.5}{n}, \qquad i = 1, \dots, n .$$

2. Rappresento con un diagramma di dispersione le coppie $(\Phi^{-1}(p_i), y_{(i)})$.
3. Se il modello normale è corretto, i punti tenderanno ad essere disposti lungo una linea retta.



<!-- ===== PAGINA 115 ===== -->

<!-- Pagina 115 -->

Situazioni di allontanamento dalla normalità possono aversi con **asimmetria** o **code pesanti**.

> **[Nota Grafico: Due grafici Q-Q plot. Il grafico a sinistra, intitolato "Asimmetria", mostra punti che si curvano verso l'alto rispetto alla retta di riferimento, tipico di una distribuzione asimmetrica a destra. Il grafico a destra, intitolato "Code pesanti", mostra punti che si discostano marcatamente dalla retta sia alle estremità inferiori che superiori, formando una tipica forma a "S", indicativa di code più pesanti rispetto alla distribuzione normale.]**

---

*a.a 2024/2025 — R. Bellio* \hfill *22 / 26*



<!-- ===== PAGINA 116 ===== -->

<!-- Pagina 116 -->

# Esempio: PM (bassa quota)

> **[Nota Grafico: Due grafici Q-Q plot a confronto. Quello a sinistra ("Dati su scala originale") mostra un forte scostamento dalla retta teorica a forma di "S" o "banana", indicando asimmetria positiva (code pesanti a destra). Quello a destra ("Dati trasformati") mostra i punti molto più allineati lungo la retta teorica dopo una trasformazione dei dati (es. logaritmica o radice).]**

---

a.a 2024/2025 — R. Bellio 
23 / 26



<!-- ===== PAGINA 117 ===== -->

# Esempio: contaminazione d'alluminio

I dati si riferiscono ad un campione di $n = 22$ contaminazioni d'alluminio (ppm).

| | | | | | | |
|---|---|---|---|---|---|---|
| 30 | 30 | 60 | 63 | 70 | 79 | 87 |
| 90 | 101 | 102 | 115 | 118 | 119 | 119 |
| 120 | 125 | 140 | 145 | 172 | 182 | |
| 183 | 191 | 222 | 244 | 291 | 511 | |

Cerchiamo un modello che sia appropriato per questi dati, scegliendo tra le distribuzioni normale, lognormale, esponenziale e Weibull, costruendo i grafici di probabilità per ciascuna di queste distribuzioni.

---
*a.a 2024/2025 — R. Bellio* \hfill *24 / 26*

<!-- ===== PAGINA 118 ===== -->

> **[Nota Grafico: Due grafici Q-Q plot a confronto. Quello a sinistra intitolato "Normale" mostra i punti che deviano marcatamente dalla linea retta teorica, specialmente per i valori più alti (coda pesante). Quello a destra intitolato "Lognormale" mostra i punti che seguono molto più da vicino la linea retta teorica, risultando complessivamente più allineati.]**

Il modello lognormale è più appropriato di quello normale...

<!-- ===== PAGINA 119 ===== -->

> **[Nota Grafico: Due grafici Q-Q plot per la valutazione della bontà di adattamento. Il grafico di sinistra è intitolato "Esponenziale" e mostra i quantili teorici rispetto ai dati empirici. Il grafico di destra è intitolato "Weibull" e mostra analogamente i quantili teorici per un modello di Weibull. Entrambi mostrano una deviazione marcata dei punti per il valore massimo superiore a 500 nei dati.]**

... e fornisce un miglior adattamento ai dati anche rispetto ai modelli esponenziale e Weibull.

---

a.a 2024/2025 — R. Bellio \hfill 26 / 26

<!-- ===== PAGINA 120 ===== -->

# STIMA PER INTERVALLO (1)

- Stima puntuale "manca" certamente il vero $\theta$
- Stima per intervallo: $\hat{\theta}_L < \theta < \hat{\theta}_U$
  
  $\underbrace{\hspace{7cm}}$
  
  Dipende dal valore osservato di $\hat{\theta}$ (e dalla sua distribuzione campionaria).
  
  è INSIEME DI VALORI PLAUSIBILI per $\theta$ alla luce dei dati.

- AMPIEZZA dell'intervallo: Indicazioni su accuratezza di $\hat{\theta}$

Def $P(\hat{\theta}_L < \theta < \hat{\theta}_U) = 1 - \alpha$, $0 < \alpha < 1$

$\hspace{0.5cm}\downarrow\hspace{1.5cm}\downarrow\hspace{2.2cm}\swarrow\hspace{1cm}\forall \theta \in \Theta$

$\hspace{0.4cm}\text{V.C.}\hspace{1.3cm}\text{V.C.}\hspace{1.8cm}\text{LIVELLO DI CONFIDENZA}$

$\begin{cases} 
\text{Per un campione osservato:} \quad \hat{\theta}_L < \theta < \hat{\theta}_U \text{ è} \\
\text{un INTERVALLO DI CONFIDENZA PER } \theta, \text{ e} \\
\text{i valori } \hat{\theta}_L \text{ e } \hat{\theta}_U \text{ sono i LIMITI DI CONFIDENZA}
\end{cases}$

- Abbrevieremo INTERVALLO DI CONFIDENZA con IC

