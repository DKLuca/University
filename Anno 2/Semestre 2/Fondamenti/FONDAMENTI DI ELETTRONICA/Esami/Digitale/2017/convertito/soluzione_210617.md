---
fonte: "soluzione_210617.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                             21 giugno 2017 parte digitale

1) Guardando la rete di pull-down si vede subito che 𝐹 = ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
                                                                  𝐸(𝐴𝑆 + 𝐵𝑆̅); usando più volte
   DeMorgan, 𝐹 = 𝐸̅ + 𝐴̅𝐵̅ + 𝐴̅𝑆 + 𝐵̅𝑆̅. Il termine 𝐴̅𝐵̅ è ridondante rispetto a 𝐴̅𝑆̅ + 𝐵̅𝑆̅. Si vede
                                    ̅
   che questa seconda relazione corrisponde alla funzione implementata dalla rete di pull-up.
2) Per valutare i tempi di salita o di discesa bisogna usare l’equazione
                                                   2𝐶𝐿
                                      𝑡𝐹,𝑅 =                 𝐹 (𝑉𝑇 /𝑉𝑑𝑑 )
                                               𝛽′𝑛,𝑝 𝑆𝑒𝑞 𝑉𝐷𝐷

   dove usiamo 𝛽′𝑛 o 𝛽′𝑝 se stiamo calcolando il tempo di discesa o quello di salita. Essendo
   F=1.99, abbiamo
                                        275𝑝𝑠         550𝑝𝑠
                                   𝑡𝐹 =          𝑡𝑅 =
                                          𝑆𝑒𝑞          𝑆𝑒𝑞

   I risultati sono riportati in tabella.
                        E     S   A    B       tR [ps]    tF [ps]      Seq
                        1     0   X    1           /       825         1/3
                        1     0   X    0        1100          /        1/2
                        1     1   1    X           /       825         1/3
                        1     1   0    X        1100          /        1/2
                        0     0   X    1         550          /         1
                        0     0   X    0         367          /        3/2
                        0     1   1    X         550          /         1
                        0     1   0    X         367          /        3/2


3) Essendo una logica statica CMOS:
                                               2
                                      𝑃𝑑 = 𝐶𝐿 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝐹 (1 − 𝑃𝐹 )
   risulta semplice calcolare 1 − 𝑃𝐹 = 𝑃𝐸 [𝑃𝑆 𝑃𝐴 + (1 − 𝑃𝑆 )𝑃𝐵 ] = 0.15

   che fornisce Pd=6.2W
4) Conviene tenere E nella parte finale dell’albero e poi usare S per selezionare A o B:
