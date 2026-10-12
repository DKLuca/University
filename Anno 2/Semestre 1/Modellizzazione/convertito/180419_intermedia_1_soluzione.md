---
fonte: "180419_intermedia_1_soluzione.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

MeC, Intermedia del 19/04/18
    A)[11] Si consideri il pendolo semplice in figura 1. Il corpo puntiforme di massa M = 1kg
è collegato mediante asta priva di massa di lunghezza L = 1m all’asse di rotazione. Il corpo è
soggetto a una coppia dovuta alla forza di gravità e elastica Fg+el = M g − KL cos(θ), alla coppia
di attrito riportata all’asse di rotazione τattr = −bω, dove ω è la velocità angolare del pendolo, e
alla coppia motrice sull’albero τ .




                                                      τ




                                                                                         Lcos( Θ)
                                                                         L
                                                                                    Κ

                                                                Θ




                                                                                   Mg


                                             Figure 1: Pendolo semplice


  A.1)[4] Si ricavi il modello in forma di stato avente la coppia τ come ingresso e l’angolo della
massa come uscita
  (R) Posto x1 = θ e x2 = ω si ottiene

                            ẋ1     =        x2
                            ẋ2     =        −g sin(x1 ) + K cos(x1 ) sin(x1 ) −bx2 + u
                                                             |     {z       }
                                                                    1
                                                                    2 sin(2x1 )
                             y    = x1


   A.2)[3] Si determino i punti di equilibrio del sistema1 per ū = 0 in funzione di K.
   (R) Poste a zero le derivate, si ricava x̄2 = 0 e

                                          sin(x̄1 ) (−g + K cos(x̄1 )) = 0

le cui soluzioni sono

                       sin(x̄1 ) = 0     =⇒ x̄1 = 0, π    ∀K                                        (1)
                                                        g                 g
            −g + K cos(x̄1 ) = 0         =⇒ cos(x̄1 ) =   =⇒ x̄1 = arccos     per K ≥ g             (2)
                                                        K                  K
A.3)[4] Si studi la stabilità di detti punti al variare di K.
  (R) La matrice di aggiornamento dello stato del sistema linearizzato è

                                                      0                           1
                                                                                    

                                  A=  −g cos(x̄ 1 ) + K cos(2x̄1 )               −b 
                                                         | {z }
                                                                2 cos2 (x̄1 )−1

  1 Si considerino solo i punti con valori delle variabili di stato in [0,   π]




                                                            1
La linearizzazione nei punti di equilibrio (1) è
                                                                                       
                               0      1                 0                            1
                    A0 =                        Aπ =
                           −g + K −b                   g+K                           −b

dunque x̄1 = 0 è asintoticamente stabile se K < g, instabile altrimenti (fatta eccezione
per il caso K = g per il quale la linearizzazione non fornisce risultato), mentre x̄1 = π
è instabile per qualsiasi valore di K.
                                                                    g
    Per quanto riguarda i punti (2) per K > g, dato che cos(x̄1 ) = K , si ha
                                   "                         #
                                             0         1
                            A(2) =      g       g2
                                     −g K + K 2 K 2 − 1  −b

   Il polinomio caratteristico ha entrambi le radici a parte reale negativa se e solo se

                                      g2    g2
                                 −       + 2 − K < 0 =⇒ g < K
                                      K     K
   In conclusione,

   • per K < g, esistono solo i punti di equilibrio x̄1 = 0, π che sono, rispettivamente,
     asintoticamente stabile e instabile.
   • per K > g, i due punti di equilibrio x̄1 = 0, π sono instabili, mentre è asintotica-
                                         g
     mente stabile il punto x̄1 = arccos K


   B)[11] Utilizzando la definizione di matrice esponenziale e la proprietà di commutatività
e(A+B)t = eAt eBt se AB = BA, si dimostri che
                   −1
   • B.1)[2] eAt       = e−At
                At
   • B.2)[2] dedt = AeAt = eAt A
                                      R t Aτ
                                         e dτ = A−1 eAt − I
                                                            
   • B.3)[3] se det(A) 6= 0, allora    0

Si dimostri inoltre che
   • B.4)[2] se la matrice A ha n autovalori λ1 , . . . , λn reali, distinti e negativi, per qualsiasi
     matrice B e C la risposta a un gradino unitario e condizione iniziali nulle del sistema

                                              ẋ      = Ax + Bu
                                                  y   = Cx

     non può presentare modi del tipo eαt cos(ωt) con ω 6= 0




   C)[10] Per il sistema dinamico
                                                                          
                                               0        1                0
                                 ẋ   =                         x+               u
                                              −2       −3                1
                                                      
                                 y    =       0       1 x

   C.1)[2] Si calcoli la funzione di trasferimento
                   s
   (R) G(s) = s2 +3s+2
   C.2)[2] Si calcoli la risposta al gradino unitario nel dominio del tempo
   (R) y = e−t − e−2t
                                                       2
