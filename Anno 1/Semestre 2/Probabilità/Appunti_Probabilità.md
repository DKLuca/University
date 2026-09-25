

<!-- ===== PAGINA 1 ===== -->

<!-- Pagina 1 -->

### (IIII) VALORE ATTESO (1)

**Def** $X$ v.c. : MEDIA o VALORE ATTESO di $X$ è (o SPERANZA MATEMATICA)

$$\mu_X = E(X) = \begin{cases} \sum_{x} x \, p_X(x) & \text{CASO DISCRETO} \\ \int_{-\infty}^{\infty} x \, f_X(x) \, dx & \text{CASO CONTINUO} \end{cases}$$

* **Nota**: similarità con $\bar{x}$ della STAT. DESCRITTIVA

---

### ES 4.2

Commesso viaggiatore, 2 appuntamenti (INDIP.):
* 1° appuntamento: guadagno $1000 \text{ \$}$ prob. $70\%$
* 2° appuntamento: guadagno $1500 \text{ \$}$ prob. $40\%$

$$X = \text{guadagno, v.c.}$$

| $x$ | $p_X(x)$ |
| :--- | :--- |
| $0$ | $0.18$ |
| $1000$ | $0.42$ |
| $1500$ | $0.12$ |
| $2500$ | $0.28$ |
| | **$1$** |

$$E(X) = 1300 \text{ \$}$$

$$\downarrow$$

$$\text{GUADAGNO ATTESO}$$



<!-- ===== PAGINA 2 ===== -->

<!-- Pagina 2 -->

# ES 4.3 <span style="float: right; border: 1px solid red; border-radius: 50%; padding: 2px 8px; color: red;">2</span>

$X = \text{tempo vita dispositivo}$

$$f_X(x) = \begin{cases} \frac{20000}{x^3}, & x > 100 \\ 0, & \text{altrove} \end{cases}$$

$$\left( \int_{100}^{\infty} \frac{20000}{x^3} \, dx = 20000 \cdot \left(-\frac{1}{2}\right) \left. \left(x^{-2}\right) \right|_{100}^{\infty} = 1 \right)$$

$$E(X) = \int_{100}^{\infty} x \frac{20000}{x^3} \, dx = 200 \text{ ore}, \quad \text{DURATA MEDIA}$$

---

### PROPOSIZIONE

$$E[g(X)] = \begin{cases} \sum_{x} g(x) P_X(x) & \text{CASO DISCR.} \\ \int_{-\infty}^{\infty} g(x) f_X(x) \, dx & \text{CASO CONT.} \end{cases}$$

**Nota:** che $Y = g(X)$ sia V.C. è immediato dalla definizione di V.C.; il risultato ci permette di evitare di dover calcolare la distribuzione di $Y$ per calcolare $E(Y)$. Deriva dalle proprietà di sommatorie e integrali.



<!-- ===== PAGINA 3 ===== -->

<!-- Pagina 3 -->

(3)

* Si estende a funzioni di $2$ (o più) v.c.:

$$E\left[ g(X,Y) \right] = \begin{cases} \sum_{x} \sum_{y} g(x,y) p_{XY}(x,y) & \text{CASO DISCRETO} \\ \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x,y) f_{XY}(x,y) dx dy & \text{CASO CONTINUO} \end{cases}$$

Il caso speciale $g(X,Y) = X$ o $g(X,Y) = Y$ sono immediati:

$$E(X) = \sum_{x} \sum_{y} x \, p_{XY}(x,y) = \sum_{x} x \underbrace{\sum_{y} p_{XY}(x,y)}_{p_X(x)}$$
$$\uparrow$$
$$\text{CASO DISCRETO (PER ESEMPIO)}$$

---

### ESERCIZIO 4.3

$C = \text{costo per giocare}$  
$Y = \text{vincita netta}$

* vinco $3 \text{ \$}$ con Jack o Regina
* vinco $5 \text{ \$}$ con Asso o Re

| $y$ | $p_Y(y)$ |
| :---: | :---: |
| $0 - C$ | $36/52$ |
| $3 - C$ | $8/52$ |
| $5 - C$ | $8/52$ |
| | **1** |

<br>

$C$ per gioco EQUO?  
$$E(Y) = 0$$



<!-- ===== PAGINA 4 ===== -->

<!-- Pagina 4 -->

$$E(Y) = (0 - c) \frac{36}{52} + (3 - c) \frac{8}{52} + (5 - c) \frac{8}{52}$$
*(Nota: sopra il termine $(5-c)$ è presente un "4" cerchiato in rosso)*

$$= \frac{16}{13} - c \implies c = \frac{16}{13} = 1.23 \text{ \$}$$

---

### ESER. 4.5

Rimborso max $200\,000 \text{ \$}$ per assicurazione aereo

$$P(\text{perdita totale}) = 0.002$$
$$P(\text{perdita } 50\%) = 0.01$$
$$P(\text{perdita } 25\%) = 0.1$$

Premio per profitto medio $500 \text{ \$}$?

$$X = \text{Rimborso}$$

| $x$ | $p_X(x)$ |
| :---: | :---: |
| $200\,000$ | $0.002$ |
| $100\,000$ | $0.01$ |
| $50\,000$ | $0.1$ |
| $0$ | $0.888$ |
| | **$1$** |

$$E(X) = 6400 \text{ \$}$$

$$\text{premio} = 6400 \text{ \$} + 500 \text{ \$}$$
$$\Downarrow$$
$$6900 \text{ \$}$$



<!-- ===== PAGINA 5 ===== -->

<!-- Pagina 5 -->

*(Pagina 5)*

# ES 4.12

| $Y \setminus X$ | 2 | 4 | $p_Y(y)$ |
| :---: | :---: | :---: | :---: |
| **1** | 0.10 | 0.15 | 0.25 |
| **3** | 0.20 | 0.30 | 0.50 |
| **5** | 0.10 | 0.15 | 0.25 |
| **$p_X(x)$** | 0.40 | 0.60 | |

$$1. \quad E(X Y^2) = \sum_x \sum_y x y^2 p_{XY}(x,y) = 35.2$$

$$2. \quad \mu_X = 2 (0.40) + 4 (0.60) = 3.2$$
$$\mu_Y = 1 (0.25) + 3 (0.50) + 5 (0.25) = 3.0$$

---

# ES 4.14

$$f_X(x) = \begin{cases} \frac{1}{2000} e^{-\frac{x}{2000}} & x > 0 \\ 0 & x \le 0 \end{cases}$$

*(DENSITÀ ESPONENZIALE)*

$$E(X) = \frac{1}{2000} \int_{0}^{\infty} x e^{-x/2000} \, dx$$

$$\text{PONGO} \quad z = \frac{x}{2000} \implies \begin{aligned} x &= z \cdot 2000 \\ dx &= dz \cdot 2000 \end{aligned}$$

$$= 2000 \int_{0}^{\infty} z e^{-z} \, dz = 2000 \cdot 1$$

$$\int_{0}^{\infty} z e^{-z} \, dz \underset{\text{PER PARTI}}{=} \left[ \left(-e^{-z}\right) z \right]_{0}^{\infty} + \int_{0}^{\infty} e^{-z} \, dz = 1$$
*(Nota: il termine $\left[ \left(-e^{-z}\right) z \right]_{0}^{\infty}$ tende a $0$)*



<!-- ===== PAGINA 6 ===== -->

<!-- Pagina 6 -->

# III) VARIANZA E COVARIANZA <span style="float: right;">1</span>

**Def** $V(X)$ è la VARIANZA di $X$ (o della sua distribuzione):

$$ \sigma^2_X = V(X) = E\left[(X-\mu_X)^2\right] = \begin{cases} \sum_{x} (x-\mu_X)^2 p_X(x) & \text{CASO DISCRETO} \\ \int_{-\infty}^{\infty} (x-\mu_X)^2 f_X(x) \, dx & \text{CASO CONTINUO} \end{cases} $$

$$\rightarrow \text{Misura la VARIABILITÀ di } X$$

* $\sigma_X = \sqrt{V(X)}$ è la DEVIAZIONE STANDARD di $X$
* Nota: FORMULA DI CALCOLO (analoga a quella vista nella statistica descrittiva)

$$ E\left[(X-\mu_X)^2\right] = E(X^2) - \mu_X^2 $$

**Prova**: (CASO CONTINUO, CASO DISCRETO È ANALOGO)

$$ V(X) = \int_{-\infty}^{\infty} \left(x^2 + \mu_X^2 - 2x\mu_X\right) f_X(x) \, dx $$

$$ = \int_{-\infty}^{\infty} x^2 f_X(x) \, dx + \mu_X^2 \underbrace{\int_{-\infty}^{\infty} f_X(x) \, dx}_{1} - 2\mu_X \underbrace{\int_{-\infty}^{\infty} x f_X(x) \, dx}_{\mu_X} $$



<!-- ===== PAGINA 7 ===== -->

<!-- Pagina 7 -->

*(2)*

• Nota: $V(X) = 0 \iff$ v.c. con DISTRIBUZIONE DEGENERE

| $x$ | $p_X(x)$ |
| :---: | :---: |
| $a$ | $1$ |

---

• $V[g(X)] = E\left\{ \left[ g(X) - \mu_{g(X)} \right]^2 \right\}$ 
*(Nota in rosso su $\mu_{g(X)}$: "è una costante")*

che si calcola come:

* **Caso discreto:**
$$\sum_{x} \left[ g(x) - \mu_{g(x)} \right]^2 p_X(x)$$

* **Caso continuo:**
$$\int_{-\infty}^{\infty} \left( g(x) - \mu_{g(x)} \right)^2 f_X(x) dx$$

> **[Nota]** è l'applicazione di un risultato visto per il valore atteso

---

## Def COVARIANZA TRA $X$ e $Y$

$$\sigma_{XY} = \text{cov}(X,Y) = E\left[ (X - \mu_X)(Y - \mu_Y) \right]$$

Misura il grado della RELAZIONE LINEARE tra $X$ e $Y$

---

### Prop

$$\text{cov}(X,Y) = E(X \cdot Y) - E(X)E(Y)$$



<!-- ===== PAGINA 8 ===== -->

<!-- Pagina 8 -->

<div style="text-align: right; color: red; font-size: 1.5em; font-weight: bold;">3</div>

Di nuovo, possiamo considerare il caso continuo o quello discreto, i passaggi sono gli stessi. Qui prendiamo il caso discreto

$$Cov(X,Y) = \sum_{x} \sum_{y} (x - \mu_X)(y - \mu_Y) p_{XY}(x,y)$$

$$= \sum_{x} \sum_{y} x y p_{XY}(x,y) - \mu_X \sum_{x} \sum_{y} y p_{XY}(x,y) - \mu_Y \sum_{x} x \sum_{y} p_{XY}(x,y) + \mu_X \cdot \mu_Y \sum_{x} \sum_{y} p_{XY}(x,y)$$

$$= \sum_{x} \sum_{y} x y p_{XY}(x,y) - 2\mu_X \cdot \mu_Y + \mu_X \cdot \mu_Y$$

---

### Def COEFFICIENTE DI CORRELAZIONE TRA $X$ e $Y$

$$\rho_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y} , \quad -1 \le \rho_{XY} \le 1$$

* se $Y = a + bX \implies \begin{cases} \rho_{XY} = 1 & \text{per } b > 0 \\ \rho_{XY} = -1 & \text{per } b < 0 \end{cases}$

Ha la stessa interpretazione di $\sigma_{XY}$, con il vantaggio di essere privo di unità di misura e standardizzato (tra $-1$ e $1$)



<!-- ===== PAGINA 9 ===== -->

<!-- Pagina 9 -->

# Esempio 4.13

<div style="text-align: right; font-size: 1.5em; font-weight: bold; color: red;">4</div>

### Tabella di distribuzione di probabilità congiunta

$Y$ (righe), $X$ (colonne):

| $P_{XY}(x,y)$ | $0$ | $1$ | $2$ | $P_Y(y)$ |
| :---: | :---: | :---: | :---: | :---: |
| **$0$** | $3/28$ | $9/28$ | $3/28$ | $15/28$ |
| **$1$** | $6/28$ | $6/28$ | $0$ | $12/28$ |
| **$2$** | $1/28$ | $0$ | $0$ | $1/28$ |
| **$P_X(x)$** | $10/28$ | $15/28$ | $3/28$ | $1$ |

---

### Calcoli

$$E(XY) = \sum_{x} \sum_{y} x y P_{XY}(x,y) = 1 \cdot 1 \cdot \frac{6}{28} = \frac{3}{14}$$

$$E(X) = 3/4 \qquad E(Y) = 1/2$$

$$\text{cov}(X,Y) = \frac{3}{14} - \frac{3}{4} \cdot \frac{1}{2} = -\frac{9}{56}$$

$$V(X) = \frac{45}{112} \qquad V(Y) = \frac{9}{28} \qquad \rho_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y} = -0.447$$



<!-- ===== PAGINA 10 ===== -->

<!-- Pagina 10 -->

(5)

# PROPOSIZIONE

Se $X$ e $Y$ sono v.c. INDIPENDENTI $\Rightarrow \rho_{XY} = 0$

## Prova

$$E(X \cdot Y) \underset{\text{CASO DISCRETO}}{=} \sum_{x} \sum_{y} x \cdot y \cdot p_{XY}(x, y)$$

$$= \left( \sum_{x} x \cdot p_X(x) \right) \left( \sum_{y} y \cdot p_Y(y) \right)$$

$$= E(X) E(Y) \Rightarrow Cov(X, Y) = 0$$

---

### NOTA:
Non vale il viceversa, come mostra l'esempio che segue

| $Y \backslash X$ | $-1$ | $0$ | $1$ |
| :---: | :---: | :---: | :---: |
| **$0$** | $0$ | $0.5$ | $0$ |
| **$1$** | $0.25$ | $0$ | $0.25$ |

$p_{XY}(x,y)$ per $X$ e $Y$ discrete

Si trova facilmente $\rho_{XY} = 0$, ma le due v.c. non sono indipendenti!

$$(\text{Infatti } Y = |X|)$$



<!-- ===== PAGINA 11 ===== -->

<!-- Pagina 11 -->

### III) COMBINAZIONE LINEARE DI V.C. ①

#### Risultati notevoli:

##### RIS 1
$$a, b \in \mathbb{R} \quad ; \quad E(aX+b) = a E(X) + b$$
$$X \text{ v.c.}$$

**Prova:** (per $X$, ad es., discreta)

$$E(aX+b) \overset{\text{da risultato visto}}{=} \sum_{x} (ax+b) p_X(x)$$
$$= a \sum_{x} x p_X(x) + b \sum_{x} p_X(x)$$
$$= a E(X) + b$$

---

##### RIS 2
Siano $h$ e $g$ due funzioni $\mathbb{R} \to \mathbb{R}$

$$E[g(X) + h(X)] = E[g(X)] + E[h(X)]$$

**Prova:** si lascia per esercizio (è analoga al caso precedente)



<!-- ===== PAGINA 12 ===== -->

<!-- Pagina 12 -->

<u>RIS 3</u> &emsp; $a, b \in \mathbb{R}$ &emsp; $X, Y$ v.c. &emsp;&emsp;&emsp;&emsp; **(2)**

$aX + bY$ è una COMBINAZIONE LINEARE delle due variabili con pesi $a$ e $b$

$$E(aX + bY) = a E(X) + b E(Y)$$

**Prova:** (caso discreto)

$$E(aX + bY) = \sum_{x} \sum_{y} (ax + by) p_{XY}(x,y)$$

$$= a \sum_{x} \sum_{y} x p_{XY}(x,y) \quad +$$

$$b \sum_{x} \sum_{y} y p_{XY}(x,y)$$

> **[Nota Grafica: Una linea diagonale collega il termine $(ax+by)$ della prima equazione al coefficiente $a$ della riga successiva. Una linea verticale a sinistra raggruppa i due addendi con coefficienti $a$ e $b$ per confluire nel risultato finale]**

$$= a E(X) + b E(Y)$$

utilizzando un risultato visto in precedenza



<!-- ===== PAGINA 13 ===== -->

<!-- Pagina 13 -->

---
title: Appunti di Probabilità - Pagina 3
---

<div style="text-align: right; font-size: 1.5em; font-weight: bold; border: 1px solid red; display: inline-block; padding: 2px 8px; border-radius: 50%; float: right;">3</div>
<div style="clear: both;"></div>

### RIS 4

$g, h$ funzioni $\mathbb{R}^2 \longrightarrow \mathbb{R}$

$$E\left[ g(X,Y) + h(X,Y) \right] = E\left[ g(X,Y) \right] + E\left[ h(X,Y) \right]$$

Prova: si lascia per esercizio

---

### RIS 5

$X_1, X_2, \dots, X_n$ v.c.  
$a_1, a_2, \dots, a_n \in \mathbb{R}$

$$Y = \sum_{i=1}^{n} a_i X_i$$

> **COMBINAZIONE LINEARE** delle $n$ v.c. con pesi $a_1, a_2, \dots, a_n$

$$E(Y) = \sum_{i=1}^{n} a_i E(X_i)$$

Prova: segue da RIS 3 per INDUZIONE

---

### RIS 6

$a, b \in \mathbb{R}$ , $X$ v.c.

$$V(aX + b) = a^2 V(X)$$



<!-- ===== PAGINA 14 ===== -->

<!-- Pagina 14 -->

```markdown
Prova: $V(\underbrace{aX+b}_{Y}) = E \left[ (Y - \mu_Y)^2 \right]$  ④

$$= E \left[ (aX + b - a\mu_X - b)^2 \right]$$

$$\stackrel{!}{=} E \left[ a^2(X - \mu_X)^2 \right] = a^2 V(X)$$

---

### RIS 7
$a, b \in \mathbb{R}$, $X, Y$ v.c.

$$V(aX + bY) = a^2 V(X) + b^2 V(Y) + 2ab \operatorname{cov}(X, Y)$$

**Prova:**
$$V(aX + bY) = E \left\{ \left[ (aX + bY) - (a\mu_X + b\mu_Y) \right]^2 \right\}$$

$$= E \left\{ \left[ a(X - \mu_X) + b(Y - \mu_Y) \right]^2 \right\}$$

$$= E \left\{ a^2(X - \mu_X)^2 + b^2(Y - \mu_Y)^2 + 2ab(X - \mu_X)(Y - \mu_Y) \right\} = \longrightarrow \text{applico RIS 5}$$

$$= a^2 E \left[ (X - \mu_X)^2 \right] + b^2 E \left[ (Y - \mu_Y)^2 \right] + 2ab \cdot E \left[ (X - \mu_X)(Y - \mu_Y) \right] \text{, ovvero il risultato}$$
```



<!-- ===== PAGINA 15 ===== -->

<!-- Pagina 15 -->

(5)

## RIS 8

Se $X$ e $Y$ sono INDIPENDENTI

$$V(a X + b Y) = a^2 V(X) + b^2 V(Y)$$

si estende a $n$ v.c. INDIPENDENTI

$$V\left( \sum_{i=1}^{n} a_i X_i \right) = \sum_{i=1}^{n} a_i^2 V(X_i)$$

---

### CASO NOTEVOLE di COMB. LINEARE

**Def** Date $X_1, \dots, X_n$ v.c.,

$$\overline{X} = \frac{1}{n} \sum_{i=1}^{n} X_i \quad \text{è la v.c. MEDIA CAMPIONARIA}$$

**Nota:** la notazione usata coincide, non a caso, con l'analoga definizione vista in statistica descrittiva. Eseguito l'esperimento, e osservati i valori $x_1, x_2, \dots, x_n$, allora posso calcolare

$$\overline{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$



<!-- ===== PAGINA 16 ===== -->

<!-- Pagina 16 -->

(6)

* Proprietà di $\overline{X}$: ci interessa soprattutto il caso di $n$ v.c. **i. i. d.** ovvero INDIPENDENTI e IDENTICAMENTE DISTRIBUITE.

Se la distribuzione è la stessa per tutte le v.c., allora hanno tutte la stessa media e varianza:

$$E(X_1) = E(X_2) = \dots = E(X_n) = \mu$$
$$V(X_1) = V(X_2) = \dots = V(X_n) = \sigma^2$$

si ha (da risultati precedenti)

$$E(\overline{X}) = \mu$$

$$V(\overline{X}) = \frac{\sigma^2}{n}$$



<!-- ===== PAGINA 17 ===== -->

<!-- Pagina 17 -->

(7)

## VALORE ATTESO CONDIZIONATO

* È la media della v.c. basata sulla distribuzione condizionata

$$E(Y|X=x) = \begin{cases} \sum_{y} y \, p_{Y|X}(y|x), & \text{CASO DISCRETO} \\ \\ \int_{-\infty}^{\infty} y \, f_{Y|X}(y|x) \, dy, & \begin{matrix} \text{CASO} \\ \text{CONTINUO} \end{matrix} \end{cases}$$

* Interpretazione: è una sintesi della distribuzione di $Y$ quando $X=x$

* Analogamente definiamo la VARIANZA CONDIZIONATA
$$V(Y|X=x)$$

* Nota: $E(Y|X=x)$ e $V(Y|X=x)$ dipendono dal valore di $x$!

  Se $X$ e $Y$ sono <u>indipendenti</u>
  $$E(Y|X=x) = E(Y) \quad \text{e} \quad V(Y|X=x) = V(Y)$$



<!-- ===== PAGINA 18 ===== -->

<!-- Pagina 18 -->

# III) DISTRIBUZIONI DI PROBABILITÀ NOTEVOLI (DISCRETE) ①

* Alcuni tipi di V.C. ricorrono spesso nella pratica $\Rightarrow$ MODELLI DI RIFERIMENTO
* Distribuzioni di probabilità DISCRETE o CONTINUE che dipendono da alcuni PARAMETRI $\vartheta = (\vartheta_1, \vartheta_2, \dots, \vartheta_p)$

$$p_X(x; \vartheta) \quad \text{caso discreto}$$
$$f_X(x; \vartheta) \quad \text{caso continuo}$$

---

## ① DISTRIBUZIONE di BERNOULLI

Esperimento con $2$ possibili risultati,

$$\begin{array}{ccc} \text{"SUCCESSO"} & \text{o} & \text{"INSUCCESSO"} \\ 1 & & 0 \end{array}$$

$$P(\text{SUCCESSO}) = p \qquad P(\text{INSUCCESSO}) = 1 - p$$

$$p, \quad 0 < p < 1 \quad \text{è il PARAMETRO}$$



<!-- ===== PAGINA 19 ===== -->

<!-- Pagina 19 -->

(2)

$$X = \begin{cases} 1 & \text{SUCCESSO} \\ 0 & \text{INSUCCESSO} \end{cases}$$

> **[Nota Grafico: Una freccia con la dicitura "su distribuzione" collega la definizione di $X$ alla tabella sottostante]**

| $x$ | $P_X(x; p)$ |
| :---: | :---: |
| $0$ | $1 - p$ |
| $1$ | $p$ |

$$\begin{aligned}
P(X=1) &= p \\
P(X=0) &= 1-p
\end{aligned}$$

---

$$E(X) = p$$

$$V(X) = p(1-p)$$

---

In forma compatta: 
$$p_X(x; p) = p^x (1-p)^{1-x}, \quad x = 0, 1$$

Notazione:
$$X \sim \text{Bernoulli}(p)$$

ES: LANCIO MONETA, $\text{SUCCESSO} \Rightarrow \text{esce testa}$
$$X \sim \text{Bernoulli}(0.5)$$



<!-- ===== PAGINA 20 ===== -->

<!-- Pagina 20 -->

# DISTRIBUZIONE BINOMIALE <span style="float: right;">③</span>

### Processo di Bernoulli:

1. Esperimento formato da $n$ PROVE RIPETUTE
2. ESITO binario ($\text{SUCC.} / \text{INSUCC.}$)
3. $P(\text{SUCCESSO}) = p$, costante nelle varie prove
4. Prove INDIPENDENTI

---

> **Nota:** Quando si hanno $n$ esperimenti indipendenti effettuati nelle stesse condizioni si parla di **CAMPIONE CASUALE**

---

$$X = \text{n}^\circ \text{ SUCCESSI nelle } n \text{ prove}$$

$$X \sim \text{Bi}(n, p) \qquad x = 0, 1, \dots, n$$
$$0 < p < 1$$

> **[Nota Grafico: Una freccia rossa punta dalla formula $X \sim \text{Bi}(n, p)$ a un riquadro rosso contenente la scritta "DISTRIBUZIONE BINOMIALE"]**

---

**ES:** Lancio $3$ volte un dado, $\text{successo} \Rightarrow \text{esce } 6$

$$X = \text{n}^\circ \text{ di } 6 \text{ nelle } 3 \text{ prove}$$
$$X \sim \text{Bi}(3, 1/6)$$



<!-- ===== PAGINA 21 ===== -->

<!-- Pagina 21 -->

(4)

otteniamo la distribuzione: defini-
per prima cosa gli eventi
$$A_i = \{ \text{Esce 6 alla } i-\text{esima prova} \}$$
$$i = 1, 2, 3$$
$$A_1, A_2, A_3 \quad \text{MUTUAMENTE INDIPENDENTI}$$

$$P(X=0) = P\left(A_1^c \cap A_2^c \cap A_3^c\right)$$
$$= P\left(A_1^c\right) P\left(A_2^c\right) P\left(A_3^c\right) = \left(\frac{5}{6}\right)^3$$

$$P(X=1) = P\left(A_1^c \cap A_2^c \cap A_3\right) + P\left(A_1^c \cap A_2 \cap A_3^c\right)$$
$$+ P\left(A_1 \cap A_2^c \cap A_3^c\right) = 3 \left(\frac{1}{6}\right)^1 \left(\frac{5}{6}\right)^2$$

$$P(X=2) = 3 \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^1$$

$$P(X=3) = \left(\frac{1}{6}\right)^3$$

In generale: per $X \sim B_i(n,p)$

$$\boxed{P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x=0, 1, \dots, n}$$



<!-- ===== PAGINA 22 ===== -->

<!-- Pagina 22 -->

(5)

* Il testo di Walpole et al. usa una simbologia particolare per $p_X(x; p)$, ovvero
$$b(x; n, p) = \binom{n}{x} p^x (1-p)^{n-x}$$

Proprietà:

i) Posto $q = 1-p$ si ha
$$\underbrace{(p+q)^n}_{1} = \sum_{x=0}^n \binom{n}{x} p^x (1-p)^{n-x} = 1$$
$$\llap{\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\llap{\llap{\llap{\llap{\llap{\llap{\llap{\llap{\llap{\llap{\llap{\llap{formula di Newton}}}}}}}}}}}}$$

a riprova che la distribuzione è ben definita.

ii) MEDIA e VARIANZA

$$Z_i = \begin{cases} 1 & \text{successo } i\text{-esima prova} \\ 0 & \text{insuccesso } \text{" } \quad \text{"} \end{cases}$$

$$Z_i \sim \text{Bernoull}(p) \quad i = 1, \dots, n$$

v.c. indipendenti



<!-- ===== PAGINA 23 ===== -->

<!-- Pagina 23 -->

(6)

$$X = Z_1 + Z_2 + \dots + Z_n$$

Dai risultati sulle combinazioni lineari:

$$E(X) = E\left(\sum_{i=1}^{n} Z_i\right) = \sum_{i=1}^{n} E(Z_i) = np$$

$$V(X) = V\left(\sum_{i=1}^{n} Z_i\right) = \sum_{i=1}^{n} V(Z_i) = np(1-p)$$

* Area di applicazione

$\rightarrow$ ESTRAZIONI CON REINSERIMENTO

* Controllo di qualità: PEZZO DIFETTOSO / NON DIFETTOSO
* Medicina: FARMACO FUNZIONA / NON FUNZIONA



<!-- ===== PAGINA 24 ===== -->

<!-- Pagina 24 -->

# DISTRIBUZIONE IPERGEOMETRICA

* Adatta a ESTRAZIONI SENZA REINSERIMENTO

* $n$ prove, selezione senza reinserimento da $N$ unità

* $K$ successi, $N-K$ insuccessi

$$X = n^\circ \text{ di successi nelle } n \text{ prove}$$

$$X \sim H(N, n, K) \quad \text{DISTRIBUZIONE IPERGEOMETRICA}$$

$$P(X=x) = \frac{\binom{K}{x} \binom{N-K}{n-x}}{\binom{N}{n}} = h(x; N, n, K)$$

$\downarrow$
METODO DEL CONTEGGIO

Supporto:

$$\begin{cases}
0 \le x \le n \\
n - (N-K) \le x \le K
\end{cases}$$

$\hookrightarrow \max(0, n - (N-K)) \le x \le \min(n, K)$



<!-- ===== PAGINA 25 ===== -->

<!-- Pagina 25 -->

- ES: 10 oggetti, 3 difettosi, 7 non difettosi

$$N = 10 \quad , \quad k = 7 \quad , \quad X = n^\circ \text{ di non difettosi}$$

Supporto: se $\begin{cases} n = 4 & 1 \le x \le 4 \\ n = 8 & 5 \le x \le 7 \\ n = 3 & 0 \le x \le 3 \end{cases}$

Nota: se $k \ge n \quad \text{e} \quad N-k \ge n \implies 0 \le x \le n$

- PROPOSIZIONE

$$E(X) = n \frac{k}{N} = n p \quad \text{se pongo } p = \frac{k}{N}$$

$$V(X) = n \frac{k}{N} \left(1 - \frac{k}{N}\right) \frac{N-n}{N-1}$$

$$= n \ p \ (1-p) \frac{N-n}{N-1}$$

Prova: (pura algebra, la prendiamo per buona)



<!-- ===== PAGINA 26 ===== -->

<!-- Pagina 26 -->

Confronto con la binomiale: (3)

- Se estraggo con reinserimento $X \sim Bi(n,p)$
- " " senza " " e $n \le 0.05 N$

$$H(N, n, K) \approx Bi\left(n, \frac{K}{N}\right)$$

Ma se $n$ è piccolo in confronto a $N$ posso agire come se le estrazioni avvengano con reinserimento!

- La distribuzione ipergeometrica si estende a più di 2 categorie, ma è poco usata.

- UTILIZZO DELLA DISTRIBUZIONE IPERGEOMETRICA NEL CAMPIONAMENTO PER ACCETTAZIONE

Esercizio 5.18

- Lotto $N = 50$, ne campiono $n = 5$ e accetto il lotto se al max 2 sono difettosi



<!-- ===== PAGINA 27 ===== -->

<!-- Pagina 27 -->

(4)

Proporzione di lotti con il $20\%$ che saranno accettati?

$$K = 10 \qquad X = n^\circ \text{ difettosi } n \ 5$$

$$X \sim H(50, 5, 10), \quad 0 \le x \le 5$$

$$P(X \le 2) = \sum_{x=0}^{2} \frac{\binom{10}{x}\binom{40}{5-x}}{\binom{50}{5}} = 0.9517$$

- Se uso $X \sim \text{Bi } (5, 0.2), \quad P(X \le 2) = 0.9421$

- Esercizio 3.6

$$N = 7 \qquad K = 2 \text{ difettosi} \qquad n = 3$$

$$X = n^\circ \text{ difettosi} \qquad X \sim H(7, 3, 2)$$

$$x = 0, 1, 2$$

| $x$ | $P_X(x)$ |
| :---: | :---: |
| 0 | $2/7$ |
| 1 | $4/7$ |
| 2 | $1/7$ |



<!-- ===== PAGINA 28 ===== -->

<!-- Pagina 28 -->

# LA DISTRIBUZIONE DI POISSON (1)

Problema: $X = n^\circ$ viaggiatori che transitano per una stazione in un giorno feriale qualsiasi

Assunzioni:
- $n^\circ$ potenziali viaggiatori $N$
- agiscono in maniera indipendente
- hanno tutti la stessa probabilità "di successo" (transito)

$\Rightarrow X \sim \text{Bi}(N, p)$

Definiamo $\lambda = N \cdot p$ tasso passaggio medio

$$P(X=x) = \binom{N}{x} p^x (1-p)^{N-x}$$

$$= \binom{N}{x} \left(\frac{\lambda}{N}\right)^x \left(1-\frac{\lambda}{N}\right)^{N-x}$$

Assumiamo che $\begin{cases} N \to \infty \\ p \to 0 \end{cases}$ e $\lambda \to \text{costante}$

e calcoliamo il limite di $P(X=x)$:



<!-- ===== PAGINA 29 ===== -->

<!-- Pagina 29 -->

$$ \lim_{N \to \infty} P(X = n) = \lim_{N \to \infty} \underbrace{\frac{N!}{(N-n)! n!} \cdot \frac{\lambda^n}{N^n}}_{\to 1} \cdot \underbrace{\left(1 - \frac{\lambda}{N}\right)^N}_{\to e^{-\lambda}} \underbrace{\left(1 - \frac{\lambda}{N}\right)^{-n}}_{\to 1} $$

ovvero

$$ \lim_{N \to \infty} P(X = n) = \frac{\lambda^n e^{-\lambda}}{n!} $$

$$ n = 0, 1, \dots $$

- Il risultato giustifica la seguente definizione:

<u>Def</u> $X$ v.c. di Poisson, con supporto $n = 0, 1, 2, \dots$

$$ \Big[ P(X = n) = e^{-\lambda} \frac{\lambda^n}{n!} $$

Commenti:
- È approssimazione della binomiale per $n$ elevato, $p$ piccolo e $\lambda = np$ costante
- Va bene per conteggi senza limite superiore



<!-- ===== PAGINA 30 ===== -->

<!-- Pagina 30 -->

### Proprietà:

$$\begin{cases} E(X) = \lambda \\ V(X) = \lambda \end{cases} \quad \begin{minipage}{0.4\textwidth}Segue da proprietà delle serie, ma anche dalla approssimazione binomiale\end{minipage}$$

---

## 1 PROCESSO DI POISSON (omogeneo)

1. ARRIVI indipendenti nel tempo o nello spazio
2. Non ci sono arrivi simultanei
3. $\lambda$ tasso di arrivi medio in una unità di tempo (è lo stesso per tutte le unità) [spazio]

$X = n^\circ$ arrivi in $t$ unità di tempo (spazio)

$$1 + 2 + 3 \implies X \sim \text{Poisson}(\lambda t)$$
$$\left(\text{o anche si indica } \mathcal{P}(\lambda t)\right)$$

* **ES:** Accessi sito web (in un intervallo di tempo)
$\lambda = 5$ accessi al minuto

$$P(17 \text{ accessi in } 3 \text{ minuti}) = e^{-15} \frac{15^{17}}{17!} = 0.0847$$



<!-- ===== PAGINA 31 ===== -->

<!-- Pagina 31 -->

Infatti: $X = n^{\circ} \text{ accessi in } 3 \text{ minuti}$

$$X \sim \mathcal{P}(\underbrace{1 \cdot 3}_{15})$$

---

Proprietà:

$X_1 \sim \mathcal{P}(\lambda_1) \text{ , } X_2 \sim \mathcal{P}(\lambda_2) \text{ indip.}$

$$X_1 + X_2 \sim \mathcal{P}(\lambda_1 + \lambda_2)$$

$(\text{Prova: si utilizza la FUNZIONE GENERATRICE DEI MOMENTI, che vedremo})$

ES: Viaggiatori in transito per stazione

$X_1 = n^{\circ} \text{ arrivi tip } 1 \text{ (pendolari lavoratori)}$

$X_2 = \text{ "} \text{ "} \text{ "} 2 \text{ ( "} \text{ studenti)}$

$X_3 = \text{ "} \text{ "} \text{ "} 3 \text{ (occasionali)}$

$\downarrow X_K = \text{ "} \text{ "} \text{ "} K \text{ (}\dots\text{)}$
<span style="color:red">VIAGGIATORI TOTALI</span>

$$X_T = X_1 + X_2 + \dots X_K \sim \mathcal{P}(\lambda_1 + \lambda_2 + \dots + \lambda_K)$$



<!-- ===== PAGINA 32 ===== -->

<!-- Pagina 32 -->

# DISTRIBUZIONE UNIFORME CONTINUA

* $X$ v.c. continua con $f$ di densità costante nell'intervallo $(a,b)$, con $a, b \in \mathbb{R}$

$$X \sim \mathcal{U}(a,b) \quad , \quad f_X(x; a, b) = \begin{cases} \frac{1}{b-a} &, a \le x \le b \\ 0 &, \text{altrove} \end{cases}$$

> **[Nota Grafico: Grafico cartesiano della funzione di densità $f_X(x; a, b)$. Sull'asse delle ordinate è segnato il valore $\frac{1}{b-a}$, sull'asse delle ascisse sono segnati i punti $a$ e $b$. La funzione è costante a livello $\frac{1}{b-a}$ per $x \in [a, b]$ e zero altrove.]**

$$E(X) = \frac{a+b}{2} \quad \text{per la simmetria}$$

$$V(X) = \frac{(b-a)^2}{12} \quad \text{calcoli semplici}$$

$$F_X(x; a, b) = \begin{cases} 0 &, x \le a \\ \frac{x-a}{b-a} &, a \le x \le b \\ 1 &, x \ge b \end{cases}$$



<!-- ===== PAGINA 33 ===== -->

<!-- Pagina 33 -->

## III DISTRIBUZIONE NORMALE 2

$$f_X(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \quad, x \in \mathbb{R}$$

$$X \sim N(\mu, \sigma^2)$$

$$n(x; \mu, \sigma) \quad (\text{Walpole et al.})$$

- È la più importante distribuzione continua, si trova in moltissimi fenomeni fisici, biologici e anche socio-economici.

- Il grafico della f. di densità è la famosa "campana di Gauss".

> **[Nota Grafico: Schizzo del grafico di una funzione di densità normale a forma di campana, simmetrica rispetto all'asse verticale tratteggiato passante per il punto $\mu$ sull'asse orizzontale]**

- Si trova $E(X) = \mu$ (per simmetria), mentre $V(X) = \sigma^2$ richiede l'integrazione per parti



<!-- ===== PAGINA 34 ===== -->

<!-- Pagina 34 -->

* Proprietà: per qualsiasi scelta di $\mu \in \mathbb{R}$ e $\sigma > 0$
(Prova: vedi $F_x$)

> **[Nota Grafico: Schizzo di una curva gaussiana (campana) simmetrica rispetto all'asse centrale $\mu$. Sull'asse orizzontale sono indicati i punti $\mu-3\sigma$, $\mu-2\sigma$, $\mu-\sigma$, $\mu$, $\mu+\sigma$, $\mu+2\sigma$, $\mu+3\sigma$ con linee tratteggiate verticali che salgono dalla base verso la curva.]**

$$P(\mu - \sigma \le X \le \mu + \sigma) \simeq 0.68$$

$$P(\mu - 2\sigma \le X \le \mu + 2\sigma) \simeq 0.95$$

$$P(\mu - 3\sigma \le X \le \mu + 3\sigma) \simeq 0.99$$

Ecco perché possiamo utilizzare la distribuzione anche per grandezze fisiche che hanno un campo di variazione limitato (p.es., lunghezze ecc.)

* STANDARDIZZAZIONE

Sia $X \sim N(\mu, \sigma^2)$, definiamo

$$Z = \frac{X - \mu}{\sigma} : \quad \text{si ha} \quad Z \sim N(0,1)$$



<!-- ===== PAGINA 35 ===== -->

<!-- Pagina 35 -->

- Il risultato è un caso speciale di un risultato più generale: se $a, b \in \mathbb{R}$
  $$a + bX \sim \mathcal{N}\left(a + b\mu, \, b^2\sigma^2\right)$$

Prova: si dimostra tramite la FUNZIONE GENERATRICE DEI MOMENTI, che vedremo ($f. \, g. \, m.$)

- Def $Z \sim \mathcal{N}(0,1)$ è la DISTRIBUZIONE NORMALE STANDARD (o STANDARDIZZATA)

Notazione:
$$f_Z(z; 0, 1) = \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}$$

$$F_Z(z; 0, 1) = \Phi(z) = \int_{-\infty}^{z} \phi(t) \, dt$$

↳ non ammette forma analitica: esistono però tabelle, le TAVOLE DELLA NORMALE



<!-- ===== PAGINA 36 ===== -->

<!-- Pagina 36 -->

Proprietà di $\Phi(z)$:

i) 
$$\Phi(-z) = 1 - \Phi(z)$$
per la simmetria di $\phi(z)$

ii) Utilizzo: sia $X \sim \mathcal{N}(\mu, \sigma^2)$

$$P(x_1 < X < x_2) = P\left(\frac{x_1-\mu}{\sigma} < \underbrace{\frac{X-\mu}{\sigma}}_{Z \sim \mathcal{N}(0,1)} < \frac{x_2-\mu}{\sigma}\right)$$

$$= P\left(\frac{x_1-\mu}{\sigma} < Z < \frac{x_2-\mu}{\sigma}\right)$$

$$= \Phi\left(\frac{x_2-\mu}{\sigma}\right) - \Phi\left(\frac{x_1-\mu}{\sigma}\right)$$

l'ultimo passaggio utilizza una proprietà vista della F.d. ripartizione nel caso continuo

Ovvero: la funzione $\Phi$ ci permette di calcolare prob. per $X$ v.c. normale qualsiasi.

Inoltre:
$$F_X(x; \mu, \sigma) = \Phi\left(\frac{x-\mu}{\sigma}\right)$$



<!-- ===== PAGINA 37 ===== -->

<!-- Pagina 37 -->

6

* PERCENTILI di $X \sim N(\mu, \sigma^2)$

$x_\alpha$: $F_X(x_\alpha; \mu, \sigma) = \alpha$, $0 < \alpha < 1$

$$\Phi\left(\frac{x_\alpha - \mu}{\sigma}\right) = \alpha$$

quindi 

$$\frac{x_\alpha - \mu}{\sigma} = z_\alpha$$
$$\uparrow$$
percentile di $N(0,1)$

$$x_\alpha = \mu + \sigma \ z_\alpha$$

* Si noti: $\Phi(z_\alpha) = \alpha$, $z_\alpha = \Phi^{-1}(\alpha)$
$$\uparrow$$
FUNZIONE QUANTILE

e per la simmetria di $\phi(z)$ attorno a $z=0$ si ottiene:

$$z_{1-\alpha} = -z_\alpha$$

* Percentili notevoli:
$z_{0.95} = 1.645$
$z_{0.975} = 1.96$
$z_{0.99} = 2.33$
$z_{0.995} = 2.58$



<!-- ===== PAGINA 38 ===== -->

<!-- Pagina 38 -->

ESEMPIO

$X = \text{durata certo tipo di batteria (ore)}$

$X \sim N(50, 25) \rightarrow \mu = 50, \sigma = 5$

$x_{0.05} = \sigma z_{0.05} + \mu = 50 + 5(-1.645)$
$$= 41.775 \text{ ore}$$

$x_{0.95} = \sigma z_{0.95} + \mu = 50 + 5(1.645)$
$$= 58.225 \text{ ore}$$

> **[Nota Grafico: Grafico di una distribuzione normale con media $\mu = 50$, punti critici a $41.775$ e $58.225$. Vengono evidenziate le aree di probabilità: $0.05$ nella coda di sinistra, $0.90$ nella parte centrale tratteggiata, e $0.05$ nella coda di destra.]**

ESEMPIO 6.5

$$X \sim N(300, 50^2)$$

$$P(X > 362) = P\left(Z > \frac{362 - 300}{50}\right)$$

$$Z \sim N(0,1) \quad = P(Z > 1.24)$$

$$= 1 - \Phi(1.24) = 0.1075$$



<!-- ===== PAGINA 39 ===== -->

<!-- Pagina 39 -->

# LA DISTRIBUZIONE NORMALE: COMPLEMENTI DI TEORIA

- Un risultato notevole:

## PROPOSIZIONE

Se $X_1, X_2, \dots, X_n$ v.c. INDIPENDENTI  
Con $X_i \sim N(\mu_i, \sigma_i^2)$, e $a_1, a_2, \dots, a_n \in \mathbb{R}$

$$Y = \sum_{i=1}^n a_i X_i \sim N\left(\sum_{i=1}^n a_i \mu_i, \sum_{i=1}^n a_i^2 \sigma_i^2\right)$$

*Prova:* si ottiene tramite la *f.g.m.* (che vedremo)

- CASO NOTEVOLE: $\mu_i = \mu$, $\sigma_i^2 = \sigma^2$, $a_i = \frac{1}{n} \quad \forall i$

$$\overline{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \quad \begin{array}{l} \text{v.c.} \\ \text{MEDIA} \\ \text{CAMPIONARIA} \end{array}$$

- È un risultato molto importante per la statistica inferenziale, come pure il risultato che segue



<!-- ===== PAGINA 40 ===== -->

<!-- Pagina 40 -->

1) TEOREMA DEL LIMITE CENTRALE (TLC)

$X_1, X_2, \dots, X_n$ $\boxed{\text{i.i.d.}}$

$E(X_i) = \mu$, $V(X_i) = \sigma^2$

sia $Z_n = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}}$

allora $\lim_{n \to \infty} F_{Z_n}(z) = \Phi(z), \quad \forall z \in \mathbb{R}$

(Prova: anche qui si usa la f.g.m.)

- Interpretazione operativa del risultato:
per $n$ elevato, $Z_n \stackrel{a}{\sim} N(0, 1)$

ovvero $\boxed{\overline{X} \stackrel{a}{\sim} N\left(\mu, \frac{\sigma^2}{n}\right)}$

- Si può esprimere per la somma:
$\sum_{i=1}^{n} X_i \stackrel{a}{\sim} N(n\mu, n\sigma^2)$



<!-- ===== PAGINA 41 ===== -->

<!-- Pagina 41 -->

Osservazioni: (3)

- vale per ogni distribuzione, l'approssimazione è migliore per distribuzioni SIMMETRICHE e CONTINUE
- Se $Xi \sim N(\mu, \sigma^2)$, il risultato è ESATTO (non occorre invocare il teorema)
- Per $n \ge 30$ generalmente si ottiene una buona approssimazione

II DUE CASI NOTEVOLI

- BINOMIALE $X \sim Bi(n, p)$

$X = \sum_{i=1}^{n} Zi \quad, \quad Zi \sim Bernaulli(p)$

Applicando il TLC:

$\frac{X}{n} \sim N\left(p, \frac{p(1-p)}{n}\right)$

APPROSSIMAZIONE NORMALE DELLA BINOMIALE

$$X \sim N(np, np(1-p))$$



<!-- ===== PAGINA 42 ===== -->

<!-- Pagina 42 -->

- L'approssimazione è ritenuta buona se

$$\begin{cases} np \ge 5 \\ n(1-p) \ge 5 \end{cases}$$

- Correzione di continuità (CC):

$$\begin{cases} P(X \le x) = \Phi\left(\frac{x + 0.5 - np}{\sqrt{np(1-p)}}\right) \\ P(X < x) = \Phi\left(\frac{x - 0.5 - np}{\sqrt{np(1-p)}}\right) \end{cases}$$

- POISSON $x_1, x_2, \dots, x_n$ iid, $x_i \sim \mathcal{P}(\lambda)$

$$\sum_{i=1}^{n} X_i \sim \mathcal{P}(n\lambda) \quad \text{ma anche}$$

$$\sum_{i=1}^{n} X_i \approx \mathcal{N}(n\lambda, n\lambda)$$

$\text{Quindi: se}$

$\text{\color{red}APPROSSIMAZIONE}$
$\text{\color{red}NORMALE \quad DELLA}$
$\text{\color{red}POISSON}$

$$X \sim \mathcal{P}(\lambda) \implies X \approx \mathcal{N}(\lambda, \lambda)$$

l'approssimazione è ritenuta buona se $\lambda \ge 10$;
anche qui possiamo applicare una CC di $0.5$



<!-- ===== PAGINA 43 ===== -->

<!-- Pagina 43 -->

- ESERCIZIO 6.14

$$p = P(\text{Recupero}) = 0.9$$

$$X = n^\circ \text{ pazienti che recuperano } (\text{su } 100)$$

$$X \sim Bi(100, 0.9), \text{ ovvero } X \dot{\sim} N(90, 9)$$

1. $P(84 \le X \le 95) =$

   $= P(83.5 < X < 95.5) \quad Z \sim N(0, 1)$

   $\overset{!}{=} P(-2.17 < Z < 1.83)$

   $\overset{!}{\simeq} 0.9514 \quad \left[ \begin{array}{l} \cdot \text{ senza cc: } 0.9295 \\ \cdot \text{ esatta } : 0.9556 \end{array} \right]$

2. $P(X < 86) = P(X < 85.5) \simeq \Phi(-1.50)$
   $$\underbrace{\quad\quad\quad}_{0.0668}$$

$$\left[ \begin{array}{l} \text{senza cc:} \quad 0.0912 \\ \text{esatta}: \quad\quad 0.0726 \end{array} \right]$$



<!-- ===== PAGINA 44 ===== -->

<!-- Pagina 44 -->

ESEMPIO

$X = n^\circ \text{particelle in una sospensione di } 5\text{ml}$

$\lambda = 50 \text{ particelle/ml} \longrightarrow \text{TASSO MEDIO}$

Calcolare

a) $P(235 \le X \le 265)$

Sotto le ipotesi del processo di Poisson (che sono ragionevoli in questo caso)

$X \sim P(250)$

Usiamo il TLC: $X \approx N(250, 250)$

Si ottiene
$$P(-0.95 \le Z \le 0.95) = 0.6572$$

$$\left[ \begin{array}{l}
\text{con CC:} \quad 0.6730 \\
\text{esatta} \quad : \quad 0.6731
\end{array} \right] \quad \uparrow_{\text{senza CC}}$$

b) $P(48 \le \bar{X} \le 52)$, $\bar{X} = n^\circ \text{ medio particelle/ml}$



<!-- ===== PAGINA 45 ===== -->

<!-- Pagina 45 -->

$$\overline{X} = \frac{X}{5} \stackrel{a}{\sim} \mathcal{N}(50, 10)$$

$$\left(\text{NB: non è } \overline{X} \stackrel{a}{\sim} \mathcal{N}(50, 50) !\right)$$

$$P(48 \le \overline{X} \le 52) \simeq 0.4714$$

c) Quanto deve essere il volume prelevato per ottenere una probabilità del punto precedente pari a $0.55$?

$$\overline{X} = \frac{X}{v} \quad , \quad v = \text{volume prelevato}$$

$$\overline{X} \stackrel{a}{\sim} \mathcal{N}\left(50, \frac{50}{v}\right)$$

> **[Nota Grafico: Schizzo di una curva normale (gaussiana) simmetrica centrata in $50$. L'area sotto la curva è ombreggiata e indicata con $0.95$. Sull'asse orizzontale sono indicati i punti $50$, $50 - (1.96)\sqrt{\frac{50}{v}}$ e $50 + \sqrt{\frac{50}{v}} \cdot (1.96)$]**

$$\text{ovvero:} \quad 52 = 50 + \sqrt{\frac{50}{v}} \cdot (1.96) \implies V = 48.02 \text{ ml}$$



<!-- ===== PAGINA 46 ===== -->

<!-- Pagina 46 -->

# DISTRIBUZIONE LOGNORMALE

* Adatta per fenomeni ASIMMETRICI, con occasionali OUTLIERS

Sia $X \sim N(\mu, \sigma^2)$, allora $Y = e^X$ ha una distribuzione LOGNORMALE di parametri $\mu$ e $\sigma^2$

$$Y \sim \log N (\mu, \sigma^2)$$

* Ricaviamo la distribuzione di $Y$:

$$F_Y (y; \mu, \sigma) = P(Y \le y) \quad \text{per } \sigma > 0$$

$$= P(e^X \le y) = P(X \le \log(y))$$

ovvero 

$$F_Y(y; \mu, \sigma) = \Phi \left( \frac{\log(y) - \mu}{\sigma} \right)$$

* Per la densità basta calcolarne la derivata, ricordando che

$$\Phi'(z) = \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}$$



<!-- ===== PAGINA 47 ===== -->

<!-- Pagina 47 -->

Per $y > 0$

$$f_Y(y; \mu, \sigma) = \phi\left(\frac{\log(y) - \mu}{\sigma}\right) \cdot \frac{1}{\sigma} \cdot \frac{1}{y}$$

Ovvero:

$$f_Y(y; \mu, \sigma) = \begin{cases} 0 & y \le 0 \\ \frac{1}{\sqrt{2\pi}\sigma y} e^{-\frac{(\log(y) - \mu)^2}{2\sigma^2}} & y > 0 \end{cases}$$

- Grafici: si veda Fig. 6.29

- ESEMPIO 6.22

$$X \sim \log N(3.2, 1)$$

$$\log(X) \sim N(3.2, 1)$$

$$P(X > 8) = P(\log(X) > \log(8))$$

$$= 1 - \Phi\left(\frac{\log(8) - 3.2}{2}\right)$$

$$= 0.8688$$



<!-- ===== PAGINA 48 ===== -->

<!-- Pagina 48 -->

- Proprietà: se $Y \sim \log N(\mu, \sigma^2)$ (10)

$$E(Y) = e^{\mu + \sigma^2/2}$$

$$V(Y) = e^{2\mu + 2\sigma^2} - e^{2\mu + \sigma^2}$$

( si trovano mediante fgm di $\log(Y)$ )

- $y_\alpha = e^{\mu + \sigma z_\alpha}$, sfrutto i percentili di $X = \log(Y)$

ESEMPIO 6.23

$Y =$ miglia vita di un dispositivo

$Y \sim \log N(\mu, \sigma^2)$, $\mu = 5.149$
$\sigma = 0.737$

$$y_{0.05} = e^{5.149 + (0.737)(-1.645)}$$

$$= e^{3.537} = 51.625 \text{ miglia}$$



<!-- ===== PAGINA 49 ===== -->

<!-- Pagina 49 -->

## DISTRIBUZIONI DI DURATA

Adatte a modellare la "durata di vita" (tempo di funzionamento corretto) di componenti di vario tipo. In opportune situazioni, anche Normale e Lognormale possono essere adatte a modellare tempi, ma le più usate distribuzioni di durata sono:

* Esponenziale
* Gamma
* Weibull

## Esponenziale

$X$ v.c. con f. di densità, per $\beta > 0$

$$f_X(x; \beta) = \begin{cases} \frac{1}{\beta} e^{-\frac{x}{\beta}}, & x > 0 \\ 0, & x \le 0 \end{cases}$$

$X \sim \mathcal{E}(1/\beta)$ o anche $X \sim \text{Exp}(1/\beta)$



<!-- ===== PAGINA 50 ===== -->

<!-- Pagina 50 -->

$$\text{Nota: talvolta la distribuzione viene}$$
$$\text{parametrizzata in } \lambda = \frac{1}{\beta} \underbrace{\text{TASSO}}_{\uparrow} \nearrow_{\text{PARAMETRO DI SCALA}}$$
$$\left( \text{è del tutto equivalente} \right), X \sim \mathcal{E}(\lambda)$$

- $F.$ di $\text{RIPARTIZIONE}:$

$$F_X (x; \beta) = \begin{cases} 0 & x \le 0 \\ 1 - e^{-\frac{x}{\beta}} & x > 0 \end{cases}$$

$$\boxed{E(X) = \beta} \quad \boxed{V(X) = \beta^2}$$
$$\llcorner\!\!\!\rightarrow \text{Integrale per parti}$$

- $\text{Percentili} : \quad 0 < \alpha < 1$

$$1 - e^{-\frac{x_\alpha}{\beta}} = \alpha$$
$$\implies \boxed{x_\alpha = -[\log(1-\alpha)]\beta}$$



<!-- ===== PAGINA 51 ===== -->

<!-- Pagina 51 -->

# RELAZIONE CON IL PROCESSO DI POISSON ($\rightarrow$ file d'attesa)

**PROPOSIZIONE** Dato un Processo di Poisson di tasso $\lambda > 0$, il tempo $T$ che intercorre tra 2 arrivi consecutivi è $T \sim \mathcal{E}(\lambda)$

<u>Prova</u>

* Otteniamo $F_T(t)$, verificando che ha la forma tipica della distribuzione esponenziale

* se $t \le 0$ ovviamente $P(T \le 0) = 0$
  $$\downarrow$$
  è un tempo

* Se $t > 0$: per calcolare $P(T \le t)$ introduciamo la v.c. $X$

  $$X = n^\circ \text{ arrivi in } [0,t]$$
  $$X \sim \mathcal{P}(\lambda t)$$

> **[Nota Grafico: Asse temporale da $0$ a $t$. Nel punto $t$ c'è una freccia verticale verso il basso con l'etichetta "$1^\circ \text{ arrivo}$"]**

$$P(T > t) = P(X=0) = e^{-\lambda t} \text{ quindi}$$

$$\underset{\text{PASSAGGIO CHIAVE}}{\uparrow}$$

$$P(T \le t) = 1 - e^{-\lambda t}$$



<!-- ===== PAGINA 52 ===== -->

<!-- Pagina 52 -->

- PROPRIETÀ DI ASSENZA DI MEMORIA (4)

$$X \sim \mathcal{E}(1/\beta) \quad t>0, t_0>0$$

$$\overline{P(X > t_0+t \mid X > t_0) = P(X>t)}$$

Infatti:

$$P(X > t_0+t \mid X > t_0) = \frac{P(X > t_0+t)}{P(X > t_0)}$$

$$= \frac{e^{-\frac{(t_0+t)}{\beta}}}{e^{-\frac{t_0}{\beta}}} = e^{-t/\beta} = P(X>t)$$

- Nota: la proprietà implica la MANCANZA D'USURA per il componente.

$\hookrightarrow$ la distribuzione è adatta come modello per il tempo di funzionamento solo in condizioni molto particolari.



<!-- ===== PAGINA 53 ===== -->

<!-- Pagina 53 -->

## III. DISTRIBUZIONE GAMMA $\textcircled{5}$

Generalizza l'esponenziale, prende il nome dalla

$$\text{FUNZIONE GAMMA} \quad \Gamma(\alpha) = \int_{0}^{\infty} x^{\alpha-1} e^{-x} \, dx, \text{ per } \alpha > 0$$

$$\begin{aligned}
\text{Proprietà}: \quad & \Gamma(n) = (n-1)! \quad \text{per } n \text{ intero} \\
& \Gamma(\alpha) = (\alpha-1) \, \Gamma(\alpha-1) \quad, \quad \alpha > 1 \\
& \Gamma(1/2) = \sqrt{\pi}
\end{aligned}$$

$$X \sim \text{ga}\left(\alpha, 1/\beta\right) \quad \begin{aligned} \alpha > 0 \\ \beta > 0 \end{aligned}$$

$$\underset{\text{DI FORMA}}{\text{PARAMETRO}} \quad \nearrow \quad \beta \rightarrow \underset{\text{DI SCALA}}{\text{PARAMETRO}}$$

Ha f. densità di probabilità:

$$f_X(x; \alpha, \beta) = \begin{cases} \dfrac{x^{\alpha-1} e^{-x/\beta}}{\beta^\alpha \, \Gamma(\alpha)} &, x > 0 \\[10pt] 0 &, x \le 0 \end{cases}$$



<!-- ===== PAGINA 54 ===== -->

<!-- Pagina 54 -->

* PARAMETRIZZAZIONE ALTERNATIVA:

$$\lambda = \frac{1}{\beta}$$

$\text{TASSO}$

- Se $\alpha = 1 \implies X \sim \mathcal{E}\left(\frac{1}{\beta}\right)$

<u>ALTRI CASI PARTICOLARI</u>

- Se $\alpha$ è INTERO $\implies$ DISTRIBUZIONE DI ERLANG

- Se $\alpha = \frac{k}{2}$ ($k$ intero), $\beta = 2 \implies$ DISTRIBUZIONE CHI-QUADRATO

- Proprietà: 
$$\begin{cases} E(X) = \alpha \beta \\ \\ V(X) = \alpha \beta^2 \end{cases}$$

---

1. Teorema. $\longrightarrow$ RELAZIONE CON IL PROCESSO DI POISSON

$X_1, X_2, \dots, X_n \quad \text{indip.} \quad X_i \sim \mathcal{E}\left(\frac{1}{\beta}\right)$

$$Y = \sum_{i=1}^n X_i \sim \text{Ga}\left(n, \frac{1}{\beta}\right)$$

$\text{Prova:}$ usa la f.g.m.



<!-- ===== PAGINA 55 ===== -->

<!-- Pagina 55 -->

* Proprietà: se $\alpha$ è intero (distribuzione di Erlang) si può ottenere la $F_X$

Per $x > 0$:

$$F_X(x; \alpha, \beta) = 1 - \sum_{j=0}^{\alpha-1} \frac{e^{-x/\beta} (x/\beta)^j}{j!}$$

$\hookrightarrow$ F. di RIPARTIZIONE V.C. ERLANG

* Commenti: la distribuzione gamma offre un modello molto più flessibile della distribuzione esponenziale, per $\alpha \neq 1$ non gode della proprietà di assenza di memoria $\longrightarrow$ adatta a modellare fenomeni affetti da usura

* Ha inoltre un ruolo in relazione al processo di Poisson



<!-- ===== PAGINA 56 ===== -->

<!-- Pagina 56 -->

# 10. DISTRIBUZIONE WEIBULL

(8)

- Come la distribuzione gamma, estende la distr. esponenziale ma è molto più flessibile

$$X \sim \text{Weibull}(\alpha, \beta)$$

$$f_X(x; \alpha, \beta) = \begin{cases} \alpha \beta \, x^{\beta-1} e^{-\alpha x^\beta}, & x > 0 \\ 0, & x \le 0 \end{cases}$$

$\alpha > 0, \quad \beta > 0$
$\downarrow$
$\text{PARAMETRO DI FORMA}$

- Se $\beta = 1$, $\quad X \sim \mathcal{E}(\alpha)$

- F di ripartizione per $x > 0$:

$$F_X(x; \alpha, \beta) = \int_0^x \alpha \beta \, t^{\beta-1} e^{-\alpha t^\beta} \, dt$$

$$\text{poniamo} \quad u = \alpha t^\beta$$
$$du = \alpha \beta \, t^{\beta-1} dt$$



<!-- ===== PAGINA 57 ===== -->

<!-- Pagina 57 -->

$$\int_0^{\alpha x^\beta} e^{-u} \, du = 1 - e^{-\alpha x^\beta}$$

Avrò:

$$F_X(x; \alpha, \beta) = \begin{cases} 0 & x \le 0 \\ 1 - e^{-\alpha x^\beta} & x > 0 \end{cases}$$

* Con passaggi analoghi si ottiene

$$E(X) = \frac{\Gamma\left(1 + \frac{1}{\beta}\right)}{\alpha^{1/\beta}}$$

* ### TASSO DI GUASTO

$X$ V.C. DI DURATA (QUALSIASI)

$$Z(x) = \frac{f_X(x)}{1 - F_X(x)}, \quad x > 0$$

$$1 - F_X(x) = \int_x^\infty f_X(t) \, dt \quad \text{AFFIDABILITÀ}$$

La definizione di $Z(x)$ deriva dalla

$$P(x < X < x + \varepsilon \mid X > x) = \frac{F_X(x + \varepsilon) - F_X(x)}{1 - F_X(x)}$$
per $\varepsilon > 0$



<!-- ===== PAGINA 58 ===== -->

<!-- Pagina 58 -->

perciò
$$\lim_{\varepsilon \to 0^+} \frac{P(x < X < x + \varepsilon \mid X > x)}{\varepsilon} = \frac{f_X(x)}{1 - F_X(x)} = Z(x)$$

**(10)**

- Se $X \sim \text{Weibull}(\alpha, \beta)$

$$Z(x) = \alpha \beta x^{\beta-1} \quad, \quad x > 0$$

- per $\beta = 1$: $Z(x) = \alpha$, ASSENZA DI MEMORIA

- per $\beta > 1$: $Z(x)$ cresce con $x$, il componente si logora nel tempo. È il caso tipico.

- per $\beta < 1$: $Z(x)$ decresce con $x$, il componente si rafforza nel tempo. Poco comune.



<!-- ===== PAGINA 59 ===== -->

<!-- Pagina 59 -->

# La funzione generatrice dei momenti

* Data una v.c. $X$, la sua **funzione generatrice dei momenti (f.g.m.)** è la funzione reale con argomento $t \in \mathbb{R}$

$$m_X(t) = E\left(e^{tX}\right)$$

ovvero

$$m_X(t) = \begin{cases} \sum e^{t x} p_X(x) & \text{se } X \text{ è discreta} \\ \int_{-\infty}^{+\infty} e^{t x} f_X(x) dx & \text{se } X \text{ è continua} \end{cases}$$

* La f.g.m. esiste se la sommatoria o l'integrale sono finiti in un intervallo aperto che contiene lo zero, ovvero del tipo $(-t_0, t_0)$, con $t_0 > 0$.



<!-- ===== PAGINA 60 ===== -->

<!-- Pagina 60 -->

# Proprietà della f.g.m.

La f.g.m. (che nel caso continuo è simile alla trasformata di Fourier della funzione di densità) gode di alcune importanti proprietà:

1. Il comportamento della funzione nel punto $0$ è rilevante:

$$
\begin{aligned}
m_X(0) &= 1 \\
m'_X(0) &= E(X) \\
m''_X(0) &= E(X^2) \\
\dots &\quad \dots \\
m_X^{(n)}(0) &= E(X^n)
\end{aligned}
$$

2. Non è detto che la f.g.m. esista, ma **se esiste determina la distribuzione**, ovvero è in corrispondenza 1:1 con la funzione di ripartizione di $X$ (e quindi con $p_X$ o $f_X$);

---

<div style="font-size: small; display: flex; justify-content: space-between;">
<span>a.a 2024/2025 — R. Bellio</span>
<span>2 / 7</span>
</div>



<!-- ===== PAGINA 61 ===== -->

<!-- Pagina 61 -->

Proprietà della f.g.m.

3. Se $X$ e $Y$ sono indipendenti, si ottiene

$$m_{X+Y}(t) = m_X(t) \, m_Y(t) \,.$$

Più in generale: se $X_1, \dots, X_n$ sono indipendenti, e
$S_n = \sum_{i=1}^n X_i$

$$m_{S_n}(t) = \prod_{i=1}^n m_{X_i}(t) \, ,$$

e se le $X_i$ hanno tutte la stessa distribuzione

$$m_{S_n}(t) = (m_X(t))^n \,.$$

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

$$m_{X+Y}(t) = m_X(t) \, m_Y(t) = e^{\lambda_1 (e^t - 1)} \, e^{\lambda_2 (e^t - 1)},$$

$$m_{X+Y}(t) = e^{(\lambda_1 + \lambda_2)(e^t - 1)}$$

* Si riconosce la f.g.m. di una distribuzione $\mathcal{P}(\lambda_1 + \lambda_2)$, e allora dalla proprietà 2. segue che

$$X + Y \sim \mathcal{P}(\lambda_1 + \lambda_2)$$

* Il risultato si estende ad una somma di un numero qualsiasi di v.c. di Poisson indipendenti.



<!-- ===== PAGINA 64 ===== -->

<!-- Pagina 64 -->

# Applicazioni notevoli

- Si procede in maniera analoga per trovare la distribuzione della somma di v.c. normali, Gamma (con lo stesso parametro di scala $\beta$) o binomiali (con lo stesso parametro $p$) indipendenti.

- Analogamente, si ottiene la distribuzione di trasformazione lineare di una v.c. normale: i passi sono i seguenti
  - Sia $X \sim \mathcal{N}(\mu, \sigma^2)$ e $Y = a + b X$, con $a, b \in \mathbb{R}$
  - Si ottiene facilmente che

$$m_Y(t) = E[e^{(a+b X)t}] = e^{a t} m_X(b t) = e^{(a+b\mu)t + b^2 t^2 \sigma^2 / 2}\,,$$

  e si riconosce la f.g.m. di una distribuzione $\mathcal{N}(a + b\mu, b^2 \sigma^2)$, per cui

$$Y \sim \mathcal{N}(a + b\mu, b^2 \sigma^2)\,.$$



<!-- ===== PAGINA 65 ===== -->

<!-- Pagina 65 -->

# Applicazioni notevoli (continua)

* Un'altra applicazione notevole è quella per ottenere la distribuzione di una combinazione lineare di v.c. normali indipendenti.
* Anche il teorema del limite centrale si dimostra utilizzando la f.g.m.: se $X_1, \dots, X_n$ sono i.i.d. con $E(X_i) = \mu$ e $V(X_i) = \sigma^2$, si può verificare che la f.g.m. della v.c.

$$Z_n = \frac{\overline{X} - \mu}{\sqrt{\frac{\sigma^2}{n}}}$$

tende alla f.g.m. di una $\mathcal{N}(0, 1)$ per $n \to \infty$.

* Un altro risultato è che se $X \sim \mathcal{N}(\mu, \sigma^2)$, allora

$$m_X(1) = E\left(e^X\right) = e^{\mu + \frac{1}{2}\sigma^2}$$

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

$$y = (y_1, \dots, y_n),$$

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

$$T = t(Y_1, \dots, Y_n) \, .$$

Sono esempi di statistiche gli indici utilizzati nella statistica descrittiva

$$\overline{Y}, S^2 \text{, la mediana campionaria, } \dots \, ,$$

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
  $$\Rightarrow E(Y_1 + \ldots + Y_n) = \mu_1 + \ldots + \mu_n \,.$$

* $Y_1, \ldots, Y_n$ v.c. **indipendenti** con $V(Y_1) = \sigma_1^2, \ldots, V(Y_n) = \sigma_n^2$
  $$\Rightarrow V(Y_1 + \ldots + Y_n) = \sigma_1^2 + \ldots + \sigma_n^2 \,.$$



<!-- ===== PAGINA 82 ===== -->

<!-- Pagina 82 -->

# A) Richiami sulle somme di variabili casuali

Una conseguenza importante dei risultati appena visti riguarda la **variabile casuale media campionaria**

$$\overline{Y} = \frac{1}{n} \sum_{i=1}^{n} Y_i$$

- Se $Y_1, \dots, Y_n$ sono v.c. indipendenti con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, allora

$$E(\overline{Y}) = \sum_{i=1}^{n} \frac{E(Y_i)}{n} = n \frac{\mu}{n} = \mu \text{,}$$

$$V(\overline{Y}) = \sum_{i=1}^{n} \frac{V(Y_i)}{n^2} = n \frac{\sigma^2}{n^2} = \frac{\sigma^2}{n} \text{.}$$



<!-- ===== PAGINA 83 ===== -->

<!-- Pagina 83 -->

# A) La v.c. varianza campionaria

Nel caso di variabili i.i.d., con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, ci sono dei risultati anche per **variabile casuale varianza campionaria**

$$S^2 = \frac{1}{n-1} \sum_{i=1}^n (Y_i - \overline{Y})^2$$

- Se $Y_1, \dots, Y_n$ sono v.c. indipendenti con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$, allora

$$E(S^2) = \sigma^2$$

$$V(S^2) = (\sigma^2)^2 \left( \frac{2}{n-1} + \frac{\kappa}{n} \right)\text{,}$$

con $\kappa$ costante che dipende dalla distribuzione ($0$ per $Y_i$ normali, ma non in generale).



<!-- ===== PAGINA 84 ===== -->

<!-- Pagina 84 -->

# A) Teorema del limite centrale

**Teorema** Sia $Y_1, Y_2, \dots$ una successione di v.c. indipendenti, ciascuna con $E(Y_i) = \mu$ e $V(Y_i) = \sigma^2$. Allora, posto $Z_n = \sqrt{n}(\overline{Y} - \mu)/\sigma$, per ogni $z$

$$\lim_{n \to \infty} P(Z_n \le z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-t^2/2} dt = \Phi(z) \, .$$

In simboli il teorema del limite centrale (t.l.c.) si denota scrivendo

$$Z_n = \sqrt{n}\frac{(\overline{Y} - \mu)}{\sigma} \xrightarrow{\mathcal{D}} \mathcal{N}(0, 1) \, ,$$

dove $\xrightarrow{\mathcal{D}}$ si legge "converge in distribuzione".

Una lettura **pratica** del teorema del limite centrale è la seguente:

$$\overline{Y} \stackrel{a}{\sim} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right) \, ,$$

dove $\stackrel{a}{\sim}$ significa "distribuita approssimativamente".



<!-- ===== PAGINA 85 ===== -->

<!-- Pagina 85 -->

# A) Teorema del limite centrale: utilizzo

Il t.l.c. permette di approssimare la distribuzione di $\overline{Y}$, o, in maniera equivalente, della somma di $n$ v.c. i.i.d.

$$\sum_{i=1}^{n} Y_i \stackrel{a}{\sim} \mathcal{N}(n\mu, n\sigma^2) \ .$$

Si tratta di un risultato molto utile, del tipo chiamato **per grandi campioni**, nel senso che l'approssimazione è migliore per dimensioni campionarie elevate. Più precisamente, *quanto* deve essere grande $n$ dipende dalla distribuzione della popolazione:

* se il campione proviene da una distribuzione quasi simmetrica, l'approssimazione è buona già per piccoli valori di $n$;
* se la distribuzione è molto asimmetrica, è necessario un valore di $n$ abbastanza grande;
* per la maggior parte delle distribuzioni, un campione di numerosità 30 (o più) è sufficientemente elevato affinché l'approssimazione normale sia adeguata.



<!-- ===== PAGINA 86 ===== -->

<!-- Pagina 86 -->

# B) Risultati per variabili bernoulliane

Se consideriamo $n$ v.c. bernoulliane $Y_i \sim \text{Bernoulli}(p)$, $i = 1, \dots, n$, indipendenti, si ottiene facilmente che

$$\sum_{i=1}^{n} Y_i \sim Bi(n, p) \,,$$

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

$$\sum_{i=1}^n Y_i \sim \mathcal{P}\left(\sum_{i=1}^n \lambda_i\right) \text{.}$$

In particolare, per v.c. i.i.d. (dove $\lambda_i = \lambda$) si ottiene $\sum_{i=1}^n Y_i \sim \mathcal{P}(n \lambda)$. Anche in questo caso, tuttavia, il t.l.c. è spesso utilizzato, ovvero

$$\sum_{i=1}^n Y_i \stackrel{a}{\sim} \mathcal{N}(n\lambda, n\lambda) \text{.}$$

L'approssimazione è ritenuta buona se $n\lambda > 10$.



<!-- ===== PAGINA 89 ===== -->

<!-- Pagina 89 -->

## D) Risultati per variabili normali

Per il caso $Y_i \sim \mathcal{N}(\mu, \sigma^2)$, $i = 1, \dots, n$, indipendenti, esistono diversi risultati.

Come caso particolare della proprietà che combinazioni lineari di normali indipendenti sono ancora normali, si ottiene

$$\overline{Y} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right),$$

$$\sum_{i=1}^n Y_i \sim \mathcal{N}(n\mu, n\sigma^2),$$

senza alcuna approssimazione!

Altri risultati richiedono preliminarmente la definizione di due distribuzioni collegate alla normale, ovvero la **distribuzione chi-quadrato** e la **distribuzione $t$ di Student**.



<!-- ===== PAGINA 90 ===== -->

<!-- Pagina 90 -->

# La distribuzione chi-quadrato

La somma di $n$ v.c. normali standard indipendenti elevate al quadrato ha distribuzione chi-quadrato con $n$ gradi di libertà, in simboli $\chi_n^2$. Ovvero, se $Z_i \sim \mathcal{N}(0, 1)$, $i = 1, \dots, n$, indipendenti,

$$Y = \sum_{i=1}^{n} Z_i^2 \sim \chi_n^2$$

La distribuzione è un caso particolare di distribuzione Gamma, con $\alpha = n/2$ e $\beta = 2$, e allora si trova $E(Y) = n$ e $V(Y) = 2n$.

## Funzione di densità

> **[Nota Grafico: Un grafico cartesiano che mostra le funzioni di densità di probabilità per la distribuzione chi-quadrato con tre differenti gradi di libertà ($n = 5$, $n = 10$, $n = 20$). Sull'asse delle ascisse sono riportati i valori di $y$ da $0$ a $50$, mentre sull'asse delle ordinate compaiono i valori di densità $f(y)$ da $0.00$ a $0.15$. La curva continua rappresenta $n=5$, la curva tratteggiata rappresenta $n=10$, e la curva punteggiata rappresenta $n=20$.]**

---

a.a 2024/2025 — R. Bellio \hfill 25 / 28



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

<!-- ===== PAGINA 121 ===== -->

# (1) IC per la MEDIA (CASO SINGOLO CAMPIONE) (2)

$X_1, X_2, \dots, X_n \text{ ccs } (iid) \begin{cases} E(X_i) = \mu \\ V(X_i) = \sigma^2 \end{cases}$

- $\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i \approx N\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{TLC}$

$\left( e \text{ (per ora) } \right) \text{ si suppone } \sigma^2 \text{ NOTA}$

$$\searrow \quad Z = \frac{\bar{X} - \mu}{\sqrt{\frac{\sigma^2}{n}}} \approx N(0,1)$$

$\left( \cdot \text{ Nota: se } X_i \sim N(\mu, \sigma^2) \text{ il risultato è esatto!} \right)$

- Per definizione di percentile:

$$P\left( -z_{1-\alpha/2} < Z < z_{1-\alpha/2} \right) \underset{\uparrow}{\stackrel{\text{per } n \text{ elevato}}{\cong}} 1-\alpha$$
$$\uparrow_{\text{percentile } N(0,1)}$$

$$P\left( -z_{1-\alpha/2} < \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} < z_{1-\alpha/2} \right) = 1-\alpha$$

- Ora il passo decisivo è riesprimere la doppia diseguaglianza in termini di $\mu$:

<!-- ===== PAGINA 122 ===== -->

$$P\left(\overline{x} - z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}} < \mu < \overline{x} + z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}}\right) = 1-\alpha$$

$\rightarrow$ IC di livello $(1-\alpha)$ per $\mu$:

$$\overline{x} - z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}} < \mu < \overline{x} + z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}}$$

$$\overline{x} \pm z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}} \quad \rightarrow \quad \begin{matrix} \text{IC} \\ \text{OSSERVATO} \\ \text{(calcolato con i dati)} \end{matrix}$$

* Il risultato è esatto (nel senso che la probabilità di inclusione è $1-\alpha$) per campioni normali o $n$ elevato.

* Approssimazione accettabile nel caso non normale per $n \ge 30 \longrightarrow$ $\text{RISULTATO VALIDO PER GRANDI CAMPIONI}$

* Nota: ampiezza IC $\quad 2 \cdot z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}}$

  * $\text{AUMENTA} \quad \text{per} \quad (1-\alpha) \longrightarrow 1$

  * $\text{AUMENTA} \quad \text{per} \quad \sigma \text{ che aumenta}$

  * $\text{DIMINUISCE} \quad \text{al crescere di } n$

<!-- ===== PAGINA 123 ===== -->

ES: Produzione pezzi meccanici  (4)

SI SUPPONE  
$$n = 100 \quad \bar{x} = 12.05 \quad \sigma = 0.2$$

IC $95\%$ per $\mu$: 
$$12.05 - (1.96)\frac{(0.2)}{\sqrt{100}} < \mu < 12.05 + (1.96)\frac{(0.2)}{\sqrt{100}}$$

$$z_{0.975} \quad \underbrace{\hspace{2.5cm}}_{0.392}$$

$$\left(12.011 \,,\, 12.089\right)$$

Siamo "FIDUCIOSI / CONFIDENTI" al $95\%$ che l'errore nella stima di $\mu$ non supera $0.392$.

## INTERPRETAZIONE IC

Dato un intervallo osservato, non possiamo dire che includerà $\mu$ con probabilità $(1-\alpha)$: infatti, la probabilità si riferisce all'intervallo con estremi le V.C., non a quello osservato!

L'unica garanzia che abbiamo è che, in un NUMERO MOLTO ELEVATO di campioni ottenuti nelle stesse condizioni gli intervalli calcolati con quella formula includeranno il vero $\mu$ il $95\%$ delle volte.  
È questo il senso di "essere fiduciosi o confidenti" al $95\%$.

<!-- ===== PAGINA 124 ===== -->

> **[Nota Grafico: Un diagramma che illustra il concetto di intervalli di confidenza (IC). Mostra cinque intervalli orizzontali (rappresentanti diversi campioni), con una linea verticale tratteggiata centrale che indica il valore vero del parametro $\mu$. Quelli dall'1° al 3° e il 5° includono la linea verticale $\mu$, mentre il 4° campione è disallineato e non include $\mu$. Una freccia punta dal 4° campione a una nota testuale a sinistra: "i campioni con IC che non include $\mu$ sono il 5%". C'è anche una nota numerata con un cerchio rosso (5).]**

# UTILIZZARE IC per DIMENSIONARE IL CAMPIONE

Fissato $e = z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}}$, errore nella stima di $\mu$

Conoscendo $\sigma$, $e$ $(1-\alpha)$ posso ottenere $n$:

$$n = \left(\frac{z_{1-\alpha/2} \ \sigma}{e}\right)^2$$

ES: Fisso: $e = 0.015$, $\sigma$ ignoto $s = 0.2$

$$n = 1.56^2 \cdot 0.2^2 / 0.015^2 = 682.95 \rightarrow \boxed{683}$$

<!-- ===== PAGINA 125 ===== -->

## LIMITI DI CONFIDENZA UNILATERALI (6)
(IC su il sol limite inferiore o superiore)

$$\overline{x} - z_{1-\alpha} \frac{\sigma}{\sqrt{n}} \hspace{3cm} \overline{x} + z_{1-\alpha} \frac{\sigma}{\sqrt{n}}$$

Infatti: $P\left(\overline{x} - z_{1-\alpha} \cdot \frac{\sigma}{\sqrt{n}} < \mu\right) = 1-\alpha$

Utili in particolari situazioni

ES: $\overline{x} - z_{0.95} \frac{(0.2)}{10} = 12.017$

$(12.017, \infty) \longrightarrow \begin{matrix} \text{IC su il} \\ \text{sol} \\ \text{limite} \\ \text{inferiore} \\ \text{di livello } 95\% \end{matrix}$

## ① IL CASO DI $\sigma$ IGNOTA

- Se $\sigma^2$ è ignota (caso tipico nelle applicazioni) viene rimpiazzata da $s^2$, la stima campionaria
- Se $n$ è elevato, l'effetto della sostituzione è trascurabile

<!-- ===== PAGINA 126 ===== -->

* Se $n$ è piccolo ($n < 30$), l'effetto esiste, e la teoria richiede che $X_i \sim N(\mu, \sigma^2)$: per campioni normali si ottiene allora

$$T = \frac{\bar{x} - \mu}{\sqrt{\frac{s^2}{n}}} \sim t_{n-1}$$

e l'IC è quindi $\quad$ *(Nota: con una freccia rossa indicata l'etichetta "percentuale $1-\alpha/2$ di $t_{n-1}$" sopra il termine $t_{n-1; 1-\alpha/2}$)*

$$\bar{x} \pm t_{n-1; 1-\alpha/2} \frac{s}{\sqrt{n}}$$

* Nota: se $n$ è elevato $t_{n-1} \sim N(0,1)$, confermando che per grandi campioni l'effetto di utilizzare $s^2$ è trascurabile.

ESEMPIO 3.5: $n = 7 \quad \bar{x} = 10.0 \quad s = 0.283$

$$(1-\alpha) = 0.95 \quad t_{6; 0.975} = 2.447$$

$$10 \pm 2.447 \frac{(0.283)}{\sqrt{7}} = (9.74, 10.26)$$

<!-- ===== PAGINA 127 ===== -->

NOTA
$$\sigma_{\overline{x}} = \frac{\sigma}{\sqrt{n}} = \text{ERRORE STANDARD}$$

$$\widehat{\sigma}_{\overline{x}} = \frac{s}{\sqrt{n}} = \text{ERRORE STANDARD STIMATO}$$

IC per $\mu$ (grandi campioni):
$$\begin{cases}
\overline{x} \pm z_{1-\alpha/2} \,\, \sigma_{\overline{x}} &, \sigma \text{ NOTA} \\
\overline{x} \pm z_{1-\alpha/2} \,\, \widehat{\sigma}_{\overline{x}} &, \sigma \text{ IGNOTA}
\end{cases}$$

## 10 INTERVALLI DI PREVISIONE (CASO NORMALE)

- Siamo interessati a PREVEDERE il valore di una V.C. prima della sua realizzazione, sulla base dei dati di un campione osservato
$$X_1, X_2, \dots, X_n \quad \text{CCS} \quad X_i \sim N(\mu, \sigma^2)$$
$$\searrow_{\text{DATI DISPONIBILI}}$$

$$X_0 \quad \text{IGNOTA}$$

$$X_0 \sim N(\mu, \sigma^2) \text{, indipendente dalle altre v.c.}$$

<!-- ===== PAGINA 128 ===== -->

• CASO $\sigma$ NOTA:

$$X_0 - \overline{X} \sim N\left(\mu - \mu, \sigma^2 + \frac{\sigma^2}{n}\right)$$

$$Z = \frac{X_0 - \overline{X}}{\sigma \sqrt{1 + \frac{1}{n}}} \sim N(0, 1)$$

Con passaggi analoghi a quelli per $IC$ per $\mu$:

$$P\left(\overline{X} - z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}} < X_0 < \overline{X} + z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}}\right) = 1-\alpha$$

$$\llcorner \rightarrow \quad \overline{X} \pm z_{1-\alpha/2} \sigma \sqrt{1 + \frac{1}{n}}$$

INTERVALLO DI PREVISIONE (IP) DI LIVELLO $(1-\alpha)$

• Se $\sigma$ è IGNOTA: $\quad \overline{X} \pm t_{n-1; 1-\alpha/2} S \sqrt{1 + \frac{1}{n}}$

e per $n$ elevato posso usare $z_{1-\alpha/2}$ invece di $t_{n-1; 1-\alpha/2}$

NOTA:
$\begin{bmatrix}
\text{Gli intervalli di previsione sono sempre più} \\
\text{ampi degli $IC$ per $\mu$, e non hanno ampiezza} \\
\text{che $\rightarrow 0$ per $n \rightarrow \infty$}
\end{bmatrix}$

<!-- ===== PAGINA 129 ===== -->

- ESEMPIO 9.7:

$X_0 = \text{ammontare prestito prossimo cliente}$

DATI: $n = 50$
$\bar{x} = 257300 \text{ \$}$
$\sigma = 25000 \text{ \$}$ (DATI STORICI)

IP di livello $95\%$:
$$257300 \pm (1.96) \cdot 25000 \cdot \sqrt{1 + \frac{1}{50}}$$
$$= (207812, 306788)$$

NOTA: IC per $\mu$ è invece $(250370, 264230)$

IP vengono spesso usati per individuare VALORI ANOMALI (OUTLIERS):

> Un' osservazione è anomala se NON è inclusa nell' IP calcolato senza includere quell' osservazione nel campione

<!-- ===== PAGINA 130 ===== -->

### III) IC DIFFERENZA TRA DUE MEDIE (CASO NUMEROSITÀ CAMPIONARIE ELEVATE)

* Alcuni problemi inferenziali coinvolgono **DUE CAMPIONI** (indipendenti), relativi a due diverse sotto-popolazioni.

#### ASSUNZIONI

* i) $X_1, X_2, \dots, X_{n_x}$ CCS

  $$E(X_i) = \mu_X \quad , \quad V(X_i) = \sigma^2_X \quad \text{NOTA}$$

* ii) $Y_1, Y_2, \dots, Y_{n_y}$ CCS

  $$E(Y_i) = \mu_Y \quad , \quad V(Y_i) = \sigma^2_Y \quad \text{NOTA}$$

* iii) I DUE CAMPIONI SONO INDIPENDENTI

Dal TLC: 

$$\bar{X} \stackrel{a}{\sim} N\left(\mu_X, \frac{\sigma^2_X}{n_x}\right)$$

$\downarrow$

$$n_x, n_y \ge 30$$

$$\bar{Y} \stackrel{a}{\sim} N\left(\mu_Y, \frac{\sigma^2_Y}{n_y}\right)$$

Inoltre, da $iii)$ segue che $\bar{X}$ e $\bar{Y}$ sono V.C. INDIPENDENTI

<!-- ===== PAGINA 131 ===== -->

Quindi:

$$\overline{X} - \overline{Y} \stackrel{a}{\sim} N\left(\mu_X - \mu_Y, \frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}\right)$$

$$Z = \frac{(\overline{X} - \overline{Y}) - (\mu_X - \mu_Y)}{\sqrt{\frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}}} \stackrel{a}{\sim} N(0, 1)$$

IC per $\mu_X - \mu_Y$ di livello $(1-\alpha)$, caso VARIANZE NOTE E GRANDI CAMPIONI:

$$\left(\overline{x} - \overline{y}\right) \pm z_{1-\alpha/2} \sqrt{\frac{\sigma_X^2}{n_X} + \frac{\sigma_Y^2}{n_Y}}$$

- ESATTO per V.C. NORMALI

<!-- ===== PAGINA 132 ===== -->

(III) CASO VARIANZE IGNOTE 3

$\rightarrow$ campioni elevati, rimprazziamo $\sigma_x^2$ e $\sigma_y^2$
con le stime $S_x^2$ e $S_y^2$, senza ulteriori cambiamenti ($n_x \geq 30$, $n_y \geq 30$)

$\rightarrow$ piccoli campioni, V.C. NORMALI con VARIANZE IGNOTE e NON NECESSARIAMENTE UGUALI: usiamo

$$T = \frac{(\bar{X} - \bar{Y}) - (\mu_x - \mu_y)}{\sqrt{\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}}} \sim t_\nu$$

$\llcorner$ RISULTATO APPROSSIMATO, ma l'errore è trascurabile

$$\nu = \frac{\left(\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}\right)^2}{\left[ \frac{\left(\frac{S_x^2}{n_x}\right)^2}{n_x - 1} + \frac{\left(\frac{S_y^2}{n_y}\right)^2}{n_y - 1} \right]}$$

$\llcorner$ ARROTONDATO ALL'INTERO INFERIORE

$\llcorner$ FORMULA di WELCH / SATTERTHWAITE

IC: $(\bar{x} - \bar{y}) \pm t_{\nu; 1-\alpha/2} \sqrt{\frac{S_x^2}{n_x} + \frac{S_y^2}{n_y}}$

<!-- ===== PAGINA 133 ===== -->

* Esistono formule anche per il caso di VARIANZE IGNOTE MA UGUALI

$$(\bar{x} - \bar{y}) \pm t_{n_x+n_y-2 \;;\; 1-\alpha/2} \; s_p \sqrt{\frac{1}{n_x} + \frac{1}{n_y}}$$

$$s_p^2 = \frac{(n_x-1)s_x^2 + (n_y-1)s_y^2}{n_x + n_y - 2} \quad \begin{array}{c} \text{STIMA} \\ \text{"POOLED"} \\ \text{DELLA VARIANZA} \end{array}$$

* In pratica, l'IC con la formula di WELCH può essere usato anche se le varianze sono uguali

<u>ES 9.22</u>

| FARMAG 1 | FARMAG 2 |
| :--- | :--- |
| $n_x = 14$ | $n_y = 16$ |
| $\bar{x} = 17$ | $\bar{y} = 19$ |
| $s_x^2 = 1.5$ | $s_y^2 = 1.8$ |

* IC $95\%$ : il testo calcola $(0.70, 3.30)$, assumendo uguali varianze.

* Formula di Welch: $\nu = 27.9 \implies \nu = 27$

$$t_{27 \;;\; 0.995} = 2.771$$

<!-- ===== PAGINA 134 ===== -->

$$\left(\overline{y}-\overline{x}\right)\pm 2.771 \sqrt{\frac{1.5}{14}+\frac{1.8}{16}} \quad \text{(5)}$$

$$\Rightarrow \left(\;0.701 \;,\; 3.259\;\right)$$

---

# III) OSSERVAZIONI APPAIATE

**ESEMPIO:** Misuro carico di rottura per $n=8$ provini di tessuto (diversi tra loro) su due diversi macchinari

| Provino | Macc. 1 | Macc. 2 | Differenza |
| :---: | :---: | :---: | :---: |
| 1 | 74 | 78 | $-4$ |
| 2 | 76 | 79 | $-3$ |
| 3 | 74 | 75 | $-1$ |
| 4 | 69 | 66 | $3$ |
| 5 | 58 | 63 | $-5$ |
| 6 | 71 | 70 | $1$ |
| 7 | 66 | 66 | $0$ |
| 8 | 65 | 67 | $-2$ |

$$X_1, X_2, \dots, X_n \quad \text{ccs } 1^\circ \text{ macchinario}$$

$$Y_1, Y_2, \dots, Y_n \quad \text{ccs } 2^\circ \text{ macchinario}$$

<!-- ===== PAGINA 135 ===== -->

PROBLEMA: $X_i$ e $Y_i$ (STESSO PROVINO) (6)

NON SONO INDIPENDENTI!
Ci aspettiamo $\rho_{X_i, Y_i} > 0$ (e infatti $\rho_{X, Y} > 0.5$)

Non possiamo usare le formule per campioni indipendenti!

SOLUZIONE: Considero le $n$ DIFFERENZE

$$D_i = X_i - Y_i, \quad i = 1, 2, \dots, n \quad \text{CCS}$$

$$E(D_i) = \mu_X - \mu_Y = \mu_D$$

$$V(D_i) = \sigma_D^2 \quad \text{IGNOTA}$$

$\longrightarrow$ Uso formula per IC per $\mu$ caso singolo campione, con varianza ignota

$$\hat{\mu}_D \pm t_{n-1; \, 1-\alpha/2} \sqrt{\frac{S_D^2}{n}}$$

* Al solito, per $n$ elevato uso $z_{1-\alpha/2}$, invece di $t_{n-1; \, 1-\alpha/2}$

<!-- ===== PAGINA 136 ===== -->

Nell'esempio: $\hat{\mu}_D = \bar{d} = -1.375$

$SD = 2.669$

$1 - \alpha = 0.95 \ , \ t_{7; 0.975} = 2.364$

$IC \ 95\%$ per $\mu_D \ : \ (-3.607, \ 0.857)$

che include il valore $0$, che implica

$\mu_X = \mu_Y$

<!-- ===== PAGINA 137 ===== -->

### (11) IC PER UNA PROPORZIONE (1)

$X_1, X_2, \dots, X_n \quad \text{c.c.s.} \quad X_i \sim \text{Bernoulli}(p)$

$$X = \sum_{i=1}^n X_i \quad , \quad \hat{p} = \frac{X}{n} = \bar{X}$$

$$\text{TLC}: \quad \hat{p} \stackrel{a}{\sim} N\left(p, \frac{p(1-p)}{n}\right)$$

$$\text{Infatti} \quad \mu = p \quad \text{e} \quad \sigma^2 = p(1-p)$$

- Se particolarizziamo l'IC per $p$ nel caso di grandi campioni otteniamo:

$$\hat{p} \pm z_{1-\alpha/2} \sqrt{\frac{p(1-p)}{n}}$$

Che tuttavia non è utilizzabile perché $p$ non è noto!

- Se $n$ è elevato, rimpiazzo $p$ con $\hat{p}$:

$$\hat{p} \pm z_{1-\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$ 
$\left\{ \begin{array}{l} \text{IC CLASSICO} \\ \to \text{RISTRETTO A } (0,1) \end{array}\right.$

<!-- ===== PAGINA 138 ===== -->

# IC MIGLIORATI

Hanno senso se $n$ non è elevato (come criterio approssimato potremmo adottare $n\hat{p}$ o $n(1-\hat{p}) < 5$)

Ne esistono di diversi tipi, tra i quali:

- Il metodo del Testo di Walpole et al., che tuttavia è molto complesso ("Metodo 2")
- Il metodo di Agresti e Coull, che invece è molto semplice: la formula dell'IC è la stessa, ma si applica dopo aver AGGIUNTO 2 SUCCESSI E 2 INSUCCESSI al campione osservato!

- ESEMPIO 9.14:

$n = 500$

$x = 340$

Abbonati ad un servizio (nuclei famigliari)

$p =$ probabilità che una famiglia a caso si abboni

$= \text{proporzione di famiglie abbonate}$

$$\hat{p} = \frac{340}{500} = 0.68$$

$$\left( \tilde{p} = \frac{342}{504} = 0.679 \right) \quad \text{Per A-C:}$$

<!-- ===== PAGINA 139 ===== -->

<div style="text-align: right;">3</div>

- 3 diversi IC:

IC classico: $(0.639, \,\, 0.721)$
IC Metodo 2: $(0.638, \,\, 0.719)$
IC Agresti-Coull: $(0.638, \,\, 0.719)$

Ipottiziamo $n = 50$ e $x = 34$ ($\hat{p} = 0.68$)

IC classico: $(0.551, \,\, 0.809)$
IC Metodo 2: $(0.542, \,\, 0.792)$
IC A-C: $(0.541, \,\, 0.792)$

$n = 25$ e $x = 17$: $\hat{p} = 0.68$ ($n(1-\hat{p}) = 8$)

IC Classico: $(0.457, \,\, 0.863)$
IC Metodo 2: $(0.484, \,\, 0.828)$
IC A-C: $(0.482, \,\, 0.828)$

$n = 25$ e $x = 21$ ($n(1-\hat{p}) = 4$)

IC Classico: $(0.696, \,\, 0.984)$
IC Metodo 2: $(0.653, \,\, 0.936)$
IC A-C: $(0.646, \,\, 0.541)$

$\longrightarrow$ Il metodo A-C coniuga SEMPLICITÀ e ACCURATEZZA!

<!-- ===== PAGINA 140 ===== -->

# DIMENSIONAMENTO DEL CAMPIONE

$$n = \frac{z_{1-\alpha/2}^2 \cdot \sigma^2}{e^2} \longrightarrow \frac{z_{1-\alpha/2}^2 \cdot p(1-p)}{e^2}$$

* La formula generale è inutilizzabile, salvo che non si disponga di una stima preliminare di $p$
* In caso contrario pongo $p = 1/2$ (caso "peggiore", dato che è il valore che rende massima $p(1-p)$)

# IC PER LA DIFFERENZA TRA DUE PROPORZIONI

i) $X_1, X_2, \dots, X_{n_x}$ CCS $\quad X_i \sim \text{Bernoulli}(p_x)$

ii) $Y_1, Y_2, \dots, Y_{n_y}$ CCS $\quad Y_i \sim \text{Bernoulli}(p_y)$

iii) I DUE CAMPIONI SONO INDIPENDENTI

* Di nuovo, particolarizziamo le formule generali; rimpiazzando $p_x$ e $p_y$ con le loro stime nella radice

<!-- ===== PAGINA 141 ===== -->

5

IC Classico (per grandi campioni):

$$(\hat{p}_x - \hat{p}_y) \pm z_{1-\alpha/2} \sqrt{\frac{\hat{p}_x(1-\hat{p}_x)}{n_x} + \frac{\hat{p}_y(1-\hat{p}_y)}{n_y}}$$

> **[Nota Grafico: Una freccia curva parte dalla formula e punta a una nota che dice "Ristretto all'intervallo (-1, 1)"]**

* IC Migliorati: il metodo di Agresti-Coull si applica anche in questo caso, si ottiene AGGIUNGENDo 1 successo e 1 insuccesso a ciascun campione ($2 + 2$ in totale) e applicando poi la formula

<!-- ===== PAGINA 142 ===== -->

# VERIFICA D'IPOTESI: CONCETTI GENERALI

Nel seguito verranno introdotte molte definizioni (in blu)

- Un'IPOTESI STATISTICA è una CONGETTURA riguardante una o più (sotto) popolazioni
  > **[Nota Grafico: Una freccia indica una nuvola di testo in un riquadro rosso]**
  > è un'AFFERMAZIONE su $\theta$ di un MODELLO STATISTICO PARAMETRICO

Idea di base: sulla base dei DATI, decidiamo se RIFIUTARE o NO l'ipotesi

ES: Dati binari, 12 difettosi su 100, è ragionevole concludere che $p = \text{PROP. DIFETTOSE}$ sia $>10\%$?

# IPOTESI NULLA e ALTERNATIVA

- IPOTESI NULLA $H_0$: è l'ipotesi da verificare
- IPOTESI ALTERNATIVA $H_1$: è l'ipotesi che vale se RIFIUTO $H_0$

ES: Dati binari $\begin{cases} H_0: p = 0,10 \\ H_1: p > 0,10 \end{cases}$

<!-- ===== PAGINA 143 ===== -->

<div align="right">2</div>

Mediante la verifica d'ipotesi:

* RIFIUTO $H_0$ se c'è sufficiente evidenza nei dati
* NON RIFIUTO $H_0$ in caso contrario

Analogia con un processo penale:

$$
\begin{cases}
H_0: \text{imputato innocente} \longrightarrow \text{"status quo"} \\
H_1: \text{imputato colpevole}
\end{cases}
$$

> **[Nota Grafico: Parentesi graffa esterna con due frecce che collegano le condizioni del processo penale alle relative conseguenze sul verdetto]**

* Con prove schiaccianti $\longrightarrow$ imputato è condannato (RIFIUTO $H_0$)
* In mancanza di prove $\longrightarrow$ imputato non viene condannato (NON RIFIUTO $H_0$)

* $\underline{\text{STATISTICA TEST}}$: è una statistica che
  $(T \text{ o } Z)$ utilizziamo per decidere
  se rifiutare o meno $H_0$

$\llcorner_{\rightarrow}$ Viene utilizzata per effettuare il TEST d'ipotesi

<!-- ===== PAGINA 144 ===== -->

*(3)*

* Sia $T$ la statistica test prescelta: i valori possibili della statistica vengono divisi in 2 gruppi:
* REGIONE CRITICA: solo i valori che portano al rifiuto di $H_0$

RIMANENTI VALORI: non portano al rifiuto di $H_0$

ES: 
$$\begin{cases} H_0: p = 0.10 \\ H_1: p > 0.10 \end{cases}$$
$$X_1, X_2, \dots, X_n$$
$$\text{CCS} \quad , \quad n = 100$$
$$X_i \sim \text{Bernoulli}(p)$$

Poniamo:
$$T = \sum_{i=1}^{100} X_i$$

$$\text{Regione Critica}_{R_c} = \{ T > 15 \}$$

> **[Nota Grafico: Linea retta orizzontale numerata da 0 a 100, con un segno di divisione a 15. L'intervallo da 0 a 15 è etichettato come "NON RIFIUTO $H_0$", mentre l'intervallo da 15 a 100 è etichettato come "RIFIUTO $H_0$".]**

Nota: se $t \in R_c$ si dice che "IL RISULTATO È SIGNIFICATIVO (CONTRO $H_0$)"

<!-- ===== PAGINA 145 ===== -->

4

* ERRORI nella verifica d'ipotesi

* ERRORE $I^\circ$ TIPO: Rifiuto $H_0$ quando è VERA

* ERRORE $II^\circ$ TIPO: NON RIPIUTO $H_0$ quando è FALSA

L'errore di $I^\circ$ TIPO è ritenuto più grave: si pensa all'analogia con il processo penale

* LIVELLO di SIGNIFICATIVITÀ (AMPIEZZA DEL TEST)

* $\alpha = P (\text{ERRORE } I^\circ \text{ TIPO})$

ES: $\alpha = P(T > 15\ ; p = 0.10)$

$$= \sum_{t=16}^{100} \binom{100}{t} \ 0.10^t \ (0.90)^{100-t} = 0.04$$

È un valore basso, il che è una buona proprietà perché voglio commettere ERRORE $I^\circ$ TIPO raramente

Associato al livello $\alpha$ esiste anche

* $\beta = P (\text{ERRORE } II^\circ \text{ TIPO})$

<!-- ===== PAGINA 146 ===== -->

<div align="right">5</div>

Nell' esempio: $\beta$ è una funzione del valore di $p$,
tra quelli $> 0.10$

$$\beta(p) = P(\ T \le 15\ ;\ p\ )$$

Se
$$
\begin{aligned}
p &= 0.15 &\quad \beta &= 0.568 \\
p &= 0.20 &\quad \beta &= 0.129 \\
p &= 0.40 &\quad \beta &= 0.0004
\end{aligned}
$$

> **[Nota Grafico: Un grafico cartesiano che rappresenta la funzione $\beta(p)$ in funzione di $p$. Sull'asse verticale vi è $\beta(p)$ con il valore segnato $0.96$, sull'asse orizzontale vi è $p$ con i valori $0.10$ e $0.3$. La curva parte da un punto evidenziato in alto a sinistra a $p = 0.10$ (con valore $0.96$) e decresce asintoticamente verso destra all'aumentare di $p$.]**

* POTENZA di un Test : è $1-\beta$ ovvero
la PROBABILITÀ di un CORRETTO RIFIUTO di $H_0$

<u>Nota bene</u>: $\alpha$ e $\beta$ sono collegati tra loro, non
posso annullarli simultaneamente.
In pratica: fissiamo $\alpha$ ad un valore basso,
e verifichiamo il valore di $\beta$

<!-- ===== PAGINA 147 ===== -->

PROPRIETÀ: per un test CONSISTENTE (ragionevole), (6)
per $\alpha$ fissato si ha che $\beta$ decresce
dell' aumentare della dimensione del
campione
$\longrightarrow$ posso agire su $\beta$ aumentando $n$

ES: Ipotizziamo di raddoppiare $n=200$

$$R_c = \{ T > 27 \}$$

$$\alpha = \sum_{t=28}^{200} P(T=t; p=0.10) = 0.043$$
$\llap{\raise 1.5ex\hbox{}}_\text{o più o meno come prima}$

Se
$$
\begin{array}{ll}
p = 0.15: & \beta = 0.317 \\
p = 0.20: & \beta = 0.011 \\
p = 0.25: & \beta \approx 0
\end{array}
\}
\text{più bassi}\\\text{del caso}\\\text{n=100}
$$

<!-- ===== PAGINA 148 ===== -->

ES: STATICA TEST NORMALE

$n=36$ pesi $X_1, \dots, X_n$ CCS $\begin{cases} E(X_i) = \mu \\ V(X_i) = \sigma^2 \end{cases}$

$\sigma = 3.6 \text{ kg (NOTA)}$

$\begin{cases} H_0: & \mu = 68 \\ H_1: & \mu \neq 68 \longrightarrow \text{cioè } \mu > 68 \text{ oppure } \mu < 68 \end{cases}$

$T = \overline{X} \sim N\left(\mu, \frac{3.6^2}{36}\right)$ STATISTICA TEST

$R_c = \{ T < 66.8 \text{ oppure } T > 69.2 \}$

$\alpha = P_{H_0} (\overline{X} < 66.8) + P_{H_0} (\overline{X} > 69.2)$

$\alpha = 0.0228 + 0.0228 = 0.0455$

$\beta$ dipende da vero $\mu$: per $\begin{cases} \mu = 69 \longrightarrow \beta = 0.630 \\ \mu = 70 \longrightarrow \beta = 0.0912 \\ \mu = 71 \longrightarrow \beta = 0.013 \end{cases}$

<!-- ===== PAGINA 149 ===== -->

> **[Nota Grafico: Grafico in alto a destra contrassegnato dal numero (8). Mostra due distribuzioni normali sovrapposte (in nero la distribuzione nulla sotto $H_0$ centrata a $68$, in rosso la distribuzione alternativa sotto $H_1$ centrata a $70$). Vengono evidenziate le aree delle code per il livello di significatività $\alpha/2$ (a sinistra e a destra) e l'errore di tipo II ($\beta$) in rosso tra le due curve, con valori numerici sull'asse delle ascisse: $66.8$, $68$, $69.2$, $70$.]**

* DISTRIBUZIONE NULLA di $T$: vale sotto $H_0$
* DISTRIBUZIONE ALTERNATIVA di $T$: "$ \quad "$ $H_1$

* TIPI DI IPOTESI

* IPOTESI ALTERNATIVA UNILATERALE

$$\begin{cases} H_0: \vartheta = \vartheta_0 \\ H_1: \vartheta > \vartheta_0 \quad \left( \text{oppure } \vartheta < \vartheta_0 \right) \end{cases} \quad \nearrow \text{TEST AD UNA CODA}$$

<u>NOTA BENE</u> $\quad H_0: \vartheta \le \vartheta_0$ è lo stesso se $H_1: \vartheta > \vartheta_0$

* IPOTESI ALTERNATIVA BILATERALE

$$\begin{cases} H_0: \vartheta = \vartheta_0 \\ H_1: \vartheta \neq \vartheta_0 \end{cases} \quad \longrightarrow \text{TEST A DUE CODE}$$

<!-- ===== PAGINA 150 ===== -->

- Come scelgo $H_0$ e $H_1$? Dipende dal contesto applicativo, da quali informazioni sono disponibili e a quale conclusione si vuole giungere.

ES 1: Se $p = 0.10$ era il tasso di prodotti difettosi e sospetto sia peggiorato, l'alternativa ragionevole è $p > 0.10$.

ES 2: Se $\mu = 68$ era un peso medio ragionevole, ma non abbiamo informazioni riguardo in quale direzione potrebbe essere diversa, allora $\mu \neq 68$ è l'alternativa ragionevole.

---

## IL P-VALUE

- PROCESSO DECISIONALE nella VERIFICA D'IPOTESI
  - Fisso $\alpha = 0.05$ (oppure $\alpha = 0.01$, di solito)
  - Se uso una statistica test $Z \sim N(0,1)$ _sotto_ $H_0$ per un Test bilaterale ottengo:

$$R_C = \{ Z < -1.96 \cup Z > 1.96 \}$$

$\ll$ _$\alpha_{0.05}$ serve per indicare il valore di $\alpha$_

<!-- ===== PAGINA 151 ===== -->

(10)

> **[Nota Grafico: Schizzo di una distribuzione normale (curva a campana) con asse simmetrico centrato a $0$, e due code evidenziate all'esterno dei valori critici $-1,96$ e $1,96$, annotate con $\alpha/2$]**

- Tuttavia $z_{oss} = 2$ o $z_{oss} = 4$, che cadono entrambe in $R_{0.05}$, forniscono evidenze molto diverse! Questo è quantificato dal P-VALUE

- Il P-VALUE è una STATISTICA calcolata sul campione osservato: è definita come

IL LIVELLO PIÙ BASSO A CUI RISULTA SIGNIFICATIVO IL VALORE OSSERVATO DELLA STATISTICA TEST

ES: $z_{oss} = 2 \quad p = P_{H_0}(|Z| > 2) = 0.0455$
$\llcorner$ EVIDENZA MODERATA CONTRO $H_0$

$z_{oss} = 4 \quad p = P_{H_0}(|Z| > 4) = 0.0000633$
$\llcorner$ EVIDENZA FORTE CONTRO $H_0$

<!-- ===== PAGINA 152 ===== -->

- In pratica: calcolo p-value e lo confronto con una soglia (che, in pratica, corrisponde al valore di $\alpha$)
TABELLA SPESSO (ma non sempre) UTILIZZATA

| Valori p-value | Evidenza contro $H_0$ |
| :--- | :--- |
| $0.05 < p \le 0.1$ | MARGINALE (molto debole) |
| $0.01 < p \le 0.05$ | MODERATA |
| $0.001 < p \le 0.01$ | FORTE |
| $p \le 0.001$ | MOLTO FORTE |

- Esiste una differenza sostanziale tra SIGNIFICATIVITÀ STATISTICA e SIGNIFICATIVITÀ INGEGNERISTICA o SCIENTIFICA

N.B.:
> **[Nota Grafico: riquadro arancione evidenziato con la scritta "N.B.:" sopra, contenente la formula di equivalenza tra test statistico e p-value]**

$$\text{STATISTICA TEST} \in R_\alpha \iff \text{p-value} \le \alpha$$

<!-- ===== PAGINA 153 ===== -->

1

# VERIFICA DI IPOTESI SULLA MEDIA (VARIANZA NOTA)

$X_1, X_2, \dots, X_n \quad \text{CCS}$
$n \text{ elevato}$

$\begin{cases} E(X_i) = \mu \\ V(X_i) = \sigma^2 \text{ NOTA} \end{cases}$

$\text{TLC: } \overline{X} \stackrel{a}{\sim} N\left(\mu, \frac{\sigma^2}{n}\right)$

$\begin{cases} H_0: \mu = \mu_0 \\ H_1: \mu \neq \mu_0 \end{cases}$

$\underline{\text{Sotto } H_0} \quad \overline{X} \stackrel{a}{\sim} N\left(\mu_0, \frac{\sigma^2}{n}\right)$

$$Z = \frac{\overline{X} - \mu_0}{\sqrt{\frac{\sigma^2}{n}}}$$
$\text{STATISTICA TEST}$

$$R_\alpha = \left\{ Z < z_{\alpha/2} \quad \text{oppure} \quad Z > z_{1-\alpha/2} \right\}$$
$$= \left\{ |Z| > z_{1-\alpha/2} \right\}$$

<!-- ===== PAGINA 154 ===== -->

- $\alpha$ è $P(\text{ERRORE } I^\circ \text{ TIPO})$, infatti:

$$P_{H_0} \left( |Z| > z_{1-\alpha/2} \right) = \alpha \quad (\text{per } n \text{ elevato})$$

- $\text{P-VALUE} : \quad p = P_{H_0} \Big( Z > |z_{\text{oss}}| \cup Z < -|z_{\text{oss}}| \Big)$

$$= 2 \,\, P_{H_0} \Big( Z > |z_{\text{oss}}| \Big) = 2 \Big(1 - \Phi(|z_{\text{oss}}|)\Big)$$

- $H_1 \text{ UNILATERALE}$

$$\begin{cases} H_0: \mu = \mu_0 \quad (\text{o anche } \mu \le \mu_0) \\ H_1: \mu > \mu_0 \end{cases}$$

$$\mathcal{R}_\alpha = \Big\{ Z > z_{1-\alpha} \Big\}$$

$$\text{P-VALUE}: \quad p = P_{H_0} \big( Z > z_{\text{oss}} \big) = 1 - \Phi(z_{\text{oss}})$$

- $\text{Per il caso } \quad \begin{cases} H_0: \mu = \mu_0 \quad (\text{o anche } \mu \ge \mu_0) \\ H_1: \mu < \mu_0 \end{cases}$

<!-- ===== PAGINA 155 ===== -->

si ottiene
$$R_\alpha = \{ Z < z_\alpha \}$$

$$p = P_{H_0}(Z < z_{oss}) = \Phi(z_{oss})$$

## ESEMPIO 10.4
$\mu_0 = 8.0 \text{ kg}$ carico di rottura $\to$ affermazione produttore

CCS $n = 50$ \quad $\overline{x} = 7.8 \text{ kg}$ \quad $\sigma = 0.5$

$$\begin{cases} H_0: \mu = 8 \\ H_1: \mu \neq 8 \end{cases} \quad \alpha = 0.01$$

$$R_{0.01} = \{ |Z| > 2.575 \}$$

$$z_{oss} = \frac{7.8 - 8.0}{0.5 / \sqrt{50}} = -2.83 \to \text{RIFIUTO } H_0$$

$$p = 2 P_{H_0}(Z > 2.83) = \underline{0.0046}$$

<!-- ===== PAGINA 156 ===== -->

### (III) RELAZIONE CON IC (4)

* Non rifiuto $H_0$ se $-z_{1-\alpha/2} < Z < z_{1-\alpha/2}$
  
  ovvero se $-z_{1-\alpha/2} < \frac{\overline{x} - \mu_0}{\frac{\sigma}{\sqrt{n}}} < z_{1-\alpha/2}$

$$\Downarrow$$

$$\overline{x} - z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}} < \mu_0 < \overline{x} + z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}}$$

* In altri termini: Non RIFIUTO $H_0$ in $H_0: \mu = \mu_0$ (con $R_{\alpha}$) $\begin{cases} H_0: \mu = \mu_0 \\ H_1: \mu \neq \mu_0 \end{cases}$

  se $\mu_0 \in IC$ per $\mu$ di livello $1-\alpha$

$$\boxed{LIVELLO \ IC = 1 - P(\text{errore } I^\circ TIPO)}$$

* Ovvero:
  * Posso usare $IC$ per effettuare verifica d'ipotesi
  * Posso definire $IC$ utilizzando la verifica d'ipotesi

* Per $H_1$ unilaterale la relazione vale con $IC$ unilaterale

<!-- ===== PAGINA 157 ===== -->

*(5)*

# CASO $\sigma^2$ IGNOTA

* Grandi CAMPIONI ($n \geq 30$): rimpiazzo $\sigma^2$ con $s^2$
* PICCOLI CAMPIONI: abbiamo risultati per campioni NORMALI

$$X_1, X_2, \dots, X_n \quad CCS \quad X_i \sim N(\mu, \sigma^2)$$

$$\begin{cases} H_0: \mu = \mu_0 \\ H_1: \mu \neq \mu_0 \end{cases}$$

Sotto $H_0$:

$$T = \frac{\bar{X} - \mu_0}{\sqrt{\frac{s^2}{n}}} \sim t_{n-1}$$

$$R_\alpha = \left\{ |t| > t_{n-1; \, 1-\alpha/2} \right\}$$

P-VALUE:

$$p = 2 \left(1 - F_{t_{n-1}}(|t_{oss}|)\right)$$

<!-- ===== PAGINA 158 ===== -->

$$H_1: \mu > \mu_0 \quad R_\alpha = \{ t > t_{n-1,\, 1-\alpha} \}$$

$$p = 1 - F_{t_{n-1}}(t_{\text{obs}})$$

$$H_1: \mu < \mu_0 \quad R_\alpha = \{ t < \underbrace{t_{n-1,\, \alpha}}_{-t_{n-1,\, 1-\alpha}} \}$$

$$p = F_{t_{n-1}}(t_{\text{obs}})$$

<!-- ===== PAGINA 159 ===== -->

(7)

# VERIFICA D'IPOTESI SULLE MEDIE DI DUE CAMPIONI

1) VARIANZE NOTE (e campioni elevati)
2) VARIANZE IGNOTE
3) DATI APPAIATI

- 1) VARIANZE NOTE (grandi campioni)

ASSUNZIONI:

i) $X_1, X_2, \dots, X_{n_x}$ CCS $\left\{\begin{array}{l}E(X_i) = \mu_x \\ V(X_i) = \sigma_x^2 \\ \text{NOTA}\end{array}\right.$
   $n_x$ elevato

ii) $Y_1, Y_2, \dots, Y_{n_y}$ CCS $\left\{\begin{array}{l}E(Y_i) = \mu_y \\ V(Y_i) = \sigma_y^2 \\ \text{NOTA}\end{array}\right.$
   $n_y$ elevato

iii) I DUE CAMPIONI SONO INDIPENDENTI

$$\begin{cases}
H_0: \mu_x = \mu_y \\
H_1: \mu_x \neq \mu_y \\
\quad \;\; > \\
\quad \;\; <
\end{cases}$$

Si estende a

$$H_0: \mu_x - \mu_y = \Delta_0$$

<!-- ===== PAGINA 160 ===== -->

**(8)**

$$Z = \frac{\overline{X} - \overline{Y} - \Delta_0}{\sqrt{\frac{\sigma_x^2}{n_x} + \frac{\sigma_y^2}{n_y}}} \stackrel{a}{\sim} N(0,1) \quad \begin{matrix} \text{sotto} \\ H_0 \end{matrix}$$

$$z_{oss} = \frac{\overline{x} - \overline{y} - \Delta_0}{\sqrt{\frac{\sigma_x^2}{n_x} + \frac{\sigma_y^2}{n_y}}}$$

$$R_\alpha = \{|z| > z_{1-\alpha/2}\}$$

$$p = 2\left(1 - \Phi(|z_{oss}|)\right)$$

* Per **VARIANZE IGNOTE**, ma **CAMPIONI ELEVATI**: stesse formule utilizzando $s_x^2$ e $s_y^2$

2) **VARIANZE IGNOTE** (e **possibilmente diverse**)

* Campioni **NORMALI** (e **piccoli**)

$$T = \frac{\overline{X} - \overline{Y} - \Delta_0}{\sqrt{\frac{s_x^2}{n_x} + \frac{s_y^2}{n_y}}} \sim t_\nu \begin{matrix} , \text{sotto} \\ H_0 \end{matrix}$$

$\nu =$ formula di **WELCH / SATTERTHWAITE**

<!-- ===== PAGINA 161 ===== -->

$$R_\alpha = \{ |t| > t_{0; 1-\alpha/2} \}$$

* Per $H_1$ unilaterale, $R_\alpha$ è come nel caso per grandi campioni rimpiazzando i percentili della $N(0,1)$ con quelli della $t$

3) DATI APPAIATI

$X_i$ e $Y_i$ RILEVATI SULLA STESSA UNITÀ (NON INDIPENDENTI)

$$D_i = X_i - Y_i \quad , i = 1, \dots, n$$

$$D_i \sim N(\mu_D, \sigma_D^2) \quad (\text{CASO NORMALE})$$

$$T = \frac{\overline{D} - \Delta_0}{\sqrt{\frac{S_D^2}{n}}} \sim t_{n-1} \quad \text{sotto } H_0$$

Nota:

$$\begin{cases} H_0: \mu_X - \mu_Y = \Delta_0 \\ H_1: \mu_X - \mu_Y \neq \Delta_0 \\ \quad\quad\quad\quad > \\ \quad\quad\quad\quad < \end{cases} \longrightarrow \begin{cases} H_0: \mu_D = \Delta_0 \\ H_1: \mu_D \neq \Delta_0 \\ \quad\quad\quad\quad > \\ \quad\quad\quad\quad < \end{cases}$$

<!-- ===== PAGINA 162 ===== -->

# VERIFICA D'IPOTESI PER UNA PROPORZIONE

$X_1, X_2, \dots, X_n \quad CCS$

$X_i \sim Bernoulli(p)$

$$\begin{cases} H_0: p = p_0 \\ H_1: p \neq p_0 \end{cases}$$

$\hookrightarrow$ oppure $H_1$ UNILATERALE

Sotto $H_0$: 

$n\hat{p} = \sum_{i=1}^n X_i \sim B(n, p_0)$

$TLC \quad \hat{p} \stackrel{a}{\sim} N\left(p_0, \frac{p_0(1-p_0)}{n}\right)$

STATISTICA TEST: di solito si usa la V.C. standardizzata

$$Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} \stackrel{a}{\sim} N(0,1)$$

Sotto $H_0$

<!-- ===== PAGINA 163 ===== -->

* Regione di rifiuto

$$R_\alpha = \{ |z| > z_{1-\alpha/2} \}$$

P-VALUE: $p = 2 \left(1 - \Phi\left(|z_{\text{oss}}|\right)\right)$

* Per $H_1: p > p_0$

$$R_\alpha = \{ z > z_{1-\alpha} \}$$

$$p = 1 - \Phi\left(z_{\text{oss}}\right)$$

* Per $H_1: p < p_0$

$$R_\alpha = \{ z < -z_{1-\alpha} \}$$

$$p = \Phi\left(z_{\text{oss}}\right)$$

<!-- ===== PAGINA 164 ===== -->

- NOTA: Non è in genere necessario apportare delle correzioni per $n$ piccolo, perché sotto $H_0$ la quantità sotto radice è nota senza errore, a differenza di quanto capita per gli $IC$.

Inoltre, la regola $\min(n p_0, n(1-p_0)) > 5$ è affidabile sotto $H_0$.

Nel caso la condizione non fosse soddisfatta una soluzione semplice è:
- risolvo la verifica d'ipotesi sfruttando la relazione tra verifica d'ipotesi e $IC$
- uso $IC$ migliorato

(NOTA: un'altra possibilità è usare la distribuzione nulla ESATTA $Bi(n, p_0)$, che però richiede un computer)

<!-- ===== PAGINA 165 ===== -->

### VERIFICA D'IPOTESI PER DUE PROPORZIONI (4)

Assunzioni:

i) $X_1, X_2, \dots, X_{n_x}$ CCS  
$X_i \sim \text{Bernoulli}(p_x)$

ii) $Y_1, Y_2, \dots, Y_{n_y}$ CCS  
$Y_i \sim \text{Bernoulli}(p_y)$

iii) I DUE CAMPIONI SONO INDIPENDENTI

$$\begin{cases} H_0: p_x = p_y \\ H_1: p_x \neq p_y \\ \phantom{H_1: } > \\ \phantom{H_1: } < \end{cases}$$

- Vediamo il risultato per grandi campioni  
  (per piccoli campioni possiamo agire come  
  nel caso del test per una proporzione)

- Al solito, si parte da uno stimatore di $p_x - p_y$

<!-- ===== PAGINA 166 ===== -->

TLC: $\hat{p}_X - \hat{p}_Y \stackrel{a}{\sim} N\left(p_X - p_Y, \frac{p_X(1-p_X)}{n_X} + \frac{p_Y(1-p_Y)}{n_Y}\right)$

Sotto $H_0$, $p_X = p_Y = p$ e perciò

$$\sum_{i=1}^{n_X} X_i + \sum_{i=1}^{n_Y} Y_i \sim \text{Bi}(n_X + n_Y, p)$$

$$\hat{p} = \frac{\sum_{i=1}^{n} X_i + \sum_{i=1}^{n} Y_i}{n_X + n_Y}$$

$\text{STIMATORE}$
$\text{"POOLED"}$
$\text{DELLA PROPORZIONE}$
$(\text{valido sotto } H_0)$

STATISTICA TEST:

$$Z = \frac{\hat{p}_X - \hat{p}_Y}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_X} + \frac{1}{n_Y}\right)}}$$

Sotto $H_0$:

$$Z \stackrel{a}{\sim} N(0, 1)$$

- Per $R_\alpha$ e P-VALUE: stesse formule del caso di una proporzione

<!-- ===== PAGINA 167 ===== -->

Soluzione degli esercizi di ripasso (versione 10/1/2024)

## Avvertenza importante

Questo documento riporta le soluzioni sintetiche degli esercizi di ripasso per alcuni capitoli del testo di Walpole et al. (2016), limitatamente ai quesiti per i quali la soluzione è numerica.

Visto che tali soluzioni non sono incluse nel materiale reso disponibile dalla casa editrice del testo, **la loro diffusione non infrange nessun diritto di copyright**.

## Cap. 2

* Es. 2.52: 0.0005844
* Es. 2.53: Soluzione grafica.
* Es. 2.54: $\frac{\binom{13}{4}\binom{13}{6}\binom{13}{1}\binom{13}{2}}{\binom{52}{13}}=0.001959$
* Es. 2.55:
  * (1) 0.054
  * (2) 4/9
* Es. 2.56: 13/120
* Es. 2.57:
  * (1) 7/25
  * (2) 18/25
* Es. 2.58:
  * (1) 0.5515
  * (2) 0.2941
* Es. 2.59:
  * (1) 0.0016
  * (2) 0.1048
* Es. 2.60:
  * (1) 0.6312
  * (2) 0.2841
  * (3) 0.0847
* Es. 2.61: $P(\text{Ing.1}|E) = 0.5385$, mentre $P(\text{Ing.2}|E) = 0.4615$, quindi è più probabile si sia trattato dell'Ing.1
* Es. 2.62: 0.23
* Es. 2.63: 1/4

1

<!-- ===== PAGINA 168 ===== -->

- Es. 2.64: $1/9$

**Cap. 3**
- Es. 3.30:
  - (1) $0.3125$
  - (2) $f_Y(y) = 12 \, y (1 - y)^2$, per $0 < y < 1$ (e $0$ altrove)
  - (3) $0.25$
- Es. 3.31:
  - (1) $f_Y(y) = e^{-y}$, per $y > 0$ (e $0$ altrove)
  - (2) $\dfrac{1}{e^6 \, 3} = 0.0008263$
- Es. 3.32:
  - (1) Basta sostituire alla formula i valori richiesti.
  - (2) Soluzione grafica.
  - (3) Basta calcolare le somme cumulate dei valori trovati al punto 1.
- Es. 3.33: L'esercizio si risolve facilmente utilizzando la distribuzione binomiale, argomento del capitolo 5.
- Es. 3.34:
  - (1) $f_X(x) = \dfrac{1}{50} \, e^{-x/50}$, $x > 0$ (e $0$ altrove)
  - (2) $0.2466$
- Es. 3.35: $0.2231$
- Es. 3.36:
  - (1) Occorre risolvere l'integrale.
  - (2) $0.0001$
- Es. 3.37:
  - (1) $f_{X_1} = 2 \, (1 - x_1)$, per $0 < x_1 < 1$ (e $0$ altrove)
  - (2) $f_{X_2} = 2 \, x_2$, per $0 < x_2 < 1$ (e $0$ altrove)
  - (3) $0.2$
  - (4) $f_{X_1|X_2}(x_1|x_2) = \dfrac{1}{x_2}$, per $0 < x_1 < x_2$ (e $0$ altrove)
- Es. 3.38:
  - (1) $p_X(x) = \dfrac{3}{4} \, \dfrac{1}{4^x}$, $x = 0, 1, 2, \dots$; risultato analogo vale per $Y$, e le due v.c. sono indipendenti.
  - (2) $63/64$
- Es. 3.39: $0.999991$

2

<!-- ===== PAGINA 169 ===== -->

Cap. 4

* Es. 4.40: Non in programma.
* Es. 4.41: $333$
* Es. 4.42: $-2/75$
* Es. 4.43:
  (1) $900$ (ore)
  (2) $1620000$
  (3) $\sigma_X^2 = 810000$, $\sigma_X = 900$.
* Es. 4.45: $0$
* Es. 4.46:
  (1) $1/18 * 5000^2$ (si veda Es. $4.19$)
  (2) Non in programma.
  (3) $0.81$
* Es. 4.47: $13000\text{ \$}$
* Es. 4.48:
  (1) $33500\text{ \$}$
  (2) $39689\text{ \$}$
* Es. 4.49:
  1., 2., 4., 5., 7.: immediate
  (3) La distribuzione condizionata di $X_1$ dato $X_2 = 3$ ha supporto $(0, 1, 2, 3, 4)$ con rispettive probabilità $(7/15, 3/15, 1/15, 3/15, 1/15)$
  (4) $1.2$
* Es. 4.50: $6.55\text{\$}$
* Es. 4.51:
  (1) $1/11$
  (2) $10/11$
  (3) $0.006887$

Cap. 5

* Es. 5.39:
  (1) $0.1710$
  (2) $0.2832$
* Es. 5.40: $0.0308$
* Es. 5.41:
  (1) $0.000562$
  (2) Non sembra credibile l'affermazione del produttore riguardo il tasso di difettosità del $5\%$, dato il valore molto basso della probabilità calcolata al punto 1.

<!-- ===== PAGINA 170 ===== -->

- Es. 5.42:
  - (1) $0.2642$
  - (2) $0.0371$
- Es. 5.43:
  - (1) $0.5177$
  - (2) $0.4914$
- Es. 5.44:
  - (1) $6$
  - (2) $5.82$
  - (3) $0.0023$
- Es. 5.45:
  - (1) $0.9277$
  - (2) $0.000981$
  - (3) $0.01$
- Es. 5.46: $0.4661$
- Es. 5.47: $0.1301$
- Es. 5.48:
  - (1) $0.3633$
  - (2) Anche se il lotto contiene due difettosi, la probabilità di non accettare il lotto non è molto alta (è inferiore a $0.5$). Per aumentarla si dovrebbero campionare più di $n = 10$ elementi; ad esempio, con $n = 15$ si ottiene $P(X > 0) = \dots$
  - (3) $0.4$
- Es. 5.49:
  - (1) $0.008$
  - (2) $0.096$
  - (3) $0.896$
- Es. 5.50: $0.3351$. L'approssimazione binomiale non è molto buona visto che $n / N = 0.2$ è troppo elevato.
- Es. 5.51:
  - (1) $P(X \ge 5) \approx 0$. Si tratta di un evento rarissimo, per cui l'affermazione non sembra corretta.
  - (2) Anche con l'approssimazione con la distribuzione di Poisson si ha $P(X \ge 5) \approx 0$.

**Cap. 6**
- Es. 6.31: $0.6086$
- Es. 6.32: $0.5768$
- Es. 6.33: $0.052$
- Es. 6.34:
  - (1) $0.1056$

4

<!-- ===== PAGINA 171 ===== -->

(2) $0.4013$

- Es. 635:
  (1) $\approx 0$
  (2) $0.1587$
  (3) $0.9270$

- Es. 636: 1-$0.9772$=$0.0228$

- Es. 637: $1097.633$

- Es. 638:
  (1) Si verifica che $f(y) \geq 0$ e il suo integrale tra $0$ e $1$ vale $1$.
  (2) $0.4^{10} = 0.0001$
  (3) $\alpha = 1$, $\beta = 10$
  (4) $0.0909$
  (5) $0.006887$

- Es. 639: $E(Z) = 10$, $V(Z) = 10^2$

- Es. 640:
  (1) $1 - e^{-21/15} = 1 - 0.2466$
  (2) $e^{-30/15} = 0.1353$

- Es. 641: Svolto a lezione. Per calcolare l'integrale richiesto dalla funzione di ripartizione è consigliabile effettuare un cambio di variabile, utilizzando $z = \alpha t^{\beta}$.

- Es. 642: Basta ricordare l'espressione di media e varianza di una v.c. Gamma.

## Cap. 9

- Es. 9.46: Si noti che $\widehat{\sigma}^2$ è lo stimatore $S^{'2}$ degli esercizi 9.16 e 9.18, e il confronto tra i due è stato già fatto in quei due esercizi. Oltre alle conclusioni di questi due esercizi, si noti che entrambi gli stimatori sono consistenti.

- Es. 9.47: Dopo aver notato che si tratta di dati appaiati, si ottiene l'intervallo osservato $(0.99, 6.12)$ per la differenza $\mu_{PRIMA} - \mu_{DOPO}$; l'intervallo non include lo $0$, per cui c'è un effetto positivo del trattamento. L'intervallo inoltre include il valore medio $4.5\text{ Kg}$, e quindi l'affermazione appare giustificata.

- Es. 9.48: Dopo aver notato che si tratta di dati appaiati, si ottiene l'intervallo osservato $(-0.12, 3.12)$ per la differenza $\mu_{PRIMA} - \mu_{DOPO}$; l'intervallo include lo $0$, per cui non c'è nessuna evidenza di un effetto positivo. Tuttavia l'intervallo anche include il valore medio $2\text{ cm}$ corrispondente all'affermazione del produttore, per cui in questo senso l'affermazione è giustificata; permangono tuttavia dei dubbi e sarebbero necessari ulteriori dati.

- Es. 9.49: Dopo aver notato che si tratta di due campioni indipendenti, utilizzando la formula che assume le varianze note (e quindi utilizza i percentili della normale), ovvero

$$(\overline{x} - \overline{y}) \pm z_{1-\alpha/2} \sqrt{\frac{4000^2}{8} + \frac{4000^2}{8}},$$

dove $z_{1-\alpha/2} = 1.96$, si ottiene l'intervallo osservato $(2492.5, 10332.5)$, che indica che la lucidatura porta ad una resistenza limite media maggiore.

- Es. 9.50: Non in programma.

5

<!-- ===== PAGINA 172 ===== -->

* Es. 9.51: L'equazione da risolvere nel metodo dei momenti è
$$E(X_i) = \bar{x}$$
da cui si trova subito $\widehat{\lambda} = \bar{x}$.
* Es. 9.52: Si deve risolvere il sistema
$$\begin{cases} e^{\mu + \sigma^2/2} &= \bar{x} \\ (e^{2\mu + \sigma^2}) (e^{\sigma^2} - 1) &= s^2 \end{cases}$$
Si trova $\widehat{\sigma}^2 = \log \left(1 + \frac{s^2}{\bar{x}^2}\right)$ e $\widehat{\mu} = \log(\bar{x}) - \frac{\widehat{\sigma}^2}{2}$.
* Es. 9.53:
  1. $(2781.5, 4818.5)$, che non include lo $0$, suggerendo che il salario medio nella regione settentrionale è maggiore.
  2. Gli assunti sono che i dati provengono da due CCS indipendenti; non occorre assumere la normalità delle variabili che rappresentano le singole osservazioni perché si tratta di campioni elevati, e si può utilizzare il teorema del limite centrale per la media campionaria.
* Es. 9.54: Non in programma.
* Es. 9.55: $301$, arrotondando all'intero superiore.
* Es. 9.56: Si trova l'intervallo osservato $0.161 < \sigma < 0.310$, che include il valore $0.3$: i dati suggeriscono che la variabilità del processo, pur diminuita, è compatibile con quella precedente.
* Es. 9.57: Il risultato si trova immediatamente tenendo conto i due stimatori dati dalle varianze campionarie sono non distorti per $\sigma^2$.
* Es. 9.58:
  1. $0.0227, 0.0623$
  2. $(0, 0.0591)$
  3. Usando entrambi gli intervalli (e il secondo appare più appropriato, visto che l'interesse è in particolare rivolto verso proporzioni di difettosità più elevate), non abbiamo elementi per contestare l'affermazione del produttore. Infatti, in entrambi i casi il valore $0.05$ è incluso nell'intervallo di confidenza osservato.

## Cap. 10

* Es. 10.49: L'esercizio fornisce solo una descrizione stringata e interamente pre-sperimentale, per cui la formulazione delle ipotesi di interesse non è del tutto agevole. Un'interpretazione ragionevole è quella di assumere sempre l'alternativa bilaterale, salvo quando il testo suggerisce di fissare $H_1$ unilaterale utilizzando termini del tipo "non più" o "almeno il". Pertanto:
(1), (3), (5): si adotta $H_1$ bilaterale, quindi (ad esempio) nel caso (1) si scriverà $H_0 : \mu = 21.8$ contro $H_1 : \mu \neq 21.8$.
(2): coerentemente con i punti sopracitati, la descrizione sembra riferita all'ipotesi nulla, per cui si scriverà $H_0 : p \le 0.2$ contro $H_1 : p > 0.2$. Poi, va ricordato, le conclusioni saranno le stesse se si passa a $H_0 : p = 0.2$, con la medesima $H_1$.
(4), (6): in linea con il punto precedente, per il punto (4) ad esempio si scriverà $H_0 : p \ge 0.7$ contro $H_1 : p < 0.7$; anche qui è possibile passare a $H_0 : p = 0.7$.
* Es. 10.50: Test per due proporzioni con $z_{oss} = 2.12$, il test è significativo al livello del $5\%$. Si rifiuta $H_0$.

<!-- ===== PAGINA 173 ===== -->

* Es. 10.51: Test per due medie (piccoli campioni, varianze ignote) con $t_{oss} = 3.978$, distribuzione di riferimento $t_5$. Si ottiene $0.005 < \text{P-value} < 0.01$, con forte evidenza contro $H_0$.
* Es. 10.52: Non in programma.
* Es. 10.53: Test per dati appaiati con $t_{oss} = -2.12$, si trova $0.05 < \text{P-value} < 0.10$, con evidenza molto debole contro $H_0$. Non si rifiuta $H_0$, pur con qualche dubbio.
* Es. 10.54: L'esercizio si può risolvere utilizzando un test per due medie (piccoli campioni, varianze ignote), senza fare considerazioni sulle varianze. Si trova $t_{oss} = -5.90$, distribuzione di riferimento $t_{13}$. Si trova $\text{P-value} > 0.001$, si rifiuta $H_0$ senza esitazione.
* Es. 10.55: L'esercizio si può risolvere utilizzando un test per due medie (piccoli campioni, varianze ignote), senza fare considerazioni sulle varianze. Si trova $t_{oss} = 2.592$, distribuzione di riferimento $t_{29}$. Si trova $0.01 < \text{P-value} < 0.015$, ovvero con una moderata evidenza contro $H_0$.
* Es. 10.56: Si trova $z_{oss} = 2.183$, con $\text{P-value} = 0.0145$, con una moderata evidenza contro $H_0$.

<div align="center">7</div>