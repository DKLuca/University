---
fonte: "soluzione_260117.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                       del 26 gennaio 2017, parte digitale

1) Siamo in presenza di una logica a pass-transistor con 𝐹 = 𝐴̅𝐵 + 𝐴𝐵̅ .
2) Essendo una logica a pass-transistor con solo il transistore di tipo n, siamo in grado di
   scaricare CL fino a 0V, ma possiamo caricarlo solo fino a VDD-VT . Abbiamo quindi:
                                   A        B           F
                                   0        0           0
                                   0      VDD       VDD-VT
                                  VDD       0       VDD-VT
                                  VDD     VDD           0
3) L’unico caso in cui la porta preleva energia dall’alimentazione per caricare C L è quando
   abbiamo A=0 e B=1 (cioè con probabilità 𝑃𝐴̅𝐵 = 0.25) dato che in tutti gli altri casi non c’è
   percorso tra VDD e CL. Va però aggiunto che il prelievo è necessario solo quando CL è
   scarica (cioè con probabilità 𝑃𝐹=0 = 0.5). Quindi:
                          𝑃𝐷 = 𝐶𝐿 𝑉𝐷𝐷 (𝑉𝐷𝐷 − 𝑉𝑇 )𝑓𝑃𝐹=0 𝑃𝐴̅𝐵 = 3.26𝜇𝑊
                    2
   dove il termine 𝑉𝐷𝐷 è stato sostituito da 𝑉𝐷𝐷 (𝑉𝐷𝐷 − 𝑉𝑇 ) dato che la carica si ferma a VDD-VT




4) Per prima cosa calcoliamo il ritardo di un invertitore ad area minima che carica se stesso:
                                         2𝐶𝑖𝑛𝑣      𝑉𝑇
                                 𝑡𝑝0 =    ′
                                                𝐹(     ) = 13.7𝑝𝑠
                                         𝛽𝑛 𝑉𝐷𝐷    𝑉𝐷𝐷
   dove F=1.98, 𝐶𝑖𝑛𝑣 = (1 + 𝜀)𝐶𝑚1 = 2.48𝑓𝐹 e 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.83𝑓𝐹.
   Passando poi al buffer, i primi 3 stadi pilotano una capacità che è il doppio della loro capacità
   di ingresso, mentre il quarto (che ha capacità di ingresso 8C inv) pilota CL. Abbiamo quindi:
                                                       𝐶𝐿
                              𝑡𝑡𝑜𝑡 = 3 ∙ 2𝑡𝑝0 + 𝑡𝑝0         = 771𝑝𝑠
                                                      8𝐶𝑖𝑛𝑣
