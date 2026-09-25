---
fonte: "08-SviluppoPotenze-26-05-02.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Funzioni sviluppabili in serie di potenze


           Lorenzo D’Ambrosio
      lorenzo.dambrosio@uniud.it



             2 maggio 2026




                                            1 / 23
Serie di potenze di punto iniziale x0 ̸= 0

Si tratta di serie di funzioni del tipo:
                                           X
                                                 an (x − x0 )n .                    (∗)
                                           n≥0

Fin’ora abbiamo visto teoremi nel caso in cui x0 = 0. Tutte le cose che abbiamo detto
fin’ora valgono a meno di traslazione. Ossia studiando
                                      X
                                         an (x − 0)n                              (∗∗)
                                           n≥0

e poi traslando di x0 .
Ad esempio. (∗∗) converge uniformemente/puntualmente/totalmente in [a, b], se e solo
se (∗) converge uniformemente/puntualmente/totalmente in [a + x0 , b + x0 ]. Pertanto
l’insieme di convergenza C di (∗) sarà tale che

                            ]x0 − ρ, x0 + ρ[⊂ C ⊂ [x0 − ρ, x0 + ρ]

dove ρ è il raggio di convergenza di (∗∗), che continueremo a chiamare raggio di
convergenza della (∗).



                                                                                          2 / 23
Quando una funzione data coincide con una serie di potenze?
Definizione
Sia f : I → R, e sia x0 punto interno all’intervallo I . Diremo che f è sviluppabile in serie
di potenze di Taylor con punto inizialeP x0 (di centro   x0 ) se esiste δ > 0 ed una
successione (an )n≥0 tale che la serie    an (x − x0 )n ha raggio di convergenza ρ ≥ δ e la
                                        n≥0
sua somma coincide con f in ]x0 − δ, x0 + δ[:
                           X
                   f (x) =     an (x − x0 )n ,        x ∈]x0 − δ, x0 + δ[.
                               n≥0

 Osservazione. Se f è sviluppabile in serie di potenze di Taylor allora
f ∈ C ∞ e necessariamente f (n) (x0 ) = an n!, ossia i coefficienti an sono determinati a priori
a partire dalla f .
Un altro modo di vedere la definizione è il seguente.
Sia f ∈ C ∞ (I ). Posso considerare la successione di coefficienti an := f (n) (x0 )/n! e la serie
            ∞ (n)
                f (x0 )
                        (x − x0 )n questa serie si dice serie di Taylor di f di centro x0 (Mac
            P
di potenze          n!
            n=0
Laurin se x0 = 0)
Tale serie di potenze avrà un suo raggio di convergenza 0 ≤ ρ ≤ ∞ e una somma
          ∞ (n)
             f (x0 )
                     (x − x0 )n .
          P
F (x) :=       n!
         n=0
È vero che f = F in un intorno di x0 ?
se la risposta è affermativa, allora f è sviluppabile in serie di Taylor di centro x0 .      3 / 23
Se f è sviluppabile in serie di potenze di Taylor di centro x0 allora
             ∞
             X f (n) (x0 )
   f (x) =                   (x − x0 )n
             n=0
                    n!
                                           1 ′′                           f (n) (x0 )
         =f (x0 ) + f ′ (x0 )(x − x0 ) +      f (x0 )(x − x0 )2 + · · · +             (x − x0 )n + · · ·
                                           2!                                 n!
con convergenza totale su ogni intervallo [a, b] ⊂ (x0 − ρ, x0 + ρ).
Possiamo anche scrivere, ∀h ≥ 1, ∀x ∈ (x0 − ρ, x0 + ρ),

                                              1 ′′                           f (h) (x0 )
       f (x) = f (x0 ) + f ′ (x0 )(x − x0 ) +    f (x0 )(x − x0 )2 + · · · +             (x0 )h +
               |                              2!    {z                           h!           }
                                            polinomio di Taylor di ordine h
                                                                              ∞
                                                                              X f (n) (x0 )
                                                                         +                     (x − x0 )n
                                                                                      n!
                                                                              n=h+1
                                                                              |         {z              }
                                                                                       resto

Avremo quindi che su ogni intervallo [a, b] ⊂ (x0 − ρ, x0 + ρ):
• polinomio di Taylor converge a f uniformemente (per h → ∞),
• resto converge a 0 uniformemente



                                                                                                            4 / 23
Esempio
Non tutte le funzioni di classe C ∞ sono sviluppabili in serie di Taylor. Infatti
                                        −1/x 2
                                         e        se x ̸= 0
                              f (x) :=
                                         0        se x = 0

Non è sviluppabile in serie di Taylor di centro 0.
Infatti: f ∈ C ∞ (dimostrate)e per ogni n, risulta f (n) (0) = 0 (dimostrate).
tutti i polinomi di Taylor di f di centro 0 sono il polinomio nullo,
quindi laP serie di Taylor di f è la funzione nulla,
ma f ̸= n≥0 0 = 0.




                                                                                    5 / 23
Teorema (Condizione necessaria e sufficiente per la sviluppabilità)
Sia I intervallo aperto, f ∈ C ∞ (I ), x0 ∈ I .
f è sviluppabile in serie di Taylor in x0 se e solo se
esistono M > 0, δ > 0, r > 0 tali che
                                                                           n!M
                            ∀x ∈]x0 − δ, x0 + δ[, ∀n ≥ 0 : |f (n) (x)| ≤       .
                                                                            rn

In particolare, se la successione f (n) è equilimitata in un intorno di x0 allora f è
sviluppabile in serie di Taylor in x0 .
Esplicitando: se Esistono M > 0, δ > 0 tali che

                             ∀x ∈]x0 − δ, x0 + δ[, ∀n ≥ 0 : |f (n) (x)| < M
                 ∞ (n)
                   f (x0 )
                              (x − x0 )n
                 P
allora f (x) =         n!
                                           ∀x ∈]x0 − δ, x0 + δ[.
                 n=0

(senza dim)
Usando il teorema si puo’ dimostrare che se f e g sono sviluppabili in serie di Taylor in x0
  1 allora anche f + g e αf (α ∈ R) sono sviluppabili in serie di Taylor in x0 (facile)

  2 allora anche f · g è sviluppabile in serie di Taylor in x0 (meno immediato)

  3 Se f è sviluppabile in serie di Taylor in x0 , g è sviluppabile in serie di Taylor in

     y0 = f (x0 ), allora g ◦ f è sviluppabile in serie di Taylor in x0 (difficile).
                                                                                          6 / 23
Osserviamo che se una funzione continua f è dispari allora f (0) = 0. Se essa è anche
derivabile, la sua derivata è pari.
Analogamente se una funzione pari è derivabile allora la sua derivata è dispari.
Pertanto se una funzione f ∈ C ∞ è dispari, la derivata seconda sarà dispari e f (2) (0) = 0.
Iterando avremo che f (2k) (0) = 0 per ogni k.
Analogamente se e f ∈ C ∞ è pari, avremo che f (2k+1) (0) = 0 per ogni k.
Quindi se una funzione f è sviluppabile in serie di Taylor in 0
• se f è dispari, nel suo sviluppo di Taylor tutti i coefficienti pari sono nulli.
                                               ∞
                                               X
                                     f (x) =         a2n+1 x 2n+1
                                               n=0


• se f è pari, nel suo sviluppo di Taylor tutti i coefficienti dispari sono nulli.
                                                 ∞
                                                 X
                                       f (x) =         a2n x 2n
                                                 n=0


In ogni caso basterà studiare cosa succede per x > 0.




                                                                                            7 / 23
Elenchiamo alcune serie di Taylor notevoli con relativa somma e raggio di convergenza:
                        ∞
                        X xn
            ex      =              ,       ρ = +∞
                        n=0
                              n!
                         ∞
                        X     (−1)n 2n+1
          sin x     =                 x  ,                 ρ = +∞
                        n=0
                            (2n + 1)!
                        ∞
                        X (−1)n
          cos x     =             x 2n ,           ρ = +∞
                        n=0
                            (2n)!
                         ∞
                               !                                   !
                α
                        X    α n                               α           α(α − 1) · · · (α − n − 1)
      (1 + x)       =           x ,               ρ = 1,               =
                        n=0
                             n                                 n                       n!
                        ∞
                        X (−1)n+1
    log(1 + x)      =                      x n,      ρ=1
                        n=1
                                       n
                         ∞
                        X   (−1)n 2n+1
       arctan x     =              x                 ρ=1
                        n=0
                            2n + 1




                                                                                                        8 / 23
Esempio 1 Sappiamo (vedi Analisi 1) che
                            ∞
                            X 1
                     ex =            xn     con raggio di convergenza ρ = ∞.
                            n=0
                                n!
⇒ la funzione esponenziale e x è sviluppabile in serie di potenze su R.
                       e x + e −x
Esempio 2 cosh x =                . Per ogni x ∈ R, sommo e poi moltiplico per 12 le identità
                            2
                       +∞                      +∞             +∞
                       X    1 n                X    1         X   (−1)n n
                ex   =         x ,      e −x =        (−x)n =            x
                       n=0
                            n!                 n=0
                                                   n!         n=0
                                                                    n!
                e x + e −x            P 1 + (−1)n 1 n
                                      +∞
per ottenere               = cosh x =                  x
                     2         (      n=0   2       n!
                                 1−1
                      1+(−1)n      2
                                     = 0 se n è dispari
          Si ha          2
                              = 1+1
                                   2
                                     = 1 se n è pari, cioè n = 2j per un j ≥ 0
⇒    la funzione cosh x è sviluppabile in serie di potenze su R, e
                                                      +∞
                                                      X    x 2j
                                           cosh x =
                                                      j=0
                                                          (2j)!
In modo simile, si ha che la funzione sinh x è sviluppabile in serie di potenze su R, e
                                                     +∞
                                                     X     x 2j+1
                                          sinh x =
                                                     j=0
                                                         (2j + 1)!
                                                                                           9 / 23
Esempio 3 Sappiamo che
                             ∞
                       1    X
                          =     xn        con raggio di convergenza ρ = 1,
                      1−x   n=0

                     1
⇒ la funzione x 7→ 1−x  è sviluppabile in serie di potenze su (−1, 1).
Esempio 4 Grazie all’Esempio 3 e ai teoremi precedenti abbiamo che ∀x ∈ (−1, 1)
                 Zx              ∞ Z      x    ∞               ∞
                        1       X             X    1          X   xm
                           dt =      t n dt =         x n+1 =
                       1−t      n=0           n=0
                                                  n+1         m=1
                                                                  m
                  0                   0
                                     ∞             Zx
                                     X xm                1
                                ⇒              =            dt = − ln(1 − x).
                                     m=1
                                         m              1−t
                                                   0

Quindi la funzione x 7→ ln(1 − x) è sviluppabile in serie di potenze su (−1, 1), e
                                                        ∞
                                                        X xm
                                    ln(1 − x) = −
                                                        m=1
                                                              m

Scambiando x con −x otteniamo anche la formula
                      ∞             ∞                          ∞
                      X (−x)m       X −(−1)m x m              X           xm
    ln(1 + x) = −               =                       =         (−1)m+1      ∀x ∈ (−1, 1)
                      m=1
                            m       m=1
                                              m               m=1
                                                                          m

                                                                                              10 / 23
Riassumendo, abbiamo che
                                                ∞
                                               X           xn
                                 ln(1 + x) =       (−1)n+1                                (1)
                                               n=1
                                                           n
con convergenza totale su ogni intervallo [a, b] ⊂ (−1, 1),
e quindi anche con convergenza puntuale assoluta su (−1, 1).
                                                     ∞
                                                    X          1
Inoltre la serie a destra in (1) nel punto x = 1 è     (−1)n+1 che converge per il
                                                    n=1
                                                               n
teorema di Leibniz.
Usando il Teorema di Abel, abbiamo che la convergenza è uniforme in [0, 1] e la somma
della serie è continua anche in x = 1.
Possiamo quindi concludere
      la serie in (1) converge uniformemente (e quindi puntualmente) alla funzione
                                       x 7→ ln(1 + x)
                      anche su ogni intervallo del tipo [a, 1] ⊂ (−1, 1].
   Su intervalli di questo tipo la convergenza NON è totale e NON è puntuale assoluta.
                                                         ∞
                                                           1
                                                         P
   Infatti la serie dei valori assoluti in x = 1 diventa   n
                                                             che diverge.
                                                        n=1
   In particolare, per x = 1 otteniamo dalla (1) (si ricordi il criterio di Leibnitz )
    ∞                                                                    ∞
    X (−1)m+1             1  1 1                                         X (−1)m+1
                  =1−       + − + · · · = ln 2 ∈ R ,          anche se                   =∞
    m=1
            m             2  3 4                                         n=1
                                                                                 m
                                                                                          11 / 23
                                                                                     ∞
                                                                                       xm
                                                                                     P
La traccia dell’esercizio poteva essere : Determinare la somma della serie                 m
                                                                                     m=1
La serie ha raggio di convergenza ρ = 1, converge in x = −1 e non converge in x = 1.
Sia f la somma della serie (che è la funzione che dobbiamo determinare).
Derivando termine a termine abbiamo
                                    ∞               ∞
                                    X               X                                 1
         ∀x ∈] − 1, 1[: f ′ (x) =         x m−1 =         x n = serie geometrica =
                                    m=1             n=0
                                                                                     1−x

Pertanto, integrando
                                  Z x
                                         1
                f (x) − f (0) =             dt = − ln(1 − x),        ∀x ∈] − 1, 1[
                                    0   1−t
e poiché f (0) = 0 abbiamo
                           ∞
                           X xm
                                        = − ln(1 − x)       ∀x ∈ [−1, 1[
                           m=1
                                  m




                                                                                               12 / 23
Ritorniamo alla serie in (1), cioè:
                                                       ∞
                                                      X           xn
                                        ln(1 + x) =       (−1)n+1                      (1)
                                                      n=1
                                                                  n

Ricordiamo il teorema di Leibniz (analisi 1)
Teorema.
P∞        Sia bn ≥ 0 una successione infinitesima e decrescente. Allora la serie
          n
  n=1 (−1) bn converge e si ha la seguente stima

                                  ∞
                                  X            k
                                               X
                              |     (−1)n bn −   (−1)n bn | ≤ bk+1 .
                                  n=1             n=1


Applichiamo il teorema con bn = n1 x n con x ∈ [0, 1] ottenendo che la serie converge per
ogni x ∈ [0, 1] e posto f (x) la somma della serie, abbiamo che
                              k
                             X          xn    x k+1     1
                  |f (x) −       (−1)n+1 | =≤       ≤                  ∀x ∈ [0, 1]
                             n=1
                                        n     k + 1   k + 1

Oss. Abbiamo riottenuto la convergenza uniforme (che già sapevamo) e in questo caso
abbiamo anche una stima esplicita della velocità di convergenza ovvero una stima
uniforme del resto.


                                                                                       13 / 23
Esempio 5 Dalla serie geometrica di ragione −t 2 otteniamo
                                                  ∞              ∞
                              1          1       X              X
            ∀t ∈ (−1, 1),        2
                                   =           =     (−t 2 )n =     (−1)n t 2n
                             1+t     1 − (−t )
                                            2
                                                 n=0            n=0
                        1
⇒ la funzione t 7→ 1+t    2 è sviluppabile in serie di potenze su (−1, 1).
A sinistra compare la derivata della funzione arcotangente;
                                 Zx                ∞ Zx                 ∞
                                       1          X          n 2n
                                                                       X    (−1)n 2n+1
    ∀x ∈ (−1, 1), arctan x =              2
                                            dt =         (−1) t   dt =             x   .
                                     1+t          n=0                  n=0
                                                                            2n + 1
                                 0                   0

la funzione x 7→ arctan x è sviluppabile in serie di potenze su (−1, 1), e
                                             ∞
                                             X (−1)n
                                arctan x =                x 2n+1                           (2)
                                             n=0
                                                 2n + 1
con convergenza totale su ogni intervallo [a, b] ⊂ (−1, 1) e quindi anche con convergenza
puntuale assoluta su (−1, 1).
                                       ∞
                                       P (−1)n
Inoltre nei punti x = ±1 la serie è ±    2n+1
                                                che converge per il teorema di Leibniz.
                                      n=0
Applicando il teorema di Abel, la serie in (2) converge uniformemente (quindi
puntualmente) alla funzione arctan anche in [−1, 1] (quindi in ogni suo sottointervallo).
In [−1, 1] la convergenza NON è totale e NON è puntuale assoluta.
                        ∞
                       X   (−1)m           1    1   1                    π
Per x = 1 abbiamo                  = 1 − + − + · · · = arctan 1 = .
                       m=0
                           2m +  1         3    5   7                    4
                                                                                           14 / 23
Il risultato di convergenza uniforme in [−1, 1], lo si può ottenere come in precedenza
usando il teorema di Leibniz che ci permette di stimare anche l’errore commesso.
Quindi dalla relazione
                                                         ∞
                                                         X (−1)n
                           ∀x ∈ (−1, 1),    arctan x =                x 2n+1 ,                (2)
                                                         n=0
                                                             2n + 1

essendo dispari, possiamo studiare per x > 0 ossia la convergenza uniforme in [0, 1].
                                             1
Applichiamo il teorema di Leibniz con bn = 2n+1 x 2n+1 otteniamo

   ∞                       k
   X (−1)n                 X (−1)n                      1                       1
                x 2n+1 −                x 2n+1 ≤                x 2(k+1)+1 ≤        ∀x ∈ [0, 1]
   n=0
       2n + 1              n=0
                               2n + 1              2(k + 1) + 1              2k + 3

abbiamo la convergenza uniforme in [0, 1], e per disparità anche in [−1, 0], quindi in
[−1, 1].




                                                                                              15 / 23
 Esempio 6 Le funzioni cos x, sin x sono sviluppabili in serie di potenze su R. Infatti tutte
le loro derivate sono limitate e applicando il teorema (sulla sviluppabilità) enunciato
abbiamo la tesi.
Calcolando le derivate di sin e cos in 0 abbiamo che gli sviluppi di centro 0 sono
                           +∞                                       +∞
                           X  (−1)n                                 X      (−1)n 2n+1
            (c) cos x =                  x 2n ,     (s) sin x =                    x  .
                           n=0
                                 (2n)!                               n=0
                                                                         (2n + 1)!
e le convergenza sono uniformi su ogni limitato. Dobbiamo dimostrare solo la conv.
uniforme, ma questa segue dal calcolo del raggio di convergenza che è +∞ (dimostrate).
Ulteriore dimostrazione 1) usare Leibniz come in precedenza (fate esercizio)
   Ulteriore dimostrazione 2) (analisi 1) Ci limitiamo alla dimostrazione per la funzione cos x, ed
   essendo pari al caso x > 0
   Fissato x > 0, scriviamo la seguente formula di Taylor con resto di Lagrange:
                                             n
                                             X (−1)k              (−1)n+1 2n+2
              ∃ξx,n ∈ (0, x) :     cos x =               x 2k +             x  cos ξx,n
                                             k=0
                                                 (2k)!            (2n + 2)!
                               n
                               X (−1)k              (−1)n+1 2n+2              x 2n+2
               ⇒     cos x −               x 2k =             x  cos ξx,n ≤
                               k=0
                                   (2k)!            (2n + 2)!               (2n + 2)!

   Abbiamo dimostrato che vale (c) per ogni fissato x ∈ R (solo convergenza puntuale). Se
   x ∈ [0, b] allora
                                     n
                                    X   (−1)k 2k         b 2n+2
                           cos x −             x    ≤            →0
                                    k=0
                                        (2k)!          (2n + 2)!

                                                                                               16 / 23
Esercizi svolti                                      ∞
                                                     X
1) Calcolare, per gli x ∈ R per cui esiste, la somma   n x n−1
                                                                   n=1
Il raggio di convergenza della serie è ρ = 1. Inoltre non converge in ±1.
Possiamo applicare il (TPLSSD) per dire che
               ∞
               X                  ∞
                                  X                  ∞
                                                    X            ′
                      n x n−1 =         (x n )′ =            xn
                n=1               n=1                n=1
                                   ∞                ′                 ′
                                  X
                                           n
                                                                 1          1
                             =            x −1           =           −1 =
                                   n=0
                                                                 1−x      (1 − x)2




                                                                                     17 / 23
                                                  P∞          x n+1
2)Determinare la somma della serie di potenze          n=1
                                                             n2 + n
    Raggio di convergenza ρ = 1.
    la serie converge in x = 1 e x = −1, pertanto la serie converge uniformemente in
    [−1, 1] (usando la definizione si vede che converge totalmente in [−1, 1]).
    Sia f la somma ndella serie. Derivando termine a termine si ottiene la serie
                   x
    f ′ (x) = ∞
             P
               n=1
                   n
    che corrisponde alla serie di Taylor della funzione f (x) = − log(1 − x), cioè
                           ∞
                           X xn
                                     = − log(1 − x)           ∀ x ∈ (−1, 1)
                           n=1
                                 n

    per il teorema di integrazione per serie, si ha, per ogni x ∈ (−1, 1)
                              ∞ Z x n                 Z x
                              X    t
                                             dt = −         log(1 − t) dt
                              n=1    0   n             0


    ovvero, mettendo insieme tutte le informazioni
           ∞              Z x
          X    x n+1
                     = −      log(1 − t) dt = x + (1 − x) log(1 − x) ∀x ∈ [−1, 1].
          n=1
              n2 + n       0



                                                                                       18 / 23
                                                                   ∞
                                                                   X
3) Calcolare, per gli x ∈ R per cui esiste, la somma                     n2x n
                                                                   n=1
(ρ = 1 e non converge in ±1)
        ∞
        X       X∞                         ∞
                                             X                 ∞
                                                               X
          n2x n=     n(n − 1)x n + nx n =x 2   n(n − 1)x n−2+x   nx n−1
         n=1      n=1                                      n=2                   n=1
                     ∞
                     X              ∞
                                    X                ∞
                                                    X   ′′   ∞
                                                              X    ′
                =x 2   (x n )′′ + x   (x n )′ = x 2    xn + x    xn
                         n=2              n=1                    n=2             n=1
                          ∞
                         X                     ′′         ∞
                                                           X             ′
                =x 2               xn − 1 − x         +x         xn − 1
                             n=0                           n=0

                     2
                             1      ′′  1    ′   2x 2        x
                =x               −1−x +x      −1 =          +
                             1−x          1−x      (1 − x)3   (1 − x)2




                                                                                       19 / 23
                                                                                     2
4) Calcolare lo sviluppo in serie di potenze delle funzioni x 7→ e x ,                     x 7→ e 2x
                           ∞
                           X 1
Sappiamo che        et =              tn   con raggio di convergenza ρ = ∞.
                           n=0
                                 n!
Basta allora sostituire t con x 2 e poi con 2x per trovare
                      ∞                             ∞                  ∞
                2     X 1                           X 1                X 2n
              ex =               x 2n ,    e 2x =            (2x)n =            xn       (ρ = ∞).
                      n=0
                          n!                        n=0
                                                        n!             n=0
                                                                           n!

                                                                                            ∞
                                                                                              1
                                                                                                      2n = e 2 .
                                                                                            P
Possiamo dedurne le somme di alcune serie numeriche, ad esempio                                  n!
                                                                                           n=0




                                                                                                                   20 / 23
                                   R1       2
5) Calcolare erf (1) = √2π          0
                                        e −x dx con un errore di 1/1000
                         2
Lo sviluppo di e −x è
                                                           ∞
                                                    2      X (−1)n
                                                e −x =                  x 2n
                                                           n=0
                                                                   n!
Per stimare l’errore nel considerare la somma parziale al posto della funzione, possiamo
usare sia il teorema di Taylor con resto di Lagrange, che in questo caso il teorema di
Leibniz.
                                         k
                                   2   X    (−1)n 2n
                               e −x =            x + Rk (x)
                                        n=0
                                              n!
e per x > 0
                                                                  x 2k+2
                                                 |Rk (x)| ≤
                                                                 (k + 1)!
                     k
 R1      2        R1 P (−1)n                R 1 x 2k+2
  0
      e −x dx −     0         n!
                                   x 2n ≤       0 (k+1)!
                                                                     1
                                                           dx = (k+1)!(2k+3)
                        n=0
                                            k
                                   2 X (−1)n             2          1
                        erf (1) − √                   ≤ √
                                    π n=0 n! (2n + 1)     π (k + 1)!(2k + 3)
Scegliamo k in modo tale che (k + 1)! (2k + 3) > 1000 √2π ≈ 1129
(per k = 4 abbiamo (k + 1)! (2k + 3) = 1320 una stima dell’errore di 0.85/1000 ) Quindi
             4
                 (−1)n
erf (1) ≈ π2                   5651
                         = √2π 7560
             P
               n! (2n+1)
                                    ≈ 0.84344 (una stima migliore erf (1) = 0.84270..)
              n=0
                                                                                       21 / 23
                                                    R1      2
5) Soluzione alternativa Calcolare erf (1) = √2π    0
                                                         e −x dx con un errore di 1/1000
                   2
Lo sviluppo di e −x è
                                              ∞
                                        2     X (−1)n
                                     e −x =               x 2n
                                              n=0
                                                    n!
Per il (TPLSSI) abbiamo che
        Z 1           Z 1X∞            ∞ Z           ∞
                2            (−1)n 2n X 1 (−1)n 2n X (−1)n
            e −x dx =             x =           x =                12n+1
         0             0 n=0   n!     n=0  0 n!     n=0
                                                        (2n + 1)n!
ovvero
                                                ∞
                                          2 X (−1)n
                               erf (1) = √
                                           π n=0 (2n + 1)n!
Per stimare l’errore che commetto nel considerare la somma parziale al posto della
funzione con il teorema di Leibniz.
                                 k
                             2 X (−1)n             2          1
                  erf (1) − √                   ≤ √
                              π n=0 n! (2n + 1)     π (k + 1)!(2k + 3)

Scegliamo k in modo tale che (k + 1)! (2k + 3) > 1000 √2π ≈ 1129
(per k = 4 abbiamo (k + 1)! (2k + 3) = 1320 una stima dell’errore di 0.85/1000 ) Quindi
             4
                 (−1)n
erf (1) ≈ π2                   5651
                         = √2π 7560
             P
               n! (2n+1)
                                    ≈ 0.84344 (una stima migliore erf (1) = 0.84270..)
           n=0
                                                                                           22 / 23
Serie di potenze di punto iniziale x0 ̸= 0
Esempio: la funzione f (x) = ln x è sviluppabile in serie di potenze (o di Taylor) di punto
iniziale x0 = 1 e raggio di convergenza ρ = 1.
                                  1                             1
ln(x) = ln(1) + (D ln)(1)(x − 1) + (D 2 ln)(1)(x − 1)2 + · · · + (D n ln)(1)(x − 1)n + · · ·
                                  2                             n!

                                  1                           1
              ln(x) = (x − 1) −     (x − 1)2 + · · · + (−1)n−1 (x − 1)n + · · ·
                                  2                           n

(ovviamente ottenibile da ln(1 + x) attraverso una traslazione)
Esempio. La funzione esponenziale di punto iniziale x0 = 1
                               1                              1
e x = e 1 + (D exp)(1)(x − 1) + (D 2 exp)(1)(x − 1)2 + · · · + (D n exp)(1)(x − 1)n + · · ·
                               2                              n!


                                       e                   e
                e x = e + e(x − 1) +     (x − 1)2 + · · · + (x − 1)n + · · ·
                                       2                   n!
con raggio di convergenza +∞.




                                                                                         23 / 23
