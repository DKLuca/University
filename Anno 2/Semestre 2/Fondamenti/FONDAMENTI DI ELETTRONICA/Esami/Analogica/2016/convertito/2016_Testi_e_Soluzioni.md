---
fonte: "2016_Testi_e_Soluzioni.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                      3 febbraio 2016
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

     Con riferimento al circuito di figura e ai valori assegnati dei parametri si risponda ai seguenti quesiti:

    1. Determinare il valore statico di tutte le tensioni e correnti del circuito tenendo conto esplicitamente
       dell’eﬀetto Early. (12 punti)

    2. Disegnare il circuito equivalente per piccolo segnale e determinare l’espressione analitica ed il valore
       numerico dei suoi componenti. (6 punti)

    3. Determinare la funzione di trasferimento Vout (s)/Vin (s) e calcolarne il valore di poli e zeri. (12
       punti)




                                                                                  R1       Vcc
                                                                    Cin


                                                                                  R2          Cout
                                                                Vin
                                                                                                  Vout

                                                                                              L



Vth = 0.025 V, Vγ = 0.7 V, VCC = 5 V, R1 = 5 kΩ, R2 = 1 kΩ, L = 100 nH. Cin = Cout = ∞. βF 0 = 100,
VA = 20 V.
                 Soluzione del compito di Fondamenti di Elettronica
                                  3 febbraio 2016
1. In condizioni stazionarie l’induttore e il condensatore si comportano rispettivamente come un corto
   circuito ed un circuito aperto. Il circuito si riduce pertanto ad un semplice transistore con collettore
   ed emettitore a massa, mentre la base é polarizzata dalle resistenze R1 ed R2 . Chiaramente il
   transistor funziona in regione normale. Considerato il modello a soglia per il transistore e ricordando
   che in presenza di eﬀetto Early βF = βF 0 (1 + VCB /VA ) = βF 0 (1 + [VCC − Vγ ]/VA ) ≃ 121.5 abbiamo
                                                VCC − Vγ
                             IR1       =                  ≃ 860 µ                                                                (1)
                                                    R1
                                                Vγ
                             IR2       =            ≃ 700 µA                                                                     (2)
                                                R2
                                                VCC − Vγ     Vγ
                              IB =                        −     ≃ 160 µA                                                         (3)
                                                    R1       R2
                              IC       =        βF IB ≃ 19.44 mA                                                                 (4)
                                                                        Vγ
                              IL =              IE + IR2 = (βF + 1)IB +    ≃ 20.3 mA                                             (5)
                                                                        R2
2. Il circuito equivalente é mostrato in figura:
                                    Cin


                                                   R2         rbe
                                       Vin                                                  Cout
                                                          ib                                    Vout
                                                                       beta0*ib




                                       R1                     L                       rce



   I parametri diﬀerenziali del transistore valgono:
                                                                Vth
                                                    rbe =           ≃ 156 Ω
                                                                IB
                                                                IC
                                                   gm         =     ≃ 0.78 S
                                                                Vth
                                                                VA
                                                    rce       =     ≃ 1029 Ω
                                                                IC
                                                    β0        = βF ≃ 121, 5

3. Poiché i condensatori hanno valore tendenzialmente infinito il segnale di ingresso é applicato diret-
   tamente alla base del transistore. La resistenza R1 é dunque ininfluente sul guadagno di tensione.
   L’espressione del guadagno puó essere facilmente ottenuta osservando che:
                                                                    rbe
                                            !                                     "
                    Vin = rbe ib + (β0 + 1)ib +                         ib (sL||rce )                                            (6)
                                                                    R2
                                                     rbe
                             !                                 "
                   Vout =      (β0 + 1)ib +              ib (sL||rce )                                                           (7)
                                                     R2
                                   #                      $                                       #                  $
                  Vout             β0 + 1 + rRbe2 (sL||rce )                                   sL β0 + 1 + rRbe2
                         =              #                      $                      =               #                      $   (8)
                  Vin         rbe + β0 + 1 + rRbe2 (sL||rce )                             rbe + sL        rbe          rbe
                                                                                                          rce β0 + 1 + R2

   La funzione di trasferimento presenta uno zero nell’origine ed un polo con pulsazione
                                             1
                                p≃ #                  $ ≃ 12.8 Mrad/s.
                                         1
                                     L rce + gm + R12
                                        Prova scritta di Fondamenti di Elettronica
                                                     17 febbraio 2016
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura dove VX é una opportuna tensione statica di controllo sempre
compresa nell’intervallo 0 < VX < VCC /2 si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare il valore delle resistenze RB e RC che nella condizione VX = VCC /2 polarizzano il
       transistore BJT alla corrente IB0 ≃ 1µA ed il transistore MOS al limite della regione lineare di
       funzionamento. (11 punti)

    2. Determinare il valore dei parametri diﬀerenziali dei transistori corrispondenti al punto di lavoro di
       cui al quesito precedente. (3 punti)

    3. Discutere qualitativamente l’andamento della tensione VO ed del valore dei parametri diﬀerenziali
       dei transistori al variare della tensione VX . (2 punti)

    4. Determinare l’espressione del guadagno di tensione Vo (s)/Vi (s) nel punto di lavoro di cui al quesito
       precedente. A tal fine si consideri anche l’eﬀetto della capacitá Cbe della giunzione base-emettitore
       del BJT. (punti 10)

    5. Indicare se la funzione di trasferimento precedentemente calcolata é di tipo passa-alto, passa-basso,
       passa-banda o elimina-banda e descrivere in modo sintentico e qualitativo come si modifica il dia-
       gramma di Bode di |Vo (s)/Vi (s)| al variare di Vx nelll’intervallo assegnato. (4 punti)



                                                                                             Vcc

                                                                                          RC
                                                                  RB                                                              Vx
                                                                                                CL
                                                                                           Vo                         p−MOS
                                               Ri                 Ci
                               Vi                                                        BJT



VCC = 5 V, Ci = ∞, CL = 2 pF,
βp,M OS = 40 µA/V2 , VT P = −1 V, γM OS = 0 V1/2 , λM OS = 0 V−1 ,
Vth = 26 mV, IS = 10−14 A, βF = β0 = 80, VA,BJT = ∞ (no eﬀetto Early).
                 Soluzione del compito di Fondamenti di Elettronica
                                  17 febbraio 2016
1. Ipotizziamo che la regione di funzionamento del transistore BJT sia quella normale. La regione
   di funzionamento del transistore MOS é invece nota. I dati forniti suggeriscono di utilizzare un
   modello esponenziale per il transistore BJT. Possiamo dunque scrivere:
                                                         !            "
                                                             βF IB0
                           VCC − VBE   VCC − Vth ln            IS             5 − 0.5929
                 RB =                =                                    ≃              ≃ 4.41 M Ω   (1)
                              IB0              IB0                               10−6

   Dobbiamo inoltre imporre che per VX = VCC /2 = 2.5 V si abbia VGS − VT p = VDS e cioé VX −
   VCC − VT p = Vo − VCC che fornisce Vo = VCC /2 + |VT p | = 3.5 V. La corrente nel transistore MOS
   vale dunque IM OS = βp,M OS (VGS − VT p − VDS /2)VDS ≃ 45 µA. Otteniamo infine

                                               VCC − VO
                                   RC    =                  ≃ 42.86 kΩ.                               (2)
                                             βF IB0 − IM OS

2. Poiché il transistore MOS al confine della regione lineare di funzionamento ed in virtú del valore
   dei parametri ad esso assegnati possiamo certamente dire che gm,M OS = βp,M OS VDS ≃ 60 µS,
   gmb = gds = 0 S. Per il transistore BJT abbiamo invece gm,BJT ≃ IC0 /Vth ≃ 3.08 mS, rbe ≃
   Vth /IB0 ≃ 26 kΩ, ro,BJT = ∞ in quanto si trascura l’eﬀetto Early.

3. Al calare della tensione Vx da VCC /2 a 0 V il transistore MOS entra in regione lineare e la sua
   rds si riduce (al punto precedente era rds = ∞). La tensione Vo cresce ma questo non modifica il
   punto di lavoro del transistore BJT in quanto stiamo trascurando l’eﬀetto Early. Pertanto anche i
   parametri diﬀerenziali del BJT rimangono i medesimi calcolati in precedenza.

4. Il circuito equivalente di piccolo segnale é rappresentato in Figura. Nel punto di lavoro assegnato la
   conduttanza gds é nulla e potrebbe essere dunque cancellata dal circuito. Viene tuttavia mantenuta
   in vista per facilitare la comprensione della risposta al quesito successivo. I generatori controllati
   corrispondenti a gm,M OS e gmb non compaiono in quanto VGS é costante e l’eﬀetto body é trascurato.

                    Ri             Vbe(s)                                               Vo(s)


                                                  rbe                                    rds
       Vi(s)          RB
                                     Cbe                                                        CL
                                                     gmBJT*Vbe(s)                 RC


   Poste

                               Zi (s) = RB ||rbe ||1/sCbe                                             (3)
                                                                        1
                               Zo (s) = RC ||rds ||1/sCL =                                            (4)
                                                                  GC + gds + sCL
   abbiamo
                             Zi (s)        (RB ||rbe )              1
                                       =                 ·                          .                 (5)
                           Ri + Zi (s)   (RB ||rbe ) + Ri 1 + sCbe (RB ||rbe ||Ri )
   Il guadagno di tensione richiesto vale dunque

               Vo (s)               (RB ||rbe )              1                   (RC ||rds )
                      = −gm,BJT ·                 ·                         ·                         (6)
               Vi (s)             (RB ||rbe ) + Ri 1 + sCbe (RB ||rbe ||Ri ) 1 + sCL (RC ||rds )
5. La funzione di trasferimento é chiaramente di tipo passa basso con due poli reali negativi relativi a
   Zi (s) e Zo (s), i quali valgono pi = [Cbe (RB ||rbe ||Ri )]−1 e po = [CL (RC ||rds )]−1 , rispettivamente.
   Al calare della tensione Vx da VCC /2 a 0 V la rds si riduce, come discusso prima. Di conseguenza
   cala il valore del guadagno statico del circuito a centro banda, mentre la frequenza di po aumenta.
   Nel caso quest’ultimo si mantiene apprezzabilmente superiore a quella di pi , la variazione di Vx non
   modifica apprezzabilmente la larghezza di banda a -3dB del circuito, mentre se po piú piccolo o di
   frequenza simile a pi , anche la larghezza di banda del circuito aumenta all’abbassarsi di VX .
                                        Prova scritta di Fondamenti di Elettronica
                                                      17 giugno 2016
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, calcolare le correnti e tensioni di polarizzazione del transistore
       bipolare e calcolare il valore della resistenza R6 che permette di polarizzare il transistore MOSFET
       alla corrente ID = 1 mA. (8 punti)

    2. Disegnare inoltre il circuito equivalente ai piccoli segnali e calcolare i parametri diﬀerenziali dei
       transistori. (4 punti)

    3. Calcolare il valore della resistenza di ingresso vista dal generatore Vi . (6 punti)

    4. Calcolare il guadagno di tensione AV = vo /vi . (12 punti)

R1 = 7.3 kΩ, R2 = 2.7 kΩ, R3 = 1 kΩ, R4 = R7 = 2 kΩ, R5 = 4 kΩ, R8 = 3 kΩ, VCC = 10 V,
Vth = 25 mV, IS,bjt = 1.4 × 10−15 A, βF = β0 = 100, βM OS = 2 mA/V2 , VT = 1 V.


                                                                                                                                 Vcc

                                                                                        R5
                                                                                                                          R8
                                                      R4                                                Vg
                                      R1                                                R6
                                                      Vc                                                                  Vo
                               Vi               Vb
                                                                 Ve                    R7
                                      R2
                                                      R3




                                                                               Fig. 1
                   Soluzione del compito di Fondamenti di Elettonica
                                    17 giugno 2016
1. A livello statico le capacitá possono essere considerate come circuiti aperti. Ipotizzando il BJT
   acceso e in regione normale e trascurando la corrente di base si puó calcolare la corrente che scorre
   su R1 e R2 : I1 ≃ RV1CC
                         +R2 = 1 mA. Questa consente di calcolare la tensione di base e di emettitore
   del BJT: VB = R2 I1 = 2.7 V. A questo punto é possibile risolvere il seguente sistema di equazioni:
                                                                      !            "
                                                                           IC
                                     VBE    = VB − VE = Vth exp                                             (1)
                                                                          IS,bjt
                                                      βF + 1
                                      VE = R3                IC                                             (2)
                                                        βF

                                                                                        VE            IC
                                                                                         [V]        [mA]
   il quale é un sistema non lineare che puó essere risolto con il metodo iterativo:    2          1.98
                                                                                       2.006        1.981
                                                                                       2.005        1.981
   Le correnti di base ed emettitore valgono quindi IB = IC /βF = 19.81 µA e IE = βFβF+1 IC ≃ 2 mA.
   La tensione di collettore é pari a VC = VCC − R4 IC = 6.04 V. Le tensioni calcolate confermano
   che il transistore é in regione normale, mentre le correnti ottenute sono coerenti con l’ipotesi di
   trascurare la corrente di base.
   Per calcolare il valore di resistenza R6 , ipotizziamo il transistore polarizzato in regime di saturazione
   e scriviamo le equazioni che descrivono correnti e tensioni nella seconda parte del circuito:


                                               βM OS
                                      ID =            (VGS − VT )2
                                                 2
                                     VGS     = R6 I 6
                                     VCC     = (R5 + R6 )I6 + R7 (I6 + ID )

   dove I6 é la corrente che scorre nelle resistenze R6 e R5 . Dalla prima equazione si ottiene VGS =
   2 V, mentre dalle altre ricavo I6 = 1 mA e R6 = 2 kΩ. Inoltre la tensione del drain si calcola
   immediatamente come VD = VCC −R8 ID = 7 V, la quale conferma che il MOSFET é in saturazione.

2. I parametri diﬀerenziali dei due transistori valgono: rbe = Vth βF /IC = 1.26 kΩ, gmB = IC /Vth =
   79.24 mS e gmM = βM OS (VGS − VT ) = 2 mS. Non essendoci dati riguardanti l’eﬀetto Early e la
   modulazione di canale per il MOSFET, considero rce = rds = ∞.
   Il circuito equivalente ai piccoli segnali ’e quello indicato in figura:
                                                                                     gmM vgs
              Vi    ii          ib                         vc             vs
                                           gmB vbe                                             vo

                              rbe                     R4        R7   R6            vgs         R8
                R1||R2

                                                 ve                             vg
                                            R3                       R5
3. La resistenza di ingresso si calcola come vi /ii . Perció, la tensione, la corrente e la resistenza di
   ingresso valgono:


                              vi = rbe ib + R3 (β0 + 1)ib
                                       vi           rbe ib + R3 (β0 + 1)ib
                               ii =         + ib =                         + ib
                                    R1 ||R2                 R1 ||R2
                              Ri = R1||R2 ||[rbe + R3 (β0 + 1)] = 1.93 kΩ

4. Per calcolare il guadagno di tensione risolvo il seguente sistema di equazioni:

           vo = −R8 gmM vgs
                                  R5                    R6
          vgs = vg − vs =               vs − vs = −           vs
                               R6 + R5              R6 + R5
                    vs     vs       vs                            1   1   1 + gmM R6      R5
                                                              !                      "!      "
       −β0 ib    =      +     +            − gmM vgs = −vgs         +   +              1+
                   R4 R7 R6 + R5                                R4 R7       R6 + R5       R6
            vi   = rbe ib + R3 (β0 + 1)ib = [rbe + R3 (β0 + 1)]ib

   da cui ottengo:
                                                       R8 gmM β0
                     AV =                         #                       $#       $ = 1.067          (3)
                                                      1     1    1+gmM R6       R5
                            [rbe + R3 (β0 + 1)]       R4 +  R7 +  R6 +R5    1 + R6
                                        Prova scritta di Fondamenti di Elettronica
                                                       14 luglio 2016
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, calcolare il valore della tensione di ingresso Vi da applicare al
       circuito in modo da ottenere una tensione di uscita VO = 2 V. (7 punti)

    2. Supponendo di applicare una tensione Vi molto bassa, tale da spegnere T1 , calcolare qual é la
       tensione di uscita VO che si ottiene. (3 punti)

    3. Disegnare inoltre il circuito equivalente ai piccoli segnali e calcolare i parametri diﬀerenziali dei
       transistori. (4 punti)

    4. Calcolare la funzione di trasferimento AV = VO (s)/Vi (s) e indicare il valore massimo del guadagno
       di tensione e la frequenza di transizione della funzione ottenuta. (10 punti)

    5. Determinare per il circuito in esame l’impedenza di ingresso e quella di uscita. (6 punti)

R1 = R2 = 2 kΩ, R3 = 1 kΩ, C = 1 nF, VCC = 10 V, Vth = 25 mV, IS = 10−14 A, βF = β0 = 100,
I = 5 mA.


                                                                                                Vcc

                                      R1                                         R2

                                                                                                                                  Vo
                               Vi
                                                                                                             R3                 C
                                                 T1                   T2



                                                                      I



                                                                               Fig. 1
                  Soluzione del compito di Fondamenti di Elettonica
                                   14 luglio 2016
1. Per avere una tensione VO = 2 V, su R2 deve scorrere una corrente IR2 = (VCC − VO )/R2 = 4 mA.
   Inoltre su R3 scorre la corrente IR3 = VO /R3 = 2 mA. Tali correnti mi consentono di calcolare
   quella che scorre in T2 come IC2 = IR2 − IR3 = 2 mA. Considerato che VB2 = 0 V, T2 si trova in
   condizioni di funzionamento in regione normale (VCB2 = 2 > 0), per cui posso calcolare VBE2 =
   Vth ln(IC2 /IS ) ≃ 0.65 V, da cui ottengo che la tensione di emettitore VE = VB2 − VBE2 = −0.65 V.
   Tale tensione é anche la tensione di emettitore di T1 .
   Ora applicando la legge di Kirchhoﬀ per le correnti, la corrente che scorre in T1 vale IC1 ≃ IE1 =
   I − IE2 = I − βFβF+1 IC2 ≃ 3 mA. Ipotizzando T1 in regione normale di funzionamento, possiamo
   calcolare VBE1 = Vth ln(IC1 /IS ) ≃ 0.66 V. A questo punto ottengo Vi = VE + VBE1 = 0.01 V.
   La tensione di collettore invece vale VC1 = VCC − R1 IC1 = 4 V, la quale verifica l’ipotesi di
   funzionamento in regime normale in quanto VCB1 = VC1 − Vi = 3.99 > 0.

2. Quando il transitore T1 é spento, tutta la corrente del generatore scorre in T2 . Supponendo che
   quest’ultimo lavori ancora in regione normale di funzionamento, allora avremo che IC2 ≃ 5 mA. Il
   valore della tensione di uscita si ottiene da questo semplice sistema di equazioni:

                                                     I2 = IC2 + I3                                (1)
                                                 VO = R3 I3                                       (2)
                                                 VO = VCC − R2 I2                                 (3)

   da cui si ottiene I3 = 0, I2 = 5 mA e VO = 0. Tale risultato verifica il funzionamento in regione
   normale per T2 in quanto VCB2 = 0.

3. Il circuito equivalente ai piccoli segnali é il seguente:
                              ib1   beta0 ib1                ib2 beta0 ib2
                        vi                                                        vo

                                                R1                      R2||R3
                             rbe1                          rbe2                    C




   I parametri diﬀerenziali dei transistori valgono: rbe1 = Vth βF /IC1 = 833 Ω, gm1 = IC1 /Vth =
   120 mS, rbe2 = Vth βF /IC2 = 1.25 kΩ, gm2 = IC2 /Vth = 80 mS.

4. Per il circuito sopra si imposta il seguente sistema di equazioni:

                    (β0 + 1)IB1 (s) = −(β0 + 1)IB2 (s)                                            (4)
                               Vi (s) = rbe1 IB1 − rbe2 IB2 = (rbe1 + rbe2 )IB1                   (5)
                                                                                    R2 ||R3
                              VO (s) = −β0 IB2 [R2 ||R3 ||(sC)−1 ] = β0 IB1                       (6)
                                                                                 1 + sCR2 ||R3

   da cui otteniamo
                                            VO        β0        R2 ||R3
                                    AV =       =            ·                                     (7)
                                            Vi   rbe1 + rbe2 1 + sCR2 ||R3

   La funzione di trasferimento presenta un solo polo alle frequenza fp = (2πCR2 ||R3 )−1 = 239 kHz,
   per cui si tratta di un circuito con caratteristiche passa–basso. La frequenza di transizione cor-
   risponde alla frequenza del polo calcolata, mentre il valore massimo del guadagno si ottiene per
                                                  0 R2 ||R3
   frequenza del segnale nulla e vale AV (0) = rβbe1 +rbe2 ≃ 32.
5. L’impedenza di ingresso si calcola facilmente da Eq.(5) in quanto la corrente ib1 é anche la corrente
   di ingresso del circuito. Perció otteniamo Zi = (rbe1 + rbe2 ) = 2083 Ω.
   L’impedenza di uscita, invece, si calcola annullando la tensione di ingresso vi . A questo punto,
   otteniamo da Eq.(5) che ib1 = 0 ed entrambi i transistori sono spenti. Il terminale di uscita quindi
   “vede” solo il parallelo delle resistenze R2 e R3 e del condensatore C. L’impedenza di uscita vale,
                                         R2 ||R3
   quindi, Zo = [R2 ||R3 ||(sC)−1 ] = 1+sCR   2 ||R3
                                        Prova scritta di Fondamenti di Elettronica
                                                     9 settembre 2016
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, calcolare il valore della resitenza R2 che permette di ottenere
       una tensione VO = 3 V (tenere conto dell’eﬀetto Early per il transistore bipolare). (10 punti)

    2. Disegnare inoltre il circuito equivalente ai piccoli segnali e calcolare i parametri diﬀerenziali dei
       transistori. (4 punti)

    3. Calcolare il guadagno di tensione vo /vi dell’amplificatore (trascurare l’eﬀetto Early sul BJT). (9
       punti)

    4. Determinare per il circuito in esame la resistenza di ingresso e quella di uscita (trascurare l’eﬀetto
       Early sul BJT). (7 punti)

R1 = R3 = 3 kΩ, VG = 4 V, VCC = 10 V, Vth = 25 mV, IS = 10−14 A, βF 0 = β0 = 100, VA = 30 V,
βM OS = 2 mA/V2 , VT = −1 V, C = ∞.


                                                                                                Vcc

                                                                                                R1
                                                                               R2

                                                       Vi

                                                                                                Ve
                                                                     Vg
                                                                                                           Vo


                                                                                                R3



                                                                               Fig. 1
                  Soluzione del compito di Fondamenti di Elettonica
                                  9 setttembre 2016
1. Per avere una tensione VO = 3 V, su R3 deve scorrere una corrente ISD = VO /R3 = 1 mA.
   Considerato che VG = 4 V, !  il MOSFET si trova in condizioni di saturazione (VD = 3 V), per cui
   posso calcolare VGS = VT − 2ISD /βM OS = −2 V, da cui ottengo che VE = VS = VG − VGS = 6 V.
   Inoltre ISD = IE , perció anche il BJT é acceso e in regione normale perché la corrente di base
   induce una caduta su R2 che impone VC > VB .
   Per cui posso impostare la sequenti equazioni:
                VCE    = VC − VE = VCC − R1 (IC + IB ) − VE = VCC − R1 IE − VE = 1 V                                         (1)
                                   VCE
                             "          #
                  βF   = βF O 1 +         = 103.3                                                                            (2)
                                    VA
                           βF                 VBE         VCE
                                            "     # "         #
                  IC   =        IE = IS exp        · 1+                                                                      (3)
                         βF + 1               Vth          VA
                                     IE
                VCE    = VBE + R2                                                                                            (4)
                                   βF + 1
                                                                                        $                         %
                                                                                              βF IE        VA
   In Eq.(3) l’unica incognita é VBE , per cui ottengo VBE = Vth ln                        (βF +1)IS · VA +VCE       = 0.632 V,
   mentre da Eq.(4) posso ricavare R2 come R2 = βFIE+1 (VCE − VBE ) = 38.38 kΩ. Inoltre la corrente
   di collettore vale IC = βFβF+1 IE ≃ 0.99 mA.
2. Il circuito equivalente ai piccoli segnali é il seguente:
                                                        i2   R2
                                         vi
                                                                                i1
                                                        ib
                                                                                R1
                                                 rbe     beta ib
                                                                          rce
                                                             ve=vs
                                                   vg
                                                               gmvgs
                                                                     vo

                                                        R3




                                                                                 BJT = I /V
   I parametri diﬀerenziali dei transistori valgono: rbe = βF Vth /IC = 2.6 kΩ, gm      C  th =
   39.6 mS, rce = VA /IC = 30.3 kΩ, gmM OS  = βM OS |VGS − VT | = 2 mS.
3. Se trascuriamo l’eﬀetto Early, in pratica consideriamo rce = ∞. Per cui, per il circuito sopra si
   imposta il seguente sistema di equazioni:
                 vgs = vg − vs = −vs                                                                                         (5)
           M OS        M OS                                                 vbe            vi − vs    BJT
         −gm    vgs = gm    vs = (β0 + 1) ib = (β0 + 1)                         = (β0 + 1)         ≃ gm   (vi − vs )
                                                                            rbe              rbe
                                   vi
                  vs =     $         M OS
                                             %                                                                               (6)
                               1 + ggmBJ T
                                     m

                                                      gM OS R3
                         M OS
                  vo = −gm              M OS
                              vgs R3 = gm    vs R3 = $ m gM OS % · vi                                                        (7)
                                                      1 + gmBJ T
                                                                                m

                                          M OS
   da cui otteniamo AV = vvoi = $ gmgM OS
                                       R3 %
                                            = 5.71.
                                         1+ m
                                            BJ T
                                              gm
4. Per quanto riguarda la resistenza di ingresso possiamo scrivere le seguenti equazioni:

                                          i2 = i1 + β0 ib                                         (8)
                                            ii = i2 + ib = i1 + (β0 + 1)ib                        (9)
                                          vi = R1 i1 + R2 i2                                     (10)
                                      rbe ib = vi − vs                                           (11)
                                     M OS v e sfruttando Eq.(6) ottengo:
  Inoltre, sapendo che (β0 + 1)ib = gm     s

                                 gmM OS
                  ib =                        v
                                M OS + g BJT ) i
                                                                                                 (12)
                          rbe (gm       m
                                      &                        '
                             1                   gM OS g BJT
                  i1 =                    1 − R2 MmOS mBJT         vi                            (13)
                          R1 + R2               gm   + gm
                          (             &                       '                   )
                                 1                 gM OS gBJT         g M OS gBJT
                  ii =                      1 − R2 MmOS mBJT        + MmOS mBJT vi               (14)
                              R1 + R2             gm   + gm          gm    + gm
                                  (            &                        '                  )−1
                          vi      1                       gM OS gBJT          gM OS gBJT
                 Ri =        =                     1 − R2 MmOS mBJT         + MmOS mBJT          (15)
                          ii   R1 + R2                   gm   + gm           gm   + gm
                              $                 %
                                M OS + g BJT (R + R )
                               gm       m      1   2
                      =    M OS + g BJT + R g M OS g BJT
                                                               = 6.12 kΩ
                          gm       m       1 m      m


  Per il calcolo della resistenza di uscita bisogna imporre vi = 0. Equazione (6) ci impone immedi-
  atamente che anche vs = 0, per cui nel MOSFET non c’é corrente di piccolo segnale. A questo
  punto, la resistenza di uscita é semplicemente Ro = R3 .
