---
fonte: "soluzione_17_luglio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica del 17 luglio
                          2014, parte digitale

1) Essendoci l’invertitore, F=PD; lo schema risultante è il seguente:




   dove il PU non è banalmente il duale, dato che se facciamo la serie dei paralleli tra pMOS
   controllati da A e B, e C e Ā, solo due percorsi sono possibili, non potendo essere A e Ā
   contemporaneamente a zero.
2) La scarica del gate CMOS avviene sempre tramite due nMOS in serie, mentre la carica su
   pMOS in serie. Nel primo caso il fattore di forma equivalente è Sn,eq=1/2, mentre nel
   secondo Sp,eq=1; però gli nMOS hanno ’ doppio dei pMOS. Possiamo scrivere
            2𝐶                           2𝐶𝐿                      2𝐶                 2𝐶𝐿
    𝑡𝑡𝑜𝑡 = 𝛽′ 𝑉𝑖𝑛𝑣 𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + 𝛽′ 𝑆           𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = 𝛽′ 0.5𝑖𝑛𝑣 𝐹 + 𝛽′ 𝑆           𝐹
            𝑝 𝐷𝐷                   𝑛 𝑛,𝐼𝑁𝑉 𝑉𝐷𝐷                   𝑛     𝑉
                                                                       𝐷𝐷      𝑛 𝑛,𝐼𝑁𝑉 𝑉𝐷𝐷


   dove F=2.2 e 𝐶𝑖𝑛𝑣 = 𝑆𝑛,𝐼𝑁𝑉 (1 + 𝜀)(𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 𝑆𝑛,𝐼𝑁𝑉 (1 + 𝜀)𝐶𝑀1 è la
   capacità di ingresso del invertitore. Coi valore numerici, 𝐶𝑀1 = 1.125𝑓𝐹, Con la
   minimizzazione si ottiene
                                                       𝐶𝐿
                                    𝑆𝑛,𝐼𝑁𝑉 = √                 = 3.85.
                                                  2(1 + 𝜖 )𝐶𝑀1
3) Dalla 𝑆𝑛,𝐼𝑁𝑉 appena trovata segue che 𝐶𝑖𝑛𝑣 = 13𝑓𝐹. Il ritardo è lo stesso per ogni
   configurazione e non fa differenza tra carica e scarica (vedi commento al punto sopra). Segue
   che:
                          2𝐶𝑖𝑛𝑣                     2𝐶𝐿
                 𝑡𝑡𝑜𝑡 =    ′
                                 𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′            𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = 573𝑝𝑠.
                          𝛽𝑝 𝑉𝐷𝐷               𝛽𝑛 𝑆𝑛,𝐼𝑁𝑉 𝑉𝐷𝐷

4) La potenza dinamica è data da:
                                                  2
                                𝑃𝑑 = (𝐶𝐿 + 𝐶𝑖𝑛𝑣 )𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝐹 (1 − 𝑃𝐹 ).
   infatti se si scarica CL, vuol dire che si carica Cinv e viceversa. I due addendi nella formula
   F=AC+ĀB sono mutualmente esclusivi, quindi 𝑃𝐹 = 𝑃𝐴 𝑃𝐶 + (1 − 𝑃𝐴 )𝑃𝐵 = 0.4. Otteniamo
   quindi Pd=32.5W
