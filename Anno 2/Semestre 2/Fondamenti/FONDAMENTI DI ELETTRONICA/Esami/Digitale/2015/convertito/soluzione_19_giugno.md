---
fonte: "soluzione_19_giugno.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                          del 19 giugno 2015, parte digitale

1) Essendoci l’invertitore, F=PD. Abbiamo il parallelo tra A e B in serie con C, quindi
   F=(A+B)C
2) Nella carica di caso peggiore abbiamo 2 pMOS in serie, così come abbiamo 2 nMOS in
   serie nella scarica di caso peggiore. Quindi Sp=Snn’/ p’=2
3) Ciascun segnale di ingresso (A, B e C) va su un nMOS e un pMOS, quindi
                                         Ci=( Sn+ Sp)CM1=1.8fF
   essendo 𝐶𝑀1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.6𝑓𝐹
4) Sia per la porta a monte che per l’inverter i tempi di salita e di discesa sono gli stessi, quindi
   possiamo considerare il ritardo totale come somma dei tempi di discesa
            2𝐶𝐼𝑁𝑉                    2𝐶𝐿                    2𝐹                         𝐶𝐿
    𝑡𝑝 =       1   𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′          𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = ′     [2(1 + 𝜀)𝐶𝑀1 𝑆𝐼𝑁𝑉 +      ]
             ′
           𝛽𝑛 2𝑉𝐷𝐷               𝛽𝑛 𝑆𝐼𝑁𝑉 𝑉𝐷𝐷               𝛽𝑛 𝑉𝐷𝐷                     𝑆𝐼𝑁𝑉

   la minimizzazione fornisce

                    𝐶
   𝑆𝐼𝑁𝑉 = √2(1+𝜀𝐿)𝐶            = 3.7
                          𝑀1

   da cui CINV=6.7fF
5) Il ritardo dell’invertitore è sempre lo stesso per ogni configurazione degli ingressi
                                             2𝐶𝐿
                                𝑡𝐼𝑁𝑉 =    ′
                                                     𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = 104𝑝𝑠
                                         𝛽𝑛 𝑆𝐼𝑁𝑉 𝑉𝐷𝐷
   A questo va sommato il ritardo della porta a monte, che vale
                             2𝐶𝐼𝑁𝑉                                 2𝐶𝐼𝑁𝑉
                   𝑡𝐹 =               𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) o    𝑡𝑅 =                𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                          𝛽𝑛′ 𝑆𝑒𝑞 𝑉𝐷𝐷                           𝛽𝑝′ 𝑆𝑒𝑞 𝑉𝐷𝐷

   a seconda che si tratti di carica o scarica. Per i diversi casi otteniamo:
                   A      B      C       Seq     tF+tINV [ps]       tR+tINV [ps]
                   0      0      0       3                               138
                   0      0      1       1                               208
                   0      1      0       2                               156
                   0      1      1       ½             208
                   1      0      0       2                               156
                   1      0      1       ½             208
                   1      1      0       2                               156
                   1      1      1       2/3           182


6) Essendo una logica dinamica, preleviamo energia dall’alimnetazione con probabilità P F(1-PF)
   sia quando dobbiamo caricare CL che quando dobbiamo caricare CINV. Dalla tabelle di verità
   vediamo che PF=3/8 Quindi:
                     2
   𝑃𝐷 = (𝐶𝐿 + 𝐶𝐼𝑁𝑉 )𝑉𝐷𝐷 𝑓𝐶𝐾 𝑃𝐹 (1 − 𝑃𝐹 ) = 21.5𝜇𝑊
