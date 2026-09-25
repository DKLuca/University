---
fonte: "soluzione_090916.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                       del 9 settembre 2016, parte digitale

1) Il primo stadio implementa la funzione NAND tra A e B; mentre il secondo blocco fa
   l’AND tra il negato del risultato del primo blocco ed il negato dell’ingresso C.
   Quindi 𝐹 = 𝐴𝐵𝐶̅ .
2) Durante la fase di pre-scarica (clock a ‘0’), il transistore 8 scarica CL. Abbiamo
                                                  2𝐶𝐿
                                   𝑡𝑝𝑟𝑒_𝑠𝑐 =    ′
                                                         𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                               𝛽𝑛 𝑆8 𝑉𝐷𝐷
   Dove F=1.99. Per avere un tempo di 150ps serve un S8=1.84.
3) Nella fase di valutazione abbiamo la carica di CL solo per la configurazione A=B=1, C=0. Il
   ritardo complessivo è dato dalla scarica del nodo X1 (capacità di gate del transistore 6) tramite
   3 transistori n ad area minima, quindi dalla carica di CL tramite 3 transistori p (5,6 e 7) con
   fattore di forma SX. Abbiamo quindi:
                                2𝐶𝑚1 𝑆𝑋                      2𝐶𝐿
                       𝑡𝑣𝑎𝑙 =       1    𝐹 ( 𝑉𝑇 /𝑉𝐷𝐷 ) +             𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                𝛽𝑛′ 3𝑉𝐷𝐷                 𝛽𝑝′ 𝑆3𝑋 𝑉𝐷𝐷

   La capacità di ingresso del transistore 6 è data da Cm1Sx, dove 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 +
   2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.83𝑓𝐹. La minimizzazione rispetto a Sx fornisce:

                                                  𝐶𝐿 𝛽′𝑛
                                        𝑆𝑥 = √           = 11
                                                 𝐶𝑚1 𝛽′𝑝

4) Inserendo il valore di Sx nell’espressione di tval, si trova tval=301ps. L’unica configurazione
   da considerare è A=B=1, C=0. Per il tempo di precarica del nodo X1, abbiamo la carica
   della capacità di gate del transistore 6 tramite il transistore 1, di tipo p; quindi
                                        2𝐶𝑚1 𝑆𝑥
                             𝑡𝑝𝑟𝑒_𝑐 =            𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = 100𝑝𝑠
                                         𝛽𝑝′ 𝑉𝐷𝐷

5) Preleviamo energia dall’alimentazione per caricare C L ogni volta che F=1 in fase di
   valutazione, dato che poi CL viene scaricata nella fase successiva. Quindi
                                            2
                                   𝑃𝑑 = 𝐶𝐿 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝐹 = 2.02𝜇𝑊
   essendo PF=PAPB(1-PC)=1/8
