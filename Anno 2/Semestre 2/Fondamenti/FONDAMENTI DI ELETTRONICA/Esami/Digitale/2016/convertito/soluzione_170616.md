---
fonte: "soluzione_170616.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                       del 17 giugno 2016, parte digitale

1) Essendoci l’invertitore, 𝐹 = 𝑃𝐷 = 𝐴𝑆 + 𝐵𝑆̅.
2) Indipendentemente dalla configurazione degli ingressi, nel primo stadio abbiamo sempre o
   la carica attraverso 2 pMOS oppure la scarica attraverso 2 nMOS. Essendo i pMOS grandi il
   doppio degli nMOS, ma essendo  n=2p (cioè =2), il ritardo del primo stadio è sempre lo
   stesso. Il ritardo complessivo vale quindi:
                               2𝐶𝑖𝑛𝑣                     2𝐶𝐿
                      𝑡𝑝 =             𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) + ′          𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                 1                   𝛽𝑛 𝑆𝑖𝑛𝑣 𝑉𝐷𝐷
                             𝛽𝑛′ 2 𝑉𝐷𝐷

dove 𝐶𝑖𝑛𝑣 = (1 + 𝜀)𝐶𝑚1 𝑆𝑖𝑛𝑣 . In cui Sinv è il dimensionamento del transistor “10”, laddove il
transistore “9” è  volte più grande. Abbiamo: 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.83𝑓𝐹.
Ponendo dtp/dSinv=0, troviamo:

                                                   𝐶𝐿
                                   𝑆𝑖𝑛𝑣 = √               = 4.5
                                              2(1 + 𝜀)𝐶𝑚1

3) Inserendo la Sinv appena trovata nell’espressione di tp troviamo tp=246ps, dove abbiamo
   usato F=1.99 e Cinv=11.1fF. Come detto sopra, il valore del ritardo complessivo non dipende
   dalla configurazione degli ingressi
4) Quando commuta CL commuta anche Cinv (in altre parole, CL viene caricata con probabilità
   PF(1-PF) e Cinv come (1-PF)PF, che sono la stessa cosa), quindi:
                                  2
                          𝑃𝑑 = 𝑉𝐷𝐷  𝑓𝑐𝑘 (𝐶𝑖𝑛𝑣 + 𝐶𝐿 )𝑃𝐹 (1 − 𝑃𝐹 ) = 18𝜇𝑊.
              1
   dove 𝑃𝐹 = 2

5) Senza usare l’invertitore, bisogna scegliere PU=F, considerando che i pMOS negano i segnali
   sui loro gate. Il pull-down è il duale, in cui però possiamo togliere la linea “orizzontale”.
   Otteniamo:
