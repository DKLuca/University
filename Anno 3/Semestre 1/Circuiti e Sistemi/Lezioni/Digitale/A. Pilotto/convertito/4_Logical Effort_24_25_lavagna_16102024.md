---
fonte: "4_Logical Effort_24_25_lavagna_16102024.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

CIRCUITI
                                                ELECTRONIC    E SISTEMI
                                                           CICUITS FOR HIGH       1
                                                                         ELETTRONICI
                                                                            FREQUENCIES

                                 Sensibilità a numero stadi
❑ Cosa accade al ritardo quando ci si discosta dalla condizione di ottimo per il numero di stadi o per i
  dimensionamenti?
            ෡ il numero ottimo di stadi (con 𝑁
❑ Definiamo 𝑁                                ෡ ∈ 𝑅) e supponiamo che il numero di stadi usato sia N = s𝑁
                                                                                                       ෡

❑ Semplifichiamo i calcoli assumendo stadi con stesso parasitic effort



❑ Ritardo ottimo                                            ❑ Ritardo non-ottimo
                     ෡
                     𝑁                                                              𝑁
        ෡ =𝑁
    𝑡𝑎𝑑 𝑁  ෡                  ෡ 𝜌+𝑝
                         𝐹+𝑝 =𝑁                                      𝑡𝑎𝑑 𝑁 = 𝑁          𝐹+𝑝




                                                                                                       1
     CIRCUITI
ELECTRONIC    E SISTEMI
           CICUITS FOR HIGH       2
                         ELETTRONICI
                            FREQUENCIES



                      𝑝=1       𝜌 = 3.53
                      𝑝=2       𝜌 = 4.24




                                           2
                                CIRCUITI
                           ELECTRONIC    E SISTEMI
                                      CICUITS FOR HIGH       3
                                                    ELETTRONICI
                                                       FREQUENCIES



                                           s         r
    𝑝=1         𝜌 = 3.53
                                         0.40       2.16
                                         0.50       1.49
                                         0.66       1.12
                                         0.88       1.01
                                           1        1.00
                                         1.17       1.02
                                          1.5       1.10
                                          2.0       1.27
                                          2.5       1.46

0.2 0.3   0.5        2     3

                                                                     3
                      CIRCUITI
                 ELECTRONIC    E SISTEMI
                            CICUITS FOR HIGH       4
                                          ELETTRONICI
                                             FREQUENCIES


                                ෡ = 𝑙𝑛𝐹 Τ𝑙𝑛𝜌
                                𝑁
𝑝=1   𝜌 = 3.53




                                                           4
                                                   CIRCUITI
                                              ELECTRONIC    E SISTEMI
                                                         CICUITS FOR HIGH       5
                                                                       ELETTRONICI
                                                                          FREQUENCIES

                           Sensibilità ai dimensionamenti
                 ෡ sia intero
❑ Supponiamo che 𝑵
❑ Supponiamo anche che in uno degli stadi sia presente un dimensionamento diverso da quello ottimo
  (limiti tecnologici, …)




                                                                                                     5
                                                        CIRCUITI
                                                   ELECTRONIC    E SISTEMI
                                                              CICUITS FOR HIGH       6
                                                                            ELETTRONICI
                                                                               FREQUENCIES

                                 Sensibilità ai dimensionamenti
❑ Gli 𝑁 − 2 stadi conservano lo stage effort ottimo 𝐹 1Τ𝑁෡                       𝑝𝐼𝑁𝑉 = 1     𝜌 = 3.53
❑ Assumendo tutti uguali i parasitic effort                                      𝑝𝐼𝑁𝑉 = 2     𝜌 = 4.24

                             ෡
                             𝑁
       𝑡ෞ              ෡
        𝑎𝑑 = 𝑡𝑎𝑑 𝑠=1 = 𝑁         𝐹+𝑝                                                          𝑁=3

     mentre
                                              ෡
                                              𝑁
                        ෡
                        𝑁              ෡
                                       𝑁       𝐹                                                    𝑁=6
               ෡−2
       𝑡𝑎𝑑 𝑠 = 𝑁                ෡ +𝑠 𝐹+
                            𝐹 + 𝑁𝑝
                                              𝑠



          𝑡𝑎𝑑 𝑁     𝑁𝜌  ෡ − 2𝜌 + 𝜌𝑠 + 𝜌
                    ෡ + 𝑁𝑝
     𝑟=         =                     𝑠
              ෡
          𝑡𝑎𝑑 𝑁             ෡ + 𝑁𝑝
                            𝑁𝜌  ෡

                             𝜌
                        𝜌𝑠 + 𝑠 − 2𝜌
                 =1+
                            ෡ 𝜌+𝑝
                            𝑁                                Sensibilità modesta in caso di              6
                                                             dimensionamenti non ottimali
                                                          CIRCUITI
                                                     ELECTRONIC    E SISTEMI
                                                                CICUITS FOR HIGH       7
                                                                              ELETTRONICI
                                                                                 FREQUENCIES

                     Calibrazione del modello del logical effort
La calibrazione del modello consiste nell’e t azione di 𝑡𝑝0
e 𝑝𝑖𝑛𝑣 basata sulla simulazione del comportamento                          𝑡𝑝,𝑖𝑛𝑣 = 𝑡𝑝0 𝑔ℎ + 𝑝𝑖𝑛𝑣
dell’inve tito e al variare della capacità di carico (quindi
dell’electrical effort h), attraverso un’adeguata struttura di
test.

                              Non è il circuito adatto per calibrare il modello del logical effort.
                              Soluzione migliore: caricare l’inve tito e con invertitori identici.
                              h corrisponde al numero di stadi connessi all’u cita del gate il
                              cui ritardo intendiamo caratterizzare
                                 𝑡𝑝,𝑖𝑛𝑣 [ps]


                                                                   ❑ 𝑡𝑝0 ∶ pendenza della retta interpolatrice
                                                                   ❑ 𝑝𝑖𝑛𝑣 𝑡𝑝0 ∶inte cetta con l’a e ve ticale
                                                             𝑡𝑝0
                           𝑡𝑝0 × 𝑝𝑖𝑛𝑣

                                                                                                                 7
                                                            CIRCUITI
                                                       ELECTRONIC    E SISTEMI
                                                                  CICUITS FOR HIGH       8
                                                                                ELETTRONICI
                                                                                   FREQUENCIES

    struttura di test necessaria alla calibrazione del modello
                                 𝑡𝑝

                                                                    ❑ Tengo conto del tempo di transizione in ingresso
    a               a             a             a                   ❑ Capacità prodotte dai transistori variano con le
                                                                      tensioni

                                                                    ❑ Gate «a» sono quelli lungo i quali si propaga il
                                                                      ritardo
              b              b            b               b         ❑ Gate «b» forniscono (h-1) degli h gate di carico
                                                                      per i gate «a»
                                                                    ❑ I gate «c» servono a fare in modo che le uscite
                                                                      dei gate «b» non commutino troppo velocemente
          c              c            c               c               → la presenza di questi gate è necessaria per
                                                                      rallentare il transitorio all’u cita del gate «b» che
                                                                      per effetto Miller potrebbe comportare errori non
                                                                      trascurabili nella stima del ritardo (a causa
                                                                      dell’effetto Miller una rapida variazione della
                                                                      tensione all’u cita di un gate ne aumenta la
primi due stadi forniscono                    il quarto stadio
                                                                      capacità di ingresso)
una pendenza «realistica» dei                 fornisce      una
fronti in ingresso al DUT                     capacità di carico
(Device Under Test)                           «realistica»     al
                                                                                                                         8
                                              DUT stesso.
                                CIRCUITI
                           ELECTRONIC    E SISTEMI
                                      CICUITS FOR HIGH       9
                                                    ELETTRONICI
                                                       FREQUENCIES

struttura di test necessaria alla calibrazione del modello




                     Circuito di test per h=2                        9
                                CIRCUITI
                           ELECTRONIC    E SISTEMI
                                      CICUITS FOR HIGH       10
                                                    ELETTRONICI
                                                       FREQUENCIES

struttura di test necessaria alla calibrazione del modello




                                                                     10
                    Circuito di test per h=4
                                         CIRCUITI
                                    ELECTRONIC    E SISTEMI
                                               CICUITS FOR HIGH       11
                                                             ELETTRONICI
                                                                FREQUENCIES


Modello pMOS       Modello nMOS                NMOS:            PMOS:
                                               L=0.35u,         L=0.35u,
+VTO=-0.4 [V]       +VTO=0.4 [V]
                                               W=0.35u,         W=0.7u,
+KP=200e-6 [A/V^2] +KP=400e-6 [A/V^2]
+GAMMA=0.5 [V^1/2] +GAMMA=0.5 [V^1/2]
+PHI=0.9 [V]        +PHI=0.9 [V]
+NSUB=6e17 [cm-3]   +NSUB=6e17 [cm-3]
+LAMBDA=0.05 [V^-1] +LAMBDA=0.05 [V^-1]
+TOX=4e-9 [m]       +TOX=4e-9 [m]                      𝑝𝑠
+CGSO=8e-10 [F/m]   +CGSO=8e-10 [F/m]
+CGDO=8e-10 [F/m]   +CGDO=8e-10 [F/m]
+CJ=2e-3[F/m^2]     +CJ=2e-3[F/m^2]                                           →       da
+PB=1 [V]           +PB=1 [V]                                                     simulazioni
+MJ=0.5             +MJ=0.5

                                                                              →
                                                                                  da teoria




                                                                                      11
                                                 CIRCUITI
                                            ELECTRONIC    E SISTEMI
                                                       CICUITS FOR HIGH       12
                                                                     ELETTRONICI
                                                                        FREQUENCIES

                           struttura di test non ottimale

                                  ❑ In questo caso 𝐶𝑜𝑢𝑡 corrisponde a 𝐶𝑖𝑛 per ℎ = 1
                                  ❑ Valori di ℎ > 1 vengono ottenuti aumentando il valore della
                                    capacità di uscita




                                  ❑ Si ottengono i seguenti valori:

                  𝑡𝑝0 ≅ 4.5𝑝𝑠 (con precedente struttura di test avevamo ottenuto 𝑡𝑝0 ≅ 12 𝑝𝑠)
                  𝑝𝑖𝑛𝑣 ≅ 1.33 (con precedente struttura di test avevamo ottenuto 𝑝𝑖𝑛𝑣 ≅ 0.75 )


𝑡𝑝0 piccolo significa poca dipendenza di 𝑡𝑝 da ℎ → dovuto al fatto che l’aumento del carico non
influisce sulla forma d’onda del fronte di ingresso (che rimane ideale)
                                                                                                 12
