---
fonte: "soluzione_25_settembre.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                25 settembre 2012
                                  parte digitale
1. La funzione logica implementata é F = A + BC come si vede dal fatto che l’uscita si scarica se
   A = 1 oppure se B = C = 1.

2. Nelle diverse configuarazioni cambia il dimensionamento S eq della rete (pull-up o pull-down) inter-
   essata. Calcoliamo
                                               2CL
                                        τ0 = 0       F (VT /VDD )                                   (1)
                                              βn VDD
  come il ritardo corrispondente a Sn = 1 (o con Sp =2), che vale τ0 = 350ps.
  Gli Seq per ogni configurazione sono indicati nella tabella seguente insieme al ritardo che é dato da
  τf = τ0 Sn /Seq per la scarica e da τr = τ0 Sp /Seq (dato che Sp /Sn =βn /βp ).
    A   B   C                Seq          τ [ps]
    0   0   0    salita   (2/3)Sp    1.5τ0 =525ps
    0   0   1    salita     Sp /2     2τ0 =700ps
    0   1   0    salita     Sp /2     2τ0 =700ps
    0   1   1   discesa    Sn /2      2τ0 =700ps
    1   0   0   discesa      Sn        τ0 =350ps
    1   0   1   discesa      Sn        τ0 =350ps
    1   1   0   discesa      Sn        τ0 =350ps
    1   1   1   discesa    1.5Sn    τ0 /1.5=233ps

3. La potenza dinamica é pari a:
                                                     2
                                             P = CL VDD fc P0→1                                      (2)
  dato che nella tabella della varitá abbiamo 5 ’0’ e 3 ’1’, P 0→1 = (3/8)(5/8) = 15/64. Sostituendo i
  valori numerici, si trova P =11.4µW.

4. Essendoci l’invertitore, il pull-down deve scaricare in base alla funzione logica PD=A + BC ovvero
   PD=A(B + C). Si ottiene lo schema seguente:
                                             Vdd               Vdd
                                        ck
                                                                          CL
                                                        Cinv
                                    B         C

                                        A
                                        ck

5. In questo caso abbiamo
                                                          2
                                         P = (CL + Cinv )VDD fc P0                                   (3)
  dato che i nodi CL e Cinv si scaricano alternativamente. P0 é la probabilitá di scaricare il nodo
  Cinv e vale 3/8, dato che la funzione logica complessiva é a ’1’ solo 3 volte su 8 configurazioni.
  Abbiamo:
                              Cinv = (Sn + Sp )(L2M IN Cox + 2CGSO LM IN )                            (4)
  Sostituendo i valori numerici si ottiene C inv =1.6fF e P = 19µW
