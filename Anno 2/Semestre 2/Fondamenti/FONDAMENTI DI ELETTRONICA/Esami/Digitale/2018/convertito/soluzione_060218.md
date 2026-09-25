---
fonte: "soluzione_060218.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                            6 febbraio 2018 parte digitale


1) Quando Vi=Vdd e Vo=0, solo M5 è acceso e si trova ad avere Vgs=Vdd e Vds=0V. E’ in regime
   lineare e la sua conduttanza di uscita vale:
                                                          1
                             𝑔𝑜 = 𝑆5 𝛽′𝑛 (𝑉𝑑𝑑 − 𝑉𝑇 ) =       → 𝑆5 = 34.5
                                                          50
   Quando invece Vi=0 e Vo=Vdd, solo M6 è acceso con Vsg=Vdd e Vsd=0V. E’ in regime lineare
   e la sua conduttanza di uscita vale:
                                                           1
                              𝑔𝑜 = 𝑆6 𝛽′𝑝 (𝑉𝑑𝑑 − 𝑉𝑇 ) =       → 𝑆6 = 69
                                                           50
2) Si tratta di una catena di invertitori in cui il terzo non è caricato e quindi non aggiunge ritardo.
   Per i primi due stadi il ritardo segue il rapporto tra capacità dello stadio successivo e quella
   dello stadio interessato:
                                           𝐶𝑖𝑛 (𝑀3+𝑀4)       𝐶𝑖𝑛 (𝑀5+𝑀6)
                                𝑡𝑝 = 𝑡𝑝0               + 𝑡𝑝0
                                           𝐶𝑖𝑛 (𝑀1+𝑀2)       𝐶𝑖𝑛 (𝑀3+𝑀4)

   Le capacità di ingresso dei vari stadi sono proporzionali ai fattori di forma degli nMOS (dato
   che i pMOS sono grandi il doppio per avere trise=tfall). Quindi:
                                                      𝑆3       𝑆5
                                           𝑡𝑝 = 𝑡𝑝0      + 𝑡𝑝0
                                                      𝑆1       𝑆3

   La minimizzazione fornisce 𝑆3 = √𝑆5 𝑆1 = 5.9 da cui segue 𝑆4 = 2 𝑆3 = 11.8

3) Quando Vi=Vdd, M6 è spento ed M5 acceso. L’unica soluzione sensata è Vo=0V dato che la
   corrente deve sia “entrare” in RL che entrare nel drain di M5.
   Quando invece Vi=0, M5 è spento ed M6 è acceso. In tal caso la corrente di drain deve essere
   uguale a quella sulla resistenza RL. Assumiamo che M6 sia in regione triodo, poi
   verificheremo che sia vero. Abbiamo:
                       𝑉𝑜
                          = 𝑆6 𝛽′𝑝 [(𝑉𝐷𝐷 − 𝑉𝑇 )(𝑉𝐷𝐷 − 𝑉𝑂 ) − 0.5(𝑉𝐷𝐷 − 𝑉𝑂 )2 ]
                       𝑅𝐿
   equazione di secondo grado con soluzione Vo=0.69V. Il valore verifica l’ipotesi che M6 operi
   in regione triodo.
