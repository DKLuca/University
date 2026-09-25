---
fonte: "soluzione_29012019.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                                       29 gennaio 2019 parte digitale

1)   Si tratta di una porta logica di tipo np-CMOS. Il primo blocco implementa la funzione 𝐴̅ ∙ 𝐵̅. Il
     secondo blocco produce la funzione 𝐹 = ̅̅̅̅̅̅̅̅̅̅
                                              𝐶 ∙ 𝐴̅ ∙ 𝐵̅ = 𝐶̅ + 𝐴 + 𝐵.

2)   Dato che iniziamo la fase di valutazione col nodo F già a V DD, il caso peggiore nella fase di
     valutazione è legato alla scarica della capacità C L. Esiste solo un caso, però, in cui CL viene scaricata,
     cioè quando A=B=0 e C=1, per cui tale caso è quello peggiore.
     Il tempo di ritardo si calcola come:

                                         2𝐶𝑋                         2𝐶𝐿
                        𝑡𝑣𝑎𝑙 =                   𝐹 (𝑉𝑇 /𝑉𝑑𝑑 ) + ′              𝐹 (𝑉𝑇 /𝑉𝑑𝑑 )
                                 𝛽′    (𝑆 /3)𝑉𝐷𝐷
                                      𝑝 𝑝
                                                               𝛽 𝑛 (𝑆𝑋 /3) 𝑉𝐷𝐷

     dove 𝐶𝑋 = 𝑆𝑋 𝐶𝑚1 è la capacità di ingresso del transitore nMOSFET del pull-down del secondo stadio,
     e 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 1𝑓𝐹.

     Minimizzando tval in funzione di SX, otteniamo:

                                                           𝛽′ 𝑝 𝐶𝐿
                                                  𝑆𝑥 = √ ′      = 10
                                                        𝛽 𝑛 𝐶𝑚1

3)   Sfruttando la formula per il tempo di ritardo che abbiamo scritto sopra, otteniamo che tval = 882 ps
     visto che la funzione F(VT/Vdd) = 2.2. Come detto sopra, A=B=0 e C=1è l’unico caso in cui la capacità
     CL viene scaricata durante la fase di valutazione.

4)   Il tempo di pre-carica del secondo stadio si calcola velocemente come:

                                                    2𝐶𝐿
                                         𝑡𝑝2 =              𝐹 (𝑉𝑇 /𝑉𝑑𝑑 ) = 2.9 𝑛𝑠
                                                 𝛽′𝑝 𝑆𝑝 𝑉𝐷𝐷

     mentre, per il primo stadio, otteniamo un tempo di pre-scarica pari a:

                                                   2𝐶𝑋
                                        𝑡𝑝1 =              𝐹 (𝑉𝑇 /𝑉𝑑𝑑 ) = 73.5 𝑝𝑠
                                                𝛽′𝑛 𝑆𝑛 𝑉𝐷𝐷

5)   Il secondo stadio scarica la capacità CL solo quando A=B=0 e C=1, cioè quando F=0. Inoltre, il
     primo stadio carica la capacità CX solo quando A=0 e B=0. Per cui, sapendo che P(F=0)=1/8, mentre
     P(A=0,B=0)=1/4, otteniamo che la potenza dinamica dissipata vale:
                                          2                   2
                                 𝑃𝑑 = 𝐶𝐿 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃(𝐹=0) + 𝐶𝑋 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃(𝐴=0,𝐵=0) = 22 𝜇𝑊
