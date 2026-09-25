---
fonte: "soluzione_01032018.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                             1 marzo 2018 parte digitale

1) Il transistore 1 è sopra soglia e quindi deve circolare una corrente non nulla nella serie dei
   due. Il transistore 2 ha la tensione di drain uguale a quella di gate e quindi è saturo. La Vds
   del transistore 1 è almeno usa soglia sotto 1V e quindi il transistore 1 è in regione triodo.
   Abbiamo quindi:
                                                            2
          ′                       2         ′ (𝑉𝑔𝑠2 −𝑉𝑡 )
    𝐼 = 𝛽𝑛 [(𝑉𝑔𝑠1 − 𝑉𝑡 )𝑉𝑑𝑠1 − 12𝑉𝑑𝑠1] = 𝛽𝑛
                                                   2

   essendo VGS1=2V e VDS1=1-VGS2, otteniamo un’equazione di 2° grado in VGS2. La soluzione è
   VGS2=0.915V, a cui corrisponde una corrente I=26.5A.
                                                                                    𝛽′
2) La capacità di ingresso di un invertitore ad area minima vale 𝐶𝑖𝑛 = (1 + 𝑛′ ) 𝐶𝑚1 =1.8fF,
                                                                                    𝛽𝑝
   essendo 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.6𝑓𝐹. Abbiamo quindi
                                             2𝐶
                                      𝑡𝑝0 = 𝛽′ 𝑉𝑖𝑛 𝐹 (𝑉𝑇 /𝑉𝑑𝑑 )=21ps
                                              𝑛 𝐷𝐷

   dato che F=2.09.
3) Il primo invertitore vede come carico una capacità tripla rispetto alla sua capacità di ingresso;
   il secondo vede uCin mentre ma ha una capacità di ingresso 3Cin; l’ultimo invertitore vede CL
   in uscita ed ha uCin come capacità in ingresso. Quindi
                                                        𝑢𝐶𝑖𝑛        𝐶𝐿
                                  𝑡𝑝 = 3 ∙ 𝑡𝑝0 + 𝑡𝑝0         + 𝑡𝑝0
                                                        3𝐶𝑖𝑛       𝑢𝐶𝑖𝑛
   la minimizzazione fornisce

                                                3𝐶𝐿
                                             𝑢=√    = 22
                                                     𝐶𝑖𝑛

   da cui segue tp=374ps.
4) Ciascun invertitore commuta ad ogni ciclo di clock, quindi
                                                      2
                             𝑃𝑑 = (3𝐶𝑖𝑛 + 𝑢𝐶𝑖𝑛 + 𝐶𝐿 )𝑉𝐷𝐷 𝑓𝑐𝑘 = 112𝜇𝑊
