---
fonte: "2014_Testi_e_Soluzioni.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                      7 febbraio 2014
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Assumendo βF ≫ 1 per entrambi i transistori, determinare i valori di RB ed RC che consentono di
       polarizzare il circuito a IE,1 =10 µA e VC =-3 V essendo VC la tensione di collettore dei transistori.
       (10 punti)

    2. Supponendo di poter schematizzare la coppia Darlington con un unico transistore pnp descritto
       dalle relazioni
                                                                                  (          )
                                                                                      VBE
                                                        IC     = IS,e exp                        = βF,e IB = βF2 IB                                             (1)
                                                                                      2Vth
                                                                     √
                                                      IS,e =             βF IS,1 IS,2                                                                           (2)

         si disegni il circuito equivalente per piccolo segnale e si calcoli il valore dei parametri diﬀerenziali
         del transistore nel punto di lavoro di cui al quesito precedente. (punti 6)

    3. Supponendo di poter iniettare nel nodo B del circuito (base del transistore T1) una corrente di
       piccolo segnale avente trasformata di Laplace Ii (s), determinare l’espressione della funzione di
       trasferimento Vo (s)/Ii (s) (Vo = VC ), tracciare il corrispondente diagramma di Bode e determinare
       la corrispondente frequenza di taglio a −3 dB. (14 punti)




                                                                                           T2
                                                                  T1                                                                  C


                                      RB                                                      Rc


                                                                                                         − Vcc
Vγ,EB =0.65 V, VCC = 6 V, βF 1 = βF 2 = βF = 100, β0,1 = β0,2 = β0 = 100, Vth = 25 mV, C = 2 pF.
                Soluzione del compito di Fondamenti di Elettronica
                                 7 febbraio 2014
1. I transistori lavorano in regione normale di funzionamento. Essendo per ipotesi βF ≫ 1 otteniamo
   immediatamente:
                                     VCC − VB
                         RB ≃                     = (6 − 1.3)/(10−5 /101) ≃ 47M Ω                (1)
                                   IE,1 /(βF + 1)
                                   VCC + VC
                         RC ≃                 ≃ 3 kΩ                                             (2)
                                     βF IE,1
2. Il circuito equivalente puó essere ottenuto o con la solita metodologia. I parametri diﬀerenziali sono
                                                           Vth
                                             rbe,1 =            ≃ 250 kΩ                              (3)
                                                           IB,1
                                                           Vth
                                             rbe,2 =            ≃ 2.5 kΩ                              (4)
                                                           IE,1
                                                           2Vth
                                             rbe,e =            ≃ 500 kΩ                              (5)
                                                            IB
3. Con riferimento al circuito equivalente di piccolo segnale di Figura 1, e indicando con ZC (s) il
   parallelo di RC e 1/sC, ZC (s) = RC /(1 + sRC C), abbiamo:
                    Vo (s) = −ZC (s)(β0 Ib1 (s) + β0 Ib2 (s)) ≃ −ZC (s)β0 (β0 + 1)Ib1 (s)             (6)
                                 ZC (s)β0 (β0 + 1)RB
                           = −                                 Ii (s)                                 (7)
                               RB + rbe,1 + (β0 + 1)rbe,2
                               ZC (s)β0 (β0 + 1)RB
                           ≃ −                          Ii (s)                                        (8)
                               RB + VIth
                                      B
                                         + (ββ0 0+1)I
                                                  Vth
                                                      B

                                     ZC (s)β02 RB
                            ≃ −                   Ii (s)                                              (9)
                                     RB + 2V   th
                                              IB
   Si osservi che alla medesima espressione si arriva utilizzando il circuito equivalente derivato dalle
   espressioni di cui al punto (2). Il polo é dunque quello dovuto all’impedenza ZC (s) e si colloca alla
   frequenza fp = 1/2πRC C ≃ 26.5 MHz.

                             |Vo(s)/Ii(s)|




                                                              fp               f



                         Arg(Vo(s)/Ii(s))

                                                                           f


                                   −45



                                   −90



                                                   Figura 1
                                        Prova scritta di Fondamenti di Elettronica
                                                      25 giugno 2014
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare tutte le tensioni e correnti statiche nel circuito. (10 punti)

    2. Tracciare il circuito equivalente di piccolo segnale corrispondente al punto di lavoro determinato al
       quesito precedente e calcolare il valore dei parametri diﬀerenziali. (punti 6)

    3. Determinare le funzioni di trasferimento Ri = VE /Ii e AV E = Vo /VE (10 punti).

    4. Determinare l’equazione che consente di dimensionare il fattore di forma S del transistore MOS al
       ﬁne di ottenere una assegnata frequenza di taglio a -3dB della funzione di trasferimento Vo (s)/Vi (s),
       indicare se si tratta di funzione passa-alto o passa-basso e calcolare il valore di S che corrisponde
       a f−3dB =10 MHz. (4 punti)



                                      VCC
                                                                                RE               RB                         RC
                                                                                      VE
                               Vi                                                                                                 Vo
                                           C
                                                                                RX




Vγ =0.7 V, VT =0.5 V, VCC =5 V, βF = β0 = 100, β ′ = 100 µA/V2 , Vth = 25 mV, RC =100 Ω, RX =100
Ω, RE =500 Ω, RB =12000 Ω, C = 10 pF.
                   Soluzione del compito di Fondamenti di Elettronica
                                    25 giugno 2014
1. Il transistore MOS opera ad ID =0, mentre non é a priori scontato che sia VGS >VT e che quindi il
   transistore sia acceso. Considerato il valore modesto di RC e RX rispetto a RE e RB é plausibile ritenere
   che il transistore operi in regione normale di funzionamento. Partiamo dunque da questa ipotesi (da
   veriﬁcare a posteriori). Le equazioni del circuito posso essere espresse nella forma:
                                             VE       VCC − VE
                                                    =           + (βF + 1)IB                              (1)
                                             RX          RE
                                                      VCC − VE − Vγ
                                             IB     =                                                     (2)
                                                           RB
                                             VO     = VCC − βF RC IB                                      (3)
                                                                                                          (4)
  da cui otteniamo
                          [                              ]                      [                ]
                            1    1     βF + 1               1     βF + 1       βF + 1
                      VE      +     +           = VCC           +         − Vγ                        (5)
                           RX   RE      RB                 RE      RB            RB
  la cui soluzione fornisce VE = 2.262 V. Per sostituzione nelle precedenti equazioni ricaviamo inoltre
  IB ≃ 170µA, IE ≃ 17.1 mA, IC ≃17 mA, Vo =3.3 V, VCB =0.34 V a conferma dell’ipotesi di funzionamento
  in regione normale. Di conseguenza abbiamo anche che il transistore MOS lavora con VGS >VT ed é
  pertanto acceso. Dovendo essere IDS =0 A non puó che essere VDS =0 V, che corrisponde al funzionamento
  in regione triodo.
2. Il circuito equivalente puó essere ottenuto applicando la solita metodologia. Poiché il MOSFET lavora in
   regione triodo a VDS =0 abbiamo immediatamente gm = gmb = 0 S, gds =β ′ S(VGS − VT )=S · 224µS. Per
   quanto riguarda il transistore bipolare, sulla base del modello a soglia per la giunzione base-emettitore
   avremmo rbe =0 Ω. Una stima di migliore approssimazione puó essere ottenuta nella forma rbe =
   Vth /IB ≃147 Ω.
3. Abbiamo:
                                                        vo                 β0 RC
                                                               =                                          (6)
                                                        vE               rbe + RB
  Inoltre vale:
                                  vE = (RX ||RE ||(rbe + RB )) (β0 iB + ii )                              (7)
                                              vE
                                  iB = −                                                                  (8)
                                         (rbe + RB )
                                          RX ||RE ||(rbe + RB )
                                  vE =         (                     ) ii = Ri ii                         (9)
                                       1 + β0 RX ||R  E ||(rbe +RB )
                                                    (rbe +RB )

4. Detta Zin (s)=1/gds +1/sC possiamo scrivere
      Vi (s) − VE (s) = Vi (s) − Ri Ii (s) = Zin (s)Ii (s)                                          (10)
               Vo (s)   Vo (s) VE (s) Ii (s)           β0 RC    Ri        β0 RC        sCRi
                      =         ·         ·       =          ·        =         ·                   (11)
               Vi (s)   VE (s) Ii (s) Vi (s)        rbe + RB Ri + Zin   rbe + RB 1 + sC(Ri + 1/gds )
  dove si é tenuto conto del fatto che Vo (s)/VE (s)=vo /ve e che Ii (s)/Vi (s)=ii /vi =1/Ri . La funzione di
  trasferimento del guadagno di tensione presenta dunque uno zero nell’origine e un polo alla frequenza
                                                        1
                                     f=                                                                   (12)
                                         2πC(Ri + 1/(Sβ ′ (VGS − VT )))
                                             1            2πCf
                                 S= ′                ·             ≃ 2.9
                                      β (VGS − VT ) 1 − 2πCf Ri
                                                                                    bo ib
                                                         VE                                 Vo
                                 Vi(s)
                                              gds                  rbe
                                         C
                                                        RX    RE           ib               RC
                                                                    RB



                                                         Figura 1
                                        Prova scritta di Fondamenti di Elettronica
                                                       17 luglio 2014
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al due porte nel riquadro tratteggiato di Figura in cui il morsetto di ingresso é collegato
ad un opportuno generatore di tensione in grado di mantenere accesa la giunzione base-emettitore di T1 ,
si risponda ai seguenti quesiti utilizzando i valori assegnati dei parametri:

    1. Determinare tutte le tensioni e correnti statiche nel circuito e il valore della resistenza RX in modo
       tale che la corrente di collettore del transistore T2 valga IC2 =100 µA e che VBE1 =VBE2 . (10 punti)

    2. Determinare le espressioni dei parametri della matrice ibrida hij del due porte. (punti 8)

    3. Determinare la funzione di trasferimento AV = Vo (s)/Vi (s) del due porte (6 punti).

    4. Supponendo ora di collegare tra ingresso e uscita del due porte il risonatore LC mostrato in ﬁgura,
       determinare la temperatura di funzionamento dei transistori T1 e T2 e il valore numerico di AV (ω =
       0) e AV (ω = ∞). (6 punti)



                                                                 Vcc
                                                                               R1            R2


                                                       Vi                     T1                           Vo

                                                                                           T2
                                                                               RX



                                                                                      C
                                                                                      L


VCC =2 V, IS2 =10 fA, Area T1 =2·Area T2 , βF = β0 = 80, Vth = 25 mV, R1 =2.5 kΩ, R2 =10 kΩ, L = 10
nH, C = 10 nF.
                    Soluzione del compito di Fondamenti di Elettronica
                                      17 luglio 2014
1. Il circuito pare essere riconducibile al collegamento in cascata di uno stadio ampliﬁcatore a doppio carico
   con uno stadio ad emettitore comune. Poiché il transistore T1 é per ipotesi acceso con Vbe1 >0, esso si
   troverá in regione normale o di saturazione. La corrente di emettitore sará dunque positiva secondo le
   normali convenzioni di segno per i transistori bipolari npn e consentirá la polarizzazione diretta anche
   della giunzione base emettitore di T2 . Anche T2 sará quindi in regione normale o di saturazione. Dalla
   speciﬁca sulla corrente IC2 otteniamo immediatamente Vo =1 V e dunque, ipotizzando per entrambi i
   transistori il funzionamento in regione normale:

                            Vbe1 = Vbe2 = Vth ln(IC2 /IS ) = 10Vth ln(10) ≃ 0.5756 V                         (1)
                             Vi = Vbe1 + Vbe2 ≃ 1.15 V                                                       (2)

   Poiché i transistori hanno per ipotesi la medesima Vbe ma area doppia, abbiamo anche IB1 =2IB2

                                 VC1 = VCC − 2IC2 R2 = 1.5 V                                                 (3)
                                                  Vbe2
                                 RX =                             ≃ 2860 Ω                                   (4)
                                       IC2 [2(βF + 1)/βF − 1/βF ]
   I valori ottentuti confermano l’ipotesi di funzionamento in regione normale in quanto sia VCB1 che VCB2
   risultano positive.

2. La ﬁgura riporta il circuito equivalente di piccolo segnale del due porte. Essendo privo di eﬀetti reattivi,
   esso sará descritto dalle seguenti equazioni ordinarie (non diﬀerenziali) nelle variabili di piccolo segnale:

                              vi = (rbe1 + (β0 + 1)(RX ||rbe2 ))ii                                           (5)
                                             vo         RX                    1
                              io = β0 ibe2 +    = β0             (β0 + 1)ii +    vo                          (6)
                                             R2      RX + rbe2                R2
   da cui otteniamo

                                        h11 = hi = rbe1 + (β0 + 1)(RX ||rbe2 )                               (7)
                                        h12 = hr = 0                                                         (8)
                                                               RX
                                        h21 = hf        = β0           (β0 + 1)                              (9)
                                                             RX + rbe2
                                                           1
                                        h22 = ho        =                                                   (10)
                                                          R2

3. In assenza di eﬀetto Early la presenza della resistenza R1 non perturba il comportamento del primo
   stadio del circuito rispetto a quello che si avrebbe in assenza di R1 . Pertanto possimo considerare a
   tutti gli eﬀetti il primo stadio come un ampliﬁcatore a singolo transistore in conﬁgurazione collettore
   comune (R1 =0 Ω). Il secondo stadio é invece un classico stadio ad emettitore comune. Ricordando le
   espressioni del guadagno di tensione degli stadi elementari possiamo dunque scrivere il guadagno totale
   come prodotto dei guadagni dei singoli stadi a patto che si tenga debitamente conto dell’eﬀetto di carico
   del secondo stadio sul primo.
                                                         [                                       ] [   ]
                                                                 (β0 + 1)(RX ||rbe2 )         β0
                       AV    = AV,c.c. · AV,e.c. =                                       · −      R2        (11)
                                                             rbe2 + (β0 + 1)(RX ||rbe2 )     rbe2

4. Per ω=0 e per ω=∞ il risonatore si comporta come corto circuito e pertanto non puó che essere AV =1.
   La temperatura di funzionamento dei transistori si evince dal valore assegnato di Vth =25 mV. Otteniamo
   in particolare T =qVth /kB ≃ 290 K.

                                            ib1
                                   vi                                                       vo
                                          rbe1                bo ib1
                                                                              bo ib2
                                                   RX                  rbe2            R2
                                                        R1
                                                                 ib2

                                                         Figura 1
