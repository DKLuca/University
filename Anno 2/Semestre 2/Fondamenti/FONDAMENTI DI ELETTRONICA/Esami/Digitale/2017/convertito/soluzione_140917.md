---
fonte: "soluzione_140917.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                          14 settembre 2017 parte digitale

1) Il transistore nMOS ha Vgsn=1.8-0.5=1.3V e Vdsn=1-0.5=0.5V<Vgsn-Vt: è quindi in regione
   triodo.
    Il pMOS ha Vsgp=1-0=1V e Vsdp=1-0.5=0.5V< Vsgp-Vt: è quindi in regione triodo.
    Segue che:
                 ′                        1        ′                       1
           𝐼 = 𝛽𝑛 [(𝑉𝑔𝑠𝑛 − 𝑉𝑡 )𝑉𝑑𝑠𝑛 − 2𝑉2𝑑𝑠𝑛 ] + 𝛽𝑝 [(𝑉𝑠𝑔𝑝 − 𝑉𝑡 )𝑉𝑠𝑑𝑝 − 2𝑉2𝑠𝑑𝑝 ] = 82.5𝜇𝐴

2) Il circuito di piccolo segnale deve includere sia la transconduttanza che la conduttanza di
   uscita. Non serve la gmb dato che non c’è effetto body (=0):




   Si vede subito che v1=0 e vac=v2.

   Quindi 𝑖𝑎𝑐 = 𝑣𝑎𝑐 (𝑔𝑚𝑝 + 𝑔𝑜𝑝 + 𝑔𝑜𝑛 ).

   Dai valori della polarizzazione DC calcoliamo:
                                                                  80𝜇𝐴⁄
                              𝑔𝑜𝑛 = 𝛽 ′ 𝑛 (𝑉𝑔𝑠𝑛 − 𝑉𝑡 − 𝑉𝑑𝑠𝑛 ) =        𝑉
                                                                  10𝜇𝐴⁄
                              𝑔𝑜𝑝 = 𝛽 ′ 𝑝 (𝑉𝑠𝑔𝑝 − 𝑉𝑡 − 𝑉𝑠𝑑𝑝 ) =        𝑉
                                                          50𝜇𝐴⁄
                                     𝑔𝑚𝑝 = 𝛽 ′ 𝑝 𝑉𝑠𝑑𝑝 =        𝑉
                     𝑣        1
   Quindi 𝑅𝑎𝑐 = 𝑖 𝑎𝑐 = 𝑔                 = 7.1𝑘Ω
                     𝑎𝑐   𝑜𝑛 +𝑔𝑜𝑝 +𝑔𝑚𝑝
                                                                                  𝛽′
3) La capacità di ingresso di un invertitore ad area minima vale 𝐶𝑖𝑛 = (1 + 𝛽𝑛′ ) 𝐶𝑚1 =1.8fF,
                                                                                   𝑝

   essendo 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.6𝑓𝐹. Abbiamo quindi
                                           2𝐶
                                   𝑡𝑝0 = 𝛽′ 𝑉𝑖𝑛 𝐹(𝑉𝑇 /𝑉𝑑𝑑 )=21ps
                                           𝑛 𝐷𝐷

   dato che F=2.09.
4) Il primo invertitore vede come carico una capacità quadrupla rispetto alla sua capacità di
   ingresso; il secondo vede uCin mentre ma ha una capacità di ingresso 4Cin; l’ultimo invertitore
   vede CL in uscita ed ha uCin come capacità in ingresso. Quindi
                                                      𝑢𝐶𝑖𝑛        𝐶𝐿
                                 𝑡𝑝 = 4 ∙ 𝑡𝑝0 + 𝑡𝑝0        + 𝑡𝑝0
                                                      4𝐶𝑖𝑛       𝑢𝐶𝑖𝑛
   la minimizzazione fornisce

                                              4𝐶 𝐿
                                           𝑢=√     = 21
                                                  𝐶𝑖𝑛

   da cui segue tp=304ps.
