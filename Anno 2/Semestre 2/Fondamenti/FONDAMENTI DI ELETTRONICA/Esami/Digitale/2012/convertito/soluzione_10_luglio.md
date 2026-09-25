---
fonte: "soluzione_10_luglio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                   10 luglio 2012
                                   parte digitale
1. essendoci l’invertitore, F =P D. La rete di pull-down é quindi composta da un nMOS comandato
   da C in serie col parallelo di due nMOS comandati da A e B. La rete di pull-up é il duale ed é
   composta da un pMOS comandato dal segnale C in parallelo alla serie di due pMOS comandati da
   A e B.
2. Nel caso peggiore il transitorio da salita avviene tramite la serie dei transistori pMOS pilotati da A
   e B, quindi con un Seq = Sp /2. Il transitorio di discesa di caso peggiore avviene attraverso la serie
   del nMOS pilotato da C ed uno dei due nMOS pilotati da A e B, quindi S eq = Sn /2. Ne consege
   che
                                                                 β0
                                  βn0 Sn /2 = βp0 Sp /2 → Sp = Sn n0 = αSn                             (1)
                                                                 βp
   Ogni ingresso va sul gate di un nMOS e di un pMOS, quindi

                        Cin = (Sn + Sp )(L2M IN Cox + 2CGSO LM IN ) = Sn (1 + α)Cm                         (2)

   Sostituendo i valori numerici si ottiene C m =0.355fF. Ne consegue che Sn =1.06 ed Sp =1.76.
   Potremmo anche approssimarli agli interi piú vicini, ma per semplicitá teniamo i valori di cui
   sopra.
3. La capacitá di ingresso dell’invertitore é data da

                                           Cinv = Sn,inv (1 + α)Cm                                         (3)

   Se consideriamo il transitorio di discesa del nodo intermedio e quello di salita dell’uscita dell’invertitore:
                                    2Cinv                      2CL
                        τr =                 F (VT /VDD ) + 0            F (VT /VDD )                      (4)
                               βn (Sn /2)VDD
                                0                          βp Sp,inv VDD

   dove, sostituendo i valori numerici, si trova che F =1.92. Essendo β p0 Sp,inv =βn0 Sn,inv e scrivendo la
   Cinv in funzione di Sn,inv , troviamo:
                                                                                  "                              #
        2Cm (1 + α)Sn,inv                    2CL                        2F  Cm (1 + α)           CL
   τr =                   F (VT /VDD )+ 0              F (VT /VDD ) = 0                Sn,inv +
          βn (Sn /2)VDD
           0                             βn Sn,inv VDD               βn VDD   Sn /2             Sn,inv
                                                                                                  (5)
   che viene minimizzato se dτr /dSn,inv =0. Si ottiene
                                                    s
                                                         CL Sn /2
                                         Sn,inv =                  = 4.1                                   (6)
                                                        Cm (1 + α)
   che fornisce τr =112ps e Cinv =3.9fF.
4. Nel caso peggiore abbiamo τr =τf =112ps. Se inseriamo il valore di Sn,inv nella formula del ritardo
   vediamo che metá é il transitorio di C inv e metá il transitorio di CL . Questo secondo contributo
   non cambia se gli ingressi cambiano, dato che dipende dall’invertitore.
   La discesa di CL (che é l’uscita della porta complessiva) di caso migliore la si ha quando il pull-up
   é piú conduttivo, ovvero tutti i pMOS sono accesi. In tal caso S eq =1.5Sp (Sp in parallelo con Sp /2)
   che é 3 volte il caso peggiore. Quindi il ritardo sará τ f =56/3+56=75ps.
   La salita di caso migliore la si ha con tutti gli nMOS del pull-down accesi, con S eq =(2/3)Sn (serie
   tra Sn e 2Sn ) che é 4/3 quella del caso peggiore, quindi τ r =56 · 3/4 + 56=98ps.
5. La potenza dinamica é pari a:
                                                          2
                                         P = (CL + Cinv )VDD fc P0→1                                       (7)
   dove abbiamo sommato CL e Cinv dato che essendoci l’invertitore, quando commuta un nodo
   commuta anche l’altro. Nella tabella della veritá abbiamo 3 ’1’ e 5 ’0’, quindi P 0→1 = (3/8)(5/8) =
   15/64. Sostituendo i valori numerici, si trova P =15.9µW.
