---
fonte: "soluzione_21_febbraio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                  21 febbraio 2014
                                   parte digitale
1. In un invertitore ad area minima con tempo di salita uguale al tempo di discesa, il transistore
   nMOS ha fattore di forma Sn =1, mentre il pMOS ha Sp = Sn βn′ /βp′ =3. La capacitá di ingresso
   vale
                                         Ci = (1 + ǫ)CM 1                                      (1)
   con ǫ = βn′ /βp′ =3 e CM 1 = Cox L2M IN + 2CGSO LM IN =1.9fF.
   Otteniamo Ci =7.7fF.

2. Il ritardo di un invertitore ad area minima che carica una capacitá Ci vale

                                               2(1 + ǫ)CM 1
                                       tp0 =                F (VT /VDD )                                 (2)
                                                  βn′ VDD

   dove F =2.0.
   Otteniamo tp0 =41ps.

3. Sappiamo che il ritardo di ogni invertitore della catena é pari a tp0 per il rapporto tra la capacitá
   di carico e la capacitá di ingresso. I primi N − 1 stadi vedono in uscita una capacitá che é 2 volte
   la loro capacitá di ingresso, quindi ciascuno di loro ritarda 2tp0 . L’ultimo stadio ha una capacitá
   di ingresso 2N −1 Ci . Il ritardo complessivo vale quindi:
                                                                    CL
                                      tp = (N − 1) · 2 · tp0 + tp0 N −1                                  (3)
                                                                  2     Ci
   Sostituendo i valori numerici, tp =663ps.

4. L’attivitá del buffer é 1/4; tutte la capacitá della catena vengono caricate (o scaricate) durante ogni
   transitorio; abbiamo quindi:
                                                              N −1
                                                                             !
                                                                     2n Ci
                                                              X
                                                 2
                                      P = 0.25f VDD CL +                                                 (4)
                                                              n=1

   dove ovviamente non contiamo la Ci del primo invertitore, dato che non viene caricata dal buffer.
   Sostituendo i valori numerici, P =577µW.
