---
fonte: "soluzione_6_febbraio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                 7 febbraio 2014
                                  parte digitale
1. In un invertitore ad area minima con tempo di salita uguale al tempo di discesa, il transistore
   nMOS ha fattore di forma Sn =1, mentre il pMOS ha Sp = Sn βn′ /βp′ =2. La capacitá di ingresso
   vale
                                          Ci = (1 + ǫ)CM                                       (1)
   con ǫ = βn′ /βp′ =2 e CM 1 = Cox L2M IN + 2CGSO LM IN =1.12fF.
   Otteniamo Ci =3.4fF.

2. Il ritardo di un invertitore ad area minima che carica una capacitá Ci vale

                                               2(1 + ǫ)CM
                                       tp0 =              F (VT /VDD )                                (2)
                                                 βn′ VDD

   dove F =2.2.
   Otteniamo tp0 =37ps.

3. Sappiamo che il ritardo di ogni invertitore della catena é pari a tp0 per il rapporto tra la capacitá
   di carico e la capacitá di ingresso. I primi N − 1 stadi vedono in uscita una capacitá che é 3 volte
   la loro capacitá di ingresso, quindi ciascuno di loro ritarda 3tp0 . L’ultimo stadio ha una capacitá
   di ingresso 3N −1 Ci . Il ritardo complessivo vale quindi:
                                                                   CL
                                     tp = (N − 1) · 3 · tp0 + tp0 N −1                                (3)
                                                                 3     Ci
   Il numero di stadi ottimo lo si trova ponendo dtp /dN = 0. Con semplici passaggi si trova:
                                                                      
                                                                 CL
                                                        ln       Ci ln3
                                               Nopt =                                                 (4)
                                                                 ln3
   Dato che ln3 non é molto lontano da 1, l’espressione per Nopt non di discosta troppo da quanto
   visto a lezione per il caso in cui ogni stadio é e volte il precedente.
   Eq.4 fornisce Nopt =5.3.

4. In base ai calcoli al punto precedente, dobbiamo calcolare il ritardo usando Eq.3 con N =5 ed N = 6.
   Avremmo fatto la stessa cosa anche utilizzando la formula vista a lezione, dato che ln(CL /Ci )=5.7.
   Per N =5, troviamo tp =582ps.
   Per N =6, troviamo tp =603ps.
