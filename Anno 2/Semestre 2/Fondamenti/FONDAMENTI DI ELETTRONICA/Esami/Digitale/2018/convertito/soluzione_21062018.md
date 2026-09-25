---
fonte: "soluzione_21062018.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                            21 giugno 2018 parte digitale

1) Entrambi i transistori sono sopra soglia, con VGSn=VSGp=1V. La somma VDSn+VSDp=1V
   implica che uno deve essere triodo e l’altro saturo. Essendo il transistore nMOS più
   conduttivo, possiamo assumere che lui sia triodo, dato che una V DSn<0.5V potrebbe dare la
   stessa corrente del p-MOS con VSDp>0.5V (in tal caso saturo). Dall’uguaglianza delle correnti
   abbiamo quindi:
                                                              2
          ′                         2         ′ (𝑉𝑆𝐺𝑝 −𝑉𝑇 )
    𝐼 = 𝛽𝑛 [(𝑉𝐺𝑆𝑛 − 𝑉𝑇 )𝑉𝐷𝑆𝑛 − 12𝑉𝐷𝑆𝑛] = 𝛽𝑝
                                                     2

   Otteniamo un’equazione di 2° grado in VDSn. Le soluzioni sono VDSn=0.85V e 0.146V. La
   prima è chiaramente da scartare dato che non verifica l’assunzione di funzionamento nel
   nMOS in regione triodo. Alla seconda soluzione corrisponde una corrente I=18.75A.
                                                                                         𝛽′
2) La capacità di ingresso di un invertitore ad area minima vale 𝐶𝑖𝑛 = (1 + 𝛽𝑛′ ) 𝐶𝑚1 =3fF,
                                                                                          𝑝

    essendo 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 1𝑓𝐹. Abbiamo quindi
                                              2𝐶𝑖𝑛
                                     𝑡𝑝0 =             𝐹 (𝑉𝑇 /𝑉𝑑𝑑 )=22ps
                                             𝛽′𝑛 𝑉𝐷𝐷

   dato che F=2.2.
3) Il primo invertitore ed il secondo vedono come carico una capacità tripla rispetto alla loro
   capacità di ingresso; l’ultimo invertitore vede CL in uscita ed ha 9Cin come capacità in
   ingresso. Quindi
                                                                   𝐶𝐿
                                𝑡𝑝 = 3 ∙ 𝑡𝑝0 + 3𝑡𝑝0 + 𝑡𝑝0              = 295𝑝𝑠
                                                                  9𝐶𝑖𝑛
4) Ciascun invertitore commuta ad ogni ciclo di clock, quindi
                                                       2
                              𝑃𝑑 = (3𝐶𝑖𝑛 + 9𝐶𝑖𝑛 + 𝐶𝐿 )𝑉𝐷𝐷 𝑓𝑐𝑘 = 189𝜇𝑊

5) Essendoci l’invertitore, ci conviene scrivere 𝐹 = ̿̿̿̿̿̿̿̿̿
                                                         𝐴 + 𝐵𝐶 = 𝐴̅̅̅̅̅̅̅̅̅̅̅̅
                                                                     ̅(𝐵̅ + 𝐶̅ ). Quindi la rete di
   interruttori deve realizzare la funzione 𝐴̅(𝐵̅ + 𝐶̅ ). Otteniamo quindi:
