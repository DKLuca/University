---
fonte: "soluzione_170216.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                          del 17 febbraio 2016, parte digitale

1) La discesa di Co implica scarica di CL tramite il transistore nMOS dell’invertitore. La C inv0 di
   tale invertitore (e la capacità di ingresso della rete che poi produce S, a sua volta pari a C inv0)
   deve essere caricata dalla rete di pull-up a monte. Quindi:
                                    2 ∙ 2𝐶𝑖𝑛𝑣0                 2𝐶𝐿
                         𝑡𝑓𝑎𝑙𝑙 =     ′
                                                𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′     𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                   𝛽𝑝 𝑆𝑝,𝑒𝑞 𝑉𝐷𝐷               𝛽𝑛 𝑉𝐷𝐷

   dove F=2.09. La capacità di ingresso dell’invertitore ad area minima è:
                                        Cinv0=( Sn+ Sp)CM1=1.35fF
    con 𝐶𝑀1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 ) e Sn=1 Sp=2.
    Nel caso della salita di Co, invece, CL si carica tramite il transistore pMOS dell’invertitore:
                                    2 ∙ 2𝐶𝑖𝑛𝑣0                  2𝐶𝐿
                       𝑡𝑟𝑖𝑠𝑒 =       ′
                                                𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′      𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                   𝛽𝑛 𝑆𝑛,𝑒𝑞 𝑉𝐷𝐷               𝛽𝑝 2𝑉𝐷𝐷

   I risultati per i diversi casi sono in tabella:
     A     B    C      Co      Seq                                         trise [ps]     tfall [ps]
     0     0    0      0       21/(1/(3/2)+1/(1/2))=12/7                          -             179
     0     0    1      0       21/(1/(1/2)+1/2)=4/5                               -             207
     0     1    0      0       21/2=1                                             -             196
     0     1    1      1       ½                                                  196             -
     1     0    0      0       21/2=1                                             -             196
     1     0    1      1       ½                                                  196             -
     1     1    0      1       ½                                                  196             -
     1     1    1      1       ½ + 1/(1+1/2)=7/6                                  173             -

2) Abbiamo:
                                    2                         2
                      𝑃𝑑𝑦𝑛 = 𝐶𝐿,𝑆 𝑓𝑉𝐷𝐷 𝑃𝑆 (1 − 𝑃𝑆 ) + 𝐶𝐿,𝐶𝑜 𝑓𝑉𝐷𝐷 𝑃𝐶𝑜 (1 − 𝑃𝐶𝑜 )

    dalla tabella della verità si vede che sia S che Co sono a ‘1’ nel 50% dei casi. Sono poi
    collegate alla stessa CL=20fF. Troviamo
                                                    2
                                              2𝐶𝐿 𝑓𝑉𝐷𝐷
                                       𝑃𝑑𝑦𝑛 =          = 16.2𝜇𝑊
                                                  4
3) La carica di Co di caso peggiore è quando abbiamo 2 nMOS in serie nel pull-down della rete
   che poi comanda l’invertitore. Se chiamiamo Sinv il dimensionamento del nMOS
   dell’invertitore:
                         2(𝐶𝑖𝑛𝑣0 + 𝑆𝑖𝑛𝑣 𝐶𝑖𝑛𝑣0 )                   2𝐶𝐿
               𝑡𝑟𝑖𝑠𝑒 =          ′
                                                𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′           𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                              𝛽𝑛 0.5𝑉𝐷𝐷                       𝛽𝑝 2𝑆𝑖𝑛𝑣 𝑉𝐷𝐷

    la minimizzazione fornisce

                                                        𝐶𝐿
                                           𝑆𝑖𝑛𝑣 = √          = 2.7
                                                      2𝐶𝑖𝑛𝑣0
