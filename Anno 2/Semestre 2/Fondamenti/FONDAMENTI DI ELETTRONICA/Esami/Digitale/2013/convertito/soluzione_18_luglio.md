---
fonte: "soluzione_18_luglio.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                   18 luglio 2013
                                   parte digitale
1. essendoci l’invertitore, F=PD; la topologia del PD é quindi quella indicata di seguito:


                                          ck
                                                                                 F

                                   A           C        A


                                   B           B        C


                                               ck




2. ogni ingresso va a 2 nMOS, quindi C in = CM 1 2Sn , dove CM 1 = (L2M IN Cox + 2CGSO LM IN )=0.52fF.
   Essendo Sn =1, abbiamo Cin =1.05fF

3. Nella scarica di caso peggiore abbiamo due nMOS in serie, a loro volta in serie al transistore di
   clock, tutti con Sn =1; quindi Seq = 1/3. Questi devono caricare la Cinv = Sn,inv CM 1 (1 + ) (con
    = βn0 /βp0 ) mentre l’invertitore carica CL . Quindi:
                                                                                                        !
                    2Cinv         2CL             2F                                            CL
              τ= 0          F+ 0            F = 0                        3CM 1 (1 + )Sn,inv +
                βn (1/3)VDD   βp Sp,inv VDD    βn VDD                                          Sn,inv

   dove F = 2.2. La minimizzazione ponendo dτ /dS n,inv =0 fornisce
                                                       s
                                                               CL
                                        Sn,inv =                         = 2.5
                                                           3CM 1 (1 + )

   da cui Cinv =4.0fF;

4. il ritardo vale
                                              2Cinv         2CL
                                    τ=                F+ 0            F
                                           βn Seq VDD
                                            0           βn Sn,inv VDD
   Abbiamo 2 casi:

      • ingressi con due ’1’: é il caso peggiore del punto 3 sopra, quindi S eq = 1/3; troviamo τ =262ps;
      • tutti gli ingressi a ’1’: nel PD abbiamo il parallelo di 3 serie da 2 transistori, in serie col
        transistore di clock; quindi Seq = 1/(1/(3/2) + 1/1) = 3/5; troviamo τ =204ps;

5. il pMOS di clock carica Cinv , quindi:
                                                    2Cinv        2CL
                                       τpre =              F+ 0            F
                                                    βp VDD
                                                     0       βn Sn,inv VDD

   (essendo Sp = 1) che fornisce τpre =218ps;

6. CL e Cinv commutano insieme: una si carica e l’altra si scarica. Il processo lo si innesca se abbiamo
   una scarica indotta dal PD. Questo avviene col 50% delle configurazioni degli ingressi. Quindi
                                                    2
                                   P = (Cinv + CL )VDD fck 0.5 = 34µW
