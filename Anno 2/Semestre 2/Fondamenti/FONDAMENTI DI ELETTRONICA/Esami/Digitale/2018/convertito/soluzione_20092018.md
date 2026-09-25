---
fonte: "soluzione_20092018.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                                      20 settembre 2018 parte digitale
1)   Si tratta di una porta logica di tipo domino. Il blocco p implementa la funzione 𝐴 + 𝐵̅ ∙ 𝐶̅ . A valle
     dell’invertitore abbiamo quindi 𝐹 = ̅̅̅̅̅̅̅̅̅̅̅̅
                                            𝐴 + 𝐵̅ ∙ 𝐶̅ = 𝐴̅ ∙ (𝐵 + 𝐶).
2)   Il caso peggiore lo si ha quando A=B=C=0 e quindi il pull-up realizzato a pMOS deve caricare la
     capacità d’ingresso dell’invertitore. Questa prima operazione vede 3 pMOS in serie. Il ritardo
     complessivo vale quindi:
                           2𝐶𝑖𝑛𝑣                       2𝐶𝐿
                   𝑡𝑝 =       1    𝐹 (𝑉𝑇 /𝑉𝑑𝑑 ) +               𝐹 (𝑉𝑇 /𝑉𝑑𝑑 )
                          𝛽′𝑝 3𝑉𝐷𝐷                𝛽′𝑛 𝑆𝑖𝑛𝑣 𝑉𝐷𝐷
                                       2𝐶𝑚1 (1 + 𝜀)𝑆𝑖𝑛𝑣                        2𝐶𝐿
                                    =                    𝐹 ( 𝑉𝑇 /𝑉 𝑑𝑑 ) +              𝐹 (𝑉𝑇 /𝑉𝑑𝑑 )
                                           𝛽′𝑝 13𝑉𝐷𝐷                      𝛽′𝑛 𝑆𝑖𝑛𝑣 𝑉𝐷𝐷

     dove 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 1𝑓𝐹 e F=2.2.
     La minimizzazione fornisce

                                                          𝐿𝐶
                                               𝑆𝑥 = √3𝜀(1+𝜀)𝐶 =3.3
                                                               𝑚1


     Segue che 𝐶𝑖𝑛𝑣 = 10𝑓𝐹
3)   Nel caso in cui F=1, il tempo di valutazione è nullo, dato che iniziamo la fase di valutazione col nodo
     F già a VDD. Negli altri casi:
                                           2𝐶𝑖𝑛𝑣                          2𝐶𝐿
                               𝑡𝑣𝑎𝑙 =                 𝐹 (𝑉𝑇 /𝑉𝑑𝑑 ) +              𝐹 (𝑉𝑇 /𝑉𝑑𝑑 )
                                        𝛽′𝑝 𝑆𝑝,𝑒𝑞 𝑉𝐷𝐷                𝛽′𝑛 𝑆𝑖𝑛𝑣 𝑉𝐷𝐷

     dove Sp,eq è il fattore di forma equivalente del pull-up del blocco p (incluso il transistore di clock). I
          risultati sono ripostati in tabella
                    A      B      C        Sp,eq                    tval [ps]
                    0      0      0        1/3                      880
                    0      0      1        -                        0
                    0      1      0        -                        0
                    0      1      1        -                        0
                    1      0      0        1/(1+1/(1+1/2))=3/5      686
                    1      0      1        1/2                      735
                    1      1      0        1/2                      735
                    1      1      1        1/2                      735


4)   La pre-scarica di Cinv tramite un nMOS, con in seguito la carica di CL richiede un tempo:
                                     2𝐶𝑖𝑛𝑣                      2𝐶𝐿
                           𝑡𝑣𝑎𝑙 =           𝐹 (𝑉𝑇 /𝑉𝑑𝑑 ) +               𝐹(𝑉𝑇 /𝑉𝑑𝑑 ) = 514𝑝𝑠
                                    𝛽′𝑛 𝑉𝐷𝐷                𝛽′𝑝 𝜀𝑆𝑖𝑛𝑣 𝑉𝐷𝐷

5)   Spendiamo energia in valutazione quando il pull-up del blocco p deve caricare Cinv. Questo
     obbliga l’invertitore a caricare CL nel ciclo di pre-scarica successivo. La potenza dissipata vale:
                                                            2
                                          𝑃𝑑 = (𝐶𝐿 + 𝐶𝑖𝑛𝑣 )𝑉𝐷𝐷 𝑓𝑐𝑘 (1 − 𝑃𝐹 ) = 52.5𝜇𝑊
     essendo PF=3/8.
