---
fonte: "soluzione_30_gennaio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                  30 gennaio 2013
                                   parte digitale
1. un possibile schema é rappresentato in figura:
                                           A
                                                              C
                                 A
                                           A
                                 B
                                                              C
                                                  C

2. Il ritardo al 90% dell’invertitore é dato da:
                                                          2CL
                                          τinv =                 F (VT /VDD )                            (1)
                                                      βn0 Sn VDD
   dove F=2.2. Mentre il ritardo dei pass-transistors nel caso peggiore vale
                                τpass = 2.3Req 3Ceq + 2.3 · 2Req (2Ceq + Cinv )                          (2)
   come si vede dalla figura riportata qui sotto, in cui la prima resistenza R eq deve caricare 3 ca-
   pacitá Ceq , mentre la serie delle due Req carica 2 capacitá Ceq in parallelo alla capacitá di ingresso
   dell’inverter.
                                       R eq
                                                           caso peggiore
                                     C eq Ceq           Req

                                                      Ceq Ceq        Cinv
                                                                                 C
                                                Ceq                               L

                                                            Ceq


                                                        caso migliore

                                                            Ceq      Cinv
                                                        Req                      C
                                                                                  L

                                                      Ceq Ceq


   Essendo
                                 Cinv = (1 + α)(L2min Cox + 2Lmin CGSO )Sn                               (3)
   otteniamo
                                                                       b
                               τtot = 2.3Req Ceq (3 + 4) + 2.3 · 2Req aSn +                              (4)
                                                                      Sn
                    2                                    0
   con a = (1 + α)(Lmin Cox + 2Lmin CGSO ) e b = 2CL F/(βn VDD ). Da dτtot /dSn =0 segue che
                                                      s
                                                                b
                                              Sn =                     = 4.1                             (5)
                                                          2.3 · 2Req a
3. il caso peggiore lo abbiamo giá analizzato; il ritardo vale
                                                                            b
                        τpeggiore = 2.3Req Ceq (3 + 4) + 2.3 · 2Req aSn +      = 140ps             (6)
                                                                           Sn
   Nel caso migliore invece (figura riportata poco sopra) abbiamo solo un pass-transistor che carica 2
   capacitá Ceq in parallelo alla capacitá di ingresso dell’inverter, quindi
                                                                             b
                                τigliore = 2.3 · Req (2Ceq + aSn ) +           = 90ps                    (7)
                                                                            Sn
