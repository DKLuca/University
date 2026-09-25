---
fonte: "soluzione_2_luglio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                   2 luglio 2013
                                   parte digitale
1. si puó partire dal PU applicando la doppia negazione F = A B + A C + B C, che significa mettere
   in parallelo 3 rami composti da 2 pMOS in serie; il PD é il duale, come si vede in figura:
                                                                      Vdd

                                         A        C           A


                                         B        B           C




                                              A           B


                                              C           B


                                              A           C




2. ogni ingresso va a 2 pMOS e 2 nMOS, quindi C in = CM 1 2(Sn + Sp ), dove
   CM 1 = (L2M IN Cox + 2CGSO LM IN )=0.52fF.
   Nella scarica di caso peggiore abbiamo due nMOS in parallelo, in serie con la serie di altri 2, quindi
   Seq,S = (2/5)Sn .
   Nella carica di caso peggiore abbiamo due pMOS in parallelo, quindi S eq,C = Sp /2.
   Imporre uguali i tempi di salita e di discesa significa β n0 (2/5)Sn = βp0 Sp /2, quindi Sp = (4/5)Sn
   con  = βn0 /βp0 =2.
   Quindi: Cin = Sn CM 1 2(1 + (4/5)2). Segue che Sn =1 e Sp = (8/5)Sn =1.75.

3. inv1 carica la capacitá di ingresso di inv2 che é C inv2 = Sn,inv2 CM 1 (1 + ) mentre inv2 carica CL .
   Quindi:
                                                2Cinv2            2CL
                                  τinv1+inv2 = 0       F+ 0                 F
                                               βn VDD        βn Sn,inv2 VDD
   dove F = 2.2. La minimizzazione ponendo dτ inv1+inv2 /dSn,inv2 =0 fornisce
                                                      s
                                                              CL
                                       Sn,inv2 =                       = 4.4
                                                          CM 1 (1 + )

4. per la scarica abbiamo
                                                2Cinv1
                                      τf =                F + τinv1+inv2
                                             βn Seq,S VDD
                                              0

   dove Cinv1 = CM 1 (1 + ). Mentre per la carica
                                                 2Cinv1
                                      τr =                 F + τinv1+inv2
                                             βp0 Seq,C VDD

   Abbiamo 4 casi:

      • ingressi con due ’1’: é il caso peggiore del punto 2 sopra, quindi S eq,C = Sp /2; troviamo
        τ =191ps;
      • ingressi con due ’0’: anche questo é il caso peggiore del punto 2 sopra, quindi S eq,S = (2/5)Sn ;
        troviamo τ =191ps;
      • tutti gli ingressi a ’1’: abbiamo S eq,C = (3/2)Sp ; troviamo τ =165ps;
      • tutti gli ingressi a ’0’: abbiamo S eq,S = (2/3)Sn ; troviamo τ =175ps.
