---
fonte: "An2_2026_pres17_int_mult.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Integrali multipli

                L.Freddi


              April 27, 2026




L.Freddi                        April 27, 2026   1 / 67
Insiemi normali del piano
Definizione
Un sottoinsieme E di R2 si dice normale rispetto all’asse x se esistono a, b ∈ R e
due funzioni α, β ∈ C([a, b]), tali che

                    E = {(x, y) ∈ R2 : a ≤ x ≤ b, α(x) ≤ y ≤ β(x)}.
                                      y

                                      β(x)


                                  E



                                                            x
                              a                      b
                                      α(x)


         L.Freddi                                               April 27, 2026   2 / 67
Insiemi normali del piano
Osserviamo che
    per definizione gli insiemi normali sono compatti (chiusi e limitati)
    la misura (area) di un insieme normale è definita da
                          Z b
                                           
                m(E) :=         β(x) − α(x) dx
                           a




        L.Freddi                                                April 27, 2026   3 / 67
Insiemi normali del piano
Osserviamo che
    per definizione gli insiemi normali sono compatti (chiusi e limitati)
    la misura (area) di un insieme normale è definita da
                          Z b                      Z b Z β(x)
                                                               
                m(E) :=         β(x) − α(x) dx =              dy dx
                           a                         a    α(x)




        L.Freddi                                                 April 27, 2026   3 / 67
Insiemi normali del piano
Osserviamo che
     per definizione gli insiemi normali sono compatti (chiusi e limitati)
     la misura (area) di un insieme normale è definita da
                           Z b                      Z b Z β(x)
                                                                
                 m(E) :=         β(x) − α(x) dx =              dy dx
                               a                      a    α(x)


Analogamente,
Definizione
Un sottoinsieme E di R2 si dice normale rispetto all’asse y se esistono c, d ∈ R e
due funzioni γ, δ ∈ C([c, d]), tali che

                    E = {(x, y) ∈ R2 : c ≤ y ≤ d, γ(y) ≤ x ≤ δ(y)}.




         L.Freddi                                                 April 27, 2026   3 / 67
Integrale su un insieme normale
Diamo le seguenti definizioni di integrale su un insieme normale.
     Sia E un insieme normale rispetto all’asse x dato da
                    E = {(x, y) ∈ R2 : a ≤ x ≤ b, α(x) ≤ y ≤ β(x)}
     e sia f : E → R una funzione continua. Si definisce
                   Z                   Z b  Z β(x)            
                      f (x, y) dxdy :=              f (x, y) dy dx
                       E                  a     α(x)

     dove gli integrali a secondo membro esistono per la continuità di f .




         L.Freddi                                               April 27, 2026   4 / 67
Integrale su un insieme normale
Diamo le seguenti definizioni di integrale su un insieme normale.
     Sia E un insieme normale rispetto all’asse x dato da
                    E = {(x, y) ∈ R2 : a ≤ x ≤ b, α(x) ≤ y ≤ β(x)}
     e sia f : E → R una funzione continua. Si definisce
                   Z                   Z b  Z β(x)            
                      f (x, y) dxdy :=              f (x, y) dy dx
                       E                  a     α(x)

     dove gli integrali a secondo membro esistono per la continuità di f .
     Se invece F è un insieme normale rispetto all’asse y, cioè
                    F = {(x, y) ∈ R2 : c ≤ y ≤ d, γ(y) ≤ x ≤ δ(y)}
     e f : F → R è continua allora si definisce
                    Z                    Z d  Z δ(y)            
                       f (x, y) dxdy :=               f (x, y) dx dy
                       F                  c     γ(y)



         L.Freddi                                                   April 27, 2026   4 / 67
Integrale su un insieme normale

   Le formule di integrazione precedenti sono dette formule di riduzione perché
   riducono il calcolo di un integrale in due variabili al calcolo di integrali di
   funzioni di una sola variabile




       L.Freddi                                                April 27, 2026   5 / 67
Integrale su un insieme normale

   Le formule di integrazione precedenti sono dette formule di riduzione perché
   riducono il calcolo di un integrale in due variabili al calcolo di integrali di
   funzioni di una sola variabile
   osserviamo che per f ≡ 1 tutti gli integrali forniscono la misura di E




       L.Freddi                                                April 27, 2026   5 / 67
Integrale su un insieme normale

   Le formule di integrazione precedenti sono dette formule di riduzione perché
   riducono il calcolo di un integrale in due variabili al calcolo di integrali di
   funzioni di una sola variabile
   osserviamo che per f ≡ 1 tutti gli integrali forniscono la misura di E
   le variabili di integrazione sono mute; ad esempio, se E ⊆ R2 l’integrale di f
   su E si indica anche con
                           Z                         Z
                              f (x1 , x2 ) dx1 dx2 =   f (x) dx
                          E                       E




       L.Freddi                                                April 27, 2026   5 / 67
Insiemi normali di R3

Definizione
Un sottoinsieme E di R3 si dice normale rispetto al piano (y, z) se esiste un
sottoinsieme normale D di R2 e due funzioni α, β ∈ C(D), tali che

            E = {(x, y, z) ∈ R3 : (y, z) ∈ D, α(y, z) ≤ x ≤ β(y, z)}.

Per un tale insieme si ha
                   Z
                                         
          m(E) =        β(y, z) − α(y, z) dydz
                    D




         L.Freddi                                              April 27, 2026   6 / 67
Insiemi normali di R3

Definizione
Un sottoinsieme E di R3 si dice normale rispetto al piano (y, z) se esiste un
sottoinsieme normale D di R2 e due funzioni α, β ∈ C(D), tali che

            E = {(x, y, z) ∈ R3 : (y, z) ∈ D, α(y, z) ≤ x ≤ β(y, z)}.

Per un tale insieme si ha
                   Z                             Z     Z β(y,z)
                                                                   
          m(E) =        β(y, z) − α(y, z) dydz =                  dx dydz
                    D                              D    α(y,z)




         L.Freddi                                                 April 27, 2026   6 / 67
Insiemi normali di R3

Definizione
Un sottoinsieme E di R3 si dice normale rispetto al piano (y, z) se esiste un
sottoinsieme normale D di R2 e due funzioni α, β ∈ C(D), tali che

            E = {(x, y, z) ∈ R3 : (y, z) ∈ D, α(y, z) ≤ x ≤ β(y, z)}.

Per un tale insieme si ha
                   Z                             Z     Z β(y,z)
                                                                   
          m(E) =        β(y, z) − α(y, z) dydz =                  dx dydz
                    D                              D     α(y,z)

Se f : E → R è continua, si definisce
                Z              Z     Z β(y,z)
                                                            
                   f (x) dx =                 f (x, y, z) dx dydz
                    E            D    α(y,z)




         L.Freddi                                                 April 27, 2026   6 / 67
Insiemi normali di R3

Definizione
Un sottoinsieme E di R3 si dice normale rispetto al piano (y, z) se esiste un
sottoinsieme normale D di R2 e due funzioni α, β ∈ C(D), tali che

            E = {(x, y, z) ∈ R3 : (y, z) ∈ D, α(y, z) ≤ x ≤ β(y, z)}.

Per un tale insieme si ha
                   Z                             Z     Z β(y,z)
                                                                   
          m(E) =        β(y, z) − α(y, z) dydz =                  dx dydz
                    D                              D     α(y,z)

Se f : E → R è continua, si definisce
                Z              Z     Z β(y,z)
                                                            
                   f (x) dx =                 f (x, y, z) dx dydz
                    E            D    α(y,z)


Analogamente si possono definire i sottoinsiemi di R3 (o di Rn ) normali rispetto a
ciascuno degli altri (iper)piani coordinati.

         L.Freddi                                                 April 27, 2026   6 / 67
Esempio

Calcoliamo                  Z
                                 x log(1 + y) dxdy
                             E
con E = {(x, y) ∈ R2 : y ≥ x , y ≤ 1, x ≥ 0}.
                            2




        L.Freddi                                     April 27, 2026   7 / 67
Esempio

Calcoliamo                   Z
                                  x log(1 + y) dxdy
                              E
con E = {(x, y) ∈ R2 : y ≥ x , y ≤ 1, x ≥ 0}. L’insieme E è rappresentato in
                             2

figura.
                                      y




                                         1
                                                y=1
                                         E
                                                       x




        L.Freddi                                            April 27, 2026   7 / 67
Esempio

È evidente che E si può scrivere
     in forma normale rispetto all’asse x nel modo seguente
                      E = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, x2 ≤ y ≤ 1}
     in forma normale rispetto all’asse y come
                                                              √
                     E = {(x, y) ∈ R2 : 0 ≤ y ≤ 1, 0 ≤ x ≤        y}.




         L.Freddi                                             April 27, 2026   8 / 67
Esempio

È evidente che E si può scrivere
     in forma normale rispetto all’asse x nel modo seguente
                      E = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, x2 ≤ y ≤ 1}
     in forma normale rispetto all’asse y come
                                                               √
                     E = {(x, y) ∈ R2 : 0 ≤ y ≤ 1, 0 ≤ x ≤         y}.
     E è compatto e la funzione integranda è continua in E




         L.Freddi                                              April 27, 2026   8 / 67
Esempio

È evidente che E si può scrivere
     in forma normale rispetto all’asse x nel modo seguente
                      E = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, x2 ≤ y ≤ 1}
     in forma normale rispetto all’asse y come
                                                               √
                     E = {(x, y) ∈ R2 : 0 ≤ y ≤ 1, 0 ≤ x ≤         y}.
     E è compatto e la funzione integranda è continua in E
     si possono pertanto applicare le formule di riduzione




         L.Freddi                                              April 27, 2026   8 / 67
Esempio

È evidente che E si può scrivere
     in forma normale rispetto all’asse x nel modo seguente
                        E = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, x2 ≤ y ≤ 1}
     in forma normale rispetto all’asse y come
                                                                   √
                        E = {(x, y) ∈ R2 : 0 ≤ y ≤ 1, 0 ≤ x ≤          y}.
     E è compatto e la funzione integranda è continua in E
     si possono pertanto applicare le formule di riduzione
     la più comoda per i calcoli è quella in cui E si considera normale rispetto
     all’asse y (provare, per esercizio, con l’altra):
               Z                             Z 1 Z √y                   
                   x log(1 + y) dxdy =                   x log(1 + y) dx dy
                    E                        0        0
                                                Z 1
                                            1                             1
                                        =             y log(1 + y) dy =     .
                                            2    0                        8

         L.Freddi                                                   April 27, 2026   8 / 67
Esercizi

Esercizio (per casa)
Calcolare                           Z
                                         x dxdy
                                     A
dove A è il sottoinsieme aperto del piano delimitato dalle rette y = x, y = −x,
         x
y =1+ .
         2




            L.Freddi                                           April 27, 2026      9 / 67
Esercizi

Esercizio (per casa)
Calcolare                           Z
                                         x dxdy
                                     A
dove A è il sottoinsieme aperto del piano delimitato dalle rette y = x, y = −x,
         x
y =1+ .
         2
Risulta: 16/27




            L.Freddi                                           April 27, 2026      9 / 67
Esercizi

Esercizio (per casa)
Calcolare                              Z
                                            x dxdy
                                        A
dove A è il sottoinsieme aperto del piano delimitato dalle rette y = x, y = −x,
         x
y =1+ .
         2
Risulta: 16/27
Esercizio (per casa)
Calcolare l’area dell’ellisse
                                            x2  y2
                       E = {(x, y) ∈ R2 :    2
                                               + 2 ≤ 1} a, b > 0.
                                            a   b




            L.Freddi                                            April 27, 2026     9 / 67
Esercizi

Esercizio (per casa)
Calcolare                              Z
                                            x dxdy
                                        A
dove A è il sottoinsieme aperto del piano delimitato dalle rette y = x, y = −x,
         x
y =1+ .
         2
Risulta: 16/27
Esercizio (per casa)
Calcolare l’area dell’ellisse
                                            x2  y2
                       E = {(x, y) ∈ R2 :    2
                                               + 2 ≤ 1} a, b > 0.
                                            a   b
Risulta: m(E) = abπ


            L.Freddi                                            April 27, 2026     9 / 67
Esempio

Calcoliamo il volume del sottoinsieme E di R3 contenuto nel primo ottante e
delimitato
     dal paraboloide di equazione z = x2 + y 2 ,
     dal cilindro di equazione x2 + y 2 = 9.

                                      z




                                               E

                                                    y
                                       D

                              x
         L.Freddi                                            April 27, 2026   10 / 67
Esempio

   E si può scrivere come insieme normale rispetto al piano (x, y)
                  E = {(x, y, z) ∈ R3 : (x, y) ∈ D, 0 ≤ z ≤ x2 + y 2 }.




       L.Freddi                                                April 27, 2026   11 / 67
Esempio

   E si può scrivere come insieme normale rispetto al piano (x, y)
                  E = {(x, y, z) ∈ R3 : (x, y) ∈ D, 0 ≤ z ≤ x2 + y 2 }.
   per le formule di riduzione si ha
                                        Z
                               m(E) =        (x2 + y 2 ) dxdy
                                         D




       L.Freddi                                                 April 27, 2026   11 / 67
Esempio

   E si può scrivere come insieme normale rispetto al piano (x, y)
                  E = {(x, y, z) ∈ R3 : (x, y) ∈ D, 0 ≤ z ≤ x2 + y 2 }.
   per le formule di riduzione si ha
                                        Z
                               m(E) =        (x2 + y 2 ) dxdy
                                         D

   anche il settore circolare D si può scrivere in forma normale rispetto, per
   esempio all’asse x:
                                                            p
                D = {(x, y) ∈ R2 : 0 ≤ x ≤ 3, 0 ≤ y ≤ 9 − x2 }




       L.Freddi                                                 April 27, 2026    11 / 67
Esempio

   E si può scrivere come insieme normale rispetto al piano (x, y)
                  E = {(x, y, z) ∈ R3 : (x, y) ∈ D, 0 ≤ z ≤ x2 + y 2 }.
   per le formule di riduzione si ha
                                        Z
                               m(E) =        (x2 + y 2 ) dxdy
                                         D

   anche il settore circolare D si può scrivere in forma normale rispetto, per
   esempio all’asse x:
                                                            p
                D = {(x, y) ∈ R2 : 0 ≤ x ≤ 3, 0 ≤ y ≤ 9 − x2 }
   applicando di nuovo le formule di riduzione, si ha dunque
                          Z 3  Z √9−x2                     81
                 m(E) =                  (x2 + y 2 ) dy dx =    π.
                           0     0                           8



       L.Freddi                                                 April 27, 2026    11 / 67
Integrale su insiemi misurabili limitati
Definizione
Un sottoinsieme E (limitato) di Rn è detto misurabile se è unione finita di domini
normali, anche rispetto ad iperpiani differenti, senza parti interne comuni.




         L.Freddi                                               April 27, 2026   12 / 67
Integrale su insiemi misurabili limitati
Definizione
Un sottoinsieme E (limitato) di Rn è detto misurabile se è unione finita di domini
normali, anche rispetto ad iperpiani differenti, senza parti interne comuni.

Dato un insieme misurabile
                                  k
                                  [
                             E=         Ei ,       k ∈ N \ {0},
                                  i=1
                                   ◦           ◦
con Ei normale per i = 1, ..., k e E i ∩ E j = ∅ per ogni i ̸= j,




         L.Freddi                                                   April 27, 2026   12 / 67
Integrale su insiemi misurabili limitati
Definizione
Un sottoinsieme E (limitato) di Rn è detto misurabile se è unione finita di domini
normali, anche rispetto ad iperpiani differenti, senza parti interne comuni.

Dato un insieme misurabile
                                  k
                                  [
                             E=         Ei ,       k ∈ N \ {0},
                                  i=1
                                   ◦           ◦
con Ei normale per i = 1, ..., k e E i ∩ E j = ∅ per ogni i ̸= j, la sua misura è
definita da
                                          Xk
                                m(E) :=       m(Ei ).
                                               i=1




         L.Freddi                                                 April 27, 2026     12 / 67
Integrale su insiemi misurabili limitati
Definizione
Un sottoinsieme E (limitato) di Rn è detto misurabile se è unione finita di domini
normali, anche rispetto ad iperpiani differenti, senza parti interne comuni.

Dato un insieme misurabile
                                   k
                                   [
                             E=          Ei ,        k ∈ N \ {0},
                                   i=1
                                    ◦           ◦
con Ei normale per i = 1, ..., k e E i ∩ E j = ∅ per ogni i ̸= j, la sua misura è
definita da
                                          Xk
                                m(E) :=       m(Ei ).
                                                i=1

Data una funzione f : E → R tale che f|Ei è continua per i = 1, ...k, si definisce
                          Z           Xk Z
                              f dx :=          f dx
                               E                    i=1   Ei

e diremo che f è integrabile su E.
         L.Freddi                                                   April 27, 2026   12 / 67
Estensione della definizione di integrale
Osserviamo che
    la definizione di integrale multiplo su un insieme normale e le sue estensioni
    si applicano a funzioni limitate su domini chiusi e limitati
    nel caso n = 1, queste definizioni si riducono a quelle date per l’integrale di
    Riemann in Analisi 1




        L.Freddi                                                April 27, 2026   13 / 67
Estensione della definizione di integrale
Osserviamo che
    la definizione di integrale multiplo su un insieme normale e le sue estensioni
    si applicano a funzioni limitate su domini chiusi e limitati
    nel caso n = 1, queste definizioni si riducono a quelle date per l’integrale di
    Riemann in Analisi 1
    anche nel caso degli integrali multipli, la definizione di integrale si può
    estendere al caso di funzioni non limitate su domini non limitati




        L.Freddi                                                  April 27, 2026   13 / 67
Estensione della definizione di integrale
Osserviamo che
    la definizione di integrale multiplo su un insieme normale e le sue estensioni
    si applicano a funzioni limitate su domini chiusi e limitati
    nel caso n = 1, queste definizioni si riducono a quelle date per l’integrale di
    Riemann in Analisi 1
    anche nel caso degli integrali multipli, la definizione di integrale si può
    estendere al caso di funzioni non limitate su domini non limitati
       ▶ nel caso n = 1 l’estensione era stata fatta introducendo la nozione di

         integrale improprio o generalizzato




        L.Freddi                                                April 27, 2026   13 / 67
Estensione della definizione di integrale
Osserviamo che
    la definizione di integrale multiplo su un insieme normale e le sue estensioni
    si applicano a funzioni limitate su domini chiusi e limitati
    nel caso n = 1, queste definizioni si riducono a quelle date per l’integrale di
    Riemann in Analisi 1
    anche nel caso degli integrali multipli, la definizione di integrale si può
    estendere al caso di funzioni non limitate su domini non limitati
       ▶ nel caso n = 1 l’estensione era stata fatta introducendo la nozione di

         integrale improprio o generalizzato
       ▶ nel caso degli integrali multipli conviene procedere in modo diverso




        L.Freddi                                                April 27, 2026   13 / 67
Estensione della definizione di integrale
Osserviamo che
     la definizione di integrale multiplo su un insieme normale e le sue estensioni
     si applicano a funzioni limitate su domini chiusi e limitati
     nel caso n = 1, queste definizioni si riducono a quelle date per l’integrale di
     Riemann in Analisi 1
     anche nel caso degli integrali multipli, la definizione di integrale si può
     estendere al caso di funzioni non limitate su domini non limitati
        ▶ nel caso n = 1 l’estensione era stata fatta introducendo la nozione di

          integrale improprio o generalizzato
        ▶ nel caso degli integrali multipli conviene procedere in modo diverso

Estendiamo anzitutto la definizione di insieme misurabile
Definizione
Un sottoinsieme E (anche non limitato) di Rn si dice misurabile se l’insieme
E ∩ Br (0) è misurabile per ogni r > 0. Si definisce la misura di E

                          m(E) := lim m(E ∩ Br (0)).
                                    r→∞

         L.Freddi                                                April 27, 2026   13 / 67
Funzioni non limitate su misurabili non limitati
Definizione
Sia E un sottoinsieme misurabile di Rn e f : E → R.
    Se f ≥ 0, f si dice integrabile in E se
       ▶  la funzione fr (x) = min{f (x), r} è integrabile su E ∩ Br (0) ∀ r > 0;
                                 Z                    Z
    e, in tal caso, si definisce   f (x) dx := lim              fr (x) dx
                                E             r→+∞    E∩Br (0)




           L.Freddi                                              April 27, 2026   14 / 67
Funzioni non limitate su misurabili non limitati
Definizione
Sia E un sottoinsieme misurabile di Rn e f : E → R.
    Se f ≥ 0, f si dice integrabile in E se
       ▶  la funzione fr (x) = min{f (x), r} è integrabile su E ∩ Br (0) ∀ r > 0;
                                 Z                    Z
    e, in tal caso, si definisce   f (x) dx := lim              fr (x) dx
                                   E             r→+∞    E∩Br (0)
    se f non è sempre positiva, la si scompone nella somma
                      f (x) = f + (x) − f − (x) dove
                      f + (x) := max{f (x), 0} (parte positiva di f )
                      f − (x) := − min{f (x), 0} (parte negativa di f )




           L.Freddi                                                 April 27, 2026   14 / 67
Funzioni non limitate su misurabili non limitati
Definizione
Sia E un sottoinsieme misurabile di Rn e f : E → R.
    Se f ≥ 0, f si dice integrabile in E se
       ▶  la funzione fr (x) = min{f (x), r} è integrabile su E ∩ Br (0) ∀ r > 0;
                                 Z                    Z
    e, in tal caso, si definisce   f (x) dx := lim              fr (x) dx
                                   E             r→+∞    E∩Br (0)
    se f non è sempre positiva, la si scompone nella somma
                      f (x) = f + (x) − f − (x) dove
                      f + (x) := max{f (x), 0} (parte positiva di f )
                      f − (x) := − min{f (x), 0} (parte negativa di f )
     e si dice che f è integrabile se lo sono le funzioni (positive) f + e f − e se i
    loro integrali non sono entrambi uguali a +∞. In tal caso, si pone
                      Z                Z                Z
                          f (x) dx : =     f + (x) dx −    f − (x) dx
                         E               E               E
           L.Freddi                                                 April 27, 2026   14 / 67
Funzioni non limitate su misurabili non limitati
Osservazione
Osserviamo che se si assume che f ≥ 0 allora

                               r < s =⇒ fr ≤ fs .                                   (1)

Ne consegue che il limite
                                     Z
                               lim               fr (x) dx
                              r→+∞    E∩Br (0)

che compare nella definizione esiste sempre perché, per la positività di f e la
monotonia dell’integrale, si tratta del limite per r → +∞ di una funzione
crescente di r.




         L.Freddi                                                 April 27, 2026    15 / 67
Sommabilità e valore assoluto
Definizione
f si dice sommabile se è integrabile con integrale finito




         L.Freddi                                            April 27, 2026   16 / 67
Sommabilità e valore assoluto
Definizione
f si dice sommabile se è integrabile con integrale finito

Proposizione

Le seguenti proposizioni sono equivalenti
  1   f è sommabile
  2   f + e f − sono sommabili
  3   |f | è sommabile




          L.Freddi                                           April 27, 2026   16 / 67
Sommabilità e valore assoluto
Definizione
f si dice sommabile se è integrabile con integrale finito

Proposizione

Le seguenti proposizioni sono equivalenti
  1   f è sommabile
  2   f + e f − sono sommabili
  3   |f | è sommabile

Dimostrazione Segue dalle definizioni e dal fatto che |f | = f + + f − .




          L.Freddi                                            April 27, 2026   16 / 67
Sommabilità e valore assoluto
Definizione
f si dice sommabile se è integrabile con integrale finito

Proposizione

Le seguenti proposizioni sono equivalenti
  1   f è sommabile
  2   f + e f − sono sommabili
  3   |f | è sommabile

Dimostrazione Segue dalle definizioni e dal fatto che |f | = f + + f − .
Osservazione
Nel caso degli integrali impropri, gli integrali finiti sono detti convergenti e si ha
  1   |f | convergente =⇒ f convergente (criterio del confronto)
  2                  ̸
      f convergente =⇒ |f | convergente (prossimo esempio)

          L.Freddi                                                 April 27, 2026   16 / 67
Confronto con l’integrale improprio
Esempio
                                               sen x
L’integrale improprio della funzione f (x) =         in [1, +∞) è convergente, ma
                                                 x
quello di |f | non lo è




          L.Freddi                                               April 27, 2026   17 / 67
Confronto con l’integrale improprio
Esempio
                                            sen x
L’integrale improprio della funzione f (x) =       in [1, +∞) è convergente, ma
                                              x
quello di |f | non lo è ( =⇒ f non è sommabile in [1, +∞))




          L.Freddi                                             April 27, 2026   17 / 67
Confronto con l’integrale improprio
Esempio
                                            sen x
L’integrale improprio della funzione f (x) =       in [1, +∞) è convergente, ma
                                              x
quello di |f | non lo è ( =⇒ f non è sommabile in [1, +∞))

Infatti, integrando per parti, si ha
             Z +∞                      Z c
                   sen x                   sen x
                         dx = lim                dx
              1      x            c→+∞ 1     x
                                                           Z c
                                        cos c                 cos x 
                              = lim −            + cos 1 −          dx
                                  c→+∞       c              1   x2
                                        Z +∞
                                               cos x
                              = cos 1 −              dx
                                         1      x2




          L.Freddi                                             April 27, 2026   17 / 67
Confronto con l’integrale improprio
Esempio
                                            sen x
L’integrale improprio della funzione f (x) =       in [1, +∞) è convergente, ma
                                              x
quello di |f | non lo è ( =⇒ f non è sommabile in [1, +∞))

Infatti, integrando per parti, si ha
             Z +∞                      Z c
                   sen x                   sen x
                         dx = lim                dx
              1      x            c→+∞ 1     x
                                                           Z c
                                        cos c                 cos x 
                              = lim −            + cos 1 −          dx
                                  c→+∞       c              1   x2
                                        Z +∞
                                               cos x
                              = cos 1 −              dx
                                         1      x2
Poiché
                                     | cos x|      1
                                          2
                                               ≤ 2
                                        x         x
                                   Z +∞
                                            cos x
allora, per confronto, l’integrale                dx è convergente
                                    1        x2
          L.Freddi                                                    April 27, 2026   17 / 67
Confronto con l’integrale improprio
Quindi anche       Z +∞
                          sen x
                                dx è convergente.
                   1        x




        L.Freddi                                     April 27, 2026   18 / 67
Confronto con l’integrale improprio
Quindi anche               Z +∞
                                       sen x
                                             dx è convergente.
                            1            x
D’altra parte,
           Z +∞                   Z π                 ∞     Z (k+1)π
                                        | sen x|      X                | sen x|
                   |f (x)| dx =                  dx +                           dx
             1                     1        x                kπ            x
                                                      k=1




        L.Freddi                                                         April 27, 2026   18 / 67
Confronto con l’integrale improprio
Quindi anche               Z +∞
                                       sen x
                                             dx è convergente.
                            1            x
D’altra parte,
           Z +∞                   Z π                 ∞     Z (k+1)π
                                        | sen x|      X                | sen x|
                   |f (x)| dx =                  dx +                           dx
              1                    1        x                kπ            x
                                                      k=1
Visto che
        Z (k+1)π                                Z (k+1)π
                   | sen x|          1                                         2
                            dx ≥                           | sen x| dx =
         kπ            x         (k + 1)π        kπ                        (k + 1)π




        L.Freddi                                                           April 27, 2026   18 / 67
Confronto con l’integrale improprio
Quindi anche                    Z +∞
                                            sen x
                                                  dx è convergente.
                                 1            x
D’altra parte,
           Z +∞                        Z π                  ∞     Z (k+1)π
                                                | sen x|      X              | sen x|
                        |f (x)| dx =                     dx +                         dx
               1                        1           x              kπ            x
                                                            k=1
Visto che
        Z (k+1)π                                      Z (k+1)π
                        | sen x|          1                                          2
                                 dx ≥                            | sen x| dx =
          kπ                x         (k + 1)π         kπ                        (k + 1)π
allora             Z +∞                 Z π                       ∞
                                                | sen x|      2X 1
                          |f (x)| d ≥                    dx +       = +∞
                    1                       1       x         π k+1
                                                                  k=1




         L.Freddi                                                                April 27, 2026   18 / 67
Confronto con l’integrale improprio
Quindi anche                    Z +∞
                                            sen x
                                                  dx è convergente.
                                 1            x
D’altra parte,
           Z +∞                        Z π                  ∞     Z (k+1)π
                                                | sen x|      X              | sen x|
                        |f (x)| dx =                     dx +                         dx
               1                        1           x              kπ            x
                                                            k=1
Visto che
        Z (k+1)π                                      Z (k+1)π
                        | sen x|          1                                          2
                                 dx ≥                            | sen x| dx =
          kπ                x         (k + 1)π         kπ                        (k + 1)π
allora             Z +∞                 Z π                       ∞
                                                | sen x|      2X 1
                          |f (x)| d ≥                    dx +       = +∞
                    1                       1       x         π k+1
                                                                  k=1
e pertanto f non è sommabile.




         L.Freddi                                                                April 27, 2026   18 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1




         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).




         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).

Proposizione

           g : A → B diffeomorfismo      =⇒      det(∇g(x)) ̸= 0 ∀ x ∈ A

Dimostrazione Infatti
                                    id = g −1 ◦ g
e, derivando,
                         ∇id = ∇(g −1 ◦ g)




         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).

Proposizione

           g : A → B diffeomorfismo      =⇒      det(∇g(x)) ̸= 0 ∀ x ∈ A

Dimostrazione Infatti
                                    id = g −1 ◦ g
e, derivando,
                    I = ∇id = ∇(g −1 ◦ g)




         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).

Proposizione

           g : A → B diffeomorfismo      =⇒      det(∇g(x)) ̸= 0 ∀ x ∈ A

Dimostrazione Infatti
                                    id = g −1 ◦ g
e, derivando,
                    I = ∇id = ∇(g −1 ◦ g) = [(∇g −1 ) ◦ g][∇g]




         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).

Proposizione

           g : A → B diffeomorfismo      =⇒      det(∇g(x)) ̸= 0 ∀ x ∈ A

Dimostrazione Infatti
                                    id = g −1 ◦ g
e, derivando,
                    I = ∇id = ∇(g −1 ◦ g) = [(∇g −1 ) ◦ g][∇g]
Passando ai determinanti si ha




         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).

Proposizione

           g : A → B diffeomorfismo      =⇒        det(∇g(x)) ̸= 0 ∀ x ∈ A

Dimostrazione Infatti
                                    id = g −1 ◦ g
e, derivando,
                    I = ∇id = ∇(g −1 ◦ g) = [(∇g −1 ) ◦ g][∇g]
Passando ai determinanti si ha
             det(I) = det [(∇g −1 ) ◦ g][∇g]
                                               



         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).

Proposizione

           g : A → B diffeomorfismo      =⇒       det(∇g(x)) ̸= 0 ∀ x ∈ A

Dimostrazione Infatti
                                    id = g −1 ◦ g
e, derivando,
                    I = ∇id = ∇(g −1 ◦ g) = [(∇g −1 ) ◦ g][∇g]
Passando ai determinanti si ha
        1 = det(I) = det [(∇g −1 ) ◦ g][∇g]
                                              



         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).

Proposizione

           g : A → B diffeomorfismo      =⇒      det(∇g(x)) ̸= 0 ∀ x ∈ A

Dimostrazione Infatti
                                    id = g −1 ◦ g
e, derivando,
                    I = ∇id = ∇(g −1 ◦ g) = [(∇g −1 ) ◦ g][∇g]
Passando ai determinanti si ha
        1 = det(I) = det [(∇g −1 ) ◦ g][∇g] = det[(∇g −1 ) ◦ g] · det[∇g].
                                           



         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Per fare i cambiamenti di variabile negli integrali useremo funzioni invertibili di
classe C 1 dette diffeomorfismi
Definizione
Siano A e B sottoinsiemi aperti di Rn . Una funzione g : A → B si dice un
diffeomorfismo (di classe C 1 ) se è biiettiva, g ∈ C 1 (A) e g −1 ∈ C 1 (B).

Proposizione

           g : A → B diffeomorfismo      =⇒      det(∇g(x)) ̸= 0 ∀ x ∈ A

Dimostrazione Infatti
                                    id = g −1 ◦ g
e, derivando,
                    I = ∇id = ∇(g −1 ◦ g) = [(∇g −1 ) ◦ g][∇g]
Passando ai determinanti si ha
        1 = det(I) = det [(∇g −1 ) ◦ g][∇g] = det[(∇g −1 ) ◦ g] · det[∇g].
                                           



         L.Freddi                                                 April 27, 2026   19 / 67
Cambiamento di variabile negli integrali
Teorema (di cambiamento di variabile per gli integrali)
Siano A e B aperti di Rn e g : A → B un diffeomorfismo. Sia E ⊆ B misurabile
e f : E → R integrabile in E. La funzione composta f ◦ g : g −1 (E) → R è
integrabile in g −1 (E) e vale la formula
                   Z              Z
                      f (y) dy =          (f ◦ g)(x) | det ∇g(x)| dx.
                        E     g −1 (E)


                                         f ◦g
                                                                            R
                                g
                                                             f
                   −1
        A      g        (E)                     E   B




        L.Freddi                                           April 27, 2026       20 / 67
Cambiamento di variabile negli integrali
Esercizio (per casa)
Riconoscere che nel caso n = 1 la formula del cambiamento di variabile per gli
integrali si riduce a quella nota per l’integrale di Riemann di funzioni di una sola
variabile.




         L.Freddi                                                April 27, 2026   21 / 67
Cambiamento di variabile negli integrali
Esercizio (per casa)
Riconoscere che nel caso n = 1 la formula del cambiamento di variabile per gli
integrali si riduce a quella nota per l’integrale di Riemann di funzioni di una sola
variabile.
Come regola mnemonica per eseguire il cambiamento di variabile y = g(x) si può
tenere a mente lo schema seguente
     y si sostituisce con g(x)
     dy si sosituisce con | det(∇g(x))|dx
     E si sostituisce con g −1 (E)




         L.Freddi                                                April 27, 2026   21 / 67
Cambiamento di variabile negli integrali




      L.Freddi                             April 27, 2026   22 / 67
Cambiamento di variabile negli integrali
Esempio
Calcoliamo l’area dell’insieme E = {(x, y) ∈ R2 : 0 < x ≤ y ≤ 2x, 1 ≤ xy ≤ 2}.
              y




                     E



                           x




          L.Freddi                                          April 27, 2026   22 / 67
Cambiamento di variabile negli integrali
Esempio
Calcoliamo l’area dell’insieme E = {(x, y) ∈ R2 : 0 < x ≤ y ≤ 2x, 1 ≤ xy ≤ 2}.
              y




                     E



                           x




          L.Freddi                                          April 27, 2026   22 / 67
Cambiamento di variabile negli integrali
Esempio
Calcoliamo l’area dell’insieme E = {(x, y) ∈ R2 : 0 < x ≤ y ≤ 2x, 1 ≤ xy ≤ 2}.
              y




                     E



                            x




Osserviamo che
    E si può scrivere E come unione di insiemi normali e calcolare l’integrale su
    ciascuno di essi (provare per esercizio)




          L.Freddi                                             April 27, 2026   22 / 67
Cambiamento di variabile negli integrali




      L.Freddi                             April 27, 2026   23 / 67
Cambiamento di variabile negli integrali
   invece, il cambiamento di variabili
                                   (
                                      u = xy
                                      v = y/x
   lo trasforma nel quadrato
                   Q = {(u, v) ∈ R2 : 1 ≤ u ≤ 2, 1 ≤ v ≤ 2}




      L.Freddi                                          April 27, 2026   23 / 67
Cambiamento di variabile negli integrali
   invece, il cambiamento di variabili
                                   (
                                      u = xy
                                      v = y/x
   lo trasforma nel quadrato
                     Q = {(u, v) ∈ R2 : 1 ≤ u ≤ 2, 1 ≤ v ≤ 2}
   osserviamo che la funzione che esegue il cambiamento di variabili
                                    φ(x, y) = (xy, y/x)
                                1
   è biiettiva e di classe C




       L.Freddi                                             April 27, 2026   23 / 67
Cambiamento di variabile negli integrali
   invece, il cambiamento di variabili
                                   (
                                      u = xy
                                      v = y/x
   lo trasforma nel quadrato
                     Q = {(u, v) ∈ R2 : 1 ≤ u ≤ 2, 1 ≤ v ≤ 2}
   osserviamo che la funzione che esegue il cambiamento di variabili
                                    φ(x, y) = (xy, y/x)
                                1
   è biiettiva e di classe C
   inoltre φ(E) = Q
                                          f ◦g
                                    g = φ−1                 R
                                                     f
                       Q = g −1 (E)              E

       L.Freddi                                             April 27, 2026   23 / 67
Cambiamento di variabile negli integrali
                 p               √
   si ha x =         u/v e y =       uv, cioè
                                                p    √
                                     g(u, v) = ( u/v, uv).




      L.Freddi                                               April 27, 2026   24 / 67
Cambiamento di variabile negli integrali
                 p               √
   si ha x =         u/v e y =       uv, cioè
                                                p    √
                                     g(u, v) = ( u/v, uv).
   quindi                                                     √       !
                                                   √1
                                                 2 uv
                                                          − v√uv
                             ∇g(u, v) =                                   .
                                                 1
                                                   pv     1
                                                            pu
                                                 2    u   2       v




      L.Freddi                                                                April 27, 2026   24 / 67
Cambiamento di variabile negli integrali
                 p               √
   si ha x =         u/v e y =       uv, cioè
                                                p    √
                                     g(u, v) = ( u/v, uv).
   quindi                                                        √       !
                                                   √1
                                                 2 uv
                                                            − v√uv
                             ∇g(u, v) =                                      .
                                                 1
                                                   pv       1
                                                              pu
                                                 2    u      2       v
   quindi
                                                           1
                                           det(∇g) =         .
                                                          2v




      L.Freddi                                                                   April 27, 2026   24 / 67
Cambiamento di variabile negli integrali
                 p               √
   si ha x =         u/v e y =       uv, cioè
                                                p    √
                                     g(u, v) = ( u/v, uv).
   quindi                                                     √       !
                                                   √1
                                                 2 uv
                                                          − v√uv
                             ∇g(u, v) =                                   .
                                                 1
                                                   pv     1
                                                            pu
                                                 2    u   2       v
   quindi
                                              1
                                           det(∇g) =
                                                 .
                                             2v
   per la formula del cambiamento di variabile si ha quindi
                         Z            Z
                                           1
              m(E) =         1 dxdy =           dudv
                           E           Q 2v
                         Z              Z 2Z 2
                              1                     1        log 2
                      =         dudv =                du dv =
                           Q 2v          1      1  2v           2



      L.Freddi                                                                April 27, 2026   24 / 67
Cambiamento di variabile negli integrali

Esercizio (per casa)
          Z
Calcolare   (x + y) dxdy con
          E

                   E = {(x, y) ∈ R2 : 0 < x < y < 2x, 1 < xy < 2}




        L.Freddi                                             April 27, 2026   25 / 67
Cambiamento di variabile negli integrali

Esercizio (per casa)
          Z
Calcolare   (x + y) dxdy con
           E

                    E = {(x, y) ∈ R2 : 0 < x < y < 2x, 1 < xy < 2}
          √
Risulta 4−3 2




         L.Freddi                                             April 27, 2026   25 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:   [0, +∞) × [0, 2π) → R2
                          (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)




         L.Freddi                                               April 27, 2026   26 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:    [0, +∞) × [0, 2π) → R2
                           (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)
     è suriettiva




         L.Freddi                                                April 27, 2026   26 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:    [0, +∞) × [0, 2π) → R2
                           (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)
     è suriettiva
     non è iniettiva, infatti g(0, θ) = (0, 0) per ogni θ ∈ [0, 2π).




         L.Freddi                                                   April 27, 2026   26 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:    [0, +∞) × [0, 2π) → R2
                           (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)
     è suriettiva
     non è iniettiva, infatti g(0, θ) = (0, 0) per ogni θ ∈ [0, 2π).
Tolti dal dominio i punti cattivi (del tipo ρ = 0) la restrizione
                        g : (0, +∞) × [0, 2π) → R2 \ {(0, 0)}
è iniettiva e suriettiva (notare che dominio e codominio sono cambiati).




         L.Freddi                                                   April 27, 2026   26 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:    [0, +∞) × [0, 2π) → R2
                           (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)
     è suriettiva
     non è iniettiva, infatti g(0, θ) = (0, 0) per ogni θ ∈ [0, 2π).
Tolti dal dominio i punti cattivi (del tipo ρ = 0) la restrizione
                        g : (0, +∞) × [0, 2π) → R2 \ {(0, 0)}
è iniettiva e suriettiva (notare che dominio e codominio sono cambiati).
Ma ha ancora un difetto:




         L.Freddi                                                   April 27, 2026   26 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:    [0, +∞) × [0, 2π) → R2
                           (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)
     è suriettiva
     non è iniettiva, infatti g(0, θ) = (0, 0) per ogni θ ∈ [0, 2π).
Tolti dal dominio i punti cattivi (del tipo ρ = 0) la restrizione
                        g : (0, +∞) × [0, 2π) → R2 \ {(0, 0)}
è iniettiva e suriettiva (notare che dominio e codominio sono cambiati).
Ma ha ancora un difetto:
     g −1 non è continua, perché è discontinua in tutti i punti del tipo (ρ, 0).
     Infatti, attraversando l’asse x, l’angolo θ salta da 2π a 0, o viceversa




         L.Freddi                                                   April 27, 2026    26 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:    [0, +∞) × [0, 2π) → R2
                           (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)
     è suriettiva
     non è iniettiva, infatti g(0, θ) = (0, 0) per ogni θ ∈ [0, 2π).
Tolti dal dominio i punti cattivi (del tipo ρ = 0) la restrizione
                        g : (0, +∞) × [0, 2π) → R2 \ {(0, 0)}
è iniettiva e suriettiva (notare che dominio e codominio sono cambiati).
Ma ha ancora un difetto:
     g −1 non è continua, perché è discontinua in tutti i punti del tipo (ρ, 0).
     Infatti, attraversando l’asse x, l’angolo θ salta da 2π a 0, o viceversa
     per ottenere un diffeomorfismo occorre considerare opportune restrizioni,




         L.Freddi                                                   April 27, 2026    26 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:    [0, +∞) × [0, 2π) → R2
                           (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)
     è suriettiva
     non è iniettiva, infatti g(0, θ) = (0, 0) per ogni θ ∈ [0, 2π).
Tolti dal dominio i punti cattivi (del tipo ρ = 0) la restrizione
                        g : (0, +∞) × [0, 2π) → R2 \ {(0, 0)}
è iniettiva e suriettiva (notare che dominio e codominio sono cambiati).
Ma ha ancora un difetto:
     g −1 non è continua, perché è discontinua in tutti i punti del tipo (ρ, 0).
     Infatti, attraversando l’asse x, l’angolo θ salta da 2π a 0, o viceversa
     per ottenere un diffeomorfismo occorre considerare opportune restrizioni,
Ad esempio, la restrizione
                g : (0, +∞) × (0, 2π) → R2 \ {(x, 0) ∈ R2 : x ≥ 0}
è un diffeomorfismo.
         L.Freddi                                                   April 27, 2026    26 / 67
Coordinate polari
La funzione che fa passare dalle coordinate polari alle coordinate cartesiane
               g:    [0, +∞) × [0, 2π) → R2
                           (ρ, θ)      7 → g(ρ, θ) = (ρ cos θ, ρ sen θ)
     è suriettiva
     non è iniettiva, infatti g(0, θ) = (0, 0) per ogni θ ∈ [0, 2π).
Tolti dal dominio i punti cattivi (del tipo ρ = 0) la restrizione
                        g : (0, +∞) × [0, 2π) → R2 \ {(0, 0)}
è iniettiva e suriettiva (notare che dominio e codominio sono cambiati).
Ma ha ancora un difetto:
     g −1 non è continua, perché è discontinua in tutti i punti del tipo (ρ, 0).
     Infatti, attraversando l’asse x, l’angolo θ salta da 2π a 0, o viceversa
     per ottenere un diffeomorfismo occorre considerare opportune restrizioni,
Ad esempio, la restrizione
                g : (0, +∞) × (0, 2π) → R2 \ {(x, 0) ∈ R2 : x ≥ 0}
è un diffeomorfismo. Esercizio: verificare che si ha | det ∇g(ρ, θ)| = ρ.
         L.Freddi                                                   April 27, 2026    26 / 67
Coordinate polari
Esempio
Calcoliamo l’integrale della funzione f (x, y) = x + y 2 sul settore di corona
circolare di raggi 1 e 2 contenuto nel primo quadrante.




          L.Freddi                                               April 27, 2026   27 / 67
Coordinate polari
Esempio
Calcoliamo l’integrale della funzione f (x, y) = x + y 2 sul settore di corona
circolare di raggi 1 e 2 contenuto nel primo quadrante.

Indicato con E l’insieme in questione:




          L.Freddi                                               April 27, 2026   27 / 67
Coordinate polari
Esempio
Calcoliamo l’integrale della funzione f (x, y) = x + y 2 sul settore di corona
circolare di raggi 1 e 2 contenuto nel primo quadrante.

Indicato con E l’insieme in questione:
     E si può scrivere come unione di due insiemi normali




          L.Freddi                                               April 27, 2026   27 / 67
Coordinate polari
Esempio
Calcoliamo l’integrale della funzione f (x, y) = x + y 2 sul settore di corona
circolare di raggi 1 e 2 contenuto nel primo quadrante.

Indicato con E l’insieme in questione:
     E si può scrivere come unione di due insiemi normali
     oppure si può passare a coordinate polari che trasformano E nel rettangolo
                     R = {(ρ, θ) ∈ R2 : 1 ≤ ρ ≤ 2, 0 ≤ θ ≤ π/2}.




          L.Freddi                                               April 27, 2026   27 / 67
Coordinate polari
Esempio
Calcoliamo l’integrale della funzione f (x, y) = x + y 2 sul settore di corona
circolare di raggi 1 e 2 contenuto nel primo quadrante.

Indicato con E l’insieme in questione:
     E si può scrivere come unione di due insiemi normali
     oppure si può passare a coordinate polari che trasformano E nel rettangolo
                         R = {(ρ, θ) ∈ R2 : 1 ≤ ρ ≤ 2, 0 ≤ θ ≤ π/2}.
     per la formula del cambiamento di variabile si ha
               Z                 Z
                 (x + y ) dxdy = (ρ cos θ + ρ2 sen2 θ)ρdρdθ
                        2
                     E                   R
                                        Z 2         Z π/2                        
                                    =         ρ2             (cos θ + ρ sen2 θ) dθ dρ
                                         1            0
                                        Z 2
                                                      ρ3         15
                                    =         (ρ2 +      π) dρ =    π
                                         1            4          16

          L.Freddi                                                         April 27, 2026   27 / 67
Esempio: integrale di Gauss
Si può utilizzare un passaggio a coordinate polari per calcolare
                                Z +∞             √
                                         2         π
                                     e−x dx =
                                  0               2




         L.Freddi                                                   April 27, 2026   28 / 67
Esempio: integrale di Gauss
Si può utilizzare un passaggio a coordinate polari per calcolare
                                Z +∞             √
                                         2         π
                                     e−x dx =
                                  0               2

    osserviamo che
    Z +∞ Z +∞                      Z +∞         Z +∞            Z +∞ 2 2
                −(x2 +y 2 )              −x2         −y 2
              e             dxdy =     e     dx     e     dy =       e−x dx
      0       0                      0             0                      0




          L.Freddi                                                  April 27, 2026   28 / 67
Esempio: integrale di Gauss
Si può utilizzare un passaggio a coordinate polari per calcolare
                                Z +∞             √
                                         2         π
                                     e−x dx =
                                  0               2

    osserviamo che
    Z +∞ Z +∞                      Z +∞         Z +∞            Z +∞ 2 2
                −(x2 +y 2 )              −x2         −y 2
              e             dxdy =     e     dx     e     dy =       e−x dx
      0       0                      0             0                      0

     quindi          Z +∞
                            2
                                   Z +∞ Z +∞    2  2
                                                            1/2
                         e−x dx =            e−(x +y ) dxdy
                      0                  0    0




          L.Freddi                                                  April 27, 2026   28 / 67
Esempio: integrale di Gauss
Si può utilizzare un passaggio a coordinate polari per calcolare
                                Z +∞             √
                                         2         π
                                     e−x dx =
                                  0               2

    osserviamo che
    Z +∞ Z +∞                      Z +∞         Z +∞            Z +∞ 2 2
                −(x2 +y 2 )              −x2         −y 2
              e             dxdy =     e     dx     e     dy =       e−x dx
      0       0                      0             0                      0

     quindi          Z +∞
                            2
                                   Z +∞ Z +∞    2  2
                                                            1/2
                         e−x dx =            e−(x +y ) dxdy
                      0                  0    0
     passando a coordinate polari si ha
     Z +∞ Z +∞                       Z π/2 Z +∞                   2
                  −(x2 +y 2 )                   −ρ2        π h e−ρ i+∞   π
                e             dxdy =           e ρ dρ dθ =    −        =
      0     0                         0     0              2    2 0      4




          L.Freddi                                                  April 27, 2026   28 / 67
Esempio: integrale di Gauss
Si può utilizzare un passaggio a coordinate polari per calcolare
                                Z +∞             √
                                         2         π
                                     e−x dx =
                                  0               2

    osserviamo che
    Z +∞ Z +∞                      Z +∞         Z +∞            Z +∞ 2 2
                −(x2 +y 2 )              −x2         −y 2
              e             dxdy =     e     dx     e     dy =       e−x dx
      0       0                      0             0                      0

     quindi          Z +∞
                            2
                                   Z +∞ Z +∞    2  2
                                                            1/2
                         e−x dx =            e−(x +y ) dxdy
                        0                0    0
     passando a coordinate polari si ha
     Z +∞ Z +∞                       Z π/2 Z +∞                   2
                  −(x2 +y 2 )                   −ρ2        π h e−ρ i+∞   π
                e             dxdy =           e ρ dρ dθ =    −        =
      0     0                         0     0              2    2 0      4
     e quindi la tesi


          L.Freddi                                                  April 27, 2026   28 / 67
Coordinate polari

Esercizio
Calcolare l’area del dominio D di R2 delimitato dalla spirale di equazione polare
ρ(θ) = θ, θ ∈ [ π2 , 3π
                      2 ] e dalla retta x = 0.




         L.Freddi                                              April 27, 2026   29 / 67
Coordinate polari

Esercizio
Calcolare l’area del dominio D di R2 delimitato dalla spirale di equazione polare
ρ(θ) = θ, θ ∈ [ π2 , 3π
                      2 ] e dalla retta x = 0.

Si ha
                                       π       3π
                    D = {(ρ, θ) :        ≤θ≤      , 0 ≤ ρ ≤ θ}
                                       2        2
cioè, in coordinate polari, D è un trapezio.




         L.Freddi                                                April 27, 2026   29 / 67
Coordinate polari

Esercizio
Calcolare l’area del dominio D di R2 delimitato dalla spirale di equazione polare
ρ(θ) = θ, θ ∈ [ π2 , 3π
                      2 ] e dalla retta x = 0.

Si ha
                                        π        3π
                     D = {(ρ, θ) :        ≤θ≤        , 0 ≤ ρ ≤ θ}
                                        2         2
cioè, in coordinate polari, D è un trapezio. Allora
                Z             Z 3π  Z θ           Z 3π2 θ2      h θ3 i 3π
                                  2                                     2   13 3
       A(D) =      1 dxdy =             ρ dρdθ =           dθ =           =    π
                 D             π
                               2     0              π
                                                    2
                                                         2        6    π
                                                                       2
                                                                            24




         L.Freddi                                                April 27, 2026    29 / 67
Coordinate sferiche
Le coordinate sferiche o coordinate polari in R3 di un punto o vettore di R3 sono
     la distanza ρ dall’origine,
     l’angolo di colatitudine φ formato dal vettore col verso positivo dell’asse z
     l’angolo di longitudine θ formato dalla proiezione del vettore sul piano xy col
     verso positivo dell’asse x
                     z
                                                          
                                 .P(x,y,z)                 x = ρ sen φ cos θ
                         f                                  y = ρ sen φ sen θ
                                                            z = ρ cos φ
                                                          
                             r
                                                 Come nel caso delle coordinate polari,
                                                 per ottenere un diffeomorfismo occorre
                                             y   considerare opportune restrizioni.
                     q
                                 .(x,y)
                                                 Verificare per esercizio che si ha
      x

                                                          | det(∇g)| = ρ2 sen φ.


          L.Freddi                                                      April 27, 2026   30 / 67
Coordinate sferiche
Esercizio
            Z p
Calcolare              |z| dxdydz con
              E

                  E = {(x, y, z) ∈ R3 : x2 + y 2 + z 2 ≤ 1, x ≥ 0, y ≥ 0}




            L.Freddi                                               April 27, 2026   31 / 67
Coordinate sferiche
Esercizio
            Z p
Calcolare              |z| dxdydz con
              E

                  E = {(x, y, z) ∈ R3 : x2 + y 2 + z 2 ≤ 1, x ≥ 0, y ≥ 0}
             4
Risposta:       π
             21




            L.Freddi                                               April 27, 2026   31 / 67
Solidi di rotazione. Coordinate cilindriche
Sia E un sottoinsieme misurabile del piano yz, contenuto nel semipiano y ≥ 0 e
sia S il sottoinsieme di R3 ottenuto facendo ruotare E attorno all’asse z.




        L.Freddi                                             April 27, 2026   32 / 67
Solidi di rotazione. Coordinate cilindriche
Sia E un sottoinsieme misurabile del piano yz, contenuto nel semipiano y ≥ 0 e
sia S il sottoinsieme di R3 ottenuto facendo ruotare E attorno all’asse z. Per
calcolare il volume di S si possono usare le coordinate cilindriche (ρ, θ, z):
                                    z



                                             .P(x,y,z)       
                                                              x = ρ cos θ
                                                               y = ρ sen θ
                                              z
                                                               z=z
                                                             

                                                         y
                                     q   r
                                             .(x,y)
                              x




        L.Freddi                                               April 27, 2026   32 / 67
Solidi di rotazione. Coordinate cilindriche
Sia E un sottoinsieme misurabile del piano yz, contenuto nel semipiano y ≥ 0 e
sia S il sottoinsieme di R3 ottenuto facendo ruotare E attorno all’asse z. Per
calcolare il volume di S si possono usare le coordinate cilindriche (ρ, θ, z):
                                    z



                                             .P(x,y,z)       
                                                              x = ρ cos θ
                                                               y = ρ sen θ
                                              z
                                                               z=z
                                                             

                                                         y
                                     q   r
                                             .(x,y)          | det(∇g)| = ρ
                              x




        L.Freddi                                               April 27, 2026   32 / 67
Solidi di rotazione. Coordinate cilindriche
Sia E un sottoinsieme misurabile del piano yz, contenuto nel semipiano y ≥ 0 e
sia S il sottoinsieme di R3 ottenuto facendo ruotare E attorno all’asse z. Per
calcolare il volume di S si possono usare le coordinate cilindriche (ρ, θ, z):
                                     z



                                             .P(x,y,z)              
                                                                     x = ρ cos θ
                                                                      y = ρ sen θ
                                              z
                                                                      z=z
                                                                    

                                                          y
                                     q   r
                                             .(x,y)                     | det(∇g)| = ρ
                               x




Si ha               Z 2π Z                   Z                      Z
           m(S) =            ρ dρdzdθ = 2π            ρ dρdz = 2π        y dydz.
                     0   E                     E                    E




        L.Freddi                                                         April 27, 2026   32 / 67
Solidi di rotazione. Coordinate cilindriche
Sia E un sottoinsieme misurabile del piano yz, contenuto nel semipiano y ≥ 0 e
sia S il sottoinsieme di R3 ottenuto facendo ruotare E attorno all’asse z. Per
calcolare il volume di S si possono usare le coordinate cilindriche (ρ, θ, z):
                                     z



                                             .P(x,y,z)              
                                                                     x = ρ cos θ
                                                                      y = ρ sen θ
                                              z
                                                                      z=z
                                                                    

                                                          y
                                     q   r
                                             .(x,y)                     | det(∇g)| = ρ
                               x




Si ha               Z 2π Z                   Z                      Z
           m(S) =            ρ dρdzdθ = 2π            ρ dρdz = 2π     y dydz.
                     0   E                     E                     E
                                                                        Z
Se la figura ruota di un angolo 0 < θ0 ≤ 2π, si ha            m(S) = θ0    y dydz.
                                                                             E

        L.Freddi                                                         April 27, 2026   32 / 67
Solidi di rotazione. Baricentro.
Se la figura ruota di un angolo θ0 ∈ (0, 2π], si ha
                                          Z
                              m(S) = θ0       y dydz.
                                           E




         L.Freddi                                       April 27, 2026   33 / 67
Solidi di rotazione. Baricentro.
Se la figura ruota di un angolo θ0 ∈ (0, 2π], si ha
                                          Z
                              m(S) = θ0       y dydz.
                                              E
Il punto di coordinate            Z                         Z
                            1                         1
                    ȳ =              y dxdy, z̄ =              z dzdy
                           m(E)   E                  m(E)   E
è detto baricentro di E.




         L.Freddi                                                    April 27, 2026   33 / 67
Solidi di rotazione. Baricentro.
Se la figura ruota di un angolo θ0 ∈ (0, 2π], si ha
                                          Z
                              m(S) = θ0       y dydz.
                                                E
Il punto di coordinate            Z                          Z
                            1                          1
                    ȳ =               y dxdy, z̄ =              z dzdy
                           m(E)   E                   m(E)   E
è detto baricentro di E.
Usando il baricentro si ha
                                      m(S) = θ0 ȳ m(E)




         L.Freddi                                                     April 27, 2026   33 / 67
Solidi di rotazione. Baricentro.
Se la figura ruota di un angolo θ0 ∈ (0, 2π], si ha
                                          Z
                              m(S) = θ0       y dydz.
                                              E
Il punto di coordinate            Z                         Z
                            1                         1
                    ȳ =              y dxdy, z̄ =              z dzdy
                           m(E)   E                  m(E)   E
è detto baricentro di E.
Usando il baricentro si ha
                              m(S) = θ0 ȳ m(E)
che traduce il seguente teorema:
Teorema (di Pappo e Guldino)
Il volume di un solido ottenuto per rotazione di un insieme misurabile del piano
attorno ad un asse che non lo interseca è uguale al prodotto dell’area della figura
rotante per la lunghezza del cammino percorso dal suo baricentro.




         L.Freddi                                                    April 27, 2026   33 / 67
Solidi di rotazione. Baricentro.
Se la figura ruota di un angolo θ0 ∈ (0, 2π], si ha
                                          Z
                              m(S) = θ0       y dydz.
                                              E
Il punto di coordinate            Z                         Z
                            1                         1
                    ȳ =              y dxdy, z̄ =              z dzdy
                           m(E)   E                  m(E)   E
è detto baricentro di E.
Usando il baricentro si ha
                              m(S) = θ0 ȳ m(E)
che traduce il seguente teorema:
Teorema (di Pappo e Guldino)
Il volume di un solido ottenuto per rotazione di un insieme misurabile del piano
attorno ad un asse che non lo interseca è uguale al prodotto dell’area della figura
rotante per la lunghezza del cammino percorso dal suo baricentro.

Esercizio
Cosa succede se l’asse di rotazione interseca E?
         L.Freddi                                                    April 27, 2026   33 / 67
Solidi di rotazione. Baricentro.
Più in generale...
Definizione
Sia E ⊆ Rn misurabile. Si chiama baricentro di E il punto di coordinate
                              Z
                          1
                 x̄i =          xi dx1 . . . dxn , i = 1, . . . , n.
                       m(E) E




          L.Freddi                                           April 27, 2026   34 / 67
Esercizi
Esercizio (per casa)
Sia                                      √              x
              E = {(x, y) ∈ R2 : 1 ≤ y x ≤ 2, 0 < ≤ y ≤ x}.
                                                         2
Rappresentare graficamente l’insieme E e calcolarne l’area. Calcolare le
coordinate del baricentro di E e il volume del solido ottenuto da una rotazione
completa di E attorno alla retta x + y = 0.




         L.Freddi                                              April 27, 2026   35 / 67
Esercizi
Esercizio (per casa)
Sia                                      √              x
              E = {(x, y) ∈ R2 : 1 ≤ y x ≤ 2, 0 < ≤ y ≤ x}.
                                                         2
Rappresentare graficamente l’insieme E e calcolarne l’area. Calcolare le
coordinate del baricentro di E e il volume del solido ottenuto da una rotazione
completa di E attorno alla retta x + y = 0.
                                                        √
Eseguendo il cambiamento di variabile (u, v) = (y/x, y x), con inversa
                             (x, y) = (v 2/3 u−2/3 , u1/3 v 2/3 ),
l’insieme E si trasforma nel dominio normale
                                                           1
                    g −1 (E) = {(u, v) ∈ R2 : 1 ≤ v ≤ 2,      ≤ u ≤ 1}.
                                                           2
dove g(u, v) = (v 2/3 u−2/3 , u1/3 v 2/3 ). La matrice Jacobiana risulta
                                                                      
                      ∂x   ∂x                 2 2/3 −5/3   2 −1/3 −2/3
                      ∂u   ∂v               −   v  u         v     u
           ∇g =                = 3                      3
                                                                         
                      ∂y   ∂y                1 2/3 −2/3     2 1/3 −1/3
                      ∂u   ∂v                3 v  u         3 u   v
         L.Freddi                                                    April 27, 2026   35 / 67
Esercizi
Il modulo del determinante Jacobiano risulta quindi
                                           2
                          det |∇g(u, v)| = v 1/3 u−4/3 .
                                           3
L’area di E è data da
                     Z           Z
                                         2 1/3 −4/3
         m(E) =          dxdy =           v u       dudv
                       E          g (E) 3
                                   −1


                      2 2 1 1/3 −4/3
                        Z Z
                                                  3
                 =              v u       dudv = (21/3 − 1)(24/3 − 1).
                      3 1 1/2                     2
Le coordinate (x̄, ȳ) del baricentro di E sono
                                        1 2 2 1
                       Z                     Z Z
                 1                                                1
         x̄ =              x dxdy =                vu−2 dudv =        ,
                m(E) E               m(E) 3 1 1/2              m(E)
                                         1 2 2 1 v
                         Z                     Z Z
                    1                                         log 2
            ȳ =             y dxdy =                 dudv =        .
                 m(E) E                m(E) 3 1 1/2 u         m(E)



         L.Freddi                                            April 27, 2026   36 / 67
Esercizi
Per determinare la distanza del baricentro dalla retta r di equazione x + y = 0
osserviamo che l’equazione della normale ad r passante per (x̄, ȳ) è
                                           log 2 − 1
                                  y =x+
                                             m(E)
e che il punto di intersezione tra le due rette ha coordinate
                                  log 2 − 1 1 − log 2
                                (          ,          )
                                   2m(E) 2m(E)
e la distanza tra i due punti, cioè il raggio della circonferenza percorsa dal
baricentro nella rotazione attorno alla retta r, risulta
                                        1 + log 2
                                              √ .
                                        m(E) 2
Per il Teorema di Guldino il volume del solido di rotazione risulta quindi
                                    1 + log 2      1 + log 2
                     V = m(E)2π           √ =π √             .
                                    m(E) 2              2



         L.Freddi                                                  April 27, 2026   37 / 67
Esercizi per casa
Esercizio
Determinare le coordinate del baricentro e il volume dell’insieme
                                       x2 + y 2 + z 2 1
     B = {(x, y, z) ∈ R3 : 0 ≤ z ≤                   ,   ≤ x2 + y 2 + z 2 ≤ 1}.
                                            2          4

Esercizio
Si consideri l’insieme B = {(x, y, z) : x2 + y 2 ≤ (1 − z 2 )2 , 0 ≤ z ≤ 2}.
Tracciare l’intersezione B ′ dell’insieme B con il piano zx. Calcolare il volume di
B. Calcolare l’integrale           Z
                                       (z + x3 ) dxdz.
                                  B′




         L.Freddi                                                April 27, 2026   38 / 67
Esercizi per casa
Esercizio
Sia D = {(x, y) ∈ R2 : 1 ≤ |x| + |y| ≤ 2}. Rappresentare graficamente l’insieme
D e calcolarne l’area. Calcolare quindi il volume del solido ottenuto da una
rotazione completa dell’insieme D attorno all’asse x = 5. Calcolare infine
l’integrale                  Z
                                (x2 − x) |y| − 1 dxdy.
                              D


Esercizio
Data la funzione f (x, y) = max{|x|, 2|y|, |x| + y}, sia

                        D = {(x, y) ∈ R2 : f (x, y) ≤ 2}.

Rappresentare graficamente l’insieme D e calcolarne l’area. Calcolare le
coordinate del baricentro di D ed il volume del solido ottenuto da una rotazione
completa
Z         dell’insieme D attorno all’asse x = 5. Calcolare infine l’integrale doppio
   (|x| + x)y dxdy.
 D
         L.Freddi                                                April 27, 2026   39 / 67
Esercizi per casa
Esercizio
Calcolare l’integrale
                           x2 + y 2
                        Z
                                       y
                               2
                                    log dxdy
                         D   x         x
dove D è la porzione di corona circolare
                                                       √
                                                        
                            2         2   2   x
          D = (x, y) ∈ R : 1 ≤ x + y ≤ 9, y ≥ √ , y ≤ x 3 .
                                               3




         L.Freddi                                  April 27, 2026   40 / 67
Esercizi per casa
Esercizio
Calcolare l’integrale
                              x2 + y 2
                          Z
                                          y
                                  2
                                       log dxdy
                            D   x         x
dove D è la porzione di corona circolare
                                                       √
                                                        
                            2         2   2   x
          D = (x, y) ∈ R : 1 ≤ x + y ≤ 9, y ≥ √ , y ≤ x 3 .
                                               3

Per ragioni di simmetria
                     x2 + y 2
                                             ZZ 2
                                                 x + y2
                 ZZ
                                  y                        y
            I=             2
                              log   dxdy = 2         2
                                                        log dxdy
                   D     x        x            S   x       x
dove S = D ∩ {x ≥ 0, y ≥ 0}.




         L.Freddi                                        April 27, 2026   40 / 67
Esercizi per casa
Passando a coordinate polari x = ρ cos θ, y = ρ sin θ, ρ ≥ 0, θ ∈ [0, 2π[, si ha
                                                π           π
                    S = {(ρ, θ) : 1 ≤ ρ ≤ 3,       ≤θ≤ }
                                                6           3
e
     Z π3 Z 3                                  2 3 Z π
                                                ρ         3
I=2           (1+tan2 θ) log(tan θ)ρ dρdθ = 2               (1+tan2 θ) log(tan θ) dθ
       π
       6   1                                     2   1 6
                                                        π


e, integrando per parti
                                                        Z π3
                                              π
                    I   = 8 [tan θ log(tan θ)] π3 − 8          (1 + tan2 θ) dθ =
                                               6         π
                                                         6
                                                     π    16
                        = 8 [tan θ (log(tan θ) − 1)] π3 = √ (log 3 − 1).
                                                      6
                                                           3




         L.Freddi                                                           April 27, 2026   41 / 67
Esercizi per casa
Esercizio
Sia D ⊂ R2 la regione di piano cosı̀ definita:

                        D{(x, y) ∈ R2 t.c. 0 < x < y : x < x2 + y 2 < 2x}.

Si calcoli                            Z
                                                xy
                                                            dxdy.
                                       D   (x2 + y 2 )3/2




             L.Freddi                                                 April 27, 2026   42 / 67
Esercizi per casa
Esercizio
Calcolare l’integrale     Z        √
                                       xy            y
                                              artg         dxdy,
                           D   (x2 + y 2 )2           x
dove D è il dominio cosı̀ definito:

                      D = (x, y) ∈ R2 : 0 < x < x2 + y 2 .
                            


Esercizio
Calcolare il seguente integrale:
                               Z
                                       1
                                               dxdy,
                                D 1 + (x + y)4

ove D = {(x, y) ∈ R2 , x > 0, y > 0}.



         L.Freddi                                                  April 27, 2026   43 / 67
Esercizi per casa
Esercizio
Determinare il volume del solido D individuato dall’intersezione del cilindro

                    C = {(x, y, z) ∈ R3 : x2 + y 2 ≤ 4, 0 ≤ z ≤ 2}

col sottografico della funzione
                                                1
                                  f (x, y) = p       .
                                              x + y2
                                               2




         L.Freddi                                               April 27, 2026   44 / 67
Esercizi per casa
Esercizio
Determinare il volume del solido D individuato dall’intersezione del cilindro

                    C = {(x, y, z) ∈ R3 : x2 + y 2 ≤ 4, 0 ≤ z ≤ 2}

col sottografico della funzione
                                                1
                                  f (x, y) = p       .
                                              x + y2
                                               2


D si può scrivere come unione dei domini D1 e D2 definiti nel modo seguente
                    D1 = {(x, y, z) : (x, y) ∈ B(0, 1/2), 0 ≤ z ≤ 2}
                                                                 1
      D2 = {(x, y, z) : (x, y) ∈ B(0, 2) \ B(0, 1/2), 0 ≤ z ≤ p         }
                                                               x2 + y 2
B(0, 1/2) e B(0, 2) essendo le sfere di R2 di centro (0, 0) e raggio,
rispettivamente, 1/2 e 2.


         L.Freddi                                                April 27, 2026   44 / 67
Esercizi per casa
In coordinate cilindriche        
                                  x = ρ cos θ
                                   y = ρ sen θ
                                   z=z
                                 
divengono
                    D1 = {(ρ, θ, z) : 0 ≤ ρ ≤ 1/2, 0 ≤ z ≤ 2}
                                                           1
                D2 = {(ρ, θ, z) : 1/2 ≤ ρ ≤ 2, 0 ≤ z ≤ p        }.
                                                         x + y2
                                                          2

Si ha dunque, passando da ccordinate cartesiane a coordinate colindriche e
usando le formule di riduzione per domini normali
                       Z              Z            Z
            m(D) =         dxdydz =       dxdydz +      dxdydz
                        ZD1/2 Z 2      D1            D2
                                              Z 2 Z 1/ρ
                                                                 7
                    2π            ρ dzdρ + 2π           ρ dzdρ = π.
                         0     0               1/2 0             2




         L.Freddi                                             April 27, 2026   45 / 67
Esercizi per casa
Si poteva ottenere lo stesso risultato osservando che D è un solido di rotazione,
ottenuto ruotando attorno all’asse z il dominio normale di R2
A = {(x, z) : 0 ≤ x ≤ 1/2, 0 ≤ z ≤ 2} ∪ {(x, z) : 1/2 ≤ x ≤ 2, 0 ≤ z ≤ 1/x}
e applicando il Teorema di Guldino.




         L.Freddi                                               April 27, 2026   46 / 67
Esercizi per casa
Esercizio
Calcolare l’area del solido ottenuto facendo ruotare attorno all’asse z il dominio
normale di R2

         D = {(x, z) ∈ R2 : 0 ≤ z ≤ 2, 0 ≤ x ≤ 2π − arccos(z − 1)}.




         L.Freddi                                                April 27, 2026   47 / 67
Esercizi per casa
Esercizio
Calcolare il volume del solido ottenuto facendo ruotare attorno all’asse x il
dominio costituito dall’unione del quadrato Q e del settore circolare S
rappresentati in figura.

                                y
                               6




                                            S




                               3




                                            Q




                                                       x
                                    1              4




         L.Freddi                                                April 27, 2026   48 / 67
Esercizi per casa
Esercizio
Calcolare l’area del dominio normale
                                       √ p              p
          D = {(x, y) ∈ R2 : 0 ≤ y ≤ 1/ 2, 1 + y 2 ≤ x ≤ 2 − y 2 }.

Sia poi
                     S = {(x, y) ∈ R2 : x2 − y 2 ≤ 1, x2 + y 2 ≤ 2};
rappresentare graficamente S e calcolarne l’area.




          L.Freddi                                               April 27, 2026   49 / 67
Esercizi per casa
Esercizio
Calcolare l’area del dominio normale
                                       √ p              p
          D = {(x, y) ∈ R2 : 0 ≤ y ≤ 1/ 2, 1 + y 2 ≤ x ≤ 2 − y 2 }.

Sia poi
                     S = {(x, y) ∈ R2 : x2 − y 2 ≤ 1, x2 + y 2 ≤ 2};
rappresentare graficamente S e calcolarne l’area.

Per le formule di riduzione degli integrali doppi su domini normali
                           Z            Z 1/√2  Z √2−y2 
              m(D) =           dxdy =               √      dx dy
                                D           0             1+y 2
                              Z 1/√2 p                Z 1/√2 p
                          =              2 − y 2 dy −         1 + y 2 dy
                                0                     0




          L.Freddi                                                 April 27, 2026   49 / 67
Esercizi per casa
                                        √
Facendo il cambiamento di variabile y = 2 sen t nel primo integrale e y = senht
nel secondo si ha
                  Z π/6             Z senh(1/√2)
         m(D) = 2          2
                        cos t dt −               cosh2 t dt
                         0               0
                      Z π/6                           √
                                            1 senh(1/ 2)
                                             Z
                    =    [1 + cos(2t)] dt −              [1 + cosh(2t)] dt
                       0                    2 0
                         √
                      π    3 1           1     1               1 
                    = +      − senh( √ ) − senh 2senh( √ )
                      6   4    2          2    4                2
                         √                      √
                      π    3 1           1     ( 3 + 1)4 + 4
                    = +      − senh( √ ) −          √        .
                      6   4    2          2      16( 3 + 1)
Infine
                                  |S| = 2π − 4m(D).




         L.Freddi                                               April 27, 2026   50 / 67
Esercizi per casa
Esercizio
Calcolare il volume della porzione di solido sferico racchiuso in una superficie
cilindrica circolare di diametro uguale al raggio R di una data sfera, nei casi in cui
  1   l’asse del cilindro passi per il centro della sfera;
  2   la superficie cilindrica passi per il centro della sfera.




          L.Freddi                                                April 27, 2026   51 / 67
Esercizi per casa
Esercizio
Calcolare il volume della porzione di solido sferico racchiuso in una superficie
cilindrica circolare di diametro uguale al raggio R di una data sfera, nei casi in cui
  1   l’asse del cilindro passi per il centro della sfera;
  2   la superficie cilindrica passi per il centro della sfera.

1. In un sistema di riferimento cartesiano ortogonale centrato nel centro della
sfera, la sfera ha equazione cartesiana x2 + y 2 + z 2 ≤ R2 , mentre la superficie
cilindrica ha equazione (in R3 ) x2 + y 2 = R2 /4. Indicato con D il cerchio del
piano xy
                          D = {(x, y) : x2 + y 2 ≤ R2 /4},
il solido in questione può essere scritto come insieme normale nel modo seguente
                                        p                     p
      S = {(x, y, z) : (x, y) ∈ D, − R2 − x2 − y 2 ≤ z ≤ R2 − x2 − y 2 }




          L.Freddi                                                April 27, 2026   51 / 67
Esercizi per casa
Pertanto                            Z p
                           m(S) = 2    R2 − x2 − y 2 dxdy.
                                      D
Passando a coordinate polari nel piano xy:
                      
                        x = ρ cos θ
                                      , ρ ≥ 0, θ ∈ [0, 2π[
                        y = ρ sin θ
D viene trasformato nell’insieme
                      g −1 (D) = {(ρ, θ) : 0 ≤ θ ≤ 2π, 0 ≤ ρ ≤ R/2}
e quindi, applicando la formula del cambiamento di variabile, si ha
             Z 2π Z R/2 p
                                              2 2π  2
                                                Z
                                                                    R/2
  m(S) = 2                   2     2
                         ρ R − ρ dρ dθ = −            (R − ρ2 )3/2 0 dθ
              0    0                          3  0
             4  2                          4      3          8 − 33/2
         = − π (R − R2 /4)3/2 − R3 = − πR3 )3/2 − 1 =                    πR3 .
                                       
             3                              3       4                 6




           L.Freddi                                              April 27, 2026   52 / 67
Esercizi per casa
2. In un opportuno sistema di riferimento cartesiano ortogonale centrato nel
centro della sfera, la sfera ha equazione cartesiana x2 + y 2 + z 2 ≤ R2 , mentre la
superficie cilindrica ha equazione (in R3 ) x2 + (y − R/2)2 = R2 /4. Indicato con
D il cerchio del piano xy
                    D = {(x, y) : x2 + (y − R/2)2 ≤ R2 /4},
il solido in questione può essere scritto come insieme normale nel modo seguente
                                        p                    p
      S = {(x, y, z) : (x, y) ∈ D, − R2 − x2 − y 2 ≤ z ≤ R2 − x2 − y 2 }
e pertanto                      Z p
                       m(S) = 2    R2 − x2 − y 2 dxdy.
                                   D




         L.Freddi                                                April 27, 2026   53 / 67
Esercizi per casa
Passando a coordinate polari nel piano xy:
                      
                        x = ρ cos θ
                                      , ρ ≥ 0, θ ∈ [0, 2π[
                        y = ρ sin θ
D viene trasformato nell’insieme
                    g −1 (D) = {(ρ, θ) : 0 ≤ θ ≤ π, 0 ≤ ρ ≤ R sin θ}
e quindi, applicando la formula del cambiamento di variabile, si ha
              Z π Z R sin θ p
                                                2 π 2
                                                  Z
                                                                    R sin θ
  m(S) = 2                     2     2
                           ρ R − ρ dρ dθ = −          (R − ρ2 )3/2 0         dθ
               0                                3 0
                 Z π0                                   Z π
              2                                       2
                       (R − R2 sin2 θ)3/2 − R3 dθ = −
                       2                                    3
                                                             R cos3 θ − R3 dθ
                                                                              
         =−
              3 0                                     3 0
            2 3
         = πR .
            3




         L.Freddi                                                April 27, 2026   54 / 67
Esercizi per casa
Esercizio
Data la funzione
                            f (x, y) = x3 y 2 (1 − x − y),


  1   disegnare l’insieme L0 = {(x, y) ∈ R2 : f (x, y) = 0} (cioè l’insieme di
      livello 0 di f );
  2   l’insieme L0 individua una partizione di R2 costituita da un sottoinsieme
      limitato che denotiamo con T e da altri sottoinsiemi non limitati;
       a. discutere la questione dell’esistenza del massimo e del minimo di f
          sulla chiusura di T e, nel caso in cui esistano, calcolarli;
       b. calcolare                    Z
                                           f (x, y) dxdy.
                                         T




          L.Freddi                                               April 27, 2026   55 / 67
Esercizi per casa
Esercizio
Data la funzione
                             f (x, y) = x3 y 2 (1 − x − y),


  1   disegnare l’insieme L0 = {(x, y) ∈ R2 : f (x, y) = 0} (cioè l’insieme di
      livello 0 di f );
  2   l’insieme L0 individua una partizione di R2 costituita da un sottoinsieme
      limitato che denotiamo con T e da altri sottoinsiemi non limitati;
       a. discutere la questione dell’esistenza del massimo e del minimo di f
          sulla chiusura di T e, nel caso in cui esistano, calcolarli;
       b. calcolare                    Z
                                           f (x, y) dxdy.
                                          T

1. L’insieme L0 è costituito dai punti degli assi coordinati e da quelli della retta di
equazione y = 1 − x.

          L.Freddi                                                 April 27, 2026   55 / 67
Esercizi per casa
2.a. Poichè T è chiuso e limitato e f è continua in T , allora per il teorema di
Weierstrass esistono il massimo e il minimo di f in T .
T si può scrivere in vari modi. Ad esempio, osservando che si tratta di un insieme
normale rispetto ad entrambi gli assi, si può scrivere nella forma
                    T = {(x, y) ∈ R2 : 0 ≤ x ≤ 1, 0 ≤ y ≤ 1 − x}
Cominciamo la ricerca del massimo e del minimo di f su T cercando eventuali
punti stazionari interni. Si ha
         fx (x, y) = x2 y 2 (3 − 4x − 3y),   fy (x, y) = x3 y(2 − 2x − 3y),
e risultano quindi stazionari tutti i punti degli assi coordinati e le soluzioni del
sistema                          
                                    3 − 4x − 3y = 0
                                    2 − 2x − 3y = 0
I punti degli assi non ci interessano perchè non sono interni, mentre l’unica
soluzione del sistema, cioè il punto (1/2, 1/3), è un punto stazionario interno.
Cerchiamo di stabilire se si tratta di un punto di massimo o di minimo locale con
il criterio della matrice hessiana.

         L.Freddi                                                April 27, 2026   56 / 67
Esercizi per casa
Si ha
         fxx (x, y) = 6xy 2 − 12x2 y 2 − 6xy 3 , fyy (x, y) = 2x3 − 2x4 − 6x3 y,
                             fx,y (x, y) = 6x2 y − 8x3 y − 9x2 y 2 ,
quindi                                                                
                            2                     −1/9 −1/12
                           ∇ f (1/2, 1/3) =
                                                  −1/12 −1/8.
che ha determinante positivo, quindi il punto (1/2, 1/3) è di massimo locale.
Poiché f sulla frontiera di T è identicamente nulla, possiamo concludere che
                      min f = 0,       max f = f (1/2, 1/3) = 1/432.
                       T                 T




           L.Freddi                                                        April 27, 2026   57 / 67
Esercizi per casa
2.b. Per le formule di riduzione si ha
              Z                   Z 1  Z 1−x                        
                 f (x, y) dxdy =               x3 y 2 (1 − x − y) dy dx
               T                   0     0
                               Z 1  Z 1−x
                                                                  
                                   x3
                                                2
                                                y (1 − x) − y 3 dy dx
                                0        0
                               Z 1 h                         i1−x
                                   x3 y 3 (1 − x)/3 − y 4 /4       dx
                                0                             0
                               Z 1
                                      (1 − x)4                 299
                                   x3           dx = · · · =       .
                                0        12                   3480




         L.Freddi                                                April 27, 2026   58 / 67
Esercizi per casa
Esercizio
                                                    ex + e−x
Sia D la parte di sottografico della funzione y =              contenuta nel
                                                        2
semipiano delle y ≥ 0 e nella striscia |x| ≤ 1, privata della palla di centro (0, 1/2)
e raggio 1/4.
  1     Disegnare D, dire se è misurabile e, in caso affermativo, calcolarne l’area.
  2     Calcolare il volume del solido S ottenuto ruotando D attorno alla retta di
        equazione y = −1.
                                                                  ex + e−x
1. Indicata con T la parte di sottografico della funzione y =              contenuta
                                                                      2
nel semipiano delle y ≥ 0 e nella striscia |x| ≤ 1, cioè
                                                            ex + e−x
                       T = {(x, y) : −1 ≤ x ≤ 1, 0 ≤ y ≤             },
                                                                2
si ha
                                       D =T \B
dove B denota la palla di centro (0, 1/2) e raggio 1/4.
            L.Freddi                                                April 27, 2026   59 / 67
Esercizi per casa
Poiché gli insiemi a secondo membro sono entrambi misurabili e
                                        B⊆T
allora D è misurabile e, per l’additività della misura, si ha
                             m2 (D) = m2 (T ) − m2 (B).
T è un dominio normale e per le formule di riduzione si ha
                         Z 1 Z cosh x         h      i1     e2 − 1
               m2 (T ) =              dydx = senhx        =
                          −1 0                        −1       e
e perciò
                                           e2 − 1 π
                                m2 (D) =         − .
                                              e   4




            L.Freddi                                              April 27, 2026   60 / 67
Esercizi per casa
2. Per l’additività dell’integrale
                Z            Z             Z        Z        Z
                     y dy =         y dy =   y dy −   y dy =   y dy
                    D       T \B          T          B         T
           R
in quanto B y dy = 0. Si ha dunque
                                            cosh2 x
         Z         Z 1 Z cosh x         Z 1
                                                        1 senh2
            y dy =              ydydx =             dx = +      .
          D         −1 0                 −1    2        2   4
Poiché la distanza del baricentro dall’asse di rotazione è
                            1 senh2             3 senh2
                              +         +1= +
                            2      4            2      4
allora, per teorema di Guldino, il volume di S è
                                               senh2 
                              m3 (S) = π 3 +            .
                                                   2




         L.Freddi                                                  April 27, 2026   61 / 67
Esercizi per casa
Esercizio
Calcolare il volume del sottoinsieme C di R3 delimitato dal cono di equazione

                                  |x| + |y| = z

e dal piano di equazione
                                x + y + 2z = 3.




         L.Freddi                                             April 27, 2026    62 / 67
Esercizi per casa
Esercizio
Determinare per quali valori di p ∈ R risulta sommabile su R2 la funzione
                                                 1
                               (x, y) 7→
                                           (1 + x2 + y 2 )p

e, in corrispondenza di essi, calcolare il valore dell’integrale
                              Z
                                          1
                                          2     2 p
                                                    dx dy.
                               R2 (1 + x + y )




          L.Freddi                                                 April 27, 2026   63 / 67
Esercizi per casa
Esercizio
Determinare per quali valori di p ∈ R risulta sommabile su R2 la funzione
                                                 1
                               (x, y) 7→
                                           (1 + x2 + y 2 )p

e, in corrispondenza di essi, calcolare il valore dell’integrale
                              Z
                                          1
                                          2     2 p
                                                    dx dy.
                               R2 (1 + x + y )

Indicata con BR (0) la palla di R2 di raggio R si ha, passando a coordinate polari,
 Z                                 Z R Z 2π                       Z R
                1                                ρ                       2ρ
                2   2 p
                        dx  dy   =                 2  p
                                                        dθ dρ = π           2 p
                                                                                dρ
   BR (0) (1 + x + y )              0    0   (1 + ρ )              0 (1 + ρ )
                                        h            iR
                                        log(1 + ρ2 )
                                       
                                                                  se p = 1
                                                              0
                                  =π     h (1 + ρ2 )1−p iR
                                       
                                       
                                                                  se p ̸= 1
                                              1−p        0
          L.Freddi                                                    April 27, 2026   63 / 67
Esercizi per casa
Si ha dunque
                                                 
                    Z                             +∞
                                                            se p ≤ 1
                                 1
            lim                  2   2 p
                                         dx dy =    π
          R→+∞      BR (0) (1 + x + y )                     se p > 1.
                                                   p−1
                                                 
                                                                          π
quindi la funzione è sommabile per ogni p > 1 con integrale uguale a        .
                                                                         p−1




         L.Freddi                                              April 27, 2026    64 / 67
Esercizi per casa
Esercizio
Calcolare il volume del solido ottenuto da una rotazione completa attorno alla
retta di equazione y = −x dell’insieme

                D = {(x, y) ∈ R2 : x ∈ [0, 2π], 0 ≤ y ≤ 2 + cos x}.




         L.Freddi                                              April 27, 2026    65 / 67
Esercizi per casa
Esercizio
Calcolare il volume del solido delimitato dal cilindro di equazione

                                    x2 + y 2 = log 2

e dalle superfici ottenute ruotando l’iperbole del piano yz di equazione
z 2 − y 2 = 1 attorno all’asse z.

Considerato l’insieme
                                            p              p
                    E = {(y, z) : 0 ≤ y ≤    log 2, 0 ≤ z ≤ 1 + y 2 }
e detto S il solido generato dalla rotazione di E attorno all’asse z si ha
                                     V = 2m3 (S).
Il solido di cui si chiede di calcolare il volume è rappresentato in figura.




         L.Freddi                                                   April 27, 2026   66 / 67
Esercizi per casa
Per il Teorema di Guldino, detta
                                                 Z
                                         1
                               ȳ =                   y dydz
                                       m2 (E)     E
si ha                                                     Z
                       m3 (S) = 2π ȳ m2 (E) = 2π              y dydz.
                                                           E
Essendo E un insieme normale, per le formule di riduzione si ha
                      Z √log 2 Z √1+y2
         R
           E
             y dydz =                   ydzdy
                          0            0
                           Z √log 2 p
                         1
                       =           2y 1 + y 2 dy
                         2 0
                         1h2               ilog 2  1
                       =     (1 + y 2 )3/2        = [(1 + log2 2)3/2 − 1].
                         2 3                0      3
e quindi
                                   Z
                                                      4
                V = 2m3 (S) = 4π           y dydz =     π[(1 + log2 2)3/2 − 1].
                                   E                  3
           L.Freddi                                                      April 27, 2026   67 / 67
