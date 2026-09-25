---
fonte: "06-SerieDiFunzioni-25-04-17.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Serie di funzioni


    Lorenzo D’Ambrosio
lorenzo.dambrosio@uniud.it



       17 aprile 2025




                             1/1
Definizione
Sia X 6= ∅, per ogni n ∈ N sia fn : X → R. Definiamo somma parziale n-esima
associata a (fn )n , la funzione
                           n
                           X
               Sn (x) :=         fk (x) = f1 (x) + f2 (x) + · · · + fn (x),     ∀x ∈ X
                           k=1

Chiamiamo serie di funzioni di termine generale fn la successione di funzioni (Sn )n
che indicheremo con
                              X                                  ∞
                                                                 X
                                    fn       oppure con                f n .a
                              n≥1                                n=1

  a
      La serie può partire anche da n = 0 o ad esempio n = 2 a seconda dei casi.
                                                     P
Nota:
P     Per ogni x ∈ X, la serie di funzioni             n≥1 fn determina la serie numerica
  n≥1 n (x), che si è già studiato.
      f




                                                                                            2/1
Esempi fondamentali di serie numeriche (Analisi 1)
                  P∞ n                                                    1
Serie geometrica.   n=0 q converge se e solo se −1 < q < 1 (e converge a 1−q )
                              P∞ 1
Serie armonica generalizzata.   n=0 nα converge se e solo se α > 1

Altri esempi dall’analisi 1
      P       x                        P     nx                      P                x2n
 a)         3 + n2
                   su [0, ∞)      b)        4 + x4
                                                                c)         n arctan
      n≥1 x                            n≥1 n                         n≥1               n

                                                                           2n x2n
            xn (1 − x)                       (1 − x)n x
      P                                P                             P
 d)                               e)                            f)              2 n
      n≥1                              n≥1                           n≥0 (1 + x )


                          2            P ln(n2 x2 + 1)
            n3 e−nx                                                        nx sin n+1
                                                                                   1
      P                                                              P
 g)                               h)                            i)
      n≥1                              n≥1 1 + n2 x2                 n≥1

                 √
      P n−           n+1               P nx + n2 + 2                 P n4 + n2 + 4
 l)                               m)                            n)
      n≥1        nx                    n≥1 n4 + 1                    n≥1 nx + n

                     x                 P 2n−1 (arctan x)n            P 2n+1 (sin x)2n
            2n sin
      P
 o)                               p)                            q)
      n≥0            3n                n≥1     π n−1                 n≥1   3n−1


                                                                                        3/1
Definizione
Se (Sn )n converge puntualmente in X con funzione limite puntuale f (1 ), diciamo
che la serie di funzioni di termine generale (fn )n converge puntualmente in X con
funzione somma puntuale f in tal caso scriveremo
                                                     ∞
                                                     X
                                                f=         fn .
                                                     n=1

 Se (Sn )n converge uniformemente in X con funzione limite uniforme f (2 ), diciamo
che la serie di funzioni di termine generale (fn )n converge uniformemente in X con
funzione somma uniforme f .

Diremo brevemente che f è la somma puntuale/uniforme della serie ∞
                                                                      P
                                                                        n=1 fn .




  1
      ossia ∀x ∈ X risulta che Sn (x) → f (x)
  2
      ossia kSn − f kL∞ (X) → 0
                                                                                     4/1
Osserviamo che se la serie converge uniformemente significa esplitamente
                 n
                 X            ∞
                              X                          n
                                                         X                ∞
                                                                          X
           lim         fk −         fn       = lim sup         fk (x) −         fn (x) = 0.
          n→∞                                 n→∞ x∈X
                 k=1          n=1        ∞               k=1              n=1

o se indichiamo con f la somma della serie
                        n
                        X                                n
                                                         X
                 lim          fk − f         = lim sup         fk (x) − f (x) = 0.
                 n→∞                          n→∞ x∈X
                        k=1              ∞               k=1


Ovviamente si ha il seguente

Teorema
Se la serie converge uniformemente allora converge anche puntualmente.




                                                                                              5/1
Definizione
        P
La serie Pn≥1 fn converge puntualmente assolutamente se ∀ fissato
                                                              P∞x ∈ X, la serie
numerica n≥1 fn (x) converge assolutamente cioè, se ∀x ∈ X,    n=1 |fn (x)| ∈ R.

Nota: Dall’Analisi 1 sappiamo che
P         converge               P           converge
  n≥1 fn                      ⇒ n≥1 fn                    ⇒ fn → 0 puntualmente
          puntualmente ass.                  puntualmente


Teorema
  P
    n≥1 fn converge uniformemente ⇒        fn → 0 uniformemente

Dim. Per definizione, la successione delle somme parziali Sn = f1 + · · · + fn converge
uniformemente ad f , ossia Sn → f uniformemente.
Ovviamente Sn+1 → f uniformemente.
Pertanto Sn+1 − Sn → f − f = 0 uniformemente.
Basta riconoscere che fn+1 = Sn+1 − Sn per avere la tesi.




                                                                                    6/1
Attenzione:                           P
• fn → 0 uniformemente NON implica che n≥1 fn converge unif.

Esempio
fn (x) = n1 . Sappiamo
                   P che fn → 0 uniformemente vista l’indipendenza di fn dal
particolare x, ma n≥1 fn non converge essendo la serie armonica.
  P                                            P
• n≥1 fn converge uniformemente NON implica che n≥1 fn conv. punt.
assolutamente
Esempio
             n
fn (x) = (−1)
                               P
           n
               . Sappiamo che n≥1 fn converge per il criterio di Leibnitz e vista
l’indipendenza di fn dal particolare x la convergenza è uniforme. Ma non converge
assolutamente.
Si osservi che per poter applicare la definizione di convergenza uniforme, ovvero
                                n
                                X                ∞
                                                 X
                          lim         fk (x) −         fn (x)   =0
                          n→∞
                                k=1              n=1∞

bisogna conoscere, per ogni fissato x ∈ I, la somma ∞
                                                   P
                                                    n=1 fn (x). In generale è
difficile stabilire se una serie di funzioni converge uniformemente, perché sappiamo
che solo in pochi casi si riesce a calcolare la somma di una serie numerica.
                                                                                        7/1
Definizione (Convergenza totale)
                      P
Diremo che la serie n≥1 fn converge totalmente se per ogni n ≥ 1 la funzione fn è
limitata, ed inoltre, la serie     X
                                       kfn k∞
                                         n≥1

converge (come serie numerica).
La convergenza totale è la più forte (ed è facile da stabilire): vale infatti il seguente
risultato.
Teorema
                                 P
    X                           1. Pn≥1 fn
                                                        conv. punt. assolutamnente
        fn converge totalmente ⇒ 2.    n≥1 fn            converge uniformemente
                                
    n≥1                         
                                 3. fn → 0               uniformemente

Dim 1. Sia x ∈ X fissato. Devo far vedere che la succ. |f1 (x)| + · · · + |fn (x)|
converge. In questo caso basta far vedere che non diverge:
                                                                      X
          |f1 (x)| + · · · + |fn (x)| ≤ ||f1 ||∞ + · · · + ||fn ||∞ ≤   kfn k∞ < ∞
                                                                 n≥1


Non dimostriamo 2.
2. ⇒ 3. già visto                                                                         8/1
Teorema
Sia (X, d) uno spazio metrico. Sia (fn )n una successione di funzioni X → R.
Supponiamo    che le funzioni siano continue in x0 ∈ X.
Se n≥1 fn converge uniformemente ⇒ la funzione somma x ∈ X 7→ ∞
   P                                                                  P
                                                                         n=1 fn (x) è
continua in x0 .
In particolare se le funzioni sono continue su X allora la somma è continua su X.

Dim. ....




                                                                                     9/1
                                                 n
                                   P
Esempio: la serie geometrica           n≥0 x

                               P       n
Esempio: la serie geometrica   n≥0 x       .
Si ha che:
    Converge puntualmente assolutamente (solo) su ( −1, 1 ), e
                               ∞
                               X                1
                                     xn =          ∀x ∈ (−1, 1)
                               n=0
                                               1−x

    Non converge uniformemente su (−1, 1) ma converge uniformemente su ogni
    intervallo chiuso [a, b] ⊂ (−1, 1);
    Non converge totalmente su (−1, 1) ma converge totalmente su ogni intervallo
    chiuso [a, b] ⊂ (−1, 1)




                                                                               10 / 1
                                       n
                               P
Esempio: serie geometrica         n≥0 x : Convergenza puntuale


Convergenza puntuale : vedi Analisi 1
                 n
                 X                                                1
                       xk = (1 + x + x2 + · · · + xn )(1 − x)
                                                                 1−x
                 k=0
                                                         !
                     1 − xn+1          poiche0 |x| < 1            1
                   =          →                              →
                       1−x               per n → ∞               1−x




                                                                       11 / 1
                                       n
                               P
Esempio: serie geometrica         n≥0 x : Convergenza uniforme


 Convergenza uniforme: la serie n≥0 xn non converge uniformemente a 1−x
                                                                     1
                                P
                                                                        su
(−1, 1)
               n
                     !
               X   k       1              1 − xn+1    1
        sup      x     −       = sup               −
      x∈(−1,1)           1 − x   x∈(−1,1)   1−x      1−x
                k=0

                                                xn+1            |x|n+1
                                   =    sup           = sup            =∞    !!!
                                       x∈(−1,1) 1 − x  x∈(−1,1) 1 − x


Convergenza uniforme su ogni intervallo chiuso [a, b] ⊂ (−1, 1): Basta dimostrare che
per ogni fissato R ∈ (0, 1) c’è convergenza uniforme su [−R, R]. Infatti procedendo
come prima,
                  n
                         !
                 X     k         1               |x|n+1   Rn+1
        sup          x     −         = sup              ≤      → 0 per n → ∞
     x∈[−R,R]                 1−x       x∈[−R,R] 1 − x    1−R
                k=0




                                                                                   12 / 1
                                   n
                            P
Esempio: serie geometrica     n≥0 x : Convergenza uniforme

                                  P        n                              1
 Convergenza uniforme: la serie       n≥0 x non converge uniformemente a 1−x   su
(−1, 1)




                                                                               13 / 1
                                           n
                                 P
Esempio: serie geometrica             n≥0 x : Convergenza totale


Convergenza totale: Posto fn (x) = xn per x ∈ (−1, 1), si ha

                            kfn kL∞ (−1,1) =       sup      |xn | = 1
                                                 x∈(−1,1)


Poiché la serie numerica n≥0 1 diverge ⇒ La serie n≥0 xn NON converge
                          P                       P
totalmente su su (−1, 1)
Fissiamo R ∈ (0, 1), si ha

                 kfn kL∞ ([−R,R]) =     sup      |xn | =     sup      |x|n = Rn .
                                      x∈[−R,R]             x∈[−R,R]

                                        P         n                            P         n
Poiché R ∈ (0, 1), la serie numerica    n≥0 R        converge ⇒ La serie           n≥0 x converge
totalmente su su [−R, R]




                                                                                               14 / 1
                                    P         xn
Esempio: la serie esponenziale            n≥0 n!


 1   Converge puntualmente assolutamente su R (vedi Analisi 1) e
                                  ∞
                                  X xn
                                               = ex    ∀x ∈ R
                                  n=0
                                          n!

 2   Non converge uniformemente su R;
             xn                            X xn
         sup    =∞        ⇒    la serie               non converge uniformemente su R
         x∈R n!                                 n!
                                          n≥0

     (e quindi non converge totalmente) su R);
 3   Converge totalmente (e quindi anche uniformemente) su ogni intervallo limitato.
     Sia R > 0
                                                              ∞
                        xn          |x|n   |R|n               X Rn
                 sup       = sup         =                e              = eR < ∞   ⇒
               x∈[−R,R] n!  x∈[−R,R] n!     n!                n=0
                                                                    n!

                              ⇒     conv. totale su [−R, R]



                                                                                        15 / 1
Teorema (Integrazione per serie)
Sia [a, b] un intervallo
                    P    chiuso e limitato, (fn )n≥1 successione in C 0 ([a, b]) tale che la
serie
P∞    di  funzioni   n≥1 fn converge uniformemente su [a, b] alla funzione somma
  n=1  f n . Allora
                                 ∞
                           Z b X           !       ∞ Z b
                                                  X
                                     fn (t) dt =         fn (t)dt
                            a    n=1                n=1    a

                                                     Pn
Dim. Consideriamo le somme parziali Sn (t) :=             k=1 fk (t).    Sappiamo che
                                       ∞
                                       X
                                Sn →         fn uniformemente.
                                       n=1

Il teorema del passaggio al limite sotto segno di integrale per successioni implica
subito che
         Z bX∞              Z b                                    Z b
                 fn (t)dt =     lim Sn (t)dt = {T P LSSI} = lim        Sn (t)dt
           a n=1                a n→∞                                   n→∞    a

                                   n
                                Z bX                      n Z b
                                                          X
                      = lim              fk (t)dt = lim             fk (t)dt
                         n→∞     a k=1             n→∞          a
                                                          k=1



                                                                                         16 / 1
Teorema (Operazioni con le serie)
Sia [a, b] un intervallo chiuso e limitato,
                                        P (fn )n≥1 ,P
                                                    (gn )n≥1 successioni di funzioni
[a, b] → R tali che le serie di funzioni n≥1 fn e n≥1 gn convergano puntualmente
su [a, b]. Sia ψ : [a, b] →
                          PR una funzione. Allora
1) la serie di funzioni n≥1 (fn + gn ) converge puntualmente e
                                X                    X            X
                                      (fn + gn ) =         fn +         gn     (1)
                                n≥1                  n≥1          n≥1
                          P
2) la serie di funzioni       n≥1 ψfn converge puntualmente e
                                        X               X
                                              ψfn = ψ         fn .             (2)
                                        n≥1             n≥1
              P           P
3) se le serie n≥1 fn e n≥1 gn convergono uniformemente e ψ è limitata, allora le
serie in (1) e (2) convergono anche uniformemente.

Dim. Esercizio.




                                                                                 17 / 1
Teorema (Derivazione per serie)
Sia[a, b] un intervallo chiuso e limitato, (fn )n≥1 successione in C 1 ([a, b]) tale che
                                                 P
     ∃x0 ∈ [a, b] tale che la serie di funzioni n≥1 fn converge puntualmente in x0 ,
     la serie delle derivate n≥1 fn0 converge uniformemente.
                             P

Allora la funzione somma ∞                 1
                             P
                                n=1 fn è C ([a, b]), e

                                       ∞
                                            !0      ∞
                                      X            X
                                          fn =          fn0 .
                                    n=1         n=1

Dim. per esercizio: basta applicare il teorema di passaggio al limite sotto segno di
derivata per successioni.

Proposizione
                                                                              P
Sia E ⊆ R e sia fn una successione di funzioni continue in E. Se la serie         fn
converge uniformemente in E allora converge uniformemente in E.

Dim. Usare l’analogo per successioni.




                                                                                       18 / 1
I criteri per serie numeriche
                           p possono essere usati per le serie Pdi funzioni. Ricordiamo:
 Teorema Sia lim supn n |an | = `. Se ` < 1 allora la serie n an converge
assolutamente. Se ` > 1 la serie non converge.
                      |a    |
 Teorema Sia limn |an+1
                                                            P
                         n|
                              = `. Se ` < 1 allora la serie n an converge
assolutamente. Se ` > 1 la serie non converge.
                                             |an+1 |                      p
(Ricordiamo anche che se esiste limn→∞ |an | , allora esiste limn→∞ n |an | ed i due
limiti sono uguali, ma non valeP   l’implicazione inversa.)
Rivediamo la serie geometrica n xn . In questo caso an = xn .
                                p               p
Usando il crit. Radice: limn n |an | = limn n |xn | = |x|.
Perciò: se |x| < 1 la serie converge assolutamente, per |x| > 1 la serie non converge.
Per x = 1 e x = −1 non converge poichè....
Questa la convergenza puntuale. Come stabilire quella uniforme? Si può usare il
criterio dellapradice (o del rapporto) per stabilire la Pconvergenza totale:
Se lim supn n ||fn ||∞ < 1 allora la serie di funzioni n fn converge totalmente.
                   p
Se il limite limn n |xn | = |x| è < 1 uniformemente rispetto a x, allora possiamo
concludere la convergenza totale.
Nel caso in esame tale limite non è uniformemente < 1. Ma se scelgo R ∈ (0, 1) ho che
                                      p
               ∀x ∈ [−R, R], lim n |xn | = |x| ≤ R(< 1, uniformemente)
                               n
ovvero            q                   r                √
                                                       n
              lim n kxn k[−R,R] = lim n sup |xn | = lim Rn = R < 1
               n                    n    [−R,R]         n

Considerazioni analoghe per il criterio del rapporto.
                                                                                    19 / 1
                                                         P∞      x2n
Esercizio. Studiare la convergenza della serie              n=1 1+x2n , x ∈ R.


In generale, per studiare la convergenza di una serie di funzioni,
  1   si determina la regione A dove essa converge puntualmente
  2   si cercano i sottoinsiemi B di A dove essa converge uniformemente (ad esempio
      studiando la convergenza totale su B).

Posto
                                                 x2n
                                   fn (x) :=
                                               1 + x2n
si ha fn ∈ C(R) ∩ B(R); in particolare, 0 ≤ fn (x) ≤ 1 per ogni x ∈ R.
Iniziamo studiando la convergenza totale su R, cioè la convergenza della serie
                                      ∞
                                      X
                                            kfn k∞ .
                                      n=1

 Si vede facilmente che kfn k∞ = 1, pertanto la serie non converge totalmente




                                                                                  20 / 1
                                                         P∞     x2n
Esercizio. Studiare la convergenza della serie             n=1 1+x2n , x ∈ R.


Studiamo la convergenza puntuale, cioè la convergenza della seria numerica
                                      ∞
                                      X     x2n
                                      n=1
                                          1 + x2n

per ogni punto x fissato (come facevamo in Analisi 1).
    Verifica la condizione necessaria, osserviamo che
                                           
                                           0
                                                  se |x| < 1
                              lim fn (x) = 1/2 se |x| = 1
                                n          
                                             1     se |x| > 1
                                           

    per |x| ≥ 1, non essendo verificata la condizione necessaria per la convergenza e
    siccome il termine generale è positivo, la serie diverge
    per |x| < 1, x 6= 0, per il criterio del rapporto

                         x2n+2     1 + x2n       1 + x2n
                                 ·         = x2           → x2 < 1
                       1 + x2n+2     x2n        1 + x2n+2
    la serie converge puntualmente.

                                                                                  21 / 1
                                                           P∞    x2n
Esercizio. Studiare la convergenza della serie              n=1 1+x2n , x ∈ R.


   riassumendo, la serie converge puntualmente nell’intervallo (−1, 1) e diverge
   altrove.
   la serie non converge uniformemente su (−1, 1), infatti, se cosı̀ fosse, essa
   dovrebbe convergere uniformemente (e quindi puntualmente) anche in [−1, 1]
   perché il termine generale è continuo in [−1, 1]
   per x ∈ [−c, c] (con 0 < c < 1) si ha

                                             x2n
                                   0≤              ≤ c2n
                                           1 + x2n
   e la serie n c2n è convergente se 0 < c < 1; vi è convergenza totale, e quindi
             P
   uniforme, in ogni intervallo del tipo [−c, c] con 0 < c < 1




                                                                                      22 / 1
Esercizi.

E2.1 Studiare la convergenza delle seguenti serie di funzioni
      P         x                              P        nx               P                x2n
 a)                           su [0, ∞)   b)                        c)         n arctan
      n≥1    x3 + n2                           n≥1   n4 + x4             n≥1               n

                                                                               2n x2n
            xn (1 − x)                               (1 − x)n x
      P                                        P                         P
 d)                                       e)                        f)              2 n
      n≥1                                      n≥1                       n≥0 (1 + x )


                          2                    P ln(n2 x2 + 1)
            n3 e−nx                                                            nx sin n+1
                                                                                       1
      P                                                                  P
 g)                                       h)                        i)
      n≥1                                      n≥1 1 + n2 x2             n≥1

                 √
      P n−           n+1                       P nx + n2 + 2             P n4 + n2 + 4
 l)                                       m)                        n)
      n≥1        nx                            n≥1 n4 + 1                n≥1 nx + n

                     x                         P 2n−1 (arctan x)n        P 2n+1 (sin x)2n
            2n sin
      P
 o)                                       p)                        q)
      n≥0            3n                        n≥1     π n−1             n≥1   3n−1




                                                                                           23 / 1
Esercizi.

E2.2 Studiare la convergenza delle seguenti serie di funzioni su [0, ∞), al variare del
parametro α ∈ (0, ∞)
     X         x3α
2.1)
            2α + n2 )3/2
     n≥1 (x
     X       x
2.2)
         xα + n2
       n≥1

       X      nα x
2.3)
             n4 + x4
       n≥1


                                                                          1
E2.3 È data la successione di funzioni fn : R → R, fn (x) = x4 + e−n 2 .
i) Studiare la convergenza della successione di funzioni (fn )n ;
ii) Detto f (x) il limite puntuale della
                                     P successione di funzioni (fn )n studiare la
convergenza della serie di funzioni n≥0 |fn − f |.




                                                                                    24 / 1
