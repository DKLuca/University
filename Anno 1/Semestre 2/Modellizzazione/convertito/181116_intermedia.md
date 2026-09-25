---
fonte: "181116_intermedia.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

MeC, Prima prova intermedia del 16/11/18
   A)[8] Per il sistema dinamico

                                         ẋ1     =     σ(x2 − x1 )
                                         ẋ2     =     x1 (ρ − x3 ) − x2
                                         ẋ3     =     x1 x2 − βx3
                                           y     =     x3 + 2u

   A.1)[3] si verifichi, giustificando, che per σ > 0, β > 0 e ρ < 1 il sistema ammette un solo
punto di equilibrio.
   R:
   Ponendo a zero le derivate si ottiene

                           x̄1 = x̄2 ,         x̄22 = β x̄3 ,   x̄2 (ρ − x̄3 − 1) = 0

   La prima soluzione dell’ultima equazione è x̄3 = ρ − 1 < 0, ma tale soluzione non
soddisfa la condizione x̄22 = β x̄3 , quindi è da scartare.
   La soluzione x̄2 = 0, da cui si ricava x̄1 = 0 e x̄3 = 0 è l’unica possibile.
   A.2)[3] Si valuti la stabilità di tale punto.
   R: La linearizzazione del sistema è
                                                                 
                                                       −σ σ   0
                                    ∂f
                              J=        f (x)|x̄=0 =  ρ −1 0 
                                    ∂x
                                                        0 0 −β
il cui polinomio caratteristico è

                              (s + β) s2 + (s + σ)s + σ(1 − ρ) = 0
                                                              

Dal momento che σ > 0 e ρ < 1, il polinomio ha tutte le radici a parte reale negativa,
dunque il punto è asintoticamente stabile.
  A.3)[2] Si risponda, giustificando, alle seguenti domande:

   • Il sistema è lineare? R. No, perchè compaiono i prodotti delle variabili di stato
   • Il sistema è del primo ordine? No, perchè l’ordine coincide con il numero di equazioni
     differenziali del primo ordine presenti, pari a 3
   • Il sistema è strettamente proprio? No, perché la variabile u compare in uscita
   • Il sistema ha numero di stati pari al numero di uscite? No, ha una uscita e tre stati
   • Per condizioni iniziali nulle, per qualsiasi ingresso u(t) vale la relazione Y (s) = 2U (s)? Sı̀,
     perchè per atli condizioni iniziali l’evoluzione dello stato è nulla

   B)[4] Per il sistema a tempo continuo
                                                       
                                       −2   0            1
                              ẋ =               x(t) +     u(t)
                                      1  −0.5
                                                        1
                            y(t) =    0 1 x(t)
                                                                       T
   Si calcoli l’evoluzione libera (dell’uscita) a partire da x(0) = 1 1
   R. Per x(0) = B la risposta di evoluzione libera coincide con risposta impulsiva, la
cui trasformata coincide con la funzione di trasferimento del sistema

                                                 s+1                 2/3    1/3
                             G(s) =                             =        +
                                         s2 + 2.5s + 1              s + 2 s + 0.5

                                                           1
da cui, antitrasformando, si ricava la risposta impulsiva y(t) = 2/3e−2t + 1/3e−t/2
   C)[3]
   Per la funzione di trasferimento
                                                        µ
                                             G(s) =
                                                    1 + sT
si calcoli l’espressione della risposta al gradino e si fornisca il calcolo del tempo di assestamento
all’1%.
    R. Si veda il libro di testo
    D)[10] Si consideri il circuito in figura 1. Utilizzando le relazioni
      u − vR − vC = 0,     vC = vL ,   iR = iL + iC ,               vR = RiR ,   iC = C v̇C ,   vL = Li̇L
D.1)[6] si ricavi la forma di stato del sistema avente ingresso u e uscita y = vR
                                                       i
                                                       R
                                        + +            _i       i
                                                 v          C + L
                                                  R
                                        u         v                  v
                                                   C                  L
                                                                _
                                        _


                                         Figure 1: D) RLC


   R.
   Posto x1 = vC e x2 = iL si ricava

u−RiR −x1 = 0,      u−R(iL +iC )−x1 = 0,          u−R(x2 +C v̇c )−x1 = 0,             u−Rx2 −RC ẋ1 −x1 = 0
e dunque la prima equazione differenziale
                                              1     1      1
                                   ẋ1 = −      x1 − x2 +    u
                                             RC     C     RC
Dalle relazioni x1 = vC = vL = Li̇L = Lẋ2 infine si ricava
                                                 1
                                          ẋ2 = x1
                                                 L
  La forma di stato del sistema è dunque
                                        1
                                              − C1
                                                        1 
                                     − RC                  RC
                           ẋ =        1             x +       u
                                    L        0            0
                           y =       −1 0 x + u
  D.2)[2] si determinino la relazione che devono soddisfare i parametri affinchè il sistema esibisca
modi smorzati oscillanti.
                                                              1      1
  R. Il polinomio caratteristico della matrice è s2 + RC       s + LC , polinomio il cui deter-
minante deve essere negativo per avere radici smorzate, ovvero
                                                      2
                                                  1              4
                                       ∆=                   −      <0
                                                 RC             LC

   D.3)[2] si determini il valore della resistenza per cui il sistema ammette modi oscillanti non
smorzati.
   R. Affinchè il sistema ammetta modi oscillanti non smorzati, la parte reale delle
radici deve essere nulla, condizione che si verifica solo se R = ∞ (ovvero non c’e’
perdita)


                                                       2
