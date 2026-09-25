---
fonte: "soluzione_150217.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                       del 15 febbraio 2017, parte digitale

1) Siamo in presenza di una logica a pass-transistor con 𝐹 = 𝐴̅𝐵 + 𝐴𝐵̅ . Infatti quando A=1 è
   attivo il MOS di tipo n e porta 𝐵̅ sull’uscita; quando invece A=0, si attiva il pMOS e porta B
   in uscita
2) Il transistore nMOS è in grado di scaricare fino a 0, ma carica solo fino a V DD-VT. Il pMOS,
   da parte sua, carica fino a VDD ma scarica solo fino a VT. Abbiamo quindi:
                            A          B           F
                            0          0           VT       scarica il
                                                              pMOS
                            0        VDD          VDD        carica il
                                                              pMOS
                          VDD          0         VDD-VT      carica il
                                                              nMOS
                          VDD        VDD            0       scarica il
                                                              nMOS


3) Per prima cosa calcoliamo il ritardo di un invertitore ad area minima che carica se stesso:
                                           2𝐶𝑖𝑛𝑣      𝑉𝑇
                                  𝑡𝑝0 =     ′
                                                  𝐹(     ) = 13.7𝑝𝑠
                                           𝛽𝑛 𝑉𝐷𝐷    𝑉𝐷𝐷
   dove F=1.98, 𝐶𝑖𝑛𝑣 = (1 + 𝜀)𝐶𝑚1 = 2.48𝑓𝐹 e 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.83𝑓𝐹.
   Passando poi al buffer, i primi 3 stadi pilotano una capacità che è il triplo della loro capacità
   di ingresso, mentre il quarto (che ha capacità di ingresso 33Cinv) pilota CL. Abbiamo quindi:
                                                        𝐶𝐿
                                𝑡𝑡𝑜𝑡 = 3 ∙ 23 + 𝑡𝑝0          = 327𝑝𝑠
                                                      27𝐶𝑖𝑛𝑣
4) Avendo in ingresso un’onda quadra, tutti gli invertitori commutano ad ogni ciclo di clock e
   caricano/scaricano la capacità a valle; quindi:
                                                           2
                    𝑃 = (3𝐶𝑖𝑛𝑣 + 9𝐶𝑖𝑛𝑣 + 27𝐶𝑖𝑛𝑣 + 𝐶𝐿 )𝑓𝐶𝐾 𝑉𝐷𝐷 = 355𝜇𝑊
