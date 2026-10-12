---
fonte: "140709soluzione.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

A)[10] Per il sistema dinamico non lineare

                                  ẋ1     = −α(x1 − x2 )2 − β(x1 − x2 )
                                  ẋ2     = α2 (x1 − x2 )2 − βx2 + u

in cui α > 0 e β > 0
    A.1)[4] Si determinino tutti i punti di equilibrio in funzione dell’ingresso u
    A.1) R. Eguagliando a zero i membri destri dell’equazione dinamica del sistema,
si ottiene
                               −α(x̄1 − x̄2 )2 − β(x̄1 − x̄2 ) = 0
                                    α2 (x̄1 − x̄2 )2 − β x̄2 + ū = 0
La prima equazione non dipende da ū ed ha le due soluzioni
                                                         
                         (1)   (1)              (2)   (2)
                   (1) x̄1 = x̄2       (2) α x̄1 − x̄2      = −β

La prima delle due, sostituita nella seconda equazione, porge come soluzione

                                                        (1)         (1)      ū
                                            (1)     x̄2 = x̄1 =
                                                                             β
                                                            2
                                                     (2) (2)
Per quanto riguarda la seconda, sostituendo α2 x̄1 − x̄2        = β 2 nella seconda equazione
si ottiene
                                             (2)
                                   β 2 − β x̄2 + ū = 0
e dunque
                                    (2)      ū + β 2               (2)          β   ū + β 2
                            2)     x̄2 =                        x̄1 = −            +
                                                β                                α      β

    A.2)[6] Si valuti la stabilità dei punti trovati.
    A.2) R. Lo Jacobiano J(x1 , x2 ) del sistema dinamico é
                                                                               
                            ∂f        −2α(x̄1 − x̄2 ) − β  2α(x̄1 − x̄2 ) + β
                      J=        =
                            ∂x           2α2 (x̄1 − x̄2 ) −2α2 (x̄1 − x̄2 ) − β

Lo Jacobiano, valutato sulla prima soluzione, diventa
                                                     
                                 (1)  (1)     −β β
                              J(x1 , x2 ) =
                                               0 −β

I cui autovalori sono −β, − β, e dunque tutti i punti di equilibrio con x̄1 = x̄2 risultano
asintoticamente stabili.
   Per quanto rigarda la seconda soluzione conviene sostituire
                                             
                                                  (2)         (2)
                                                                            β
                                                 x̄1 − x̄2              =−
                                                                             α
nello Jacobiano,
                                       β                      β
                                                                                                                
               (2)  (2)         −2α(− α  )−β             2α(− α )+β                                β       −β
            J(x1 , x2 ) =                β                      β                      =
                                  2α2 (− α )            −2α2 (− α )−β                              2αβ   2αβ − β
                                                                                               −
    Il polinomio caratteristico dello Jacobiano è

                  det(sI − J) = (s − β) (s − (2αβ − β)) − 2αβ 2 = s2 − 2αβs − β 2


e ha una radice a parte reale positiva dato che il coefficiente di s2 è positivo e gli altri
due negativi e dunque tutti i punti di equilibrio trovati sono instabili.
