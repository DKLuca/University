---
fonte: "soluzione_220715.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                          del 22 luglio 2015, parte digitale

1) La capacità di ingresso dell’invertitore ad area minima è:
                                      Ci=( Sn+ Sp)CM1=1.8fF

   essendo 𝐶𝑀1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.6𝑓𝐹 e Sn=1 Sp==2.
   Il ritardo di tale invertitore che carica una capacità Cin vale:
                                          2𝐶𝑖𝑛
                                 𝑡𝑝0 =           𝐹(𝑉𝑇 /𝑉𝐷𝐷 ) = 14𝑝𝑠
                                         𝛽𝑛′ 𝑉𝐷𝐷
   con F=2.09
2) Ogni stadio ritarda tp0 per il rapporto tra capacità di uscita e di ingresso, quindi:
                                                     9   𝐶𝐿
                                     𝑡𝑝 = 𝑡𝑝0 (𝑢 +     +    )
                                                     𝑢 9𝐶𝑖𝑛
   la minimizzazione fornisce

   𝑢 = √9 = 3
   da cui tp=255ps
3) Abbiamo
                            2
   𝑃𝐷 = (𝐶𝐿 + 3𝐶𝑖𝑛 + 9𝐶𝑖𝑛 )𝑉𝐷𝐷 𝑓𝐶𝐾 𝑃𝑖𝑛 (1 − 𝑃𝑖𝑛 ) = 57𝜇𝑊
   dove Pin=0.2
4) Ricordare che per il MOSFET di tipo n il source è il potenziale più basso, mentre per quello
   di tipo p è il più alto. Quindi
         VDS        VGS      regione                       corrente
     a   2V         1V       saturo                        54A
     b   0.1V       0.5V     confine saturo/triodo         1.5A
     c   2V         0.5V     saturo                        1.5A
     d   -0.4V      -0.5V    saturo                        0.75A
     e   -0.6V      -0.6V    saturo                        3A


   Nel caso del pMOS i valori delle tensioni sono negativi, ma vengono inseriti come positivi
   nella formula della corrente dato che VSD=-VDS e VSG=-VGS.
