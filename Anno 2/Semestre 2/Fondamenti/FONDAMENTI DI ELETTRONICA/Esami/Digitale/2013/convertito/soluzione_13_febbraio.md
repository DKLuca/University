---
fonte: "soluzione_13_febbraio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                  13 febbraio 2013
                                   parte digitale
1. lo schema é rappresentato in figura:

                                                        VDD
                                       φ                               VDD
                                                    M2


                                   A                          A
                                                                                CL
                                   B                          B

                                           φ        M1




2. Il ritardo al 90% dell’invertitore é dato da:
                                                        2CL
                                           τinv =               F (VT /VDD )                          (1)
                                                    βn Sinv VDD
                                                     0


   dove F=2.2. Mentre il ritardo del (pull-down + M1) vale

                                                        2Cinv
                                           τP D =               F (VT /VDD )                          (2)
                                                    βn (1/3)VDD
                                                     0


   perché abbiamo 3 nMOS a dimensionamento S=1 in serie. Essendo

                       Cinv = (1 + α)(L2min Cox + 2Lmin CGSO )Sinv = (1 + α)Cm Sinv                   (3)

   otteniamo
                                2(1 + α)Cm Sinv                   2CL
                       τtot =                   F (VT /VDD ) + 0          F (VT /VDD )                (4)
                                  βn (1/3)VDD
                                   0                          βn Sinv VDD
   Da dτtot /dSn =0 segue che                           s
                                                               CL
                                               Sinv =                   = 2.6                         (5)
                                                            3Cm (1 + α)
   quindi il pMOS avrá S=5.2. Segue poi C inv =3.8fF.

3. la scarica avviene sempre attraverso 3 transistori, il ritardo quindi lo si calcola con Eq.4 e vale
   167ps.

4. la precarica avviene tramite il pMOS, che a W minimo, quindi:
                                2Cinv                    2CL
                      τprec =          F (VT /VDD ) + 0          F (VT /VDD ) = 139ps                 (6)
                                βp VDD
                                 0                   βn Sinv VDD

5. preleviamo energia dall’alimentazione solo in precarica se nella valutazione precedente c’é stata una
   carica; l’invertitore commuta solo se commuta la porta, quindi
                                                                   2
                                                P = f (CL + Cinv )VDD P0                              (7)

   Essendo P0 =1/2, P =34µW .
