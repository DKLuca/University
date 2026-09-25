---
fonte: "An2_2026_pres12_dini.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Funzioni implicite

                 L.Freddi


              April 16, 2026




L.Freddi                        April 16, 2026   1 / 22
Curve in forma implicita

Vediamo ora come ci si possa ricondurre alla rappresentazione cartesiana locale di
una curva in R2 quando la curva viene data nella forma implicita
                                   F (x, y) = 0




         L.Freddi                                              April 16, 2026   2 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                       F (x0 , y0 ) = 0 e     (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                    ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.                     (1)




         L.Freddi                                                April 16, 2026   3 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                       F (x0 , y0 ) = 0 e     (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                     ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.                    (1)




In altri termini,




          L.Freddi                                               April 16, 2026   3 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                       F (x0 , y0 ) = 0 e     (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                     ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.                    (1)




In altri termini,
     (1) si può sostituire con: esiste una funzione f : U → V con legge y = f (x)
     tale che F (x, f (x)) = 0




          L.Freddi                                               April 16, 2026   3 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                       F (x0 , y0 ) = 0 e     (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                     ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.                    (1)




In altri termini,
     (1) si può sostituire con: esiste una funzione f : U → V con legge y = f (x)
     tale che F (x, f (x)) = 0
     cioè nell’intorno U la curva cartesiana implicita F (x, y) = 0 ammette la
     rappresentazione esplicita y = f (x)


          L.Freddi                                               April 16, 2026   3 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                       F (x0 , y0 ) = 0 e     (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                     ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.                        (1)




In altri termini,
     (1) si può sostituire con: esiste una funzione f : U → V con legge y = f (x)
     tale che F (x, f (x)) = 0
     cioè nell’intorno U la curva cartesiana implicita F (x, y) = 0 ammette la
     rappresentazione esplicita y = f (x)
     derivando F (x, f (x)) = 0 si ottiene Fx (x, f (x)) + Fy (x, f (x))f ′ (x) = 0

          L.Freddi                                                 April 16, 2026     3 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                       F (x0 , y0 ) = 0 e     (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                    ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.                       (1)
                1
Inoltre f ∈ C (U ) e si ha
                                        Fx (x, f (x))
                            f ′ (x) = −               .                             (2)
                                        Fy (x, f (x))

In altri termini,
     (1) si può sostituire con: esiste una funzione f : U → V con legge y = f (x)
     tale che F (x, f (x)) = 0
     cioè nell’intorno U la curva cartesiana implicita F (x, y) = 0 ammette la
     rappresentazione esplicita y = f (x)
     derivando F (x, f (x)) = 0 si ottiene Fx (x, f (x)) + Fy (x, f (x))f ′ (x) = 0 e
     quindi la formula (2)
          L.Freddi                                                 April 16, 2026       3 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                       F (x0 , y0 ) = 0 e     (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                    ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.
                1
Inoltre f ∈ C (U ) e si ha
                                        Fx (x, f (x))
                            f ′ (x) = −               .
                                        Fy (x, f (x))

In altri termini,
     la curva risulta localmente grafico di una funzione, quindi ha
     rappresentazione parametrica φ(t) = (t, f (t))




          L.Freddi                                               April 16, 2026   4 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                        F (x0 , y0 ) = 0 e    (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                    ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.
                1
Inoltre f ∈ C (U ) e si ha
                                        Fx (x, f (x))
                            f ′ (x) = −               .
                                        Fy (x, f (x))

In altri termini,
     la curva risulta localmente grafico di una funzione, quindi ha
     rappresentazione parametrica φ(t) = (t, f (t))
     poiché |φ′ (t)|2 = 1 + |f ′ (t)|2 ̸= 0, la curva è regolare (localmente)




          L.Freddi                                                   April 16, 2026   4 / 22
Il teorema delle funzioni implicite
Teorema (del Dini o delle funzioni implicite)
Sia F ∈ C 1 (Ω) dove Ω è un aperto di R2 . Sia (x0 , y0 ) ∈ Ω tale che
                                           ∂F
                        F (x0 , y0 ) = 0 e    (x0 , y0 ) ̸= 0.
                                           ∂y
Allora esistono un intorno U di x0 ed un intorno V di y0 tali che
                    ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.
                1
Inoltre f ∈ C (U ) e si ha
                                        Fx (x, f (x))
                            f ′ (x) = −               .
                                        Fy (x, f (x))

In altri termini,
     la curva risulta localmente grafico di una funzione, quindi ha
     rappresentazione parametrica φ(t) = (t, f (t))
     poiché |φ′ (t)|2 = 1 + |f ′ (t)|2 ̸= 0, la curva è regolare (localmente)
     la condizione sufficiente ∂F
                               ∂y (x0 , y0 ) ̸= 0 viene quindi detta condizione di
     regolarità

          L.Freddi                                                   April 16, 2026   4 / 22
Il teorema delle funzioni implicite
                                                        ∂F
Dimostrazione Supponiamo, per fissare le idee, che         (x0 , y0 ) > 0. Poichè
                                                        ∂y
       1
F ∈ C (Ω) allora Fy è continua, quindi per la permanenza del segno esiste un
rettangolo chiuso R = W × V centrato in (x0 , y0 ) tale che Fy > 0 in R.
Per ogni fissato x ∈ W , la funzione
                                     y 7→ F (x, y)
è dunque crescente in V = [y0 − h, y0 + h]. In particolare è strettamente
crescente la funzione
                                 y 7→ F (x0 , y),
e, siccome F (x0 , y0 ) = 0, si ha
                      F (x0 , y0 − h) < 0 e F (x0 , y0 + h) > 0.                    (3)
D’altra parte, le funzioni
                       x 7→ F (x, y0 − h),   x 7→ F (x, y0 + h),
sono continue in W .



          L.Freddi                                                 April 16, 2026    5 / 22
Il teorema delle funzioni implicite
Per il teorema della permanenza del segno e per le (3) esisterà un intorno U di
x0 , U ⊆ W , tale che
              F (x, y0 − h) < 0 e F (x, y0 + h) > 0 per ogni x ∈ U.
                                   y

                            y +h
                               0
                                                       .
                                           +++++++++++++++++++++
                                                 (x 0, y0 +h)



                           Ω
                                       V              .
                                                    (x , y )
                                                      0    0




                            y -h
                               0
                                                    .
                                                  (x 0, y0 -h)
                                           -------------------
                                                    U
                                                      W
                                                                   x



Riassumendo, per ogni fissato x ∈ U la funzione y 7→ F (x, y) è continua e
strettamente crescente in V = [y0 − h, y0 + h]. Per il teorema degli zeri si può
dunque concludere che esiste uno ed un sol punto y ∈ V tale che F (x, y) = 0, o,
in altre parole, che esiste una funzione f : U → V tale che
                        F (x, f (x)) = 0              per ogni x ∈ U.
         L.Freddi                                                       April 16, 2026   6 / 22
Il teorema delle funzioni implicite
Abbiamo cosı̀ dimostrato la prima parte del teorema. Resta da mostrare che la
funzione f (x) è di classe C 1 in U . A tal scopo consideriamo x e x1 in U . I punti
(x, f (x)) e (x1 , f (x1 )) appartengono al rettangolo U × V tutto contenuto in Ω e
quindi è contenuto in Ω il segmento che li congiunge. Poichè F ∈ C 1 (Ω), per il
teorema di Lagrange esisterà un punto (ξ, η) appartenente al segmento (e quindi
a Ω) tale che
    F (x, f (x)) − F (x1 , f (x1 )) = Fx (ξ, η)(x − x1 ) + Fy (ξ, η)(f (x) − f (x1 )).
D’altra parte, per definizione di f , il primo membro di quest’ultima uguaglianza è
nullo, e quindi si ottiene
                             f (x) − f (x1 )    Fx (ξ, η)
                                             =−                                          (4)
                                 x − x1         Fy (ξ, η)
da cui segue immediatamente
                                               max |Fx |
                                                R
                         |f (x) − f (x1 )| ≤               |x − x1 |
                                               min |Fy |
                                                R
e quindi la continuità della funzione f .

          L.Freddi                                                     April 16, 2026    7 / 22
Il teorema delle funzioni implicite
La formula che fornisce la derivata di f in x si trova infine passando al limite per
x → x1 nella (4) tenendo conto della continuità di f e delle derivate parziali di
F.




         L.Freddi                                                April 16, 2026   8 / 22
Il teorema delle funzioni implicite
Osserviamo che
    è chiaro che, se invece
                                                   ∂F
                          F (x0 , y0 ) = 0 e          (x0 , y0 ) ̸= 0,
                                                   ∂x
    allora in un intorno di (x0 , y0 ) l’insieme
                               Z = {(x, y) : F (x, y) = 0}
    sarà grafico di una funzione x = g(y)




        L.Freddi                                                         April 16, 2026   9 / 22
Il teorema delle funzioni implicite
Osserviamo che
    è chiaro che, se invece
                                                   ∂F
                          F (x0 , y0 ) = 0 e          (x0 , y0 ) ̸= 0,
                                                   ∂x
    allora in un intorno di (x0 , y0 ) l’insieme
                               Z = {(x, y) : F (x, y) = 0}
    sarà grafico di una funzione x = g(y)
    in conclusione, se
                          F (x0 , y0 ) = 0 e       ∇F (x0 , y0 ) ̸= 0,
    allora in un intorno di (x0 , y0 ) l’insieme Z degli zeri di F è sostegno di una
    curva grafico (rispetto a uno degli assi)




        L.Freddi                                                         April 16, 2026   9 / 22
Il teorema delle funzioni implicite
Osserviamo che
    è chiaro che, se invece
                                                   ∂F
                          F (x0 , y0 ) = 0 e          (x0 , y0 ) ̸= 0,
                                                   ∂x
    allora in un intorno di (x0 , y0 ) l’insieme
                               Z = {(x, y) : F (x, y) = 0}
    sarà grafico di una funzione x = g(y)
    in conclusione, se
                          F (x0 , y0 ) = 0 e       ∇F (x0 , y0 ) ̸= 0,
    allora in un intorno di (x0 , y0 ) l’insieme Z degli zeri di F è sostegno di una
    curva grafico (rispetto a uno degli assi)
    se poi il gradiente non si annulla mai su Z, allora Z è unione di sostegni di
    curve grafico (anche rispetto ad assi diversi),



        L.Freddi                                                         April 16, 2026   9 / 22
Il teorema delle funzioni implicite
Osserviamo che
    è chiaro che, se invece
                                                   ∂F
                          F (x0 , y0 ) = 0 e          (x0 , y0 ) ̸= 0,
                                                   ∂x
    allora in un intorno di (x0 , y0 ) l’insieme
                                Z = {(x, y) : F (x, y) = 0}
    sarà grafico di una funzione x = g(y)
    in conclusione, se
                          F (x0 , y0 ) = 0 e       ∇F (x0 , y0 ) ̸= 0,
    allora in un intorno di (x0 , y0 ) l’insieme Z degli zeri di F è sostegno di una
    curva grafico (rispetto a uno degli assi)
    se poi il gradiente non si annulla mai su Z, allora Z è unione di sostegni di
    curve grafico (anche rispetto ad assi diversi), cosicchè gli eventuali punti
    singolari di Z sono da ricercare tra quelli in cui risulta
                               F (x, y) = 0 e      ∇F (x, y) = 0
        L.Freddi                                                         April 16, 2026   9 / 22
Il teorema delle funzioni implicite
Esempio
Sia
                     F (x, y) = x2 + y 2 − 1.




          L.Freddi                              April 16, 2026   10 / 22
Il teorema delle funzioni implicite
Esempio
Sia
                     F (x, y) = x2 + y 2 − 1.
Si ha
                      Fx = 2x,    Fy = 2y




          L.Freddi                              April 16, 2026   10 / 22
Il teorema delle funzioni implicite
Esempio
Sia
                             F (x, y) = x2 + y 2 − 1.
Si ha
                              Fx = 2x,    Fy = 2y
Risulta ∇F (x, y) = 0 solamente per (x, y) = (0, 0) che non è uno zero di F .




          L.Freddi                                             April 16, 2026    10 / 22
Il teorema delle funzioni implicite
Esempio
Sia
                             F (x, y) = x2 + y 2 − 1.
Si ha
                              Fx = 2x,    Fy = 2y
Risulta ∇F (x, y) = 0 solamente per (x, y) = (0, 0) che non è uno zero di F .
Allora il luogo degli zeri di F è sostegno di una curva regolare.




          L.Freddi                                             April 16, 2026    10 / 22
Il teorema delle funzioni implicite
Esempio
Se invece si considera la funzione

                            F (x, y) = y 2 (y + 1) − x2




          L.Freddi                                        April 16, 2026   11 / 22
Il teorema delle funzioni implicite
Esempio
Se invece si considera la funzione

                            F (x, y) = y 2 (y + 1) − x2
allora si ha
                          Fx = −2x,     Fy = 3y 2 + 2y.




          L.Freddi                                        April 16, 2026   11 / 22
Il teorema delle funzioni implicite
Esempio
Se invece si considera la funzione

                             F (x, y) = y 2 (y + 1) − x2
allora si ha
                           Fx = −2x,      Fy = 3y 2 + 2y.
 Il gradiente si annulla nei punti (0, 0) e (0, −2/3) di cui solamente il primo è zero
di F .




          L.Freddi                                                 April 16, 2026   11 / 22
Il teorema delle funzioni implicite
Esempio
Se invece si considera la funzione

                             F (x, y) = y 2 (y + 1) − x2
allora si ha
                           Fx = −2x,      Fy = 3y 2 + 2y.
 Il gradiente si annulla nei punti (0, 0) e (0, −2/3) di cui solamente il primo è zero
di F . L’unico punto singolare di Z può essere l’origine.




          L.Freddi                                                 April 16, 2026   11 / 22
Il teorema delle funzioni implicite
Esempio
Se invece si considera la funzione

                             F (x, y) = y 2 (y + 1) − x2
allora si ha
                           Fx = −2x,      Fy = 3y 2 + 2y.
 Il gradiente si annulla nei punti (0, 0) e (0, −2/3) di cui solamente il primo è zero
di F . L’unico punto singolare di Z può essere l’origine.




          L.Freddi                                                 April 16, 2026   11 / 22
Il teorema delle funzioni implicite
Osservazione
La circostanza che il gradiente si annulli in uno zero di F è solo una condizione
necessaria affinchè questo punto sia singolare, ma non sufficiente.




         L.Freddi                                                April 16, 2026   12 / 22
Il teorema delle funzioni implicite
Osservazione
La circostanza che il gradiente si annulli in uno zero di F è solo una condizione
necessaria affinchè questo punto sia singolare, ma non sufficiente. Infatti il luogo
degli zeri della funzione
                             F (x, y) = (x2 + y 2 − 1)2
è il cerchio unitario che è sostegno di una curva chiusa, semplice e regolare.




         L.Freddi                                                 April 16, 2026   12 / 22
Il teorema delle funzioni implicite
Osservazione
La circostanza che il gradiente si annulli in uno zero di F è solo una condizione
necessaria affinchè questo punto sia singolare, ma non sufficiente. Infatti il luogo
degli zeri della funzione
                             F (x, y) = (x2 + y 2 − 1)2
è il cerchio unitario che è sostegno di una curva chiusa, semplice e regolare.
D’altra parte si ha

                    Fx = 4(x2 + y 2 − 1)x,   Fy = 4(x2 + y 2 − 1)y

e quindi il gradiente si annulla addirittura in ogni punto (x, y) tale che
F (x, y) = 0.




         L.Freddi                                                 April 16, 2026   12 / 22
Esercizio
Esercizio
Dire per quali α > 0 l’eguaglianza

                        sen(y 2 − αxy − x2 y + αx3 ) = 0

definisce implicitamente una funzione y = y(x) oppure x = x(y) in un intorno
dell’origine.




         L.Freddi                                            April 16, 2026    13 / 22
Esercizio
Esercizio
Dire per quali α > 0 l’eguaglianza

                         sen(y 2 − αxy − x2 y + αx3 ) = 0

definisce implicitamente una funzione y = y(x) oppure x = x(y) in un intorno
dell’origine.

Anzitutto osserviamo che in un intorno dell’origine l’equazione equivale a
                            y 2 − αxy − x2 y + αx3 = 0
e le derivate parziali risultano entrambe nulle per ogni valore di α.




         L.Freddi                                                April 16, 2026   13 / 22
Esercizio
Esercizio
Dire per quali α > 0 l’eguaglianza

                         sen(y 2 − αxy − x2 y + αx3 ) = 0

definisce implicitamente una funzione y = y(x) oppure x = x(y) in un intorno
dell’origine.

Anzitutto osserviamo che in un intorno dell’origine l’equazione equivale a
                           y 2 − αxy − x2 y + αx3 = 0
e le derivate parziali risultano entrambe nulle per ogni valore di α.
Quindi l’uguaglianza non definisce implicitamente alcuna funzione y = y(x)
oppure x = x(y) in un intorno dell’origine. Cosa succede nell’origine?




         L.Freddi                                              April 16, 2026   13 / 22
Esercizio
Esercizio
Dire per quali α > 0 l’eguaglianza

                         sen(y 2 − αxy − x2 y + αx3 ) = 0

definisce implicitamente una funzione y = y(x) oppure x = x(y) in un intorno
dell’origine.

Anzitutto osserviamo che in un intorno dell’origine l’equazione equivale a
                            y 2 − αxy − x2 y + αx3 = 0
e le derivate parziali risultano entrambe nulle per ogni valore di α.
Quindi l’uguaglianza non definisce implicitamente alcuna funzione y = y(x)
oppure x = x(y) in un intorno dell’origine. Cosa succede nell’origine?
Lo si scopre osservando che l’equazione si puó scrivere nella forma
                               (y − αx)(y − x2 ) = 0
e disegnando il luogo degli zeri.

         L.Freddi                                              April 16, 2026   13 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .




         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3




         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3
     una ipersuperficie (dimensione n − 1) in Rn




         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3
     una ipersuperficie (dimensione n − 1) in Rn
La dimensione n dello spazio ambiente va specificata prima di tutto il resto.




         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3
     una ipersuperficie (dimensione n − 1) in Rn
La dimensione n dello spazio ambiente va specificata prima di tutto il resto.
Se F dipende da più variabili,
     F (x, y, z) = 0




         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3
     una ipersuperficie (dimensione n − 1) in Rn
La dimensione n dello spazio ambiente va specificata prima di tutto il resto.
Se F dipende da più variabili,
     F (x, y, z) = 0 7→ una superficie (dimensione 2) in R3 (es. z = f (x, y))




         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3
     una ipersuperficie (dimensione n − 1) in Rn
La dimensione n dello spazio ambiente va specificata prima di tutto il resto.
Se F dipende da più variabili,
     F (x, y, z) = 0 7→ una superficie (dimensione 2) in R3 (es. z = f (x, y))
     F (x, y, z, w) = 0




         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3
     una ipersuperficie (dimensione n − 1) in Rn
La dimensione n dello spazio ambiente va specificata prima di tutto il resto.
Se F dipende da più variabili,
     F (x, y, z) = 0 7→ una superficie (dimensione 2) in R3 (es. z = f (x, y))
     F (x, y, z, w) = 0 7→ una ipersuperficie (dimensione 3) in R4 (es.
     w = f (x, y, z))




         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3
     una ipersuperficie (dimensione n − 1) in Rn
La dimensione n dello spazio ambiente va specificata prima di tutto il resto.
Se F dipende da più variabili,
     F (x, y, z) = 0 7→ una superficie (dimensione 2) in R3 (es. z = f (x, y))
     F (x, y, z, w) = 0 7→ una ipersuperficie (dimensione 3) in R4 (es.
     w = f (x, y, z))
     F (x1 , x2 , ..., xn ) = 0



         L.Freddi                                                   April 16, 2026   14 / 22
Funzioni implicite di più variabili
Il teorema del Dini fornisce una condizione sufficiente affinché
                                    F (x, y) = 0
rappresenti una curva localmente grafico di una funzione (dimensione 1) in R2
(es. y − x = 0) .
Ma (attenzione!) perché la stessa equazione potrebbe anche rappresentare:
     una superficie (dimensione 2) in R3
     una ipersuperficie (dimensione n − 1) in Rn
La dimensione n dello spazio ambiente va specificata prima di tutto il resto.
Se F dipende da più variabili,
     F (x, y, z) = 0 7→ una superficie (dimensione 2) in R3 (es. z = f (x, y))
     F (x, y, z, w) = 0 7→ una ipersuperficie (dimensione 3) in R4 (es.
     w = f (x, y, z))
     F (x1 , x2 , ..., xn ) = 0 7→ una ipersuperficie (dimensione n − 1) in Rn (es.
     xn = f (x1 , x2 , ..., xn−1 ))
La dimensione n viene sempre diminuita di 1 (una equazione)
         L.Freddi                                                   April 16, 2026    14 / 22
Funzioni implicite di più variabili
Se F ha più di una componente
                             (
                                 F1 (x, y, z) = 0
                                 F2 (x, y, z) = 0
essa potrebbe rappresentare,




         L.Freddi                                   April 16, 2026   15 / 22
Funzioni implicite di più variabili
Se F ha più di una componente
                             (
                                 F1 (x, y, z) = 0
                                 F2 (x, y, z) = 0
essa potrebbe rappresentare, in R3 ,




         L.Freddi                                   April 16, 2026   15 / 22
Funzioni implicite di più variabili
Se F ha più di una componente
                             (
                                   F1 (x, y, z) = 0
                                   F2 (x, y, z) = 0
essa potrebbe rappresentare, in R3 , l’intersezione tra due superfici, cioè




         L.Freddi                                                  April 16, 2026   15 / 22
Funzioni implicite di più variabili
Se F ha più di una componente
                             (
                                   F1 (x, y, z) = 0
                                   F2 (x, y, z) = 0
essa potrebbe rappresentare, in R3 , l’intersezione tra due superfici, cioè
     una curva (dimensione 1) in R3




         L.Freddi                                                  April 16, 2026   15 / 22
Funzioni implicite di più variabili
Se F ha più di una componente
                             (
                                   F1 (x, y, z) = 0
                                   F2 (x, y, z) = 0
essa potrebbe rappresentare, in R3 , l’intersezione tra due superfici, cioè
     una curva (dimensione 1) in R3
     una superficie (dimensione 2) in R3




         L.Freddi                                                  April 16, 2026   15 / 22
Funzioni implicite di più variabili
Se F ha più di una componente
                             (
                                   F1 (x, y, z) = 0
                                   F2 (x, y, z) = 0
essa potrebbe rappresentare, in R3 , l’intersezione tra due superfici, cioè
     una curva (dimensione 1) in R3
     una superficie (dimensione 2) in R3
     una varietà (mix di curve e superfici)




         L.Freddi                                                  April 16, 2026   15 / 22
Il teorema del Dini per i sistemi
Consideriamo il caso generale in cui
     n = d + m variabili x1 , . . . , xd , y1 , . . . , ym
     sono legate da m equazioni
                        
                        
                          F1 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                           F2 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        
                        
                                              ...
                           Fm (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        




          L.Freddi                                                       April 16, 2026   16 / 22
Il teorema del Dini per i sistemi
Consideriamo il caso generale in cui
     n = d + m variabili x1 , . . . , xd , y1 , . . . , ym
     sono legate da m equazioni
                        
                        
                          F1 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                           F2 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        
                        
                                              ...
                           Fm (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        

Notiamo che
     m = numero di equazioni (vincoli)




          L.Freddi                                                       April 16, 2026   16 / 22
Il teorema del Dini per i sistemi
Consideriamo il caso generale in cui
     n = d + m variabili x1 , . . . , xd , y1 , . . . , ym
     sono legate da m equazioni
                        
                        
                          F1 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                           F2 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        
                        
                                              ...
                           Fm (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        

Notiamo che
     m = numero di equazioni (vincoli)
     d = numero di variabili in eccesso (rispetto al numero di equazioni)




          L.Freddi                                                       April 16, 2026   16 / 22
Il teorema del Dini per i sistemi
Consideriamo il caso generale in cui
     n = d + m variabili x1 , . . . , xd , y1 , . . . , ym
     sono legate da m equazioni
                        
                        
                          F1 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                           F2 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        
                        
                                              ...
                           Fm (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        

Notiamo che
     m = numero di equazioni (vincoli)
     d = numero di variabili in eccesso (rispetto al numero di equazioni)
Indicando con
            x := (x1 , . . . , xd ),   y := (y1 , . . . , ym ),   F := (F1 , . . . , Fm )
il sistema si scrive nella forma più concisa
                                           F (x, y) = 0.

          L.Freddi                                                             April 16, 2026   16 / 22
Il teorema del Dini per i sistemi
Consideriamo il caso generale in cui
     n = d + m variabili x1 , . . . , xd , y1 , . . . , ym
     sono legate da m equazioni
                        
                        
                          F1 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                           F2 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        
                                                                                                 (5)
                        
                                              ...
                           Fm (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        

Poniamo poi
                                                                    
                 ∂F         ∂Fi                       ∂F         ∂Fi
                    =                             ,      =
                 ∂x         ∂xj       i=1,...m        ∂y         ∂yh       i=1,...m
                                      j=1,...,d                            h=1,...,m




          L.Freddi                                                              April 16, 2026   17 / 22
Il teorema del Dini per i sistemi
Consideriamo il caso generale in cui
     n = d + m variabili x1 , . . . , xd , y1 , . . . , ym
     sono legate da m equazioni
                        
                        
                          F1 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                           F2 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        
                                                                                                   (5)
                        
                                              ...
                           Fm (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        

Poniamo poi
                                                                      
                 ∂F           ∂Fi                       ∂F         ∂Fi
                    =                               ,      =
                 ∂x           ∂xj       i=1,...m        ∂y         ∂yh       i=1,...m
                                        j=1,...,d                            h=1,...,m
                     rettangolare                       quadrata




          L.Freddi                                                                April 16, 2026   17 / 22
Il teorema del Dini per i sistemi
Consideriamo il caso generale in cui
     n = d + m variabili x1 , . . . , xd , y1 , . . . , ym
     sono legate da m equazioni
                        
                        
                          F1 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                           F2 (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        
                                                                                                   (5)
                        
                                              ...
                           Fm (x1 , . . . , xd , y1 , . . . , ym ) = 0
                        

Poniamo poi
                                                                      
                 ∂F           ∂Fi                       ∂F         ∂Fi
                    =                               ,      =
                 ∂x           ∂xj       i=1,...m        ∂y         ∂yh       i=1,...m
                                        j=1,...,d                            h=1,...,m
                     rettangolare                       quadrata

Con queste notazioni il teorema delle funzioni implicite si enuncia formalmente
come nel caso di due sole variabili.



          L.Freddi                                                                April 16, 2026   17 / 22
Il teorema del Dini per i sistemi
Teorema (del Dini in più variabili)
Sia Ω un aperto di Rd × Rm ed F : Ω → Rm una funzione di classe C 1 . Sia
(x0 , y0 ) ∈ Ω tale che

                                                 ∂F           
                     F (x0 , y0 ) = 0 e    det      (x0 , y0 ) ̸= 0.
                                                 ∂y

Allora esistono un intorno U di x0 in Rd ed un intorno V di y0 in Rm tali che

                      ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.

Inoltre la funzione x 7→ f (x) è di classe C 1 (U ) e si ha
                                                −1
                                ∂F                     ∂F
                     ∇f (x) = −    (x, f (x))             (x, f (x)).
                                ∂y                     ∂x




          L.Freddi                                                      April 16, 2026   18 / 22
Il teorema del Dini per i sistemi
Teorema (del Dini in più variabili)
Sia Ω un aperto di Rd × Rm ed F : Ω → Rm una funzione di classe C 1 . Sia
(x0 , y0 ) ∈ Ω tale che

                                                 ∂F           
                     F (x0 , y0 ) = 0 e    det      (x0 , y0 ) ̸= 0.
                                                 ∂y

Allora esistono un intorno U di x0 in Rd ed un intorno V di y0 in Rm tali che

                      ∀ x ∈ U ∃! y =: f (x) ∈ V : F (x, y) = 0.

Inoltre la funzione x 7→ f (x) è di classe C 1 (U ) e si ha
                                                −1
                                ∂F                     ∂F
                     ∇f (x) = −    (x, f (x))             (x, f (x)).
                                ∂y                     ∂x

Ricordiamo che ∂F
               ∂y (x0 , y0 ) è una matrice quadrata di ordine n



          L.Freddi                                                      April 16, 2026   18 / 22
Il teorema del Dini per i sistemi
Osserviamo che
    la condizione affinché F = 0 sia localmente grafico di una funzione C 1 è che




        L.Freddi                                               April 16, 2026   19 / 22
Il teorema del Dini per i sistemi
Osserviamo che
    la condizione affinché F = 0 sia localmente grafico di una funzione C 1 è che
    ∇F contenga almeno un minore di ordine m con det ̸= 0,




        L.Freddi                                               April 16, 2026   19 / 22
Il teorema del Dini per i sistemi
Osserviamo che
    la condizione affinché F = 0 sia localmente grafico di una funzione C 1 è che
    ∇F contenga almeno un minore di ordine m con det ̸= 0, cioè
                   rango(∇F (x0 , y0 )) = m   (condizione di regolarità)
    cioè che la matrice jacobiana di F abbia rango massimo (m)




        L.Freddi                                                  April 16, 2026   19 / 22
Il teorema del Dini per i sistemi
Osserviamo che
    la condizione affinché F = 0 sia localmente grafico di una funzione C 1 è che
    ∇F contenga almeno un minore di ordine m con det ̸= 0, cioè
                   rango(∇F (x0 , y0 )) = m    (condizione di regolarità)
    cioè che la matrice jacobiana di F abbia rango massimo (m)
    se tutti i punti sono regolari, cioè se
                         rango(∇F ) = m su tutti gli zeri di F
    allora Z è detto una varietà regolare di dimensione d immersa in Rn .




        L.Freddi                                                   April 16, 2026   19 / 22
Il teorema del Dini per i sistemi
Osserviamo che
    la condizione affinché F = 0 sia localmente grafico di una funzione C 1 è che
    ∇F contenga almeno un minore di ordine m con det ̸= 0, cioè
                   rango(∇F (x0 , y0 )) = m    (condizione di regolarità)
    cioè che la matrice jacobiana di F abbia rango massimo (m)
    se tutti i punti sono regolari, cioè se
                         rango(∇F ) = m su tutti gli zeri di F
    allora Z è detto una varietà regolare di dimensione d immersa in Rn . Casi
    particolari:
       ▶ se d = n − 1 (quindi m = 1) sono dette ipersuperfici di Rn




        L.Freddi                                                   April 16, 2026   19 / 22
Il teorema del Dini per i sistemi
Osserviamo che
    la condizione affinché F = 0 sia localmente grafico di una funzione C 1 è che
    ∇F contenga almeno un minore di ordine m con det ̸= 0, cioè
                   rango(∇F (x0 , y0 )) = m    (condizione di regolarità)
    cioè che la matrice jacobiana di F abbia rango massimo (m)
    se tutti i punti sono regolari, cioè se
                         rango(∇F ) = m su tutti gli zeri di F
    allora Z è detto una varietà regolare di dimensione d immersa in Rn . Casi
    particolari:
       ▶ se d = n − 1 (quindi m = 1) sono dette ipersuperfici di Rn
       ▶ se n = 3 e d = 2 (quindi m = 1) si tratta di ipersuperfici di R3 , anche

          dette semplicemente superfici




        L.Freddi                                                   April 16, 2026   19 / 22
Il teorema del Dini per i sistemi
Osserviamo che
    la condizione affinché F = 0 sia localmente grafico di una funzione C 1 è che
    ∇F contenga almeno un minore di ordine m con det ̸= 0, cioè
                   rango(∇F (x0 , y0 )) = m    (condizione di regolarità)
    cioè che la matrice jacobiana di F abbia rango massimo (m)
    se tutti i punti sono regolari, cioè se
                         rango(∇F ) = m su tutti gli zeri di F
    allora Z è detto una varietà regolare di dimensione d immersa in Rn . Casi
    particolari:
       ▶ se d = n − 1 (quindi m = 1) sono dette ipersuperfici di Rn
       ▶ se n = 3 e d = 2 (quindi m = 1) si tratta di ipersuperfici di R3 , anche

          dette semplicemente superfici
       ▶ se d = 1 (quindi m = n − 1) si tratta di curve di Rn




        L.Freddi                                                   April 16, 2026   19 / 22
Il teorema del Dini per i sistemi
Osserviamo che
    la condizione affinché F = 0 sia localmente grafico di una funzione C 1 è che
    ∇F contenga almeno un minore di ordine m con det ̸= 0, cioè
                   rango(∇F (x0 , y0 )) = m    (condizione di regolarità)
    cioè che la matrice jacobiana di F abbia rango massimo (m)
    se tutti i punti sono regolari, cioè se
                         rango(∇F ) = m su tutti gli zeri di F
    allora Z è detto una varietà regolare di dimensione d immersa in Rn . Casi
    particolari:
       ▶ se d = n − 1 (quindi m = 1) sono dette ipersuperfici di Rn
       ▶ se n = 3 e d = 2 (quindi m = 1) si tratta di ipersuperfici di R3 , anche

          dette semplicemente superfici
       ▶ se d = 1 (quindi m = n − 1) si tratta di curve di Rn

       ▶ le curve di R2 corrispondono a n = 2 e d = n − 1 (quindi m = 1)

          quindi sono ipersuperfici di R2

        L.Freddi                                                   April 16, 2026   19 / 22
Esempio
Data l’equazione
                                 F (x, y, z) = 0
           1
con F ∈ C , si ha m = 1 e intorno ad uno zero di F si possono verificare i casi:
     rango∇F = 1 = m (caso regolare)

     rango∇F = 0 < m (caso singolare)




         L.Freddi                                             April 16, 2026   20 / 22
Esempio
Data l’equazione
                                 F (x, y, z) = 0
           1
con F ∈ C , si ha m = 1 e intorno ad uno zero di F si possono verificare i casi:
     rango∇F = 1 = m (caso regolare) =⇒ d = n − 1 =⇒ ipersuperficie
     (superficie se n = 3)
     rango∇F = 0 < m (caso singolare)




         L.Freddi                                             April 16, 2026   20 / 22
Esempio
Data l’equazione
                                 F (x, y, z) = 0
           1
con F ∈ C , si ha m = 1 e intorno ad uno zero di F si possono verificare i casi:
     rango∇F = 1 = m (caso regolare) =⇒ d = n − 1 =⇒ ipersuperficie
     (superficie se n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha




         L.Freddi                                             April 16, 2026   20 / 22
Esempio
Data l’equazione
                                 F (x, y, z) = 0
           1
con F ∈ C , si ha m = 1 e intorno ad uno zero di F si possono verificare i casi:
     rango∇F = 1 = m (caso regolare) =⇒ d = n − 1 =⇒ ipersuperficie
     (superficie se n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha
       ▶ C = 0 =⇒ l’insieme degli zeri di F è tutto Rn




         L.Freddi                                             April 16, 2026   20 / 22
Esempio
Data l’equazione
                                 F (x, y, z) = 0
           1
con F ∈ C , si ha m = 1 e intorno ad uno zero di F si possono verificare i casi:
     rango∇F = 1 = m (caso regolare) =⇒ d = n − 1 =⇒ ipersuperficie
     (superficie se n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha
       ▶ C = 0 =⇒ l’insieme degli zeri di F è tutto Rn
       ▶ C ̸= 0 =⇒ l’insieme degli zeri di F è ∅




         L.Freddi                                             April 16, 2026   20 / 22
Esempio
Data l’equazione
                                 F (x, y, z) = 0
           1
con F ∈ C , si ha m = 1 e intorno ad uno zero di F si possono verificare i casi:
     rango∇F = 1 = m (caso regolare) =⇒ d = n − 1 =⇒ ipersuperficie
     (superficie se n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha
       ▶ C = 0 =⇒ l’insieme degli zeri di F è tutto Rn
       ▶ C ̸= 0 =⇒ l’insieme degli zeri di F è ∅

Se quindi, ad esempio,         ∂F
                                  (x0 , y0 , z0 ) ̸= 0
                               ∂z




         L.Freddi                                             April 16, 2026   20 / 22
Esempio
Data l’equazione
                                      F (x, y, z) = 0
            1
con F ∈ C , si ha m = 1 e intorno ad uno zero di F si possono verificare i casi:
     rango∇F = 1 = m (caso regolare) =⇒ d = n − 1 =⇒ ipersuperficie
     (superficie se n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha
       ▶ C = 0 =⇒ l’insieme degli zeri di F è tutto Rn
       ▶ C ̸= 0 =⇒ l’insieme degli zeri di F è ∅

Se quindi, ad esempio,           ∂F
                                     (x0 , y0 , z0 ) ̸= 0
                                 ∂z
 allora m = 1 e l’insieme degli zeri si può scrivere in un intorno di (x0 , y0 , z0 )
nella forma cartesiana
                                     z = f (x, y)
e il grafico è una ipersuperficie;



          L.Freddi                                                    April 16, 2026     20 / 22
Esempio
Data l’equazione
                                        F (x, y, z) = 0
            1
con F ∈ C , si ha m = 1 e intorno ad uno zero di F si possono verificare i casi:
     rango∇F = 1 = m (caso regolare) =⇒ d = n − 1 =⇒ ipersuperficie
     (superficie se n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha
       ▶ C = 0 =⇒ l’insieme degli zeri di F è tutto Rn
       ▶ C ̸= 0 =⇒ l’insieme degli zeri di F è ∅

Se quindi, ad esempio,           ∂F
                                     (x0 , y0 , z0 ) ̸= 0
                                 ∂z
 allora m = 1 e l’insieme degli zeri si può scrivere in un intorno di (x0 , y0 , z0 )
nella forma cartesiana
                                     z = f (x, y)
e il grafico è una ipersuperficie; si ha inoltre (verificare per esercizio)
                          Fx (x, y, f (x, y))                     Fy (x, y, f (x, y))
          fx (x, y) = −                       ,   fy (x, y) = −                       .
                          Fz (x, y, f (x, y))                     Fz (x, y, f (x, y))
          L.Freddi                                                         April 16, 2026   20 / 22
Esempio
Dato il sistema                 
                                    F1 (x, y, z) = 0
                                    F2 (x, y, z) = 0
con F1 e F2 funzioni C 1 , si ha n=3, m = 2, d=1.
Intorno ad uno zero si possono verificare i casi seguenti:
     rango∇F = 2 = m (caso regolare)
     rango∇F = 1 < m (caso singolare)

     rango∇F = 0 < m (caso singolare)




         L.Freddi                                            April 16, 2026   21 / 22
Esempio
Dato il sistema                 
                                    F1 (x, y, z) = 0
                                    F2 (x, y, z) = 0
con F1 e F2 funzioni C 1 , si ha n=3, m = 2, d=1.
Intorno ad uno zero si possono verificare i casi seguenti:
     rango∇F = 2 = m (caso regolare) =⇒ curva perché d=1
     rango∇F = 1 < m (caso singolare)

     rango∇F = 0 < m (caso singolare)




         L.Freddi                                            April 16, 2026   21 / 22
Esempio
Dato il sistema                 
                                    F1 (x, y, z) = 0
                                    F2 (x, y, z) = 0
con F1 e F2 funzioni C 1 , si ha n=3, m = 2, d=1.
Intorno ad uno zero si possono verificare i casi seguenti:
     rango∇F = 2 = m (caso regolare) =⇒ curva perché d=1
     rango∇F = 1 < m (caso singolare) =⇒ le due equazioni sono equivalenti
     =⇒ ipersuperficie (=superficie perché n = 3)
     rango∇F = 0 < m (caso singolare)




         L.Freddi                                            April 16, 2026   21 / 22
Esempio
Dato il sistema                 
                                    F1 (x, y, z) = 0
                                    F2 (x, y, z) = 0
con F1 e F2 funzioni C 1 , si ha n=3, m = 2, d=1.
Intorno ad uno zero si possono verificare i casi seguenti:
     rango∇F = 2 = m (caso regolare) =⇒ curva perché d=1
     rango∇F = 1 < m (caso singolare) =⇒ le due equazioni sono equivalenti
     =⇒ ipersuperficie (=superficie perché n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha




         L.Freddi                                            April 16, 2026   21 / 22
Esempio
Dato il sistema                 
                                    F1 (x, y, z) = 0
                                    F2 (x, y, z) = 0
con F1 e F2 funzioni C 1 , si ha n=3, m = 2, d=1.
Intorno ad uno zero si possono verificare i casi seguenti:
     rango∇F = 2 = m (caso regolare) =⇒ curva perché d=1
     rango∇F = 1 < m (caso singolare) =⇒ le due equazioni sono equivalenti
     =⇒ ipersuperficie (=superficie perché n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha
       ▶ C = 0 =⇒ tutto Rn




         L.Freddi                                            April 16, 2026   21 / 22
Esempio
Dato il sistema                 
                                    F1 (x, y, z) = 0
                                    F2 (x, y, z) = 0
con F1 e F2 funzioni C 1 , si ha n=3, m = 2, d=1.
Intorno ad uno zero si possono verificare i casi seguenti:
     rango∇F = 2 = m (caso regolare) =⇒ curva perché d=1
     rango∇F = 1 < m (caso singolare) =⇒ le due equazioni sono equivalenti
     =⇒ ipersuperficie (=superficie perché n = 3)
     rango∇F = 0 < m (caso singolare) =⇒ F = C = costante e si ha
       ▶ C = 0 =⇒ tutto Rn
       ▶ C ̸= 0 =⇒ ∅




         L.Freddi                                            April 16, 2026   21 / 22
Esempio
Se quindi, ad esempio,
                            ∂F1                     ∂F1                     
                                   (x0 , y0 , z0 )         (x0 , y0 , z0 )
                             ∂x                      ∂y                     
                                                                              ̸= 0.
                     det 
                            ∂F2                     ∂F2                     
                                   (x0 , y0 , z0 )         (x0 , y0 , z0 )
                             ∂x                      ∂y




         L.Freddi                                                                      April 16, 2026   22 / 22
Esempio
Se quindi, ad esempio,
                             ∂F1                     ∂F1                     
                                    (x0 , y0 , z0 )         (x0 , y0 , z0 )
                              ∂x                      ∂y                     
                                                                               ̸= 0.
                      det 
                             ∂F2                     ∂F2                     
                                    (x0 , y0 , z0 )         (x0 , y0 , z0 )
                              ∂x                      ∂y

 allora l’insieme degli zeri è una curva in R3 di equazioni parametriche con
parametro t                          
                                      x = f1 (t)
                                        y = f2 (t)
                                        z=t
                                     




         L.Freddi                                                                       April 16, 2026   22 / 22
Esempio
Se quindi, ad esempio,
                                   ∂F1                      ∂F1                     
                                          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                                    ∂x                       ∂y                     
                                                                                      ̸= 0.
                         det 
                                   ∂F2                      ∂F2                     
                                          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                                     ∂x                       ∂y

 allora l’insieme degli zeri è una curva in R3 di equazioni parametriche con
parametro t                          
                                      x = f1 (t)
                                        y = f2 (t)
                                        z=t
                                     
Se invece               ∂F1                      ∂F1                     ∂F1
                               (x0 , y0 , z0 )          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                         ∂x                       ∂y                       ∂z                     
               rango                                                                               = 1.
                        ∂F2                      ∂F2                      ∂F2                     
                               (x0 , y0 , z0 )          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                         ∂x                        ∂y                       ∂z




         L.Freddi                                                                                  April 16, 2026   22 / 22
Esempio
Se quindi, ad esempio,
                                   ∂F1                      ∂F1                     
                                          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                                    ∂x                       ∂y                     
                                                                                      ̸= 0.
                         det 
                                   ∂F2                      ∂F2                     
                                          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                                     ∂x                       ∂y

 allora l’insieme degli zeri è una curva in R3 di equazioni parametriche con
parametro t                          
                                      x = f1 (t)
                                        y = f2 (t)
                                        z=t
                                     
Se invece               ∂F1                      ∂F1                     ∂F1
                               (x0 , y0 , z0 )          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                         ∂x                       ∂y                       ∂z                     
               rango                                                                               = 1.
                        ∂F2                      ∂F2                      ∂F2                     
                               (x0 , y0 , z0 )          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                         ∂x                        ∂y                       ∂z

e, ad esempio,
                                           ∂F1
                                               (x0 , y0 , z0 ) ̸= 0
                                           ∂z



         L.Freddi                                                                                  April 16, 2026   22 / 22
Esempio
Se quindi, ad esempio,
                                   ∂F1                      ∂F1                     
                                          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                                    ∂x                       ∂y                     
                                                                                      ̸= 0.
                         det 
                                   ∂F2                      ∂F2                     
                                          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                                     ∂x                       ∂y

 allora l’insieme degli zeri è una curva in R3 di equazioni parametriche con
parametro t                          
                                      x = f1 (t)
                                        y = f2 (t)
                                        z=t
                                     
Se invece               ∂F1                      ∂F1                     ∂F1
                               (x0 , y0 , z0 )          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                         ∂x                       ∂y                       ∂z                     
               rango                                                                               = 1.
                        ∂F2                      ∂F2                      ∂F2                     
                               (x0 , y0 , z0 )          (x0 , y0 , z0 )          (x0 , y0 , z0 )
                         ∂x                        ∂y                       ∂z

e, ad esempio,
                                   ∂F1
                                        (x0 , y0 , z0 ) ̸= 0
                                    ∂z
 allora l’insieme degli zeri si può scrivere in un intorno di (x0 , y0 , z0 ) nella forma
cartesiana
                                        z = f (x, y)
e il grafico  è una ipersuperficie.
           L.Freddi                                                                                April 16, 2026   22 / 22
Esercizio
Esercizio
Studiare il luogo degli zeri della funzione

                           F (x, y, z) = x2 ez + zey + y 2




         L.Freddi                                            April 16, 2026   23 / 22
Esercizio
Esercizio
Studiare il luogo degli zeri della funzione

                           F (x, y, z) = x2 ez + zey + y 2

Siccome Fz = x2 ez + ey > 0 allora il luogo degli zeri di F è grafico di una
funzione
                                  z = f (x, y)




         L.Freddi                                                April 16, 2026   23 / 22
Esercizio
Esercizio
Studiare il luogo degli zeri della funzione

                           F (x, y, z) = x2 ez + zey + y 2

Siccome Fz = x2 ez + ey > 0 allora il luogo degli zeri di F è grafico di una
funzione
                                  z = f (x, y)




         L.Freddi                                                April 16, 2026   23 / 22
