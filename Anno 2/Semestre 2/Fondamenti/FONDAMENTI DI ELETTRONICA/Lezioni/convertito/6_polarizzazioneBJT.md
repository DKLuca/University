---
fonte: "6_polarizzazioneBJT.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Polarizzazione del BJT

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                                               Polarizzazione del BJT
           Click
               Click     totoedit
                Polarizzazione   edit
                    Polarizzazione     Masterdel
                                          Master del    title
                                                     transistor
                                                           title
                                                       transistor   style
                                                                      style
      Per polarizzare il BJT abbiamo bisogno di generatori di tensione e resistenze
 rizzare il transistor
  Polarizzare           vuolvuol
               il transistor diredire
                                    scegliere  il punto di lavoro,   ovvero      IBQI,BQ
                                                                                       V,BEQ , ICQ  e VeCEQ . .
    à Definizione       del punto      discegliere
                                           lavoro:ilQpunto
                                                        ≡ (VdiBE,lavoro,
                                                                   V   , I
                                                                    CE B C
                                                                          ovvero
                                                                             , I )        VBEQ   , ICQ   VCEQ
meCome
    primaprima
            cosacosa
                   eliminiamo  l’alimentatore
                       eliminiamo                 VBB.VEsaminiamo
                                     l’alimentatore    BB . Esaminiamoil seguente
                                                                           il seguente circuito:
                                                                                          circuito:




 ansistor
 tor      in questo esempio lavora  nella
                                      zonazona  attiva, a patto  di scegliere in maniera opportunaCCV,CCR,BReB eRCRC
  • inTramite
       questo  esempio  lavora
                la tensione  di nella       attiva,
                                alimentazione       Va patto
                                                         e lediresistenze
                                                              CC
                                                                scegliere  inRmaniera
                                                                                 e R opportuna
                                                                                       riesco ad V
                                                                                          B      applicare
                                                                                                 C
       tensione alle giunzioni BE e BC
  •  BJT componente non lineare à per determinare il punto di lavoro posso procedere
     per via grafica: V
 È bene             VCC! CC se si vuole la massima “dinamica” dell’amplificatore
        scegliere VCEQ
ene scegliere           se
  à maglia VdiCEQingresso
                  !      2 si vuole la massima
                           definisce   VBE e IB “dinamica”
                                                (incrocio tradell’amplificatore
                                                              retta di carico e caratteristica del BJT)
                           2
   à maglia
   Nell’ipotesi  didiconoscere
         Nell’ipotesi uscita  miβ definisce
                       di conoscere            VCE
                                    βF (di fatto     e IC (incrocio
                                                 significa misurarlotra
                                                                     perretta
                                                                         l’esemplare
                                                                              di caricoche stiamo utilizzando),
                                                                                         e caratteristica del BJT)
                                 F (di fatto significa misurarlo per l’esemplare che stiamo utilizzando),
         questa procedura ci consente di progettare il circuito
                                  Uso del modello di Ebers-Moll
    Il metodo grafico è quantitativamente poco pratico
    à Uso il modello di Ebers-Moll per trovare il punto di lavoro: Q ≡ (VBE, VCE, IB, IC)
    à Sostituisco il BJT con il circuito elettrico del modello (Hp. semplificativa: no effetto Early)

                                                          Vcc

                                                            Rc       𝐼! = 𝛽" 𝐼#$ − 𝛽% 𝐼#&
                                        Vbe         Ibc
                                                                        𝐼$ = 𝐼! + 𝐼#$
                                              Ibe            It         𝐼& = 𝐼! − 𝐼#&

                                                                        𝐼# = 𝐼#& + 𝐼#$


•     In regione normale il modello si semplifica à IBC = 0
                   𝑉#$
       𝐼! = 𝐼" 𝑒𝑥𝑝             es.: VCC=5 V; VBE=0.7 V; IS=10-15 A; bF=100; RC=1 kW
                   𝑉%&
             𝐼!
       𝐼# =                    à IC=1.45 mA; IB=14.5 µA; VCE=VCC-RCIC=3.55 V > VCE,SAT
            𝛽'
                                                                                            OK !
                                             Equazioni non lineari
Il modello di Ebers-Moll è un modello non lineare. Effetto Early complica le equazioni.
Es.:

                                                   Vcc

                                                    Rc      𝐼! = 𝛽" 𝐼#$ − 𝛽% 𝐼#&
                                 Vbe         Ibc
                                                               𝐼$ = 𝐼! + 𝐼#$
                                       Ibe           It        𝐼& = 𝐼! − 𝐼#&

                                                               𝐼# = 𝐼#& + 𝐼#$


              𝑉#$         𝑉!$
𝐼! = 𝐼" 𝑒𝑥𝑝          1+                 Sistema 2 equazioni in 2 incognite
              𝑉%&          𝑉(
                                        à in questo caso siamo fortunati, esiste ancora
𝑉!$ = 𝑉!! − 𝑅! 𝐼!                          la soluzione analitica


Spesso però non c’è soluzione analitica!
à Metodo di Newton, approssimazione successive
                      Trans-caratteristiche del circuito
Qual è il legame tra tensione di ingresso e tensione di uscita?
Il circuito può essere risolto con il modello di Ebers-Moll includendo la tensione VBE
come variabile di ingresso


                                          𝑉#$
                              𝐼! = 𝐼" 𝑒𝑥𝑝
                                          𝑉%&
                                                                  𝑉#$
                              𝑉!$ = 𝑉!! − 𝑅! 𝐼! = 𝑉!! − 𝑅! 𝐼" 𝑒𝑥𝑝
                                                                  𝑉%&
                               Vce

                                Vcc                           Fino a quando posso considerare
                                                              il BJT in regione attiva?
                                                    SATURO
                                      Reg. ATTIVA




                                                              à VCE,SAT criterio per valutare
                                                                saturazione


                          Vce,sat

                                                             Vbe
                                        Applicazioni del circuito
                                                                  Vce
                          •   A VBE bassa risponde con VCE alta
                                                                   Vcc
                              (BJT OFF)
                          •   A VBE alta risponde con VCE bassa                             SATURO




                                                                         Reg. ATTIVA
                              (BJT ON)
                                Applicazioni digitali:
                               à Porta logica NOT
                                                             Vce,sat
                                    (INVERTER)
                                                                                                     Vbe


                                                                  Vce

                                                                   Vcc

                                                                                           DVCE > DVBE
                                                                                       Q
                                                              t                            se la pendenza
                                                                                               è alta !!

                                                             Vce,sat
Applicazioni analogici:
                                                                                                      Vbe
    à AMPLIFICATORE
                                                                                       t
                                           Modello a soglia del BJT
Il modello di Ebers-Moll è un modello non lineare
                                                                Approssimazione lineare
à Spesso non c’è soluzione analitica del circuito
                                                                à MODELLO A SOGLIA
à Soluzione numerica onerosa

 • Sostituisco le equazioni non lineari con equazioni lineari
 • Il funzionamento del BJT è regolato dalla giunzione BE
 • La giunzione BE trattata come in diodo: ON/OFF
 BE OFF à BJT OFF à correnti nulle (non considero la regione attiva inversa)
 BE ON à VBE = VBE,g se IB, IC > 0
 VBE,g tensione soglia di accensione del BJT


 VBE < VBE,g à BJT OFF à IB, IC, IE = 0
 VBE = VBE,g à BJT ON:
 1. Regione attiva à             𝐼! = 𝛽' 𝐼#
 2. Regione di saturazione à VCE = VCE,SAT (la variazione di VCE in saturazione è
      molto limitata; caratteristiche di uscita molto ripide)
                              Esempio: circuito con BJT
            Vcc = 3 V
                             Hp.: Regione normale; no effetto Early

                             𝑉)* = 𝑉#$ + 𝑅# 𝐼#
                            𝑉+,- = 𝑉!! − 𝑅! 𝐼!                  𝛽" 𝑉/0 𝛽" 𝑅#
                                          𝑉#$       𝐼& = 𝐼. 𝑒𝑥𝑝       −      𝐼
                                                                 𝑉!1    𝑉!1 &
                             𝐼! = 𝐼" 𝑒𝑥𝑝
                                          𝑉%&     - NO SOLUZIONE ANALITICA
                                 𝐼! = 𝛽' 𝐼#       - soluzione numerica
                                                  - uso modello a soglia

1. VBE < VBE,g BJT OFF à IB, IC, IE = 0 à 𝑉+,- = 𝑉!! ; 𝑉)* = 𝑉#$ < VBE,g

                                                                  𝑉/0 − 𝑉#$,4
                                                             𝐼# =
                                                                      𝑅#
2. BJT ON in regione attiva à VBE = VBE,g; 𝐼! = 𝛽' 𝐼# à
                                                             𝑉567 = 𝑉&& − 𝑅& 𝛽" 𝐼#

                                                                    𝑉/0 − 𝑉#$,4
                                                               𝐼# =
3. BJT ON saturo à VBE = VBE,g; VCE = VCE,SAT = VOUT à                  𝑅#
                                                                    𝑉&& − 𝑉&$,89!
                                                               𝐼& =
                                                                         𝑅&
                Esempio: caratteristica statica
Vcc = 3 V
                    1. BJT OFF à 𝑉+,- = 𝑉!! ; 𝑉)* < VBE,g


                    VIN ≥ VBE,g
                    2. BJT ON in regione attiva
                                                                 𝑉/0 − 𝑉#$,4
                                           𝑉567 = 𝑉&& − 𝑅& 𝛽"
                                                                     𝑅#

                    3. BJT ON saturo à VOUT = VCE,SAT


                                  Applicazioni digitali: Porta logica NOT
 BJT OFF        regione attiva        (INVERTER) à BJT OFF; saturazione
                                           prima porta logica con transistor:
                                           RTL (resistor-transistor logic)
                        saturazione
                                  Applicazioni analogiche: AMPLIFICATORE
                                  à regione normale
        VBE,g
                        Scelta del punto di lavoro
Vcc = 3 V          Applicazioni digitali: INVERTER à BJT OFF; saturazione

                   Applicazioni analogiche: AMPLIFICATORE à regione normale


                   SCELTA DEL PUNTO DI LAVORO FONDAMENTALE !!
                   à anche la stabilità del punto di lavoro è importante
                   à non deve cambiare con il tempo:
                             la sensibilità alla variabilità dei parametri con
                                         invecchiamento, temperatura, sostituzione
                                         dei componenti, etc. vanno limitate


                                         TECNICHE DI STABILIZZAZIONE
                                         DEL PUNTO DI LAVORO !!
 BJT OFF        regione attiva           •   utilizzo di generatori di corrente
                                             per fissare la corrente
                                         •   utilizzo di una resistenza
                        saturazione          sull’emettitore (vedremo in seguito)



        VBE,g
  ./ ....../ ....../ ....../ ......= .........
Con riferimento         per      VBE,ondimentre
                         al circuito                        è1indicato           il sotto
                                                                                     valoreindicati
                                                                                                  di IS cerchiamo                   una soluzione             attraverso
                                                                                                                                                                     seguentiil
        Con riferimento            al circuitoFigura
                                                  Soluzione
                                                  di  Figura    e1ai   e valori
                                                                          aidel
                                                                             valori
                                                                     Soluzione       compito
                                                                                        sotto
                                                                                        del       indicati
                                                                                               compito    di deidei
                                                                                                               di    parametri,
                                                                                                                       parametri, si
                                                                                                                 Fondamenti
                                                                                                                     Fondamenti                risponda
                                                                                                                                       Esercizio di
                                                                                                                                           sidirisponda
                                                                                                                                                 Elettronica  alleseguenti
                                                                                                                                                      Elettronica
                                                                                                                                                            alle
ra
ande:1 e ai valori sottoche indicati
                                  tiene conto          della natura
                                             dei parametri,                      esponenziale
                                                                        si risponda        alle seguenti  della        caratteristica             IC ° VBE . Un insi
   domande:                                                                                     14 14 Giugno
                                                                                                           Giugno          2004
                                                                                                                            2004
                        indipendenti è dato da:
   Determinare          il In
                            valore           1. In regime
                                         stazionario           stazionario
                                                             delle      tensioni il valore   della tensione
                                                                                        e ecorrenti               di, ingresso     è chiaramente     ininfluente     sul funziona
       1. Determinare1.         ilregime
                                     valore   stazionario
                                             stazionario          delle
                                                                  il        tensioni
                                                                       valore      della      correntiIR1,0
                                                                                             tensione       IdiR1,0ingressoR2,0,, II
                                                                                                                      , IIR2,0      è        = IIE,0
                                                                                                                                              =
                                                                                                                                       chiaramente
                                                                                                                                      RL,0
                                                                                                                                      RL,0              (Q1ininfluente
                                                                                                                                                    E,0(Q    1),),IB,0
                                                                                                                                                                    IB,0(Q(Q   1 ),
                                                                                                                                                                            1 ), su
o delle tensioni e correnti IR1,0del              , IR2,0    , IRL,0
                                                       circuito           = IE,0
                                                                  in quanto           (Q1 ), èIB,0
                                                                                  l’ingresso           (Q1 ),
                                                                                                   disaccoppiato         dal circuito tramite il condensatore. Inoltre,
   I (Q      1 ),(Q
           IC,0     1 ), (Q
                  VB,0   Vdel  1 ),     ), V= Vin
                                  (QV12,0        =    V(Q
                                                        E,01(Q) corrispondenti
                                                                 1 )l’ingresso
                                                                       corrispondenti         a aV1,0
                                                                                                    V1,0= =1.25 1.25    VVPoichè
                                                                                                                            ecircuito
                                                                                                                              e VV11 =nonVviene  ==specificato
                                                                                                                                                     2.5 V.
                                                                                                                                                     2.5  ilV.condensatore
                                                                                                                                                                (6(6   punti).
                                                                                                                                                                     punti).
Q1C,0) corrispondenti          a circuito
                             B,0
                                   V1,0 = 2,01.25 E,0quanto
                                                 parametri
                                                     V   e V1del = circuito
                                                                       V1,0 = e2.5     èV.
                                                                                     del  disaccoppiato
                                                                                          transistore
                                                                                               (6 punti).sono         dal
                                                                                                                  noti.                      tramite
                                                                                                                                            1,0
                                                                                                                                            1,0                    alcun   valore d
                            parametri delpercircuito   VBE,on mentre e del
                                                                         VCC       ° R1 (I
                                                                             ètransistore
                                                                                indicato     il B   +
                                                                                                valore
                                                                                                    sonoIdi   )S cerchiamo
                                                                                                         R2Inoti.    = Poichè
                                                                                                                             VBE   una+          IB (Ø
                                                                                                                                         soluzione
                                                                                                                                        nonRLviene          + 1) il metodo
                                                                                                                                                      attraverso
                                                                                                                                                        Fspecificato         alcu it
   Valori   dei
 ri dei parametri:parametri:                     che tiene conto della natura esponenziale della caratteristica IC ° VBE . Un insieme di equ
   VCC    =V,2.5            per     V
                  V,=ØF50,=I50,=IS10=°14
                                      BE,on    mentre
                                                   °14 A, è
                                               10indipendenti R  indicato
                                                                     =   1000
                                                                     è dato       il valore
                                                                               da:≠,   R= 2 =
                                                                                                   di I≠,
                                                                                                 1000    S cerchiamo
                                                                                                               RL=    =100 100VBE ≠,una+thR
                                                                                                                                       V     =     B (ØFV,+
                                                                                                                                            soluzione
                                                                                                                                               LI0.025         CC1)
                                                                                                                                                            attraverso
                                                                                                                                                                  1 ==2 2pF.
                                                                                                                                                                                il m
  =   2.5
R1 = 1000 ≠,    Ø F R2 = 1000           ≠, R        A,
                                               L = 100
                                                         R     = 1 1000      ≠,     R
                                                            1≠, Vth = 0.0252V, C1 = 2 pF.     1000     ≠,I  R        =           ≠,    V     =    0.025   V,                 pF.
                            che Stiene       conto      della      natura esponenziale
                                                                                    V                     della
                                                                                                          R2 L
                                                                                                                       caratteristica    th
                                                                                                                                                RI2C ° VBE .1 Un insie
                  VCC indipendentiSoluzione        è dato da: del             Vcompito
                                                                              VCB  CC> 0 à ILdi
                                                                                       CC
                                                                                                         BJT Fondamenti
                                                                                                                   E’ IN REGIONE
                                                                                                                                         µ di Elettronica
                                                                                                                                            ØF IB
                                                                                                                                                     ∂
                                                                                       VCC14  ° R1Giugno
                                                                                                    (IBV+    IR2 ) ==    2004   th ln
                                                                                                                             VVBE    + RL IB (ØF + 1)
                                                                              NORMALE                 àBE  correnti           proporzionali
                                                                                                                              VBE + RL IBI(Ø
                       𝐼%;                                              R                                               =
                                                                                                                                                 S F + 1)
                                       𝐼&                                  1                                   IR2
                                                                                                                                           R2
        R1         1. In      regime       stazionario
                        Elaborando queste equazioni            il Rvalore
                                                                       1        della     tensione
                                                                                 otteniamo:               di ingresso è chiaramente   µ         ∂        ininfluente sul
                                                                          V  CC     °   R  1
                                                                                            Q(I 1B + IR2V) == V                 BE     + ØFRILB IB (ØF + 1)
                                                                                                                              Vth ln tramite il condensatore.
                        del
                          Q1circuito in quanto           V1 l’ingresso è disaccoppiato  Q1                     BEdal circuito             IS
                                                   V                                                                          V        +
                                                                                                                                       R   RL IB (ØF + 1)
                        parametri del Elaborando circuito
                                                      1          e   del    transistore
                                                                                 = VBEotteniamo: sono    Inoti.
                                                                                               + RL IBR2(ØF + 1) +   = Poichè
                                                                                                                           V    BE
                                                                                                                                      non1 viene
                                                                                                                                            (VR        specificato alcun
                                                                                                                                                BE + RL IB (ØF + 1))
                                                                                                                              2
                                                      VV2CC °queste   R1 IBequazioni
                                                                                                                         V2 unaRµsoluzione
                        per VBE,on mentre è indicato il valore di IS cerchiamo                                                          2        2
                                                                                                                                                     ∂ attraverso il m
                                                                C1                                                                          Ø    I
   C1               𝐼#che tiene conto della natura                        VCCesponenziale
                                                                                ° R1 IB = VBE +della    VRL IB (Ø   caratteristica
                                                                                                                    µ=F + 1) V
                                                                                                                                     R 1
                                                                                                                                 + ln (VBE    FI+BR
                                                                                                                                                 C °L IV  (ØF .+∂
                                                                                                                                                        BBE         Un
                                                                                                                                                                    1)) insiem
                                                            C1                           V CC 2  R        BE               R    R
                                                                                                                                th
                                                                                                                              1 2 2  R
                                                                                                                                              IS (Ø + 1)
       𝐼%:              indipendenti è dato da: VBE = R2                                              R°L IB µ                          +R
                       R2             RL             𝐼$                                 R1 + R    VCC2 R2               R1R+  1 R2R2
                                                                                                                                                 L F∂
                            Elaborando queste equazioni otteniamo:                    VBE =
                                                                                      R                       ° IB                     + RL (ØF + 1)
                                                                                         2       R1R  + LR2               R1 + R2
                        Sostituendo i valori dei parametri ed esplicitando rispetto ad IB si ha infine:
                                                 Sostituendo i valori dei parametri ed esplicitando rispetto ad IB si ha infine:
                                                                        VCC     ° R1 (IB1+ IR2 ) 1.25V
                                                                              FIGURA                              = +V1)            +RR1 L(VIB (Ø+   F + RL1)IB (ØF + 1))
                                                                          1 IB = VBE + RL IB (Ø
                                                         VCC ° R                                                             BE+
                                                                                                                   F1.25V °   ° VVBE  BE        BE
              FIGURA 1                                                                               IB = IB =             VBE≠≠+RR      2 L IB (ØF + 1)
                                                                          FIGURA             1         I          =    5600
                                                                                                                          5600
   ———————————————-       Sistema nonRisolvendo     lineare questa di due                                R2         µ                       R2                    ∂
                                                                             equazioneVCC   iterativamente
                                                                                                  R                con l’eq.
                                                                                                                           R    R3 2otteniamo:
        Il circuito equivalente
                        Risolvendo
                          equazioni        perinpiccolo
                                              questa          segnaleVBE
                                                   due equazione
                                                            incognite       deliterativamente
                                                                                   circuito
                                                                                    =            compreso
                                                                                                     2
                                                                                                         ° Icon    nel riquadro
                                                                                                                              1
                                                                                                                B l’eq. 3 otteniamo:
                                                                                                                                      µ+  tratteggiato
                                                                                                                                             R     ∂
                                                                                                                                                 L (ØF + 1)
                                                                                                                                                              di Figura 2
                                                                                                                                         Ø    I
 —————————————-
segnale
   presenta deli seguenti
                  circuitoà compreso
                                 valori    dei nel
                                 approssimazioni      riquadro
                                                parametri:          z11tratteggiato
                                                                 successive= 1100 ≠,     R1diz+21Figura
                                                                                                   R
                                                                                                   =V   BEIB2(µA)
                                                                                                      21000      ≠=degliRV1th+
                                                                                                                            VBEln
                                                                                                                                   R2
                                                                                                                               elementi
                                                                                                                                  (V ) I
                                                                                                                                           F    B
                                                                                                                                               della matrice Z. Con
 l riferimento
ri:circuito
     z11 = 1100 equivalente
                   ai≠,valori21 =     per
                                      1000piccolo
                                    sotto
                           zSostituendo       ≠ idegli
                                            indicati     segnale
                                                    valori elementi
                                                         dei   parametri del   circuito
                                                                           della
                                                               dei parametri               edcompreso
                                                                                   simatrice
                                                                                       risponda    Z.aiCon       -nel riquadro
                                                                                                          seguenti
                                                                                                 esplicitando               quesiti.      tratteggiato
                                                                                                                                             S                  di Figura 2
                                                                                                      IB (µA) VBE (V ) IB si ha infine:
                                                                                                                           rispetto
                                                                                                                                 0         ad
 . / . . . . . . / . Sostituendo
                     . . . . . / . . . . . . / i. .valori
                                                    . . . . = .dei
                                                                . . . .parametri
                                                                       ....      ed esplicitando
                                                                                              IS rispetto ad IB si ha infine:
                                                                                                                       R1
                                                                                            VCC ° R1 IB = VBE + RL IB (ØF + 1) +                            (VBE +
Con    riferimento       al circuito       di Figura      1tensione
                                                             e1aie valori    sotto    indicati       dei   parametri,          si  risponda       alleseguenti
                                                                                                                                                         Rseguenti
In   regime
        Con
 Elaborando
ra
ande:
                 stazionario
               riferimento
                     queste     al  il valore
                                    circuito
                                  equazioni      della
                                                di    Esercizio: soluzione numerica
                                                    Figura
                                                   otteniamo:      ai   di
                                                                      valori
     1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
   domande:
                                                                            ingresso
                                                                                sotto      è chiaramente
                                                                                         indicati      dei
                                                                                                      1.25V          ininfluente
                                                                                                             parametri,
                                                                                                                    °
                                                                                           IB =tramite il Vcondensatore.
                                                                                                                         V BE
                                                                                                                               si         sul
                                                                                                                                   risponda
                                                                                                                                            µ
                                                                                                                                               funzionamento
                                                                                                                                                 alle       2

del    circuito in quanto l’ingresso è disaccoppiato dal circuito                                                       CC R2                  Inoltre,
                                                                                                                                                R 1 R2
                                                                                                                                                            +tutti
                                                                                                                                                               RL (ØiF
                                                                                                        VBE  5600=
                                                                                                R1 viene specificato    ≠          °   I
                                                                                                                     R1 + R2 alcunRvalore
                                                                                                                                         B
                                                                                                                                                1 + R2 definito
parametri del circuito                e del   transistore
                                                   =          + sono    noti.
                                                                          (Ø     Poichè
                                                                                  +   1)   +   non    (V         +             (Ø     +    1))
    Determinare
       1. Determinare   il valore
                            V        °
                              il valore
                              CC       stazionario
                                        R    I        V
                                           1stazionario
                                               B         delle
                                                        BE       tensioni
                                                             delleR   I B Fe e
                                                                    Ltensioni
                                                                 Sostituendo      correnti
                                                                                   i correnti
                                                                                      valori      IR1,0
                                                                                                dei IR1,0 , , IIR2,0
                                                                                                          BE
                                                                                                      parametri  R2,0,, ed
                                                                                                                     R   L I B =
                                                                                                                         IIRL,0    =
                                                                                                                             esplicitando    (Qrispetto
                                                                                                                                         E,0(Q
                                                                                                                                   F IIE,0      11),),IB,0
                                                                                                                                                        IB,0(Q(Q
                                                                                                                                                             ad ),1B),s(
per
o delle            Risolvendo
                   mentre
            tensioni
       VBE,on            e correnti     questa
                                è indicato          equazione
                                         IR1,0 , ilIR2,0
                                                     valore    di I=S iterativamente
                                                         , IRL,0       Icerchiamo
                                                                         E,0 (Q1 ), IB,0   una      2con
                                                                                                     ), l’eq.attraverso
                                                                                              (Q1soluzione
                                                                                                R                     3 otteniamo:
                                                                                                                           RL,0
                                                                                                                                         il metodo iterativo   1I
    IC,0 (Q  1 ),(Q
           IC,0     1 ), (Q
                  VB,0       1 ),
                          VB,0        ), V=
                                (QV12,0    2,0V=E,0V(Q
                                                     E,01(Q) corrispondenti
                                                             1 ) corrispondenti      a aV1,0
                                                                                           V1,0==    1.25
                                                                                                       1.25VV ee VV11 = V1,0     1,0 == 2.52.5 V.
                                                                                                                                                V.(6(6punti).
                                                                                                                                                           punti).
Q1 ) corrispondenti
che     tiene conto della    a V1,0     = 1.25esponenziale
                                     natura        V e V1 = V1,0della  = 2.5caratteristica
                                                                               µV. (6 punti). IC ° VBE . ∂                    Un insieme           di
                                                                                                                                          1.25V ° VBE    equazioni
                                                        VCC R2                       R1 R2                                      IB =
indipendenti
 riValori             è dato da: VBE =
            dei parametri:                                            ° IB                          + R (Ø + 1)                               5600 ≠                   (
     dei parametri:                                    R1 + R2                    R1 +IR      B2(µA) L VFBE (V )
          =V,2.5  V, ØF50,=I50,=IS10=°14     10 A, R  A, R      =Risolvendo
                                                                   1000   ≠,        =1000
                                                                                        1000equazione
                                                                                               ≠,≠,-RRLL==100    100 ≠,
                                                                                                                       0≠, VVth
                                                                                                                              th == 0.025      V,        ==2 2pF.
                                                °14
R =V1CC
      2.5
      =  1000     F =
                Ø≠,  R     = 1000
                                S ≠, RL =           100 1≠, =1V1000=   ≠,  R2RV,
                                                                       0.025     =
                                                                                 2questa
                                                                                    C      =  2  pF.            iterativamente        0.025    V,CC
                                                                                                                                        con l’eq.               pF.
                                                                                                                                                     31 1otteniamo:
 Sostituendo i valori dei parametri ed esplicitando
                        2                                       th
                                                                           VCC       rispetto
                                                                                       1             ad    I B    si ha     infine:
                  VCC                                                   VCC                   223.2               0.6935
                                          VCC ° R1 (IB + IR2 ) 1.25V          = VBE     ° V+      RL IB (ØF0.6733
                                                                                              99.37                 + 1) IB (µA) VBE (V )                          (1)
                                                                                               BE                                     -              0
                        𝐼%;                                        IB =              V        +   R     I    (Ø      +    1)                                           (
                                     𝐼&                           R  I        =   5600 BE   ≠102.98   L   B      F0.6742           223.2         0.6935            (2)
         R1                                                   R1 1 R2              Q1 3102.82         R
 Risolvendo questa               equazione        iterativamente          con     l’eq.        µ
                                                                                               otteniamo:
                                                                                                         2
                                                                                                              ∂ 0.6741 99.37                     0.6733
                          Q1                          V 1                       Q                  ØF IB                          102.98         0.6742
                                                V1                  VBE = 1Vth ln                                                 102.82         0.6741
                                                                                                                                                                   (3)
                                                                                                      IS V2
                                                    V2              IB (µA) VBE (V )                           V2
Elaborando queste  da    cui   otteniamo           infine:
                                 equazioni otteniamo:        C1
    C1              𝐼 #                                          da cui- otteniamo 0infine:
                                                        C1            223.2
       𝐼%:                                                               IC R=2 0.6935   ØFRR  I1BL ' 5.141           mA
                       R2VCC °      RLR1 IB = VBE + RL I99.37         B F(Ø    +   1)   +
                                                                                      0.6733       (VBE + R       ICL IB  =(ØØFF+   IB1))' 5.141 mA                (4)
                                                                              R
                                                                         IE 2= 0.6742       R R
                                                                                         (ØFL2+ 1)IB '
                                                                     102.98                                       IE 5.244= (ØmA   F + 1)IB ' 5.244 mA
                                                                             µ                                             ∂
                                                       VCC R2 102.82      V       =
                                                                                  R   0.6741
                                                                                       R R      I     '    0.5244 V2 =    V    RL IE ' 0.5244 V
                                                                    °FIGURA            1
                                                                            2        1     2  L   E
                                          VBE =                         IB                      + RL (ØF V+ 1)= V + V ' 1.1985 V (5)
              FIGURA 1                                R1 + R2           VB R=      1 +V   R2 + V ' 1.1985          B
                                                                                                                                 VBE        2
                                                                    FIGURA 1                BE            2
   ———————————————-                                                                                              IR2 = VB /R2 ' 1.1985 mA
Sostituendo         i valori dei parametri ed esplicitando                        rispetto
                                                                                  = compreso      ad    I      si  ha infine:
                                                                                                         nel1.1985
                                                                        IR2              VB /R2 '        B
 da cui     otteniamo
        Il circuito           infine: per piccolo segnale del
                       equivalente                                         circuito                              IR1 =mA
                                                                                                                riquadro       (VCC ° VB )/R
                                                                                                                               tratteggiato              ' 1.3015
                                                                                                                                                  di1 Figura     2 m
 —————————————-
segnale
   presenta deli seguenti
                  circuito compreso
                               valori dei nel       riquadroz11
                                              parametri:            = 11001.25V
                                                                 tratteggiato
                                                                        IR1    ≠,=diz°   (V
                                                                                      21Figura
                                                                                          V=BE1000°          B )/R
                                                                                                     2 ≠Vdegli             ' 1.3015
                                                                                                                  IBelementi
                                                                                                                        1=     IR1della
                                                                                                                                     ° IR2  matrice
                                                                                                                                            mA ' 103 Z.  µA Con
 l riferimento
ri: circuito
      z11 = 1100equivalente
                   ai≠,            per
                                    1000piccolo
                           z21 =sotto
                        valori              ≠ degli
                                          indicati          = del
                                                     Isegnale
                                                       elementi
                                                      dei
                                                                 I    =
                                                                      Icircuito
                                                                        B si'
                                                                  ØFdella
                                                                   B
                                                            parametri           5.141
                                                                             matrice compreso
                                                                              risponda     mA
                                                                                              CC
                                                                                              aiCon
                                                                                                  seguenti        quesiti. tratteggiato di Figura 2 (
                                                                                                        nel riquadro                                               (6)
                                                      C
                                                                         I     5600      ≠ Z.
                                                                                  = I ° I ' 103 µA
                                                                    L’ultimo
                                                                           B valore, molto
                                                                                     R1 prossimo
                                                                                           R2    a quello calcolato in partenza (102
                                                . . .+
 . / . . . . . . / . . . . . . /I . . . .=. . /VBE   . .R
                                                        .=  . .(Ø. F. .+
                                                         L IB          . .1)
                                                                          ..
                                                                           (2)                     IS
                               R2
                                        R2
Con riferimento    al circuito  di Figura    ∂1 e ai valori sotto indicati dei parametri, si risponda alle seguenti
ra
     Con riferimento
   1 e ai valori sotto
ande:
 domande:
                   VBE
                        al circuito
                     Elaborando
                       indicati
                          = Vthdei
                                    µ
                                    di  Figura
                                 ln parametri,
                                       F
                                        IS
                                           B                          Esercizio: modello a soglia
                                                 1 e ai valoriotteniamo:
                                      queste equazioni
                                      Ø  I                     sotto indicati dei parametri, si risponda alle seguenti
                                                   si risponda alle seguenti
                                                                           (3)

uazioni otteniamo:il valore stazionario V                                                                     R1
  Determinare                                   R I =e Vcorrenti
                                        delle°tensioni
        1. Determinare il valore stazionarioCCdelle tensioni + RI I
                                                              1 B     e BE        I B (Ø
                                                                        correnti LR1,0          + ,1)
                                                                                       , , IFIR2,0     + =
                                                                                                   , IIRL,0  =(V  BE(Q
                                                                                                                IIE,0  +1),R
                                                                                                                      (Q   ),L    (Ø
                                                                                                                                B(Q
                                                                                                                              IIB,0
                                                                                                                             IB,0   (Q  1+
                                                                                                                                     1F), ),
 o delle tensioni e correnti IR1,0 , IR2,0 , IRL,0 = IE,0 (Q1 ), IB,0 (Q1 ),R1,0 R2,0 RL,0R2 E,0 1
  IC,0 (Q    1 ),(Q
           IC,0    1 ), (Q
                  VB,0    1 ),
                        VB,0      ), V=
                             (QV12,0      1 V(Q
                                         V=
                                      2,0R         ) corrispondenti
                                              E,01(Q 1 ) corrispondenti a aV1,0
                                                                            V1,0==1.25
                                                                                    1.25VV ee VV11 = V1,0       = 2.5
                                                                                                            1,0 =  2.5 V.
                                                                                                                        V.(6(6punti).
                                                                                                                                punti).
°QR1 )1 Icorrispondenti
         B = VBE + RL IBa  (ØV      =+
                                 + 1)
                              F 1,0   1.25E,0
                                            VBE
                                           (V  eV +1R=L IV (ØF=+2.5
                                                         B1,0    1)) V. (6 punti).(4)         µ                                  ∂
                                                  R2                                 VCC R2           R1 R2
riValori  dei parametri:µ
   dei parametri:                                  ∂ VBE =                 ° IB              + RL (ØF + 1)
  VCCBE=
   V2.5
            VCC R2
         =2.5 V,=ØF50,
                               R1 R2 °14
                     °=IIB50,=IS10
                                 =°14
                                    10+A, A,
                                          (ØFR
                                        RLR    + =
                                                 1) 1000  ≠, R=  R
                                                               2 =
                                                                    + R
                                                                  11000 ≠,        R
                                                                            RL==100
                                                                        2 (5)         +
                                                                                 1001≠, R
                                                                                     ≠, V
                                                                                        Vth2 = 0.025 V, C1 = 2 pF.
=       V,
R1 = 1000 ≠,
           RØ  +
             1 R22 = 1000 ≠,
              F  R        S  R   +
                               1 RLR         = 1 1000  ≠,  R     1000 ≠,
                                    2 = 100 ≠, Vth = 0.025 V, C1 = 2 pF.
                                           1                 2            R L             th = 0.025 V, C1 = 2 pF.
                      Sostituendo i valori dei parametri   V      ed esplicitando rispetto ad IB si ha infine:
i parametri ed  esplicitando rispetto ad IB si ha infine:V CCCC
              VCC
                          1.25V ° VBE                                       1.25V ° VBE
                            B =
                          𝐼I%;                                      IB(6)=
                             5600 ≠
                              𝐼&                  R                             5600 ≠
      R1                                       R1 1
 azione iterativamente con l’eq. 3 otteniamo:                Q1
                     Q1 Risolvendo     questa
                                          V 1 equazione  iterativamente
                                                           Q1              con l’eq. 3 otteniamo:
                                       V                             VBE = VVBE,g = 0.7 V
                    IB (µA) VBE (V ) 1                                           2
                                        V
                        -          0      2                          IB (µA) 2 VBE (V )
                                                                             V
                                              C                                𝐼# = 98.2
  C1             𝐼# 223.2 0.6935                1                        -            0 𝜇𝐴
                      99.37     0.6733      C1
     𝐼%:             102.98     0.6742                             RL 223.2 𝐼& =
                                                  soluzioneR2modello               0.6935
                                                                                     𝛽" 𝐼# = 4.91 𝑚𝐴
                   R102.82   RL0.6741
                     2                                   R2a soglia
                                                                  RL à99.37 𝐼 =
                                                                                $
                                                                                   0.6733
                                                                                     (𝛽" +1)𝐼# = 5.01 𝑚𝐴
                                                                                              102.98   0.6742
                                                                                                     𝑉 = 1.201 𝑉
                                                                                              102.82 # 0.6741
 e:                                                                            FIGURA 1
           FIGURA 1
          IC = ØF IB ' 5.141 mA
  ———————————————-                                    FIGURA 1                (7)
          IE = (Ø
      Il circuito       + 1)I
                      F da   cui
                   equivalente     5.244
                              B 'otteniamo
                                  per    mA infine:
                                       piccolo  segnale  del circuito compreso(8) nel riquadro tratteggiato di Figura 2
                                                 ß soluzione      numerica
—————————————-
segnale
  presentadel
          V    = RL IE compreso
               circuito
           2 i seguenti   ' 0.5244
                          valori  deiVnel riquadroz11
                                      parametri:    tratteggiato
                                                      = 1100 ≠, di z21Figura
                                                                       = 1000 (9)
                                                                               2 ≠ degli elementi della matrice Z. Con
l riferimento
  circuito
ri:          equivalente
    z11 =VB1100=ai≠,  z21+ =
                   Vvalori
                     BE      2per
                              1000
                           Vsotto  piccolo
                                         V segnale
                                     ≠ degli
                                   indicati
                               ' 1.1985      elementi
                                            dei      del  circuito
                                                        della
                                                 parametri      IC compreso
                                                             simatrice=Z.aiØCon
                                                               risponda           nel
                                                                                   ' riquadro
                                                                             seguenti
                                                                             (10)
                                                                             F IB     5.141
                                                                                       quesiti.
                                                                                             mA tratteggiato di Figura 2
