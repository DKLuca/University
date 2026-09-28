<!-- ===== PAGINA 1 ===== -->

<!-- Pagina 1 -->

### (IIII) VALORE ATTESO (1)

**Def** $X$ v.c. : MEDIA o VALORE ATTESO di $X$ è (o SPERANZA MATEMATICA)

$$
\mu_X = E(X) = \begin{cases} \sum_{x} x \, p_X(x) & \text{CASO DISCRETO} \\ \int_{-\infty}^{\infty} x \, f_X(x) \, dx & \text{CASO CONTINUO} \end{cases}
$$

* **Nota**: similarità con $\bar{x}$ della STAT. DESCRITTIVA

---

### ES 4.2

Commesso viaggiatore, 2 appuntamenti (INDIP.):
* 1° appuntamento: guadagno $1000 \text{ dollari}$ prob. $70\%$
* 2° appuntamento: guadagno $1500 \text{ dollari}$ prob. $40\%$

$$
X = \text{guadagno, v.c.}
$$

| $x$ | $p_X(x)$ |
| :--- | :--- |
| $0$ | $0.18$ |
| $1000$ | $0.42$ |
| $1500$ | $0.12$ |
| $2500$ | $0.28$ |
| | **$1$** |

$$
E(X) = 1300 \text{ dollari}
$$

$$
\downarrow
$$

$$
\text{GUADAGNO ATTESO}
$$

<!-- ===== PAGINA 2 ===== -->

<!-- Pagina 2 -->

# ES 4.3 <span style="float: right; border: 1px solid red; border-radius: 50%; padding: 2px 8px; color: red;">2</span>

$X = \text{tempo vita dispositivo}$

$$
f_X(x) = \begin{cases} \frac{20000}{x^3}, & x > 100 \\ 0, & \text{altrove} \end{cases}
$$

$$
\left( \int_{100}^{\infty} \frac{20000}{x^3} \, dx = 20000 \cdot \left(-\frac{1}{2}\right) \left. \left(x^{-2}\right) \right|_{100}^{\infty} = 1 \right)
$$

$$
E(X) = \int_{100}^{\infty} x \frac{20000}{x^3} \, dx = 200 \text{ ore}, \quad \text{DURATA MEDIA}
$$

---

### PROPOSIZIONE

$$
E[g(X)] = \begin{cases} \sum_{x} g(x) P_X(x) & \text{CASO DISCR.} \\ \int_{-\infty}^{\infty} g(x) f_X(x) \, dx & \text{CASO CONT.} \end{cases}
$$

**Nota:** che $Y = g(X)$ sia V.C. è immediato dalla definizione di V.C.; il risultato ci permette di evitare di dover calcolare la distribuzione di $Y$ per calcolare $E(Y)$. Deriva dalle proprietà di sommatorie e integrali.

<!-- ===== PAGINA 3 ===== -->

<!-- Pagina 3 -->

(3)

* Si estende a funzioni di $2$ (o più) v.c.:

$$
E\left[ g(X,Y) \right] = \begin{cases} \sum_{x} \sum_{y} g(x,y) p_{XY}(x,y) & \text{CASO DISCRETO} \\ \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x,y) f_{XY}(x,y) dx dy & \text{CASO CONTINUO} \end{cases}
$$

Il caso speciale $g(X,Y) = X$ o $g(X,Y) = Y$ sono immediati:

$$
E(X) = \sum_{x} \sum_{y} x \, p_{XY}(x,y) = \sum_{x} x \underbrace{\sum_{y} p_{XY}(x,y)}_{p_X(x)}
$$

$$
\uparrow
$$

$$
\text{CASO DISCRETO (PER ESEMPIO)}
$$

---

### ESERCIZIO 4.3

$C = \text{costo per giocare}$  
$Y = \text{vincita netta}$

* vinco $3 \text{ dollari}$ con Jack o Regina
* vinco $5 \text{ dollari}$ con Asso o Re

| $y$ | $p_Y(y)$ |
| :---: | :---: |
| $0 - C$ | $36/52$ |
| $3 - C$ | $8/52$ |
| $5 - C$ | $8/52$ |
| | **1** |

<br>

$C$ per gioco EQUO?  

$$
E(Y) = 0
$$

<!-- ===== PAGINA 4 ===== -->

<!-- Pagina 4 -->

$$
E(Y) = (0 - c) \frac{36}{52} + (3 - c) \frac{8}{52} + (5 - c) \frac{8}{52}
$$

*(Nota: sopra il termine $(5-c)$ è presente un "4" cerchiato in rosso)*

$$
= \frac{16}{13} - c \implies c = \frac{16}{13} = 1.23 \text{ dollari}
$$

---

### ESER. 4.5

Rimborso max $200\,000 \text{ dollari}$ per assicurazione aereo

$$
P(\text{perdita totale}) = 0.002
$$

$$
P(\text{perdita } 50\%) = 0.01
$$

$$
P(\text{perdita } 25\%) = 0.1
$$

Premio per profitto medio $500 \text{ dollari}$?

$$
X = \text{Rimborso}
$$

| $x$ | $p_X(x)$ |
| :---: | :---: |
| $200\,000$ | $0.002$ |
| $100\,000$ | $0.01$ |
| $50\,000$ | $0.1$ |
| $0$ | $0.888$ |
| | **$1$** |

$$
E(X) = 6400 \text{ dollari}
$$

$$
\text{premio} = 6400 \text{ dollari} + 500 \text{ dollari}
$$

$$
\Downarrow
$$

$$
6900 \text{ dollari}
$$

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

$$
1. \quad E(X Y^2) = \sum_x \sum_y x y^2 p_{XY}(x,y) = 35.2
$$

$$
2. \quad \mu_X = 2 (0.40) + 4 (0.60) = 3.2
$$

$$
\mu_Y = 1 (0.25) + 3 (0.50) + 5 (0.25) = 3.0
$$

---

# ES 4.14

$$
f_X(x) = \begin{cases} \frac{1}{2000} e^{-\frac{x}{2000}} & x > 0 \\ 0 & x \le 0 \end{cases}
$$

*(DENSITÀ ESPONENZIALE)*

$$
E(X) = \frac{1}{2000} \int_{0}^{\infty} x e^{-x/2000} \, dx
$$

$$
\text{PONGO} \quad z = \frac{x}{2000} \implies \begin{aligned} x &= z \cdot 2000 \\ dx &= dz \cdot 2000 \end{aligned}
$$

$$
= 2000 \int_{0}^{\infty} z e^{-z} \, dz = 2000 \cdot 1
$$

$$
\int_{0}^{\infty} z e^{-z} \, dz \underset{\text{PER PARTI}}{=} \left[ \left(-e^{-z}\right) z \right]_{0}^{\infty} + \int_{0}^{\infty} e^{-z} \, dz = 1
$$

*(Nota: il termine $\left[ \left(-e^{-z}\right) z \right]_{0}^{\infty}$ tende a $0$)*

<!-- ===== PAGINA 6 ===== -->

<!-- Pagina 6 -->

# III) VARIANZA E COVARIANZA <span style="float: right;">1</span>

**Def** $V(X)$ è la VARIANZA di $X$ (o della sua distribuzione):

$$
\sigma^2_X = V(X) = E\left[(X-\mu_X)^2\right] = \begin{cases} \sum_{x} (x-\mu_X)^2 p_X(x) & \text{CASO DISCRETO} \\ \int_{-\infty}^{\infty} (x-\mu_X)^2 f_X(x) \, dx & \text{CASO CONTINUO} \end{cases}
$$

$$
\rightarrow \text{Misura la VARIABILITÀ di } X
$$

* $\sigma_X = \sqrt{V(X)}$ è la DEVIAZIONE STANDARD di $X$
* Nota: FORMULA DI CALCOLO (analoga a quella vista nella statistica descrittiva)

$$
E\left[(X-\mu_X)^2\right] = E(X^2) - \mu_X^2
$$

**Prova**: (CASO CONTINUO, CASO DISCRETO È ANALOGO)

$$
V(X) = \int_{-\infty}^{\infty} \left(x^2 + \mu_X^2 - 2x\mu_X\right) f_X(x) \, dx
$$

$$
= \int_{-\infty}^{\infty} x^2 f_X(x) \, dx + \mu_X^2 \underbrace{\int_{-\infty}^{\infty} f_X(x) \, dx}_{1} - 2\mu_X \underbrace{\int_{-\infty}^{\infty} x f_X(x) \, dx}_{\mu_X}
$$

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

$$
\sum_{x} \left[ g(x) - \mu_{g(x)} \right]^2 p_X(x)
$$

* **Caso continuo:**

$$
\int_{-\infty}^{\infty} \left( g(x) - \mu_{g(x)} \right)^2 f_X(x) dx
$$

> **[Nota]** è l'applicazione di un risultato visto per il valore atteso

---

## Def COVARIANZA TRA $X$ e $Y$

$$
\sigma_{XY} = \text{cov}(X,Y) = E\left[ (X - \mu_X)(Y - \mu_Y) \right]
$$

Misura il grado della RELAZIONE LINEARE tra $X$ e $Y$

---

### Prop

$$
\text{cov}(X,Y) = E(X \cdot Y) - E(X)E(Y)
$$

<!-- ===== PAGINA 8 ===== -->

<!-- Pagina 8 -->

<div style="text-align: right; color: red; font-size: 1.5em; font-weight: bold;">3</div>

Di nuovo, possiamo considerare il caso continuo o quello discreto, i passaggi sono gli stessi. Qui prendiamo il caso discreto

$$
Cov(X,Y) = \sum_{x} \sum_{y} (x - \mu_X)(y - \mu_Y) p_{XY}(x,y)
$$

$$
= \sum_{x} \sum_{y} x y p_{XY}(x,y) - \mu_X \sum_{x} \sum_{y} y p_{XY}(x,y) - \mu_Y \sum_{x} x \sum_{y} p_{XY}(x,y) + \mu_X \cdot \mu_Y \sum_{x} \sum_{y} p_{XY}(x,y)
$$

$$
= \sum_{x} \sum_{y} x y p_{XY}(x,y) - 2\mu_X \cdot \mu_Y + \mu_X \cdot \mu_Y
$$

---

### Def COEFFICIENTE DI CORRELAZIONE TRA $X$ e $Y$

$$
\rho_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y} , \quad -1 \le \rho_{XY} \le 1
$$

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

$$
E(XY) = \sum_{x} \sum_{y} x y P_{XY}(x,y) = 1 \cdot 1 \cdot \frac{6}{28} = \frac{3}{14}
$$

$$
E(X) = 3/4 \qquad E(Y) = 1/2
$$

$$
\text{cov}(X,Y) = \frac{3}{14} - \frac{3}{4} \cdot \frac{1}{2} = -\frac{9}{56}
$$

$$
V(X) = \frac{45}{112} \qquad V(Y) = \frac{9}{28} \qquad \rho_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y} = -0.447
$$

<!-- ===== PAGINA 10 ===== -->

<!-- Pagina 10 -->

(5)

# PROPOSIZIONE

Se $X$ e $Y$ sono v.c. INDIPENDENTI $\Rightarrow \rho_{XY} = 0$

## Prova

$$
E(X \cdot Y) \underset{\text{CASO DISCRETO}}{=} \sum_{x} \sum_{y} x \cdot y \cdot p_{XY}(x, y)
$$

$$
= \left( \sum_{x} x \cdot p_X(x) \right) \left( \sum_{y} y \cdot p_Y(y) \right)
$$

$$
= E(X) E(Y) \Rightarrow Cov(X, Y) = 0
$$

---

### NOTA:
Non vale il viceversa, come mostra l'esempio che segue

| $Y \backslash X$ | $-1$ | $0$ | $1$ |
| :---: | :---: | :---: | :---: |
| **$0$** | $0$ | $0.5$ | $0$ |
| **$1$** | $0.25$ | $0$ | $0.25$ |

$p_{XY}(x,y)$ per $X$ e $Y$ discrete

Si trova facilmente $\rho_{XY} = 0$, ma le due v.c. non sono indipendenti!

$$
(\text{Infatti } Y = |X|)
$$

<!-- ===== PAGINA 11 ===== -->

<!-- Pagina 11 -->

### III) COMBINAZIONE LINEARE DI V.C. ①

#### Risultati notevoli:

##### RIS 1

$$
a, b \in \mathbb{R} \quad ; \quad E(aX+b) = a E(X) + b
$$

$$
X \text{ v.c.}
$$

**Prova:** (per $X$, ad es., discreta)

$$
E(aX+b) \overset{\text{da risultato visto}}{=} \sum_{x} (ax+b) p_X(x)
$$

$$
= a \sum_{x} x p_X(x) + b \sum_{x} p_X(x)
$$

$$
= a E(X) + b
$$

---

##### RIS 2
Siano $h$ e $g$ due funzioni $\mathbb{R} \to \mathbb{R}$

$$
E[g(X) + h(X)] = E[g(X)] + E[h(X)]
$$

**Prova:** si lascia per esercizio (è analoga al caso precedente)

<!-- ===== PAGINA 12 ===== -->

<!-- Pagina 12 -->

<u>RIS 3</u> &emsp; $a, b \in \mathbb{R}$ &emsp; $X, Y$ v.c. &emsp;&emsp;&emsp;&emsp; **(2)**

$aX + bY$ è una COMBINAZIONE LINEARE delle due variabili con pesi $a$ e $b$

$$
E(aX + bY) = a E(X) + b E(Y)
$$

**Prova:** (caso discreto)

$$
E(aX + bY) = \sum_{x} \sum_{y} (ax + by) p_{XY}(x,y)
$$

$$
= a \sum_{x} \sum_{y} x p_{XY}(x,y) \quad +
$$

$$
b \sum_{x} \sum_{y} y p_{XY}(x,y)
$$

> **[Nota Grafica: Una linea diagonale collega il termine $(ax+by)$ della prima equazione al coefficiente $a$ della riga successiva. Una linea verticale a sinistra raggruppa i due addendi con coefficienti $a$ e $b$ per confluire nel risultato finale]**

$$
= a E(X) + b E(Y)
$$

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

$$
E\left[ g(X,Y) + h(X,Y) \right] = E\left[ g(X,Y) \right] + E\left[ h(X,Y) \right]
$$

Prova: si lascia per esercizio

---

### RIS 5

$X_1, X_2, \dots, X_n$ v.c.  
$a_1, a_2, \dots, a_n \in \mathbb{R}$

$$
Y = \sum_{i=1}^{n} a_i X_i
$$

> **COMBINAZIONE LINEARE** delle $n$ v.c. con pesi $a_1, a_2, \dots, a_n$

$$
E(Y) = \sum_{i=1}^{n} a_i E(X_i)
$$

Prova: segue da RIS 3 per INDUZIONE

---

### RIS 6

$a, b \in \mathbb{R}$ , $X$ v.c.

$$
V(aX + b) = a^2 V(X)
$$

<!-- ===== PAGINA 14 ===== -->

<!-- Pagina 14 -->

```markdown
Prova: $V(\underbrace{aX+b}_{Y}) = E \left[ (Y - \mu_Y)^2 \right]$  ④

$$
= E \left[ (aX + b - a\mu_X - b)^2 \right]
$$

$$
\stackrel{!}{=} E \left[ a^2(X - \mu_X)^2 \right] = a^2 V(X)
$$

---

### RIS 7
$a, b \in \mathbb{R}$, $X, Y$ v.c.

$$
V(aX + bY) = a^2 V(X) + b^2 V(Y) + 2ab \operatorname{cov}(X, Y)
$$

**Prova:**

$$
V(aX + bY) = E \left\{ \left[ (aX + bY) - (a\mu_X + b\mu_Y) \right]^2 \right\}
$$

$$
= E \left\{ \left[ a(X - \mu_X) + b(Y - \mu_Y) \right]^2 \right\}
$$

$$
= E \left\{ a^2(X - \mu_X)^2 + b^2(Y - \mu_Y)^2 + 2ab(X - \mu_X)(Y - \mu_Y) \right\} = \longrightarrow \text{applico RIS 5}
$$

$$
= a^2 E \left[ (X - \mu_X)^2 \right] + b^2 E \left[ (Y - \mu_Y)^2 \right] + 2ab \cdot E \left[ (X - \mu_X)(Y - \mu_Y) \right] \text{, ovvero il risultato}
$$

```

<!-- ===== PAGINA 15 ===== -->

<!-- Pagina 15 -->

(5)

## RIS 8

Se $X$ e $Y$ sono INDIPENDENTI

$$
V(a X + b Y) = a^2 V(X) + b^2 V(Y)
$$

si estende a $n$ v.c. INDIPENDENTI

$$
V\left( \sum_{i=1}^{n} a_i X_i \right) = \sum_{i=1}^{n} a_i^2 V(X_i)
$$

---

### CASO NOTEVOLE di COMB. LINEARE

**Def** Date $X_1, \dots, X_n$ v.c.,

$$
\overline{X} = \frac{1}{n} \sum_{i=1}^{n} X_i \quad \text{è la v.c. MEDIA CAMPIONARIA}
$$

**Nota:** la notazione usata coincide, non a caso, con l'analoga definizione vista in statistica descrittiva. Eseguito l'esperimento, e osservati i valori $x_1, x_2, \dots, x_n$, allora posso calcolare

$$
\overline{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

<!-- ===== PAGINA 16 ===== -->

<!-- Pagina 16 -->

(6)

* Proprietà di $\overline{X}$: ci interessa soprattutto il caso di $n$ v.c. **i. i. d.** ovvero INDIPENDENTI e IDENTICAMENTE DISTRIBUITE.

Se la distribuzione è la stessa per tutte le v.c., allora hanno tutte la stessa media e varianza:

$$
E(X_1) = E(X_2) = \dots = E(X_n) = \mu
$$

$$
V(X_1) = V(X_2) = \dots = V(X_n) = \sigma^2
$$

si ha (da risultati precedenti)

$$
E(\overline{X}) = \mu
$$

$$
V(\overline{X}) = \frac{\sigma^2}{n}
$$

<!-- ===== PAGINA 17 ===== -->

<!-- Pagina 17 -->

(7)

## VALORE ATTESO CONDIZIONATO

* È la media della v.c. basata sulla distribuzione condizionata

$$
E(Y|X=x) = \begin{cases} \sum_{y} y \, p_{Y|X}(y|x), & \text{CASO DISCRETO} \\ \\ \int_{-\infty}^{\infty} y \, f_{Y|X}(y|x) \, dy, & \begin{matrix} \text{CASO} \\ \text{CONTINUO} \end{matrix} \end{cases}
$$

* Interpretazione: è una sintesi della distribuzione di $Y$ quando $X=x$

* Analogamente definiamo la VARIANZA CONDIZIONATA

$$
V(Y|X=x)
$$

* Nota: $E(Y|X=x)$ e $V(Y|X=x)$ dipendono dal valore di $x$!

  Se $X$ e $Y$ sono <u>indipendenti</u>
  
$$
E(Y|X=x) = E(Y) \quad \text{e} \quad V(Y|X=x) = V(Y)
$$

<!-- ===== PAGINA 18 ===== -->

<!-- Pagina 18 -->

# III) DISTRIBUZIONI DI PROBABILITÀ NOTEVOLI (DISCRETE) ①

* Alcuni tipi di V.C. ricorrono spesso nella pratica $\Rightarrow$ MODELLI DI RIFERIMENTO
* Distribuzioni di probabilità DISCRETE o CONTINUE che dipendono da alcuni PARAMETRI $\vartheta = (\vartheta_1, \vartheta_2, \dots, \vartheta_p)$

$$
p_X(x; \vartheta) \quad \text{caso discreto}
$$

$$
f_X(x; \vartheta) \quad \text{caso continuo}
$$

---

## ① DISTRIBUZIONE di BERNOULLI

Esperimento con $2$ possibili risultati,

$$
\begin{array}{ccc} \text{"SUCCESSO"} & \text{o} & \text{"INSUCCESSO"} \\ 1 & & 0 \end{array}
$$

$$
P(\text{SUCCESSO}) = p \qquad P(\text{INSUCCESSO}) = 1 - p
$$

$$
p, \quad 0 < p < 1 \quad \text{è il PARAMETRO}
$$

<!-- ===== PAGINA 19 ===== -->

<!-- Pagina 19 -->

(2)

$$
X = \begin{cases} 1 & \text{SUCCESSO} \\ 0 & \text{INSUCCESSO} \end{cases}
$$

> **[Nota Grafico: Una freccia con la dicitura "su distribuzione" collega la definizione di $X$ alla tabella sottostante]**

| $x$ | $P_X(x; p)$ |
| :---: | :---: |
| $0$ | $1 - p$ |
| $1$ | $p$ |

$$
\begin{aligned}
P(X=1) &= p \\
P(X=0) &= 1-p
\end{aligned}
$$

---

$$
E(X) = p
$$

$$
V(X) = p(1-p)
$$

---

In forma compatta: 

$$
p_X(x; p) = p^x (1-p)^{1-x}, \quad x = 0, 1
$$

Notazione:

$$
X \sim \text{Bernoulli}(p)
$$

ES: LANCIO MONETA, $\text{SUCCESSO} \Rightarrow \text{esce testa}$

$$
X \sim \text{Bernoulli}(0.5)
$$

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

$$
X = \text{n}^\circ \text{ SUCCESSI nelle } n \text{ prove}
$$

$$
X \sim \text{Bi}(n, p) \qquad x = 0, 1, \dots, n
$$

$$
0 < p < 1
$$

> **[Nota Grafico: Una freccia rossa punta dalla formula $X \sim \text{Bi}(n, p)$ a un riquadro rosso contenente la scritta "DISTRIBUZIONE BINOMIALE"]**

---

**ES:** Lancio $3$ volte un dado, $\text{successo} \Rightarrow \text{esce } 6$

$$
X = \text{n}^\circ \text{ di } 6 \text{ nelle } 3 \text{ prove}
$$

$$
X \sim \text{Bi}(3, 1/6)
$$

<!-- ===== PAGINA 21 ===== -->

<!-- Pagina 21 -->

(4)

otteniamo la distribuzione: defini-
per prima cosa gli eventi

$$
A_i = \{ \text{Esce 6 alla } i-\text{esima prova} \}
$$

$$
i = 1, 2, 3
$$

$$
A_1, A_2, A_3 \quad \text{MUTUAMENTE INDIPENDENTI}
$$

$$
P(X=0) = P\left(A_1^c \cap A_2^c \cap A_3^c\right)
$$

$$
= P\left(A_1^c\right) P\left(A_2^c\right) P\left(A_3^c\right) = \left(\frac{5}{6}\right)^3
$$

$$
P(X=1) = P\left(A_1^c \cap A_2^c \cap A_3\right) + P\left(A_1^c \cap A_2 \cap A_3^c\right)
$$

$$
+ P\left(A_1 \cap A_2^c \cap A_3^c\right) = 3 \left(\frac{1}{6}\right)^1 \left(\frac{5}{6}\right)^2
$$

$$
P(X=2) = 3 \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^1
$$

$$
P(X=3) = \left(\frac{1}{6}\right)^3
$$

In generale: per $X \sim B_i(n,p)$

$$
\boxed{P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x=0, 1, \dots, n}
$$

<!-- ===== PAGINA 22 ===== -->

<!-- Pagina 22 -->

(5)

* Il testo di Walpole et al. usa una simbologia particolare per $p_X(x; p)$, ovvero

$$
b(x; n, p) = \binom{n}{x} p^x (1-p)^{n-x}
$$

Proprietà:

i) Posto $q = 1-p$ si ha

$$
\underbrace{(p+q)^n}_{1} = \sum_{x=0}^n \binom{n}{x} p^x (1-p)^{n-x} = 1
$$

$$
\quad \text{formula di Newton}}}}}}}}}}}}}
$$

a riprova che la distribuzione è ben definita.

ii) MEDIA e VARIANZA

$$
Z_i = \begin{cases} 1 & \text{successo } i\text{-esima prova} \\ 0 & \text{insuccesso } \text{" } \quad \text{"} \end{cases}
$$

$$
Z_i \sim \text{Bernoull}(p) \quad i = 1, \dots, n
$$

v.c. indipendenti

<!-- ===== PAGINA 23 ===== -->

<!-- Pagina 23 -->

(6)

$$
X = Z_1 + Z_2 + \dots + Z_n
$$

Dai risultati sulle combinazioni lineari:

$$
E(X) = E\left(\sum_{i=1}^{n} Z_i\right) = \sum_{i=1}^{n} E(Z_i) = np
$$

$$
V(X) = V\left(\sum_{i=1}^{n} Z_i\right) = \sum_{i=1}^{n} V(Z_i) = np(1-p)
$$

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

$$
X = n^\circ \text{ di successi nelle } n \text{ prove}
$$

$$
X \sim H(N, n, K) \quad \text{DISTRIBUZIONE IPERGEOMETRICA}
$$

$$
P(X=x) = \frac{\binom{K}{x} \binom{N-K}{n-x}}{\binom{N}{n}} = h(x; N, n, K)
$$

$\downarrow$
METODO DEL CONTEGGIO

Supporto:

$$
\begin{cases}
0 \le x \le n \\
n - (N-K) \le x \le K
\end{cases}
$$

$\hookrightarrow \max(0, n - (N-K)) \le x \le \min(n, K)$

<!-- ===== PAGINA 25 ===== -->

<!-- Pagina 25 -->

- ES: 10 oggetti, 3 difettosi, 7 non difettosi

$$
N = 10 \quad , \quad k = 7 \quad , \quad X = n^\circ \text{ di non difettosi}
$$

Supporto: se $\begin{cases} n = 4 & 1 \le x \le 4 \\ n = 8 & 5 \le x \le 7 \\ n = 3 & 0 \le x \le 3 \end{cases}$

Nota: se $k \ge n \quad \text{e} \quad N-k \ge n \implies 0 \le x \le n$

- PROPOSIZIONE

$$
E(X) = n \frac{k}{N} = n p \quad \text{se pongo } p = \frac{k}{N}
$$

$$
V(X) = n \frac{k}{N} \left(1 - \frac{k}{N}\right) \frac{N-n}{N-1}
$$

$$
= n \ p \ (1-p) \frac{N-n}{N-1}
$$

Prova: (pura algebra, la prendiamo per buona)

<!-- ===== PAGINA 26 ===== -->

<!-- Pagina 26 -->

Confronto con la binomiale: (3)

- Se estraggo con reinserimento $X \sim Bi(n,p)$
- " " senza " " e $n \le 0.05 N$

$$
H(N, n, K) \approx Bi\left(n, \frac{K}{N}\right)
$$

Ma se $n$ è piccolo in confronto a $N$ posso agire come se le estrazioni avvengano con reinserimento!

- La distribuzione ipergeometrica si estende a più di 2 categorie, ma è poco usata.

- UTILIZZO DELLA DISTRIBUZIONE IPERGEOMETRICA NEL CAMPIONAMENTO PER ACCETTAZIONE

Esercizio 5.18

- Lotto $N = 50$, ne campiono $n = 5$ e accetto il lotto se al max 2 sono difettosi

<!-- ===== PAGINA 27 ===== -->

<!-- Pagina 27 -->

(4)

Proporzione di lotti con il $20\%$ che saranno accettati?

$$
K = 10 \qquad X = n^\circ \text{ difettosi } n \ 5
$$

$$
X \sim H(50, 5, 10), \quad 0 \le x \le 5
$$

$$
P(X \le 2) = \sum_{x=0}^{2} \frac{\binom{10}{x}\binom{40}{5-x}}{\binom{50}{5}} = 0.9517
$$

- Se uso $X \sim \text{Bi } (5, 0.2), \quad P(X \le 2) = 0.9421$

- Esercizio 3.6

$$
N = 7 \qquad K = 2 \text{ difettosi} \qquad n = 3
$$

$$
X = n^\circ \text{ difettosi} \qquad X \sim H(7, 3, 2)
$$

$$
x = 0, 1, 2
$$

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

$$
P(X=x) = \binom{N}{x} p^x (1-p)^{N-x}
$$

$$
= \binom{N}{x} \left(\frac{\lambda}{N}\right)^x \left(1-\frac{\lambda}{N}\right)^{N-x}
$$

Assumiamo che $\begin{cases} N \to \infty \\ p \to 0 \end{cases}$ e $\lambda \to \text{costante}$

e calcoliamo il limite di $P(X=x)$:

<!-- ===== PAGINA 29 ===== -->

<!-- Pagina 29 -->

$$
\lim_{N \to \infty} P(X = n) = \lim_{N \to \infty} \underbrace{\frac{N!}{(N-n)! n!} \cdot \frac{\lambda^n}{N^n}}_{\to 1} \cdot \underbrace{\left(1 - \frac{\lambda}{N}\right)^N}_{\to e^{-\lambda}} \underbrace{\left(1 - \frac{\lambda}{N}\right)^{-n}}_{\to 1}
$$

ovvero

$$
\lim_{N \to \infty} P(X = n) = \frac{\lambda^n e^{-\lambda}}{n!}
$$

$$
n = 0, 1, \dots
$$

- Il risultato giustifica la seguente definizione:

<u>Def</u> $X$ v.c. di Poisson, con supporto $n = 0, 1, 2, \dots$

$$
\Big[ P(X = n) = e^{-\lambda} \frac{\lambda^n}{n!}
$$

Commenti:
- È approssimazione della binomiale per $n$ elevato, $p$ piccolo e $\lambda = np$ costante
- Va bene per conteggi senza limite superiore

<!-- ===== PAGINA 30 ===== -->

<!-- Pagina 30 -->

### Proprietà:

$$
\begin{cases} E(X) = \lambda \\ V(X) = \lambda \end{cases} \quad \begin{minipage}{0.4\textwidth}Segue da proprietà delle serie, ma anche dalla approssimazione binomiale\end{minipage}
$$

---

## 1 PROCESSO DI POISSON (omogeneo)

1. ARRIVI indipendenti nel tempo o nello spazio
2. Non ci sono arrivi simultanei
3. $\lambda$ tasso di arrivi medio in una unità di tempo (è lo stesso per tutte le unità) [spazio]

$X = n^\circ$ arrivi in $t$ unità di tempo (spazio)

$$
1 + 2 + 3 \implies X \sim \text{Poisson}(\lambda t)
$$

$$
\left(\text{o anche si indica } \mathcal{P}(\lambda t)\right)
$$

* **ES:** Accessi sito web (in un intervallo di tempo)
$\lambda = 5$ accessi al minuto

$$
P(17 \text{ accessi in } 3 \text{ minuti}) = e^{-15} \frac{15^{17}}{17!} = 0.0847
$$

