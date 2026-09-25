---
fonte: "soluzione_140716.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                          del 14 luglio 2016, parte digitale

1) Essendo ad area minima, abbiamo:
                                      𝐶𝑖𝑛 = (1 + 𝜀)𝐶𝑚1 =2.5fF


     dove: 𝐶𝑚1 = (𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 0.83𝑓𝐹. Mentre per il ritardo:
                                           2𝐶𝑖𝑛
                                  𝑡𝑝0 =           𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = 13.7𝑝𝑠
                                          𝛽𝑛′ 𝑉𝐷𝐷
     con F=1.99
2) Ogni singolo invertitore ritarda tp0 per il rapporto tra la capacità di carico e quella di ingresso;
   il ritardo totale è quindi:
                                                       𝑢   𝐶𝐿
                                      𝑡𝑝 = 𝑡𝑝0 (4 +      +    )
                                                       4 𝑢𝐶𝑖𝑛
     ponendo dtp/du=0 si trova

                                                  4𝐶𝐿
                                            𝑢=√       = 12.7
                                                  𝐶𝑖𝑛

3) Con il valore di u appena trovato si ottiene tp=142ps
4) Ognuna delle capacità commuta ad ogni fronte dell’onda quadra, quindi
                                                     2
                            𝑃𝐷 = (4𝐶𝑖𝑛 + 𝑢𝐶𝑖𝑛 + 𝐶𝐿 )𝑉𝐷𝐷 𝑓𝐶𝐾 = 46𝜇𝑊
5)
                      |VGS| [V]      |VDS| [V]                     corrente [A]
                  a        1               1            saturo          84.5
                  b        1              0.1           triodo           24
                  c        0               2            spento            0
                  d       0.5             0.5           saturo          2.25
                  e       0.6             1.6           saturo          6.25
