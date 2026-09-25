---
fonte: "Esercizi_scelti.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Esercizi scelti

                                        24 ottobre 2025


Contents
1 Funzioni e serie                                                                                   2
  1.1 Successioni . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      2
  1.2 Serie di funzioni . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    3
  1.3 Serie di Fourier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     6

2 Equazioni differenziali                                                                        8
  2.1 Equazioni differenziali del primo ordine . . . . . . . . . . . . . . . . . . . . . . . 8
  2.2 Analisi Qualitativa delle soluzioni . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
  2.3 Equazioni del Secondo Ordine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

3 Differenziabilità                                                                                15

4 Teorema del Dini                                                                                  15

5 Ottimizzazione                                                                                16
  5.1 Ottimizzazione libera . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
  5.2 Ottimizzazione vincolata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

6 Integrali multipli                                                                                21

7 Campi vettoriali                                                                                  25

    Quella che segue è una selezione di esercizi presi dal libro consigliato o dalle slide presentate
a lezione. L’indicazione [CP 2.2] significa Esercizio n 2.2 del testo [CP] dove
[CP] = Catino, Punzo - Esercizi svolti di Analisi Matematica e Geometria 2 - Esculapio (2020)
[S5] = Slide presentate a lezione sulle successioni di funzioni
[S6] = Slide presentate a lezione sulle serie di funzioni
[S7] = Slide presentate a lezione sulle serie di potenze
[S9] = Slide presentate a lezione sulle serie di Fourier
[S10] = Slide presentate a lezione sulle ODE
[S11] = Slide presentate a lezione sulle ODE lineari
[S09F] = Slide presentate a lezione sui massimi e minimi (Prof. Freddi)
[S13F] = Slide presentate a lezione sui massimi e minimi vincolati (Prof. Freddi)
[S16F] = Slide presentate a lezione sui campi vettoriali (Prof. Freddi)
[S17F] = Slide presentate a lezione sugli integrali multipli (Prof. Freddi)




                                                  1
1     Funzioni e serie
1.1    Successioni
Esercizio 1 [S5 1.2]. Determinare tutti e soli gli α > 0 tali che la successione di funzioni
                             x
fn : [0, ∞) → R, fn (x) = α        converge uniformemente su [0, ∞).
                          x + nα
Esercizio 2 [S5 1.3]. Determinare gli intervalli di R su cui la successioni di funzioni

                                                       x2n
                                   fn (x) = n arctan
                                                        n
converge puntualmente; determinare quindi gli intervalli di R su cui c’è convergenza
uniforme.
Esercizio 3 [CP 2.2]. Studiare la convergenza puntuale e uniforme nell’intervallo [0, 1]
della successione
                                             n2 x
                                  fn (x) =
                                           1 + n 2 x2
Esercizio 4 [CP 2.3]. Studiare la convergenza puntuale ed uniforme, sia in tutto R che
in ogni intervallo limitato I = [0, a], della successione di funzioni

                                                x2
                                     fn (x) = 2
                                             n + x2
Esercizio 5 [CP 2.4]. Studiare la convergenza puntuale ed uniforme, sia in tutto R che
in ogni intervallo limitato, della successione di funzioni
                                         (
                                           2, en ≤ x < en+1
                                fn (x) =
                                           0, altrimenti

Esercizio 6 [CP 2.5]. Studiare, al variare del parametro α > 0, la convergenza puntuale
ed uniforme nell’intervallo [0, 1], della successione di funzioni
                                    
                                         α
                                    xn ,
                                                  0 ≤ x ≤ 1/n
                                       2       α
                         fn (x) = ( n − x)n , 1/n < x ≤ 2/n
                                                   2
                                      0,              <x≤1
                                    
                                                    n

Esercizio 7 [CP 2.6]. Studiare, al variare del parametro α > 0, la convergenza puntuale
ed uniforme in ogni intervallo [0, a] con a > 0, della successione di funzioni

                                     fn (x) = xnα e−nx

Esercizio 8 [CP 2.12]. Studiare la convergenza puntuale ed uniforme in [1, +∞], in
[1, 2] e in [2, +∞) della successione di funzioni

                                  fn (x) = 2n(x − 1)x−n

Esercizio 9 [CP 2.13]. Studiare la convergenza puntuale e uniforme in [0, 2] della suc-
cessione di funzioni
                                             nx
                                 fn (x) =
                                          3 + n 4 x4

                                             2
Esercizio 10 [CP 2.14]. Studiare la convergenza puntuale ed uniforme in R della suc-
cessione di funzioni
                                    n cos(x2 + 1) + n2 x
                           fn (x) =
                                         n 2 x2 + n 2
Esercizio 11 [CP 2.16]. Sia
                                                      n
                                   fn (x) = arctan
                                                        x
Determinare l’insieme di convergenza puntuale della successione di funzioni {fn }, la fun-
zione limite f (x) e in quali intervalli la convergenza è uniforme.

Esercizio 12 [CP 2.17]. Sia

                                                n2 x2 + nx
                                    fn (x) =
                                                 x2 + n 2
Determinare l’insieme di convergenza puntuale della successione di funzioni {fn }, la fun-
zione limite f (x) e in quali intervalli la convergenza è uniforme.

1.2    Serie di funzioni
Esercizio 13 [S6]. Studiare la convergenza puntuale, uniforme e totale della serie
                                   ∞
                                   X      x2n
                                                , x ∈ R.
                                    n=1
                                        1 + x2n

Esercizio 14 [CP 2.18]. Trovare gli insiemi di convergenza uniforme e totale della serie
                                      +∞     √
                                      X  cos( nx) + 1
                                      n=1
                                            log(n)n2
                                                                               P       (−1)n n2   x−2 n
                                                                                                      
Esercizio 15 [S7 6]. Studiare la convergenza puntuale e uniforme della serie       n    n4 +2     x+5
                                                                                                        .

Esercizio 16 [S7 7(a)]. Studiare la convergenza puntuale ed uniforme della serie
                                       X      3n x2n
                                       n≥0
                                           2 (x2 + 1)n

calcolarne la somma, ove possibile.

Esercizio 17 [S7 9]. Studiare la convergenza puntuale della serie
                                   X 2n−1
                                                (arctan x)n
                                    n≥1
                                        π n−1

e calcolarne la somma puntuale, ove possibile.
    Caratterizzare inoltre gli intervalli di R su cui la serie data converge totalmente/uniformemente.




                                                3
Esercizio 18 [CP 2.19]. Sia
                                                                     
                                         x                  |x| + n
                             fn (x) =          log
                                      1 + n|x|                 n
Determinare l’insieme di convergenza puntuale e l’insieme di convergenza uniforme della
serie di funzioni
                                      +∞
                                      X
                                          fn (x)
                                         n=1

Esercizio 19 [CP 2.20]. Si consideri la serie di funzioni
                                           +∞
                                           X
                                                 enx
                                           n=1

Si determini l’insieme di convergenza puntuale, la somma della serie e in quali intervalli
la convergenza è uniforme.
Esercizio 20 [CP 2.21]. Studiare la convergenza puntuale, uniforme e totale della serie
                                +∞
                                X  n! arctan((n2 + 1)x)
                                n=1
                                                   nn

Esercizio 21 [CP 2.22]. Studiare la convergenza puntuale, uniforme e totale della serie
                                       +∞
                                       X
                                              cos(x)n
                                        n=1

nell’insieme [π/4, π/2].
Esercizio 22 [CP 2.25]. Studiare la convergenza puntuale e totale, in [0, +∞) e in
[a, +∞) per ogni a > 0, della serie di funzioni
                                        +∞
                                        X
                                              xe−2nx
                                        n=1

Esercizio 23 [CP 2.27]. Studiare la convergenza puntuale e totale della serie di funzioni
                                      +∞
                                      X       x
                                      n=1
                                          n(1 + nx2 )

Esercizio 24 [CP 2.28]. Sia fn (x) = cos( nx ) per x ∈ [−π, π]. Determinare le regioni di
convergenza puntuale ed uniforme delle serie
                                        +∞
                                        X
                                               fn (x)
                                         n=1

Esercizio 25 [CP 2.29]. Studiare la convergenza puntuale ed uniforme della serie
                                    +∞         √
                                    X    3n + n n
                                                    x
                                    n=1
                                        5n + log(n)

                                               4
Esercizio 26 [CP 2.30]. Studiare la convergenza puntuale ed uniforme della serie
                                           +∞
                                           X  5n
                                                       xn
                                            n=1
                                                  2n

Esercizio 27 [CP 2.31]. Determinare l’insieme di convergenza della serie
                                       +∞
                                       X  n+1
                                                        xn
                                       n=1
                                                  2n

(i) Si discuta inoltre il tipo di convergenza. (ii) Si integri la serie termine a termine e
si calcoli la somma della serie ottenuta. (iii) Si deduca infine la somma della serie di
partenza.

Esercizio 28 [CP 2.32]. Determinare l’insieme di convergenza semplice e uniforme
della serie                        √
                            +∞
                           X    n+ n+1
                                    n n)2
                                           (x − 4)n
                            n=1
                                 (2

Esercizio 29 [CP 2.33]. Si studi la convergenza puntuale ed uniforme della serie
                                       +∞
                                       X  (−2)n
                                                        xn
                                       n=1
                                                  n

Esercizio 30 [CP 2.37]. Calcolare la somma della serie
                                     +∞
                                     X  (−1)n x3n+4
                                      n=1
                                                  n+1

stabilendo il tipo di convergenza.

Esercizio 31 [CP 2.38]. Calcolare la somma della serie
                                     +∞
                                     X      1
                                                  x3n−1
                                     n=1
                                         (n − 1)!

stabilendo il tipo di convergenza.

Esercizio 32 [CP 2.39]. Calcolare la somma della serie
                                     +∞
                                     X
                                        (−1)n nx2n−1
                                     n=1

stabilendo il tipo di convergenza.




                                                  5
1.3    Serie di Fourier
Esercizio 33 [S9 1]. Determinare la serie di Fourier della funzione 2π-periodica definita
da
                          f (x) = π − |x| per x ∈ (−π, π]
e studiarne la convergenza puntuale e uniforme.
Esercizio 34 [S9 2]. Determinare la serie di Fourier della funzione 2π-periodica definita
da                                  (
                                      0 se − π ≤ x ≤ 0
                           f (x) :=
                                      1 se 0 < x < π
e studiarne la convergenza puntuale e uniforme.
Esercizio (35 [S9 3]. Determinare la serie di Fourier della funzione 2π-periodica definita
            − cos x se −π ≤ x ≤ 0
da f (x) =
            cos x     se 0 < x < π
   e studiarne la convergenza puntuale e uniforme.
Esercizio 36 [S9 4]. Determinare la serie di Fourier della funzione 2π-periodica definita
da
   f (x) = 1 + 12 x per x ∈ [0, 2π), f prolungata per periodicità su R.
   e studiarne la convergenza puntuale e uniforme.
Esercizio 37 [S9 5]. Determinare la serie di Fourier della funzione 2π-periodica definita
dalle seguenti caratteristiche:
    f è una funzione dispari, 2-periodica, definita da f (x) = 1 se x ∈ (0, 1);
    e studiarne la convergenza puntuale e uniforme.
Esercizio 38 [S9 6]. Determinare la serie di Fourier della funzione 2π-periodica definita
da                              
                                x
                                         se x ∈ [0, 1)
   f di periodo T = 3, f (x) = 1          se x ∈ [1, 2)
                                
                                  3 − x se x ∈ [2, 3)
                                
   e studiarne la convergenza puntuale e uniforme.
Esercizio 39 [S9 7]. Determinare la serie di Fourier della funzione 2π-periodica definita
da
   f (x) = 1 − x2 per x ∈ [−1, 1] e prolungata in modo periodico.
   e studiarne la convergenza puntuale e uniforme.
Esercizio 40 [S9 8]. Determinare la serie di Fourier della funzione 2π-periodica definita
da
   f (x)= funzione dispari, 2-periodica, definita da f (x) = πx2 per x ∈ [0, 1).
   e studiarne la convergenza puntuale e uniforme.
Esercizio 41 [CP 2.40]. Si consideri la funzione f (x), 2π-periodica tale che
                                   (
                                     1,    0 ≤ x ≤ π/2
                           f (x) =
                                     −1, π/2 < x ≤ π

(i) Si discuta la convergenza della serie di Fourier associata ad f . (ii) Si scriva la serie
di Fourier di f .

                                             6
Esercizio 42 [CP 2.41]. Si consideri la seguente funzione f : R → R, f (x) = x2 per
x ∈ [0, π], ripetuta periodicamente fuori dall’intervallo [0, π]. (a) Calcolare i coefficienti
di Fourier di f rispetto alla base trigonometrica. (b) Calcolare lo scarto quadratico medio
tra f e la sua media.
Esercizio 43 [CP 2.42]. Si discuta la convergenza della serie di Fourier associata alla
funzione f (x) = 1 − x2 per x ∈ [−1, 1], ed estesa per periodicità su tutto R. Si scriva la
serie di Fourier associata a f .
Esercizio 44 [CP 2.43]. Si consideri la funzione periodica di periodo 4, dispari tale che
                                    (
                                      x,      0≤x≤1
                            f (x) =
                                      2 − x, 1 < x ≤ 2
(i) Si discuta la convergenza della serie di Fourier ad essa associata; (ii) Si scriva la
serie di Fourier associata a f .
Esercizio 45 [CP 2.45]. (a) Calcolare lo sviluppo in serie di Fourier (rispetto alla base
trigonometrica) della funzione
                                 f (x) = x2      ∀x ∈ (−π, π]
ripetuta periodicamente fuori dall’intervallo [−π, π]. (b) Ricordando la formula di Werner
sin α cos β = 12 [sin(α + β) + sin(α − β)], e sfruttando l’identità di Parseval, trovare lo
sviluppo in serie di Fourier (sempre rispetto alla base trigonometrica) della funzione
                               f (x) = x cos x     ∀x ∈ (−π, π]
ripetuta periodicamente fuori dall’intervallo [−π, π].
Esercizio 46 [CP 2.47]. Si consideri una funzione 2π-periodica definita in questo modo:
                                    (
                                     x, x ∈ [0, 2π/3]
                            f (x) =
                                     0, x ∈ (−4π/3, 0)
ripetuta periodicamente. (a) Calcolare i coefficienti di Fourier di f . (b) Discutere la
convergenza della serie di Fourier ad essa associata.
                                                                                         √
Esercizio 47 [CP 2.48]. Si consideri la seguente funzione f : R → R, f (x) = cos( 2x)
per x ∈ [−π/2, π/2], ripetuta periodicamente fuori dall’intervallo [−π/2, π/2]. (a) Cal-
colare i coefficienti di Fourier di f , ricordando l’identità cos A cos B = 12 (cos(A + B) +
cos(A − B)). (b) Valutando lo sviluppo di Fourier di f in x = π2 , calcolare il valore della
serie numerica
                                          +∞
                                          X      1
                                                2
                                              2k − 1
                                          k=1

Esercizio 48 [CP 2.50]. Sia f : R → R la funzione
                                  
                                  −1, x ∈ [−2, −1]
                                  
                           f (x) = x,     x ∈ (−1, 1)
                                  
                                    1,    x ∈ [1, 2]
                                  

ripetuta periodicamente fuori dall’intervallo [−2, 2]. (a) Trovare i coefficienti di Fourier
di f . (b) Calcolare lo scarto quadratico medio tra f e il suo polinomio di Fourier di ordine
k = 2.

                                              7
2     Equazioni differenziali
2.1    Equazioni differenziali del primo ordine
Esercizio 49 [CP 4.1]. Si consideri il seguente problema di Cauchy
                         (
                           y ′ (t) = 2√
                                      1
                                        t
                                          y(t) − √1t , t > 0
                               y(1) = a.
(a) Determinare, al variare di a ∈ R, la soluzione ya .
(b) Calcolare, al variare di a ∈ R, il valore del seguente limite
                                             ya (t) − a
                                       lim
                                       t→1     t−1
Esercizio 50 [CP 4.2]. Sia a > 0. Dato il problema di Cauchy
                                 (
                                          e−y
                                   y ′ = t(t−1)
                                        y(2) = ln a,
(a) determinarne la soluzione;
(b) determinare il più ampio intervallo Ia di definizione della soluzione.
Esercizio 51 [CP 4.3]. Risolvere il problema di Cauchy:
                               (
                                 (2x2 + 1)y ′ = 2x
                                                 y
                                 y(0) = −2.
Esercizio 52 [CP 4.5]. Si consideri il problema di Cauchy
                                  (
                                    y ′ = −x6 y 2
                                    y(0) = β
dove β ∈ R.
1. Trovare la soluzione yβ del problema al variare di β, specificando qual è il suo più
grande intervallo
               R di definizione Iβ .
2. Stabilire se Iβ yβ (x)dx esiste finito o meno al variare di β.
Esercizio 53 [CP 4.6]. (a) Trovare la soluzione del problema di Cauchy:
                               (
                                 x′ (t) = 4t3 x(t)
                                 x(1) = −1.
(b) Trovare il valore minimo e il valore massimo di f sull’intervallo [1, 3].
Esercizio 54 [CP 4.7]. Si consideri l’equazione differenziale
                                      y ′ = et − 2et−y ,
dove y = y(t).
i) Riconoscere di che tipo di equazione differenziale si tratta;
ii) determinare le eventuali soluzioni stazionarie
iii) individuare la soluzione ȳ che passa per il punto (0, 1);
iv) scrivere il polinomio di Mac Laurin di grado due generato dalla funzione ȳ, senza
calcolare esplicitamente la derivata di ȳ nel generico punto t di R.

                                               8
Esercizio 55 [CP 4.8]. Si consideri l’equazione differenziale

                                             y ′ + ty = t,

dove y = y(t).
i) Determinare le soluzioni dell’equazione.
ii) Determinare la soluzione ȳ che assume valore massimo uguale a 2.
iii) Definita la funzione                   Z              x
                                         F (x) =               ȳ(t)dt,
                                                       0
verificare che il grafico di F ammette un asintoto obliquo a +∞.
Esercizio 56 [CP 4.9]. Data l’equazione differenziale

                                       y ′ + 2y cos x = cos x,

a) trovare l’integrale generale;
b) trovare la soluzione che passa per il punto ( π4 , 1);
c) scrivere il polinomio di Taylor di secondo grado centrato in x = π4 della soluzione
trovata al punto b) e disegnare un grafico locale di tale soluzione in un intorno di x = π4 .
Esercizio 57 [CP 4.10]. Si consideri l’equazione differenziale

                                            y ′ = 2y − y 2 .

1. Trovarne tutte le soluzioni.
2. Sia ȳ la soluzione particolare che soddisfa la condizione ȳ(0) = 1. Calcolare le derivate
ȳ ′ (0), ȳ ′′ (0), ȳ ′′′ (0). (Non si richiede di trovare esplicitamente ȳ). Stabilire se x0 = 0 è,
per ȳ, un punto di estremo locale, un punto di flesso, o né l’uno né l’altro.
Esercizio 58 [CP 4.12]. Si consideri il seguente problema di Cauchy
                                  (
                                    y ′ = x2 y 3
                                    y(1) = 3.

(a) Determinare l’unica soluzione u, specificandone l’intervallo (−∞, a) più ampio in cui
risulta essere soluzione. (b) Dire se la soluzione è limitata nel suo dominio e discutere la
convergenza dell’integrale               Z        a
                                                      u(x)dx.
                                              0

Esercizio 59 [CP 4.13]. Si consideri il seguente problema di Cauchy
                             (
                              y ′ (t) + 1+t
                                         t
                                           2 y(t) = 3t,

                              y(0) = 2.

1. Determinare la soluzione y(t). 2. Tracciare un grafico qualitativo della solutione in
un intorno di x = 0 (senza studiare la funzione, ma calcolando lo sviluppo di Taylor).
Esercizio 60 [CP 4.14]. Risolvere il problema di Cauchy
                              (
                                y ′ + xy − sin x = 0
                                y(π) = 2.

                                                       9
Esercizio 61 [CP 4.19]. Si consideri il problema di Cauchy
                                  (         x
                                    y ′ = xe
                                          2y
                                    y(0) = y0 .
Esiste qualche valore di y0 per cui la soluzione del problema di Cauchy sia costante?
Determinare la soluzione del problema di Cauchy nel caso sia y0 = −1.
Esercizio 62 [CP 4.20]. Risolvere il seguente problema di Cauchy
                                (
                                  y ′ = xy + log x
                                  y(2) = 1.
Esercizio 63 [CP 4.21]. Trovare l’integrale generale nell’intervallo (1, +∞) dell’equazione
differenziale
                                         y         2
                                y′ =         +       .
                                       x+1 x−1
Esercizio 64 [CP 4.22]. Risolvere il problema di Cauchy
                                 (
                                   y ′ = ex cos2 (y)
                                   y(0) = π4 .
Esercizio 65 [CP 4.24]. E’ data l’equazione differenziale
                                        y
                                 y′ =       − f (x), x > 3.
                                      x−3
1. Determinare l’integrale generale dell’equazione con f (x) = 0.
2. Determinare l’integrale generale dell’equazione con f (x) = x.
3. Determinare la soluzione ȳ(x) dell’equazione con f (x) = x che soddisfa la condizione
y(4) = 1.
4. Scrivere la formula di Taylor di ȳ(x) di ordine 2 e punto iniziale x0 = 4. Inoltre,
disegnare il grafico di ȳ in un intorno di x0 = 4.
Esercizio 66 [CP 4.27]. Si consideri il seguente problema di Cauchy
                             (
                               y ′ = (2 − y)(3 − y),
                               y(0) = 0.
(a) Determinare l’unica soluzione y, specificandone il dominio più ampio in cui risulta
essere soluzione. (b) Dire se la soluzione è limitata sul dominio e discutere la convergenza
dell’integrale                          Z   +∞
                                                 y(x)dx.
                                        0
Esercizio 67 [CP 4.28]. Risolvere i seguenti problemi di Cauchy
                       (                   (
                               y                    y
                        y ′ + x+1 =0         y ′ + x+1 =x
                        y(0) = 2;            y(0) = 1.
Esercizio 68 [CP 4.35]. Si consideri l’equazione differenziale
                                        y 1
                                   y ′ = − e1/t , t > 0.
                                        t  t
Si dica in quale regione valgono i teoremi di esistenza e unicità in piccolo e in grande. Si
trovi la soluzione di tale equazione che ammette limite finito per t → +∞ e si calcoli tale
limite.

                                                 10
2.2    Analisi Qualitativa delle soluzioni
Esercizio 69 [S10 Es.4]. Dato il problema di Cauchy
                                y ′ = arctan(y);        y(0) = 1
studiarne la soluzione (insieme di definizione, asintoti, max, min, crescenza, concavità)
Esercizio 70 [S10 Es.5]. Dato il problema di Cauchy
                                             1
                                   y′ =            ;    y(0) = 1
                                          1 + 3y 2
studiarne la soluzione (insieme di definizione, asintoti, max, min, crescenza, concavità)
Esercizio 71 [S10 Es.7]. Dato il problema di Cauchy
                                           ln(y)
                                    y′ =         ;     y(0) = 2
                                             y
studiarne la soluzione (insieme di definizione, asintoti, max, min, crescenza, concavità)
Esercizio 72 [S10 Es.8.2]. Determinare per ogni α ∈ R \ {0} la soluzione del problema
di Cauchy
                            y ′ = y − y −2 , y(0) = α.
   Nel caso non si riesca a risolvere il problema, si faccia uno studio qualitativo.
Esercizio 73 [S10 Es.8.3(a)]. Determinare l’unica soluzione locale e l’intervallo mas-
simale di esistenza per i problemi:
                                       |y|
                            y′ =               ,          y(0) = −1.
                                   2 + 2x + x2
Nel caso non si riesca a risolvere il problema, si faccia uno studio qualitativo.
Esercizio 74 [S10 Es.8.3(b)]. Determinare l’unica soluzione locale e l’intervallo mas-
simale di esistenza per i problemi:
                                      1 + y4
                               y′ =          ,         y(0) = −1.
                                        y
Nel caso non si riesca a risolvere il problema, si faccia uno studio qualitativo.
Esercizio 75 [S10 Esercizio 8.7]. È dato il problema di Cauchy
                                 (               2
                                   y ′ = xy 3 ey
                                                                                       (P)
                                   y(0) = 1.

Calcolare il valore minimo dell’unica soluzione locale y = y(x) di (P), sul suo dominio
di esistenza, giustificando opportunamente la risposta, quindi dimostrare che y(x) è pari.
Esercizio 76 [CP 4.49]. E’ dato il problema di Cauchy
                        (
                          y ′ = − arctan(x)(ey − 1 − y)
                          y(0) = y0 ,

essendo y0 > 0.

                                                 11
  1. Sono verificate le ipotesi del teorema di esistenza e unicità locale? E di quello
     globale?
  2. Determinare il luogo dei punti a tangente orizzontale, il luogo dove le soluzioni sono
     crescenti o decrescenti ed eventuali soluzioni costanti.
  3. Determinare l’intervallo massimale di esistenza.
Esercizio 77 [CP 4.51]. E’ dato il problema di Cauchy
                             (           p
                               y ′ = log( 1 + 2y 2 )
                               y(0) = y0 ,
con y0 ∈ R.
  1. Sono verificate le ipotesi del teorema di esistenza e unicità locale? E di quello
     globale?
  2. Determinare, al variare di y0 ∈ R, il luogo dei punti a tangente orizzontale, il luogo
     dove le soluzioni sono crescenti o decrescenti ed eventuali soluzioni costanti.
  3. Determinare, al variare di y0 ∈ R, le regioni di convessità e concavità delle soluzioni.
Esercizio 78 [CP 4.54]. Eseguire l’analisi qualitativa del problema di Cauchy
                           (
                             y ′ = (x2 − 1)(1 − sin y)
                             y(1) = 0,
senza calcolare esplicitamente la soluzione.
Esercizio 79 [CP 4.55]. Eseguire l’analisi qualitativa della soluzione del problema di
Cauchy                            (
                                    y ′ = yey
                                    y(0) = 1.
Esercizio 80 [CP 4.57]. Eseguire lo studio qualitativo della soluzione del problema di
Cauchy                         (
                                 y′ = y2 − y − 2
                                 y(0) = 23 .
(insieme di definizione, asintoti, max, min, crescenza, concavità)

2.3    Equazioni del Secondo Ordine
Esercizio 81 [CP 4.98]. Determinare l’integrale generale dell’equazione
                                      y ′′ + y ′ = t2 + 1.
Esercizio 82 [CP 4.99]. Si consideri la seguente equazione lineare del second’ordine, a
coefficienti costanti:
                          x′′ − 2x′ + 2x = cos t ∀t ∈ R.
(a) Trovare l’integrale generale dell’equazione omogenea associata. (b) Trovare una soluzione
particolare, e scriverne quindi l’integrale generale. (c) Risolvere il problema di Cauchy
con dati iniziali
                                            1
                                   x(0) = , x′ (0) = 0.
                                            5
                                               12
Esercizio 83 [CP 4.100]. Si calcoli l’integrale generale dell’equazione

                                     y ′′ + 9y = cos(3t).

Esercizio 84 [CP 4.101]. Risolvere l’equazione differenziale

                                     y ′′ − 4y = 5 sin(x).

Esercizio 85 [CP 4.102]. Si scriva l’integrale generale dell’equazione

                                     y ′′ + 6y ′ + 9y = 7.

Esercizio 86 [CP 4.103]. Si consideri la seguente equazione lineare del second’ordine,
a coefficienti costanti:
                          2x′′ − 4x′ + 2x = t ∀t ∈ R.
(a) Calcolare l’integrale generale dell’equazione omogenea associata. (b) Trovare una
soluzione particolare e scriverne l’integrale generale. (c) Sapendo che x̄(t) è una soluzione
tale che x̄(0) = 2 e x̄′ (0) = −1, calcolare x̄′′ (0).
Esercizio 87 [CP 4.104]. Risolvere il problema di Cauchy
                            
                                ′′     ′        x
                            y + 2y + 3y = e
                            
                               y(0) = 0             .
                            
                             ′
                               y (0) = 0

Esercizio 88 [CP 4.105]. Determinare l’integrale generale dell’equazione

                                     y ′′ − 2y ′ + y = ex .

Esercizio 89 [CP 4.106]. Determinare l’integrale generale dell’equazione

                                  y ′′ − 3y ′ + 2y = x + e3x .

Esercizio 90 [CP 4.107]. Determinare l’integrale generale dell’equazione
                                           y′
                                  y ′′ −      = 2x2 − 3x − 4.
                                           3
Esercizio 91 [CP 4.108]. Si calcoli una soluzione particolare dell’equazione
                                          2     1
                                    y ′′ − y ′ − y = et .
                                          3     3
Esercizio 92 [CP 4.109]. Determinare f (t) tale che

                                     y(t) = 1 + cos(4t)

sia soluzione dell’equazione
                                       y ′′ + 4y = f (t).
Si determini inoltre l’integrale generale dell’equazione.
Esercizio 93 [CP 4.110]. Si consideri l’equazione differenziale

                           y ′′ (x) + 2ay ′ (x) + y(x) = 0,      a > 0.

                                                13
  1. Determinarne l’integrale generale ya (x) al variare di a > 0.

  2. Esistono valori di a > 0 in corrispondenza dei quali le soluzioni sono limitate su
     [0, +∞)?
Esercizio 94 [CP 4.111].       1. Al variare del parametro reale k, scrivere la soluzione
     generale dell’equazione
                                 y ′′ + 2ky ′ − 3(2k + 3)y = 0.
                                                                                2
  2. Determinare un valore del parametro reale k per cui la funzione y(x) = ex sia una
     soluzione particolare dell’equazione
                                                                     2
                     y ′′ + 2ky ′ − 3(2k + 3)y = (11 − 12x + 4x2 )ex .   (∗)

  3. In corrispondenza del valore di k trovato al punto precedente, scrivere la soluzione
     generale dell’equazione (*).
Esercizio 95 [CP 4.113]. Determinare l’integrale generale dell’equazione differenziale

                                  y ′′ − 2y ′ + y = 2e2x .

Esercizio 96 [CP 4.114]. Risolvere l’equazione differenziale

                               y ′′ + 2y ′ − 3y = ex sin(2x).

Esercizio 97 [CP 4.115]. Risolvere l’equazione differenziale

                                   y ′′ − 2y ′ = x + ex .

Esercizio 98 [CP 4.116]. Risolvere l’equazione differenziale

                                  y ′′ + y ′ − 6y = 2e−x .

Esercizio 99 [CP 4.117]. Risolvere il problema di Cauchy
                               
                                   ′′
                               y − y = cos x
                               
                                 y(0) = − 12
                               
                                ′
                                 y (0) = 1.

Esercizio 100 [CP 4.118]. Si consideri la seguente equazione lineare omogenea del
second’ordine:
                                x′′ + 2x′ = αx,
dove α è un parametro reale fissato, maggiore di −1.
 (a) Posto α = 3, risolvere il problema di Cauchy con dati iniziali x(0) = 1 e x′ (0) = 1.

 (b) Determinare per quali valori di α > −1 vale la seguente proprietà: ogni soluzione
     della (4.12) soddisfa
                                       lim x(t) = 0.
                                         t→+∞

Esercizio 101 [CP 4.119]. Risolvere l’equazione differenziale

                                y ′′ − 2y ′ + y = cos(3x).

                                            14
Esercizio 102 [CP 4.120]. Risolvere l’equazione differenziale

                                    y ′′ + 4y = ex cos(x).

Esercizio 103 [S11 Esercizio 2.1]. Determinare gli autovalori del problema
                              
                                   ′′
                              −z = µz
                              

                                   
                                       z(0) = z(1) = 0,
                                   

cioè determinare tutti e soli i µ ∈ R tali che il problema abbia almeno una soluzione non
nulla.

Esercizio 104 [S11 Esercizio 2.2]. Determinare gli autovalori del problema
                              
                                   ′′   ′
                              −z + 2z = µz
                              

                                   
                                       z(0) = z(1) = 0,
                                   

Esercizio 105 [S11 Esercizio 3]. Determinare l’integrale generale delle seguenti equazioni
differenziali lineari:

                 (a) y ′′ − 2y ′ − 3y = 3e2t (b) y ′′ − y ′ − 2y = −2t + 4t2
                 (c) y ′′ + 9y = t2 e3t + 6 (d) y ′′ + 2y ′ + 5y = 3 sin(2t)
                 (e) y ′′ + 2y ′ + y = 2e−t (f ) y (4) − y = 3t + cos(t)

3      Differenziabilità
Gli esercizi in questo caso si limitano a calcolare il piano tangente ad una funzione data
in un punto dato.


4      Teorema del Dini
Esercizio 106 [Esame 13/06/2023 (risolto su elearning)]. Siano a > 0, x0 ∈ R e
y0 > 0. Data la funzione
                                           1    1
                              F (x, y) =      −    + a(x − x0 )2
                                           y 2 y02

    1. stabilire se l’equazione F (x, y) = 0 definisce implicitamente una funzione y = y(x)
       o x = x(y) in un intorno del punto (x0 , y0 );

    2. determinare la derivata della funzione y = y(x) o x = x(y) definita implicitamente,
       nel caso in cui esista;

    3. in base al risultato ottenuto dire se la funzione y = y(x) o x = x(y), definita
       implicitamente, risolve un problema di Cauchy e quale.




                                               15
5     Ottimizzazione
5.1    Ottimizzazione libera
Esercizio 107 [CP 8.2]. Sia f (x, y) = x3 + y 3 + 4x2 − 2y 2 . Determinare i punti critici
di f e classificarli.

Esercizio 108 [CP 8.3]. Determinare e classificare i punti critici della funzione

                           f (x, y) = −x4 − y 4 + 2x2 − 4xy + 2y 2 .

Esercizio 109 [CP 8.4]. Trovare e classificare i punti critici della funzione

                                  f (x, y) = x3 y 2 (1 − x − y).

Esercizio 110 [CP 8.5]. Sia f la funzione di due variabili data dall’espressione
                                               2    2
                             f (x, y) = xye−x −y        ∀(x, y) ∈ R2 .

(a) Spiegare perché f ∈ C 2 (R2 ) e calcolarne la matrice Hessiana Hf (x, y).
(b) Trovare tutti i punti critici di f e classificarli.

Esercizio 111 [CP 8.7]. Sia

                                f (x, y) = (ey − 1)(2 + y − ex ).

Trovare i punti critici di f e per ciasuno di essi, dire se si tratta di un punto di minimo
relativo, di massimo relativo o di sella.

Esercizio 112 [CP 8.8]. Determinare gli estremi relativi di

                            f (x, y) = ex (x − 1)(y − 1) + (y − 1)2 .

Esercizio 113 [CP 8.9]. Sia f : R2 → R la seguente funzione:
                                                            2
                                     f (x, y) = y 2 + ye−x .

(a) Trovare tutti i punti critici di f .
(b) Classificare tali punti critici.

Esercizio 114 [CP 8.10]. Sia f (x, y) = −x4 + 2x2 + x2 y − y 2 + 4y. Trovare i punti
critici di f e, per ciascuno di essi, dire se si tratta di un punto di minimo relativo, di
massimo relativo o di sella.

Esercizio 115 [CP 8.12]. Sia

                                                                x4
                                  f (x, y) = −αx2 + y 2 +
                                                                4
con α ∈ R. Al variare del parametro α ∈ R, i) trovare i punti critici di f e dire se si
tratta di punti di massimo o minimo relativo, o di sella;
ii) determinare f (R2 ).


                                               16
Esercizio 116 [CP 8.15]. Determinare e classificare i punti stazionari della funzione

                                 f (x, y) = x(x + y)ey−x .

Esercizio 117 [CP 8.16]. Determinare e classificare i punti critici di

                                f (x, y) = ex−y (x2 − 2y 2 ).

Esercizio 118 [CP 8.17]. Determinare e classificare i punti critici della funzione
                                              4    3   2       2
                                f (x, y) = ex +y −4x −3y .

Esercizio 119 [CP 8.18]. Determinare, se esistono, i punti di massimo e di minimo
assoluto della funzione
                          f (x, y) = −x4 − y 2 + 4y − 2.
Esercizio 120 [CP 8.19]. Determinare, se esistono, i punti di massimo e di minimo
assoluto della funzione
                            f (x, y) = x2 + 2xy + y 2 .
Esercizio 121 [S09F pag 24]. Determinare i punti stazionari della seguente funzione
e stabilire se sono di massimo o minimo locale

                                   f (x, y) = x2 y − xy

Esercizio 122 [S09F pag34]. Determinare eventuali punti di massimo e di minimo
relativo per la funzione

                           f (x, y, z) = x2 + y 3 + z 2 − xy − xz

Esercizio 123 [S09F pag35]. Determinare eventuali punti di massimo e di minimo
relativo per la funzione

                        f (x, y, z) = 4xy + xz + 6y 2 + x2 z + 2xyz

5.2    Ottimizzazione vincolata
Esercizio 124 [S09F pag 19]. Cercare eventuali punti di massimo o minimo locali della
funzione
                         f (x, y) = (y − x2 )(x2 + y 2 + 2y)
sul suo dominio e poi il massimo e il minimo di f sulla palla chiusa di centro l’origine e
raggio 2.
                                                           4
Esercizio 125 [CP 8.13]. Sia f (x, y) = −x2 + y 2 + x4 . Determinare massimo e minimo
assoluti di f nell’insieme

                       P = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, 0 ≤ y ≤ x2 }.

Esercizio 126 [CP 8.20]. Determinare massimo e minimo assoluti di
                                                   x2
                                  f (x, y) = x +      + y2
                                                   2
nell’insieme R = {(x, y) ∈ R2 : |x| ≤ 2, |y| ≤ 1}. Determinare f (R). Determinare f (R2 ).

                                             17
Esercizio 127 [CP 8.22]. Determinare il massimo e il minimo assoluti di

                                         f (x, y) = xey

sul bordo del quadrato Q di vertici A = (−1, −1), B = (1, −1), C = (1, 1), D = (−1, 1).
Esercizio 128 [CP 8.23]. Sia

                                 f (x, y) = x4 + x2 + y 4 − y 6 .

Determinare i punti critici di f e dire se si tratta di punti di minimo relativo, di massimo
relativo o di sella. Determinare l’insieme di punti di minimo assoluto nei seguenti insiemi:
R2 , V = {(x, y) ∈ R2 : |y| ≤ 2}, U = {(x, y) ∈ R2 : |x| ≤ 2}. Determinare f (R2 ),
f (U ), f (V ).
                                                        2
Esercizio 129 [CP 8.24]. Sia f (x, y) = x2 + y2 + x2 y + 2.
    (i) Determinare i punti critici liberi di f e classificarli.
    (ii) Determinare il massimo assoluto e il minimo assoluto di f nella regione triango-
lare chiusa di vertici (0, 0), (1, −1), (1, 0).
Esercizio 130 [CP 8.25]. Trovare gli estremi di

                                         f (x, y) = ex+y

sul vincolo x2 + y 2 = 1.
Esercizio 131 [CP 8.26]. Determinare il massimo assoluto e il minimo assoluto di

                                        f (x, y) = x2 + y

sul vincolo Z = {(x, y) ∈ R2 : x2 + 2y 2 = 1}.
Esercizio 132 [CP 8.27]. Determinare massimo e minimo assoluti di
                                           √
                                f (x, y) = 3 xy

nell’insieme A = {(x, y) ∈ R2 : x2 + y 2 − xy − 1 = 0}.
Esercizio 133 [CP 8.28]. Siano f e g le funzioni
                                                    2       2
                f (x, y) = x2 + y 2 ,   g(x, y) = ex + ey − 4       ∀(x, y) ∈ R2 .

   (a) Calcolare ∇f (x, y) e ∇g(x, y). Spiegare perché f e g sono differenziabili in R2 .
   (b) Risolvere il seguente problema di ottimizzazione vincolata, utilizzando i moltipli-
catori di Lagrange: trovare il massimo di f (x, y) soggetta al vincolo g(x, y) = 0.
Esercizio 134 [CP 8.29]. Determinare il massimo e il minimo assoluti di

                                         f (x, y) = xy 3

nell’insieme A = {(x, y) ∈ R2 : 2x2 + y 2 = 3}.
Esercizio 135 [CP 8.30]. Determinare, se esistono, i punti di massimo e di minimo
assoluto di
                                f (x, y) = x2 y
nell’insieme D = {(x, y) ∈ R2 : x2 + y 2 ≤ 1}.

                                               18
Esercizio 136 [CP 8.31]. Sia f : R2 → R la seguente funzione:

                         f (x, y) = (3x − 1)2 + (3y − 1)2         ∀(x, y) ∈ R2 .

    (a) Trovare i punti critici di f e classificarli.
    (b) Trovare i punti di massimo e minimo globale per f ristretta all’insieme K ⊂ R2
costituito dal triangolo di vertici O = (0, 0), P = (1, 0) e Q = (0, 1).
Esercizio 137 [CP 8.35]. Calcolare massimo e minimo assoluti di

                                            f (x, y) = x2 y

nell’insieme
                         A = {(x, y) ∈ R2 : x ≥ 0, y ≥ 0, 2x2 + y 2 ≤ 4}.
Esercizio 138 [CP 8.36]. Trovare il massimo della funzione

                            f (x, y, z) = x2 yz 2 ,    x > 0, y > 0, z > 0,

sul vincolo x + y + z = 1.
Esercizio 139 [CP 8.37]. Sia

                                          g(x, y) = x2 − y 2

e sia
                                D = {(x, y) ∈ R2 : x2 + 2y 2 ≤ 1}.
Determinare massimo e minimo assoluto di g in D.
Esercizio 140 [CP 8.38]. Determinare l’insieme di definizione e i massimi e i minimi
assoluti della funzione
                                              √
                              f (x, y) = cos ( xy) .
Esercizio 141 [CP 8.39]. Si determinino (senza studiarne la natura) i punti critici
della funzione
                             f (x, y) = xy − y 2 + 3,
vincolata all’insieme
                                    {(x, y) ∈ R2 : x + y 2 = 1}.
Esercizio 142 [CP 8.40]. Sia m ∈ N, m ≥ 4 pari e sia

                                          f (x, y) = x2 + y 2 .

Determinare i punti di massimo e di minimo di f sul vincolo

                             Z = {(x, y) ∈ R2 : xm + y m − 1 = 0}.

Esercizio 143 [CP 8.41]. Trovare i punti stazionari della funzione

                                           f (x, y) = x − y

vincolati alla regione

                   A = {(x, y) ∈ R2 : arctan(x2 + y 2 − 2) = 2 − x + y}.

                                                      19
Esercizio 144 [CP 8.42]. Determinare massimi e minimi assoluti della funzione
                                                     2
                                     f (x, y) = ey−x

nella regione                                             √
                       A = {(x, y) ∈ R2 : x + 1 ≤ y ≤         1 − x2 }.
Esercizio 145 [CP 8.43]. Determinare massimo e minimo assoluti della funzione
                                         p
                          f (x, y) = xy + 4 − x2 − y 2

nell’insieme
                            D = {(x, y) ∈ R2 : x2 + y 2 ≤ 1}.
Esercizio 146 [CP 8.44]. Determinare massimo e minimo assoluti della funzione

                               f (x, y) = x2 y 2 − 2x2 y + x2

nell’insieme
                            C = {(x, y) ∈ R2 : x2 + y 2 ≤ 1}.
Esercizio 147 [CP 8.45]. Sia

                              f (x, y) = (x + y)2 + 2y 2 + 3.

Trovare, se esistono, tutti i punti di minimo e di massimo assoluti di f in

                      T = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, 0 ≤ y ≤ 1 − x}.

Esercizio 148 [CP 8.46]. Determinare tutti i punti di massimo e di minimo assoluto
di
                                             2x2 y
                                f (x, y) = 2
                                            x + y2
nell’insieme
                   I = {(x, y) ∈ R2 , x, y ∈ [0, 1], x2 + y 2 ≥ 1}.
Esercizio 149 [CP 8.47]. Stabilire se

                                   f (x, y) = −x + x|y|

ammette massimi e minimi assoluti nel cerchio di centro (0, 1) e raggio 21 , e in caso
affermativo determinarli.
Esercizio 150 [CP 8.48]. Determinare massimo e minimo assoluti di

                              h(x, y) = 4x + 6y − x2 − y 2

in [0, 4] × [0, 5].
Esercizio 151 [CP 8.49]. Trovare i punti di massimo e minimo assoluti di

                                    f (x, y) = xye2y−x

in
                          D = {(x, y) : 0 ≤ y ≤ 1, 0 ≤ x ≤ 2y}.

                                            20
Esercizio 152 [S13F pag 16]. Determinare massimo e minimo di f (x, y) = xy sulla
circonferenza x2 + y 2 = 1.

Esercizio 153 [S13F pag 12]. Determinare il massimo e il minimo della funzione

                                   f (x, y, z) = x + 3y − z

sugli insiemi C = {(x, y, z) ∈ R3 : z 2 ≤ x2 + y 2 ≤ 1} e D = {(x, y, z) ∈ R3 : x2 + y 2 − z =
0, z = 2x + 4y}.

Esercizio 154 [S13F pag 25]. Data la funzione
                                              2        2
                              f (x, y) = e−(x /2+y /3) (x2 + y 2 ).

    1. determinare massimi e minimi relativi di f sul suo dominio naturale;
    2. discutere l’esistenza del massimo e del minimo di f sul dominio ellittico

                                                       x2 y 2
                             E = {(x, y) ∈ R2 :          +    ≤ 4}
                                                       2   3
e, qualora esistano, determinarli.

Esercizio 155 [S13F pag 29]. Discutere l’esistenza di massimo e minimo della funzione
                                              p
                            f (x, y) = (x + y) x2 + y 2

sulla palla chiusa di R2 di centro 0 e raggio 1 e, se esistono, determinarli.

Esercizio 156 [Esame 18/09/2023 (risolto su elearning)]. Data la funzione

                                     f (x, y) = (xy − 1)2

    1. determinare i punti stazionari e stabilire se sono di massimo o minimo;
                                                                                2
    2. stabilire se esistono
                           √ il massimo e il minimo di f sulla palla chiusa di R di centro
       l’origine e raggio 2 e, se esistono, determinarli.


6     Integrali multipli
Esercizio 157 [S17F pag 27]. Calcoliamo l’integrale della funzione f (x, y) = x + y 2
sul settore di corona circolare di raggi 1 e 2 contenuto nel primo quadrante.

Esercizio 158 [S17F pag 40]. Calcolare l’integrale
                             Z 2
                                x + y2       y
                                     2
                                         log dxdy
                              D    x         x
dove D è la porzione di corona circolare
                                                          x        √
                 D = {(x, y) ∈ R2 : 1 ≤ x2 + y 2 ≤ 9, y ≥ √ , y ≤ x 3}.
                                                           3



                                                  21
Esercizio 159 [CP 9.2]. Calcolare
                                          ZZ
                                                    xy dx dy,
                                                T

essendo T il triangolo di vertici (0, 0), (1, 1), (3, −1).

Esercizio 160 [CP 9.4]. Calcolare l’integrale
                               ZZ √        √
                                      x3 ey x dx dy,
                                          Ω

essendo                                                          √
                         Ω = {(x, y) ∈ R2 : 0 ≤ x ≤ 2, 0 ≤ y ≤    x}.

Esercizio 161 [CP 9.5]. Sia

                       Ω = {(x, y) ∈ R2 : x ≥ 0, y ≤ x, x2 + y 2 ≤ 1}.

Calcolare                             ZZ        √
                                                  2  2
                                               e x +y dx dy.
                                           Ω

Esercizio 162 [CP 9.6]. Sia

                        Ω = {(x, y) ∈ R2 : x ≥ 0, 3x2 − 1 ≤ y ≤ x2 }.

Calcolare                                 ZZ
                                                   xe2y dx dy.
                                               Ω

Esercizio 163 [CP 9.7]. Calcolare l’integrale
                             ZZ p
                                     y − x2 + 2 dx dy,
                                      D

essendo
                      D = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, x2 − 2 ≤ y ≤ x2 }.

Esercizio 164 [CP 9.8]. Calcolare
                               ZZ
                                               (2x + y) dx dy,
                                          A

dove A è la regione
               √     compresa tra le circonferenze x2 + y 2 = 1 e x2 + y 2 = 9, e le rette
y = x e y = − 3x, nel semipiano y ≥ 0.

Esercizio 165 [CP 9.9]. Calcolare

                                               xy 2
                                ZZ
                                              2     2
                                                      dx dy,
                                           A x +y

dove
                        A = {(x, y) ∈ R2 : x2 + y 2 < 9, x < 0, y > 0}.

                                                     22
Esercizio 166 [CP 9.10]. Calcolare
                                ZZ
                                                          2
                                                 xyex dx dy,
                                             D

dove D è dato dall’unione del triangolo di vertici (−1, 0), (0, 1), (0, −1) con il semicerchio
B1 (0) ∩ {x ≥ 0}.
Esercizio 167 [CP 9.11]. Calcolare
                                  ZZ
                                                      y
                                                     e x dx dy,
                                                 D

dove                  n                        y               o
                   D = (x, y) ∈ R2 : 0 ≤ y ≤ 2, ≤ x ≤ min{y, 1} .
                                               2
                                                                           p
Esercizio 168 [CP 9.13]. Sia E ⊂ R2 la regione delimitata da x =               9 − y 2 e x = 0.
Calcolare                     ZZ
                                      2  2
                                  e−(x +y ) dx dy.
                                         E

Esercizio 169 [CP 9.14]. Calcolare l’integrale
                               ZZ
                                   (x2 + y 2 ) dx dy,
                                         Ω

essendo
                                         Ω = T ∪ C,
T la regione triangolare di vertici (−1, 0), (0, 0), (0, 1) e C = {(x, y) ∈ R2 : x2 + y 2 ≤
1, x ≥ 0, y ≥ 0}.
Esercizio 170 [CP 9.16]. Sia E ⊂ R2 la regione limitata, delimitata dall’ellisse di
equazione
                               9x2 + 4y 2 = 36.
Calcolare                                ZZ
                                                     x2 dxdy.
                                                 E

Esercizio 171 [CP 9.18]. Calcolare l’integrale
                            ZZ
                                (x2 + y 2 − xy) dxdy,
                                     A

dove
                             A = {(x, y) ∈ R2 : x2 + 4y 2 ≤ 4}.
Esercizio 172 [CP 9.20]. Calcolare:
                       ZZ               y 2  2 2
                                2 y
                            sin        1+          ex +y dxdy
                          D        x        x

dove D = (x, y) ∈ R2 : y ≥ 0, x ≥ y, 14 ≤ x2 + y 2 ≤ 1 . Si suggerisce di fare uso del
           

cambio di coordinate:
                                     y
                                 u = , v = x2 + y 2
                                     x
                                                     23
Esercizio 173 [CP 9.22]. Calcolare
                             ZZ
                                          x cos(1 − y) dxdy,
                                      E

dove E = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, x2 − 1 ≤ y ≤ 1 − x2 }.
Esercizio 174 [CP 9.23]. Calcolare
                               ZZ
                                                  2   2
                                              x2 ex +y dxdy,
                                          Ω
dove Ω è il cerchio di raggio 2 e centro O.
Esercizio 175 [CP 9.26]. Calcolare
                                             2x2 y
                               ZZ
                                             2     2
                                                     dxdy,
                                          D x +y
essendo                   (                               √       )
                                                           3
                   D=     (x, y) ∈ R2 : 1 < x2 + y 2 < 3,    x<y<x .
                                                          3
Esercizio 176 [CP 9.28]. Si consideri la seguente trasformazione T nel piano R2 :
                                 (
                                  x = uv
                     T (u, v) :=                ∀(u, v) ∈ R2 .
                                  y=v
   (a) Calcolare la matrice Jacobiana JT e il corrispondente Jacobiano.
   (b) Utilizzando il cambiamento di variabili dato dalla (9.1), calcolare l’integrale doppio
                                    ZZ
                                         x+y
                                            2
                                                dxdy,
                                       Ω y
dove
                      Ω := {(x, y) ∈ R2 : 0 ≤ x ≤ y 2 , −2 ≤ y ≤ −1}.
Esercizio 177 [Esame 06/07/2023 (risolto su elearning)]. Disegnare il sottonsieme
S di R3 definito da
                   S = {(x, y, z) ∈ R3 : x2 + y 2 + z 2 ≤ 2, z ≥ x2 + y 2 }
e calcolarne il volume.
Esercizio 178 [S17F pag 35]. Sia
                                            √           x
                    E = {(x, y) ∈ R2 : 1 ≤ y x ≤ 2, 0 < ≤ y ≤ x}.
                                                        2
Rappresentare graficamente l’insieme E e calcolarne l’area. Calcolare le coordinate del
baricentro di E e il volume del solido ottenuto da una rotazione completa di E attorno
alla retta x + y = 0.
Esercizio 179 [S17F pag 38]. Determinare le coordinate del baricentro e il volume
dell’insieme
                                 3           x2 + y 2 + z 2 1
             B = {(x, y, z) ∈ R : 0 ≤ z ≤                  , ≤ x2 + y 2 + z 2 ≤ 1}.
                                                   2        4
Esercizio 180 [Esame 22.01.2024 (risolto su elearning)]. Determinare il volume e
la superficie laterale totale del solido compreso tra il piano z = 0, il paraboloide z = x2 +y 2
ed il cilindro di equazione x2 + y 2 = 1.

                                                 24
7      Campi vettoriali
Esercizio 181 [CP 10.2]. Calcolare l’integrale del campo vettoriale
                                      r          r     !
                                         y+3       x+3
                         F (x, y) =            ,
                                         x+3       y+3
                                      2
esteso all’ellisse di equazione x2 + y9 = 1 percorsa in verso antiorario.
Esercizio 182 [S16F pag 22]. Dato il campo vettoriale
                                2
                                                 x2 + 2x
                                                          
                                x + 2xy + 2y
                    F (x, y) =               ,− 2
                                  (x2 − 2y)2    (x − 2y)2

    (a) determinarne il dominio e stabilire se è un insieme aperto connesso e, nel caso
in cui non lo sia, stabilire se si può scrivere come unione di uno o più aperti connessi
(componenti connesse);
    (b) per ciascuna componente connessa del dominio, stabilire se si tratta di un insieme
semplicemente connesso;
    (c) dire se il campo F è conservativo ed in caso affermativo determinarne tutti i
potenziali;
    (d) calcolare l’integrale di F su una curva congiungente i punti P = (−2, 1) e Q =
(2, 1). È possibile affermare che il valore dell’integrale non dipende dalla curva scelta per
andare da P a Q?
Esercizio 183 [S16F pag 26]. Dato il campo vettoriale

                                F (x, y) = (A(x, y), B(x, y))

dove
                       x2 − y 2 − 1                             2xy
    A(x, y) =     2    2     2   2       4
                                           , B(x, y) = 2                            ,
                (x − 1) + 2y (x + 1) + y              (x − 1) + 2y 2 (x2 + 1) + y 4
                                                             2


   (a) Determinare il dominio di F e dire se è connesso, convesso o semplicemente
connesso;
   (b) stabilire se il campo è conservativo
   b.1) nella palla aperta di centro l’origine e raggio 1;
   b.2) nel suo dominio.
Esercizio 184 [S16F pag 31]. Dato il campo vettoriale
                                                                 
                                      4x               9y
                   F (x, y) =                   ,
                                log(4x2 + 9y 2 ) log(4x2 + 9y 2 )

    (a) determinarne il dominio D di F e stabilire se è un insieme aperto connesso e,
nel caso in cui non lo sia, stabilire se si può scrivere come unione di uno o più aperti
connessi (componenti connesse);
    (b) per ciascuna componente connessa di D, stabilire se si tratta di un insieme con-
vesso o semplicemente connesso;
    (c) dire se il campo F è conservativo su tutto il dominio e, nel caso in cui non lo sia,
indicare eventuali sottoinsiemi del dominio in cui risulta conservativo.

                                             25
Esercizio 185 [CP 10.5]. Sia F il seguente campo vettoriale:
                                            x2 z 2
                                                         
                         F (x, y, z) = xyz,        , log z .
                                             2
   (a) Determinare il dominio di F e calcolarne il rotore. Il campo è conservativo?
   (b) Calcolare la circuitazione di F lungo la circonferenza
                       C1 := (x, y, z) ∈ R3 : x2 + y 2 = 1, z = 1 .
                              

Esercizio 186 [CP 10.6]. Sia F il seguente campo vettoriale:
                                                         
                              2x            8y
            F (x, y) =                ,              + 2y    ∀(x, y) ∈ Ω,
                         x2 + 4y 2 − 1 x2 + 4y 2 − 1
dove
                             Ω := {(x, y) ∈ R2 : x2 + 4y 2 > 1}.
   (a) Trovare tutti i potenziali di F in Ω.
   (b) Si poteva dedurre l’esistenza del potenziale dalla teoria?
   (c) Calcolare il lavoro di F lungo la curva
                             φ(t) = (2 cos t, sin t),         t ∈ [0, 2π].
Esercizio 187 [CP 10.8]. Siano F : R3 → R3 un campo vettoriale e r : [−π, π] → R3
una curva, definiti in questo modo:
                         F (x, y, z) = (x, zy, z)            ∀(x, y, z) ∈ R3 ,
                            r(t) = (cos t, sin t, t2 )   ∀t ∈ [−π, π].
   (a) Stabilire se r è chiusa e se è regolare (eventualmente a tratti).
   (b) Calcolare il lavoro di F lungo la curva descritta da r. Dal valore trovato è possibile
dedurre che il campo è conservativo o meno?
Esercizio 188 [CP 10.11]. Sia F il seguente campo vettoriale:
                                                             !
                                     x              y
                   F (x, y) = p               ,p               .
                                 x2 + y 2 − 4   x2 + y 2 − 4
   (a) Determinare il dominio Ω di F e descriverne le caratteristiche topologiche.
   (b) Mostrare che F è irrotazionale e trovarne un potenziale in Ω.
   (c) Calcolare il lavoro di F lungo la curva
                                           √
                                 r(t) = (t, t) t ∈ [2, 3].
Esercizio 189 [CP 10.12]. Sia
                                                   x2 y
                                                       
                                              y
                                 F (x, y) = xe + 3, e
                                                   2
Calcolare                                  Z
                                                 F · T ds,
                                             γ
essendo γ la curva                                    
                                       4             2
                          γ(t) =         arctan(t), t ,          0 ≤ t ≤ 1.
                                       π

                                                  26
Esercizio 190 [CP 10.15]. Si calcoli il lavoro del campo vettoriale
                                  F (x, y) = (2xy, x2 − y 2 )
lungo la curva γ di equazione
                                  γ(t) = (t2 , t)    t ∈ [0, 1].
Esercizio 191 [CP 10.17]. Dati il campo vettoriale
                                    2xy 2
                                                          
                                                    2    2
                      F (x, y) =          , y log[(x + 1) ]
                                   x2 + 1
e la curva                          √
                                     3
                                                    
                                         t     2
                           r(t) = 2         , t − 3t , t ∈ [0, 3],
                                     t +1
   • dire se il campo è irrotazionale e se è conservativo nel suo dominio;
   • calcolare, se risulta conservativo, il potenziale f (x, y);
   • calcolare il lavoro di F (x, y) sulla curva r.
Esercizio 192 [CP 10.18]. Sia dato il campo vettoriale
                                                   x2
                                                         
                                               2        3
                     F (x, y, z) = ax log z, by z,    +y .
                                                   z
   (i) Trovare a, b ∈ R in modo che il campo sia conservativo.
   (ii) Calcolare il lavoro del campo
                              G(x, y, z) = (2x log z, 2y 2 z, y 3 )
lungo il segmento che congiunge (1, 1, 1) a (2, 1, 2).
Esercizio 193 [CP 10.19]. Sia
                                                                
                                              1
                             F (x, y) =          + sin y, x cos y .
                                              x2
    (i) Determinare l’insieme di definizione D del campo vettoriale F e dire se D è sem-
plicemente connesso;
    (ii) Stabilire se F è conservativo in
                       Ω := {(x, y) ∈ R2 : (x − 3)2 + (y − π)2 ≤ 1},
motivando la risposta;
   (iii) Se esiste, determinare un potenziale U di F in Ω tale che U (3, π) = 0.
Esercizio 194 [CP 10.21]. Sia dato il campo vettoriale
                                                       
                                     y − 4x     x+y
                       F (x, y) =            ,−           .
                                    4x2 + y 2 4x2 + y 2
   (i) Trovare il dominio D di F e stabilire se è semplicemente connesso;
   (ii) Dimostrare che F è irrotazionale in D.
   (iii) Calcolare il lavoro di F lungo la curva
                             γ(t) = (cos t, 2 sin t),    t ∈ [0, 2π].

                                                27
Esercizio 195 [Esame 15/02/2024 (risolto su elearning)]. Dire per quali valori di
a ∈ R (se esistono) il campo vettoriale
                                          2x                  y            
                      F (x, y) =                     + y,               + x
                                       (ax2 + y 2 )2      (ax2 + y 2 )2

è conservativo. Per tali valori di a ∈ R

   • calcolare un potenziale del campo,

   • calcolare l’integrale del campo vettoriale sull’ellisse di equazione ax2 + y 2 = 2.

Esercizio 196 [Esame 04/09/2023 (risolto su elearning)]. Stabilire per quali valori
di a ∈ R il campo vettoriale
                                           ax                  y             
                      A(x, y) =                      + y,               + ax
                                       (ax2 + y 2 )2      (ax2 + y 2 )2

è conservativo e calcolarne i potenziali.

Esercizio 197 [Esame 15/02/2023 (risolto su elearning)]. Dato il campo vettoriale

                                                 (x − 3, y − 1)
                               F (x, y) =                         ,
                                              (x − 3)2 + (y − 1)2

  1. stabilire il dominio;

  2. stabilire se è irrotazionale;

  3. calcolare l’integrale del campo lungo la circonferenza di centro (3, 1) e raggio 1;

  4. stabilire se è conservativo e, in caso affermativo, determinarne un potenziale.




                                                  28
