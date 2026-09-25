---
fonte: "soluzione_030215.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                        del 3 febbraio 2015, parte digitale

1) Il ritardo minimo della tecnologia è dato da
                                             2𝐶𝑖𝑛
                                    𝑡𝑝0 =           𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                            𝛽𝑛′ 𝑉𝐷𝐷
dove 𝐶𝑖𝑛 = (1 + 𝜀)(𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) è la capacità di un invertitore ad area minima. Coi
parametri del nostro caso: F=2.00 e Cin=1.8fF; segue tp0=24ps.
2) I primi 3 invertitori ritardano ciascuno 2tp0, dato che pilotano carichi capacitivi che sono il
   doppio della loro capacità di ingresso; il 4° invertitore ha carico 0.5pF e capacità di ingresso
   8Cin. Quindi il ritardo totale vale:
                                                      0.5𝑝𝐹
                                𝑡𝑡𝑜𝑡 = 𝑡𝑝0 (3 ∙ 2 +         ) = 980𝑝𝑠.
                                                       8𝐶𝑖𝑛
3) Ogni inverter della catena commuta in media ogni 4 cicli di clock, quindi
                             1                            2
                      𝑃𝑑 =     (2𝐶𝑖𝑛 + 4𝐶𝑖𝑛 + 8𝐶𝑖𝑛 + 𝐶𝐿 )𝑉𝐷𝐷 𝑓𝑐𝑘 = 89𝜇𝑊.
                             4
4) I primi 2 inverter ritardano sempre 2tp0; il 3° ha una capacità di ingresso 4Cin e si trova in
   uscita la capacità del 4° stadio, che diciamo avere un dimensionamento u. Il 4° stadio ha
   capacità di ingresso uCin e come carico i 0.5pF. Quindi:
                                                      𝑢 0.5𝑝𝐹
                                  𝑡𝑡𝑜𝑡 = 𝑡𝑝0 (2 ∙ 2 + +        ).
                                                      4   𝑢𝐶𝑖𝑛
   La minimizzazione fornisce:

                                               4 ∙ 0.5𝑝𝐹
                                       𝑢=√               = 33,
                                                   𝐶𝑖𝑛

   cioè Sn=u=33 e Sp=2u=66. Il ritardo diventa: ttot=497ps.
5) I blocchi n e p possono implementare solo funzioni negate, quindi invece di fare due porte
   AND che entrano in un OR, facciamo due NAND in logica n che entrano in un altro NAND
   di tipo p:




   Attenzione al clock del blocco p, che deve essere il negato del caso n, per avere la
   valutazione contemporaneamente in tutti i blocchi.
