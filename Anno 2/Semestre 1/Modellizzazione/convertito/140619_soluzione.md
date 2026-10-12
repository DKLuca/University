---
fonte: "140619_soluzione.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

MeC, 19/06/14
    A)[9] Si consideri il sistema dinamico in figura 1 costituito da una massa concentrata di valore
M posta all’estremità di una asta priva di massa e di lunghezza pari a L. Una molla ideale di
costante elastica pari a K e lunghezza a riposo nulla è collegata a un estremo alla massa M e
all’altra a un pattino privo di attrito libero di scorrere sul binario orizzontale.




                                        θ

                                                      L
                                                                        K


                                                                        F
                                                                         el
                                                              M
                                                                         F
                                                                            g



                                       Figure 1: Pendolo con molla


    A.1)[3] Si ricavi il modello in forma di stato del sistema considerando quale uscita l’angolo θ
(nel caso non si sia in grado di ricavare il sistema, chiedere al docente);
    A.2)[3] Si dica per quali valori dei parametri il sistema ammette tre punti di equilibrio
nell’intervallo θ ∈ [−π, π] e per tali valori dei parametri si ricavi il sistema linearizzato in forma
di stato;
    A.3)[3] Si dica quali condizioni debbono essere verificate affinché i modi del sistema linearizzato
in ciascuno dei punti di equilibrio siano puramente oscillanti;
    R. A.1) La somma delle forze agenti sulla massa M , considerato positivo il verso
della forza di gravità,    è pari a Ftot = M g − KL cos(θ). L’equazione fondamentale del
                      τagenti = I θ̈, posto che I = M L2 , diventa dunque
                   P
moto rotatorio

                             M L2 θ̈    =        (M g − KL cos(θ))(−L sin(θ))
                              M Lθ̈     =        (KL cos(θ) − M g) sin(θ)

Ponendo x1 = θ e x2 = θ̇, la forma di stato risulta essere
                                  ẋ1       = x2
                                               K            g
                                                              
                                  ẋ2       =  M cos(x1 ) − L sin(x1 )
                                    y       = x1

R. A.2) Ponendo a zero la derivata,
                                                                  
                                                 K             g
                              x̄2 = 0              cos(x̄1 ) −         sin(x̄1 ) = 0
                                                 M             L
si vede che nell’intervallo [−π, π] il sistema ammette i seguenti punti di equilibrio

                             x̄1 = 0    per ogni valore dei parametri
            Mg
inoltre, se KL  ≤ 1 (ovvero alla massima estensione la forza elastica é superiore alla
forza di gravità), i punti                          
                                                   Mg
                                  x̄1 = ± arccos
                                                   KL

                                                          1
   Il sistema linearizzato in un punto di equilibrio x̄1 , x̄2 è
                                                              
                         ˙                  0               1
                        ∆x   =     K           g                  ∆x
                                        1 ) − L cos(x̄1 ) 0
                                 M cos(2x̄
                        ∆y =      1 0 ∆x

R. A.3) Le radici del polinomio caratteristico della matrice A sono le radici di
                                                             
                              2       K             g
                            λ −         cos(2x̄1 ) − cos(x̄1 ) = 0
                                      M             L

Affinché le due radici siano puramente immaginarie, dev’essere verificata la condizione
                                   K             g
                                     cos(2x̄1 ) < cos(x̄1 )
                                   M             L
Per x̄1 = 0 la condizione è complementare a quella richiesta per l’esistenza di tre punti
di equilibrio, ovvero
                                       KL ≤ M g
(perché, intuitivamente, se la forza elastica alla massima estensione fosse maggiore
della forza di gravità il sistema, perturbato, scapperebbe via dall’origine).
                                                                                        Mg
   Per gli altri due punti di equilibrio, dato che soddisfano la condizione cos(x̄1 ) = KL ,
la condizione di oscillazione può essere riscritta come
                                                          Mg
                              cos(x̄1 )2 − sin(x̄1 )2 ≤      cos(x̄1 )
                                                          KL
ovvero, sostituendo
                                  (M g)2              2   (M g)2
                                         − sin(x̄ 1 )   ≤
                                  (KL)2                   (KL)2
semplificando i membri si vede che dev’essere verificata la condizione

                                          sin(x̄1 )2 ≥ 0

e dunque, se il sistema ammette punti di equilibrio diversi dall’origine, i modi del
sistema linearizzato in corrispondenza ad essi sono certamente oscillanti.




                                                 2
