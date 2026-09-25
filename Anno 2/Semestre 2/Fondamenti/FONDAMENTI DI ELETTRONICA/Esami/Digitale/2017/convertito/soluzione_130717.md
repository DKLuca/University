---
fonte: "soluzione_130717.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                            13 luglio 2017 parte digitale

                                                                                   𝛽′
1) La capacità di ingresso di un invertitore ad area minima vale 𝐶𝑖𝑛 = (1 + 𝛽𝑛′ ) 𝐶𝑚1 =1.8fF,
                                                                                       𝑝

   essendo 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.6𝑓𝐹. Abbiamo quindi
                                              2𝐶
                                  𝑡𝑝0 = 𝛽′ 𝑉𝑖𝑛 𝐹 (𝑉𝑇 /𝑉𝑑𝑑 )=12.6ps
                                              𝑛 𝐷𝐷

   dato che F=1.89.
2) I primi due invertitori vedono come carico una capacità tripla rispetto alla loro capacità di
   ingresso; l’ultimo invertitore vede CL in uscita ed ha 9Cin come capacità in ingresso. Quindi
                                                              𝐶𝐿
                                𝑡𝑝 = 2 ∙ 3 ∙ 𝑡𝑝0 + 𝑡𝑝0            = 309𝑝𝑠
                                                             9𝐶𝑖𝑛
3) Abbiamo:
                                               2
                      𝑃𝑑 = (𝐶𝐿 + 3𝐶𝑖𝑛 + 9𝐶𝑖𝑛 )𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝑖𝑛 (1 − 𝑃𝑖𝑛 ) = 22𝜇𝑊
   dove Pin=0.3 (probabilità che ingresso sia ‘1’, ovvero che uscita sia ‘0’)
4) In questo caso, chiamando u il dimensionamento del nMOS nell’ultimo invertitore:
                                                           𝑢𝐶𝑖𝑛        𝐶𝐿
                                 𝑡𝑝 = 3 ∙ 𝑡𝑝0 + 𝑡𝑝0             + 𝑡𝑝0
                                                           3𝐶𝑖𝑛       𝑢𝐶𝑖𝑛
   la minimizzazione fornisce

                                                 3𝐶𝐿
                                              𝑢=√    = 22.4
                                                     𝐶𝑖𝑛

   da cui segue tp=226ps.
5) Il transistore nMOS ha Vgsn=1.8-1=0.8V e Vdsn=1.5-1=0.5V=Vgsn-Vt: è quindi al confine tra
   saturazione e regione triodo. Il pMOS ha Vsgp=1.5-0=1.5V e Vsdp=1.5-1=0.5V< Vsgp-Vt: è
   quindi in regione triodo. Segue che:
                                        2
                       ′ (𝑉𝑔𝑠𝑛 − 𝑉𝑡 )          ′                       1
                  𝐼 = 𝛽𝑛                    + 𝛽𝑝 [(𝑉𝑠𝑔𝑝 − 𝑉𝑡 )𝑉𝑠𝑑𝑝 − 2𝑉2𝑠𝑑𝑝] = 109𝜇𝐴
                              2
