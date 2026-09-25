---
fonte: "Analogica_ALL_EXAMS.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova scritta di Fondamenti di Elettronica I
                                                       24 Marzo 2004
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

ATTENZIONE:
1) riportare nella tabella in calce le espressioni ed i valori numerici ottenuti in risposta ai diversi quesiti
2) non verranno corretti elaborati che non riportino in modo leggibile nome, cognome e numero di ma-
tricola SU TUTTI I FOGLI CONSEGNATI

     Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . = . . . . . . . . .

Il circuito di figura rappresenta un front-end per fibra ottica in configurazione emettitore comune. Impulsi
di luce provenienti dalla fibra colpiscono il diodo generando una variazione della corrente Ii rispetto al
valore di riposo Ii,0 . Con riferimento ai valori indicati dei parametri si risponda alle seguenti domande:

    1. Determinare lo stato del transistore, quello del diodo e stimare la resistenza differenziale rD del
       diodo (5 punti).

    2. Determinare il valore di RF che corrisponde a Vo,0 = 1.65 V (10 punti).

    3. Determinare la matrice ammettenze del due porte compreso all’interno del riquadro tratteggiato (5
       punti).

    4. Determinare l’espressione analitica della transimpedenza per bassa frequenza (vo /ii per ω → 0) del
       due porte compreso all’interno del riquadro (6 punti).

    5. Determinare l’espressione analitica ed il valore numerico della transimpedenza di cui al punto
       precedente nel limite RF → ∞ (4 punti).

RL = 2 kΩ, VCC = 3.3V , IS (diodo) = 1 fA, IS (BJT ) = 1 fA, βF = β0 = 50, Vth = 25 mV


                                                                                                       +VCC
                                                               D
                                                                                                         RL
                                                                Ii                RF

                                                      Vi                                                                  VO
                                                                                                    T1
                                                                                    CBE

     rD = . . . . . . . . . [. . . . . . . . .]

     RF = . . . . . . . . . [. . . . . . . . .]

     y11 = . . . . . . . . . . . . . . . . . . . . . . . . . . .     y12 = . . . . . . . . . . . . . . . . . . . . . . . . . . . ,

     y21 = . . . . . . . . . . . . . . . . . . . . . . . . . . .     y22 = . . . . . . . . . . . . . . . . . . . . . . . . . . . ,

     vo /ii (j0) = . . . . . . . . . . . . . . . . . . . . . . . .

     limRF →0 (vo /ii (j0)) = . . . . . . . . . . . . [. . . . . . . . . . . .]
                                        Prova scritta di Fondamenti di Elettronica
                                                      14 Giugno 2004
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
domande:

    1. Determinare il valore stazionario delle tensioni e correnti IR1,0 , IR2,0 , IRL,0 = IE,0 (Q1 ), IB,0 (Q1 ),
       IC,0 (Q1 ), VB,0 (Q1 ), V2,0 = VE,0 (Q1 ) corrispondenti a V1,0 = 1.25 V e V1 = V1,0 = 2.5 V. (6 punti).

Valori dei parametri:
VCC = 2.5 V, βF = 50, IS = 10−14 A, R1 = 1000 Ω, R2 = 1000 Ω, RL = 100 Ω, Vth = 0.025 V, C1 = 2 pF.
                                                                                VCC


                                                                     R1
                                                                                        Q1
                                                       V1
                                                                                                                   V2
                                                               C1
                                                                                     R2            RL


                                                                           FIGURA 1

———————————————-
    Il circuito equivalente per piccolo segnale del circuito compreso nel riquadro tratteggiato di Figura 2
presenta i seguenti valori dei parametri: z11 = 1100 Ω, z21 = 1000 Ω degli elementi della matrice Z. Con
riferimento ai valori sotto indicati dei parametri si risponda ai seguenti quesiti.

    1. Determinare l’espressione della trans-resistenza v2 /i1 tenendo conto della capacità del diodo D1.
       (4 punti)

    2. Determinare il valore delle resistenze R1 ed R2 e l’espressione analitica del rapporto tra valore
       minimo e massimo di v2 /i1 . (2 punti)

Valori dei parametri:
z11 = 1100 Ω, z21 = 1000 Ω,


                                                                    R1                      D1                      V2
                                                I 1


                                                                                         R2          RL


                                                                           FIGURA 2
                                        Prova scritta di Fondamenti di Elettronica
                                                      23 Giugno 2004
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
domande:

    1. Determinare la regione di funzionamento del transistore ed valore stazionario delle tensioni e correnti
       IE,0 , IB,0 , IC,0 , VE,0 , VB,0 , VC,0 e del parametro di saturazione σ corrispondenti a Vi,0 = 0.5 V,
       Vi,0 = 5 V e Vi,0 10 V rispettivamente. (5 punti).

    2. Considerando esplicitamente l’effetto della capacità differenziale base-emettitore di Q1 si determini
       l’espressione del guadagno di tensione per piccoli segnali Av = vC /vi , nonchè il suo valore e la sua
       fase per ω → 0 e per ω → ∞ (5 punti).

    3. Determinare il valore limite di RC che porta il transistore sulla soglia della regione di saturazione
       in corrispondenza di un valore Vi,0 = 5 V (2 punti).

Valori dei parametri:
VCC = 10 V, hF E = 100, RE = 150 Ω, RC = 150 Ω, L = 1 nH, Vth = 0.025 V, VBE,on = 0.6 V.
VBE,sat = 0.75 V. VCE,sat = 0.07 V.
                                                                                         VCC


                                                                                         RC

                                                                                                                VC
                                                       VI                             VB
                                                                                                             Q1

                                                                  L1                                            VE
                                                                                                 RE


                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                       13 luglio 2004
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
domande:

    1. Determinare la regione di funzionamento del transistore e dimensionare il resistore R in modo tale
       da polarizzare il transistore ad una corrente di Base IB = 2 µA. (5 punti).

    2. Disegnare il circuito equivalente per piccoli segnali dello schema in figura e determinare l’espressione
       del guadagno di corrente io /ii esprimendo il medesimo come rapporto di due polinomi in s (5 punti).

    3. Dimensionare il valore di L in modo tale che la frequenza di taglio del circuito valga f−3dB =
       100M Hz. Indicare se il circuito è di tipo passa alto o passa basso. (2 punti).

Valori dei parametri:
VCC = 2.5 V, VEE = −2.5 V, hF E = 50, Vth = 0.025 V, IS = 10−15 A, RL = 100Ω.


                                                            VCC
                                                                                        L
                                                                                            VO         RL

                                                                               Q1

                                                                     VE                                VI
                                                                     RE                 C


                                                                           -VEE
                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                     8 settembre 2004
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura 1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
domande:

    1. Determinare il valore di RBp ed i valori stazionari di tutte le correnti e tensioni del circuito nella
       condizione VOut,0 = 0 V. (5 punti).

Valori dei parametri:
VCC = 3 V, VEE = 1.5 V, βF = 25, Vth = 0.025 V, JS = 2 · 10−14 A/µm2 , Area=0.5µm2 , RCp = 15kΩ,
REp = 20 kΩ.


Con riferimento al circuito di Figura 2 e ai valori sotto indicati dei parametri, si risponda alle seguenti
domande:

    1. Determinare il valore limite della capacità CE affinchè il modulo dell’impendenza ZE sia inferiore
       a 0.1 Ω e quindi ZE diventi trascurabile alla frequenza f = 1 MHz. (2 punti).

    2. Determinare il valore di L che rende puramente reale l’impedenza di carico ZL alla frequenza di
       1 MHz. (2 punti).

    3. Ipotizzando il transistore operante in regione normale di funzionamento, determinare il modulo e
       la fase del guadagno di tensione AV = vout /vin del circuito alla frequenza di 1 MHz corrispondente
       al punto di lavoro ICn,0 = 1 mA. A tal fine si supponga Cin → ∞. (4 punti).

Valori dei parametri:
VA = 20 V, Vth = 0.025 V, RCn = 1 kΩ, REn = 50Ω, RL = 1 kΩ, CL = 10 nF.

                                  VCC                                         VCC
                                                                                    RCn
                     REp                                            RY
                                                                                                                          L
                                                                                                     VOut                              RL
                                                           VIn
                                               Q1                                          Q1
                                                                                                                CL
                     R Bp                                           CIn
                                                 VOut
                                                                                                                              ZL
                                        RCp                         RX              REn                  CE
                                                                              ZE

                                            -VEE

                          FIGURA 1                                                                                            FIGURA 2
                                        Prova scritta di Fondamenti di Elettronica
                                                    23 settembre 2004
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura 1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
domande:

    1. Determinare il valore della corrente di riposo Iu,0 corrispondente ad Ii,0 = 2 mA. (8 punti).

    2. Determinare l’espressione della funzione di trasferimento Iu (s)/Ii (s) che descrive il comportamento
       ai piccoli segnali del circuito nell’intorno del punto di riposo calcolato sopra, e calcolare il valore di
       eventuali poli e zeri. (12 punti)

    3. Noto che la corrente di ingresso al circuito ha l’espressione Ii = Ii,0 + Ii,1 cos(ω1 t), con Ii,1 = 2 µA
       e ω1 = 40 · 106 rad/s, determinare l’andamento a regime della corrente di uscita. (6 punti)

Valori dei parametri:
VCC = 5 V, βF = 20, Vth = 0.025 V, C = 2 nF, L = 10 µH.



                                                                                                  VCC
                                                                                                                                 L
                                                                                                            I U
                                                                                                                             VO
                                                        I I               Q1                                           Q2

                                                                                                            VE
                                                                                       C

                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                     30 novembre 2004
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura 1 e ai valori indicati dei parametri, si risponda alle seguenti domande:

    1. Determinare i valori di R1 , R2 , R3 , RC in modo tale che: a) Il consumo statico del circuito sia pari
       a 25 mW; b) l’assorbimento statico di corrente di alimentazione attraverso R3 sia pari al 20% dell’
       assorbimento totale; c) in presenza di un segnale di ingresso vi la tensione di uscita Vo possa subire
       un’escursione massima di ±1 V rispetto al valore di polarizzazione Vo,0 ; d) l’ escursione di cui al
       punto precedente non comporti la saturazione del transistore. (6 punti).

    2. Determinare inoltre i valori di riposo Vbe1,0 , Vbe2,0 , Vcb1,0 , Vcb2,0 , Ve2,0 (1 punto).

    3. Determinare l’espressione del guadagno di tensione per piccoli segnali vu /vi nell’intorno del punto
       di riposo di cui sopra (6 punti).

    4. Calcolare il valore numerico del guadagno di tensione di cui al punto precedente (1 punto).

Valori dei parametri:
VCC = 5 V, βF = β0 = 100, Vth = 0.025 V, IS1 = IS2 = 10−15 A, C1 = C2 = C3 = ∞.



                                                                   VCC
                                                                             RC
                                                  R3
                                                                                                  VO                         VU
                                                                   VB2
                                                                                        Q2
                                                                                                                C3
                                                  C2
                                                                                           VE2
                                                  R2
                                              C1
                                    VI                             VB1                  Q1

                                                  R1



                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                      17 marzo 2005
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura 1 (nel quale i transistori Q1 e Q2 sono perfettamente complementari),
ed ai valori indicati dei parametri, si risponda alle seguenti domande:

    1. Determinare: a) la regione di funzionamento dei transistori ed i valori Vx,0 e Vy,0 corrispondenti
       a Vi1,0 = Vi2,0 = VCC /2; b) la regione di funzionamento dei transistori corrispondente a Vi1,0 =
       Vi2,0 = VCC (12 punti).

    2. Tracciare il circuito equivalente per piccoli segnali nel punto di riposo corrispondente alla condizione
       (a) di cui al quesito precedente, e determinare il valore dei corrispondenti parametri differenziali (6
       punti).

    3. Calcolare l’espressione analitica del guadagno di tensione per piccoli segnali vy /vi1 nell’ipotesi che:
       a) vi1 = vi2 ; b) vi1 = −vi2 (8 punti).

Valori dei parametri:
VCC = 10 V, βF,npn = βF,pnp = β0,npn = β0,pnp = 50, Vth = 0.025 V, IS,npn = IS,pnp = 10−15 A,
Rx = Ry = R = 1 kΩ.


                                                                               VCC


                                                                                         Rx

                                                                                      Vx
                                                            Vi1                                      Vi2

                                                                                     Vy

                                                                                         Ry



                                                                           FIGURA 1
                                                                   "!#  $
                                                                                      %'&)( $* (  %++,
 -/. 021435657575657565757565756575756575657575657565757565756598:.4; <=. 0214356575657575657565757565756575756575657575657565757565?>A@CBED?FHGI. JH@356575657565757565756575
  KML <BNFPORQNQE17; < @CBNFS3575657565759T565657575659T575657565759TVUW56575756575657575
    8:. <XD?FZY[17D?FH0216<BE.@4J G7FZD?G7L FZBE.\ F ]FZ; L=D?@X^/_`<=16J aL @4JZ1bF4BED?@4< QNFHQEBE.4D?Fcd/1'ce<=. <fQE. <=./QEg16<BNFC1MQE. <=.g17DNY[17BEBN@40216<BE1
   GI. 02ghJZ160216<BN@CD?F[i?j=16\k@4FPlC@4JZ.4D?FmFH< \ FHG7@CBNF\=16Fgh@CD?@40217BED?FSj QNFPD?FHQEg. < \ @@4JHJZ1XQE17; L=16<BNFn\=. 0V@4< \=143
            ^C5/oR16QNGID?FZl417DN1FH<k0216<=.p\ Fb^7q4qVgh@CDN. JZ1rFHJPY`L <=s6FZ. < @40216<BE.p\=16JmG7FZD?G7L FZBE.21JZ1rQNL=1rG7@CD?@CBEBE17D?FHQEBNFHG?t=1r16QNQE16<=s6FH@4JHFM_Su
                ghL <BNF[i?5
          u5/oR17BE17D?0VFH< @CDN1vFHJ/lC@4JZ.4DN1v\ F/w'exBN@4JZ1vG?t=143y@ipJSz FH02g16\=16<=s6@{\ FRFH<=;4DN16QNQE.y@4JQE16GI. < \=.)QEBN@4\ FZ.)\=16JRG7FZD?G7L FZBE.
                    _[|6} ei/lFHQEBN@; L @CD?\ @4< \=."\=16<BEDN.kJH@~h@4QE12\=16JBED?@4< QNFHQEBE.4DN1pcejnQNFH@pgh@CD?F@^Vm~i/JH@g.4BE16<=s6@@4QNQE.4DN~hFZBN@
                 \ @4JHJSz @4JHFH0216<BN@Cs6FZ. <=1X\ @gh@CDNBE1r\=16JPQE16GI. < \=.pQEBN@4\ FZ.VQNFH@gh@CD?FP@2CqVP_^7qVghL <BNF[i?5
            5/oR17BE17D?0VFH< @CDN1FHJhlC@4JZ.4DN1\ Fhg. JH@CD?FZs7s6@Cs6FZ. <=1R\=16JHJH@fBE16< QNFZ. <=1\ FhL QNG7FZBN@GI.4DND?FHQEg. < \=16<BE1R@4JHJZ1GI. < \ FZs6FZ. < Fh\ FhG7L F
                  @4JPghL <BE.2g DN16GI16\=16<BE1_[VghL <BNF[i?5
          =5/oR17BE17D?0VFH< @CDN1:L <fFH< QNFZ16021b\ F4DN16JH@Cs6FZ. < F <=16GI16QNQN@CD?FZ1M1:QNL=pG7FZ16<BNF @/\=16QNGID?FZl417DN1:FHJ GI. 02g.4DNBN@40216<BE.\=16J G7FZD?G7L FZBE.
                   FH<VDN17; FH021\ F ghFHG7GI. JHFhQE17; < @4JHFhQEBN@CBNFHG7F1G7@4JHGI. JH@CDN1JSz 16QEg DN16QNQNFZ. <=1/\=16Jh; L @4\ @C; <=.\ F BE16< QNFZ. <=1/46C}:_SfghL <BNF[i?5
b@4JZ.4D?Fm\=16Fgh@CD?@40217BED?FS3
     hPU  j h= dUh= erUh9 d2Uh9 eU^7q4qj=HUq q u425

                                                                                          VCC


                                                     Vi                                Qn                            Rp
                                                                                                                                    Vo
                                                                     Ven                                         Qp
                                                                    Rn

                                                                                                                                r_ip
                                                                                       ]N¡R¢/O£^
                                        Prova scritta di Fondamenti di Elettronica
                                                       14 luglio 2005
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Il dispositivo a due porte all’interno del riquadro a tratto continuo di Figura 1 è descritto, in regime di
piccoli segnali statici, dalla seguente matrice ibrida: hi = 1723 Ω, hr = 0, hf = 75, ho = 50 · 10−6 S. Con
riferimento ai valori dei parametri indicati, si risponda alle seguenti domande:

    1. Determinare l’espressione analitica ed il valore numerico dei parametri differenziali della matrice
       ammettenze del due porte (2 punti).

    2. Determinare il valore del resistore RL che connesso alla porta di uscita consente di ottenere un
       guadagno Av = vo /vg negativo e pari in modulo a 26 dB (8 punti).

    3. Determinare la configurazione (emettitore comune, base comune, collettore comune) ed il punto di
       lavoro (IC,0 , IB0 ) di uno stadio a singolo transistore BJT in grado di implementare l’amplificatore
       di cui ai punti precedenti ALLA TEMPERATURA DI 400 K. (6 punti).

    4. Determinare l’espressione analitica ed il valore numerico del guadagno di corrente io /ig dello stadio
       precedente (4 punti).

    5. Determinare il valore della tensione di polarizzazione Vg,0 e stimare il minimo valore della tensione
       di alimentazione VCC necessari al corretto funzionamento del circuito di cui ai punti precedenti,
       motivando le scelte effettuate nell’operare la stima. (4 punti).

    6. Discutere in meno di 100 parole i principali fattori cui si dovrebbe prestare attenzione nel caso si
       volesse sostituire al transistore bipolare utilizzato un transistore MOS nella medesima configurazione
       circuitale (cioè: emettitore comune ⇐⇒ source comune, base comune ⇐⇒ gate comune, collettore
       comune ⇐⇒ drain comune) (2 punti).

Valori dei parametri:
βF (400 K) = β0 (400 K) = 75, VA (400 K)=30 V, k = 1.38 · 10−23 J/K, q = 1.602 · 10−19 C,
Vth (300 K) = 0.0258 V, IS (400 K) = 10−14 A, RG = 100 Ω.



                                                     R_G                                                                    i_o
                                                                    v_i
                                                                                                                                      v_o
                                                                              i_i
                                                                                                      h
                          v_g                                                                                                       R_L



                                                                           FIGURA 1
                                                                      !#"$  %
                                                                                     &(' $( )+*,,-
.0/ 1325467686867686968686768676868676867686869686768686768676;:</5= > / 1325467686768686968676868676867686867686968686768676868676@?BADCFE@GIHJ/ KIA4L67686768676868676869686
 MON(>CPGQSRPRF28= > ADCPG468676867686;T67696868676;T68676867686;T#67686867686UTV67686968686UT68686768676;TXWY68676868676867686
   :</ >ZE@GI[\28E@G]1327>CF/^A5K_H8G`E@H8N(G`CF/ba G cGI= NdE@AZef27a A5G_gDA5K`/5E@G ad27G h(ADE@A51i28CFE@G_GI> a G]H8ADCPGkjLRPGSE@GIRPhl/ >(a AmA5KIKI2fRP28= Nd27>CPG
  ad/ 1iA5>(ad254
          eD6LMOEP/5=528CFCPADEP2mN(> AmE@28CF2nHJ/ RFCPG`CPN G`CPA^a AoN >ZN > G]HJ/oHJ/ 13hp/ >d27>CF2nH@q 25jSHJ/ KIKI28= ADCF/bCFE@A^GIK >d/ra /tsu.v2w1iA5RPR@Aj
              hp/ KIADE;G`x8x7G(GIKH8G`E@H8N GICF/yA3z({|@W~}_yjrHJ/ >#27>CFE@A51(GlGCFE;A5> RPGIRFCF/5E;G(GI>VEP28= G`/ >d2 >d/5E@1XA5K`2L2_H8A5KIHJ/ KIADE@2SGIKgDA5K`/5EP2 a G
                  _H;qd2~ad28CF28E@1XGI> Aiz({8W 6kh(N >CPG\;6
         6L GIRP28= > ADEP2GIKH8G`E;H8N G`CF/f27N(G`gA5KI27>CF2#hp28E3h(GIH8HJ/ KIGRP28= > A5KIGRFCPADx7G`/ >(ADE@G2H8A5KIHJ/ KIADEP2BGIK<gA5K`/5E@2ad27Gh(ADE@A51328CFE;G
                  a(Gl28E@27>dx7GIA5KIG5a GCPNdCFCPG = K]G 27K`271327>CPGrGI>_27RPRF/Sh EP27RP27>CPG>d27KIK`2OHJ/ >(a G`x7G`/ > G5a(G E@G`hp/ RF/0a G H8N GA5Kh(N(>CF/~eD6kh(N >CPG\;6
         r6LS28CF28E@1XGI> ADEP2K`2[N >dx7GI/ > GDa GDCFE@A5RF[28E@GI1327>CF/~  {|UD 2L  {9D jDG`hp/5CPG`x8x7A5> ad/hp28ERF2713hKIGIH8G`C A z((dW z r W  6
                   k¡3h(N >CPG\;6
       ¢d6LS28CF28E@1XGI> ADEP2yKk£¤27RFh EP27R@RPG`/ >d2 A5> A5K]G`CPGIH8Aiad27Gh(ADE@A51328CFE@Ga Gp28EP27>dx7GIA5K]Gl¥DU|S2_¥DFad27KIKIA31XADCFE@GIHJ2a 27KIK`2 HJ/ > a N Cu¦
               CPA5> x8254                                                                  §§             §         §            §
                                                                                               §§  §§§ Wª©¤«i© §§§ D¬ §§§                                                                ue9
                                                                                                 § ¨ {| §             §  {| §
                2H8A5KIHJ/ KIADE@>d2 G]KpgA5K`/5E@2 >N 1i28E@GIHJ/d6Lkh(N(>CPG\;¨ 6
A5K`/5E@G­ad27Gph(ADE@A51328CFE;Gk4
 ®(¯ bW±°D²j ®¯ mW±°D²jzd³7+W´²µ¶°fyj·z³@mWv²µ¶°¸j·z((+Wvz(mW  ²fj·z¹¹ªWºe8²wyjOzd»I¼tWv²µ½²  °fyj
  |·W¾e~¿dÀ 6

                                                                                                                              VCC
                                                                                               Ied                   R1
                                               I bp =Ibd                                                                                 VO1

                                         IN
                                                                              I cp =Ibn                                                   VO2
                                                                                Icd =Ien                             R2
                                                   rete da progettare
                                                                                      csFÁ_Â0Ã0QYe
                                        Prova scritta di Fondamenti di Elettronica
                                                    21 settembre 2005
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura 1 ed ai valori dei parametri indicati, si risponda alle seguenti
domande:

    1. Determinare la regione di funzionamento del transistore. (2 punti).

    2. Determinare il valore del resistore Ri necessario ad ottenere IB,0 = 1 mA, ed i corrispondenti valori
       di polarizzazione di tutte le tensioni e correnti del circuito (IL,0 , IE,0 , IC,0 , IR,0 , VBE,0 ). (10 punti).

    3. Calcolare il valore dei parametri del circuito equivalente per piccoli segnali corrispondente al punto
       di lavoro di cui sopra. (7 punti).

    4. Determinare l’espressione della trans-resistenza Rt (s) = vo (s)/ib (s) e calcolare la pulsazione cor-
       rispondente ai poli e zeri di Rt (s). (7 punti).

Valori dei parametri:
βF = 50, βR = 1, IS = 10−14 A, Vi,0 = VDD = 5 V, Vth = 0.025 V, R = 5 kΩ, L = 25µH.



                                                                                                     
                                                                                                     




                                                                                                     
                                                                                                                    V_dd

                                                                                                                  R

                                                R_i                                                                                v_o
                                                                                                             
                                                                                                                             
                                                                                                                             




                                                                                                             
                                                                                                                             
                                                                                                                             




                                                                                  i_i                                            L
                                            V_i,0+v_i                                                                    




                                                                                                                                 i_L
                                                                                                                         




                                                                                                                         




                                                                                                         
                                                                                                         




                                                                                                         
                                                                                                         




                                                                           FIGURA 1
                                        
                                                   
             !"#$%       
&'!# ()) !# ** * *   *   * +    
 "#,"#! % $#"$'#! -# .# /  # 0 %"# -# 1 " !"# #-#$ !#2 )# "#)1- # )'!# 3')#!#
   / 41!#55 - $6 #% !" )#)!" 7 % 0"# # "# " % -# ,'5# ! 2 -!"# " #% 0 %"
       )! 5# "# -# !'!! % !)##  $""!# % 1'! -# "#1) -% $#"$'#! 89 1'!#:
   ; <'11- $6 - ' #$"! -# !1" !'" -# ;= " -# $!#" -# $""#)1- ' #$"!
       -% 0 %" -# !'!!# # ")#)!"# -% >?2 $6 @AB + @AC )# 1"!# - ' 0 %" 1 "# - D=2 $6 % $G""! -#
       ) !'" 5# EF -#1- - %% !1" !'" )$- % % EF + EFG H;IJKLMNOPNQJRKLMNOPNSTU ))-
       VWXYZ[\Z % !1" !'" # " -# %)#')2 -!"# " #% 1'! -# % 0" -% $#"$'#! %% !1" !'"
       -# ];= " -# ^%0# _#')!#`$ " #  -# >= 1 "% #% "#)'%! ! !!'! 8D 1'!#:
   ]  %$% " #% 0 %" -%% !)# -# )%# ab $6 -)$"#0 # - !!# % % $ " !!"#)!#$ )! !#$
       EWC + EWC8acd : %%e#!" -% 1'! -# % 0" ]== ^ $ %$% ! # 1"$-5 8; 1'!#:
   f  g#) " #% $#"$'#! 3'#0 %! 1" 1#$$% ) % -% $#"$'#! 1"1)! 8f 1'!#:
   > <'11- -# 1!" ##!! " % $#"$'#! ' 1#$$% ) % -# !)# h[ -#"!! ! )'% ")!!
       -# i ) -% !" )#)!" 7&2 $ %$% " %e)1"))# -% ' -  -# !)# hjkh[ %%e#1!)# $6 #%
       - -# ')$#! )# $%% !  )) !" #! ' $-) !" l + / 1. 89 1'!#:
m %"# -# 1 " !"# ]== ^ nc 8]==o : + /] pq2 nU 8]==o : + />= pq2 nr8]==o : + /]> pq2 aWW + ] m 2
ast 8]==o : + =u=;>D m 2 @AB8]==o : + @AC8]==o : + v=2 EF8]==o : + /=QUw (

                                                                        VCC
                                                  ICp
                                      R1                      RE

                                             IBp                              VO
                                                          QP

                                      R2                                 QN
                                                           IBn


                                                 .4_xy( /
                                                                        !#"$  %
                                                                                          &&('*),+ "%$-../
 021 35476898:8:898:8;8:8:898:898:8:898:898:8:8;8:898:8:898:898=<>17? @ 1 35476898:898:8:8;8:898:8:898:898:8:898:8;8:8:898:898:8:898BADCFEHGBIKJL1 MKC6N898:898:898:8:898:8;8:8
  OQPR@ESITVUSUH4:? @ CFESI68:898:898:8=W898;8:8:898=W898:898:898=W#8:898:8:898=XY898:8:8;8:898:898
   <>1 @ZG=I\[]4:G=IK3549@EH1^C7M_J:I\GBJ:P I\EH15` IaI\?b8cd4eC7IfFC7M\17GBIg`b49IihCFGBC7354:EHGBIgIj@ ` IKJ:CFESIlkUSIG=IKUHhi1 @ ` CmC7IgUH4:? Pb49@ESIgnoPb49USI\ESI6
            cF8NJ:C7MjJL1 MKCFGS42Mpq49UHh GS49USUBI\1 @b4C7@ C7MKIKESIKJ:Ce`b49MKMjCeJ:CFGBCFEHEH4:GBIKUSESIKJ:C*UHESCFESIjJ:CIK@ ?7GS49USUH1FrsP UBJ:I\ESCtuvXxwzy|{:}=~N=kEH49@ 49@ `b1*49UHr
                hMKIKJ:I\ESC73549@EH4JL1 @EH1`b49MKM\4` I\f74:G=UH4CFGS4:4N`b49IEHGBC7@RUSIKUHEH17GBIy|*9kVko2>42,GBIKUHhi4:EHESI\fFC73549@EH44EHGBC7USJ:PbGBC7@R`b1
                   Mpq4L4:EHEH1QCFGBM\78z@b1 M\EHGB47k J:C7MKJL1 MKCFGS4eESP EHEH4M\4eJL17GSGB49@ESI4MKC^EH49@ USI\1 @ 4e` IP USJ:I\ESC5@ 49MgJ:I\GBJ:P IKEH1mhi4:GNIjMihRP @EH1` I
                 hi1 MKCF9IK:9CF9I\1 @b4e{L u X 53Tyl^hRPR@ESI]=
          o8=Fb|:7 g 7¡£¢F¤ |¥ :¦l¦¨§7=¤ª©FkNJ:C7MKJL1 MKCFGS4«IhCFGBC7354:EHGBIV` I¬i4:GS49@b9IKC7MjI` IESP EHESI2INEHGBC7@ USIKUSEH17GBI
                  ­ I\hi1 MKCFGBIGS49MKCFESI\fFC73549@EH4*C7MhRP @EH1` IiGBIKh1 US1^J:C7MjJL1 MKCFEH1®C7MhP @EH15hRGS49JL49`b49@EH4®y¯hRP @ESI]=
           ° 8N`RIKUH4:? @ CFGS4dIKMJ:IKGBJ:P I\EH1^49noP I\fFC7M\49@EH4dC7IhIKJ:JL1 MKIiUH4:? @ C7MKIi4eJ:C7MjJL1 MKCFGS4*Mlpq49USh GS49USUSIK1 @b4V` 49MKMKCmEHGBC7@ U=W±J:CFG=CFEHEH4:GBIKUHESIKJ:C
                    Ij@b?7GS49USUH1FrsPRUSJ:I\ESC^² uz³´  yc:µ5hRP @ESI]=
         ¯b8N`RIK3549@ USIK1 @ CFGS4dMKCJ:CFhRC7J:IKE C#¶ ·¸IK@¹351`b1ESC7MK4JBº 4Mlpq49UHhRGS49USUSI\1 @ 4*` I² u ³´h GB49UH49@ESIP @Zhi1 M\1»C7MjMKC^[]GB49nPb49@ 9C
                     wL¼eX ½FµA¿¾2®y¯hP @ESI=8
ÀC7M\17GBI,`b49IÁhRCFGBC734:EHGBIl6»ÂÃXÄ½¹ÅbÆ kÁtÇÇXÈ½DÀmk*»XÉFVFkQV#XÈF27kÊRËiÌÍXÎÊRË ¼ XÄÏ±µk>tRÐRÌ£X ° µÑÀmk
    tRÐ ¼ X ° µ»Àkt ÒKÓX 7Ô53À8

                                                                                                                                                  VCC
                                           Ii
                                                                                T3                                              T4
                                                                                                                                                  VO

                                             T1                                               T2
                                                                                                                                    R
                                                                              C


                                                                                          aHÕdÖ2×2TYc
                                                                   !#"$ %
                                                                                    &' ( ) &**,+
-/. 0214356575657565756565856575656575657565657565856565756575:9;.4< =>. 0214357565756565756585656575657565657565756565856575656575@?BADCFEHGJIK. LJAM358565756565756575657565
 NPO =QC@GSRT@TF16< = ADC@GU3/56575656575:VQ57575656585:VQ57565756575:V56585656575:V2WX56575658565657565
            9;. =YEHG[Z\16EHGJ0]17=QCF.^A4L_I6GJEHI6O G[CF.^` G_aG[< O>EHAcbd17`YA4G_efA4LJ.4EHG`>17G/g$ADEHA40]16CFEHG_GJ= ` GhI6ADC@GT@GEHGhTFg. = ` AiA4G/TF16< O 17=C@G
  j O 17T@G[C@GU3
          b8kmlUn]NoO =QC@Gpk:5,q16CF16EH02GJ= ADEH1rL[.2TFC@ADCF.s` 17GSCFEHA4= T@GhTFCF.4EHGSIK.4E@EHGhTFg. = `>17=QCF1tAvu wyx]W{zD|1u wyx]W}u$~S~o5
        n kmlUNoO =QC@Gpk:52q16CF16EH02GJ= ADEH12GJLefA4LJ.4E@12` GPu wxBIH>1vg.4EHC@AGJLCFEHA4= T@GhTFCF.4E@1srn#A Z\O = 7G[. = ADE@1]T@O LhLJA#TF.4< LJGJA`>17LhLJA
               E@16< GJ. =>1r` GST@ADC@O>E:AD7G[. =>1r17` GhLSIK.4E@EHGJTFg. = ` 17=CF1teDA4L[.4E@1r` Gu  5
          kmlU]NoO =QC@Gpk:5Pq16CF16EH02GJ=$ADE@1rGJLSI6G[EHI6O$G[CF.]1 j O$G[efA4LJ17=CF1rGJ= E@16< GJ0]1r` GgGJI6IK. L[.2TF16< = A4LJ1IK.4E@EHGJT@g. =$`>17=CF1rA4Lg$O =QCF.
                ` GSLhA7e4.4E@.u wyx]W(bK| 17`dGJLefA4LJ.4E@1r`>17GIK.4E@E:GJTFg. = `>17=QC@Gg$ADEHA40]16CFEHGS`$Gy16EH17=>7GJA4LJGU5
       QkmlUNPO$=C@Gpk:5t%g.4C@G[67A4= `>.#IH>1]CFE:AsLUO$T@I6G[C@Au>1!0vA4T@T@A#T@GJAIK. LJL[16< ADC@AO =$AsGJ02g17` 17=>7AIK. TFC@G[C@O G[C@A#` A4LhLJA
                 IK. = = 17T@T@G[. =>1!TF16EHG[1!` GO =dIK. = ` 17= T@ADCF.4E@1v17`iO =dGJ=$` O>CFCF.4E@1!{`>16CF16EH02GJ=$ADE@1LU17T@g E@17T@T@GJ. =>1`>17L< O A4` AD< =>.
                  u  lUfkF4u wyxlUDko1rCFEHA4I6I6GJADEH1GJLS` GJAD<4E:A40202A]` GS;.M`>1`>17LST@O .20].`$O L[.>5
   u$~S~mW{nf|!$7vW(b6zS 8R>¡¢£W¤¡$¥/W{nDzM ¡¦iW(bDu>§J¨W n4©fª«u25

                                                                                   V cc
                                                                                                        Q1
                                                                                                         Vx
                                                                         Vin                            Q2

                                                                                                        Vy
                                                                                                       Q3

                                                                                  aF¬t­®/R¯b
                                        Prova scritta di Fondamenti di Elettronica
                                                       2 luglio 2007
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 ed ai valori dei parametri indicati si risponda ai seguenti
quesiti:

    1) (10 Punti). Considerando un modello a soglia per il solo diodo D, disegnare qualitativamente la
       caratteristica statica VO = f (Vin ) del circuito per Vin compresa tra 0 e VCC , calcolando i valori di
       tensione dei punti pi significativi della caratteristica.

    2) (2 Punti). Determinare il valore esatto di VCE,sat per σ = 0.8.

    3) (8 Punti). Determinare il circuito equivalente in regime di piccolo segnale e i parametri differenziali
       corrispondenti al punto di lavoro Vin = 1 V, e l’espressione del guadagno di corrente di corto circuito
       Ai,CC .

    4) (6 Punti). Dimensionare i condensatori C1 e C2 in modo tale che il guadagno di corrente di corto
       circuito Ai,CC presenti un polo e uno zero in ωp = 3 krad/s e ωz = 900 krad/s, rispettivamente.
       Inoltre calcolare il valore di Ai,CC per ω = 20 krad/s.

VCC = 5V, IS = 10−14 A, βF = β0 = 100, βR = 1, Vth = 25mV , R = 1kΩ, Vγ,D = 0.6V, VA = 30V,
CBC = 1pF, CBE = 3pF.


                                                                                      Vcc

                                                                                                         R
                                                                                 C2
                                                                 D                                           VO
                                                     Vin
                                                                                                     Q

                                                                       C1


                                                                           FIGURA 1
                                                                     !#"$  %
                                                                                      &' "$(*)+"%$,--.
/10 2436578797978797:7979787978797978797879797:797879797879787<;=06> ? 0 2436578797879797:79787979787978797978797:79797879787979787A@CBEDGFAHJIK0 LJB5M7879787978797978797:797
 NPOQ?DRHSUTRTG39> ? BEDRH579787978797<V787:7979787<V79787978797<V#78797978797WVX78797:79797WV79797879787<VZY[79787979787978797
  ;=0 ?\FAHJ]^39FAH_2438?DG0`B6L+I9HaF<I9O HaDG0`b HcHa>d7ef38bgB6H+hEB6La06FAHB6TRTG39> ?QBEDRHbd38HiQBEFAB62j39DGFAH+TRHFAHJTRik0 ?Qb BXB6H+TR39> Od38?DRHPlOd38TAHaDRH
    m DGFAB6TRI9O FABEFR3nLpoq3Krs39DGDG0ZtuBEFALav#?d38LJLa3wbd0 2jB6?Qbd3jeExyf3nz {<5
              eE7MNPFR06>639DGDRBEFR3`HJLPFR38TRHJTGDG06FA3X| }jHJ?~240b 0DRB6La3#IAd3#HJL+iO ?DG0b HPL_B8h606FR0\bd38LuDGFAB6? TRHJTRDG06FR3XTRH_BC %YeE7 mp
                  iO ?DRH{
            y7MU39DG39FA2ZHJ? BEFR3HJLI9HJFAI9O HaDG0f38lO HahEB6La38?DG3wis39FiQH_I9IK0 La0jTG39> ? B6La3w3whEB6LJOdDRBEFA3HsiQBEFAB62439DGFAHb Hrs39FR38?d8HJB6LJHkbd38LsDGFAB6?d
                     TAHJTGDG06F87 m iO ?DRH{
             z7U;B6LJIK0 LJBEFR3ZLoq38TGi FR38TRTAHa0 ?d34bd38L+> O B6bQBE> ?d0Cb HDG38?QTRHa0 ?d3j69E*? 38LJLpoHais06DG38TRHIA 3XLpoO TAI9HaDRB`TRHJBIK0 L_La39> BEDRBB6b~O ?
                      I9BEF<HJIK0jiQOdF<B62438?DG3wFA38TRHJTGDRHah60j| 7 m e94iQO ?DRH^{
            7UdOdi is0 ?d38? bd0Q Y¡yE¢38b~HJ?h£BEFAH_BEDRBLJBCIK06FRFR38?DG3b H¤QB6TG3Xb 38LDGFAB6? TAHJTGDG06FR36x+bd39DG39FA2ZHJ? BEFR3ZL_B2jB6TRTRH_2jB
                   hEBEFAHJBE8HJ0 ?d3fik39F<IK38?DRO B6LJ3jb H|U}fI<d3Z2jB6?DRHa38?d3jHJLDGFAB6?QTRHJTGDG06FR34HJ?\FA39> Ha0 ?d3j?d06FA2ZB6La34b H]O ? 8Ha0 ? B62438?DG0d7 mp
                    iO ?DRH{
   ¥¥\Y¦zfxsd§J¨nY  y6jx©8ªZY«e9¬­ } 2jSx | ­ Y E666X®wx ¯Q°gY  x ¯Q±MY³²E7

                                                                                                  VCC


                                                                                                       L
                                                                                                               C1
                                                                                                                             VI




                                                          R1                                                     C 2 VO
                                                                                                      R2



                                                                                     c´Gµw¶1·1S[e
                                        Prova scritta di Fondamenti di Elettronica
                                                    05 settembre 2007
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Fig. 1, in cui il resistore R2 presenta una debole non linearità descritta
dalla relazione R2 = VR2 /IR2 = R20 + R21 · VR2 , si risponda ai seguenti quesiti utilizzano i valori assegnati
dei parametri:

    1. Determinare il valore stazionario di Vbe ed il corrispondente valore stazionario di Vo per Ii,0 = 0 A.
       (12 punti)

    2. Determinare il circuito equivalente per piccolo segnale e valutare i parametri differenziali di tutti i
       componenti. (8 punti)

    3. Calcolare l’espressione ed il valore numerico della transresistenza vo /ii . (6 punti)



                                                                   VCC,1                                           VCC,2

                                                                       R1                                            R2


                                                                                                                               VO
                                   Ii
                                                                                    V be



VCC,1 = 5 V, VCC,2 = 25 V, Vth = 0.0258 V, JS = 10−9 µA/µm2 , Area di giunzione del transistore
1: A1 = 100 µm2 , Area di giunzione del transistore 2: A2 = 500 µm2 , R1 = 10 kΩ, R20 = 7 kΩ,
R21 = 100 Ω/V, βF 1 = βF 2 = β01 = β02 = 20.
                                        Prova scritta di Fondamenti di Elettronica
                                                    18 settembre 2007
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Fig. 1, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare la caratteristica statica Vo = Vo (Vi ) nell’intervallo di −VCC ≤ Vi ≤ VCC , indicando
       chiaramente le regioni di funzionamento del transistore e le coordinate dei punti salienti. (10 punti)

    2. Determinare il circuito equivalente per piccolo segnale e valutare i parametri differenziali di tutti i
       componenti nel punto di lavoro corrispondente a Vo = 0 V. (8 punti)

    3. Calcolare l’espressione ed il valore numerico del guadagno di tensione vo /vi , il valore numerico dei
       suoi poli e zeri e tracciare il diagramma di Bode del suo valore assoluto. Infine indicare una possibile
       applicazione del circuito esaminato. (8 punti)




                                                                                                             VCC

                                                                                                                RC
                                                           L
                                                                                     RB
                                                                                                                             VO
                                                           C


                                                                                                       Vi

VCC = 3 V, Vγ,BE = 0.5 V, Vγ,BC = 0.3 V, RB = 1 kΩ, RC = 5 kΩ, L = 1 µH, C = 1 nF, Vth = 25.8 mV,
βF = 50, β0 = 60.
                                        Prova scritta di Fondamenti di Elettronica
                                                     19 dicembre 2007
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Fig. 1, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare la topologia del circuito amplificatore (emettitore, base o collettore comune) e la
       funzione di trasferimento vo /ig comprensiva dell’effetto delle capacitá Cbe e Cbc . (10 punti)

    2. Progettare uno specchio di corrente che, alimentato tra VXX = +2 V e massa, polarizzi il circuito
       di figura a Ig = 100 µA (10 punti).

    3. Determinare i parametri differenziali del transistore in Figura 1 e la frequenza dei poli di vo /ig . (6
       punti)

VXX = 2 V, VY Y = −2 V, Vth = 0.025 V, IS = 1 fA, RL = 10.4 kΩ, CL = 1 pF, Cbe = 300 fF, Cbc = 50 fF,
βF = 25, β0 = 25.



                                                                                         CL


                                                                                                                 VO
                                   Ig
                                                                                                                   RL

                                                                                                               V YY
                                        Prova scritta di Fondamenti di Elettronica
                                                      19 marzo 2008
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Fig. 1, nel quale i transistori T3 e T4 hanno area 5 volte superiore a quella
dei transistori T1 e T2 mentre le coppie di transistori npn e pnp T1-T2 e T3-T4 hanno caratteristiche
perfettamente duali, si risponda ai seguenti quesiti utilizzando i valori assegnati dei parametri:

    1. Determinare il punto di lavoro del circuito corrispondente alla tensione stazionaria di ingresso
       Vi,0 = 50 V (Vo,0 , IC1,0 , IC2,0 , IC3,0 , IC4,0 ). (12 punti)

    2. Determinare i parametri differenziali dei transistori. (4 punti)

    3. Determinare l’espressione della funzione di trasferimento Vo (s)/Vi (s), calcolare la frequenza di poli
       e zeri e tracciare l’andamento del diagramma di Bode di |vo /vi |. (10 punti)


                                                                                     VCC

                                                                    T1                               T3


                                                                                   Rp

                                                   Vi                                                         VO
                                                                   C
                                                                                   Rn


                                                                     T2                              T4



Vi,0 = 50 V, VCC = 4 V, Vth = 25.8 mV, IS (T1 ) = 10 fA, Rn = Rp = 5 kΩ, Ci = 3 pF, VA,n = VA,p = 50 V
βF 0,n = βF 0,p = 50.
                                        Prova scritta di Fondamenti di Elettronica
                                                      23 giugno 2008
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Fig. 1:

    1. Determinare RL e RB in modo tale da polarizzare il transistore nella condizione VO =0 V, IB =10 µA.
       (8 punti)

    2. Determinare di quanto varierebbe la tensione di uscita VO (a paritá di RB e RL calcolate al punto
       precedente) nel caso in transistore presentasse una tensione di Early VA = 20 V. (8 punti)

    3. Nell’ipotesi che la tensione di alimentazione sia affetta da un rumore vCC di piccola ampiezza,
       determinare la funzione di trasferimento vO /vCC nel dominio di Laplace (Si trascuri l’effetto Early).
       (8 punti)

    4. Determinare la variazione della tensione di uscita corrisponderente all’applicazione di una tensione
       di alimentazione VCC = 2.05 V. (2 punti)

                                                                                                   VCC


                                                                                                         L

                                                                             IB

                                                                                                                     VO
                                          C                                  RB
                                                                                                        RL

                                                                                                   VSS
VSS = −2 V, VCC = 2 V, Vth = 25.8 mV, IS = 10 fA, βF 0 = 100.
                                        Prova scritta di Fondamenti di Elettronica
                                                       15 luglio 2008
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Fig. 1, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare il valore di RL che porta Qp a lavorare alla soglia tra regione lineare e di saturazione
       ed i corrispondenti valori di tutte le tensioni e correnti nel circuito. (10 punti)

    2. Determinare i parametri differenziali dei transistori. (4 punti)

    3. Supponendo ora di collegare un induttore L2 tra i morsetti di base e collettore del transistore Qp
       disegnare il circuito equivalente ai piccoli segnali e determinare le espressioni analitiche ed il valore
       numerico del guadagno di tensione vo /vi , della resistenza di ingresso vi /ii e della resistenza di uscita
       vo /io del circuito per ω = 0 e ω = ∞. (12 punti)



                                                                                                                    V CC
                                                                 L1

                                                                                                             Qp

                                        VI                                              Qn                        VO

                                                                                                                  RL



Vth = 25.8 mV, ISn = 10 fA, ISp = 5ISn , βF 0,n = βF 0,p = 50. VCC = 1.5 V, L1 = 0.1 nH
                                        Prova scritta di Fondamenti di Elettronica
                                                     9 settembre 2008
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Fig. 1, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare i valori di RL ed R2 in modo tale che la potenza statica dissipata dal circuito per
       Vi = 0 valga P = 10 mW e che le tensioni di uscita siano pari a Vo1 = −Vo2 = VCC /2. (12 punti)

    2. Determinare l’espressione delle funzioni di trasferimento Fc (s) = (v01 + vo2 )/2vi e Fd (s) = (v01 −
       vo2 )/vi . A tal fine si consideri anche l’effetto delle capacitá delle giunzioni base-emettitore dei
       transistori. (10 punti)

    3. Si determini il valore dell’induttanza L tale per cui Fc (s) presenta uno zero alla pulsazione ω = 100
       MHz e si calcoli la frequenza di tutti gli altri poli e zeri di Fc (s). (4 punti)



                                                                                    VCC
                                                                             R1
                                                                                                               VO1

                                                                                                         L
                                                                             R2
                                                                                                         RL

                                                 Vi
                                                               C                                          RL
                                                                             R2

                                                                                                          L

                                                               R1                                             VO2

                                                                                    VCC

Vth = 25 mV, R1 = 1 kΩ, βF 0,n = βF 0,p = 60, VCC = 2 V, Vγ = 0.55 V, Cbe,n = Cbe,p = 1 pF
                                                                    !#"$  %
                                                                                      &('*) +$ &,,-
 .0/ 1325467686867686968686768676868676867686869686768686768676;:</5= > / 1325467686768686968676868676867686867686968686768676868676@?BADCFEHGJIK/ LJA4M67686768676868676869686
  NPOQ>C@GRTS@SF28= > ADC@G468676867686;U67696868676;U68676867686;U#67686867686VUW67686968686VU68686768676;UYXZ68676868676867686
   :</ >[E;G]\^28E;GJ1327>CF/_A5LI8G]EHI8O GJCF/_` GaG]=b6McDdS@GE;GJSFef/ > ` AgA5GSF28= O 27>C@G0hOb27SHG]C@GObC@GJLiG]j8j7A5> `b/kGlDA5L]/5EHGA5SHSF28= > ADC@GM` 27G
eQADEHA51m28CFEHGn4
           cD6MoT28CF28EH1YGJ> ADE@2MGiLblpA5LJ/5E@20`b27LiLJA CF27> S@G]/ > 2M` Gbef/ LJADEHGJj8j7ADj7G]/ >b2Tqrs(d` 27LJLJAtCF27> SHG]/ >b2M` GQO S@I8G]C@Aqu<d` 27LQIK/ > S@OQ13/
                `QGvef/5CF27>bj7AwSFC@ADC@GJIK/B`b27LI8G]E;I8O G]CF/wIK/5E@EHGiSFef/ > `b27>CF2mA5`_O > AwIK/5EHE@27>CF2` Gef/ LJADEHG]j8j7ADj7GJ/ >b2Y`b27LJLiAWxA5SF2meQADEHGPA
                     c8yDz{R6|n}~eO >C@G
         6MoT28CF28EH1YGJ> ADE@2mLJA#CF271me+28E;ADC@ObEHA#/5ef28EHADC@G]lDA`b27LCFEHA5> SHGJSFCF/5E@2mS@O e ef/ >b27> `b/#IHb2mLiA#E@27S@GJSFCF27> j7A#CF28EH1mGJI8ACFE;AGJL
                 `QGJSFef/ S@G]C@G]l5/2 LnA51xQG]27>CF2S@GJA~eADEHGAmXc8y tUp8: 6|meQO >C@G^
          6MNPE@/5=528CFC@ADE@2O >QAE@28CF2tIH 2 S@/ SFC@G]C@O GJSHI8A GJL=527>b28EHADCF/5E@2t` G+IK/5E@E@27>CF2t` G+GJ>b=5E@27S@S@/ 2tIHb2Tef/ LJADEHG]j8j7GGJLCFEHA5> S@GJS@CF/5E@2
                  > 27LJL]/3SFCF27S@SF/YeQO >CF/m` GLJA7l5/5EH/W`b27LfeQOQ>CF/|c9;6 |n}~eQO >C@G^
       b6Mo GJS@28= > ADE@2GiLI8G]EHI8O GJCF/_27hOQG]lpA5LJ27>CF2wef28EWeQGJI8IK/ L]/S@28= > A5L]2IK/5EHEHGJSFef/ > `b27>CF2wA5LeO >CF/` GLJA9l5/5E@/*` GI8O G0A5L
                   hOb27S@GJCF/|c9(2`b28CF28EH1YGJ> ADE@2Ln27S@e E@27S@S@GJ/ >b2t`b27LJL]2 CFEHA5> SFGJ13ef27`b27>bj82  K$ 2t5¡  60|n¢3eQO >C@G^
          £ 6MoT28CF28EH1YGJ> ADE@2 LnA513eQGJ28j8j7A`b27LiLJA IK/ 13ef/ >b27>CF2 ` GS@28= > A5L]2 `b27LJLJA CF27> S@G]/ >b2T` G+O S@I8G]C@AIK/5E@EHGJS@e+/ >Q`b27>CF20A5`OQ> A
                    IK/5EHE@27>CF2` G{SF28= > A5LJ2` GGJ>b=5E@27SHSF/3eQADEHGAwcz{R¤A5LJLiA~eQO LJS@ADj7GJ/ >b2T`QGvc8y5¥tEHA5`UpS86T|  eQO >C@G^

                                                             VCC


                                                                                                         L2
                                                                                                                                       VO

                                     IB                                            VE
                                                                                                                    R                             C
                                                                                 L1



 q ¦J§X 5£ 1m¨d©ªX «b¬ d­®X¯cW> ° d­P±YX²cY> ° dv³ªX¯cW> a<dµ´Q¶X¯c8y5yd·7r{sµ¸X¹yºJcWeQRdqQ»»X  ¨
¼½@¾ X 5£ 7:
                                        Prova scritta di Fondamenti di Elettronica
                                                     18 febbraio 2009
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

I bipoli R e G del circuito di Figura 1 sono descritti dalle seguenti caratteristiche statiche ai morsetti:
                                                                          p
                                                              VR = α IR (bipolo R)
                                                                 IG = βVG2 (bipolo G)


     Si risponda ai seguenti quesiti utilizzando i valori assegnati dei parametri:

    1. Determinare il valore statico di VG , VR , IR ed IG corrispondente alla tensione di polarizzazione V ∗ .
       (10 punti)

    2. Disegnare il circuito equivalente per piccolo segnale e determinare l’espressione analitica ed il valore
       numerico dei suoi componenti. (10 punti)

    3. Determinare la pulsazione di risonanza del circuito di piccolo segnale, l’ampiezza e la fase della
       componente di segnale della tensione vG alla pulsazione di risonanza ed alla pulsazione di 106 rad/s
       corrispondente ad una tensione di segnale v ∗ = 1 mV a fase 0. (6 punti)



                                                             L                               IR             VG
                                                                                      R

                                                                                  VR                   G                  C
                                                     V*
                                                                                               IG

                                          √
V ∗ = 1 V, L = 1 nH, C = 1 nF, α = 100 V / A, β = 10−4 A/V 2 v ∗ = 1 mV
                                        Prova scritta di Fondamenti di Elettronica
                                                      18 giugno 2009
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Fig. 1, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare le regioni di funzionamento dei diodi al variare della tensione Vg2 e la caratteristica
       statica VO (Vg2 ) per Vg1 =2 V. (8 punti)

    2. Tracciare il grafico della caratteristica VO (Vg2 ) calcolata al punto 1 per un generico valore di Vg1 .
       (4 punti)

    3. Per il punto di lavoro Vg1 =2 V, Vg2 =4 V, perfezionare il calcolo di VO utilizzando il modello
       esponenziale del diodo, considerando IS =10−15 A. (6 punti)

    4. Determinare il circuito equivalente per piccolo segnale e i valori dei parametri differenziali cor-
       rispondenti a Vg1 =2 V, Vg2 =4 V. (4 punti)

    5. Per il punto di cui sopra, determinare VO (s)/Vg2 (s) e il corrispondente diagramma di Bode del
       modulo. (4 punti)




                                                                                            D2
                                                                                                                          Vg2
                                                                                           R1
                                                          D1
                                                                                                VO
                                    Vg1
                                                                                           L

                                                                                        I2


                                                                                          R2



Vth = 30 mV, R1 = 1 kΩ, R2 = 1 kΩ, L = 1 µH, Vγ = 0.5 V, Vg1 ≥ 0, Vg2 ≥ 0.
                                        Prova scritta di Fondamenti di Elettronica
                                                       8 luglio 2009
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare la regione di funzionamento del transistore ed il valore di tutte le tensioni e correnti
       statiche nel circuito. (8 punti)

    2. Determinare il valore dei parametri differenziali del transistore nel punto di lavoro di cui al quesito
       precedente. (4 punti)

    3. Determinare l’espressione della funzione di trasferimento Vo (s)/Vi (s) nell’ipotesi che il valore della
       capacitá Co → ∞. (10 punti)

    4. Calcolare il valore delle frequenze di poli e zeri di Vo (s)/Vi (s) e tracciare l’andamento del corrispon-
       dente modulo (diagramma di Bode). (4 punti)




                                                                                                Vcc


                                                 RB
                                                                                                    L
                                                                                                                    VO
                                                     Vb
                                                                                                             CO
                                             Vi
                                                                            Ve                     C
                                                         Ci

                                                                               RE



Vth = 25 mV, RB = 1 kΩ, RE = 500 Ω, L = 2 µH, IS = 3 · 10−15 A, β0 = 80, βF = 80, VCC = 3.3 V,
C = 500 µF, Ci = 2 pF.
                                        Prova scritta di Fondamenti di Elettronica
                                                     4 settembre 2009
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 ed ai valori dei parametri indicati si risponda ai seguenti
quesiti:

    1) (10 Punti). Considerando un modello a soglia per il solo diodo D, disegnare qualitativamente la
       caratteristica statica VO = f (Vin ) del circuito per Vin compresa tra 0 e VEE , calcolando i valori di
       tensione dei punti piú significativi della caratteristica.

    2) (2 Punti). Determinare il valore esatto di VEC,sat per σ = 0.8.

    3) (8 Punti). Determinare il circuito equivalente in regime di piccolo segnale e i parametri differenziali
       corrispondenti al punto di lavoro Vin = 3.9 V, e l’espressione del guadagno di corrente di corto
       circuito Ai,CC .

    4) (6 Punti). Dimensionare i condensatori C1 e C2 in modo tale che il guadagno di corrente di corto
       circuito Ai,CC presenti un polo e uno zero in ωp = 3 krad/s e ωz = 900 krad/s, rispettivamente.
       Inoltre calcolare il valore di Ai,CC per ω = 20 krad/s.

VEE = 5V, IS = 10−14 A, βF = β0 = 100, βR = 1, Vth = 25mV , R = 1kΩ, Vγ,D = 0.6V, VA = 30V,
CBC = 100pF, CBE = 300pF.


                                                                                         VEE

                                                                           C1
                                                                    D
                                                        Vin
                                                                                                      Q
                                                                                                           VO
                                                                                    C2
                                                                                                       R


                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                    21 settembre 2009
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 ed ai valori dei parametri indicati si risponda ai seguenti
quesiti:

    1. Determinare il valore della corrente di polarizzazione del transistore pMOSFET (2 punti).

    2. Calcolare il valore della resistenza R e delle tensione di ingresso VI tali che la tensione di uscita in
       condizioni statiche sia pari a VC = 0.5 V. Determinare inoltre tutte le altre correnti e tensioni nel
       circuito (10 Punti).

    3. Calcolare i parametri differenziali dei transistori e disegnare il circuito equivalente ai piccoli segnali
       (4 Punti).

    4. Calcolare la resistenza di uscita al nodo VO dell’amplificatore realizzato (10 Punti).

VCC = 5V, VG = 4V, VO = 2.5 V, Vth = 25mV , VT M OS = −0.5 V, βM OS = 150µA/V2 , λ = 0.05 V−1 ,
IS = 10−14 A, βF = β0 = 50, VA = 30V.


                                                                                                 V CC
                                                                VG


                                                                                        VO
                                                                   VI

                                                                                            VC


                                                                                        R



                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                      26 gennaio 2010
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare Ro , RF e VO in modo tale che sia VX = VCC /2 e che la potenza statica dissipata
       dall’ultimo stadio contenente il transistore Tn sia P = 1 mW. (8 punti)

    2. Disegnare il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali
       del medesimo. (punti 4)

    3. Determinare l’espressione della funzione di trasferimento VO (s)/VGS (s). (10 punti)

    4. Calcolare il valore della frequenza del polo della funzione di trasferimento VO (s)/VGS (s). (4 punti)



                                                                                                                     Vcc


                                  R1                       Ib                               Ri2
                                                                                Tp

                                                                                                             Tn

                                                                Rf               Vx
                                                                                                                               Vo


                                  R2                              MOS                                                              C
                                                                                               Ro




Vth = 25 mV, R1 = 30 kΩ, R2 = 20 kΩ, IS = 10−15 A, β0,npn = β0,pnp = 60, βF,npn = βF,pnp = 60,
VCC = 5 V, βM OS = 200 · 10−6 A/V2 , VT = 1 V, λM OS = 0.1 V−1 , C = 1 nF.
                                        Prova scritta di Fondamenti di Elettronica
                                                       13 luglio 2010
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Il circuito di Figura opera alla temperatura di 80o C. Si risponda ai seguenti quesiti utilizzando i valori
assegnati dei parametri:

    1. Determinare il punto di lavoro del transistore, i valori statici di tutte le tensioni e correnti e la
       potenza statica dissipata dal circuito. (8 punti)

    2. Disegnare il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali.
       (punti 2)

    3. Determinare l’espressione delle funzioni di trasferimento Ve (s)/Ii (s) e Vc (s)/Ii (s). (10 punti)

    4. Tracciare l’andamento del diagramma di Bode di | (Ve (ω) − Vc (ω)) /Ii (ω)| e di | (Ve (ω) + Vc (ω)) /Ii (ω)|
       nella condizione Le (β0 + 1) = Lc β0 identificando la frequenza di poli e zeri. (6 punti)



                                                                                                          Vcc
                                                                                                             LE

                                                             C                                                      VE
                                          Vi                                                           Q1
                                                     Ii                                                             VC

                                                                         R                                    LC



IS,bjt (80o C) = IS,diodo (80o C) = 10−15 A, Vth (300K) = 0.026 V, VCC = 4 V, R = 50 kΩ, C = 10 pF,
βF (80o C) = 80, Lc = 7 mH.
                                        Prova scritta di Fondamenti di Elettronica
                                                     2 Settembre 2010
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare il fattore di forma S = W/L del transistore MOS necessario a polarizzare il transistore
       bipolare alla corrente di base IB = 5 µA, la regione di funzionamento dei transistori e il punto di
       lavoro (tensioni e correnti) dei componenti. (8 punti)

    2. Ipotizzando che gli effetti reattivi del transistore MOS possano essere schematizzati con una unica
       capacit connessa tra gate e source di valore CGS = 100 fF, si disegni il circuito equivalente per
       piccolo segnale e si calcoli il valore dei parametri differenziali dei transistori. (punti 2)

    3. Determinare l’espressione delle funzioni di trasferimento Vo (s)/Vi (s). (10 punti)

    4. Tracciare l’andamento del diagramma di Bode del modulo della funzione di trasferimento di cui al
       punto precedente identificando la frequenza di poli e zeri. (6 punti)


                                                                                                         Vcc

                                                                                                            RC
                                                      C1                                                            VO
                                     Vi

                                                                                                                      C
                                                                                                     Q1
                                                       RG
                                                                                          RB



Vγ,BJT = 0.7 V, Vth = 0.025 V, VCC = 3 V, |VT P,M OS | = 0.5 V, λM OS = 0 V −1 , RB = 1 kΩ, RG = 10
kΩ, RC = 3 kΩ, β " = 100 µA/V2 , βF = β0 = 50, C = 200 pF, CGS = 100 fF, C1 = 10 nF.
                                        Prova scritta di Fondamenti di Elettronica
                                                      26 gennaio 2011
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare l’area (A) della giunzione base-emettitore del transistore che consente di ottenere una
       tensione di collettore VC = 2.5 V. (8 punti)

    2. Commentare in meno di 50 parole l’efficacia della rete di polarizzazione adottata e la stabilitá del
       punto di riposo ottenuto (2 punti)

    3. Disegnare il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali
       nel punto di lavoro di cui al quesito precedente. (punti 4)

    4. Ipotizzando di collegare all’ingresso Vi un generatore di tensione con impedenza interna Rg =1 kΩ
       determinare l’espressione della funzione di trasferimento Vc (s)/Vg (s) nel caso semplificato in cui
       C1 → ∞, C2 → ∞ e L1 → ∞ e tracciare il corrispondente diagramma di Bode. (12 punti)




                                                                                                                  Vcc
                                                                   R1
                                                                                                 L2
                                                         C1
                                           Vi
                                                                                                         C2
                                                                                               Vc                     Vo


                                                                   L1                            R2



                                                                 VBB

JS = 10−15 A/µm2 , R1 = 1 kΩ, R2 = 2.5 kΩ, Rg = 1 kΩ, L2 = 0.47 µH, VCC = 5 V, VBB = 4.5 V,
βF 0 = β0 = 100, Vth = 25 mV.
                                        Prova scritta di Fondamenti di Elettronica
                                                     15 febbraio 2011
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Assumendo βF ! 1 per entrambi i transistori, determinare i valori di RB ed RC che consentono di
       polarizzare il circuito a IE,1 =10 µA e VC =3 V essendo VC la tensione di collettore dei transistori.
       (6 punti)

    2. Assumendo βF ! 1 per entrambi i transistori, determinare le relazioni IC (VBE ) ed IC (IB ) che
       consentono di modellizzare la coppia di transistori T 1 e T 2 come un unico transistore avente IC =
       IC,1 + IC,2 , VBE = VBE,1 + VBE,2 e IB = IB,1 . Dedurre da tali relazioni i valori efficaci del guadagno
       di corrente βF,e e della corrente di saturazione IS,e . (6 punti)

    3. Disegnare il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali
       dei transistori nel punto di lavoro di cui al quesito precedente. (punti 4)

    4. Supponendo di poter iniettare nel nodo B del circuito (base del transistore T1) una corrente di
       piccolo segnale avente trasformata di Laplace Ii (s), determinare l’espressione della funzione di
       trasferimento Vo (s)/Ii (s) (Vo = VC ), tracciare il corrispondente diagramma di Bode e determinare
       la corrispondente frequenza di taglio a −3 dB. (10 punti)



                                                                                                     Vcc


                                             RB                                             Rc


                                                                     T1                                                     C
                                                                                         T2



Vγ,BE =0.65 V, VCC = 6 V, βF 1 = βF 2 = βF = 100, β0,1 = β0,2 = β0 = 100, Vth = 25 mV, C = 1 pF.
                                        Prova scritta di Fondamenti di Elettronica
                                                       19 luglio 2011
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. utilizzando il metodo iterativo determinare il punto di lavoro dei transistori e la tensione di uscita
       a riposo VC . (12 punti)

    2. Determinare l’espressione analitica ed il valore numerico della resistenza differenziale corrispondente
       al transistore M1 ed il valore degli altri parametri differenziali del circuito. (4 punti)

    3. Supponento che la tensione di alimentazione subisca piccole fluttuazioni vCC sovrapposte al valore
       nominale VCC = 5V determinare l’equazione che fornisce l’espressione delle frequenze generalizzate
       s per le quali tali fluttuazioni non influiscono sulla tensione di uscita vC (zeri della funzione di
       trasferimento vC /vCC ). (punti 10)


                                                                                        Vcc


                                                                          M1           Rc           C

                                                                                       VC

                                                                                     T1 VE

                                                                            RE                      L




IS = 10−13 A, Vth = 25 mV, βF = β0 = 100, βn" = 100×10−6 A/V2 , W/L = 2, VT,n = 1 V, γM OS = 0V1/2 ,
λM OS = 0V−1 , VCC = 5 V, RC = 20 Ω.
                                        Prova scritta di Fondamenti di Elettronica
                                                     27 Gennaio 2012
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

Con riferimento al circuito di Figura si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare lo stato dei diodi DX , DY corrispondente a tutte le combinazioni degli ingressi (ViX ,
       ViY )=(0,0); (0, VDD ); (VDD , 0); (VDD , VDD ). (4 punti)

    2. Schematizzando i diodi nello stato ON con un modello a soglia ed una resistenza in serie di valore
       RX =RY =50 Ω, determinare la tensione ai nodi VX e VY corrispondente alle combinazioni degli
       ingressi (ViX , ViY )=(0,0); (VDD , 0); (VDD , VDD ). (12 punti)

    3. Scrivere le equazioni che consentono di calcolare le tensioni VX e VY corrispondenti alla combi-
       nazione degli ingressi (ViX , ViY )=(0, VDD ). (4 punti)

    4. Determinare l’equazione che descrive il transitorio della tensione VX corrispondente alla transizione
       (ViX , ViY ) = (VDD , VDD ) → (ViX , ViY ) = (VDD , 0) ed il tempo necessario alla tensione VX per
       compiere il 90% della propria escursione. (4 punti)

    5. Determinare il circuito equivalente di piccolo segnale ed il valore dei parametri diﬀerenziali dei diodi
       coerentemente con il modello adottato al punto precedente per la combinazione degli ingressi (VX ,
       VY )=(VDD , VDD ). (2 punti)



                                                                            Vcc
                                                                            R1
                                                                    DX                    VX
                                                         ViX
                                                                             R0
                                                                    DY
                                                         ViY                             VY
                                                                                                            C
                                                                             R2




VCC = 1.5 V, RX =RY =50Ω, Vγ =0.5 V, C=1 pF, R0 =100 Ω, R1 =1000 Ω, R2 =100 Ω
                                        Prova scritta di Fondamenti di Elettronica
                                                     23 febbraio 2012
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
domande:

    1. Determinare la regione di funzionamento del transistore e dimensionare il resistore R in modo tale
       da polarizzare il transistore ad una corrente di Base IB = 2 µA. (10 punti).

    2. Disegnare il circuito equivalente per piccoli segnali dello schema in figura e determinare l’espressione
       del guadagno di corrente io /ii esprimendo il medesimo come rapporto di due polinomi in s (10
       punti).

    3. Dimensionare il valore di L in modo tale che la frequenza di taglio del circuito valga f−3dB =
       100M Hz. Indicare se il circuito è di tipo passa alto o passa basso. (4 punti).

Valori dei parametri:
VCC = 2.5 V, VEE = −2.5 V, hF E = 50, Vth = 0.025 V, IS = 10−15 A, RL = 100Ω.


                                                                           Vcc


                                                                                     L             Io
                                                                                                              RL
                                                                                Vo
                                                                               VE
                                                                                                         Vi
                                                                  R                                Ii

                                                                                    VEE
                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                      19 giugno 2012
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

    Con riferimento allo specchio di corrente costituito dai transistori Q1, Q2 e Q3 e dal resistore R0 nel
circuito di Figura 1 e utilizzando i valori dei parametri sotto indicati, si chiede di:

    1. determinare il valore delle correnti statiche di polarizzazione IC1 , IC2 , IC3 . (9 punti).

    Con riferimento al circuito di Figura 1 e utilizzando i valori dei parametri sotto indicati, si chiede
inoltre di:

    2. Assumendo che il transistore Q4 si trovi in regione normale di funzionamento, determinare il valore
       delle correnti di polarizzazione dei transistori Q4 e Q5 ed il valore delle tensioni VB,4 , VC,4 , VE,4
       corrispondenti a Vi,0 = VCC trascurando per semplicitá l’effetto Early. (9 punti)

    3. Qual’é la regione di funzionamento del transistore Q5 ? Come si determina il valore della tensione
       Vo ? (4 punti)

    4. Considerando ovunque possibile l’effetto Early, disegnare il circuito equivalente per piccoli
       segnali del circuito in figura e determinare il valore dei parametri differenziali del transistore Q4.
       (8 punti)

Valori dei parametri:
VCC = 3.3 V, βF = 70, βR = 1, A1 = A3 = A4 = A5 = 1 µm2 , A2 = 20 µm2 , VA,1 = VA,2 = VA,3 = ∞,
VA,4 = VA,5 = 40V, Vth = 0.025 V, JS = IS,i /Ai = 10−13 A/µm2 , R0 = 1 kΩ, RB = 24 kΩ.


                                                         Vcc                                     Vcc

                                                                        Vi

                                                                                                     Q5
                                                                   RB
                                                    R0
                                                                                       Q4
                                                                                                        Vo
                                                                                                     Q2
                                                Q1                      Q3                                    C


                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                       10 luglio 2012
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

     Con riferimento al circuito di Figura 1 e utilizzando i valori dei parametri sotto indicati, si chiede di:

    1. determinare la regione di funzionamento del transistore ed il valore di tensioni e correnti statiche
       nel circuito. (8 punti).

    2. Disegnare il circuito equivalente di piccolo segnale e determinare il valore di tutti i parametri
       differenziali incluso quello della capacitá Cbe . (6 punti)

    3. Determinare la matrice ammettenze della parte di circuito racchiusa dalla linea tratteggiata. (6
       punti)

    4. Determinare l’espressione della funzione di rete Av (s) = Vo (s)/Vi (s) e tracciare il corrispondente
       diagramma di Bode. (8 punti)

    5. É possibile eliminare lo zero di Av (s) ? Come ? (2 punti)

Valori dei parametri:
VCC = 3 V, βF = 90, VA = ∞, Vg,0 = 2 V, Rg = 10 kΩ, R = 100 Ω, τbe = 0.2 ns Vth = 0.025 V,
IS = 10−14 A, Rf = 10Ω, C = 50 pF.


                                                                                          Vcc

                                                                                                                      R
                               Vg = Vg,0 + vg                                 Vi                     C
                                                                                                                                  Vo
                                                                   Rg                   Rf

                                                                                                                   T1
                                                                                       Cbe

                                                                           FIGURA 1
                                        Prova scritta di Fondamenti di Elettronica
                                                      30 gennaio 2013
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

    Con riferimento al circuito di Figura 1 ed utilizzando i valori dei parametri sotto indicati dove si é
indicato con IS0 il valore di riferimento della corrente di saturazione alla temeperatura di 25o C, si chiede
di:

    1. determinare i valori di Re ed Rc corrispondenti a Ib = 10 µA, Vc = VCC − 4V. (12 punti);

    2. ricalcolare il punto di lavoro del circuito alla temperatura di 100o C. (6 punti);

    3. disegnare il circuito equivalente di piccolo segnale e determinare il valore dei parametri diﬀerenziali
       del transistore e dei diodi alla temperatura di 25o C; (4 punti)

    4. determinare l’espressione ed il valore numerico dell’impedenza d’ingresso al transistore vista dal
       suo morsetto di base; (8 punti)

Valori dei parametri:
VCC = 6 V, IS0 = 10−15 A, IS (BJT ) = IS0 , IS (D1) = IS0 , IS (D2) = 2IS0 , IS (D3) = 3IS0 , IS (T ) =
IS0 × 2(T −T0 )/10 , R1 = 1kΩ, hF E = 80, Vth (25o C) = 0.02572 V.


                                                                           Vcc

                                                            R1                                            Re

                                                                                                                      Ve
                                                                   IB
                                                Vb                                                        T1
                                                               D1
                                                 ID                                                                   Vc
                                                               D2
                                                                                                           Rc
                                                               D3
                                        Prova scritta di Fondamenti di Elettronica
                                                     13 febbraio 2013
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1, tenendo conto dell’eﬀetto Early ed utilizzando modelli a soglia
per le giunzioni si chiede di:

    1. determinare il valore di RN =RP corrispondente a IBn = IBp = 20 µA, ID =150µA. Determinare
       inoltre il corrispondente valore di Vγ,npn =Vγ,pnp e della tensione Vo . (12 punti);

    2. supponendo ora che il circuito venga lievemente sbilanciato da una riduzione di βF 0p dal valore
       nominale al valore βF 0p =65, ricalcolare il corrispondente valore di Vo . (6 punti);

    3. disegnare il circuito equivalente di piccolo segnale e determinare il valore dei parametri diﬀerenziali
       dei transistori e dei diodi corrispondenti alla polarizzazione di cui al punto (1); (4 punti)

    4. determinare l’espressione ed il valore numerico della frequenza di polo del guadagno di tensione
       Vo (s)/Vbn (s) supponendo che l’uscita Vo sia collegata ad una capacitá di carico C=1 pF. (8 punti)

Valori dei parametri:
VCC = 2.5 V, Vγ,Dn =Vγ,Dp =0.6 V, VA,npn =VA,pnp =6 V, βF 0n = 70, βF 0p =70, Vth = 0.025 V.


                                                                             Vcc

                                                               RP
                                                                         IBp
                                                Vbp                                                        Tp
                                                                 Dp
                                                    ID                                                                Vo
                                                                 Dn
                                                Vbn                                                        Tn
                                                                          IBn
                                                               RN
                                        Prova scritta di Fondamenti di Elettronica
                                                       18 luglio 2013
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

    Con riferimento al circuito di Figura 1 dove le tensioni V1 e V2 sono fornite da opportuni generatori
in grado di garantire il funzionamento di T1 e T2 in regione normale diretta e utilizzando i valori dei
parametri sotto indicati, si chiede di:

    1. determinare il valore di Io corrispondente a Vo =0 V quando Vd =0 V. (12 punti);

    2. determinare a quale valore si porta la tensione Vo se i valori di tensione V1 e V2 vengono modiﬁcati in
       modo tale da produrre una tensione diﬀerenziale Vd =400 mV a paritá di tensione di modo comune
       Vc = (V1 + V2 )/2 rispetto al caso precedente. (6 punti);

    3. determinare l’espressione analitica della funzione di trasferimento Vo (s)/Vd (s) nel punto di lavoro
       di cui al quesito 1 e per il caso in cui all’uscita é collegata una capacitá CL verso massa. A tal ﬁne
       ricordiamo che vale la relazione IC1 = Io /(1 + exp(Vd /Vth )); (12 punti)

Valori dei parametri:
VCC = 5 V, βF 0 = β0 = 99, VA = ∞, RL =R=5 kΩ, Vth = 0.025 V, IS = 10−14 A.


                                                                          Vcc

                                                        R                              R
                                                                                            IB3
                                                                    VB3                                         T3
                                    V2               T2               T1                     V1
                                                                                                                              Vo
                                            Vd
                                                                                Io
                                                                                                               RL

                                                                −Vcc                                   −Vcc
                                                                             Figura 1
                                        Prova scritta di Fondamenti di Elettronica
                                                    12 settembre 2013
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

     Con riferimento al circuito di Figura 1 e utilizzando i valori dei parametri sotto indicati, si chiede di:

    1. determinare il valore il punto di lavoro del transistore e la corrente nell’induttore. A tal ﬁne si
       trascuri l’eﬀetto Early. (12 punti);

    2. disegnare il circuito equivalente di piccolo segnale e determinare il valore dei parametri diﬀerenziali
       del transistor tenendo esplicitamente conto dell’eﬀetto Early. (6 punti);

     Ipotizzando ora che tra il nodo B e la massa venga inserito un generatore di corrente di piccolo segnale
Ii (s)

    1. determinare la matrice ammettenza del due porte compreso all’interno della linea tratteggiata; (12
       punti)

    2. determinare la funzione di trasferimento Vo (s)/VB (s) e tracciare il diagramma di Bode del suo
       modulo e fase.

Valori dei parametri:
VCC = 5 V, βF 0 = β0 = 100, VA = 50 V, Rb = Rc =5 kΩ, Vth = 0.025 V, IS = 10−14 A.




                                                                    Vcc

                                                                      Rb

                                                      Vb
                                                                         L                  T1
                                                                                                              Io
                                                                                                                             Vo
                                                                                              Rc


                                                                 Figura 1
                                                                             Figura 1
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
                                        Prova scritta di Fondamenti di Elettronica
                                                      26 gennaio 2017
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, calcolare il punto di lavoro del circuito e tutte le tensioni e
       correnti. (12 punti)

    2. Disegnare, il circuito equivalente ai piccoli segnali e calcolare i parametri diﬀerenziali dei transistori.
       (4 punti)

    3. Calcolare la funzione di trasferimento VO (s)/VG (s) dell’amplificatore. (8 punti)

    4. Disegnare il diagramma di Bode del modulo del guadagno di tensione, indicando il valore degli
       eventuali poli e zeri e calcolare il valore massimo del guadagno. (6 punti)

RC = 5 kΩ, RB = 50 kΩ, RE = 525 Ω, VG = 5 V, VCC = 10 V, Vth = 25 mV, IS = 10−14 A,
βF = β0 = 20, βM OS = 1 mA/V2 , VT = 1 V, CE = 1 µF.



                                                                                                          Vcc
                                                  Vg
                                                                                                   Rc
                                                                 Rb                                           Vo



                                                                        Ce
                                                                                                   Re



                                                                               Fig. 1
                            Prova scritta di Fondamenti di Elettronica Analogica
                                               15 febbraio 2017
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
domande:

    1. Determinare la regione di funzionamento del transistore e dimensionare il resistore R in modo tale
       da polarizzare il transistore ad una corrente di base IB = 1 µA. Calcolare inoltre tutte le tensioni
       e correnti nel circuito (8 punti).

    2. Disegnare il circuito equivalente per piccoli segnali dello schema in figura, calcolare i parametri
       diﬀerenziali del transistore e determinare l’espressione della funzione di trasferimento Io (s)/Ii (s)
       (11 punti).

    3. Disegnare il diagramma di Bode del modulo di Io (s)/Ii (s) e dimensionare il valore di L in modo
       tale che la frequenza di taglio del circuito valga f−3dB = 100 MHz. (4 punti)

    4. Determinare l’espressione del guadagno di tensione Vo (s)/Vi (s) e disegnarne il diagramma di Bode
       del modulo. (7 punti)

Valori dei parametri:
VCC = 5 V, VEE = −5 V, βF = 40, Vth = 0.025 V, IS = 10−14 A, RL = 300 Ω, C = 1 nF.


                                                                           Vcc


                                                                                     L            Io
                                                                                                              RL
                                                                                Vo
                                                                               Ve C
                                                                                                         Vi
                                                                    R                             Ii

                                                                                    Vee
                                                                           FIGURA 1
                            Prova scritta di Fondamenti di Elettronica Analogica
                                               21 giugno 2017
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

In riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare il punto di lavoro del transistore, i valori statici di tutte le tensioni e correnti e la
       potenza statica dissipata dal circuito. (10 punti)

    2. Disegnare il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali.
       (punti 2)

    3. Determinare l’espressione delle funzioni di trasferimento VE (s)/Ii (s) e VC (s)/Ii (s). (12 punti)

    4. Nella condizione LE (β0 + 1) = LC β0 , tracciare l’andamento del diagramma di Bode del modulo di
       (VE − VC ) /Ii e di (VE + VC ) /Ii identificando la frequenza di poli e zeri. (6 punti)



                                                  Vcc

                                                                 VD                                        LE

                                                                                                                  VE

                                                                                                                  VC
                                            Ii
                                                                        R                                   LC


IS,bjt = IS,diodo = IS = 10−15 A, Vth = 0.026 V, βF = 80, VCC = 4 V, Ii,0 = 0, R = 50 kΩ, LC = 7 mH.
                            Prova scritta di Fondamenti di Elettronica Analogica
                                                13 luglio 2017
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

In riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Determinare il punto di lavoro del circuito, ergo i valori statici di tutte le tensioni e correnti nel
       circuito. (12 punti)

    2. Disegnare il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali.
       (punti 3)

    3. Calcolare il valore a centro banda del guadagno di tensione vo /vi del circuito. (13 punti)

    4. Indicare qualitativamente il tipo di comportamento in frequenza che ha la funzione di trasferimento
       VO (s)/Vi (s). (2 punti)



                                                                                                                         Vcc

                                                                                      R3                        R5

                                    Vi
                                                                                    T1                          T2
                                                   C
                                                                                                                       Vo
                                                     R1                               R2
                                                                                                                R4



IS = 10−15 A, Vth = 0.026 V, βF = 50, VCC = 5 V, R1 = 130 kΩ, R2 = R5 = 1 kΩ, R3 = 850 Ω,
R4 = 2 kΩ.
                            Prova scritta di Fondamenti di Elettronica Analogica
                                              14 settembre 2017
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

In riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
parametri:

    1. Tenendo conto dell’effetto Early per il BJT, determinare il valore della tensione di riferimento Vref
       che consente di avere in uscita la tensione VO = 5 V. (12 punti)

    2. Disegnare il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali.
       (punti 3)

    3. Trovare la matrice ammettenze del blocco circuitale a valle del condensatore C. (9 punti)

    4. Indicare come é possibile utilizzare la matrice trovata al punto precedente per determinare la fun-
       zione di trasferimento VO (s)/Vi (s) del circuito. (4 punti)

    5. Indicare qualitativamente qual é il comportamento in frequenza della funzione di trasferimento
       trovata. (2 punti)



                                                                                           Vcc
                                                                 Vref


                                                                           C
                                                    R

                                                                           Vo                                 Rb
                                                  Vi
                                                                               Rc



VCC = 12 V, Vth = 25 mV, VT = 1 V, βM OS = 4 mA/V2 , RB = 120 kΩ, RC = 1 kΩ, R = 50 Ω, βF 0 = 70,
VA = 29 V, IS = 10−14 A.
                                        Prova scritta di Fondamenti di Elettronica
                                                      6 febbraio 2018
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, calcolare le correnti e tensioni di polarizzazione del transistore
       bipolare e del transistore MOSFET. (10 punti)

    2. Disegnare inoltre il circuito equivalente ai piccoli segnali e calcolare i parametri differenziali dei
       transistori. (4 punti)

    3. Calcolare la matrice ibrida |h| del circuito. (12 punti)

    4. Calcolare il guadagno di tensione AV = vo /vi . (4 punti)

R1 = 7.3 kΩ, R2 = 2.7 kΩ, R3 = 1 kΩ, R4 = R6 = R7 = 2 kΩ, R5 = 4 kΩ, R8 = 4 kΩ, VCC = 10 V,
Vth = 25 mV, IS,bjt = 10−15 A, βF = β0 = 100, βM OS = 2 mA/V2 , VT = −1 V.


                                                                                                             Vcc

                                                              R3                   R7
                                            R2
                                                                        Ve                                      Vg
                                     Vi
                                                              Vc                                                                  Vo
                                                        Vb
                                                                                   R6
                                            R1                                                                                      R8
                                                            R4
                                                                                    R5




                                                                               Fig. 1
                                        Prova scritta di Fondamenti di Elettronica
                                                       1 marzo 2018
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, calcolare la tensione di ingresso Vi che permette di polarizzare
       il circuito a VO = 3 V (tenere conto dell’effetto Early). (10 punti)

    2. Disegnare il circuito equivalente ai piccoli segnali e calcolare i parametri differenziali del transistore
       e del diodo. (4 punti)

    3. Calcolare il valore di tutte le capacitá da inserire nel circuito equivalente per tenere conto degli
       effetti reattivi legati alle giunzioni dei componenti attivi. (3 punti)

    4. Con riferimento al circuito ottenuto al punto precedente, trascurando l’effetto della capacitá CBC
       e l’effetto Early, calcolare la funzione di trasferimento AV (s) = VO /Vi . (8 punti)

    5. Disegnare in dettaglio il diagramma di Bode del modulo di AV (s) indicando il valore numerico di
       poli e zeri. (5 punti)

R = 1 kΩ, VCC = 5 V, Vth = 25 mV, IS,bjt = 10−14 A, βF 0 = 25, VA = 30 V, IS,d = 10−15 A,
τT = τF = 10−10 s, Cj0 = 0.1 pF, Φi = 1 V (tensione di built–in della giunzione pn).



                                                                                       Vcc

                                                                                         R
                                                                                               Vo
                                                                 Vi




                                                                               Fig. 1
                                        Prova scritta di Fondamenti di Elettronica
                                                      21 giugno 2018
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, trovare il punto di lavoro dei transitori, calcolando tutte le
       correnti e tensioni nel circuito. (12 punti)

    2. Disegnare il circuito equivalente ai piccoli segnali e calcolare i parametri differenziali dei transistori.
       (4 punti)

    3. Calcolare la matrice ammettenze per il circuito ottenuto. (7 punti)

    4. Calcolare il valore della funzione di trasferimento AV = vo /vi . (3 punti)

    5. Discutere in dettaglio quale sarebbe l’effetto di una variazione della resistenza R nel circuito in
       esame, in particolare per quanto riguarda il punto di lavoro e il guadagno. (4 punti)

R = 3 kΩ, RC = 10 kΩ, RE = 100 Ω, VEE = 5 V, Vi = 4.2 V, Vth = 25.6 mV, IS = 10−14 A,
βF = β0 = 100, VT = 1 V, βM OS = 2 mA/V2 .



                                                                                                            Vee
                                                                                                    Re
                                                                                                              Vi
                                                              R                          T1
                                                                                                            Vo
                                                  T2                               T3
                                                                                                      Rc



                                                                               Fig. 1
                                        Prova scritta di Fondamenti di Elettronica
                                                       16 luglio 2018
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, trovare la tensione di ingresso utile a polarizzare il circuito in
       modo che Vo = 2 V, tenendo conto dell’effetto Early. (8 punti)

    2. Disegnare il circuito equivalente ai piccoli segnali e calcolare i parametri differenziali del transistore.
       (4 punti)

    3. Trascurando l’effetto Early (rce ), calcolare la funzione di trasferimento AV (s) = Vo /Vi . (7 punti)

    4. Disegnare in dettaglio il diagramma di Bode di AV (s), calcolando i valori di poli e zeri e dei valori
       asintotici della funzione. (6 punti)

    5. Calcolare l’impedenza in ingresso del circuito e discuterne i valori a bassa e alta frequenza. (5
       punti)

RB = 100 kΩ, RC = 1 kΩ, RE = 100 Ω, Vth = 25 mV, IS = 10−14 A, βF = β0 = 50, VA = 30 V,
C = 1 nF.



                                                               Re
                                                  Vi                                                          Vo

                                                                                               C
                                                                        Rb                                    Rc



                                                                               Fig. 1
                                        Prova scritta di Fondamenti di Elettronica
                                                    20 settembre 2018
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1, trovare il punto di lavoro del circuito, calcolando tutte le
       tensioni e correnti. (6 punti)

    2. Disegnare il circuito equivalente ai piccoli segnali e calcolare i parametri differenziali dei componenti.
       (4 punti)

    3. Determinare la matrice impedenze del circuito in oggetto. (10 punti)

    4. Calcolare la funzione di trasferimento AV (s) = Vo /Vi . (4 punti)

    5. Disegnare in dettaglio il diagramma di Bode del modulo di AV (s), calcolando i valori di poli e zeri
       e dei valori asintotici della funzione. (6 punti)

RB = 100 kΩ, RC = 10 kΩ, Vth = 25 mV, IS,d = 10−15 A, IS,bjt = 10−14 A, βF = β0 = 50, C = 10 pF,
L = 10 nH.



                                                                                                         Vee

                                                                      D                                L


                                                  Vi
                                                                                                             Vo
                                                             C
                                                                    Rb                               Rc



                                                                               Fig. 1
                                        Prova scritta di Fondamenti di Elettronica
                                                      28 gennaio 2020
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .


    1. Con riferimento al circuito di Fig. 1 in cui il MOSFET ha dimensioni L × W , calcolare la tensione
       di ingresso Vi che permette di polarizzare il circuito a VO = 3 V (tenere conto dell’eﬀetto di
       modulazione di lunghezza di canale). (8 punti)

    2. Disegnare il circuito equivalente ai piccoli segnali e calcolare i parametri diﬀerenziali del transistore
       e del diodo. Inoltre, calcolare il valore di tutte le capacitá da inserire nel circuito equivalente per
       tenere conto degli eﬀetti reattivi legati ai componenti attivi. (7 punti)

    3. Con riferimento al circuito ottenuto al punto precedente, calcolare la matrice ammettenze dell’ampliﬁcatore.
       (12 punti)

    4. Calcolare la funzione di trasferimento AV (s) = VO /Vi ed indicare quanti poli e zeri ha. (3 punti)

R = 1 kΩ, VCC = 5 V, VT 0 = 0.5 V, β  = 300 µA/V2 , COX = 50 fF/µm2 , γ = 0, λ = 0.04 V−1 ,
L = 0.25 µm, W = 0.6 µm, IS = 10−15 A, Vth = 25 mV, τT = 10−10 s.



                                                                                       Vcc

                                                                                         R
                                                                                               Vo
                                                                 Vi




                                                                               Fig. 1
                                        Prova scritta di Fondamenti di Elettronica
                                                     18 Febbraio 2020
Nome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .

Punti Assegnati: . . . . . . /. . . . . . /. . . . . . / . . . . . . / = . . . . . . . . .

   Con riferimento al circuito di Figura 1 ed ai valori dei parametri indicati si risponda ai seguenti
quesiti:

    1. Tenendo conto dell’eﬀetto Early e dell’eﬀetto di modulazione di lunghezza di canale, calcolare il
       valore della resistenza R tale che la tensione di uscita in condizioni statiche sia pari a VO = 2.5 V.
       Determinare inoltre tutte le altre correnti e tensioni nel circuito. (8 Punti)

    2. Calcolare i parametri diﬀerenziali dei transistori e disegnare il circuito equivalente ai piccoli segnali,
       includendo la capacitá di diﬀusione CBE del BJT. (5 Punti)

    3. Calcolare la matrice delle impedenze della sola parte di circuito che comprende il BJT e la resistenza
       R (escludendo quindi il MOSFET). (9 punti)

    4. Calcolare il guadagno di corrente AI = Isd /II dell’ampliﬁcatore (questa volta includendo nel calcolo
       il MOSFET) e disegnarne il diagramma di Bode, indicando il valore di poli e zeri. (8 Punti)

VCC = 5V, VG = 4V, VI = 1 V, Vth = 25 mV, VT M OS = −0.5 V, βM OS = 150µA/V2 , λ = 0.05 V−1 ,
IS = 10−14 A, βF 0 = β0 = 50, VA = 30V, τF = 2 ns.



                                                                                                     V CC
                                                          VG


                                                                                         VO
                                                             VI
                                                                                             VE

                                                                                         R


                                                                           FIGURA 1
Prova scritta di Fondamenti di Elettronica 24 giugno 2020 - parte di elettronica analogica

Nell’ipotesi che i due BJT siano identici, con riferimento al circuito di figura ed ai valori dei parametri
indicati si risponda ai seguenti quesiti:
1. Trascurando l'effetto Early, calcolare il valore della                                               Vcc
   resistenza RE2 tale che lo specchio di corrente alimenti
   l’utilizzatore U con una corrente pari a IO = 1 mA.                 RE1                   RE2
   Determinare inoltre tutte le correnti e tensioni nel circuito.
   Indicare infine qual è la tensione VO massima che consente
   il corretto funzionamento del circuito. (7 Punti)                    T1                   T2
2. Tenendo ora conto dell’effetto Early, calcolare i parametri                      Io       Vo
   differenziali dei transistori e disegnare il circuito equivalente
   ai piccoli segnali del solo specchio di corrente. (5 Punti)
3. Calcolare la matrice delle ammettenze del solo specchio di
                                                                       Ig                U
   corrente (escludendo quindi il generatore di corrente e
   l’utilizzatore U). (14 punti)
4. Calcolare la resistenza di uscita dello specchio di corrente.
   (4 punti)


VCC = 3 V, Vth = 25 mV, Ig = 2 mA, RE1 = 500 W, IS = 10-15 A, bF = b0 =30, VA = 40 V
                                                                                   V        o   i


Prova scritta di Fondamenti di Elettronica 15 luglio 2020 - parte di elettronica analogica
                                      4. Disegnare il diagramma di Bode del modulo della funzione di trasfe
                                                 valori di poli e zeri e del guadagno a centro banda. (6 punti)

Con riferimento al circuito di figura ed ai valori dei parametri indicati si risponda ai seguenti quesiti:
1. Tenendo conto dell'effetto Early per il BJT, determinare                                         Vcc
   il valore della tensione di riferimento VB che consente di
   avere in uscita la tensione Vo = 1.5 V. (10 Punti)                                  Vb
2. Tenendo ora conto dell’effetto Early, calcolare i parametri
   differenziali dei transistori e disegnare il circuito equivalente ai
   piccoli segnali del circuito. Considerare la tensione VB costante.
   (4 Punti)                                                                              C
3. Calcolare la matrice delle ammettenze del circuito, considerando
                                                                            R
   Vi e Vo i nodi di ingresso e di uscita del doppio bipolo.
   Considerare la tensione VB costante. (10 punti)                                        Vo                      Rg
                                                                          Vi
4. Trovare l’espressione del guadagno di tensione AV = Vo(s)/Vi(s)
   ed indicare quale tipo di risposta in frequenza ha il circuito.                            Rd
   (6 punti)


VCC = 7 V, Vth = 25 mV, RG = 500 kW, VCCR=D 12
                                             = 3V,kW,
                                                   Vth R
                                                       ==    mV,W,VTC==−1
                                                         26 50           1 µF
                                                                           V, βM OS = 2 mA/V2 , RG = 120 k
MOSFET: VT = -2 V, bMOS = 1 mA/V       2
                                     βF 0 = 30, VA = 30 V, IS = 10−14 A, C = 1 µF.
BJT: IS = 10-15 A, bF = b0 = 50, VA = 50 V
Prova scritta di Fondamenti di Elettronica 4 settembre 2020 - parte elettronica analogica

Con riferimento al circuito di figura ed ai valori dei parametri indicati si risponda ai seguenti quesiti:
1. Tenendo conto dell'effetto Early per il BJT, determinare
   il valore della resistenza RB che consente di avere in uscita          Vi                                 Vo
   la tensione Vo = 2.0 V. (8 Punti)
2. Tenendo ora conto dell’effetto Early, calcolare i parametri                                   C
   differenziali dei transistori e disegnare il circuito equivalente ai
   piccoli segnali dell’amplificatore. (4 Punti)
                                                                                 Rb                          Rc
3. Calcolare la matrice delle ammettenze del circuito, considerando
   Vi e Vo i nodi di ingresso e di uscita del doppio bipolo. (9 punti)
4. Trovare l’espressione del guadagno di tensione AV = Vo(s)/Vi(s)
   e disegnare in dettaglio il diagramma di Bode del modulo di AV, calcolando il valore di poli e zeri e i
   valori asintotici del guadagno. (9 punti)


Vi = 4.4 V, Vth = 25 mV, RC = 1 kW, C = 1 nF
BJT: IS = 10-14 A, bF0 = b0 = 50, VA = 30 V
Prova scritta di Fondamenti di Elettronica 15 settembre 2020 - parte elettronica analogica

Con riferimento al circuito di figura ed ai valori dei parametri indicati si risponda ai seguenti quesiti:
1. Tenendo conto dell'effetto Early per il BJT, trovare la tensione Vi
   che polarizza il circuito alla tensione Vo = 5.0 V. (12 Punti)                                            Vcc
2. Tenendo conto dell’effetto Early, calcolare i parametri differenziali
   dei transistori e disegnare il circuito equivalente ai piccoli segnali
   dell’amplificatore. (4 Punti)                                                                        R2
3. Calcolare la matrice ibrida h del circuito, considerando Vi e Vo i nodi di
                                                                                          R1                   Vo
   ingresso e di uscita del doppio bipolo. (10 punti)                            Vi
4. Trovare il valore numerico delle resistenze di ingresso e di uscita del
   circuito. (4 punti)
                                                                                               R3
VCC = 10 V, Vth = 25 mV, R1 = 10 k, R2 = 6 k, R3 = 300 ,
BJT: IS = 10-14 A, F0 = 0 = 30, VA = 30 V
Schema circuitale del
tema d'esame "abbozzato"
