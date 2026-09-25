---
fonte: "191105_intermedia_soluzioni_backup.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

MeC, Prima prova intermedia del 05/11/19
                                                            UNO

A)[8] Si consideri il sistema dinamico a tempo continuo

                                             ẋ1     = −σx1 + σx2
                                             ẋ2     = −2x2 + u
                                               y     = x1

A.1)[3] Si calcoli l’esponenziale eAt per σ 6= 2.
   R: Poichè la matrice è diagonale, gli autovalori sono λ1 = −2 e λ2 = −σ. La matrice
degli autovettori e la sua inversa sono
                                 σ                              
                                   σ−2  1           −1     0   1
                           V =                    V    =        σ
                                    1   0                  1 − σ−2

e dunque

                                           e−σt                                       e−σt    σ
                                                                                                   e−2t − e−σt
                                                                                                               
                At      Λt   −1                         0             −1                     σ−2
            e        =Ve V        =V                              V        =
                                            0       e−2t                               0            e−2t

A.2)[2] Si calcoli la trasformata di Laplace della risposta impulsiva. R.
                                                                   σ
                                            Y (s) =
                                                            (s + σ) (s + 2)

A.3)[3] Si studino i punti di equilibrio del sistema al variare di ū e se ne discuta la stabilità in
funzione del parametro σ ∈ IR.
   R. La matrice è invertibile per σ 6= 0 e l’espressione dei punti di equilibrio è
                                                             1       1
                                                                           T
                                                  x̄ =        2       2         ū

Per σ = 0 il punto di equilibrio è
                                                                          1
                                                                                  T
                                             x̄ =        libero            2 ū

Dato che il sistema è lineare, la stabilità di qualsiasi punto dipende esclusivamente
dagli autovalori del sistema. Per σ > 0 i punti di equilibrio sono asintoticamente
stabile, per σ = 0 sono stabili, ma non asintoticamente, per σ < 0 sono instabili.

B.1)[4] Si calcoli la trasformata di Laplace di y(t) = e2t δ−1 (t − 3) + 4e−βt cos(αt)
   R.
                                                                                          e6 −3s        s+β
        y(t) = e6 e2(t−3) δ−1 (t − 3) + 4e−βt cos(αt) → Y (s) =                              e   +4
                                                                                         s−2        (s + β)2 + α2

B.2)[3] Si calcoli l’antitrasformata di Y (s) = (s+4)(s+β)
                                                 (s+1)(s+2) .
  R.
                             y(t) = δ(t) + e−t (3β − 3) − e−2t (2β − 4)
             MeC, Prima prova intermedia del 05/11/19
                                                  DUE

   A)[8] Si consideri il sistema dinamico a tempo continuo

                                         ẋ1    = −2x1 + u
                                         ẋ2    = σx2 − σx1
                                           y    = x1 + x2

A.1)[3] Si calcoli l’esponenziale eAt per σ 6= −2.
   R:
                                                                e−2t
                                                                                   
                                                                               0
                           eAt = V eΛt V −1 =          σ
                                                               e−2t − eσt
                                                                          
                                                      σ+2                     eσt

   A.2)[2] Si calcoli la trasformata di Laplace della risposta impulsiva.
   R.
                                   1           σ                s − 2σ
                         Y (s) =      −                  =
                                 s + 2 (s − σ) (s + 2)      (s − σ) (s + 2)

A.3)[3] Si studino i punti di equilibrio del sistema al variare di ū e se ne discuta la stabilità in
funzione del parametro σ ∈ IR.
   R. La matrice è invertibile per σ 6= 0 e il punto di equilibrio è
                                                  1       1
                                                               T
                                          x̄ =        2    2        ū

Per σ = 0 il punto di equilibrio è
                                                ū                  T
                                        x̄ =     2        libero

σ > 0 instabile, σ = 0 stabile, σ < 0 stabile
   B.1) [4] Si calcoli la trasformata di Laplace di y(t) = eαt δ−1 (t − 2) + 4e−t cos(βt).
   R.
                                         e2α −2s         (s + 1)
                                Y (s) =      e    +4         2
                                        s−α           (s + 1) + β 2

   B.2) [3] Si calcoli l’antitrasformata di Y (s) = (s+α)(s+1)
                                                    (s+3)(s+4) .
   R.
                           Y (s) = δ(t) − e−3t (2 α − 6) + e−4t (3α − 12)
             MeC, Prima prova intermedia del 05/11/19
                                                TRE

A)[8] Si consideri il sistema dinamico a tempo continuo

                                        ẋ1   = −2x1 + σx2
                                        ẋ2   = −σx2 + u
                                          y   = x1 − x2

   A.1)[3] Si calcoli l’esponenziale eAt per σ 6= 2.
   R:
                                       −2t      σ
                                                     e−2t − e−σt
                                                                  
                                At      e       σ−2
                               e =
                                          0           e−σt

   A.2)[2] Si calcoli la trasformata di Laplace della risposta impulsiva.
   R. La trasformata di Laplace della risposta impulsiva è

                                −1                   σ          1      −(s − σ + 2)
            Y (s) = C (sI − A)       B+D =                   −      =
                                              (s + σ) (s + 2) s + σ   (s + σ) (s + 2)

    A.3)[3] Si studino i punti di equilibrio del sistema al variare di ū e se ne discuta la stabilità
in funzione del parametro σ ∈ IR.
    R. La matrice è invertibile per σ 6= 0 e il punto di equilibrio è
                                                 1 
                                            x̄ = 21 ū
                                                    σ

Per σ = 0 la condizione di equilbrio richiede x̄1 = 0 e ū = 0, quindi per ū 6= 0 il sistema
non ammette soluzioni, mentre per ū = 0 il sistema ammette i punti di equilibrio
                                                  
                                               0
                                     x̄ =
                                            libero



   B.1 [4] Si calcoli la trasformata di Laplace di y(t) = et δ−1 (t − α) + 4e−βt sin(2t) per α > 0
               eα −αs            2
   R. Y (s) = s−1 e      + 4 (s+β) 2
                                     +4
                                                      (s+2)
   B.2 [3] Si calcoli l’antitrasformata di Y (s) = (s+1)(s+α) .
               1   −t     α−2 −αt
   R. y(s) = α−1 e + α−1 e
             MeC, Prima prova intermedia del 05/11/19
                                               QUATTRO

A)[8] Si consideri il sistema dinamico a tempo continuo

                                         ẋ1    = −σx1 + u
                                         ẋ2    = σx1 − 2x2
                                           y    = x1 + x2

   A.1)[3] Si calcoli l’esponenziale eAt per σ 6= 2.
   R:

                                                     e−σt
                                                                           
                           At     Λt −1                                0
                          e =Ve V         =          −2t
                                                 σ
                                                         − e−σt      e−2t
                                                                
                                               σ−2 e

   A.2)[2] Si calcoli la trasformata di Laplace della risposta impulsiva.
   R. La trasformata di Laplace della risposta impulsiva è

                                −1               1          σ             s+σ+2
            Y (s) = C (sI − A)       B+D =          +                =
                                               s + σ (s + σ) (s + 2)   (s + σ) (s + 2)

    A.3)[3] Si studino i punti di equilibrio del sistema al variare di ū e se ne discuta la stabilità
in funzione del parametro σ ∈ IR.
    R. La matrice è invertibile per σ 6= 0 e il punto di equilibrio è
                                                 1 
                                            x̄ = σ1 ū
                                                    2

per σ = 0, per ū 6= 0 non ammette punti di equilibrio, per ū = 0 ammette il punto di
equilbrio
                                                
                                          libero
                                   x̄ =            u
                                             0

   B.1 [4] Si calcoli la trasformata di Laplace di y(t) = e−2t δ−1 (t − β) + 4e−αt sin(t) per β > 0
                −2β
   R. Y (s) = es+2 e−βs + 4 (s+α)1
                                   2
                                     +1
                                                      (s+1)
   B.2 [3] Si calcoli l’antitrasformata di Y (s) = (s+β)(s+4) .
   R. y(t) = β−1
             β−4 e
                   −βt    3
                       − β−4 e−4t
                                        ẋ1 = −2x21 + 3u
                                    
   C) [5] Per il sistema dinamico                        si risponda alle seguenti domande corredan-
                                        y = x1
dole con opportuna giustificazione.
C.1)[1] Il sistema è stabile?
C.2)[1] Il sistema è tempo invariante?
C.3)[1] Il sistema è strettamente proprio?
C.4)[1] Il sistema dinamico lineare ottenuto dalla linearizzazione in un punto di equilibrio (x̄, ȳ, ū)
ha sempre dimensione pari a 1?
C.5)[1] Il sistema dinamico lineare ottenuto dalla linearizzazione in un punto di equilibrio descrive
il legame tra ū e x̄ e ȳ?


D)[5] Si risponda, giustificando, alle affermazioni sotto riportate. Il sistema dinamico a un in-
gresso e un’uscita ẋ = Ax + Bu, y = Cx di dimensione 2 è asintoticamente stabile se
D.1)[1] A è diagonalizzabile.
D.2)[1] Gli elementi sulla diagonale sono negativi e i due elementi fuori dalla diagonale sono
discordi.
D.3)[1] Per ogni valore di ū il sistema ammette un solo punto di equilibrio.
D.4)[1] La matrice I − A è invertibile.
D.5)[1] Il punto di equilibrio x̄ associato all’ingresoo ū = 1 : x̄ = −A−1 B è asintoticamente
stabile


E)[5] Il candidato discuta della risposta di evoluzione libera e forzata per sistemi dinamici lineari
tempo invarianti.
