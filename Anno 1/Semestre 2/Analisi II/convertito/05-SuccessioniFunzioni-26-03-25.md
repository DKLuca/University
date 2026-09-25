---
fonte: "05-SuccessioniFunzioni-26-03-25.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Successioni di Funzioni


  Lorenzo D’Ambrosio



     25 marzo 2026




                          1 / 39
Richiami successioni numeriche

     Una successione di numeri reali (an )n≥0 1 è un’applicazione che ad ogni numero
     naturale n ∈ N associa il numero reale an ∈ R

                                                 n ∈ N ⇝ an ∈ R.

     Abbiamo studiato la convergenza di (an )n≥0 ad un numero reale ℓ ∈ R o più in
     generale
                                       lim an = ℓ ∈ R̄
                                                n→+∞

     ossia
     • se ℓ ∈ R allora limn |an − ℓ| = 0, che per definizione significa

                        ∀ϵ > 0 ∃ν = ν(ϵ) ∈ N t.c. ∀n ≥ ν : ℓ − ϵ < an < ℓ + ϵ

     • se ℓ = +∞ allora

                              ∀M > 0 ∃ν = ν(ϵ) ∈ N t.c. ∀n ≥ ν : an > M

     • se ℓ = −∞ allora

                             ∀M > 0 ∃ν = ν(ϵ) ∈ N t.c. ∀n ≥ ν : an < −M
 1
     o anche (an )n≥1 e per brevità indicheremo con (an )n
                                                                                        2 / 39
Richiami successioni in spazi metrici


     Sia (M, d) uno spazio metrico una successione di elementi di M (an )n≥0 2 è
     un’applicazione che ad ogni numero naturale n ∈ N associa l’elemnto an ∈ M

                                                n ∈ N ⇝ an ∈ M.

     Abbiamo definito la convergenza di (an )n≥0 ad un elemento ℓ ∈ M

                                                  lim an = ℓ ∈ M
                                                n→+∞

     che per definizione significa, lim d(an , ℓ) = 0, o più esplicitamente
                                           n

                             ∀ϵ > 0 ∃ν = ν(ϵ) ∈ N t.c. ∀n ≥ ν : d(an , ℓ) < ϵ




 2
     o anche (an )n≥1 e per brevità indicheremo con (an )n
                                                                                    3 / 39
Definizione
Sia X ̸= ∅. Una successione di funzioni (fn )n da X in R è una applicazione che ad ogni
naturale n ∈ N associa una funzione fn : X → R, ossia
N → {funzioni X → R}, n → fn

Osserviamo che fissato x ∈ X la successione (fn (x))n è una successione di numeri reali,
ossia una successione che si è già studiato.
In tale punto x fissato, la successione (fn (x))n può essere convergente oppure ammettere
limite +∞ o −∞ o non ammettere limite.
Questo comportamento può cambiare da punto a punto.
Queste osservazioni danno luogo alla nozione di successione di funzioni convergente
puntualmente.




                                                                                        4 / 39
           1
fn (x) =
           n




               5 / 39
           1
fn (x) =     x,   x ∈ [0, 1]
           n




                               6 / 39
fn (x) = x n ,   x ∈ [0, 1]




                              7 / 39
                        
           1           1   1
fn (x) =     tanh n(x − ) + ,   x ∈ [0, 1]
           2           2   2




                                             8 / 39
Definizione (Convergenza puntuale)
Sia X ̸= ∅. Per ogni n ∈ N, sia fn : X → R.
Definiamo l’insieme

            C := {x ∈ X | la successione di numeri reali (fn (x))n converge } .


che chiamiamo insieme di convergenza puntuale di (fn )n e diciamo che la successione
(fn )n converge puntualmente in C . La funzione f : C → R, definita ponendo

                          per ogni x ∈ C ,    f (x) := lim fn (x),
                                                      n→+∞

si chiama funzione limite puntuale della successione (fn )n .
Osserviamo che in tal caso si ha
      ∀x ∈ C , ∀ϵ > 0, ∃ν = ν(ϵ, x) ∈ N t.c. ∀n ≥ ν : f (x) − ϵ < fn (x) < f (x) + ϵ
o equivalentemente
           ∀x ∈ C , ∀ϵ > 0, ∃ν = ν(ϵ, x) ∈ N t.c. ∀n ≥ ν : |fn (x) − f (x)| < ϵ.

Note - Invece di ”(fn )n converge puntualmente in C con funzione limite puntuale f ”,
diremo più brevemente ”(fn )n converge puntualmente a f in C ”; o equivalentemente
                        per ogni x ∈ C : limn→+∞ |fn (x) − f (x)| = 0.
                                                                                        9 / 39
Esempi

 Determinare l’insieme di convergenza puntuale e la funzione limite puntuale della
 successione (fn )n definita ponendo fn (x) :=
        x                    1
(1)         2
                (1bis)                         (6) x n
   r 1 + nx              1 +  nx 2                     xn
            1                                  (7) 2
(2) x 2 +                                          n + x2 
            n                                      ln 1 + x 2n
     (n + x)3                                  (8)
(3) 3                                                  n+3 
      n +1                                         arctan x 2n
(4) |arctan(x −  n)|                          (9)
                                                       xn
(5) x 2 + 3−n ln x 2 + 3−n                              e nx
                                               (10) nx
                                                    e +1
       0
              x ∈ (−∞, 0]
 (11) n        x ∈ (0, 1/n]
       
         1/x x ∈ (1/n, +∞)
       
                         2
          1 − n2 x − n2        x ∈ n1 , n3
                                          
 (12)
                 0            altrimenti
        n sin(x) x ∈ [(2n − 1)π, (2n + 1)π]
 (13)      n+1
       0             altrimenti

                                                                                     10 / 39
Osservazione Se le singole fn hanno certe proprietà (limitatezza, continuità, integrabilità,
derivabilità), non è detto che la funzione limite puntuale abbia le stesse proprietà, né che
il limite della successione delle derivate [degli integrali] coincida con la derivata [con
l’integrale] della funzione limite.
Esempi
• Una successione di funzioni limitate che ha per limite una funzione non limitata: 11
• Una successione di funzioni continue che ha per limite una funzione non continua: 6 ,
10
• Una successione di funzioni derivabili tali che la successione delle derivate non converge
alla derivata della funzione limite: 1
• Una successione di funzioni derivabili che ha per limite una funzione non derivabile: 2
• Una successione di funzioni Riemann-integrabili tali che la successione degli integrali
non converge all’integrale del limite: np x(1 − x 2 )n , x ∈ [0, 1] p ∈ R
• Una successione di funzioni integrabili che ha per limite una funzione non integrabile: .
. .
Ciononostante
 Esercizio Sia (fn )n successione puntualmente convergenti a f in C . Se tutte le fn sono
pari [dispari] [[T-periodiche]], allora anche f è pari [dispari] [[T-periodica]].




                                                                                            11 / 39
Es.5) del capitolo spazi metrici Sia X ̸= ∅. Sia B(X ) := {f : X → R| f limitata}
Per ogni f ∈ B(X ) definiamo ∥f ∥∞ := sup |f (x)| (norma uniforme/ infinito).
                                        x∈X
Quindi (B(X ), ∥ · ∥∞ ) è uno spazio vettoriale normato. La distanza indotta da questa
norma, detta distanza del sup/distanza uniforme, è

                        d(f , g ) := ∥f − g ∥∞ = sup |f (x) − g (x)|
                                                    x∈X

Data una successione di funzioni (fn )n in B(X ),
    se (fn )n converge ad f rispetto alla metrica d∞ (o norma ∥ · ∥∞ ), cioè

                        ∥fn − f ∥∞ = sup{|fn (x) − f (x)| : x ∈ X } → 0

     diremo che (fn )n converge uniformemente a f
    diremo che (fn )n converge puntualmente ad f se
                              fn (x) → f (x) in ogni punto x ∈ X
    cioè
                                 |fn (x) − f (x)| → 0     ∀x ∈ X


Queste nozioni possono essere stabilite per successioni di funzioni non necessariamente in
B(X ).

                                                                                          12 / 39
Convergenza Uniforme


Definizione (Convergenza Uniforme)
Sia X ̸= ∅. Per ogni n ∈ N, sia fn : X → R. Sia f : X → R. Diciamo che la successione
(fn )n converge uniformemente a f in X se

                               lim   sup |fn (x) − f (x)| = 0
                              n→+∞ x∈X


OSSERVAZIONE: Convergenza puntuale in X :

       ∀x ∈ X , ∀ϵ > 0, ∃ν = ν(ϵ, x) ∈ N t.c. ∀n ≥ ν : |fn (x) − f (x)| < ϵ

Convergenza uniforme in X

               ∀ϵ > 0, ∃ν = ν(ϵ) ∈ N t.c. ∀n ≥ ν : |fn (x) − f (x)| < ϵ, ∀x ∈ X .

Si ha pertanto il seguente

Teorema
Se fn converge uniformemente ad f in X =⇒ fn converge puntualmente ad f in X .

                                  NON vale il viceversa

                                                                                    13 / 39
Esempi

• Sia fn (x) := n1 per x ∈ [0, 1]. fn converge uniformemente a 0 su [0, 1]
                                                   1       1
                           sup |fn − f | = sup |     − 0| = → 0
                          0≤x≤1            0≤x≤1   n       n

• Sia fn (x) := n1 x per x ∈ [0, 1]. fn converge uniformemente a 0 su [0, 1]
                                               1        1
                          sup |fn − f | = sup | x − 0| = → 0
                         0≤x≤1           0≤x≤1 n        n

• Sia fn (x) := x n per x ∈ (0, 1). fn converge puntualmente a 0 su [0, 1), ma non converge
uniformemente in [0, 1) infatti

                           sup |fn − f | = sup |x n − 0| = 1 ̸→ 0.
                         0<x<1             0<x<1

Ma converge uniformemente in ogni intervallo [0, b] con 0 < b < 1, infatti

                          sup |fn − f | = sup |x n − 0| = b n → 0.
                         0≤x≤b            0≤x≤b




                                                                                        14 / 39
Notazione 1.             sup |fn − f | := sup |fn (x) − f (x)|
                           X               x∈X
Notazione 2. Sia g : X → R                 ||g ||L∞ (X ) := sup |g | = sup |g (x)|
                                                             X           x∈X
Ovviamente a priori puo’ accadere che ||g ||L∞ (X ) = +∞
Se è chiaro chi sia X , scriveremo  ||g ||∞ := ||g ||L∞ (X )
Pertanto

     fn → f uniformemente in X            ⇐⇒ lim ||fn − f ||∞ = 0 ⇐⇒ ||fn − f ||∞ → 0
                                                   n

Osservazione 1.    Siano f1 , f2 : X → R

               ||f1 + f2 ||∞     = sup |f1 (x) + f2 (x)| ≤ sup (|f1 (x)| + |f2 (x)|)
                                      X                          X
                                 ≤ sup |f1 (x)| + sup |f2 (x)| = ||f1 ||∞ + ||f2 ||∞
                                      X                X

Analogamente, per un numero finito qualunque di funzioni

                          ||f1 + · · · + fn ||∞ ≤ ||f1 ||∞ + · · · + ||fn ||∞

Osservazione 2. ||f ||∞ = 0 se e solo se f ≡ 0
Osservazione 3. ||λf ||∞ = |λ|||f ||∞
Poiché può accadere che ||g ||L∞ (X ) = +∞, allora ||g ||L∞ (X ) non è a pieno titolo una
norma. Ma possiamo ugualmente pensare che sia una norma con alcune accortezze (es.
nella osservazione 3 ....).
                                                                                          15 / 39
• Esempio: (Suggerimento per una possibile strategia) Studiare la convergenza della
                                                                        16 x
successione di funzioni (fn )n≥1 definita da fn : [0, ∞) → R, fn (x) = 2       .
                                                                      9x + n2

Suggerimento:
  1   Studiare la convergenza puntuale: fissare x ≥ 0 e determinare

                             f (x) := lim fn (x)     (limite dell’Analisi 1)
                                       n→∞



  2   Se tale limite esiste ed è finito, valutare

                                  ∥fn − f ∥∞ = sup |fn (x) − f (x)|
                                                 x∈[0,∞)

      A tal fine può essere utile studiare, stavolta per n fissato e x variabile, la funzione

                                          x 7→ |fn (x) − f (x)|.

      Ad esempio, si può tentare di disegnarne (velocemente!) il grafico utilizzando gli
      strumenti dell’Analisi 1.
  3   Se
                                          lim ∥fn − f ∥∞ = 0
                                          n→∞

      si ha convergenza uniforme, altrimenti solo quella puntuale.
                                                                                             16 / 39
• Esercizio. Studiare la convergenza della successione di funzioni (fn )n≥1 definita da
                                                       16 x
                          fn : [0, ∞) → R, fn (x) = 2           .
                                                     9x + n2

Si vede subito che fn → 0 puntualmente.



Fissiamo n ≥ 1 e studiamo
con gli strumenti
dell’Analisi 1, la funzione
|fn (x) − f (x)| = fn (x):




                                                     n
Si vede che la funzione fn ha massimo assoluto in xn = . Quindi
                                                     3
                                                 n     8
           ∥fn − f ∥∞ = ∥fn ∥∞ = sup fn (x) = fn    =     → 0 per n → ∞
                                x∈[0,∞)          3     3n
il che vuol dire che fn → 0 uniformemente su [0, ∞).                                      17 / 39
Esempi

 Riprendiamo gli esempi precedenti.
        x
(1)         2
              → 0, ∀x ∈ R
   r nx
    1  +
                                                             
                                                      n        0 x ∈ (−1, 1)
            1                                   (6) x   →
(2) x 2 + → |x|, ∀x ∈ R                                        1     x =1
            n                                             n
                                                        x
    (n + x)3                                    (7) 2          → 0, ∀x ∈ [−1, 1]
(3) 3          → 1, ∀x ∈ R                          n + x2        
      n +1                                                 nx      0      x ∈ (−∞, 0)
                         π                               e
(4) | arctan(x − n)| → , ∀x ∈ R                 (10) nx        →     1/2       x =0
                         2                            e +1
                                                                       1    x ∈ (0, ∞)
                                                                  
       
       0
              x ∈ (−∞, 0]         
                                       0 x ∈ (−∞, 0]
 (11) n        x ∈ (0, 1/n]    →        1
                                       x
                                          x ∈ (0, +∞)
         1/x x ∈ (1/n, +∞)
       
                        2
          1 − n2 x − n2     x ∈ n1 , n3
                                      
 (12)                                     → 0, ∀x ∈ R
                0          altrimenti
        n sin(x) x ∈ [(2n − 1)π, (2n + 1)π]
 (13)      n+1                                    → 0, ∀x ∈ R
       0           altrimenti



                                                                                         18 / 39
Osservazione (convergenza uniforme e unione insiemistica).

Supponiamo che (fn )n converga uniformemente a f negli insiemi X1 , . . . Xk .
Fissato ε > 0, per ogni j ∈ {1, . . . , k} esiste νj ∈ N tale che per ogni n ≥ νj :
                                   |fn (x) − f (x)| < ε ∀x ∈ Xj                             (Dj )
Per ogni n ≥ ν := max {ν1 , . . . , νk }, ciascuna (Dj ) è soddisfatta, quindi:
                                                                k
                                                                [
                            |fn (x) − f (x)| < ε per ogni x ∈         Xj .
                                                                j=1


Ciò dimostra che
Teorema
Se (fn )n converge uniformementeSa f negli insiemi X1 , . . . Xk , allora (fn )n converge
uniformemente a f nell’insieme kj=1 Xj .

Questa proprietà non vale per unioni infinite.
Esempio
                                    h        i
(x n )n≥0 converge uniformemente in 0, 1 − 1j per qualsiasi j ∈ N∗ , ma non converge
                           S h           i
uniformemente in [0, 1) = ∞            1
                            j=1 0, 1 − j .

                                                                                             19 / 39
Teorema
Sia (fn )n converge uniformemente a f e (gn )n converge uniformemente a g in X . λ ∈ R.
Allora
- (fn + gn )n converge uniformemente a f + g in X
- (fn · gn )n converge uniformemente a f · g in X
- (λ · fn )n converge uniformemente a λ · f in X

Dim. [Come nel caso di successioni numeriche]

                      ||fn + gn − f − g ||∞ = sup |fn (x) + gn (x) − f (x) − g (x)|
                                                 x

                                            ≤ sup (|fn (x) − f | + |gn (x) − g (x)|)
                                                 x

            ≤ sup |fn (x) − f | + sup |gn (x) − g (x)| = ||fn − f ||∞ + ||gn − g ||∞
                 x                 X

Le altre per esercizio.




                                                                                       20 / 39
Teorema (convergenza uniforme e limitatezza)
Sia X ̸= ∅. Per ogni n ∈ N, sia fn : X → R una funzione limitata. Se (fn )n converge
uniformemente in X , allora la funzione limite è limitata.

   Dim. Sia f il limite uniforme. Dalla definizione di convergenza uniforme sappiamo che

                 ∀ϵ > 0, ∃ν = ν(ϵ) ∈ N t.c. ∀n ≥ ν : |fn (x) − f (x)| < ϵ, ∀x ∈ X .

   Fissato un ϵ > 0, sia ν = ν(ϵ) il numero previsto nella precendente e fissiamo un
   numero m > ν che consideriamo fissato.
   Sappaimo che la funzione fm é limitata per ipotesi, ossia esiste M > 0 tale che
   ∀x ∈ X : |fm (x)| < M.
   Unendo le informazioni abbiamo che

                     ∀x ∈ X : |f (x)| ≤ |f (x) − fm (x)| + |fm (x)| < ϵ + M.

   Ossia |f | é limitata da M + ϵ.
Il teorema può essere espresso anche come
Sia fn ∈ B(X ) e supponiamo che fn → f nella norma uniforme ∥ · ∥∞ , allora f ∈ B(X ).In
questa formulazione la dimostrazione la si è già vista (In uno spazio metrico una
successione convergente è limitata).
Osservazione 1. Se una successione di funzioni limitate converge puntualmente a una
funzione non limitata si può escludere che la convergenza sia uniforme.
                                                                                       21 / 39
Teorema (convergenza uniforme e continuità)
Sia (X , d) spazio metrico ed x0 ∈ X . Per ogni n ∈ N, sia fn : X → R una funzione
continua in x0 . Se fn → f uniformemente in X , allora la funzione limite f è continua in x0 .
Dim. f è continua in x0 equivale a dire

          ∀ϵ > 0, ∃δ = δ(x0 , ϵ) > 0, t.c. ∀x ∈ X , d(x0 , x) < δ : |f (x) − f (x0 )| < ϵ.

Fissiamo ϵ > 0. In corrispondenza di questo ϵ, usiamo la convergenza uniforme:
sappiamo che esiste ν = ν(ϵ) tale che per ogni n ≥ ν

                                   |fn (x) − f (x)| < ϵ, ∀x ∈ X .                                     (∗)

Fissiamo m ≥ ν. Per fm vale la (*). fm é continua in x0 e quindi che in corrispondenza
dell’ϵ fissato, esiste δ = δ(ϵ, x0 , m) > 0 tale che

                          ∀x ∈ X , d(x0 , x) < δ : |fm (x) − fm (x0 )| < ϵ.

Pertanto ∀x ∈ X , con d(x0 , x) < δ risulta

|f (x) − f (x0 )| ≤ |f (x) − fm (x)| + |fm (x) − fm (x0 )| + |fm (x0 ) − f (x0 )| < ϵ + ϵ + ϵ = 3ϵ.

Osservazione 2. Se ogni fn è continua in tutto X , allora anche f é continua in tutto X .
Osservazione 3. Se una successione di funzioni continue converge puntualmente a una
funzione non continua si può escludere che la convergenza sia uniforme.
                                                                                                      22 / 39
Teorema (Estensione della convergenza uniforme alla chiusura)
Sia E ⊂ R e sia (fn )n una successione di funzioni continue in Ē . Se (fn )n converge
uniformemente su E , allora converge uniformemente anche su Ē .
Dim. Dimostriamo il teorema nel caso E = [a, b[. Sia f = limn fn uniforme. Poiché fn
sono limitate in Ē , sappiamo che f è limitata in E . Sia xp := b − 1/p. Essendo la
successione p 7→ f (xp ) limitata, esiste una estratta f (xpk ) convergente e poniamo
f (b) := limk f (xpk ).
Fissato ϵ > 0, sappiamo che esiste ν tale che per n > ν:
                               |f (x) − fn (x)| < ϵ         ∀x ∈ [a, b[.                          (∗)
Vogliamo far vedere che questa sussiste per ogni x ∈ [a, b], qundi anche per x = b.
          |f (b) − fn (b)| ≤|f (b) − f (xpk )| + |f (xpk ) − fn (xpk )| + |fn (xpk ) − fn (b)|
                           <|f (b) − f (xpk )| +        ϵ       + |fn (xpk ) − fn (b)|
facendo tendere k → ∞, vista la continuità di fn e la definizione di f (b) abbiamo
                                         |f (b) − fn (b)| < ϵ                                    (∗∗)
Unendo le due relazioni (*) e (**), abbiamo la tesi.
Osservazione 4. Se le fn → f in E uniformemente, allora la convergenza uniforme ci sarà
su tutto Ē ad una estensione di f che sarà continua su tutto Ē .
Riesaminare gli esempi ...
                                                                                                  23 / 39
Nelle ipotesi del teoremi precedenti, le tesi si possono enunciare dicendo che posso
invertire i limiti per n → ∞ e x → x0

                              lim lim fn (x) = lim lim fn (x)
                             n→∞ x→x0            x→x0 n→∞

Ossia
                                   lim fn (x0 ) = lim f (x)
                                  n→∞            x→x0


Altrettanto interessante è sapere sotto quali condizioni posso scambiare limite e integrale
                              Z b            Z b
                    ∃ lim         fn (x)dx =     lim fn (x)dx        ?
                      n→+∞    a              a   n→∞



Ed anche, quando posso scambiare limite e derivata
                                                  ′
                       lim fn′ (x)dx = lim fn (x)                 ?
                        n→+∞                n→∞




                                                                                         24 / 39
Convergenza e integrabilità

Abbiamo già osservato che la convergenza puntuale non basta.
Ad esempio per la successione fn (x) := np x(1 − x 2 )n , x ∈ [0, 1] p > 1 non posso
scambiare integrale e limite:
        Z 1
                        np 1                     np                            np
                           Z                                          s=1
            fn (x)dx =        (1 − s)n ds = −            (1 − s)n+1       =
         0               2 0                  2(n + 1)                s=0   2(n + 1)

mentre fn (x) → 0 ∀x ∈ [0, 1]
Richiami
- Una funzione f : [a, b] → R è integrabile secondo Riemann se e solo se è limitata e per
ogni ε > 0 esiste una suddivisione σ dell’intervallo [a, b] tale che S(f , σ) − s(f , σ) < ε
dove S(f , σ) somma di Riemann superiore s(f , σ) somma di Riemann inferiore




                                                                                          25 / 39
Teorema (passaggio al limite sotto il segno di integrale (TPLSSI))
Per ogni n ∈ N, sia fn : [a, b] → R una funzione integrabile secondo Riemann.
Supponiamo che fn → f converga uniformemente in [a, b]. Allora: la funzione limite f è
integrabile secondo Riemann e si ha
                          Z b             Z b                 Z b
                    lim        fn (x)dx =     lim fn (x)dx =      f (x)dx.
                     n→+∞     a                   a    n→+∞                    a

Dim. Supponiamo di aver già dimostrato che f sia integrabile secondo Riemann.
Allora la tesi equivale a dire
                                              Z b            Z b
                 ∀ϵ, ∃ν = ν(ϵ), t.c. ∀n ≥ ν :     fn (x)dx −     f (x)dx < ϵ
                                                           a               a

Fissato ϵ > 0. In corrsipondenza di ϵ/(b − a) sia ν ∈ N (previsto dalla conv. uniforme)
tale che
                 ∀n ≥ ν : sup |fn (x) − f (x)| = ||fn − f ||∞ < ϵ/(b − a).
                              x∈[a,b]
Il numero ν é proprio quello che serve per la convergenza della tesi, infatti per n ≥ ν
                            Z b            Z b            Z b
                                fn (x)dx −     f (x)dx =      (fn (x) − f (x)) dx
                                  a                    a               a
               Z b                           Z b
           ≤         |fn (x) − f (x)| dx ≤            ||fn − f ||∞ dx < (b − a)ϵ/(b − a) = ϵ
                a                             a

                                                                                               26 / 39
(cont. dim.)


Teorema (passaggio al limite sotto il segno di integrale (TPLSSI))
Per ogni n ∈ N, sia fn : [a, b] → R una funzione integrabile secondo Riemann.
Supponiamo che fn → f converga uniformemente in [a, b]. Allora: la funzione limite f è
integrabile secondo Riemann e si ha
                          Z b             Z b                 Z b
                    lim        fn (x)dx =     lim fn (x)dx =      f (x)dx.
                   n→+∞     a              a   n→+∞               a

Rimane da dimostrare che f è Riemann integrabile.
Dimostramolo solo nel caso particolare in cui le fn sono continue.
In tal caso l’integrabilità della f segue dal fatto che f è continua.
   Cenno della dimostrazione nel caso generale. Prima di tutto f è limitata per un
   teorema precedente. Il resto della dimostrazione si basa sulle seguenti osservazioni
   - Sia A un insieme e siano f , g : A → R due funzioni limitate. Allora:

                 sup f − sup g ≤ sup |f − g |,      inf f − inf g ≤ sup |f − g |.
                   A       A         A                A      A            A




                                                                                          27 / 39
Esercizio per casa

Studiare la convergenza della successione
                                     (
                                                  se x ∈ 0, n1 ,
                                                             
                                      1 − nx
                            fn (x) =                    1 
                                      0           se x ∈ n , 1 .

e stabilire se
1) si può applicare il teorema di passaggio al limite sotto il segno di integrale
2) il limite degli integrali delle fn su [0, 1] è uguale all’integrale del limite?




                                                                                      28 / 39
Convergenza e derivabilità

Quando posso scambiare limite e derivata
                                                 ′
                       lim fn′ (x)dx = lim fn (x)                    ?
                         n→+∞                 n→∞



Ricordiamo
r           l’esempio (2):
        1
  x 2 + → |x| uniformemente in R.
        n
Limite uniforme di funzioni C ∞ non è detto che si derivabile.
La convergenza uniforme non basta!

Esempio
Anche se la funzione limite è derivabile non è vero che la successione delle derivate
converge alla derivata della funzione limite:
Sia fn (x) := arctan(nx)
                   n
                         . fn → f ≡ 0 uniformemente. ma fn′ (x) = 1+n12 x 2 ̸→ f ′ (per x = 0,
  ′
fn (0) = 1)

La convergenza uniforme non basta!



                                                                                             29 / 39
Teorema (passaggio al limite sotto il segno di derivata (TPLSSD))
Per ogni n ∈ N, sia fn ∈ C 1 ([a, b]). Supponiamo che
1) Esista x0 ∈ [a, b] tale che fn (x0 ) sia convergente;
2) fn′ → g converga uniformemente in [a, b].
Allora: ∃f ∈ C 1 ([a, b]) tale che f ′ = g e
a) fn → f converge uniformemente in [a, b].
b) fn′ → f ′ converge uniformemente in [a, b].
Dim. Poniamo ℓ = limn fn (x0 ). Poiché fn′ sono continue allora g è continua.
Ricordiamo dal teorema fondamentale del calcolo che per una funzione u ∈ C 1 ([a, b]):
                                                 Z x
                                u(x) = u(x0 ) +      u ′ (t)dt                         (∗)
                                                        x0

Questo ci suggerisce di porre
                                                  Z x
                                   f (x) := ℓ +          g (t)dt
                                                   x0

Abbiamo che f ∈ C 1 ([a, b]) e f ′ = g .
Il punto b) è quindi ovvio. Rimane da dimostrare che fn → f uniformemente. Da (*)
abbiamo che                                         Z x
                                fn (x) = fn (x0 ) +      fn′ (t)dt                 (∗∗)
                                                      x0
                                   Rx ′            Rx
(Oss. Dal TPLSSI abbiamo che x0 fn (t)dt → x0 g (t)dt e quindi fn → f solo
puntualmente.)                                                                      30 / 39
(cont. dim.)

                                                     Z x
                                      f (x) := ℓ +         g (t)dt
                                                      x0
                                                         Z x
                                   fn (x) = fn (x0 ) +           fn′ (t)dt                                       (∗∗)
                                                           x0
Rimane da dimostrare che fn → f anche uniformemente.
Ricordando che ||u||L∞ [a,b] := supx∈[a,b] |u(x)|
Per ogni x ∈ [a, b] abbiamo
                                    Z x                                       Z x
|f (x) − fn (x)| ≤ |ℓ − fn (x0 )| +     (g (t) − fn′ (t)dt ≤ |ℓ − fn (x0 )| +     |g (t) − fn′ (t)|dt
                                     x0                                                    x0
                                                                                      Z b
                                                                 ≤ |ℓ − fn (x0 )| +             ||g − fn′ ||L∞ [a,b] dt
                                                                                       a
                                                                ≤ |ℓ − fn (x0 )| + (b − a)||g − fn′ ||L∞ [a,b]
passando al sup[a,b] risulta

         ||f − fn ||∞ = sup |f (x) − fn (x)| ≤ |ℓ − fn (x0 )| + (b − a)||g − fn′ ||L∞ [a,b]
                         x∈[a,b]

e usando le ipotesi e il teorema di confronto per limiti di successioni numeriche abbiamo
la tesi.
                                                                                                                   31 / 39
TPSSD Estensione ad intervalli qualsiasi (Esercizio)

Corollario
Sia I ⊂ R intervallo (qualsiasi) e sia fn ∈ C 1 (I ).
Supponiamo che:
1) esiste x0 ∈ I tale che (fn (x0 ))n converge;
2) (fn′ )n converge uniformemente in ciascun intervallo compatto contenuto in I .
Allora esiste f ∈ C 1 (I ) tale che
a) (fn )n converge ad f puntualmente in I e uniformemente in ciascun intervallo compatto
contenuto in I ;
b) la funzione limite f è di classe C 1 (I ) e si ha

                              f ′ (x) = lim fn′ (x)   ∀x ∈ I .
                                         n


Esempio
Nota: anche facendo l’ipotesi più forte che (fn′ )n converga uniformemente in tutto
l’intervallo I , questo non garantisce che (fn )n converga uniformemente su tutto I come
dimostra il seguente esempio
                                   
                                    0                  x ∈ [0, n]
                          fn (x) =    1 + cos(πx/n) x ∈ (n, 2n)
                                      2                 x ∈ [2n, ∞)
                                   
                                                                                       32 / 39
Vale il seguente teorema che sarà utile negli esercizi (senza dim.)

Teorema
Sia G : [a, b] → R continua. Per ogni n ∈ N sia fn : X → [a, b] e supponiamo che (fn )n
converge uniformemente a f in X .
Allora la successione delle composte (G (fn ))n converge uniformemente a G (f ) in X .




                                                                                      33 / 39
Svolgere autonomamente i seguenti esercizi. Sugg.: disegnare i grafici delle funzioni coinvolte
Attenzione:
→ Per ogni esercizio, la risposta deve essere completa e comprensibile.
→ La sola convergenza puntuale vale 0/30 , in OGNI caso, perché argomento di Analisi
1, NON di Analisi 2
E1.1 Determinare gli intervalli di R su cui le seguenti successioni di funzioni convergono
puntualmente; determinare quindi gli intervalli di R su cui c’è convergenza uniforme.

                        xn
          a) fn (x) =               b) fn (x) = |x|n          c) fn (x) = x n
                        n!
                            x                             2                ln(n2 x 2 + 1)
          d) fn (x) = n sin         e) fn (x) = x 2 e −nx    g ) fn (x) =
                            n                                                1 + n2 x 2
E1.2 Determinare tutti e soli gli α > 0 tali che la successione di funzioni
                                  x
fn : [0, ∞) → R, fn (x) = α             converge uniformemente su [0, ∞).
                             x + nα
E1.3 Determinare gli intervalli di R su cui le seguenti successioni di funzioni sono ben definite e
convergono puntualmente; determinare quindi gli intervalli di R su cui c’è c.unif.
                          x 2n
     a) fn (x) = n arctan       b) fn (x) = x n (1 − x)      c) fn (x) = n(1 − x)n x
                           n
                    nx                          2x    n
     d) fn (x) = 4              e) fn (x) =
                  n + x4                       1 + x2
E1.4 Studiare il comportamento della successione di funzioni
                         fn (x) = (sin x)2n ,   sull’intervallo   I = [0, π]
                                                                                                  34 / 39
Derivata sotto il segno di integrale

Sia f : [c, d] × [a, b] → R una funzione tale che per ogni x ∈ [c, d], la funzione f (x, ·)
ossia la funzione t 7→ f (x, t) sia integrabile secondo Riemann (ad esempio continua),
allora si può definire la funzione
                                                     Z b
                              x ∈ [c, d] 7→ F (x) :=     f (x, t)dt.                        (∗)
                                                                 a



Teorema
Se f : [c, d] × [a, b] → R è continua nel complesso delle variabili (x, t), allora la funzione
F definita in (*) è continua.
Inoltre se f e ∂x f sono continue nelle due variabili, allora F è derivabile con derivata
continua e                                   Z b
                                  d              ∂
                                     F (x) =        f (x, t)dt
                                  dx          a  ∂x

                               Z b                        Z b
                          d                                          ∂
                                      f (x, t) dt       =               f (x, t) dt.
                          dx     a                           a       ∂x


                                                                                            35 / 39
Esercizio
Le funzioni                                                                       1/2
                              Z b                           Z b
                    ∥f ∥1 =         |f (x)| dx,   ∥f ∥2 =           |f (x)|2 dx
                               a                                a

sono delle norme su C ([a, b]). Calcolare, nel caso di [a, b] = [0, 1] le distanze

                    d∞ (f , g ) := ∥f − g ∥∞       e        d2 (f , g ) := ∥f − g ∥2

nei casi seguenti
  1   f (x) = sin(2πx), g (x) = cos(2πx)
  2   f (x) = x 2 , g (x) = αx + β.
Nel caso 2. determinare poi α e β tali che ∥f − g ∥2 risulti minima




                                                                                         36 / 39
Interpretazione geometrica

Date due funzioni continue f , g : [a, b] → R, si ha dunque
  1   d∞ (f , g ) = sup{|f (x) − g (x)| : x ∈ [a, b]}
                   Rb
  2   d1 (f , g ) = a |f (x) − g (x)| dx
Significato geometrico:
  1   d∞ (f , g ) ≤ ϵ significa che il grafico di g si trova nella striscia di spessore 2ϵ attorno
      al grafico di f
  2   d1 (f , g ) ≤ ϵ significa che l’area della regione compresa tra f e g è ≤ ϵ
Osserviamo che
      il concetto di distanza in spazi di funzioni è importante per precisare in che senso
      una funzione g approssima un’altra funzione f
      le due distanze non danno luogo a convergenze equivalenti.




                                                                                               37 / 39
Approssimazione

Esercizio (per casa)
Dimostrare che in C ([a, b]) si ha
  1 ∥fn − f ∥∞ → 0 =⇒ ∥fn − f ∥1 → 0,

  2   ∥fn − f ∥∞ → 0 =⇒ ∥fn − f ∥2 → 0,
  3 non vale il viceversa nelle implicazione precedenti (ad esempio la successione fn (x) = x n ,
    x ∈ [0, 1] converge a 0 in d1 ma non in d∞ )
Ne consegue che la convergenza uniforme è strettamente più forte della convergenza nella norma
1.


Esercizio (per casa)
Sia F : C ([a, b]) → R definita da
                                                Z b
                                     F (f ) =         f (x)g (x) dx
                                                 a
dove g ∈ C ([a, b]) è fissata. Dimostrare che F è una funzione continua sia rispetto alla norma
∥ · ∥∞ che rispetto alla norma ∥ · ∥1 .




                                                                                                38 / 39
Da Aggiustare

Es.5) (ripresa) Sia S uno insieme non vuoto. Sia X = B(S) := {f : S → R| f limitata}.
Abbiamo visto che (B(S), ∥ · ∥∞ ) è uno spazio normato. Sia (fn )n ⊂ B(S) una
successione, se (fn )n converge a f uniformemente, allora effettivamente f ∈ B(S)
(funzioni limitate che convergono uniformemente lo fanno ad una funzione limitata.)
        (fn )n converge a f uniformemente ⇔ (fn )n converge a f in (B(S), ∥ · ∥∞ )
Se consideriamo Y = C ([a, b]), è un sottospazio di X = B([a, b]) e su C ([a, b]) possiamo
considerare la restrizione della norma ∥ · ∥∞ , ossia (C ([a, b]), ∥ · ∥∞ ) è un sottospazio
normato di (B(S), ∥ · ∥∞ ).
Ricordando che la convergenza uniforme ”conserva” la continuità, abbiamo che data una
successione (fn )n ⊂ C ([a, b]) che converge uniformemente ad f , allora anche
f ∈ C ([a, b]). Questo ci dice che C ([a, b]) è un chiuso di B([a, b]).
Consideriamo Z = C 1 ([a, b]). Z è sottospazio di C e quindi anche di B perciò
(C 1 ([a, b]), ∥ · ∥∞ ) è un sottospazio di C ed anche di B. Ma Z non è chiuso in quanto ci
sono successioni di Z convergenti nella norma (ossia uniformemente), ma la funzione
limite non è in Z :....
Es.5bis) Consideriamo Z = C 1 ([a, b]). Su questo spazio vettoriale consideriamo la
funzione
                                ∥f ∥C 1 := ∥f ∥∞ + ∥f ′ ∥∞
Dimostrate che è una norma.
                                                                                          39 / 39
