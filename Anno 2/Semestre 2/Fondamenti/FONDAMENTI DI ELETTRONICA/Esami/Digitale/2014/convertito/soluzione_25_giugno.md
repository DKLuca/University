---
fonte: "soluzione_25_giugno.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica del 25 giugno
                           2014, parte digitale

1) In logica domino, essendoci l’invertitore, F=PD; lo schema risultante è il seguente:




2) La potenza dinamica è data da:
                                                 2
                                        𝑃𝑑 = 𝐶𝐿 𝑉𝐷𝐷 𝑓𝑐𝑘 𝑃𝐹 .
   Infatti la porta dissipa potenza in precarica quando nell’ultima valutazione ha scaricato (cioè
   uscita a 1). F=AB+CDE è uno in tutti i casi eccetto quando sia AB che CDE sono zero. AB è
   uno per ¼ delle configurazioni, CDE per 1/8. Quindi PF=1-(1-1/4)(1-1/8). Troviamo
   Pd=20.6W.
3) Per trovare tp0 troviamo prima la capacità di ingresso di un invertitore ad area minima:
           𝐶𝑖 = (1 + 𝜀)(𝐶𝑂𝑋 𝐿2𝑀𝐼𝑁 + 2𝐶𝐺𝑆𝑂 𝐿𝑀𝐼𝑁 ) = 3.4𝑓𝐹.
   Abbiamo quindi:
                    2𝐶
           𝑡𝑝𝑜 = 𝛽′ 𝑉 𝑖 𝐹 (𝑉𝑇 /𝑉𝐷𝐷 ) = 37𝑝𝑠.
                   𝑛 𝐷𝐷

4) I primi 4 invertitori sono caricati con una capacità che è 3 volte la loro capacità di ingresso;
   ritardano quindi 3tpo ciascuno. L’ultimo ha come carico CL e come capacità di ingresso 34Ci.
   Otteniamo:
                              𝐶
           𝑡𝑝 = 𝑡𝑝𝑜 (3 ∙ 4 + 34𝐿𝐶 ) = 580𝑝𝑠.
                                  𝑖

5) Essendo pilotato direttamente da un clock, il buffer commuta ad ogni periodo del clock,
   quindi:
                                                   2
                                        𝑃𝑑 = 𝐶𝑡𝑜𝑡 𝑉𝐷𝐷 𝑓𝑐𝑘
   con 𝐶𝑡𝑜𝑡 = 𝐶𝐿 + 𝐶𝑖 (3 + 32 + 33 + 34 ) = 1.4𝑝𝐹. Otteniamo Pd=2.8mW.
