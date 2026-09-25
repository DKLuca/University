---
fonte: "2004-2008_Soluzioni.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica I
                                 24 Marzo 2004
1. Vista la topologia del circuito Vi non può essere maggiore di VCC . Pertanto il diodo è all’equilibrio
   o in inversa. Se fosse all’equilibrio si avrebbe Vbe = Vi e pertanto una forte corrente entrerebbe
   nel terminale di base del transistor. Tale corrente non potrebbe provenire da RF in quanto Vo
   è comunque minore o uguale a VCC . Pertanto dovrebbe necessariamente provenire dal diodo, in
   contrasto con l’ipotesi che esso si trovi all’equilibrio. Se ne deduce che il diodo e‘ polarizzato in
   inversa. e che la giunzione base emettitore del BJT è polarizzata in diretta. T1 non può trovarsi
   in saturazione; infatti questo implicherebbe una giunzione base-collettore polarizzata in diretta ed
   una forte corrente Ii in grado di alimentare sia RF che la base di T1. Pertanto il transistor si trova
   in regione normale di funzionamento. La corrente di base, positiva entrante nel morsetto di base,
   proviene da VCC e scorre in massima parte attraverso RL ed RF .
   Poichè T1 opera in regione normale ci attendiamo che la sua tensione base-emettitore sia dell’ordine
   di 0.5 − 0.7 V. Questo implica una tensione inversa sul diodo dell’ordine di −VD = VCC − Vi ≈ 2.7 V
   cioè molto maggiore in modulo di Vth . Pertanto Ii ' −IS = 1 fA e
                                       Vth         Vth          Vth
                               rD =           =           '             →∞                           (1)
                                    ID + IS     −Ii + IS     −IS + IS
2. La corrente di emettitore di T1 è pari a:
                                               VCC − Vo      (3.3 − 1.65)
                            IE = IB + IC =                '               ' 825 µA                     (2)
                                                  RL             2000
   Pertanto abbiamo
                                                   βF
                                         IC =             IE ' 809 µA.                                 (3)
                                                (βF + 1)
   Poichè la corrente nel diodo è del tutto trascurabile abbiamo anche:
                                                         IC
                                         Vbe,0 = Vth ln( ) ' 0.685 V                                   (4)
                                                         IS
                                                         Vo,0 − Vbe,0
                                            IE = IC +                                                  (5)
                                                             RF
   da cui otteniamo
                                                     Vo,0 − Vbe,0
                                    RF = (βF + 1)                 ' 59.6 kΩ                            (6)
                                                          IE
3. Vista la topologia del circuito e considerando che sia l’assenza di specifiche sulla tensione di Early
   che l’uguaglianza βF = β0 inducono a trascurare l’effetto Early otteniamo:
                                                  1              1
                                        y11 =         + sCbe +                                        (7)
                                                 rbe            RF
                                                     1
                                        y12 = −                                                       (8)
                                                   RF
                                                 β0      1
                                        y21 =         −                                               (9)
                                                 rbe RF
                                                  1      1
                                        y22 =         +                                              (10)
                                                 RL RF
4. Le equazioni che descrivono il circuito sono:
                                                vi    vi − vo
                                             ii =   +                                                 (11)
                                                rbe     RF
                                                µ                 ¶
                                                          vo − vi
                                        vo = −RL gm vi +                                              (12)
                                                            RF
   Da queste otteniamo:
                      vo                    (rbe ||RF )(gm − 1/RF )
                         (j0) = −                                                                     (13)
                      ii          (1/RL + 1/RF + rbe (gm − 1/RF )/(rbe + RF ))
5. Nel limite per RF → ∞ otteniamo dall’espressione precedente
                                vo
                           lim     (j0) = −gm rbe RL = −β0 RL ' −100 kΩ                               (14)
                         RF →∞ ii
                 Soluzione del compito di Fondamenti di Elettronica
                                  14 Giugno 2004
1. In regime stazionario il valore della tensione di ingresso è chiaramente ininfluente sul funzionamento
   del circuito in quanto l’ingresso è disaccoppiato dal circuito tramite il condensatore. Inoltre, tutti i
   parametri del circuito e del transistore sono noti. Poichè non viene specificato alcun valore definito
   per VBE,on mentre è indicato il valore di IS cerchiamo una soluzione attraverso il metodo iterativo
   che tiene conto della natura esponenziale della caratteristica IC − VBE . Un insieme di equazioni
   indipendenti è dato da:


                              VCC − R1 (IB + IR2 ) = VBE + RL IB (βF + 1)                               (1)
                                                     VBE + RL IB (βF + 1)
                                              IR2 =                                                     (2)
                                                              R2
                                                          µ       ¶
                                                            βF IB
                                             VBE = Vth ln                                               (3)
                                                             IS
   Elaborando queste equazioni otteniamo:
                                                               R1
                    VCC − R1 IB = VBE + RL IB (βF + 1) +          (VBE + RL IB (βF + 1))                (4)
                                                               R2
                                                     µ                           ¶
                                    VCC R2                R1 R2
                              VBE =         − IB                 + RL (βF + 1)                          (5)
                                    R1 + R2              R1 + R2
   Sostituendo i valori dei parametri ed esplicitando rispetto ad IB si ha infine:
                                                    1.25V − VBE
                                             IB =                                                       (6)
                                                       5600 Ω
   Risolvendo questa equazione iterativamente con l’eq. 3 otteniamo:

                                              IB (µA)     VBE (V )
                                                  -           0
                                                223.2      0.6935
                                                99.37      0.6733
                                               102.98      0.6742
                                               102.82      0.6741


   da cui otteniamo infine:

                                   IC   = βF IB ' 5.141 mA                                              (7)
                                   IE = (βF + 1)IB ' 5.244 mA                                           (8)
                                   V2 = RL IE ' 0.5244 V                                                (9)
                                   VB = VBE + V2 ' 1.1985 V                                            (10)
                                  IR2 = VB /R2 ' 1.1985 mA                                             (11)
                                  IR1 = (VCC − VB )/R1 ' 1.3015 mA                                     (12)
                                   IB = IR1 − IR2 ' 103 µA                                             (13)

   L’ultimo valore, molto prossimo a quello calcolato in partenza (102.82 µA) conferma la consistenza
   del calcolo effettuato.

2. Dalla definizione di matrice impedenza abbiamo:

                                            v1 = z11 i1 + z12 i2                                       (14)
                                            v2 = z21 i1 + z22 i2                                       (15)
   Poichè nel nostro caso i2 = −v2 /RL otteniamo immediatamente:
                                                                 v2
                                           v2 = z21 i1 − z22                                       (16)
                                                                 RL
                                              v2    z21 RL
                                                 =                                                 (17)
                                              i1   z22 + RL

                                      R1               RD             V2
                           I 1


                                                            CD
                                                  R2                       RL



   Poichè il circuito ha una semplice topologia a T abbiamo:

                                        z11 = R1 + R2                                              (18)
                                        z12 = R2                                                   (19)
                                        z21 = R2                                                   (20)
                                                     rD
                                        z22 =               + R2                                   (21)
                                                 1 + sCD rD
   Pertanto:
                    v2         R2 RL                  R2 RL (1 + sCD rD )
                       =              rD    =                                                      (22)
                    i1   R2 + RL + 1+sCD rD   (R2 + rD + RL )(1 + sCD rD (R2 +RL ) )
                                                                                R2 +rD +RL

3. In base alle equazioni già riportate nella sezione precedente otteniamo: R1 = z11 − z21 = 100 Ω,
   R2 = z21 = 1000 Ω. Notiamo inoltre che la transimpedenza presenta uno zero ed un polo, il primo a
   frequenza inferiore a quella del secondo. Il valore minimo si ottiene pertanto a 0 Hz, quello massimo
   per ω → ∞. Otteniamo dunque:
                                        v2                            R2 RL
                                            (ω = 0 Hz) =                                           (23)
                                         i1                       R2 + rD + RL
                                             v2                    R2 RL
                                                (ω = ∞) =                                          (24)
                                             i1                   R2 + RL
                             v2              v2                     R2 + RL
                                (ω = 0 Hz)/ (ω = ∞) =                                              (25)
                             i1              i1                   R2 + rD + RL
                Soluzione del compito di Fondamenti di Elettronica
                                 23 Giugno 2004
1. In condizioni stazionarie l’induttanza si comporta come un corto circuito. Pertanto: per Vi,0 = 0.5 V
   si ha Vi,0 < VBE,on e Q1 è spento. Ne consegue VC,0 = VCC , VE,0 = 0 V, IC,0 = IB,0 = IE,0 = 0 A.
   σnon è definito in quanto il transistore è spento.
   per Vi,0 = 5 V si ha Vi,0 > VBE,on e Q1 è acceso. Ipotizziamo che si trovi in regione normale di
   funzionamento. Ne consegue IE = (Vi,0 − VBE,on )/RE ' (5 − 0.6)/150 ' 29 mA, IB,0 = IC,0 /hF E '
   290 µA, VC,0 = VCC − RC IC,0 ' 5.644 V, VCB,0 (Q1 ) ' 0.644 V. Quest’ultimo dato conferma il
   funzionamento in regione normale di Q1 e convalida l’ipotesi fatta.
   per Vi,0 = 10 V si ha Vi,0 > VBE,on e Q1 è acceso. Ipotizziamo che si trovi ancora in regione
   normale di funzionamento. Ne consegue IE = (Vi,0 − VBE,on )/RE ' (10 − 0.6)/150 ' 62.7 mA,
   VC,0 = VCC − RC IC,0 ' 10 − 9.4 ' 0.6 V il che implica VCB,0 (Q1 ) ¿ 0 V; pertanto Q1 deve
   essere polarizzato in saturazione. Cominciamo dunque calcolando la corrente di emettitore: IE =
   (Vi,0 −VBE,sat )/RE ' (10−0.75)/150 ' 61.7 mA. Inoltre abbiamo VC,0 = RE IE,0 +VCE,sat ' 9.32 V,
   da cui segue IC,0 = (VCC − VC,0 )/RC ' (10 − 9.32)/150 ' 4.53 mA, IB,0 = IE,0 − IC,0 ' 57.1 mA.
   Pertanto si ha σ = IC /hF E IB ' 7.9 · 10−4 .

2. Tracciato il circuito equivalente per piccolo segnale otteniamo le seguenti equazioni con ovvio sig-
   nificato dei simboli:


                      vC    = −gm RC vbe                                                              (1)
                                  vbe                           vbe                vbe
                       vi   = sL(     + sCbe vbe ) + vbe + RE (     + sCbe vbe + β0 )                 (2)
                                  rbe                           rbe                rbe
   Sostituendo otteniamo:
                            gm RC                          1
                   Av = −                                                                             (3)
                             LCbe s + s(1/rbe Cbe + RE /L) + LC1 (1 + RE (β0 + 1)/rbe )
                                   2
                                                                be


   Per ω → 0 lo stadio si trasforma in un semplice circuito amplificatore a doppio carico. Il guadagno
   tende a:
                                                               1
                                Av (ω → 0) = −gm RC                                                 (4)
                                                     (1 + RE (β0 + 1)/rbe )
   che con le ulteriori semplificazioni (β0 +1)RE À rbe , gm rbe = β0 ≈ β0 +1 fornisce la nota espressione
   Av ' −RC /RE .
   Inoltre Av (ω → ∞) ovviamente tende a zero per ω → ∞ in quanto l’induttore tende ad un circuito
   aperto e l’ingresso risulta scollegato dalla base del transistore.

3. Il valore limite cercato è quello che comporta VCB = 0. Poichè al limite della regione di saturazione
   vale ancora IC = hF E IB , e poichè abbiamo già calcolato che per Vi,0 = 5 V vale IE,0 ' 29 mA
   otteniamo IC,0 ' 28.7 mA. A questo punto si tratta ovviamente di imporre VC = VCC − RC IC =
   VB = 5 V, da cui otteniamo RC = 5V /IC,0 ' 174 Ω.
                    Soluzione del compito di Fondamenti di Elettronica
                                     13 Luglio 2004
1. Il transistore è connesso in configurazione base comune. In condizioni stazionarie l’induttore è un
   corto circuito e quindi la giunzione base collettore è certamente polarizzata in inversa. Poichè la
   giunzione base emettitore è invece polarizzata in diretta il transistore si trova in regione normale
   di funzionamento. Abbiamo dunque:

                                                             µ           ¶
                                                      hF E IB
                                         VBE = Vth ln                                                (1)
                                                        IS
                                  0 − (−VEE ) = VBE + R(βF + 1)IB                                    (2)

   da cui otteniamo:
                               VEE − Vth ln(βF IB /IS )   2.5 − 0.633
                          R=                            '               ' 18.3 kΩ                    (3)
                                    (βF + 1)IB            51 · 2 · 10−6

2. Tracciato il circuito equivalente per piccolo segnale otteniamo le seguenti equazioni con ovvio sig-
   nificato dei simboli:


                                                 vo            io RL
                                   io = gm vbe +    = gm vbe −                                       (4)
                                                 sL             sL
                                            vbe
                                   ii = −        − gm vbe                                            (5)
                                          R||rbe

   Pertanto:
                                                       R||rbe
                                         vbe = −                    ii                               (6)
                                                   1 + gm (R||rbe )
                                                gm (R||rbe )        RL
                                     io = −                    ii −    io                            (7)
                                              1 + gm (R||rbe )      sL
   da cui infine:
                                      io      gm (R||rbe )     sL
                                         =−                                                          (8)
                                      ii    1 + gm (R||rbe ) RL + sL

3. L’espressione determinata in precedenza presenta uno zero nell’origine ed un polo reale positivo.
   Pertanto è di tipo passa alto. La frequenza di taglio a -3dB è determinata dalla frequenza del polo:
                                                          1 RL
                                               f−3dB =                                               (9)
                                                         2π L
   Pertanto otteniamo:
                                                1 RL
                                         L=             ' 159 nH                                    (10)
                                               2π f−3dB
                  Soluzione del compito di Fondamenti di Elettronica
                                   8 Settembre 2004
Prima Parte:

  1) Il circuito è caratterizzato dalla presenza di un transistore bipolare di tipo pnp. Ricordiamo che
     per esso valgono le medesime equazioni che per il transistore npn a patto di scambiare i segni delle
     tensioni e delle correnti in gioco.
     Dalla conoscenza della tensione di uscita desiderata otteniamo
                                                VOut,0 − (−VEE )
                                      ICp,0 =                    ' 100 µA                             (1)
                                                       RCp
                                                      µ           ¶
                                                          ICp,0
                                   VEB,0 = Vth ln               + 1 ' 0.5756 V                        (2)
                                                          AJS
     da cui otteniamo:
                                               VEB,0
                                   IREp ,0 =         ' 28.8 µA                                        (3)
                                                REp
                                   IRBp ,0   = IREn + ICp,0 /βF ' 32.8 µA                             (4)

                                                 VCC − (VEB,0 )
                                       RBp =                    ' 74 kΩ                               (5)
                                                     IRBp

     Seconda Parte:

  1) L’impedenza ZE vale:

                                        1        1        REn (1 − jωREn CE )
                         ZE = REn ·       ·             =            2 C2                             (6)
                                      jωCE REn + 1/jωCE     1 + ω 2 REn E

     Dobbiamo quindi imporre:
                                                          REn
                                       |ZE | = q                      ≤ 0.1 Ω                         (7)
                                                           2 C2
                                                  1 + ω 2 REn E

     Pertanto si tratta semplicemente di imporre 1 + ω 2 REn
                                                          2 C 2 ≥ 5002 . Questo implica:
                                                             E
                                                 s
                                                      5002 − 1
                                         CE ≥                  2  ' 1.6 µF                            (8)
                                                     4π 2 f 2 REn
     .

  2) L’impedenza di carico è costituita dal parallelo della resistenza RCn con la connessione in serie di
     RL , CL ed L. Queste ultimi tre elementi formano un circuito risonante serie; pertanto l’impedenza
     della connessione è puramente reale (e di valore pari ad RL ) quando è soddisfatta la condizione
     ω 2 = 1/LCL . Otteniamo dunque L = 1/ω 2 CL ' 2.5 µH.
     In modo più formale e meno efficiente si può procedere al calcolo esplicito della parte immaginaria
     di ZL ottenendo:

                               ωRL RCn CL (1 − ω 2 LCL ) − ω(RL + RCn )CL RCn (1 − ω 2 LCL )
                 Im[ZL ] =                                                                            (9)
                                           (1 − ω 2 LCL )2 + ω 2 CL2 (RCn + RL )2
                                        2 C (1 − ω 2 LC )
                                     −ωRCn   L             L
                           =                        2                                                (10)
                               (1 − ω LCL ) + ω CL (RCn + RL )2
                                     2     2    2


     che porta alle medesime conclusioni già svolte in precedenza.
3) Utilizzando il circuito equivalente a 3 parametri (come suggerito dall’indicazione della tensione di
   Early tra i parametri) in cui il generatore controllato di corrente assume l’espressione ic = gm vbe
   e ricordando che in base al dimensionamento precedente, alla frequenza di 1 MHz l’emettitore è
   praticamente a massa, otteniamo molto semplicemente:

                                             AV = −gm (ZL ||ro )                                        (11)

   dove ro = VA /IC,0 ' 20 kΩ, gm = IC,0 /Vth ' 40 mS. Poichè sempre in base ai dimensionamenti
   precedenti alla frequenza di 1 MHz si ha ZL = RL ||RCn = 500Ω e poichè ZL ||ro ' 487Ω otteniamo
   AV ' −19.5.
   Si osservi che in questo caso non è lecito utilizzare la formula del guadagno di tensione per uno
   stadio a doppio carico AV = −ZC /ZE in quanto questa espressione è valida solo se rbe ¿ (β0 +1)ZE ,
   condizione niente affatto garantita nel caso in esame proprio in virtù del fatto che ZE è molto piccola.
   Anzi, partendo proprio dall’espressione più generale del guadagno di tensione AV = −β0 ZC /(rbe +
   (β0 + 1)ZE ), e trascurando il termine in ZE otteniamo AV ' −β0 ZC /rb e = −gm ZC , dove in questo
   caso ZC = ZL ||ro .
                Soluzione del compito di Fondamenti di Elettronica
                                23 Settembre 2004
1. Q1 e Q2 sono connessi a specchio di corrente ed operano in regione normale in quanto VCB1,0 = 0 V
   e VCE2,0 = VCC À VCE,sat . In condizioni statiche, poichè i transistori sono identici, si ha:

                                              Iu,0 = IC2,0 = βF IB2,0                               (1)

                                    Ii,0 = IC1,0 + 2IB1,0 = (βF + 2)IB2,0                           (2)
                                                      βF
                                           Iu,0 =          Ii,0 ' 1.82 mA                           (3)
                                                    βF + 2
2. Trascurando gli effetti reattivi dei transistori, adottando un circuito equivalente a 2 parametri,
   sapendo che gm rbe = β0 e ricordando che il transistore connesso a diodo presenta una resistenza
   differenziale pari a rbe /(β0 + 1) abbiamo:
                          vi                rbe    1     rbe    1         rbe
                               = rbe ||         ||   =       ||   =                                 (4)
                          ii              β0 + 1 sC    β0 + 2 sC    β0 + 2 + sCrbe
                          iu
                               = gm                                                                 (5)
                          vi
                          iu         β0       1
                               =                                                                    (6)
                          ii       β0 + 2 1 + sCrbe
                                              β +2  0


   Il polo vale dunque:
                                                β0 + 2
                                          p=−          = −40 · 106 rad/s                            (7)
                                                 rbe C
3. La corrente di ingresso è data dalla sovrapposizione di un termine in continua e di uno a pulsazione
   ω1 = |p|. Avremo dunque
                                       Iu (t) = Iu,0 + Iu,1 cos(ω1 t + φ)                            (8)
   dove ovviamente Iu,0 = 1.82 mA come calcolato al punto precedente, mentre

                                                Iu,1 = |Ai (jω1 )|Ii,1

                                                 φ = Arg[Ai (jω1 )]
   essendo Ai (jω) il guadagno di corrente del circuito valutato al quesito precedente. Poichè la pul-
   sazione ω1 coincide con la pulsazione di taglio del sistema abbiamo
                                                 1 β0
                                          Iu,1 = √         Ii,1 ' 1.29 mA
                                                  2 β0 + 2
                                                        φ = −45o
   Occorre naturalmente verificare che per questi valori dei parametri il transistore Q2 si mantenga in
   ogni istante in regione lineare. La tensione di uscita sarà:

                                          Vu (t) = Vu,0 + Vu,1 cos(ω1 t + θ)                        (9)

   con Vu,0 = VC C e Vu,1 = Iu,1 |jω1 L| ' 514 mV . Pertanto poichè il minimo valore di tensione
   durante il periodo del segnale Vu,min = Vu,0 − Vu,1 ' 4.486 V À VCE,sat il calcolo di Iu effettuato
   in precedenza è valido.
                 Soluzione del compito di Fondamenti di Elettronica
                                 30 Novembre 2004
1. Abbiamo IV cc = PV cc /Vcc = 5 mA. Pertanto IR3,0 = 0.2IV cc = 1 mA e Ic2,0 = 4 mA. Ib2,0 =
   Ic2,0 /βF ' 40 µA. Poichè la tensione Vc2 deve poter effettuare un’escursione di +1V rispetto al
   valore dei riposo abbiamo che Vc2,0 = Vcc − 1V = 4 V e quindi

                                        RC = (Vcc − Vc2,0 )/Ic2,0 ' 250 Ω.

   Inoltre poichè C2 = ∞ la tensione Vb2 è costante anche in presenza di un segnale di ingresso vi .
   Pertanto, affinchè il transistore non saturi a causa dell’escursione della tensione Vc2 prodotta da vi è
   sufficiente che Vb2,0 < Vc2,0 − 1V = 3 V. Poniamo dunque Vb2,0 = 3 V. Otteniamo immediatamente

                                                                   2
                                   R3 = (Vcc − Vb2,0 )/IR3,0 '        ' 2000 Ω
                                                                 10−3

   Si ha dunque IR2,0 = IR3,0 − Ib2,0 ' 0.96 mA, Ie2,0 = Ic1,0 = Ic2,0 + Ib2,0 = 4.04 mA, Ib1,0 =
   IC1,0 /βF = 40.4 µA. Abbiamo inoltre IR1,0 = IR2,0 − Ib1,0 ' 0.9196 mA; Vb1,0 = Vth ln(Ic1,0 /IS1 ) '
   0.72568 V e quindi
                                                        3 − 0.72568
                          R2 = (Vb2,0 − Vb1,0 )/IR2,0 '             ' 2369 Ω,
                                                        0.96 × 10−3
                                           R1 = Vb1,0 /IR1,0 ' 789.1 Ω.

2. Abbiamo Vbe1,0 = Vb1,0 ' 0.72568 V, Vbe2,0 = Vth ln(Ic2,0 /IS2 ) ' 0.72543 V, Ve2,0 = Vb2,0 − Vbe2,0 '
   2.2746 V, Vcb1,0 = Ve2,0 − Vb1,0 ' 1.5489 V, Vcb2,0 = 1 V.

3. I transistori funzionano tutti in regione normale. I condensatori sono assimilabili a corti circuiti
   in virtù del loro valore molto elevato. Pertanto il terminale di base del transistore 2 è connesso a
   massa agli effetti del funzionamento per piccolo segnale. Otteniamo dunque il circuito equivalente
   rappresentato in figura.
                                                                     GM2 V Be2
                                V Be1                      - V Be2                 VO

                                               GM1 V Be1
                     R1 || R2       RBe1                             RBe2           RC




                                                FIGURA 1
   Le equazioni che lo descrivono sono:

                                 vo = −gm2 RC vbe2
                                                                        rbe2 gm1 vbe1
                                vbe2 = −rbe2 (gm2 vbe2 − gm1 vbe1 ) =
                                                                        1 + gm2 rbe2
   Otteniamo dunque
                                vo    gm2 rbe2 gm1 RC      β02
                                   =−                 =−         gm1 RC ' 40.4                           (1)
                                vi     1 + gm2 rbe2      β02 + 1

4. Abbiamo: gm1 ' Ic1,0 /Vth ' 161.6 mS, gm2 ' Ic2,0 /Vth ' 160 mS, rbe1 ' Vth /Ib1,0 ' 618.8 Ω,
   rbe2 ' Vth /Ib2,0 ' 625 Ω, R1 ||R2 ' 592 Ω, e quindi Av0 ' 20.44.
                 Soluzione del compito di Fondamenti di Elettronica
                                   17 marzo 2005
1. a) Poichè le due resistenze sono uguali ed i due transistori sono identici e complementari, nella
   condizione Vi1,0 = Vi2,0 = VCC /2 il circuito è perfettamente simmetrico e le cadute sulle resistenze
   Rx ed Ry sono uguali tra loro.
   I transistori non possono essere interdetti, perchè questo comporterebbe correnti nulle, cadute nulle
   attraverso i resistori e quindi polarizzazione diretta delle giunzioni base-emettitore ed emettitore-
   base dei transistor npn e pnp, rispettivamente, negando l’ipotesi iniziale.
   I transistori non possono essere in saturazione, in quanto la polarizzazione diretta della giunzione
   base-collettore del BJT npn implicherebbe una polarizzazione inversa della giunzione emettitore-
   base del transistore pnp, e viceversa.
   Pertanto entrambi i transistor sono in regione normale di funzionamento. La simmetria impone an-
   che che Vbe,npn = Veb,pnp , IC,npn = IC,pnp , IB,npn = IB,pnp . Indichiamo genericamente con Vbe , IC , IB
   questi valori. L’equazione della maglia comprendente la giunzione base-emettitore del transistore
   npn fornisce:                          µ                 µ     ¶             µ     ¶¶
                       VCC                  βF + 1            Vbe     βF          Vbe
                              − Vbe = Ry             IS exp         +    IS exp
                         2                     βF             Vth     βF          Vth
   da cui                                                               µ    ¶
                                             VCC      2βF + 1        Vbe
                                     Vbe =       − Ry         IS exp
                                              2         βF           Vth
   che riscritta fornisce:                       Ãµ            ¶                  !
                                                      VCC              βF
                                  Vbe = Vth ln            − Vbe
                                                       2        Ry IS (2βF + 1)
   Questa equazione si presta ad una soluzione in forma iterativa. Partendo dalla soluzione di primo
                (0)                                                       (1)                  (2)
   tentativo Vbe = 0 V otteniamo la seguente successione di valori: Vbe ' 0.71343 V, Vbe '
                   (3)
   0.70958 V, Vbe ' 0.70961 V, . . . . Da questo valore consegue IC ' 2.124 mA, IB ' 42.48 µA,
   IE ' 2.1665 mA, Vy,0 = VCC /2 − Vbe = 5 − 0.70961 ' 4.29 V, VRy = Ry (IC,pnp + IE,npn ) '
   103 · 4.2905 · 10−3 ' 4.2905 V, Vx,0 = VCC − VRx = VCC − VRy = 10 − 4.2905 ' 5.7095 V.
   b) Nel caso Vi1,0 = Vi2,0 = VCC la giunzione base-emettitore del transistore npn non può che essere
   in polarizzazione diretta. Poichè la corrente di collettore non è nulla esiste una caduta di tensione su
   Rx che polarizza l’emettitore del BJT pnp a tensione inferiore al corrispondente morsetto di base.
   Pertanto il transistore pnp è interdetto (la giunzione base-collettore è infatti anch’essa certamente
   in inversa). Inoltre la caduta su Rx polarizza in diretta la giunzione base-collettore del transistore
   npn, che pertanto si porta a lavorare in regione di saturazione.

2. Il circuito equivalente per piccoli segnali è mostrato in Fig.1. Si è trascurato l’effetto Early.
                                                             B0*i2


                     vi1         r_be1                                  r_be2         vi2
                                                             B0*i1
                           i_1                                     Vx             i_2

                                                 Ry                     Rx




   Per quanto riguarda i parametri differenziali abbiamo: rbe1 = rbe2 ' Vth /IB,0 ' 588 Ω.
3. Le equazioni che descrivono il circuito equivalente sono:

                          vi1 = vy + rbe1 i1 = +R(β0 + 1)i1 + Rβ0 i2 + rbe1 i1
                          vi2 = vx − rbe2 i2 = −R(β0 + 1)i2 − Rβ0 i1 − rbe2 i2

  Nel caso vi1 = vi2 otteniamo dunque:

                    +R(β0 + 1)i1 + Rβ0 i2 + rbe1 i1 = −R(β0 + 1)i2 − Rβ0 i1 − rbe2 i2   (1)

  che implica:
                       (R(β0 + 1) + Rβ0 + rbe1 )i1 = −(R(β0 + 1) + Rβ0 + rbe2 )i2       (2)
  Poichè rbe1 = rbe2 = rbe si ha dunque

                                            i1 = −i2
                                           vi1 = (R + rbe )i1
                                            vy = Ri1 = vx
                                           vy       R
                                               =
                                           vi1   R + rbe

  Nel caso vi1 = −vi2 otteniamo invece:

                     +R(β0 + 1)i1 + Rβ0 i2 + rbe1 i1 = R(β0 + 1)i2 + Rβ0 i1 + rbe2 i2   (3)

  che implica:
                                       (R + rbe1 )i1 = (R + rbe2 )i2                    (4)
  Poichè rbe1 = rbe2 = rbe si ha dunque

                                       i1 = i2
                                      vi1 = (R(2β0 + 1) + rbe )i1
                                       vy = R(2β0 + 1)i1 = −vx
                                      vy      R(2β0 + 1)
                                          =
                                      vi1   R(2β0 + 1) + rbe
                                 "!#$%&('( 
                                                      )*,+  +  )--.
 /10324&57698;< : 5 =?>9@BA%CD57C?=?4B>95EAF4&A#C?4&AF4GC?H < A(=D5JI < HE4&57698;< : H < > < A(=?>9@BK"L5E5E=?>9@BA%CD57C?=?4B>95 M7@N&57O%AFPQ5R4&A < L@BC <TS 6T4&M7M < =?=?4B> <
       AF4&A,HO4 : < CDC < > < HE4&M7@1>95RPUPQ@1=D@V57A,W%5R> < =?=D@XIA < 6T4&A%C < N&O < 698 <Y< A(=?>9@BK"L55=?>9@BA%CD57C?=?4B>95C?4&AF4VHE4&M7@1>95RPUPQ@1=D557A
     > < N&5R4&A < AF4B>9KG@BM < 0[ZX5=?>9@1=?=D@\H < >D=D@BA(=?4]W%5^O%A_6U5R>96UO%5R=?4\C < H@1>9@1=?4B> < 6T4&C?=D5R=DO%5R=?4\W%@\W%O < C?=D@BW%5`@\6T4&M7M < =?=?4B> <
        6T4&KO%A < 57AY6U@BCD6U@1=D@X0
a03bc@#6T4B>D> < A(= < @BCDC?4B>DL5R=D@dW%@BM7MJe @BM757K < A(=D@1PQ5R4&A < W%@dH@1>D= < W < MC < 6T4&A%WF4YC?=D@BW%5R4V< : H@1>95@#fUghji k02 < >D=D@BA(=?4\lnm
         op;p fUghji kqmsr(t1u]v;wx57KyHM7576U@[fUghji kqz{/Qt1u]v}|"IfU~ hji k z{/1 r(\v}|"024&57698;< : 57M`=?>9@BA%CD57C?=?4B> < HAFH4BH < >9@]57A
      > < N&5R4&A < AF4B>9KG@BM < CD5;8%@y~ gDi k z oF7(F fU~ hji k  z/Q GF 0`24&57698;<B: 
                                                                                                       oF7
                                                   Q k"m~ gDi k3 hji k  /kz  fU~ hji k   hji k  /k

    H < >@Q < > < Q k"m/"]W <  << CDC < > < k"mBB BF   h  /^z 1F 0
0 ZX5;8%@
                                    o% i h3m op;p] k1fUghji k"z   1BF(/Qt1u1v} z/1 t¡r o
rF03b <¢ O%@1=?=?>D4 <Q¢ O%@1PQ5R4&A%5F698 < W < CD6T>95RB4&AF457M£¤O%AFPQ5R4&A%@BK < A(=?4W < MX6U5R>96UO%5R=?4¥57A¦£¤O%AFPQ5R4&A < W < M7M < 6U57A ¢ O < NB>9@BA%W < PUP <
    § ¨ §  ¨ § g$©¨?ª$~ i © ¨?ª$~ i k C?4&AF4 

                                                                    § m              k  hji k  /$ª$~ i k
                                                                 § g$©xm          §  ~ gDi k ª$~ i k
                                                                     § «m         § g$©  ~ gDi © ª$~ i ©
                                                                  § g$©xm           ¬© D hji ©  /$ª$~ i © ª$~ i k 
     ­c>9@1=?=D@BA%WF4&CD5¬W%53W%O < C?=D@BW%53@6T4&M7M < =?=?4B> < 6T4&KO%A < 57A®6U@BCD6U@1=D@XI MJe < C?H%> < CDCD5R4&A < W < MN&O%@BW%@1N&AF4,W%5= < A%CD5R4&A <
      6T4&KyHM < CDCD5RB4yHO4 : < CDC < > < W < = < >9KG57A%@1=D@G6T4&A[NB>9@BA%W < £¤@B6U57M75R=¡@¦ : 6T4&K <B
                                                                  §  m §   § g$©
                                                                   §         § g$© § 
                                                               g§ $© m                     hji ©  /  ¬© R Q k(
                                                                  §           ~ gDi ©¥ hji ©  /  ¬© R Q k(
                                                                § m                      hji k  /k
                                                               § g$©            ~ gDi k3 hji k  /k



                                   vi              r_be,n                    Ven                     i_b,p                        vo

                                          i_b,n                                        r_be,p

                                                          Rn                                         Rp
                                                                                    B0*i_b,n                                    B0*i_b,p
                Soluzione del compito di Fondamenti di Elettronica
                                  14 luglio 2005
1. Per definizione dei parametri h ed y abbiamo:

                                              vi = hi ii + hr vo
                                              io = hf ii + ho vo


                                              ii = yi vi + yr vo
                                              io = yf vi + yo vo

   Pertanto, da semplici manipolazioni delle equazioni precedenti otteniamo:
                                                 1
                                        yi =        ' 580 µS
                                                hi
                                                   hr
                                        yr    = − '0S
                                                   hi
                                                hf
                                       yf     =     ' 43.53 mS
                                                hi
                                                      hr hf
                                       yo     = h0 −        ' 50 µS
                                                       hi


2. Poichè hr = 0 il guadagno di tensione del due porte lineare é:
                                         1       RL             hi       RL
                        Av = −hf                        = −gm                                       (1)
                                      RG + hi 1 + ho RL       RG + hi 1 + ho RL
   Risolvendo quest’ultima equazione rispetto ad RL otteniamo:
                                                            Av
                                             RL = −              h
                                                                                                    (2)
                                                                  f
                                                      Av ho + hi +R G


   Dalle specifiche sappiamo che Av < 0 e che |Av | = 26 dB; pertanto Av = −1026/20 ' −20.
   Sostituendo i valori numerici abbiamo RL ' 500 Ω.

3. Il due porte deve consentire un guadagno di tensione in modulo superiore all’unità. Pertanto il
   transistore non può trovarsi in configurazione collettore comune. La configurazione base comune è
   esclusa perchè il guadagno di tensione deve essere negativo e perchè il coefficiente hr deve essere
   nullo. Concludiamo dunque che il transistore deve trovarsi in configurazione emettitore comune e
   che il punto di lavoro deve trovarsi in regione normale di funzionamento per consentire di avere
   hr = 0.
   Per questa configurazione abbiamo yf = gm ' IC,0 /Vth . Poichè Vth (400K) ' 34.46 mV otteniamo
   IC,0 ' 1.5 mA. Allo stesso valore si perviene ricordando che ho = 50 µS = IC,0 /VA . Inoltre,
   ricordando che βF = β0 = 75, otteniamo IB,0 ' 20 µA. Allo stesso valore si perviene ricordando
   che hi = 1723 Ω = rbe ' Vth /IB,0 .

4. Il guadagno di corrente è facilmente calcolabile come:
                                 io    vo RG + hi       RG + hi
                                    =−            = −Av         ' 73                                (3)
                                 ii    RL   vg            RL
   In alternativa, utilizzando l’espressione delle funzioni di rete dai parametri h abbiamo:
                                                io      hf
                                                   =                                                (4)
                                                ii   1 + ho RL
   Si osservi infine che nel caso semplice in cui si trascura la conduttanza di uscita del BJT (cioè
   ho = 0) abbiamo Ai = β0 .
5. La tensione di polarizzazione necessaria sarà data da VG,0 = VBE,0 + RG IB,0 . Abbiamo VBE,0 =
   Vth ln(IC,0 /IS ) ' 886.8 mV e RG IB,0 ' 2 mV; pertanto: VG,0 ' 0.888 V. Per quanto riguarda
   la minima tensione di alimentazione VCC essa deve garantire il funzionamento del transistore in
   regime normale al livello di corrente di collettore specificato IC,0 = 1.5 mA. Poichè RL ' 500 Ω, la
   caduta sulla resistenza RL nel punto di lavoro assegnato vale VRL = IC,0 RL ' 750 mV, cui occorre
   aggiungere la caduta VCE,0 necessaria a mantenere il bipolare in regione normale. Per esempio se
   assumiamo come criterio che nel punto di riposo valga VCB,0 = 0 V abbiamo VCE,0 = VBE,0 =
   0.886 V e pertanto VCC,min = 0.886 + 0.750 ' 1.636 V.

6. Si tratterebbe di sostituire il BJT npn con un transitore n-MOS in configurazione circuitale a source
   comune. La corrente di polarizzazione assorbita in ingresso dal MOS risulta essere nulla, vista la
   natura capacitiva dell’elettrodo di gate. Risulta quindi hi (ω = 0) = ∞. Di conseguenza anche il
   guadagno statico di corrente risulterà Ai (ω = 0) = ∞.
   Per ottenere il guadagno di tensione raltivamente alto richiesto dalle specifiche il transistore deve
   essere polarizzato in saturazione. Inoltre nell’espressione del guadagno di Eq.(1), si nota che per
   ω → 0, visto il modesto valore di RG , il termine RGh+h
                                                         i
                                                            i
                                                              vale circa 1 in entrambi i casi (emettitore
   comune o source comune). Pertanto per ottenere lo stesso guadagno basta imporre:

                                    gm = β(VGS − VT ) = yf = 43.53 mS                                (5)

   Mantenendo, inoltre, la stessa corrente di polarizzazione che scorre sulla resistenza di carico RL ,
   risulta:

                                              β
                                      IDS =     (VGS − VT )2 = 1.5 mA                                (6)
                                              2
   e quindi:

                                       IDS   VGS − VT
                                           =          =' 35 mV                                       (7)
                                        gm       2
   Otteniamo quindi VGS − VT = 70 mV. La minima tensione VDS che garantisce la polarizzazione
   del transistore MOS alle soglie della saturazione, é dunque VDS = VGS − VT = 70 mV. Da questo
   discende la possibilitá di operare il circuito ad una VCC,min = 0.750 + 0.070 = 0.820 V. Inoltre il
   valore necessario di β risulta essere:
                                    W             2IDS
                               β=     µn Cox =              = 631 mA/V2                              (8)
                                    L          (VGS − VT )2

   Data la tecnologia (cioè il valore di µn e Cox ) questa relazione pone un vincolo al dimensionamento
   del transistor (W/L).
                                 !#"$%'&' 
                                                      () * +&',.-- /
021436587:9%;=<?>A@BC9D;=>E>AFHGJI2KA5=9%@J5 I?5L@C9HB5>MI?;8;=>ONOI2P%;Q5=>OBC>A; RS5=TURSGJ5=V:9$>?WYXZ9%7[7[58\58;=>]RSI?;8R^9%;8I2T[>M;8>MR^9?T[T[>A@V[5 @C>A5 BGC>
    V:TUI?@J7[587:V:9?TU5 R^9%@J@C>A7[7_5L58@`R^9%@CaJP%GCT_I2KA589%@C>Mb!I2T_;858@JP?V:9%@c1ed@J9%;=V:T[>?f V:>A@C>A@JBC9gR^9%@'V:9hBC>A;8;iWkj l>SV:V:9gjLI2T_;8m?f 58; no
     >^lZ>SV:V[5=<?9pBC>A5cBJGC>qV:T_I?@7[587:V:9?T_5ZX GC9CWC>A7[7:>ST[>RSI?;8R^9%;8I2V:9rBItsvuwcx4sZyzGJP%GJI?;=>XZ>ST>A@V:T_I?N#\ 5{5cV:T_I?@J7_587:V:9?T_5}|U1

           noC~             noZn ocrJ0 uwcxZ nocq0 uL`u{svu_~s 2E 0LH  ?  
                                                                u                                       uJ                               26
            u             uwcwg[S*
              S*              uwcwg`u    NO¡
                                                      
               S*           y¢n oC~ £0¤|S¥i¦n oZ n oC~ S¥i4y¢n oZ n oC~ ¦n oC~ £0¤|S¥i
             n §          noZ%noC~4¦n oC~#  0?0
                S¥i               u wcw `u   £ ?©¨?ª{¡
                                 #¤y¢n § £0¤|          
                                   u   c
                                        
                !  S«¬­ 0^®C¯
      ° IR^9?T[T[>SV:V[I±XZ9%;8I2T_5=KSKAI2KA5=9%@J>DBC>A;RS5=T_RSG5=V:958NEX;Q58RSIhBJGJ@JFHGC>eR_²C>g58;\5=XZ9%;=9hI?7[7:9?T_\IGJ@JI±R^9?T[T[>A@V:>³S¥i´
         ?©¨?ª{¡BI?;C@C9HBJ9qdµ1¶!GC>A7:V:9qX Gq·9 >A7[7:>ST[>9?V:V:>A@HGCV:9X>ST¸>A7[>ANEX5=9R^9%@J@J>SV:V:>A@JBC9#GJ@I6T_>A7[587:V:>A@CKAIqB5<©I?;=9?T_>?¹
                                                                     qº  u   S`             uC_~ 
                                                                                              ¥i         ¼» 0A½´¯
    V:TUID58;¸@C9BC9Ddµ¾>MNOI?7[7[I1rd@±I?;=V:>ST_@JI2V[5=<2IDGJ@P?>A@C>ST_I2V:9?T[>$BJ5V:>A@J7[589%@C>puJ¿Àh »H eÁÂ9tGJ@´P?>A@J>ST_I2V:9?T[>$BJ5
     R^9?T_T[>A@'V:>^¿ÀOÃ  ?©¨?ª{¡ÃXZ9?V:T[>S\\>ST_9GJP%GJI?;8NE>A@V:>7:>ST[<5=T[>I?;8;897_R^9?X9C1
H1d;cRS5=T_RSG5=V:9E>AFG5=<©I?;8>A@'V:>I?5cX 58RSR^9%;85c7:>SP%@JI?;Q5Z>?W58;c7:>SP%GC>A@V:>?¹
                                                  i bp                                                                         vO1

                                              rbep        R1
                                                                                       β opi bp                     β oni bn
                                                                            rop
                                                                                                       ron
                                                  vin                                  i bn
                                                                            rben

                                                                                                                                vO2

                                                                                                                     R2

     dXI2T_I?NO>SV:T_5{BJ5ÄlZ>ST[>A@CKA5QI?;85<2I?;=P?9%@C9C¹
                                                           uJÆ8Ç              %?
                                        Å ¥i ~  S¥ ~   ?©¨ È'0SHÉÊ ?Ë    ®¯
                                               ~              u~   uJH~                  2
                                           Å¤Ì                   «~   noC~?S¥ ~ 2qÈA  ?©¨È'0S ÉÊ ¨ »   ¨?®¯
                                                            u               uJ                     2
                                          Å¤Ì    «   noZnoC~?S¥ ~  2qÈ¤2qÈÍ ?©¨#È'0S ÉÊ Ë  ¨?®J¯
                                                             J
                                                             u    8
                                                                  Æ Ç    J
                                                                         u 8
                                                                           Æ  Ç               %
                                                                                                  ?
                                                                                                        
                                       Å ¥i   S¥   noC~2S¥ ~  2È¤ ? ©¨#È'0S ÉÊ ??  ?¯
                                                                                             
 1436 587:9%58;=@$
                     <?>A@BC9];8>q>AFGJI2KA589%@J5ZI?5c@C9HB5 >I?;Q;=>qNOI2P%;85=>qBC>A;ZRS5=T_RSG5=V:9>AFGJ58<©I?;=>A@V:>q7[5cRSI?;8R^9%;8IE;QIV:>A@7[5=9%@C>qBJ5cGJ7_RS5=V[I
                         ÏzGJ@CKA589%@C>qBJ5cFGJ>A;8;8IEBJ5c58@JP?T[>A7[7:9 Î ¿Ä¹
    Î
                                                         i bp                                                               vO1

                                                      rbep      R1
                                                                                        β opi bp                β oni bn

                                                         vin                            i bn
                                                                                 rben

                                                                                                                            vO2

                                                                                                                 R2




                                Î             ¤y¢n Ì ~¥ ~  n Ì ¥  ¥ ~ |
                                 ¥ ~           Î    Î ¿Ä                   ¥  n Ì ~ ¥ ~ n Ì ~ Î
                                                                                                                   Î ¿Ä
                                                       Å ¥i ~                                                     Å ¥i ~
                                Î              ¥i  ~ y¢n Ì Hn Ì ~4¦n Ì ~4£0¤|^y Î   Î ¿Ä|
                                                     Å
                                                      0 #       y¢n n ~4 n ~6£0¤|p # y¢n 'n ~6 n ~4£0¤| È ¿Ä
                                                 
                                Î        È                             Ì Ì             Ì                               Ì Ì               Ì   Î
                                                               Å ¥i ~                                        Å ¥i ~
                                    Î                  #¤y¢n Ì Hn Ì ~6¦n Ì ~4£0¤|                 0?04È'0S  ­   Ë?Ë?
                                    Î ¿Ä          Å ¥i ~  Íy¢n Ì n Ì ~4 n Ì ~4£0¤|  ©¨%#È'0S 
      RU²C>D>AFHGJ5=<2I?;=>eI?;P%GJI?BJI2P%@J9±7[GJ;8;¬Wv>ANE>SV:V[5=V:9?T[>DBJ5G@C9´7:V[I?BJ5=9IBJ9?XJX5=9´RSI2T_58R^9`R^9%@GJ@ GJ@J5QR^9´V:T_I?@J7[587[V:9?T[>
     >AFHGJ5=<2I?;=>A@V:>rR^9%@¦n Ì §  n Ì  n Ì ~ n Ì ~ 1 6V[58;858KSKAI?@JBC9³5Q;LR^9%@JR^>SV:V:9BJ5LV:T_I?@J7[5Q7:V:9?T[>M>AFHGJ5=<2I?;=>A@V:>MXZ9%7[7[5QI?NE9
       RSI?;QR^9%;8I2T[>#58;ZP%GI?BJI2P%@C9M7[G;cR^9%;8;=>SV:V:9?T[>#BI?;c7:>SP%GC>A@V:>RS5=T_RSG5=V:9OI?5cX58RSR^9%;Q5c7:>SP%@JI?;85i¹
                                                                                                               i O1
                                                                i bp
                                                                          vebp                                        vO1
                                                                                                   g mvebp
                                                             rbep                 R1
                                                                                                   β eq i bp
                                                                                                                vO2
                                                                    vin
                                                             i in                                   R2



                                    Î c    n Ì *§ ¥ ~
                                       Î ¿Ä   Å ¥i ~ ¥ ~ ¤y¢n Ì § 0¤| ¥ ~
                                   Î c                           ! n Ì §             Ã
                                                                                                             0S??È¤?  
                                     Î ¿Ä              Å ¥i ~  ¤y¢n Ì *§ £0¤|                  ?Ë?   0S??È¤?Ë   ­  ¼»?»
¨C14b!I?;{RS58T_RSGJ5=V:9E>AFHGJ5=<2I?;=>A@V:>BJ5cRSGJ5{7:9?XT_IE7[5cRSI?;8R^9%;8I¹
                                              *          Î             §           Î    Î ¿Ä 
                                                                  Î ¥ ~                    Å ¥i ~
                                                       Î      § y Î   Î ¿Ä |{ Î   ¥i  Î ¿Ä 
                                                                                                                  Å ~
                                                     Î ¿ÄZ *§  ¥i0  ~   Î   §  #0   ¥i0  ~
                                                                                    Å                                                 Å
    >ABD>A7[7:>A@JBC9  §     " #! 7[5c9?V:V[5=>A@J>?¹
                                            %$
                                                                       n Ì § 0 Ã  0A'&
                                                                                       Å ¥i ~
                                                                  ?:  n Ì § £0  0 ­   0A'&
                                                                                   Å ¥i ~               
                 Soluzione del compito di Fondamenti di Elettronica
                                 21 settembre 2005
1. Essendo Vi,0 = 5 VÀ Vbe la giunzione base emettitore è certamente polarizzata in diretta. Inoltre,
   poichè il terminale di collettore è cortocircuitato a massa dall’induttore L, anche la giunzione base
   collettore è polarizzata in diretta. Pertanto il transistore lavora in regione di saturazione. Si osservi
   che essendo Vc,0 = 0 abbiamo Vbe,0 = Vbc,0 .

2. Sostituiamo al transistore il corrispondente circuito equivalente di Ebers - Moll, valido per arbitraria
   condizione di polarizzazione.
                                                               I BC
                                        B                                      C


                                    I BE                                  It

                                                                                   E

   Ricordando che:
                           It = βF Ibe − βR Ibc = IS (exp(Vbe /Vth ) − exp(Vbc /Vth ))                   (1)
   e che Vbe,0 = Vbc,0 abbiamo It,0 = 0. Pertanto le equazioni del circuito si riducono a:

                                            VCC
                               IR,0 =           ' 1 mA
                                             R                   µ             ¶       µ   ¶
                                                                       1    1     Vbe,0
                               Ib,0 = Ibe,0 + Ibc,0 = IS                 +    exp
                                                                      βF   βR     Vth
                                            Vi,0 − Vbe,0
                                Ri =
                                                 Ib,0

   da cui otteniamo:
                                                           µ                       ¶
                                                            Ib,0
                          Vbe,0    = Vbc,0 = Vth ln                       ' 0.6327 V
                                                     IS (1/βF + 1/βR )
                           Ic,0    = −Ibc,0 = −Ibc,s exp(Vbc,0 /Vth ) ' −980 µA

   e quindi Ri ' 4367 Ω.
   In alternativa possiamo ricordare che
                                          βF               IS
                          αF       =           = 0.98 =            ⇒ Ibe,s ' 2 · 10−16
                                        βF + 1          IS + Ibe,s
                                          βR               IS
                           αR =                = 0.50 =            ⇒ Ibc,s ' 1 · 10−14
                                        βR + 1          IS + Ibc,s

   da cui otteniamo

                                  Ib,0 = (Ibe,s + Ibc,s )(exp(Vbe /Vth ) − 1) = 1mA
                                                    Ã                     !
                                                      Ib,0
                                Vbe,0   = Vth ln               + 1 ' 0.6327 V
                                                 Ibe,s + Ibc,s

   e di conseguenza per le altre grandezze.
   Infine, un’altra possibilità per calcolare Ic,0 è quella di partire dall’espressione

                               βR − (βR + 1) exp(−Vce /Vth )           βR − (βR + 1)
              Ic,0 = βF Ib,0                                 = βF Ib,0               ' −980 µA           (2)
                                 βR + βF exp(−Vce /Vth )                 βR + βF
3. Poichè il transistore si trova in saturazione ed entrambe le giunzioni sono in polarizzazione diretta,
   abbiamo
                                  µ        ¶          µ                      ¶
                                   dIbe −1      1 IS       Vbe,0 −1
                         rbe =             =          exp(      )   ' 1280 Ω
                                   dVbe        Vth βF       Vth
                                 µ      ¶    µ                   ¶
                                   dIbc −1      1 IS       Vbc,0 −1
                         rbc   =           =          exp(      )   ' 25.5 Ω
                                   dVbc        Vth βR      Vth
   Per quanto riguarda il generatore controllato It = βF Ibe − βR Ibc procediamo calcolando le transcon-
   duttanze gm,e = ∂It /∂Vbe e gm,c = ∂It /∂Vbc . Otteniamo:
                                                 µ                   ¶
                                              IS       Vbe,0
                                  gm,e    =       exp(       ) ' 39.2 mS
                                              Vth      Vth
                                            µ                 ¶
                                              IS       Vbc,0
                                  gm,c    =       exp(       ) ' 39.2 mS
                                              Vth      Vth
                                                  4
   Poichè Vbe,0 = Vbc,0 abbiamo gm,e = gm,c = gd e dunque:

                                         it = gm,e vbe − gm,c vbc = gd vce                            (3)

   Il generatore it è dunque controllato dalla tensione ai suoi medesimi capi ed è pertanto assimilabile
   ad una conduttanza di valore gd che risulta connessa in parallelo al resistore R. Pertanto il circuito
   ai piccoli segnali risulta essere il seguente:

                       ii                  i BC
              vi                                                                     vo

                        Ri                       r BC
                                          r BE                     1_            R        sL
                                                                    gD



4. Definiamo Rx = R||1/gd . In base alle considerazioni di cui al punto precedente abbiamo:
                                                                rbe
                                         ibc =                              ii
                                                        rbe + rbc + RsR xL
                                                                      x +sL
                                                         sRx L
                                          vo =                    ibc
                                                        Rx + sL
   da cui otteniamo l’espressione cercata:

                    vo (s)    sRx L          rbe                     sLrbe
                           =        ·                   =                                             (4)
                    ii (s)   Rx + sL rbe + rbc + RsR+sL
                                                    xL
                                                          rbe + rbc + sL(1 + rbeR+rbc )
                                                            x                         x



   La trans-resistenza presenta quindi uno zero nell’origine e un polo con una pulsazione corrispondente
   pari a:
                                            Rx (rbe + rbc )
                                    ω=                        ' 1M Hz                                (5)
                                         L(rbe + rbc + Rx )
                                       
                                           
   !"#"$$" %  "#&#" "  $"$ '( "% ')  *$$+#%"#" *$* ",-
   . "#" % /0"."## 

                                                         VCC
                                                         RE
                                    I Bp   R BB
                                                               VO
                                                         QP
                           VBB +                                QN
                                   −              I Cp


   1"# 233 4 255 ')67'( 8 ')9 : ;<= >  '?? 4 '(@@' 8 = : ABCD EF G !#&#"
  ""$"-H" % IJ "K *"$"#" + $&& # %$"  G H" % IJ "K *"$"#" % #
  +"#& " +"$$"  233 # ,# L3M "K *"#" %  H"  N +"#& " % * "$" % IJ
  "K +$   23O % IPQ *"K %" R$%#" % , *0" *"## %  .   J"$#  !#&#"
  H" * "$" % IJ "K + $&& # #."$ " IJ  $. # $"!#" #$ "  *$."#%  $
    R",&#" %"  !  *+$"#%"#"  !#&#" ""$"-H" % IJ HHS
                           255 T 233 4 'O LUV 5M 8 'O L5 8 2O3 8 '33 L5M
                                                        M               UV                      79
  % $ ."$" *#!#"#"   $" &#" S
                                         2O3 4 2WX # YLLZ5M
                                                            [
                                                                                                7=9
  \ ."#% "$."#" "#S

                                   2O3 ]>^ L5M ]_`^ 23M ]>^
                                          C      Q=       -
                                   =     Q
                                       C QDabc      Q=
                                                  baQ         -
                                   d         <
                                       C QDc<D    baQac       -
                                   <   C QDc<a    baQab       -
                                   D   C Dc c     ba ab     Q< a=
   \  +"$#S L3M :  _` Q 23M : B <= 8 CBCA : B <a= >Q 2OM : =BCAA >Q L3e : AC _` Q
   L5e : < Ba ` 
= `  "+"$$ % d=C f HHS 2WX : CBC=AD= >Q LZ 7d=Cg 9 : < h Ci(j ` Q '(7d=Cg 9 :
   DABD EFQ ')7d=Cg 9 : <B A EFQ 'O 7d=Cg 9 : dBbD EFQ UV 7d=Cg 9 4 cC Q 233 4 B <= >Q
   '33 4 A< Bb EF N"$#% *" # +$"*"%"#& HHS

                                      2O3 ]>^ L5M ]_`^ 23M ]>^
                                   
                                   =        CQ QD   AdQD     -
                                          C QDcba   b AQ=b    -
                                   d            <
                                          C QDc<b     A Q<=
                                                    b Q<     -
                                   <      C Dc    A b A     Q< c<
    " +"$#S L3M : CBc<b _` Q 23M : B <= 8 CBCbd : B <c< >Q 2OM : =BCba >Q L3e : bAB < _` Q
    L5e : DB da `  N +# % .$ "K ,  # ,# " $""#&" % ""$" " H"
     %% #  $" &#" 'O  '33 6UV M 
d N . $" % 2 $*0" *#*%" *0$"#" *#  2O3 : CBDc<c > * *  # $+  +$
    ," 
<  N *$* ",. "#" +"$ +**  "!# " "K $ # !$ 

             vi                 i Bp                                    io      vo
                                                           i Bn
                                           β 0p iBp
                       R BB            r bep               r ben                 sC


                                                                    β0ni Bn
                                                RE




D G R"+$"#" %" !%!# +"$ +**  "!# " +K ""$" * *  * "#" *" "!" S
                                   
                                        4 Ue UM ?M                                            7d9
                                      4 T?M 7 ?M 8 'O 7UM 8 99                              7<9
                                   
                                        4 T                                                    7D9
   % * "#S                                Ue UM
                                      
                                         4    7 ?M 8 'O 7UM 8 99                               7b9
                                      
                                !#"$%'&' 
                                                       (() *+,-/..0
132465798;:<79=8;>@?BC A 7D?%EGFH?%I@>@?KJMLNJM= C I@F C 797POM8JM87D?Q:R: CTS > CUC 5VLN79L3:PL3>@> C :<8VI@>R8V79LWI@>RL3>R8V79LXF=A? C I<I C : C 79LQ5V7D?%5VL3>RL
    :P8VI@?%5;Y CTS JM?Z5 C[CT\ =ML3]T8V? S 8^7<O C 5 C9_ L S ?`5 C 7D?Q:<: CTS >R8a>@:<LG5;?Q:R?cb
                             d e     f         gihkjTlnmfigihTjTlnophqsr
                                                                       qut
                            jTlcvwf          jTlno xyjTz o xyjTzm{f|jTlnoh'} 1 x ~ H1  xq{r ~H1 + fijTlnoph'} 1 x ~ H 
                                                                                               qst                            
                            jTl f            jTlcvh q#
                                                       qu
                               jDf            jTl /xyjTz/xyjTz vf|jTl h'} 1 x ~c1  x q  ~c1 a fijTl +h} 1 x ~  ca
                                                                                              q#                           
     JLG79=M8IR8H:<879LTY3Lnb
                                             deKfgih q{r hh qu h                          jD                              gihTjD
                                                                                                                   f                                                          }1
                                                               qst q# } 1 x 6kt 3  } 1 x 6kt '  } 1 x 6kt   
      >R8V5V8V]9]TL S Jc?G5 C[CT\ =ML3]T8;? S 8I<7D:<8;>@> C I@?QFM:PLZF C :s8V5HF= S >@?`JM8HFH?%5VL3:<8;]9]TL3]T8V? ScC jDf GE`IR8H?Q>@>R8 CTScC b

                                                               jTl f                   j             f 13QQ3E`
                                                                                }1 x             t 
                                                                                            6k%
                                                               j lcv f          j l h qu fi %33E`
                                                               jTlnof                 jTlcq#v  fi QQ3E
                                                                                   }1 x t 
                                                                                             6k
                                                               j lnm f           j lno h qsr fi   33E`
                                                                d e f             gihkjTl qum t f    Q¡¢
 24£>@:<L S I<8VI@>@?Q:<8¤  C ¤ t I@? S ?W7D? SScC IRIR8LWJM8;?nJc?c¥ \ =M8 S J8 S ? S I@? S ?WL¦ C >@>R8{JL C ¦ C >@>@?¨§©L3:<5Vª «F C :<798kA? SMC 5
     5V?Q:R?`79LQI@?¬®­°¯ f²± 2³? S 5 C 7D?Q:R: CTS >R8a79LQ57D?%5VL3> C ¥ _ 58LQ5;>@:<8HFL3:PLQE C >@:<8JM8;¦ C : CTS ]T8VLQ5V8^J C 8 \ =ML3>@>@:R?´>@:<L S IR8VIR>@?Q:<8
    FH?%IRIR? S ? C IRI C : C 79LQ5V7D?%5VL3>R8^Y C 5;?n7 C E CTS > C b

                                                               ~¶ dM·V¸
                                                    f
                                          ¬kµ ¯                  j l f   %¹
                                                                                               Md º$xd lH»¼ ¶    Md º f  Q¾¹
                                             ¬kµ ¯ vwf 1TQ¡ %¹ « ¬ ­°¯ v f                          jTlcv     ½ jTcl v  ¡
                                              ¬kµ ¯ o f 1k Q'¹
                                               ¬kµ ¯ m f   % ¹ « ¬k­°¯            m f ¡Q ¡  ¾¹

 2465^798;:<79=8;>@? CT\ =8;YLQ5 CTS > C LQ8^F 8V797D?%5V8^I C9_%S LQ58sC A 8V5^I C9_ = CTS > C b

              ii                                           i be2                                                         v be4                            vo
             vi
                          r be1              βoi be1                                   i be3
                                                                                                βoi be3                     βoi be4
                                                              βoi be2
               i be1                                                                                                                                         R
                               C
                                                             r be2         r ce2               r be3             r be4      i be4       r ce4
        L C I<I@?IR8H:<879LTY3L S ?5 C I C9_ = CTS >R8 CT\ =ML3]T8V? S 8 b
                                               f ,µ ¯ x3nx ~¶ µ ¯ x ¬k µ ¯  v f3 } ~ ¶¬kµ x ¯ 1  x  x ¬kµ 1 ¯ v
                                   ~¶ ,µ ¯ v f ~ ¶   f µ ¯ m 1 x } ~ ¶ x 1  x 1
                                                                 ¬kµ ¯ v                    ¬®­°¯ v             ¬kµ ¯ o                ¬kµ ¯ m
                                                                        µ ¯ m
                                            f  ~¶ ¬kµ ¯ m } g ¬k­°¯ m 
      C I@FM: C I<IR8;? ScC J C 5V5LG79L3:<L3>@> C :<8VI@>R879L`8 Sc_ : C I<I@? =MIR798;>RLZ:P8V7<OM8 C I@>RLGJMLQ5 \ = C IR8;>@?C  ¥MF C :R>RL S >@?cb
                                                 f                                            ~ ¶  } g ¬k­¯ m 
                                                                                                                                                                           } 
                                                   ¬kµ ¯ m ¬kµ ¯ v    v x"! $)#&( /% o ' x (   m+*  ! $)#,( /% ' x  x )(   v+*
 2u³?%E C I<8Y C J C JMLQ5V5  C I@FM: C IRI<8;? ScC I@?QFM:PL#:<8VF?Q:<>RL3>RLn¥ 8V5:<L3FMFH?Q:R>@?  .-   FM: C I CTS >RL= S FH?%5;?c20/ C :JM8VE CTS I<8;? S L3: C
    5LG79L3FLQ798T`AL 8 S E`? Jc?`JLGI@? JJM8VI&1 L3: C 8V5HYn8 S 7D?%5;?GIR=M55VL21 : CT\ = CTS ]TLGJ C 5^FH?%5;?c¥43 LQI@>RL \ =M8 S JM8FH?Q:R: C b
                                                                   f 571 6  ~¶¬kµ x ¯ 1 x ¬®µ 1 ¯ v+ fi   987:                                                  } 
                 Soluzione del compito di Fondamenti di Elettronica
                                  6 Settembre 2006
1. Sostituendo i transistori npn con i loro circuiti equivalenti a 3 parametri si disegna il circuito ai
   piccoli segnali:

                      i be1                  vout1         i be2    r be2               i out2
                                                                                                 vout2
                              β01 i be1
                 r                                r01                             r02            R2
                                                           R1
                     be1
                                                                   β 02 i be2



   e risolvendo il circuito é possibile scrivere le espressioni per le correnti e le tensioni:

                                                                               r02
                                          iout2      = (β02 + 1)ibe2 ·
                                                                            r02 + R2
                                                       vout1 − vout2
                                             ibe2 =
                                                            rbe2
                                          vout1      = −(r01 k R1 )(ibe2 + β01 ibe1 )
                                          vout2 = (r02 k R2 )(β02 + 1)ibe2
   da cui si ricava:
                               iout2    (β02 + 1)r02                 β01 (r01 k R1 )
                      Ai =           =−              ·                                                   (1)
                                iin1      r02 + R2     rbe2 + (r01 k R1 ) + (β02 + 1)(r02 k R2 )
2. Partendo dai parametri differenziali, si possono calcolare le correnti di polarizzazione dei due tran-
   sistori:

                                              VA1                           Vth
                                   IC1 =          = 1.5 mA             IB1 =     = 12.5 µA
                                              r01                           rbe1
                                              VA2                           Vth
                                   IC2 =          = 4 mA              IB2 =      = 40 µA
                                              r02                           rbe2
                                                                                                         (2)
   a cui corrisponde un valore di β01 ≈ βF 1 = 120 e β02 ≈ βF 2 = 100
3. Considerando la configurazione dei transistori bipolari si possono scrivere le seguenti equazioni per
   le correnti e tensioni di polarizzazione:


                                             VCC        = Vce0,2 + R2 (IC2 + IB2 )
                                             VCC        = Vce0,1 + R1 (IC1 + IB2 )
                                                                                                         (3)

   da cui si ottiene R1 = 1948Ω e R2 = 743Ω a cui corrisponde Ai = −277.3.
4. La funzione di trasferimento del circuito presenta un polo che puó essere facilmente calcolato con-
   siderando l’espressione del partitore di corrente tra iin1 e iin . Infatti scrivendo:

                                             iout2   iout2 iin1   iout2      1
                                      Ai =         =      ·     =       ·                                (4)
                                              iin     iin1 iin     iin1 1 + sCrbe1
   per cui il valore di capacitá necessario per una frequenza di taglio fT = 50 MHz é:

                                                              1
                                                     C=              = 1.6 pF                            (5)
                                                           2πfT rbe1
                                  !#"$%'&' 
                                                         (*) +*&% (-,, .
  /10#/3254!687:9<;>=@?A=@68B<7:?CD/FEGC5HI=@B%;JBLKMB%;>;JEN=:=@?O9QP>?RBSPJBJ0UT EV7@6@9<;68BW;>B%;YXZB%=@=8B%;JBQ[\9<? 687@B^]_917`=@?O?A;Y7@EVa%?RB%;JEGP>?
            =:916@bJ7:91cN?RB%;JEBG?d;']<EV7:=:9S0feO=:=@?-=@917`9<;>;JBUPb>;>ghbJE#?A;L7@EVa%?RB%;JEi;JB<7:[\9<jRE$klP>?RBSPJBGm!n52B<X>XbJ7@E?A;L?A;68EV7:P>?AcN?RB%;JE
                 klP?RBhP>Bom!pp 2`0T EV7QqJrtsvuxw1yzjAEQa%?Ab;JcN?RB%;>?f{9<=8E^|^EN[}EV686@?A68B<7@EYP>?C5~EC5H=8B%;JBoKMEV7@6@9<[}EN;68E=8XZEN;68E<0
             T EV7@6@9<;68BI?Aj*P>?RBSPJBUKMB%=86@?A6@b>?R68B$P>9$CHIEF      m!ppE}ghb>?A;>P>?-;JB%;LX b*BU           =@KMB<7:7@EV7@EDKMB<7@7@EN;68E\P>?EN[}EV686@?A68B<7@E}?A;C~h0
      4 ;JB%jR687:EF?AjOP?RBhP>BWCD/IE$           KMB%;>;JEN=@=@BWKMB%;?Aj 68EV7`[\?A;>9<jRELX*9<jAj9<jA?A[}EN;6@91cN?RB%;JEF[\EN;'687@E$?AjO68EV7:[\?A;>9<jAEIX*P>ENjAjA9
       a%?db>;JcN?RB%;JEP>?*C5~IE             KMB%;>;>EN=@=8BU9G[\9<=@=:9S0T*EV7:6@9<;'68B$jA9\a%?db>;JcN?RB%;JEP>?*C5~E                 XZB%jA917:?AcVcN916@9F?A;I?d;']<EV7:=:9S0
                C5bJEN=868BW9Q=@?K`JE$9<;>K:JEIC5~L=@?A9L=@XEN;68BWEUK:>EG;JB%;=@KMB<7@7`9QKMB<7@7:EN;'68E$;JEVX>Xb>7@EF;JENjP>?RBSPJBLKMB%=86@?A6@b>?R68BQP9<j
        687`9<;>=@?A=868B<7:E$CD/10T EV7FqJrtsuq?A;']<ENKME=@?>9Qb>;>9QB<7@6@?d=@=@?A[\9IXB%jd917:?RcVcN91cN?RB%;JEGP>?R7@EV686@9W=@b>jdjRE\a%?Ab>;>cN?RB%;>?
              eP?C5~FEFC5Hh0-9$KMB<7@7:EN;'68E\P>? KMB%jAjREV6868B<7:EDP?C5~G=@KMB<7:7@E}9168687:9N]<EV7:=@BQCD/iEDP>EV68EV7:[\?A;>9Gb>;Q]_9<jAB<7@EiP?q>
               ?d;JEV7`?RB<7@E!9Uq0OT EV7@6@9<;68BU?687:9<;>=@?A=@68B<7:?-CD/!EiC5HD=@B%;JBGm!n[}EN;687@EiC5~$E#                   =:916@bJ7@BJ0
~h0f~%2{>{ ?A9<[}BJ
                                  V¡ u V¢ £¤h¥ ~#u§¦¨ £ / N© EMªSXkq« V¬ q>­A®2 u V¢¯ £¤¥ Hu§¦¨ £ / N© EMªhXikq>« ¯3¬ qJ­A®'2
                                                                   ¦¨                                                                     ¦¨
          P9}KVb>?±°JXZEV7gb9<jA=@?A9<=@?q>rtsUXZEV7jA9}ghb>9<jREC5~iEDC5H}=8B%;JBUm5n
                                                                                       q>«  uq« ¡¯ u q>~      rts
                                                                                                                        ²
         4 [}XZB%;JEN;>P>BDK`JEiC5~D=:?687@B3]S?9<jAjd9}=8B<a%jA?A9}PJENjdjA9D=@916@bJ7:91cN?RB%;>E<°P>9<jAjA9D³5P>ENj;JBhP>B}´B<6868EN;?A9<[}BJ
                                                                © EMªSXLµ q>rts u ¦¨ £ /  © EMªhXLµ qW·q>rts
                                                                             ~%q>­A®Z¶           ¦¨                              qJ­A®        ¶
                                                                                                                  £
                                                              q>rtsDu ~H µq £ q>­A® jA;µ ¦¨ / ¶ ¶¤¸ / ² H<H_¹$q ²
                                                                                                              ¦¨
 Hh0fH%2 4 j>KV?R7:KVb>?A68BENgb?R]_9<jAEN;'68EfXEV7X?AKVKMB%jA?=8EVa%;>9<jA?-Eº       [}B%=@687:9168Bi?d;\p?RaJ0A/10»S?Ef 687:9<=@KVbJ7`9168Bij±EM¼ZEV6868B}eO917:jA½iKMB%[}E
           =:bJa<a<EV7:?R68BFP9<jAjA9D[\9<;>KV9<;JcN9FP>?9<jAKVb>;]19<jRB<7@E5XZEV7jA9D68EN;=@?RB%;JEP>?e917:jR½<0

                                                            ib                                                vx
                                                vin                               β 0 ib
                                                                      r be                                        r d1                  C
                                                                              vy
                                                                                                                                        L
                                                                      rd3


                                                                                    p 48¾5¿fÀf§/

        nfENjKV9<=8Bq rts uÁ/My+91{>{?A9<[}BFq« ¡ uq>« ¯ uÂw ²ÄÃ yÁEXZEV7@6@9<;68B
                                                     V u V¡¯ u ¦ ¨ £ / N© EMªSX µ w ²ÄÃ                           /ÅÆ
                                                                             ¦¨                      >
                                                                                                      q A
                                                                                                        ­ Z
                                                                                                          ® ¶   
                                                                                                                ¸  h
                                                                                                                   Ã  ²
      P9YKVb>? V¢ u V¢¯ uÇ¹ ²ÄÈ<Ã Å° V¢ É uÊ¹ ²ÄË ~Å#°  « u  « ¯ uÇw ² ~_¹'HYÅ°  « É uÌw ² ~<HS/LÅ#0Of{>{?d9<[}B
       9<jdjRB<7:9GÍ3«  uÁÍ3« ¯ uÎ/Vw%HÏJÐ!°Í3« :É uÎ/Vw ÏJÐ!0i-ED7@EN=@?A=868EN;>cVEDP?t¼EV7:EN;JcN?A9<jA? P>? CD/iEFC5HG]_9<jAa<B%;JBIgb?A;>P>?
     Í^Ñ ¯ uÒÍ3« ¯N¬ k ¦Ó £ /32 ¸ ¹'Ô1w<w%Ð5°Í3Ñ É uÂÍ3« @É`È ¬ k ¦Ó £ /32 ¸Ã /M¹%w%Ð!0
¹J0¹2EENghb>91cN?RB%;>?K`JE#PJEN=:KM7:?R]<B%;JB\?AjKV?A7:KVb>?R68B}ENghb>?R]19<jREN;68E=8B%;JBJ
                                                          MØÙ
                                       Õ k±Ö12×u Ö Ù £ /
                                                             Ö
                                                                                                              Õ
                                     q  k±Ö12×u ·ik Õ k±Ö12VÚRÚ Í3Ñ É 2 ¦ Û  rÜsZk±Ö_2Ouv· Í3« k £ k±Ö1k 2VÚRÚ Í3Ñ £ É 2 /3¦ 2¡Û Í3Ñ ¯ qJrtsk±Ö_2
                                                                                                                  ¦Û
P9}KVb>?±
                                          q  k±Ö12 u·µ                  
                                                                           ¦  Û Í3Ñ É                Ö ØÙ £ /
                                         q>rtsk±Ö12              Í^« ¡ £ k ¦ Û £ /32¡Í3Ñ ¯ ¶ Ö ØÙ £ Ö3Í3Ñ É Ù £ /                                             k /32
 *9KVbJ7@]19P>?a%b>9<P>91a%;>BIX>7@EN=8EN;6@9IP>b;>gb>EDb;]_9<jRB<7:E ;>?R68BYkl;JEVa%916@?R]<B2XZEV7  wEFXEV7  Ò°-cVEV7`?
  ?d[\[\91a%?A;>917`?KMB%;?AbJa%916@?9<jAjd9DXb>jA=@91cN?AB%;JE  Û uÁ/ ¬  ØÙ E#P>b>E5XB%jd?9\7@ENghbJEN;JcVE#7:?A=8XZEV686@?R]19<[}EN;68E!?d;JEV7`?RB<7@E
E=@bJXZEV7:?RB<7@E!9 Û 04 jP>?Aa<7:9<[\[\9Dghb>9<jA?R6@916@?R]<BUPJENj[}BSP>b>jRB}PJENjZa%b>9<P91a%;JBFP>?Z68EN;>=:?RB%;JEE# ?Aj=@EVa%bJEN;'68E<

                                      M




                                                                                            1                  ω
                                                                                  LC        2

                                                                      p 48¾5¿fÀfÁ~
                 Soluzione del compito di Fondamenti di Elettronica
                                   2 luglio 2007
1. Fino a che la tensione Vin non é sufficiente per mandare in conduzione il diodo, la base del transistore
   risulta isolata. Per tanto il transistore rimarrá spento fino tanto che Vin < 0.6 V. Per Vin > 0.6 V,
   il transistore comincia a condurre in regione normale e sulla sua giunzione base-emettitore cade una
   tensione VBE = Vin − Vγ . Per cui risulta:
                                                          µ             ¶
                                                      Vin − Vγ
                                          IC = IS exp
                                                         Vth
   Di conseguenza la tensione VO risulta:
                                                              µ               ¶
                                                                   Vin − Vγ
                                     VO = VCC − RIS exp
                                                                      Vth
   Per tensioni Vin elevate, il transistore Q entra nella regione di saturazione e VO = VCE,sat . Questo
   accade quando la tensione di collettore scende fino al valore di tensione della base:
                                                                   µ              ¶
                                                                       Vin − Vγ
                                  Vin − Vγ = VCC − RIS exp
                                                                          Vth
   Risolvendo iterativamente quest’equazione non lineare, si ottiene:

                                                 it.     Vin [V]
                                                  1        0.8
                                                  2       1.273
                                                  3       1.270
                                                  4       1.270

   per cui il transistore entra in regione di saturazione, quando Vin = 1.27 V. La caratteristica statica
   del circuito é la seguente:


                       VO
                         5


                                                                            V CE,sat
                     0.15
                                    0.6 1.27                                          V in

                                              FIGURA 1

2. Il valore di VCE,sat vale:
                                                    µ                   ¶
                                                        σβF + βR + 1
                                 VCE,sat = Vth ln                           = 0.15V
                                                         (1 − σ)βR

3. Il circuito equivalente per piccoli segnali è mostrato in Fig.2.
                                                     C2

                                                     C bc
                          vin

                                     C be             β 0 ib
                                              r be                     rO
                          C1                                                  R
                                       ib            vy

                                              rd3


                                               FIGURA 2

   Per Vin = 1 V, il transistore lavora in regione normale, per cui la corrente di collettore vale:
                                                     µ             ¶
                                                Vin − Vγ
                                    IC = IS exp                        = 88.8nA
                                                   Vth
   per cui si ottiene:
                                                          β0 Vth
                                        rBE =                    = 28.1M Ω                            (1)
                                                           IC
                                                          VA
                                             r0 =             = 338M Ω                                (2)
                                                          IC
                                                           β0
                                            gm =                = 3.56µS                              (3)
                                                          rBE

   Il guadagno di corrente di corto circuito é espresso come segue:
                                                               ³     0    ´
                                                                   sCBC
                                                          β0 1 −    gm
                                     Ai,CC =          0     0 )r
                                                   s(CBC + CBE  BE + 1

         0
   dove CBE                 0
            = CBE + C1 and CBC = CBC + C2

4. Il polo e lo zero del guadagno di corrente di corto circuito valgono:
                                                              1
                                            ωp =            0      0 )                                (4)
                                                      rBE (CBE  + CBC
                                                       gm
                                            ωz =        0                                             (5)
                                                      CBC

   per cui i valori di capacitá necessari sono C1 = 4.9 pF e C2 = 2.96 pF.
   Il valore del guadagno di corrente di corto circuito a ω = 20 krad/s é pari a Ai,CC = 14.84.
                                !#"$%'&' 
                                                       ( ) *+,*-/.. 0
 132465879;:<>=@?;AB5DCFEG=GHI=J?;KL5D5DCNMO=GHIHIKL:<>K?;A8P CGQ>KSK   R TUCGMVAD5DWSKL:<>K?XKV<>KVHYW@AZ:;C3PAD5[K!MO=%:\<>KLMV:ADMY]XK:X=G<>KG2
                                                                        ^;_`ba ^;cDd 5D:eUfgh `Ii hLjk                                                   e61Fk
                                                                          h `ba e ^ lBlnmo^;_` k iqpr                                                        ets%k
     4<>KVHYCG:;?;=S<>HYC@5[K?;9;KuKLv9;C3wLAD=%:;ABCS7C3HI<IADHIKu?;CG5D5DCSA[78=G<>KLQIABAZ:;A[wLADCG5[K ^_*` ayx{z}|N~ =G<><>KL:;AZCGWS=X
         AD<>KVHL2          ^_*`                 h`
                   1         x 2|             |3x3
               s       x 2 1LGsq        | 2}G 
                    x 2 1 |GG|   | 2}G x  
                     x 2 1 |G Gs  | 2}G x  
       KVHI<ICG:<>=hV a fgh `S s z  x W@M]XK\ADWS7 5DADMVC p!\a| 78KVH=G<><>KL:XKVHYK9;:;CnMVCG?;9X<IC?;A<>KL:;QIAD=%:XK
       ^  _ a 1 z}|N~ 2
s 2465BMVA[HYMV9A[<>=SKLv9A[EqCG5DKL:'<>K?;A87 ADMVMO=%5[=@Q>KV%:;CG5DKSK
                                                                               R AD:;?ADMVC3<>=SAD:$;%9XHYC{2

                                vi                       vy                                             vx
                                                                                                                                   vo

                                          C1                   r                      β 0 i be             r        C2
                                                                   be

                                                  i be                  L                                      R2                       RL


                                                               R1



                                                                             4>u¡¡1

    4 7C3HYCGW@KV<>HYA?;A£¢8KVHIKL:XwLAZCG5DA QI=%:X=¤?;C3<IA?CN¥ `t_¦^;cDdi h `§| @!¨X©3ª a f« i ¥ `t_ 1L%qWJ¬82
     
 2®­!CG5MVADHYMV9;A[<>=SKLv 9;A[E3CG5[KL:<>KQ>=G7;HYCNHYAD7=GHY<IC3<>=S=G<><>KL:;ADCGWS=X
                                                                           p!±                               p!±                 p! e61 ³¸´3µOp!± k
                                                      ¯G° a p²±N³ 1 i3´3µ ¯q¶ a p!±N³ 1 i3´qµ f «O· `t_ 1 ³´qµ e p!±N³¸p² k                                         et%k
                         · `t_ e¹f « ³ 1Fk ³ ´¯3» º a ´qµ r e ¯3¼ m ¯3º k                                                                                                  e¹k
                                                    · `t_½a p r ¯3³ º ¥ `t_                                                                                                 e| k
      ?CSMV9;AB=G<><>KL:;ADCGW@=
                                                                ´qµ r ¯3¼ a ¯qº¿¾ e¹f`t_« ³À    ³ 1Fk ³ 1 ³¸´qµ r>Á
                                                                                                    pr ´F»                                                                 et%k
                                                                                       ¥
     Kv9;AZ:;?;A
                                      ¯G° a                                                ´ÂLµ r µVp!O» f «
                                                        À
                                                        ³ q
                                                          ´ 
                                                            µ      !
                                                                    p S
                                                                      ±  À
                                                                         ³  !
                                                                            p           ´   µ r »n³´F» e¹f « ³ 1Fk i e¹¥ `t_ ³Àp r k ³ 1Fk                               eÃGk
                                       ¯3¼      6
                                                e 1               e              >
                                                                                 k O
                                                                                   k e
X2®­!CG5D5D=ÄQ><I9?;A[=¤?XKL5/79;:<>=$?;AÅ5DCFEG=GHI=$KO¢KV<><I9C3<>=\AD:7HIKLMOKL?XKL:XwLCÄQIC37;7AZCGWS=JM]XKSC ^  _ a 1 z}|J~ MO=GHIHYAZQ>78=%:;?XK
       h l a s z ;1ÆW@2/²QIQI9WSKL:;?X=n9;:;C\HYKL5DC3wLA[=%:XKÄ5DAD:XKLC3HIKJh lÇ ^  _ AD:HIKV%A[=%:XKÄ5DAD:XKLC3HYK¤78=%QIQIADCGW@=\EqCG5Z9X<IC3HIK$5DC
    HYKLQIADQ><>KL:XwLC²?;A9;QIMVA[<IC¡?XKL5'<>HCG:;QIADQ><>=GHAD:#¥ °  e ^;È³@^  _ k i hV  3qG!2  KVHI<ICG:'<>=!78=%ADM]8KR 5DC¡MO=GHIHIKL:<>K?;A%PCGQIK
     Ku5DC<>KL:;QIAD=%:XK ^`t_ Q>=%:X=¿QIQYC3<>K!?CG5MVADHYMV9;A[<>=¿?;A AZ:XGHIKLQIQ>=NC3P;PAZCGWS=M]XKuAD5<>HCG:;QIADQ><>=GHYK¡KL:<>HYCNAD:ÄQIC3<I9XHYC3wLA[=%:;K
      78KVH9;:;C<>KL:;QIA[=%:;K ^  _ a¦^`t_Éx{z  1 |G  2²585DADW@A[<>K¡?XKL5D5DCQIC3<I9XHYC3wLA[= KuAD5;<>HCG:;QIADQ><>=GHYK²QIA <>HI=EGKVHIKVP;P8Ku?;9;:;v 9XK
        CNMO=%:;?9XHIHIK!9;:;C¿MO=GHIHIKL:<>Kh l a s z ;1uÊ ¸m e61 z}|¡mnx{z  1 |G k i 3qG  s z 3SW¤¦Q>=%Q><ICG:XwLAZCG5DWSKL:<>KAD?XKL:<IADMVC
         CG5Z5DC²7;HIKLMOKL?XKL:<>KG2,45{E3CG5[=GHIK?A{HIKLQIADQ><>KL:;wLC p² M]XK78=GHI<IC!Cv 9XKLQ><ICuQIA[<I9C3wLA[=%:XK!K
                                                                                                                                      R et mSx{z  1 |G k i s z 3  G%#!2
           KVHI<ICG:<>=J5ZCNEqC3HYAZC3wLA[=%:XKu78KVHYMOKL:<I9;CG5[KËK Ì p   1 xGx@Í etG% m| Gk i3|  | %ÎÄ2
                   Soluzione del compito di Fondamenti di Elettronica
                                   05 settembre 2007
1. Dato il valore relativamente basso del parametro βF = βF 1 = βF 2 dei transistori non è lecito
   trascurare la corrente di base dei medesimi. Pertanto le equazioni che descrivono il funzionamento
   del ramo sinistro del circuito sono:
                                                                 µ                        ¶
                                          VCC,1 − Vbe                1     A2
                                 IR1    =               = IC1 1 +      +                                  (1)
                                               R1                   βF   A1 βF
                                                 µ                               ¶
                                                                IR1
                                 Vbe    = Vth ln                                                          (2)
                                                   A1 JS (1 + 1/βF + A2 /A1 βF )

   Con la consueta procedura iterativa a partire da Vbe = 0V otteniamo :
    iter.       Vbe             IR1
      1        0.0 V          500µA
      2     0.569414 V       443.06µA
      3      0.56629 V       443.37µA
      4      0.56631 V       443.37µA
   Pertanto IC1 = IR1 /(1 + 1/βF + A2 /A1 βF ) ' 341.1 µA, che implica IR2 = A2 IC1 /A1 ' 1.706 mA.
   Dalla relazione R2 = VR2 /IR2 = R20 + R21 · VR2 otteniamo:

                                              R20 IR2       11.94
                                  VR2 =                 '            ' 14.39 V                            (3)
                                            1 − R21 IR2   1 − 0.1706
                                   Vo     = VCC,2 − VR2 = 25 − 14.39 ' 10.61 V                            (4)

2. Il circuito equivalente di piccolo segnale è indicato in figura.




                                                                                              vo
                                                                     i b2
              ii                       i b1                                    β 0 i b2
                                                       β0 i b1                                     r d2
                            R1                                        r
                                       r be1                              b2




   I parametri differenziali dei transistori sono dati da: rbe1 ' Vth /Ib1 ' 1512 Ω; rbe2 ' Vth /Ib2 '
   302 Ω. Per quanto riguarda R2 dalla definizione abbiamo VR2 = R20 IR2 /(1 − R21 IR2 ) e pertanto:

                           dVR2        R20                    7000
                   rd2 =        =               2
                                                  '                            ' 10.2 kΩ                  (5)
                           dIR2   (1 − R21 IR2 )    (1 − 100 × 1.706 × 10−3 )2

3. Dal circuito equivalente sopra riportato otteniamo:
                                                    rd2
                           vo = −rd2 β02 ib2 = −         β02 [R1 ||rbe2 ||(rbe1 /(βo1 + 1))] ii           (6)
                                                    rbe2
                                                                                                          (7)

   da cui otteniamo vo /ii ' −32.31 × 103 .
                Soluzione del compito di Fondamenti di Elettronica
                                18 settembre 2007
1. In condizioni stazionarie l’induttore si comporta come un corto circuito ed il condensatore come un
   circuito aperto. Poichè vengono assegnati i valori delle tensioni di soglia Vγ,BE e Vγ,BC procediamo
   utilizzando il semplice modello a squadra delle caratteristiche del transistore. Le equazioni che
   descrivono la relazione tra Vo e Vi sono:

                                  Vo = Vi + Vγ,BE − Vγ,BC ,                                          (1)
                                                    µ                ¶
                                                      0 − Vi − Vγ,BE
                                  Vo = VCC − RC βF                                                   (2)
                                                            RB
                                  Vo = VCC                                                           (3)

   nelle regioni di funzionamento di saturazione, normale e di interdizione, rispettivamente. La terza
   equazione è valida per Vi ≥ −Vγ,BE . La seconda è valida per Vo ≥ Vi +Vγ,BE −Vγ,BC = Vi +VCE,sat .
   La pendenza media della retta che descrive il funzionamento del transistore nella regione nor-
   male di funzionamento è dunque RC βF /RB ' 250 La caratteristica statica assume dunque l-
   aspetto indicato in figura. Per Vo = 0 V abbiamo IC = VCC /RC ' 0.6 mA, IB = 12 µA.
                                                         Vo

                                                                  V CC


                          −V CC                                                      V CC
                                       (−0.513,−0.313)
                                                                  −V γ,ΒΕ                   Vi


                                                                   −V CC


2. Il circuito equivalente di piccolo segnale è rappresentato in figura.

                                  vi                                        β 0 ib
                                            ib
                                                         r
                                                             be                vo


                                                                            RC
                                            RB



                                       C                          L


   I parametri differenziali del transistore sono dati da: rbe ' Vth /IB ' 2150 Ω e quindi gm = IC /Vth '
   23.3 mS.
3. Indicando con Z l’impedenza risultante dal parallelo dell’induttanza L e della capacità C (Z =
   sL/(s2 LC + 1)) abbiamo:

                                                vi RC
                           vo = RC β0 ib = +β0                                                 (4)
                                            RB + rbe + Z
                          vo                   (s2 LC + 1)
                               = +RC β0 2                                                      (5)
                          vi           s LC(RB + rbe ) + sL + rbe + RB
                                                               √ −1
  Il circuito presenta due zeri immaginari coniugati per sz = j LC = j31.62 Mrad/s e due poli
  complessi coniugati alle pulsazioni:
                                               p
                                        −L ±   L2 − 4LC(rbe + RB )2
                                sp =                                                           (6)
                                              2LC(rbe + RB )
                                sp   = 0.158 ± j31.62 Mrad/s                                   (7)

  Il diagramma di Bode del modulo del guadagno è illustrato nella figura sottostante.

                  M




                                                        1             ω
                                                   LC   2
                Soluzione del compito di Fondamenti di Elettronica
                                 19 dicembre 2007
1. Si tratta chiaramente di un amplificatore basato su transitore pnp in configurazione base comune
   pilotato in corrente. La capacità Cbc è in parallelo alla resistenza di uscita. La capacità Cbe è in
   parallelo alla resistenza differenziale base/emettitore del transistore. La funzione di trasferimento
   può essere facilmente calcolata dalle seguenti equazioni:

                             veb = rbe ib                                                              (1)
                             ig = (β0 + 1)β0 + veb sCbe                                                (2)
                                               RL
                             vo = β0 ib                                                                (3)
                                        1 + s(CL + Cbc )RL
                             vo          β0       1                 1
                                = RL                                                                   (4)
                             ig       β0 + 1 1 + s Cβbe+1
                                                       rbe 1 + s(C + C )R
                                                                  L   bc L
                                                     0



                                                    β 0 ib
                                                                                vo
                    ig         ib
                                                  C be            C bc    CL
                               r be                      RL




2. Lo specchio di corrente ha la semplice topologia di Figura. Poichè le correnti di collettore dei due
   transistori dello specchio (IC ) sono identiche abbiamo: Veb = Vth ln(IC /IS ) ' 0.6332 V e quindi
   RX = (VXX − Veb )/(IC (1 + 2/βF )) ' 12650 Ω.


                             VXX
                                                         CL

                                             IC
                                                                 VO
                                        RX
                                                                  RL

                                                                 V YY


3. Poichè abbiamo Ie = 100 µA, Ib = 3.85 µA, Ic = 96.15 µA, otteniamo rbe ' 6500 Ω e gm ' 3.85 mS.
   La frequenza dei poli è pari a f1 = 1/(2πRL (Cbc + CL )) ' 14.6 MHz, f2 = 1/(2πrbe (Cbe )) '
   81.6 MHz.
                 Soluzione del compito di Fondamenti di Elettronica
                                   19 marzo 2008
1. La tensione Vi,0 di ingresso è irrilevante sul funzionamento statico del circuito per via della presenza
   del condensatore Ci . I transistori operano tutti in regione normale o al limite tra questa e la regione
   di saturazione. Inoltre, considerata la perfetta simmetria del circuito possiamo certamente dire che
   Vo,0 = 2 V. Per calcolare le correnti nel ramo di T1 e T2 possiamo procedere ricordando che T1
   e T2 non sono soggetti ad effetto Early (in quanto la loro tensione Vcb = 0 V); la simmetria del
   circuito porta a scrivere l’equazione:


        VCC   = Veb,1 + Vbe,2 + Rn IC,n (1 + 1/βF 0,n + A/βF 0,n ) + Rp IC,p (1 + 1/βF 0,p + A/βF 0,p )
              = 2VBE + (Rn + Rp )IC (1 + 1/βF 0 + A/βF 0 )

   dove VBE = Veb,1 = Vbe,2 , IC = IC,n = IC,p , βF 0 = βF 0,n = βF 0,p , a cui si accompagna l’equazione
   che descrive la regione normale di funzionamento dei transistori T1 e T2:

                                            IC = IS exp(VBE /Vth )                                        (1)

   Otteniamo pertanto:
                                                     VCC − 2VBE
                                   IC   =                                                                 (2)
                                          (Rn + Rp )(1 + 1/βF 0 + A/βF 0 )
                                 VBE    = Vth ln(IC /IS )                                                 (3)

                                                             VBE        IC
                                                 iter.       [V ]      [µA]
                                                   1       0.00000    363.636
   Iterando tra queste due equazioni si ottiene:   2       0.62737    249.568
                                                   3       0.61766    251.334
                                                   4       0.61784    251.301
                                                   5       0.61784    251.301
   La corrente di collettore di T3 e T4 si ottiene

     IC3,4 = A(1 + VCB,4 /VA )IS exp(VBE /Vth ) = A(1 + VCB /VA )IC ' 5 · 1.0276 · IC ' 1.291 mA (4)

2. I parametri differenziali dei transistori valgono:


                                                     Vth βF 0
                                 reb,1 = rbe,2 =              ' 5133 Ω
                                                       IC
                                                     Vth βF 0
                                 reb,3 =    rbe,4 =           ' 1027 Ω
                                                      5IC
                                  ro,1 =    ro,2 = ∞
                                                    VA
                                  ro,3 =    ro,4 =      ' 39793 Ω
                                                    IC
                                  β0,1 =    β0,2 = βF 0 = 50
                                                         µ           ¶
                                                               VCB,4
                                  β0,3 =    β0,4 = βF 0 1 +            ' 51.4
                                                                VA

3. Il circuito equivalente per piccolo segnale è mostrato in figura. Le grandezze ivi riportate hanno le
   seguenti espressioni:
                          vi                                                                      vO
                                C
                                           Rn       Rp                  r on               r op


                                    iben    i bep           β 0n iben          β 0p ibep
                          rnx
                                rbe4       rbe3

                                                     r px




                                                            Vth βF 0
                                reb,1 = rbe,2 =                      ' 5133 Ω
                                                               IC
                                                            Vth βF 0
                                reb,3 =             rbe,4 =          ' 1027 Ω
                                                              5IC
                                                      rbe,2
                                rnx =                        ' 103 Ω
                                                    β0,2 + 1
                                                      reb,1
                                    rpx =                    ' 103 Ω
                                                    β0,1 + 1
                                    ron =           rop = ro,3 = ro,4 ' 39739 Ω
                                β0n = β0p = β0,3 = β0,4



L’espressione del guadagno di tensione richiesto risulta dunque:

            vo (s) = −(βon iben + βop ibep )(ron ||rop )                                               (5)
                                                     rnx               vi (s)
                   = −(βon + βop )(ron ||rop ) ·            ·                                          (6)
                                                 rnx + rbe,4 (2/sCi ) + Rn + rnx ||rbe,4
            vo (s)                                   rnx               sCi /2
                   = −(βon + βop )(ron ||rop ) ·            ·                                          (7)
            vi (s)                               rnx + rbe,4 1 + sCi (Rn + rnx ||rbe,4 )/2

La funzione di trasferimento presenta dunque uno zero nell’origine (come atteso vista la presenza
del condensatore Ci in serie all’ingresso) ed un polo reale negativo alla frequenza fp = [πCi (Rn +
rnx ||rbe,4 )]−1 ' 20.8 MHz.
                    Soluzione del compito di Fondamenti di Elettronica
                                     23 giugno 2008
1. Per VO =0, poiché VB = RB IB > 0 il transistore é certamente in regione normale di funzionamento.
   In condizioni stazionarie ho:

                                              VCC = VBE + RB IB                                    (1)

   La tensione VEB del transistore si calcola facilmente come:

                                                        βF 0 IB
                                         VBE = Vth ln           = 0.65347V                         (2)
                                                          IS
   da cui:
                                                 VCC − VBE
                                        RB =               ' 134.6 kΩ                              (3)
                                                     IB
                                                 VO − VSS
                                        RL =              = 2 kΩ                                   (4)
                                                  βF 0 IB

2. Poiché le resistenze non cambiano e Ibes =IS /βF 0 non cambia, anche VBE resta costante. Pertanto:

                                          VB = VCC − VBE = 1.3465V                                 (5)

   Risolvendo iterativamente per IC ottengo:

                                    (1)                        VBC
                                   IC      = βF 0 IB (1 +          ' 1.067 mA
                                                                VA
                                    (1)                        (1)
                                  VO       = VSS + RL IC ' 0.1347 V
                                    (1)                 (1)
                                  VBC      = VB − VO ' 1.2118 V
                                                                     (1)
                                    (2)                        VBC
                                   IC      = βF 0 IB (1 +          ' 1.0606 mA
                                                                VA
                                    (2)                        (2)
                                  VO       = VSS + RL IC ' 0.1212 V
                                    (2)                 (2)
                                  VBC      = VB − VO ' 1.2253 V
                                                                     (2)
                                    (3)                        VBC
                                   IC      = βF 0 IB (1 +          ' 1.061 mA
                                                                VA

3. Il circuito ai piccoli segnali il seguente:

             v cc                                                           vo

                        L          rbe                  β 0i

                            i                                              RL     RL


                                    RB           C
  da cui si calcola:


                                                  RB
                  vCC   = sL(β0 + 1)i + rbe i +          i
                                              1 + sCRB
                                               β0 RL (1 + sCRB )vCC
                   vO   = β0 RL i =
                                    RB + (1 + sCRB )sL(β0 + 1) + (1 + sCRB )rbe
                                                β0 RL (1 + sCRB )
                        = vCC 2                                                      (6)
                              s RB CL(β0 + 1) + s((β0 + 1)L + CRB rbe ) + RB + rbe

4. Poiché per ω=0:
                                         vO    β0 RL
                                            =          ' 1.47                        (7)
                                        vCC   RB + rbe
  e poiché vCC =50 mV abbiamo vO ' 73.5 mV. Pertanto VO = VO,0 + vO = 73.5 mV
                 Soluzione del compito di Fondamenti di Elettronica
                                   15 luglio 2008
1. Poichè Qn opera ai limiti della regione lineare di funzionamento utilizzo ancora le relazioni valide
   per questa regione.


           VCC    = Vebp + Vben
           Vben = Vth ln(ICn /ISn )
            Vebp = Vth ln(ICp /ISp ) = Vth ln(βF p IBp /ISp ) = Vth ln(βF p ICn (βF n + 1)/βF n ISp )
                  = Vth ln(ICn /ISn ) + Vth ln((βF n + 1)/5) = Vben + Vth ln((βF n + 1)/5)

   Per cui otteniamo che:

                             Vben = 0.5 · (VCC − Vth ln((βF n + 1)/5)) = 0.72 V                         (1)

   Inoltre se il transitore Qn lavora ai limiti della regione di saturazione abbiamo:

                    Vben = RL ICp = RL (βF n + 1)ICn = RL (βF n + 1)ISn exp(Vben /Vth )                 (2)

   da cui ICn = 13.2 mA RL = 1.07Ω

2. I parametri differenziali dei transistori valgono:


                                             Vth βF n
                                   rbe,n =            ' 97.7 Ω
                                               ICn
                                             Vth βF p      Vth βF p
                                   reb,p   =          =               ' 1.91 Ω
                                               ICp      (βF n + 1)ICn
                                   ro,n    = ro,p = ∞
                                   gmn = β0 /rben = 0.522 S
                                   gmp = β0 /rebp = 26.7 S

3. Il circuito equivalente per piccolo segnale è mostrato in figura:
                               L1                             L2
                 vi                                                                  vo

                                              β0 i bn             β0 i bp
                  r ben     i bn                           i bp                      RL
                                                   r ebp




   Per ω = 0 le induttanze sono dei corto circuiti per cui il circuito equivalente di semplifica e ottengo
   vo = vi per cui AV = 1. Inoltre per il calcolo della resistenza di uscita devo annullare tutti i
   generatori di ingresso, perció la tensione di uscita vale zero e quindi ottengo RO = 0. La resitenza
   di ingresso risulta essere infine il parallelo di due transistori connessi a diodo e della resistenza di
   carico RL :
                                        rben    rebp
                                RI =         ||      ||RL = 35.5mΩ                                (3)
                                       β0 + 1 β0 + 1
Per ω = ∞ le induttanze sono dei circuiti aperti per cui il circuito equivalente ai piccoli segnali si
riduce alla serie di due transistori in configurazione emettitore comune. Per cui ottengo RI = rben ,
RO = RL e:
                                      AV = gmp RL gmn rebp = 28.48                                (4)
                    Soluzione del compito di Fondamenti di Elettronica
                                     9 settembre 2008
1. Il circuito di figura é perfettamente simmetrico. Indicando con Ik le correnti entranti nel circuito
   per ciascuno dei morsetti collegati al generico generatore Vk , la potenza statica dissipata all’interno
   del circuito si esprime come:

            X
   P    =          Vk Ik = VCC (Veb,p /R1 + IE,p ) + 0 · IGN D + (−VCC )(−Vbe,n /R1 − IE,n )
               k
                                                                        ·                   µ                  ¶¸
                                                                            Vγ              (VCC − Vγ )   Vγ
        = VCC (Vγ /R1 + IE,p ) + VCC (Vγ /R1 + IE,n ) = 2VCC                   + (βF 0 + 1)             −
                                                                            R1                  R2        R1

   Nota R1 questa equazione fornisce:
                                               (βF 0 + 1)(VCC − Vγ )
                                      R2 =          P   βF 0 Vγ
                                                                       ' 2.49 kΩ                               (1)
                                                  2VCC + R1

   La condizione sulla tensione di uscita implica:
                                         µ                    ¶
                                             VCC − Vγ   Vγ           VCC
                                                      −    βF 0 RL =                                           (2)
                                                R2      R1            2
   e pertanto RL ' 516 Ω.
2. Il circuito equivalente é simmetrico per cui v02 = v01 .

                                                        vp        gmvp v
                                                                            O1
                                                                        RL
                                         R2
                                                   R1 C
                                    vi                 be,p
                                                                            L
                                                               gmvn v
                                                        vn           O2
                                                                         RL
                                         R2        R1
                                                          Cbe,n
                                                                            L
                                                                   Z

   Ovviamente per questa ragione Fd = 0, mentre Fc = v02 /vi . Ora abbiamo che:


                                                               (R1 ||rbe,n ||(1/sCbe,n ))
                      v02 = −Zgm,n vn = −(RL + sL)gm,n                                      vi                 (3)
                                                            R2 + (R1 ||rbe,n ||(1/sCbe,n ))
                                            R1 ||R2 ||rbe,n            1
                           = −(RL + sL)gm,n                                          vi                        (4)
                                                 R2         1 + sC(R1 ||R2 ||rbe,n )
   pertanto:
                                                        R1 ||R2 ||rbe,n         1
                           Fc = −(RL + sL)gm,n                                                                 (5)
                                                             R2         1 + sC(R1 ||R2 ||rbe,n )

3. Abbiamo rbe,n = Vth /Ibe,n = Vth /[(VCC − Vγ )/R2 − Vγ /R1 ] ' 774 Ω. Pertanto L = RL /2πfz '
   821nH mentre fp = 1/2π(R1 ||R2 ||rbe,n )C ' 428 MHz.
