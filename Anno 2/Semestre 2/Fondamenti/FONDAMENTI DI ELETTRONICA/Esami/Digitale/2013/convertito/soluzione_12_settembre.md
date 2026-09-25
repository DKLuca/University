---
fonte: "soluzione_12_settembre.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                 12 settembre 2013
                                   parte digitale
1. La funzione logica implementata é

                                     F = I1 A B + I 2 A B + I 3 A B + I 4 A B                                  (1)

   si tratta quindi di un multiplexer a 4 ingressi (I 1 , I2 , I3 e I4 ) selezionati dalla parola di 2 bit definita
   da A e B.

2. Il tempo di ritardo complessivo é dato da

                                           τ = τpass−tr + τinv1 + τinv2                                        (2)

   Dato che INV1 é fissato, il ritardo τ pass−tr dei pass-transistors non dipende dal dimensionamento
   di INV2. Vediamo come τinv1 e τinv2 dipendono da Sn,inv2 :

                                             2Cinv2         2Sn,inv2 CM 1 (1 + )
                               τinv1 =                  F =                       F                            (3)
                                         βn Sn,inv1 VDD
                                          0                       βn0 VDD

   dove  = βn0 /βp0 =2, F =2.09, CM 1 = Cox L2M IN + 2CGSO LM IN =0.52fF.

                                                             2CL
                                             τinv2 =                   F                                       (4)
                                                       βn0 Sn,inv2 VDD

   La condizione dτ /dSn,inv2 =0 fornisce:
                                                      s
                                                              CL
                                          Sn,inv2 =                    = 4.4                                   (5)
                                                          CM 1 (1 + )

3. Ci serve τpass−tr ; vediamo che i rami della rete a pass-transistor sono tutti mutuamente esclusivi,
   abbiamo quindi sempre 2 pass-tr in serie; peró quelli spenti contribuiscono lo stesso con la loro C P ;
   quindi il pass-tr piú a monte vede 3C P ed il secondo pass-tr, il quale, a sua volta, vede 2C P piú la
   capacitá dell’INV1:

       τpass−tr = 2.3(RP · 3CP + 2RP · (2CP + Cinv1 )) = 2.3(7RP CP + 2RP CM 1 (1 + )) = 79ps                 (6)

   Aggiungendo τinv1 e τinv2 (che sono uguali tra loro e pari a 80ps), otteniamo τ =238ps.

4. La scarica del nodo O1 passa attraverso 2 nMOS in serie, i quali possono scaricare fino a 0V. Nella
   carica invece abbiamo ancora 2 nMOS in serie, entrambi col gate a V DD ; la massima tensione al
   nodo O1 é quindi VDD − VT .

5. usiamo la formula:
                                                        2
                                                P = CL VDD fck f01                                             (7)
   la probabilitá di transizione é data da f 01 = f0 f1 ; f0 e f1 valgono entrambe 0.5. Troviamo
   P =7.3µW.
