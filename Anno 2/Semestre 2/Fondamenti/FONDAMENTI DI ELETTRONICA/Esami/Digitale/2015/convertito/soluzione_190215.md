---
fonte: "soluzione_190215.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                          del 19 febbraio 2015, parte digitale

1) La famiglia logica è np-CMOS, detta anche NORA. I due blocchi n implementano NAND
   a 2 ingressi, ma anche il blocco p è un NAND. La funzione logica è quindi F= AB+ĀC.
2) Il ritardo complessivo è il ritardo di un blocco n (hanno entrambi lo stesso ritardo e non
   commutano mai insieme) che carica il transistore 10 (o 11, non fa differenza) del blocco p,
   a cui va aggiunto il tempo richiesto dal blocco p per caricare la CL. Quindi:
                                 2𝐶𝑖𝑛,10                     2𝐶𝐿
                      𝑡𝑝 =                𝐹(𝑉𝑇 /𝑉𝐷𝐷 ) +               𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                    1                       1
                                𝛽𝑛′ 3 𝑉𝐷𝐷               𝛽𝑝′ 2 𝑆10 𝑉𝐷𝐷

dove 𝐶𝑖𝑛,10 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 )𝑆10. Si noti che il ritardo del blocco n è stato calcolato
considerando la scarica attraverso la serie di 3 nMOSFET ad area minima, mentre il ritardo del
blocco p è la carica attraverso 2 pMOSFET entrambi con fattore di forma S10. Derivando rispetto
ad S10 e ponendo la derivata a zero, troviamo:

                                                 𝛽𝑛 ′
                                                  2𝐶𝐿
                                   √             𝛽𝑝 ′
                             𝑆10 =                             = 14.9
                                    3(𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 )

3) Col valore di S10 si cui sopra troviamo tp=720ps
4) Quando il clock è basso i blocchi n sono in pre-carica, mentre i blocchi p sono in pre-
   scarica. La durata minima di questa fase è quindi il massimo trai seguenti tempi:
                      2𝐶𝑖𝑛,10               2𝐶𝐿
       𝑡𝑝𝑟𝑒 = 𝑚𝑎𝑥 {    ′
                              𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ), ′     𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )} = 𝑚𝑎𝑥 {240𝑝𝑠, 1.3𝑛𝑠} = 1.3𝑛𝑠
                      𝛽𝑝 𝑉𝐷𝐷               𝛽𝑛 𝑉𝐷𝐷

   dove 𝐶𝑖𝑛,10 = 8.9𝑓𝐹

5) Ogni blocco n (NAND) scarica la sua capacità di carico Cin,10 in media ogni 4 cicli, mentre
   il blocco p dissipa nella pre-scarica a valle di una carica della CL tramite il blocco p. Quindi

                                  2
                                           1
                            𝑃𝑑 = 𝑉𝐷𝐷 𝑓𝑐𝑘 (2 𝐶𝑖𝑛,10 + 𝑃𝐹 𝐶𝐿 ) = 12.3𝜇𝑊.
                                           4
               11    11     1
   dove 𝑃𝐹 = 2 2 + 2 2 = 2
