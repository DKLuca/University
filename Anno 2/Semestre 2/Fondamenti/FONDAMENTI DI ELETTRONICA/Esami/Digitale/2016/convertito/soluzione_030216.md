---
fonte: "soluzione_030216.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                         del 3 febbraio 2016, parte digitale

1) Il circuito è un full-adder. Essendoci invertitori prima delle uscite S e Co, per analizzare la
   funzione logica basta guardare le reti di pull-down a monte degli invertitori stessi. Si nota
   subito che
                                           𝐶𝑜 = 𝐴𝐵 + 𝐵𝐶 + 𝐴𝐶
                                        𝑆 = 𝐴𝐵𝐶 + 𝐶̅ (𝐴 + 𝐵 + 𝐶)
2) La discesa di Co implica scarica di CL tramite il transistore nMOS dell’invertitore. La C in di
   tale invertitore deve essere caricata dalla rete di pull-up a monte. Quindi:
                                  2 ∙ 2𝐶𝑖𝑛𝑣                  2𝐶𝐿
                       𝑡𝑓𝑎𝑙𝑙 =    ′
                                              𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′     𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                 𝛽𝑝 𝑆𝑝,𝑒𝑞 𝑉𝐷𝐷               𝛽𝑛 𝑉𝐷𝐷

   dove F=2.09. La capacità di ingresso dell’invertitore ad area minima è:
                                      Cinv=( Sn+ Sp)CM1=1.35fF
    con 𝐶𝑀1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 ) e Sn=1 Sp=2.
   Il dimensionamento equivalente della rete di pull-up nel caso peggiore vale
               1
    𝑆𝑝,𝑒𝑞 = 1 1 1 = 4/5
              + +
             4 2 2

   Cioè, abbiamo la serie dei 2 pMOS comandati da A e B, in serie col parallelo dei 2 pMOS
comandati anche loro da A e B.
   Otteniamo infine tfall=826ps.
3) Il ritardo di un invertitore con Sn=1 Sp=2 che carica una capacità Cinv calcolata al punto 2
   vale:
                                           2𝐶𝑖𝑛
                                  𝑡𝑝0 =           𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = 10.4𝑝𝑠
                                          𝛽𝑛′ 𝑉𝐷𝐷


4) Ogni stadio ritarda tp0 per il rapporto tra capacità di uscita e di ingresso, quindi:
                                                       4   𝐶𝐿
                                       𝑡𝑝 = 𝑡𝑝0 (𝑢 +     +    )
                                                       𝑢 4𝐶𝑖𝑛
    la minimizzazione fornisce

    𝑢 = √4 = 2
   Segue
                                                       𝐶𝐿
                                 𝑡𝑝 = 𝑡𝑝0 (2 + 2 +         ) = 1.01𝑛𝑠
                                                      4𝐶𝑖𝑛
