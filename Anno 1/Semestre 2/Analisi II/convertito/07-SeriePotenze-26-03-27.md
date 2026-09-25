---
fonte: "07-SeriePotenze-26-03-27.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Serie di Potenze


Lorenzo D’Ambrosio



  27 marzo 2026




                     1 / 20
D’ora in poi (in queste lezioni) (an )n≥0 indicherà una successione di numeri reali.

Definizione
Sia x0 ∈ R. Si chiama serie di potenze di coefficienti (an )n e centro x0 , la seguente serie
di funzioni                          X
                                         an (x − x0 )n
                                          n≥0


Ossia è una serie di funzioni il cui termine generale è il polinomio an (x − x0 )n
La somma parziale n-esima della serie di potenze è
           n
           X
                 ak (x − x0 )k = a0 + a1 (x − x0 ) + a2 (x − x0 )2 + · · · + an (x − x0 )n
           k=0

che è un polinomio di grado ≤ n.
L’insieme dei punti di convergenza della serie non è mai vuoto.Infatti la serie è sempre
convergente per x = x0 , dove ha somma pari ad a0 (infatti a0 + a1 0 + a2 ∗ 02 + . . . ).
Per semplicità consideriamo il caso di x0 = 0. Il caso generale lo si otterrà traslando.




                                                                                             2 / 20
D’ora in poi (in queste lezioni) (an )n≥0 indicherà una successione di numeri reali.

Definizione
Si chiama serie di potenze di coefficienti (an )n (e centro 0) la seguente serie di funzioni
                                          X
                                               an x n
                                              n≥0


La somma parziale n-esima della serie di potenze è
                         n
                         X
                                ak x k = a0 + a1 x + a2 x 2 + · · · + an x n
                          k=0

che è un polinomio di grado ≤ n.
L’insieme dei punti di convergenza della serie non è mai vuoto. Infatti la serie è sempre
convergente per x = 0, dove ha somma pari a a0 (a0 + a1 0 + a2 ∗ 02 + . . . ).



Osservazione. Le cose che diremo valgono anche quando la variabile x viene sostituita
con una variabile complessa z e i coefficienti an sono numeri complessi. Per semplicità ci
limiteremo al caso reale.


                                                                                           3 / 20
Definizione
Si dice raggio di convergenza il numero (eventualmente +∞) dato da
                                             p −1
                                  ρ = lim sup n |an |
                                                   n

                       −1              −1
con le convenzioni 0        = +∞, ∞         = 0.
Dimostreremo che
                                                          P             n
    se ρ = 0,    ∀x ̸= 0 fissato, la serie numerica          n>0 an x       NON converge;
    se 0 < ρ < ∞, si ha questa situazione:
NO convergenza               Convergenza Totale                         NO convergenza
  puntuale                                                                puntuale
                     su ogni intervallo [a, b] contenuto in (−ρ, ρ)



                −ρ            a             0                         ρ
                                                            b
    se ρ = ∞, la serie di potenze converge totalmente su ogni intervallo limitato di R.




                                                                                            4 / 20
Teorema (di struttura - Cauchy, Hadamard, Abel)
Data una serie di potenze con raggio di convergenza ρ, si ha
  1   la serie converge puntualmente e assolutamente in Bρ (0) = {x : |x| < ρ}
  2   se |x| > ρ la serie non converge in x
  3   per ogni 0 < r < ρ la serie converge totalmente in Br (0) = {x : |x| ≤ r }
  4   se la serie converge in x, allora la serie converge uniformemente nel segmento di
      estremi 0 e x.
Dim. Per x = 0 si ha convergenza. Sia x ̸= 0. Usando il criterio della radice con la
successione numerica |fn (x)| = |an x n | = |an | |x|n abbiamo che
                              p                          p          |x|
                       lim sup n |an | |x|n = |x| lim sup n |an | =     .
                           n                         n               ρ

Pertanto se |x| < 1 la serie ∞ |an x n | converge, ossia abbiamo il punto 1.
                             P
             ρ
Se |x|
    ρ
       > 1 la serie non converge, ossia il punto 2.
Per dimostrare 3 osserviamo che
                                              ∞
                                              X                   ∞
                                                                  X
                           |x| < r   =⇒             |an x n | ≤         |an |r n
                                              n=0                 n=0

e l’ultima serie converge in quanto 0 < r < ρ e per il punto 1. si ha convergenza.
Punto 4 no dim.
                                                                                          5 / 20
Osservazioni
                           P              n
Data la serie di potenze       n≥1 an x
NO convergenza             Convergenza Totale                      NO convergenza
  puntuale                                                           puntuale
                  su ogni intervallo [a, b] contenuto in (−ρ, ρ)



             −ρ            a                  0                    ρ
                                                         b
    Se la serie converge in un punto x allora ρ ≥ |x|
    Se la serie NON converge in un punto x allora ρ ≤ |x|
    Nulla sappiamo di cosa succede in −ρ e in ρ che devono essere studiati caso per
    caso. P
    Sia f = n≥1 an x n la somma della serie. f è continua in ] − ρ, ρ[.
    Se la serie converge in ρ (rispettivamente in −ρ) allora la serie converge uniformente
    in [0, ρ] (rispettivamente in [−ρ, 0]) e la somma è continua.
    Sintetizzando, la somma di una serie di potenze è sempre continua nel suo insieme
    di convergenza.
    Se la serie non converge in ρ allora la convergenza non è uniforme in [0, ρ[.
                                                   |a     |
                                                                                  p
    Abbiamo già ricordato che se esiste limn→∞ |an+1  n|
                                                            , allora esiste limn→∞ n |an | ed i
    due limiti sono uguali (ma non vale l’implicazione inversa). Quindi in questa
                                                    |a      |
    situazione possiamo calcolare ρ−1 = limn→∞ |an+1    n|
                                                                                            6 / 20
Esempi

                                                                P       n
   In corrispondenza di an = 1, otteniamo la serie di potenze   n≥0 x       che è la serie
   geometrica (e di cui conosciamo già tutto) e risulta
                      an+1
                           → 1 ⇒ raggio di convergenza ρ = 1 ⇒
                       an
                                      ∞                     
                                     X                    1
                      ⇒ ∀x ∈ (−1, 1)     x n converge =
                                     n=0
                                                        1−x

                                                  n
   In corrispondenza di an = 1/n! otteniamo n≥0 xn! che è la serie esponenziale e
                                           P
   risulta
                  an+1      1
                       =       → 0 ⇒ raggio di convergenza ρ = ∞ ⇒
                   an     n+1
                                                ∞
                                               X    xn
                                      ⇒ ∀x ∈ R         converge (= e x )
                                               n=0
                                                    n!




                                                                                              7 / 20
Esempio
                                    n
Consideriamo la serie n≥1 (−1)        x n : (È facile vedere che il raggio di convergenza è
                       P
                                  n
ρ = 1, ma in questo caso vogliamo ragionare in modo alternativo)
• poichè per x = −1 la serie conincide con la serie armonica n≥1 n1 che non converge,
                                                                       P
allora ρ ≤ 1 e sicuramente non converge per ogni |x| > 1;
                                                                                              n
• poichè per x = 1 la serie coincide con la serie armonica a segno alterno n≥1 (−1)
                                                                                   P
                                                                                            n
                                                                                                ,
che converge per il teorema di Leibniz, allora ρ ≥ 1 e convergerà per ogni |x| < 1;
 pertanto: ρ = 1, la serie converge uniformemente in ogni intervallo [a, b] ⊂] − 1, 1],
converge assolutamente in ogni intervallo [a, b] ⊂] − 1, 1[.
                            n
• posto f (x) := n≥1 (−1)     x n , allora f è continua in ] − 1, 1].
                  P
                          n




                                                                                                8 / 20
Teorema
Siano (an )P
           n e (bn )n due successioni numeriche e consideriamo le serie di potenze ad esse
associate n≥0 an x n , con raggio di convergenza ρa e la serie n≥0 bn x n , con raggio di
                                                                    P
convergenza ρb .
1) se esisteno β ≥ α > 0 tali che α|bn | ≤ |an | ≤ β|bn | definitivamente, allora ρa = ρb
2) se esisteno β ≥ α > 0 tali che α|bn | ≤ n|an | ≤ β|bn | definitivamente, allora ρa = ρb
                       |an |                              n|
In particolare se limn |bn|
                             = ℓ ∈ R \ {0} o se limn n|a
                                                       |bn |
                                                             = ℓ ∈ R \ {0}, allora ρa = ρb .
                       √
Dim.
√   p  2) Applicando
              √  p
                       n
                         · a√tuttip i membri della disuguaglianza abbiamo
 n
   α |bn | ≤ n |an | ≤ n β n |bn |. Passando al limite superiore abbiamo la tesi.
     n         n  n

La 1) è analoga.
È immediato verificare che le seguenti serie di potenze hanno lo stesso insieme di
convergenza
                     X             X              X              X
                         an x n ,      an x n+1 ,    an x n+1 ,     an x n+100 .
                   n≥0         n≥0            n≥k           n≥k


Corollario
Le seguenti serie di potenze hanno lo stesso raggio di convergenza
           X            X            X 10          X an n+1      X an n+1
               an x n ,    nan x n ,    n an x n ,        x ,          x .
                                                        n          n18
             n≥1         n≥1         n≥1             n≥1            n≥1

                                                                                          9 / 20
Esercizi.
                                         n   n    n
                                                       an = 2 n + 3 n
                                  P
  1 Studiare la serie di potenze
                                   n≥0 (2 + 3 ) x
Usando il Teorema di Cauchy-Hadamard:
                                s                            n
                                                   ln(1+( 2 ) )
                                       n
         p         √                    2                 3                      1
          n        n n
            |an | = 2 + 3 = 3 1 +
                           n     n
                                            = 3e        n       → 3e 0 = 3 ⇒ ρ =
                                        3                                        3
 o con il Teorema di D’Alambert:     n+1            n+1
|an+1 |    n+1    n+1    n+1  1+( 2 )       1+( 2 )
 |an |
        = 3 3n +2
               +2n
                     = 33n · 1+ 3 2 n = 3 · 1+ 3 2 n → 3 ⇒ ρ = 13
                                 (3)P          (3)
      / − 13 , 13 la serie numerica n≥0 (2n + 3n ) x n NON converge
                
•∀x ∈
•∀[a, b] ⊂ − 13 , 13 la serie di funzioni n≥0 (2n + 3n ) x n conv. totalmente su [a, b]
                                         P

•∀x ∈ − 13 , 13 la serie numerica n≥0 (2n + 3n ) x n converge assolutamente
                                      P

Attenzione: Non si è detto nulla di cosa succede in x = 31 e in x = − 13 .
In generale, i casi |x| = ρ vanno trattati separatamente.
In questo caso, il termine generale della serie | (2n + 3n ) ±31 n | = (2n + 3n ) 31n → 1 non è
infinitesimo, quindi la serie non converge.
Possiamo anche calcolare per x ∈ − 31 , 13 ,
      ∞                      ∞
                                        !   ∞
                                                        !
     X     n       n  n
                             X        n
                                           X          n
         (2 + 3 ) x =           (2x) +         (3x)
    n=0                     n=0             n=0
                             1          1       1 − 3x + 1 − 2x         2 − 5x
                        =          +          =                  =
                          1 − (2x)   1 − (3x)   (1 − 2x)(1 − 3x)   (1 − 2x)(1 − 3x)
                                                                                               10 / 20
Esercizi.
      Studiare la serie di potenze n≥0 (2n + 3n ) x n an = 2n + 3n
                                     P
  1

      • la serie convergese e solo se x ∈ − 31 , 31
                                                    

      • ∀[a, b] ⊂ − 31 , 13 la serie conv. totalmente su [a, b]
                              ∞
                              X                             2 − 5x
                                    (2n + 3n ) x n =
                              n=0
                                                       (1 − 2x)(1 − 3x)

      Studiare la serie di potenze n≥0 n (2n + 3n ) x n an = n2n + n3n
                                     P
  2

      In base all’esercizio 1, il raggio di convergenza di questa serie è sempre ρ = 31 .
      Bisogna solo ”ristudiare” i comportamneti di questa serie negli estremi dell’intervallo
      di convergenza:
      In questo caso, il termine generale della serie n| (2n + 3n ) ±31 n | = n (2n + 3n ) 31n → ∞
      non è infinitesimo, quindi la serie non
                                             converge.
      La serie converge se e solo se x ∈ − 31 , 13 uniformemente negli intervalli chiusi ivi
                                                   

      contenuti.
      A cosa converge? (lasciato per esercizio dopo i prossimi teoremi)




                                                                                              11 / 20
                                             xn
                                        P
  3   Studiare la serie di potenze      n≥0 2n +3
Calcoliamo il raggio di convergenza con il Teorema di D’Alambert:
                           1
               |an+1 |    n+1     2n + 3   2n     1 + 23n  1 1 + 2n
                                                                   3
                       = 2 1 +3 = n+1    = n+1 ·       3
                                                          = ·      3
                |an |     2n +3
                                 2    +3  2      1 + 2n+1  2 1 + 2n+1
                                         n
     / [−2, 2] la serie numerica n>0 2nx+3 NON converge
                                  P
•∀x ∈
                                               n
•∀[a, b] ⊂ (−2, 2) la serie di funzioni n≥0 2nx+3 conv. totalmente su [a, b]
                                       P
                                          n
•∀x ∈ (−2, 2) la serie numerica n≥0 2nx+3 converge assolutamente
                                  P
Completiamo l’esercizio considerando i punti x = ±2 : le serie
                        X        2n             X (−2)n            X (−1)n 2n
                                            e                  =
                               2n + 3                 2n + 3             2n + 3
                        n≥0                     n≥0                n≥0

                                 2n
NON convergono perché          2n +3
                                        → 1 ̸= 0 per n → ∞.




                                                                                  12 / 20
                                                                                2n 2n
                                                                          P
  4    Calcolare il raggio di convergenza della serie di potenze            n≥1 nn x
Attenzione: a0 e tutti i coefficienti relativi alle potenze dispari di x sono nulli! Scriviamo
”una” somma parziale
      n                                                                                   2n
      X 2k                                          21 2                        2n       X
                 x 2k = |{z}
                         0 ·x 0 + |{z}
                                   0 x1 +                            0 x 2n−1 + n x 2n =
                                                        x + · · · + |{z}                     am x m
            kk                                      1 1                         n        m=1
      k=1                   a0          a1         |{z}           a2n−1        |{z}
                                                    a2                         a2n
                                                   k=1                         k=n
                   (
                       0         se m è dispari
dove        am =       2k
                       se m = 2k è pari
                       kk
In particolare,                                                   
                                                          |am+1 |
• NON si può applicare il Teorema di D’Alambert.           |am |
                                                    (
                        p                p            0           se m è dispari
• Cauchy-Hadamard, m |am | ̸= m2 ma m |am | = q 2                                   →0
                                                          k
                                                                  se m = 2k è pari
                                        2n 2n
                                                                     n
                                               = n≥1 n1n 2x 2
                                 P                P
Alternativamente: scriviamo        n≥1 nn x
La serie ”ausiliaria” (t = 2x 2 ) n≥1 n1n t n ha raggio di convergenza ρ̃ = ∞. Infatti
                                 P
         q
limn→∞ n n1n = limn→∞ n1 = 0
                    n
⇒ la serie n≥1 n2n x 2n converge per |2x 2 | = |t| < ∞ ossia ∀x ∈ R (quindi, anch’essa ha
            P
raggio di convergenza ρ = ∞.)
                                                                                                      13 / 20
      Calcolare il raggio di convergenza della serie di potenze n≥0 (−1)n (8n + 1) x 3n
                                                                P
  5


Attenzione: si tratta di una serie di potenze del tipo m≥0 am x m in cui am = 0 se m non
                                                         P
è un multiplo
           P di 3 n n                                        n
                         (8 + 1) x 3n = n>0 (8n + 1) −x 3
                                         P
Scriviamo n>0 (−1)P
                               n       n
La serie ”ausiliaria” n≥1 (8 + 1) t        ha raggio di convergenza ρ̃ = 18 . Infatti

                               8n+1 + 1        8 · 8n + 1
                            lim         =  lim            =8
                            n→∞ 8n + 1    n→∞ 8n + 1



Pertanto: 1) la serie originale converge per −x 3 < 18 ,
2) la serie originale NON
                       P converge   per −x 3 > 18 ,
Conclusione: La serie n≥0 (−1) (8n + 1) x 3n ha raggio di convergenza
                                  n


                                            p      1
                                        ρ = 3 ρ̃ =
                                                   2
Cosa succede per x = 21 e x = − 12 ? È possibile calcolare la somma della serie?
                      P (−1)n n2 x−2 n
  6 Studiare la serie                   . Non è una serie di potenze!
                       n n4 +2    x+5

Riconducibile ad una serie di potenze. Con la sostituzione t = − x−2 x+5
                                                                         , diventa una serie di
potenze che ha raggio di convergenza ρ = 1 (controllate) e pertanto la serie converge per
| − x−2
    x+5
        | < 1, non converge per | − x−2
                                    x+5
                                        | > 1 [ossia x > − 32 , risp. x < − 32 (controllate)].
Dimostrate che la convergenza è assoluta e uniforme su [−3/2, +∞[
                                                                                           14 / 20
Esercizi
  7   Studiare le serie di funzioni
                                                               ∞ 
                                         3n x 2n
                                                                           
                                X                             X          1
                           a)                            b)       arctan     x n+1
                                      2 (x 2 + 1)n            n=1
                                                                         n
                                n≥0

  8   Studiare le serie di funzioni al variare di α ∈ R

                                     X (−1)n                  ∞
                                                              X arctan n
                                c)                x 2n   d)                x n+1
                                           4n nαn              n=1
                                                                     nα
                                     n≥1
                                                              n−1
    Studiare la convergenza puntuale della serie n≥1 π2 n−1 (arctan x)n e
                                                    P
  9

    calcolarne la somma puntuale, ove possibile.
    Caratterizzare inoltre gli intervalli di R su cui la serie data converge totalmente
 10 Calcolare il raggio di convergenza ρ della serie di potenze
                                                                        P        (−2)n x n
                                                                            n≥0 3n +n3 .
                                                                                       n n
    Determinare inoltre il comportamento della serie numerica n≥0 (−2)                   ρ
                                                                         P
                                                                                   3n +n3
                                                                                           .
                                                                 n+1         2n
 11 Studiare la convergenza della serie di funzioni
                                                       P       2     (sin x)
                                                          n≥1      3n−1
                                                                                e calcolarne la
    somma, ove possibile.




                                                                                                  15 / 20
Teorema (di derivazione per serie di potenze)
                                                           an x n avente somma f : (−ρ, ρ) → R,
                                                     P
Sia ρ > 0 il raggio di convergenza della serie
                                                     n≥0
                 ∞
                       an x n Allora
                 P
cioè f (x) :=
                 n=0
1) f ∈ C ∞ (−ρ, ρ).
                                       n(n − 1) . . . (n − h + 1)an x n−h ha raggio di
                                     P
2) per ogni h ≥ 0 si ha che la serie
                                       n≥h
convergenza ρ;
                                                     ∞      n!
                                       f (h) (x) =                 an x n−h
                                                     P
3) per ogni h ≥ 0 e x ∈ (−ρ, ρ),
                                                     n=h (n −  h)!
4) per ogni h ≥ 0 risulta f (h) (0) = h! ah .
In particolare,
                                      ∞
                                     X   f (n) (0) n
                            f (x) =               x        ∀x ∈ (−ρ, ρ).
                                     n=0
                                              n!

Dim. f è somma di una serie di funzioni C ∞ (fn (x) = an x n ) ed essendo la convergenza
uniforme su ogni intervallo chiuso contenuto in (−ρ, ρ) abbiamo che f è ivi continua e
f (0) = a0 . Ossia valgono le 2), 3) 4) per h = 0.
DimostriamoP   che f ∈ C 1 e che valgono le 2), 3) 4) per h = 1.
Che la serie n≥1 nan x n−1 ha raggio di convergenza ρ lo abbiamo già dedotto in
precedenza (la cui dimostrazione fa parte integrante della presente dimostrazione).

                                                                                                  16 / 20
Teorema (cont. dim. di derivazione per serie di potenze, h = 1)
                                                              an x n =: f (x).
                                                          P
Sia ρ > 0 il raggio di convergenza della serie di potenze
                                                          n≥0
....
                                      ∞
3) per ogni x ∈ (−ρ, ρ), f (1) (x) =     nan x n−1
                                      P
                                       n=1
4) f (1) (0) = 1! a1 .

Dim. Sia I ⊂ (−ρ, ρ) intervallo chiuso e limitato. Le serie n≥0 an x n =: f (x) e quella
                                                             P

delle sue derivate n≥1 nan x n−1 =: g (x) convergono uniformemente su I abbiamo, per il
                   P

(TPLSSD) che f è derivabile e vale f ′ = g (ossia la 3)
Sostituendo x = 0, otteniamo f ′ (0) = a1 (ossia la 4)
Ricapitolando, abbiamo dimostrato che la somma di una serie di potenze con raggio di
convergenza ρ > 0 è derivabile e che la sua derivata si ottiene andando a derivare i
termini generali della serie.
A questo punto ripetiamo il ragionamento per la serie f (1) (x) = ∞            n−1
                                                                    P
                                                                     n=1 nan x
                                                                 ′′
Questa è una serie di potenze, pertanto è derivabile (quindi ∃f )e la sua derivata la si
ottine andando a derivare i termini della serie
                         ′             ∞
                                         X            X∞
                 f (1) (x) = f (2) (x) =   D nan x n−1 =   n(n − 1)an x n−2
                                       n=1                  n=2

   ′′
e f (0) = 2(2 − 1)a2 . Iterate.
                                                                                       17 / 20
Teorema (integrazione per serie di potenze)
                                                                                      an x n =: f (x). Si ha che la
                                                                                 P
Sia ρ > 0 il raggio di convergenza della serie di potenze
                                                                                n≥0
serie di potenze                                 X        an n+1
                                                             x
                                                         n+1
                                                 n≥0

ha raggio di convergenza ρ e
                          Zx                ∞
                                            X     an n+1
                               f (t) dt =            x                      ∀x ∈ (−ρ, ρ).
                                            n=0
                                                n +1
                          0

Dim. Sia x ∈ (−ρ, ρ). Supponiamo che x > 0 (il caso x < 0 si tratta analogamente).
Essendo f somma di una serie di potenze, è continua, e la serie converge uniformemente
nell’intervallo [0, x]. Applicando il (TPLSSI) abbiamo
             Zx                Zx   ∞
                                                     !          ∞ Z     x                 ∞
                                    X            n
                                                                X                         X     an n+1
                  f (t) dt =              an t           dt =               an t n dt =            x
                                    n=0                         n=0 0                     n=0
                                                                                              n +1
             0                 0




                                                                                                                      18 / 20
Esercizi

Determinare il raggio di convergenza ρ delle serie di potenze ∞         n
                                                             P
                                                                n=1 an x nei casi seguenti
e studiare la convergenza agli estremi x = ρ e x = −ρ dell’intervallo di convergenza:
  1   an = nα con α ∈ R
              1                       n
  2   an =        con α ≥ 0 e bn =
           1 + αn                  1 + αn
           n!        (n + 1)!
  3   an = n e bn =
           n            nn
            √
              n
  4   an = α con α ≥ 0
           (n!)k
  5   an =       con k ∈ N \ {0}
           (kn)!




                                                                                       19 / 20
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



                                                                                      20 / 20
