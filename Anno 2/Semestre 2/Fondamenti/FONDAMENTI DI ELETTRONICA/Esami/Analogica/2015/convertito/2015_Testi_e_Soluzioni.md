---
fonte: "2015_Testi_e_Soluzioni.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica
                                                      3 Febbraio 2015
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori dei parametri indicati in calce si risponda ai seguenti
quesiti:

    1. Determinare il valore di RB che consente di ottenere Vo =-3 V, e le corrispondenti tensioni e correnti
       in tutti i nodi e rami del circuito. A tal fine si trascuri l’eﬀetto Early dei transistori bipolari. (12
       punti)

    2. Determinare i parametri diﬀerenziali β0n , β0p , rbe,n , reb,p dei transistori e disegnare il circuito
       equivalente di piccolo segnale. A tal fine si trascuri l’eﬀetto Early dei transistori bipolari. (6 punti)

    3. Determinare l’impedenza d’uscita Zo = vo /io del circuito in assenza di eﬀetto Early nei transistori
       bipolari. (6 punti)

    4. Determinare i parametri diﬀerenziali β0n , β0p , ron , rop e l’espressione dell’impedenza d’uscita del
       circuito tenendo conto dell’eﬀetto Early dei transistori. (6 punti)

Valori dei parametri:
Vcc = 4 V, Vee = 2 V, Vγ,npn =Vγ,pnp =0.65 V, VA,npn =VA,pnp =50 V, βF 0n = 80, βF 0p =80, RB =10 kΩ,
RE =5 kΩ, RC =2 kΩ, Vth = 0.025 V.




                                                RB

                                            IBn                            Tn
                                             Vbn

                                                                          RE
                                                                                                      Tp
                                                                              IBp                                        Vo
                                                            − Vee                                     Io
                                                                                                      RC
                                                                                                     − Vcc
                 Soluzione del compito di Fondamenti di Elettronica
                                  3 Gennaio 2015
1. Nel punto di lavoro richiesto (Vo =-3 V) il transistore pnp deve erogare una corrente di collettore
   ICp = 500 µA; inoltre, la sua tensione base-collettore é positiva. Pertanto il transitore deve trovarsi
   in regione normale di funzionamento, corrispondente ad una tensione emettitore-base Veb,p positiva
   e pari a V ,pnp . Questo implica che la corrente di emettitore del transistore npn sia anch’essa
   positiva. Poicé il collettore del transistore npn é collegato alla tensione piú elevata disponibile nel
   circuito, anch’esso dovrá trovarsi in regione normale di funzionamento. Abbiamo dunque:

                                           Vo    ( VCC ) F 0p + 1
                                IEp =                             ' 506.25 µA                            (1)
                                                 RC         F 0p
                               VEn =        VEE + V ,pnp ' 1.35 V                                        (2)
                                           VEn ( VEE )
                               I RE    =                   ' 130 µA                                      (3)
                                                  RE
                               VBn =       VEn + V ,npn ' 0.7 V                                          (4)
                                           IEp + IRE
                               IBn =                  ' 7.85 µA                                          (5)
                                             F 0p + 1
                                           0 VBn
                                RB =                 ' 81.9 k⌦                                           (6)
                                             IBn

2. In assenza di e↵etto Early abbiamo:

                                               0n      =         F 0n ' 80                               (7)
                                                0p     =         F 0p ' 80                               (8)
                                                                ICn
                                           gmn =                     ' 25 mS                             (9)
                                                                Vth
                                                                ICp
                                           gmp =                     ' 20 mS                            (10)
                                                                Vth
                                                                Vth
                                           rben =                    ' 3.18 k⌦                          (11)
                                                                IBn
                                                                Vth
                                           rebp =                    ' 4.00 k⌦                          (12)
                                                                IBp

3. L’impedenza di uscita in assenza di e↵etto Early é semplicemente pari a RC in quanto il collettore
   del transistore pnp si presenta come un generatore ideale di corrente avente impedenza di uscita
   infinita.

4. In presenza di e↵etto Early abbiamo
                                                            ✓                   ◆
                                                                     0    VBn
                                      0n   =         F 0n       1+                  ' 81.1              (13)
                                                                         VAn
                                                                                !
                                                                     VBp Vo
                                      0p   =         F 0p   1+                      ' 81.6              (14)
                                                                       VAp
                                                 VAn
                                      ron '          ' 79.56 k⌦                                         (15)
                                                 ICn
                                                 VAp
                                      rop '          ' 100 k⌦                                           (16)
                                                 ICp
                                                                                                        (17)

   Per quanto concerne l’impendenza di uscita, poiché il transistore pnp opera in configurazione base
   comune abbiamo Zo ' RC || F 0p rop .
                                        Prova scritta di Fondamenti di Elettronica
                                                     19 Febbraio 2015
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori dei parametri indicati in calce si risponda ai seguenti
quesiti:

    1. Determinare la regione di funzionamento del transistore ed il valore di ILb , ILe ed ILc . (12 punti)

    2. Disegnare il circuito equivalente di piccolo segnale e determinare i parametri diﬀerenziali del tran-
       sistore nel punto di lavoro di cui sopra. (6 punti)

    3. Determinare il valore limite della tensione Vo (ȷω) per ω→0 e ω→∞. A tal fine si consideri la
       presenza di una capacitá di giunzione Cbc ≫Cbe . (4 punti)

    4. Determinare l’espressione dell’impedenza di ingresso in condizione di corto circuito dell’uscita
       Vi (s)/Ii (s) trascurando le capacitá delle giunzioni. (8 punti)

Valori dei parametri:
Vcc = 0.7 V, IS = 10−15 A, βF = 75, βR =1, Lc =Le =Lb =1 nH, RB =10 kΩ, Vth = 0.025 V.


                                                                                                 Vcc
                                                          Lb
                                                                                                   RB


                                      Vo                                                       Tn                         Vo
                                                                          Le                                   Lc
                                        Prova scritta di Fondamenti di Elettronica
                                                      19 Giugno 2015
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori dei parametri indicati in calce si risponda ai seguenti
quesiti:

    1. Tracciare l’andamento qualitativo delle caratteristiche statiche Vo1 (Vin ) e Vo2 (Vin ) per Vin compresa
       nell’intervallo 0 V - VCC e determinare l’espressione delle tensioni Vin , Vo1 e Vo2 corrispondenti al
       cambiamento di regione di funzionamento del transistore. (12 punti)

    2. Determinare il valore (Vin,gm ) della tensione Vin per cui, essendo il transistore in regione normale
       di funzionamento, si ha anche gm = 1/RC . (4 punti)

    3. Disegnare i circuiti equivalente di piccolo segnale corrispondenti a punti di lavoro nella regione
       normale e nella regione di saturazione del transistore. (6 punti)

    4. Determinare l’espressione del guadagno diﬀerenziale (vo1 −vo2 )/vin corrispondente al punto di lavoro
       di cui al punto (2) soprastante. (8 punti)

Valori dei parametri:
Vcc = 5 V, Vγ,be = 0.6 V, Vγ,bc = 0.5 V, βF = 100, βR =1, RC =500 Ω, RE =100 Ω, Vth = 0.025 V.



                                                           Vcc
                                                                                           RC
                                                                                                                  Vo1
                                      Vin
                                                                                        T1
                                                                                                                  Vo2

                                                                                           RE
                     Soluzione del compito di Fondamenti di Elettronica
                                      19 Giugno 2015
1. Utilizzando il modello a soglia per le caratteristiche delle giunzioni appare evidente che il transistore inter-
   detto per Vin < Vγ,be . In questa regione di funzionamento Vo1 = VCC e Vo2 = 0 V. Nel momento in cui Vin
   diviene maggiore di Vγ,be il transistore entra in regione normale di funzionamento. Abbiamo allora:
                                                              βF R C
                                        Vo1 = VCC −                   (Vin − Vγ,be )                              (1)
                                                           (βF + 1)RE
                                        Vo2 = Vin − Vγ,be                                                         (2)
   Il transistore entra in saturazione per Vbc = 0, cioé quando Vin,sat = Vo1 . Sostituendo questa condizione
   nella precedente espressione di Vo1 e risolvendo per Vin otteniamo:
                                                         VCC + KVγ,be
                                             Vin,sat =                                                     (3)
                                                             1+K
                                                            βF R C
                                                 K =                                                       (4)
                                                         (βF + 1)RE
   Il valore minimo della tensione di uscita si ottiene quando Vce raggiunge il valore Vce,sat = Vγ,be − Vγ,bc .
   Ogni ulteriore incremento di Vin al di sopra di questo valore, infatti, porta la tensione di uscita a crescere
   contestualmente alla tensione di ingresso in quanto le due tensioni sono vincolate ad avere diﬀerenza pari a
   Vγ,bc . In altri termini deve essere Vo1 = Vin,min − Vγ,bc . Sostituendo l’espressione di Vo1 si ottiene ovviamente
                                                   Vin,min = Vin,sat + Vγ,bc                                      (5)

2. Poiché in regione normale di funzionamento vale la condizione gm = IC /Vth , la condizione gm = 1/RC
   implica
                                                  K                   Vth
                                           IC =      (Vin − Vγ,be ) =                                 (6)
                                                 RC                   RC
                                                         Vth
                                       Vin,gm = Vγ,be +                                               (7)
                                                          K
3. I circuiti equivalenti di piccolo segnale in regione di saturazione e normale sono indicati nella figura sot-
   tostante, rispettivamente a sinistra e destra.

                                     v_in



                         rbe     b_0r i_bc        rbc
                                                                                    b_0 i_in

                                                         v_in    rbe   i_in

                                 b_0f i_be                                               RC
                                                                               RE
                               RE           RC


4. Ricordando che la resistenza di ingresso di uno stadio a collettore comune vale Ri = rbe + (β0 + 1)RE e che
   in assenza di eﬀetto Early la resistenza di ingresso dell’amplificatore a doppio carico (quale quello di figura)
   coincinde con quella di uno stadio a collettore comune, si ottiene:
                                        vo1      vo1 iin            RC β 0
                                             =            =−                                                    (8)
                                        vin       iin vin     rbe + (β0 + 1)RE
                                        vo2          (β0 + 1)RE
                                             =                                                                  (9)
                                        vin      rbe + (β0 + 1)RE
                                                                                                               (10)
   Imponendo la condizione gm = 1/RC si ottiene infine:
                         vo1 − vo2               β0 RC + (β0 + 1)RE    rbe + (β0 + 1)RE
                                       = −                          =−                  = −1                     (11)
                            vin                   rbe + (β0 + 1)RE     rbe + (β0 + 1)RE
                                        Prova scritta di Fondamenti di Elettronica
                                                      22 Luglio 2015
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori dei parametri indicati in calce si risponda ai seguenti
quesiti:

    1. Determinare la relazione IC2 = IC2 (IR ) nell’ipotesi che tutti i transistori funzionino in regione di
       normale e determinare il valore minimo di βF in grado di garantire un errore tra IR e IC2 inferiore
       a trenta parti per milione (cioé IR = 1.000030IC2 ). (punti 6)

    2. Progettare il resistore R in modo tale da ottenere una corrente di polarizzazione IC2 = 1 mA e
       calcolare tutte le correnti e tensioni del circuito. A tal fine si assuma il valore di βF calcolato in
       precedenza. (12 punti)

    3. Disegnare il circuito equivalente di piccolo segnale del circuito di Figura 1. (punti 4)

    4. Determinare il valore della resistenza di ingresso ry = vy /iR vista tra il morsetto indicato dalla
       linea tratteggiata e la massa. (8 punti)

Valori dei parametri:
Vcc = 4 V, IS = 10−14 A, Vth (300K) = 0.026 V.



                                                                                                                   Vcc
                                                                 R
                                                                                                             Vo2
                                      Vy                                              T3

                                              T1                                                               T2
                                                                               Vx
                                        Prova scritta di Fondamenti di Elettronica
                                                     9 Settembre 2015
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori dei parametri indicati in calce si risponda ai seguenti
quesiti:

    1. Progettare i fattori di forma Sn e Sp e una rete di polarizzazione dei terminali di gate idonei a
       soddisfare simultaneamente le seguenti condizioni: 1) rendere perfettamente duali le caratteristiche
       dei transistori nMOS e pMOS; 2) ottenere Vout =Vcc /2; 3) ottenere un consumo statico del circuito
       pari a 0.2 mW nel punto di lavoro di cui sopra. (punti 12)

    2. Disegnare il circuito equivalente di piccolo segnale del circuito e determinare i valori di tutti i
       parametri diﬀerenziali nel punto di lavoro assegnato. (punti 8)

    3. Determinare l’espressione analitica della funzione di trasferimento Vout (s)/Vin (s) e tracciarne il
       diagramma di bode di ampiezza e fase. (10 punti)

Valori dei parametri:
Vcc = 1.2 V, λn = λp = 0.2 V−1 , VT n = −VT p = 0.3 V, βn′ = 0.7 mA/V2 , βp′ = 0.4 mA/V2 , C = 10 pF,
RL = 100 Ω.



                                                                                           Vcc

                                                                                 Vout
                                      Vin
                                                                                            RL                         CL
                      Soluzione del compito di Fondamenti di Elettronica
                                       9 Settembre 2015
1. Dati i valori dei parametri, per rendere duali le caratteristiche dei transistori a qualsiasi tensione di gate e
   drain é suﬃciente scegliere Sn =4 e Sp =7, cioé proporzionali (secondo il medesimo coeﬃciente di proporzion-
   alitá) alla conducibilitá intrinseca del transistore duale. Una volta resi simmetrici i transistori, la condizione
   Vout = VCC /2 é immediatamente verificata ponendo Vin = VCC /2. In questa condizione il circuito si trova
   alla soglia logica, i transistori sono in regione di saturazione e la corrente che attraversa i transistori vale
   IDS = 0.5Sn βn′ (VCC /2 − VT n )2 (1 + λn VCC /2) ≃ 141 µA. Si osservi che scegliendo fattori di forma piú piccoli
   la corrente pió essere arbitrariamente ridotta e con essa il consumo di potenza. Il consumo di potenza statico
   relativo alla coppia di transistori secondo il dimensionamento sopra prescelto vale Pmos = VCC IDS ≃ 0.17
   mW. Se si fosse partiti da valori di Sn e Sp tali da non rispettare la specifica sul consumo di potenza
   sarebbe stato ovviamente necessario passare a valori inferiori in modo da ridurre la larghezza dei transistori,
   dunque la loro corrente e quindi l’assorbimento di potenza dall’alimentazione. Si osservi che scegliendo per
   il transistore nMOS le dimensioni minime e dunque la minima corrente (in altri termini che sia dimension-
   ato a Sn =1) si otterebbe un consumo certamente inferiore da parte dei transistori e anche una inferiore
   occupazione d’area.
   Seguendo la scelta discussa in precedenza la rete di polarizzazione deve dunque dissipare al massimo 0.2-0.17
   = 0.03 mW. Poiché non c’é assorbimento statico al nodo Vin da parte dei transistori, la rete di polarizzazione
   piú semplice é costituita da un partitore resistivo tra alimentazione e massa. Per semplicitá scegliamo i due
   resistori di valore uguale pari ad R. Deve dunque valere Pbias = VCC Ibias = VCC       2 /2R da cui si deduce

   R ≃ 23300 Ω.

2. I parametri diﬀerenziali sono immediatamente determinati come gmn = gmp = 2IDS /(VGS − VT n ) ≃ 0.94
   mS, gdsn = gdsp = IDS λn /(1 + λn VDS ) ≃ 25.2 µS. Il circuito equivalente di piccolo segnale é mostrato in
   figura.

3. La funzione di trasferimento é data da:
                                                                    !                      "
                                      Vout (s)                               1
                                               = −(gmn + gmp )                      ||ZL                           (1)
                                      Vin (s)                           gdsn + gdsp

   dove ZL = RL + 1/sCL . Tenendo conto del fatto che transistore nMOS e pMOS hanno i medesimi valori
   dei parametri diﬀerenziali otteniamo dunque
                                                          #                                $
                                     Vout (s)    gmn                1 + sRL CL
                                              =−                                                                   (2)
                                     Vin (s)     gdsn         1 + sCL (RL + 1/2gdsn )

   Si tratta di una funzione di trasferimento ad un polo ed uno zero in cui la pulsazione di polo é inferiore a
   quella dello zero per via del termine 1/2gds che si somma ad RL . L’andamento del diagramma di Bode di
   ampiezza e fase é di determinazione immediata.


                                                     vout                    RL
                                            2*gds




                              vin=vgs
                                                    gmp*vsg




                                                                           gmn*vgs




                                                                                           CL
                               R/2
