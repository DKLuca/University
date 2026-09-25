---
fonte: "soluzione_17_settembre.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica del 17 settembre
                             2014, parte digitale

  1) Si vede subito che F=ABCD.
  2) Nella porta NAND, nella carica di caso peggiore abbiamo un solo pMOS, mentre nella scarica
     due nMOS in serie. Essendo = ’n/’p=2, dobbiamo avere Sp,NAND=1. Ogni ingresso va ad un
     solo nMOS e un solo pMOS, quindi 𝐶𝐼𝑁 = 2𝐶𝑀1 con 𝐶𝑀1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) =
     1.125𝑓𝐹, che fornisce CIN=2.25fF
  3) Dato che per tutte le porte imponiamo tempo di salita uguale al tempo di discesa, possiamo
     semplicemente sommare i tempi di discesa. Nel caso del NAND abbiamo 2 nMOS in serie
     con Sn,NAND=1, mentre nel NOR un solo nMOS con Sn,NOR , indeterminato al momento. Quindi
                                 2𝐶𝑥                       2𝐶𝐿
                     𝑡𝑡𝑜𝑡 =       ′
                                        𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′            𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                              0.5𝛽𝑛 𝑉𝐷𝐷               𝛽𝑛 𝑆𝑛,𝑁𝑂𝑅 𝑉𝐷𝐷

     dove F=2.2. Affinchè la porta NOR abbia tempo di salita uguale al tempo di discesa di caso
     peggiore, deve essere  ’n Sn,NOR= ’p Sp,NOR/2. Quindi Cx=Cm1 Sn,NOR(1+2). Riscriviamo:
                                     2𝐹     𝐶𝑚1 (1 + 2𝜖 )𝑆𝑛,𝑁𝑂𝑅      𝐶𝐿
                           𝑡𝑡𝑜𝑡 = ′        (                    +         )
                                    𝛽𝑛 𝑉𝐷𝐷            0.5         𝑆𝑛,𝑁𝑂𝑅
     che minimizzata fornisce
                                                        𝐶𝐿
                                      𝑆𝑛,𝑁𝑂𝑅 = √                 = 3.
                                                   2(1 + 2𝜖 )𝐶𝑀1
  4) Dalla 𝑆𝑛,𝑁𝑂𝑅 appena trovata segue che 𝐶𝑥 = 16.8𝑓𝐹. Il ritardo è quindi
                            2𝐶𝑥                       2𝐶𝐿
                𝑡𝑡𝑜𝑡 =       ′
                                   𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′            𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = 740𝑝𝑠.
                         0.5𝛽𝑛 𝑉𝐷𝐷               𝛽𝑛 𝑆𝑛,𝑁𝑂𝑅 𝑉𝐷𝐷

  5) La potenza dinamica è data da:
                                  2                          2
                         𝑃𝑑 = 𝐶𝐿 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝐹 (1 − 𝑃𝐹 ) + 2𝐶𝑥 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝑥 (1 − 𝑃𝑥 ).
     con PF=1/16 e PX=3/4. Infatti CL si carica e scarica secondo la tabella della verità di un AND
     a 4 ingressi, mentre le capacità CX sono pilotate da NAND a 2 ingressi. Otteniamo quindi
     Pd=24.3W
  6) Per evitare corse critiche, la porte NAND sono realizzate con un blocco n e la porta NOR
     con un blocco p:
