<!-- ===== PAGINA 61 ===== -->

<!-- Pagina 61 -->

Proprietà della f.g.m.

3. Se $X$ e $Y$ sono indipendenti, si ottiene

$$
m_{X+Y}(t) = m_X(t) \, m_Y(t) \,.
$$

Più in generale: se $X_1, \dots, X_n$ sono indipendenti, e
$S_n = \sum_{i=1}^n X_i$

$$
m_{S_n}(t) = \prod_{i=1}^n m_{X_i}(t) \, ,
$$

e se le $X_i$ hanno tutte la stessa distribuzione

$$
m_{S_n}(t) = (m_X(t))^n \,.
$$

Commento: la proprietà $1.$ dà il nome al metodo (e a volte è utile), ma le proprietà importanti sono la $2.$ e la $3.$

<!-- ===== PAGINA 62 ===== -->

<!-- Pagina 62 -->

# Alcune f.g.m. notevoli

| Distribuzione di $X$ | $m_X(t)$ | Definita per |
| :---: | :---: | :---: |
| $Bi(n,p)$ | $(1 - p + e^t p)^n$ | $\forall t \in \mathbb{R}$ |
| $\mathcal{P}(\lambda)$ | $e^{\lambda(e^t - 1)}$ | $\forall t \in \mathbb{R}$ |
| $\mathcal{N}(\mu, \sigma^2)$ | $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ | $\forall t \in \mathbb{R}$ |
| $\mathcal{G}a(\alpha, 1/\beta)$ | $\left(\frac{1}{1 - t\beta}\right)^\alpha$ | $t < \frac{1}{\beta}$ |

<div style="display: flex; justify-content: space-between; width: 100%; font-size: 0.9em;">
  <span>a.a 2024/2025 — R. Bellio</span>
  <span>4 / 7</span>
</div>

<!-- ===== PAGINA 63 ===== -->

<!-- Pagina 63 -->

# Applicazioni notevoli

Usando le proprietà della f.g.m. si possono ottenere molti risultati sulle v.c.

* Otteniamo la f.g.m. di $X + Y$, con $X \sim \mathcal{P}(\lambda_1)$ e $Y \sim \mathcal{P}(\lambda_2)$, indipendenti
* dalla proprietà 3. (e usando la tabella) si ottiene

$$
m_{X+Y}(t) = m_X(t) \, m_Y(t) = e^{\lambda_1 (e^t - 1)} \, e^{\lambda_2 (e^t - 1)},
$$

$$
m_{X+Y}(t) = e^{(\lambda_1 + \lambda_2)(e^t - 1)}
$$

* Si riconosce la f.g.m. di una distribuzione $\mathcal{P}(\lambda_1 + \lambda_2)$, e allora dalla proprietà 2. segue che

$$
X + Y \sim \mathcal{P}(\lambda_1 + \lambda_2)
$$

* Il risultato si estende ad una somma di un numero qualsiasi di v.c. di Poisson indipendenti.

<!-- ===== PAGINA 64 ===== -->

<!-- Pagina 64 -->

# Applicazioni notevoli

- Si procede in maniera analoga per trovare la distribuzione della somma di v.c. normali, Gamma (con lo stesso parametro di scala $\beta$) o binomiali (con lo stesso parametro $p$) indipendenti.

- Analogamente, si ottiene la distribuzione di trasformazione lineare di una v.c. normale: i passi sono i seguenti
  - Sia $X \sim \mathcal{N}(\mu, \sigma^2)$ e $Y = a + b X$, con $a, b \in \mathbb{R}$
  - Si ottiene facilmente che

$$
m_Y(t) = E[e^{(a+b X)t}] = e^{a t} m_X(b t) = e^{(a+b\mu)t + b^2 t^2 \sigma^2 / 2}\,,
$$

  e si riconosce la f.g.m. di una distribuzione $\mathcal{N}(a + b\mu, b^2 \sigma^2)$, per cui

$$
Y \sim \mathcal{N}(a + b\mu, b^2 \sigma^2)\,.
$$

<!-- ===== PAGINA 65 ===== -->

<!-- Pagina 65 -->

# Applicazioni notevoli (continua)

* Un'altra applicazione notevole è quella per ottenere la distribuzione di una combinazione lineare di v.c. normali indipendenti.
* Anche il teorema del limite centrale si dimostra utilizzando la f.g.m.: se $X_1, \dots, X_n$ sono i.i.d. con $E(X_i) = \mu$ e $V(X_i) = \sigma^2$, si può verificare che la f.g.m. della v.c.

$$
Z_n = \frac{\overline{X} - \mu}{\sqrt{\frac{\sigma^2}{n}}}
$$

tende alla f.g.m. di una $\mathcal{N}(0, 1)$ per $n \to \infty$.

* Un altro risultato è che se $X \sim \mathcal{N}(\mu, \sigma^2)$, allora

$$
m_X(1) = E\left(e^X\right) = e^{\mu + \frac{1}{2}\sigma^2}
$$

è la media di $Y = e^X$ con distribuzione $\text{lognormale}(\mu, \sigma^2)$.

<!-- ===== PAGINA 66 ===== -->

<!-- Pagina 66 -->

Introduzione all'inferenza statistica:
campionamento e distribuzioni campionarie

<!-- ===== PAGINA 67 ===== -->

<!-- Pagina 67 -->

# Inferenza Statistica

* Il punto di partenza di una indagine statistica è costituito da un insieme (**popolazione di riferimento**), che costituisce l'ambito di interesse;
* gli elementi di questo insieme (persone, componenti elettronici, titoli azionari, $\dots$) vengono indicati come **unità statistiche**;
* sono disponibili dei **dati**, ovvero delle misurazioni/rilevazioni di certe caratteristiche di interesse, ottenuti per una parte delle unità statistiche (il **campione**, da cui *indagini campionarie*);
* una descrizione delle caratteristiche del campione è in genere ottenuta mediante tecniche di **statistica descrittiva**;
* l'**inferenza statistica** utilizza i dati del campione per fare delle affermazioni sulle caratteristiche di tutta la popolazione.

---
a.a 2024/2025 — R. Bellio \hfill 2 / 28

<!-- ===== PAGINA 68 ===== -->

<!-- Pagina 68 -->

Lo schema qui sotto cerca di esemplificare la situazione. Le variabili di interesse sono rilevate solamente sulle unità statistiche che fanno parte del campione.

Nonostante le informazioni sulla popolazione siano incomplete, in un problema di inferenza si è però ambiziosi: con le informazioni rilevate sul solo campione l'obiettivo è arrivare a conclusioni su tutta la popolazione!

> **[Nota Grafico: Un diagramma che rappresenta una grande area irregolare etichettata come "popolazione", contenente vari punti segnati con la lettera "x" che indicano le "unità statistica". All'interno della popolazione è tracciata un'area tratteggiata più piccola etichettata come "campione", anch'essa contenente alcuni punti "x".]**

---

*a.a 2024/2025 — R. Bellio*  
*3 / 28*

<!-- ===== PAGINA 69 ===== -->

<!-- Pagina 69 -->

# Motivazione per le indagini campionarie

* **tempo e/o costo**

* **la popolazione di interesse può essere infinita e virtuale**

* **la rilevazione "distrugge" le unità statistiche** e quindi, dopo una rilevazione esaustiva, la popolazione di partenza non interessa più perché non esiste più!

* **precisione dei risultati**: a volte rilevazioni campionarie (incomplete) portano a risultati più precisi di rilevazioni esaustive.

<!-- ===== PAGINA 70 ===== -->

<!-- Pagina 70 -->

# Relazione tra popolazione e campione

* Supponiamo che la popolazione di riferimento siano i pezzi prodotti da svariati macchinari in un certo periodo di tempo, che sono presenti nel magazzino di una ditta . . .
* . . . e che si sia interessati a conoscere il loro peso medio ma, per far presto, si voglia pesare solamente 10 pezzi.
* Il primo problema diventa come scegliere i dieci pezzi da misurare; due possibilità veloci sono:

  A) scegliere **completamente a caso** 10 dei pezzi presenti, e misurare il loro peso;
  
  B) scegliere 10 pezzi a caso tra quelli più "semplici" da prendere (ad esempio, considerando un gruppo di 10 pezzi posti vicino all'entrata del magazzino).

<!-- ===== PAGINA 71 ===== -->

<!-- Pagina 71 -->

- In ambedue i casi, alla fine si ottengono 10 numeri (le 10 misurazioni del peso). Però per stimare il peso medio di tutti i pezzi presenti non è possibile utilizzare questi numeri nella stessa maniera nei due casi A) e B).

  - Nel primo caso posso pensare di stimare il peso medio utilizzando la media aritmetica delle 10 misurazioni fatte. Se non si è stati particolarmente sfortunati, i pezzi provengono da macchinari diversi ed è plausibile che la media delle dieci misure "cada vicino" al peso medio di tutti.

  - Nel secondo caso però occorre cautela: potremmo aver scelto pezzi prodotti tutti da un solo macchinario che produce pezzi con peso medio leggermente più basso, ed ottenere così un valore troppo basso.

Quello che cambia nei due casi è la **relazione tra la popolazione e il campione**.

<!-- ===== PAGINA 72 ===== -->

<!-- Pagina 72 -->

# Campione casuale semplice

L'esempio descrive la differenza tra un **campione casuale semplice**, che è **rappresentativo** della popolazione, e un **campione di convenienza**, che non lo è. Anche se è abbastanza intuitivo che il secondo non sia molto affidabile, purtroppo è spesso utilizzato nella pratica.

Un campione casuale semplice (c.c.s.) è un metodo per selezionare unità da una popolazione in maniera tale che ogni unità abbia la stessa possibilità di far parte del campione.

* Per ottenere un c.c.s. occorre **scegliere le unità totalmente a caso**.
* La scelta delle unità può avvenire con reinserimento oppure in blocco;
* per popolazioni infinite (o molto numerose), campionare con reinserimento o in blocco non porta a differenze sostanziali.

D'ora in poi si assumerà sempre di disporre di un c.c.s., estratto con reinserimento (esistono però schemi più sofisticati).

---
*(a.a. 2024/2025 — R. Bellio)* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *7 / 28*

<!-- ===== PAGINA 73 ===== -->

<!-- Pagina 73 -->

# L'indagine campionaria comporta sempre un errore

Per rendere utili le affermazioni fatte riguardo la popolazione è necessario cercare di quantificare il margine d'errore.

**Esempio.** Supponiamo di sperimentare un nuovo farmaco su $20$ pazienti e che solo uno di questi $20$ pazienti mostri effetti secondari indesiderati. Sembra naturale allora stimare la probabilità che il farmaco induca effetti tossici rilevanti come pari al $5\%$.

In questo caso la popolazione di riferimento è data da tutti i pazienti a cui potremmo pensare di somministrare il farmaco sotto analisi. È una popolazione virtuale e teoricamente infinita.

È chiaro che non è possibile affermare che la percentuale di tutti i possibili pazienti che potrebbero presentare problemi di tossicità sia esattamente uguale al $5\%$: è importante allora chiedersi di quanto potrebbe essere differente (ovvero quale sia **l'entità dell'errore**).

---

a.a 2024/2025 — R. Bellio \hfill 8 / 28

<!-- ===== PAGINA 74 ===== -->

<!-- Pagina 74 -->

# Inferenza statistica e Probabilità

L'idea alla base dell'inferenza statistica si concretizza nel descrivere la relazione tra la popolazione e il campione utilizzando il calcolo delle probabilità.

Nella sostanza, si interpretano i risultati sperimentali (ovvero i dati disponibili) come uno dei tanti risultati che un meccanismo probabilistico (un esperimento casuale) poteva fornire.

Una conseguenza importante è che è possibile utilizzare in maniera naturale il calcolo delle probabilità per quantificare l'errore campionario.

---

*(a.a 2024/2025 — R. Bellio)* \hfill 9 / 28

<!-- ===== PAGINA 75 ===== -->

<!-- Pagina 75 -->

# Ipotesi fondamentale per l'inferenza statistica

L'ipotesi fondamentale nell'inferenza statistica è che i dati campionari osservati, denotati anche con

$$
y = (y_1, \dots, y_n),
$$

siano la **realizzazione di $n$ variabili casuali** $Y_1, \dots, Y_n$.

Questo tiene conto del fatto che abbiamo estratto uno tra i molti possibili campioni, ovvero della presenza di **variabilità campionaria**. (L'ipotesi non sarebbe necessaria se potessimo osservare tutta la popolazione!)

Nel caso di un campione casuale semplice, le $n$ v.c. che si suppone abbiano generato i dati sono **variabili casuali indipendenti e identicamente distribuite (i.i.d.)**

<!-- ===== PAGINA 76 ===== -->

<!-- Pagina 76 -->

# Inferenza statistica parametrica

La distribuzione assunta per le singole variabili dipende dalla natura dei dati. Ad esempio, per dati binari sarà naturale ipotizzare $Y_i \sim \text{Bernoulli}(p)$, per misurazioni $Y_i \sim \mathcal{N}(\mu, \sigma^2)$, per conteggi $Y_i \sim \mathcal{P}(\lambda)$, per tempi di guasto $Y_i \sim \mathcal{G}a(\alpha, 1/\beta)$ (o Weibull), etc.

In ogni caso, la distribuzione assunta per le v.c. del campione dipenderà da ignote costanti dette **parametri**, vale a dire le quantità $p, \mu, \sigma^2, \alpha, \beta \dots$

I parametri entrano nella definizione della distribuzione delle variabili del campione $Y_1, \ldots, Y_n$. Nell'**inferenza statistica parametrica** si assume che la distribuzione delle v.c. del campione sia nota a meno dei valori dei parametri, che corrispondono tipicamente agli aspetti di interesse dell'analisi.

<!-- ===== PAGINA 77 ===== -->

<!-- Pagina 77 -->

# Modello statistico parametrico

Le assunzioni viste vanno a definire un **modello statistico parametrico** per i dati del campione.

Riassumendo, l'idea di base è che i dati siano stati generati dalle v.c. $Y_1, \dots, Y_n$, dove:

1. le variabili $Y_i$ sono indipendenti;
2. tutte le $Y_i$ hanno la stessa distribuzione di probabilità;
3. tale distribuzione è nota a meno dei valori di uno o più parametri, indicati genericamente come $\theta = (\theta_1, \dots, \theta_d)$, $d \ge 1$.

Scopo dell'inferenza statistica è utilizzare i dati del campione per ottenere informazioni su $\theta$, i cui elementi sono valori di un certo insieme $\Theta$ (**spazio parametrico**).

---

a.a 2024/2025 — R. Bellio \hfill 12 / 28

<!-- ===== PAGINA 78 ===== -->

<!-- Pagina 78 -->

# Modello statistico parametrico: alcune osservazioni

* I tre punti citati rappresentano delle *assunzioni*, che non è detto siano necessariamente soddisfatte nella pratica.
* In ogni caso, tali ipotesi possono essere considerate al più una descrizione **semplice** ed **operativamente utile** di una realtà complessa, quindi ci possiamo accontentare di una validità almeno **approssimata**.
* Esistono comunque metodi per trattare dati con una certa struttura di dipendenza (come le serie storiche), o per prescindere dalla conoscenza della forma della distribuzione (i **metodi non parametrici**). Essi comunque sono un'estensione dei metodi della statistica parametrica.

<!-- ===== PAGINA 79 ===== -->

<!-- Pagina 79 -->

# Statistiche e distribuzioni campionarie

Si chiama **statistica (campionaria)** ogni funzione dei dati, che viene usata per sintetizzare opportunamente il campione

$$
T = t(Y_1, \dots, Y_n) \, .
$$

Sono esempi di statistiche gli indici utilizzati nella statistica descrittiva

$$
\overline{Y}, S^2 \text{, la mediana campionaria, } \dots \, ,
$$

e occorre sempre distinguere tra la v.c. che rappresenta la statistica e il valore che tale statistica assume in un particolare campione osservato.

Tipicamente, è di interesse determinare la distribuzione di alcune statistiche di interesse, ovvero la loro **distribuzione campionaria**. A tal fine, si utilizzano i metodi probabilistici sviluppati per le funzioni di $n$ v.c. indipendenti.

<!-- ===== PAGINA 80 ===== -->

<!-- Pagina 80 -->

# Distribuzioni campionarie

Vedremo in sintesi alcuni risultati per variabili casuali indipendenti (con molti richiami a risultati visti in dettaglio in lezioni passate), e in particolare:

* A) Risultati per variabili qualsiasi.
* B) Risultati per variabili bernoulliane.
* C) Risultati per variabili Poisson.
* D) Risultati per variabili normali.

---
*a.a 2024/2025 — R. Bellio* \hfill *15 / 28*

<!-- ===== PAGINA 81 ===== -->

<!-- Pagina 81 -->

# A) Richiami sulle somme di variabili casuali

* $Y_1, \ldots, Y_n$ v.c. con $E(Y_1) = \mu_1, \ldots, E(Y_n) = \mu_n$
  
$$
\Rightarrow E(Y_1 + \ldots + Y_n) = \mu_1 + \ldots + \mu_n \,.
$$

* $Y_1, \ldots, Y_n$ v.c. **indipendenti** con $V(Y_1) = \sigma_1^2, \ldots, V(Y_n) = \sigma_n^2$
  
$$
\Rightarrow V(Y_1 + \ldots + Y_n) = \sigma_1^2 + \ldots + \sigma_n^2 \,.
$$

<!-- ===== PAGINA 82 ===== -->

<!-- Pagina 82 -->

# A) Richiami sulle somme di variabili casuali

Una conseguenza importante dei risultati appena visti riguarda la **variabile casuale media campionaria**

$$
\overline{Y} = \frac{1}{n} \sum_{i=1}^{n} Y_i
$$

- Se $Y_1, \dots, Y_n$ sono v.c. indipendenti con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, allora

$$
E(\overline{Y}) = \sum_{i=1}^{n} \frac{E(Y_i)}{n} = n \frac{\mu}{n} = \mu \text{,}
$$

$$
V(\overline{Y}) = \sum_{i=1}^{n} \frac{V(Y_i)}{n^2} = n \frac{\sigma^2}{n^2} = \frac{\sigma^2}{n} \text{.}
$$

<!-- ===== PAGINA 83 ===== -->

<!-- Pagina 83 -->

# A) La v.c. varianza campionaria

Nel caso di variabili i.i.d., con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, ci sono dei risultati anche per **variabile casuale varianza campionaria**

$$
S^2 = \frac{1}{n-1} \sum_{i=1}^n (Y_i - \overline{Y})^2
$$

- Se $Y_1, \dots, Y_n$ sono v.c. indipendenti con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, allora

$$
E(S^2) = \sigma^2
$$

$$
V(S^2) = (\sigma^2)^2 \left( \frac{2}{n-1} + \frac{\kappa}{n} \right)\text{,}
$$

con $\kappa$ costante che dipende dalla distribuzione ($0$ per $Y_i$ normali, ma non in generale).

<!-- ===== PAGINA 84 ===== -->

<!-- Pagina 84 -->

# A) Teorema del limite centrale

**Teorema** Sia $Y_1, Y_2, \dots$ una successione di v.c. indipendenti, ciascuna con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$. Allora, posto $Z_n = \sqrt{n}(\overline{Y} - \mu)/\sigma$, per ogni $z$

$$
\lim_{n \to \infty} P(Z_n \le z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-t^2/2} dt = \Phi(z) \, .
$$

In simboli il teorema del limite centrale (t.l.c.) si denota scrivendo

$$
Z_n = \sqrt{n}\frac{(\overline{Y} - \mu)}{\sigma} \xrightarrow{\mathcal{D}} \mathcal{N}(0, 1) \, ,
$$

dove $\xrightarrow{\mathcal{D}}$ si legge "converge in distribuzione".

Una lettura **pratica** del teorema del limite centrale è la seguente:

$$
\overline{Y} \stackrel{a}{\sim} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right) \, ,
$$

dove $\stackrel{a}{\sim}$ significa "distribuita approssimativamente".

<!-- ===== PAGINA 85 ===== -->

<!-- Pagina 85 -->

# A) Teorema del limite centrale: utilizzo

Il t.l.c. permette di approssimare la distribuzione di $\overline{Y}$, o, in maniera equivalente, della somma di $n$ v.c. i.i.d.

$$
\sum_{i=1}^{n} Y_i \stackrel{a}{\sim} \mathcal{N}(n\mu, n\sigma^2) \ .
$$

Si tratta di un risultato molto utile, del tipo chiamato **per grandi campioni**, nel senso che l'approssimazione è migliore per dimensioni campionarie elevate. Più precisamente, *quanto* deve essere grande $n$ dipende dalla distribuzione della popolazione:

* se il campione proviene da una distribuzione quasi simmetrica, l'approssimazione è buona già per piccoli valori di $n$;
* se la distribuzione è molto asimmetrica, è necessario un valore di $n$ abbastanza grande;
* per la maggior parte delle distribuzioni, un campione di numerosità 30 (o più) è sufficientemente elevato affinché l'approssimazione normale sia adeguata.

<!-- ===== PAGINA 86 ===== -->

<!-- Pagina 86 -->

# B) Risultati per variabili bernoulliane

Se consideriamo $n$ v.c. bernoulliane $Y_i \sim \text{Bernoulli}(p)$, $i = 1, \dots, n$, indipendenti, si ottiene facilmente che

$$
\sum_{i=1}^{n} Y_i \sim Bi(n, p) \,,
$$

Per $n$ elevato è più semplice utilizzare il t.l.c., che permette di **approssimare la binomiale con la normale**.

Al crescere di $n$, la distribuzione di una v.c. binomiale di parametri $n$ e $p$ si "avvicina" sempre di più a quella di una normale con parametri $\mu = np$ e $\sigma^2 = np(1-p)$.

L'approssimazione è ritenuta buona se $np > 5$ e $n(1-p) > 5$ (eventualmente utilizzando **correzioni di continuità** ($\pm 0.5$), che migliorano l'approssimazione normale per v.c. discrete).

<!-- ===== PAGINA 87 ===== -->

<!-- Pagina 87 -->

> **[Nota Grafico: Quattro grafici di distribuzioni di probabilità binomiali $Bin(n, p)$ con $p=0.2$ per valori crescenti di $n$ ($n=10, 20, 40, 80$), ciascuno accompagnato da una curva continua che approssima la distribuzione discreta.]**

> **[Nota Grafico: In alto a sinistra: $n=10, p=0.2$ sull'asse delle $x$ valori di $k$ da $0$ a $10$, asse delle $y$ (etichettato come "fd") da $0.00$ a $0.30$.]**

> **[Nota Grafico: In alto a destra: $n=20, p=0.2$ sull'asse delle $x$ valori di $k$ da $0$ a $20$, asse delle $y$ (etichettato come "fd") da $0.00$ a $0.20$.]**

> **[Nota Grafico: In basso a sinistra: $n=40, p=0.2$ sull'asse delle $x$ valori di $k$ da $0$ a $40$, asse delle $y$ (etichettato come "fd") da $0.00$ a $0.15$.]**

> **[Nota Grafico: In basso a destra: $n=80, p=0.2$ sull'asse delle $x$ valori di $k$ da $0$ a $80$, asse delle $y$ (etichettato come "fd") da $0.00$ a $0.08$.]**

---

a.a 2024/2025 — R. Bellio \hfill 22 / 28

<!-- ===== PAGINA 88 ===== -->

<!-- Pagina 88 -->

## C) Risultati per variabili Poisson

Se $Y_i \sim \mathcal{P}(\lambda_i)$, $i = 1, \dots, n$, indipendenti, allora

$$
\sum_{i=1}^n Y_i \sim \mathcal{P}\left(\sum_{i=1}^n \lambda_i\right) \text{.}
$$

In particolare, per v.c. i.i.d. (dove $\lambda_i = \lambda$) si ottiene $\sum_{i=1}^n Y_i \sim \mathcal{P}(n \lambda)$. Anche in questo caso, tuttavia, il t.l.c. è spesso utilizzato, ovvero

$$
\sum_{i=1}^n Y_i \stackrel{a}{\sim} \mathcal{N}(n\lambda, n\lambda) \text{.}
$$

L'approssimazione è ritenuta buona se $n\lambda > 10$.

<!-- ===== PAGINA 89 ===== -->

<!-- Pagina 89 -->

## D) Risultati per variabili normali

Per il caso $Y_i \sim \mathcal{N}(\mu, \sigma^2)$, $i = 1, \dots, n$, indipendenti, esistono diversi risultati.

Come caso particolare della proprietà che combinazioni lineari di normali indipendenti sono ancora normali, si ottiene

$$
\overline{Y} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right),
$$

$$
\sum_{i=1}^n Y_i \sim \mathcal{N}(n\mu, n\sigma^2),
$$

senza alcuna approssimazione!

Altri risultati richiedono preliminarmente la definizione di due distribuzioni collegate alla normale, ovvero la **distribuzione chi-quadrato** e la **distribuzione $t$ di Student**.

<!-- ===== PAGINA 90 ===== -->

<!-- Pagina 90 -->

# La distribuzione chi-quadrato

La somma di $n$ v.c. normali standard indipendenti elevate al quadrato ha distribuzione chi-quadrato con $n$ gradi di libertà, in simboli $\chi_n^2$. Ovvero, se $Z_i \sim \mathcal{N}(0, 1)$, $i = 1, \dots, n$, indipendenti,

$$
Y = \sum_{i=1}^{n} Z_i^2 \sim \chi_n^2
$$

La distribuzione è un caso particolare di distribuzione Gamma, con $\alpha = n/2$ e $\beta = 2$, e allora si trova $E(Y) = n$ e $V(Y) = 2n$.

## Funzione di densità

> **[Nota Grafico: Un grafico cartesiano che mostra le funzioni di densità di probabilità per la distribuzione chi-quadrato con tre differenti gradi di libertà ($n = 5$, $n = 10$, $n = 20$). Sull'asse delle ascisse sono riportati i valori di $y$ da $0$ a $50$, mentre sull'asse delle ordinate compaiono i valori di densità $f(y)$ da $0.00$ a $0.15$. La curva continua rappresenta $n=5$, la curva tratteggiata rappresenta $n=10$, e la curva punteggiata rappresenta $n=20$.]**

---

a.a 2024/2025 — R. Bellio \hfill 25 / 28

