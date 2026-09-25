---
fonte: "2017_Testi_e_Soluzioni.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

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
                  Soluzione del compito di Fondamenti di Elettonica
                                   26 gennaio 2017
1. Ipotizziamo il BJT in regione normale, mentre il MOSFET chiaramente lavora in regime di satu-
   razione. A questo punto é facile impostare il sistema di equazioni che descrive il circuito:
                                               VBE
                                                   !         "
                                IC   = IS exp                                                         (1)
                                               Vth
                                       IC          βM OS
                                IB   =     = IDS =       (VGS − VT )2                                 (2)
                                       βF            2
                                VG   = VGS + IB RB + VBE + (βF + 1) IB RE                             (3)

   Il sistema é chiaramente non lineare e per ottenerne la soluzione bisogno ricorrere ad una soluzione
   iterativa. Per ció, Eq. (1) viene trasformata nella forma logaritmica, mentre Eq. (2) viene invertita,
   il che permette di calcolare VBE e VGS dalla corrente IC . Il sistema diventa:
                                                            IC
                                                                   !    "
                                            VBE    = Vth ln                                           (4)
                                                            IS
                                                                   #
                                                                  2IC
                                            VGS    = VT +                                             (5)
                                                               βF βM OS
                                                         VG − VGS − VBE
                                             IC    =         RB  βF +1
                                                                                                      (6)
                                                             βF + βF RE

   Risolviamo quindi il sistema in maniera iterativa, ipotizzando una corrente IC iniziale pari a 2 mA
   e calcolando le altre grandezze incognite:

                                         IC               VGS            VGS
                                       2 mA            0.6505 V        1.447 V
                                     0.951 mA           0.632 V        1.308 V
                                     1.003 mA           0.633 V        1.317 V
                                     0.997 mA           0.633 V        1.316 V
                                       1 mA             0.633 V        1.316 V
   La tensione di uscita vale quindi VO = VCC − RC IC = 5 V, mentre la tensione di base vale
   VB = RE IE + VBE = 1.184 V, le quali confermano che il BJT si trova in regione normale.

2. Il circuito equivalente ai piccoli segnali é il seguente:
                               vg       gmvgs



                                       vs
                                      Rb                Zi
                                                  vb               beta ib
                                                                                 vo
                                                  ib         rbe
                                                                                 Rc


                                                        Ce              Re



                                                                                BJT = I /V = 40 mS,
   I parametri diﬀerenziali dei transistori valgono: rbe = βF Vth /IC = 500 Ω, gm      C  th
    M
   gm OS = βM OS |VGS − VT | = 0.316 mS.
3. Indicando con ZE l’impedenza equivalente al parallelo tra RE e CE e con Zi l’impedenza di ingresso
   di tale stadio elementare, é facile ottenere le seguenti equazioni nel dominio delle trasformate di
   Laplace:

                VO (s) = −β0 IB RC                                                                                  (7)
                               M OS
                 IB (s) =     gm    VGS                                                                             (8)
                                                   M OS               VG
               VGS (s) = VG − VS = VG − (RB + Zi )gm    VGS =      M OS
                                                                                                                    (9)
                                                              1 + gm    (RB + Zi )
                                                                RE
  esprimendo le impedenze come Zi = rbe + (βF + 1) ZE e ZE = 1+sRE CE
                                                                      , otteniamo:

                          VO                M OS R
                                        β0 gm       C
              AV (s) =         =−        M OS (R + Z )
                                                            =
                          VG       1 + gm         B      i
                                                     β0 RC (1 + sCE RE )
                        = −                                                 $                    %                 (10)
                               1                                                 1
                            g M OS + R B +  r be + (β 0 +  1)R E + sC E R E   g M OS + R B + rbe
                                m                                                        m



4. Per ottenere il diagramma di Bode di |AV (s)|, trasformiamo Eq. 10 nella forma:

                                    β0 RC                         1 + sCE RE
           AV (s) = −     1                           ·                 M OS )−1 +R +r                             (11)
                        g M OS
                               + RB + rbe + (β0 + 1)RE 1 + sCE RE M OS(g−1
                                                                        m          B   be
                          m                                                    (gm       )   +RB +rbe +(β0 +1)RE

  la quale evidenzia che la funzione ha un polo e uno zero che valgono, rispettivamente:
                                  M OS )−1 + R + r + (β + 1)R
                                (gm            B     be    0    E
                          p =                M OS )−1 + R + r ]
                                                                  = 2.29 krad/s                                    (12)
                                    CE RE [(gm           B   be
                                   1
                          z =           = 1.9 krad/s                                                               (13)
                                C E RE
  Lo zero interviene prima del polo, quindi l’amplificatore ha un comportamento di tipo passa–alto.
  A bassa frequenza il guadagno vale AV (0) = − 1 +R β+r   0 RC
                                                               +(β +1)R
                                                                        = −1.55, mentre ad altissima
                                                       M OS       B   be   0         E
                                                      gm
                                       β0 RC
  frequenza vale AV (∞) = −          1            = −1.86. Il diagramma di Bode é quindi il seguente:
                                gm  M OS +RB +rbe



                   |Av|


                   1.86



                   1.55




                                               z              p                              ω
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
         Soluzione del compito di Fondamenti di Elettronica Analogica
                               15 febbraio 2017
1. Il transistore è connesso in configurazione base comune. In condizioni stazionarie l’induttore è un
   corto circuito e quindi la giunzione base collettore è certamente polarizzata in inversa. Poichè la
   giunzione base emettitore è invece polarizzata in diretta il transistore si trova in regione normale
   di funzionamento. Abbiamo dunque:
                                                      βF IB
                                                              !       "
                                         VBE = Vth ln        = 0.553 V                               (1)
                                                       IS
                                  0 − (−VEE ) = VBE + R(βF + 1)IB                                    (2)

   da cui otteniamo:
                                               VEE − VBE
                                          R=              ≃ 109 kΩ                                   (3)
                                               (βF + 1)IB
   Chiaramento VO = VCC = 5 V e IO = VCC /RL = 16.7 mA

2. Il circuito equivalente per piccolo segnale del circuito é il seguente
                                    C                 betaib
                                                                     vo   io
                            vi
                                                    ib
                                ii
                                       R            rbe      L           RL



   dal quale otteniamo le seguenti equazioni:


                                          Vo           I o RL    β0 Ib     β0 sL
                     Io (s) = β0 Ib −        = β0 Ib −        =      R
                                                                        =         Ib (s)             (4)
                                          sL             sL     1 + sLL   sL + RL
                                    Veb             Ib rbe                 rbe
                                                                          !                 "
                       Ii (s) =           + β0 Ib =        + β0 Ib = β0 +        Ib (s)              (5)
                                   R||rbe           R||rbe                R||rbe
   da cui calcoliamo:
                         Io           β0        sL        gm (R||rbe )     sL
                            (s) =        rbe ·        =                 ·                            (6)
                         Ii       β0 + R||rbe RL + sL   1 + gm (R||rbe ) RL + sL

   I parametri diﬀerenziali del transistore valgono: rbe = Vth /IB = 25 kΩ, gm = IC /Vth = 1.6 mS.

3. L’espressione determinata in precedenza presenta uno zero nell’origine ed un polo reale positivo.
   Pertanto è di tipo passa alto. La frequenza di taglio a -3dB è determinata dalla frequenza del polo:
                                                              RL
                                                 f−3dB =                                             (7)
                                                              2πL
   Pertanto otteniamo:
                                                  RL
                                           L=           ≃ 478 nH                                     (8)
                                                2πf−3dB
4. per trovare Vo (s)/Vi (s) basta esprimere le due tensioni in funzione delle correnti di ingresso ed
   uscita, cioé:

                                  Vo = RL Io                                                         (9)
                                                          #                        $
                                          Ii                   1       rbe
                                  Vi =       + rbe IB =          +         rbe         Ii           (10)
                                         sC                   sC   β0 + R||r  be
ed esprimere il guadagno di corrente come:

                 Vo   Vo I o I i          gm (R||rbe )     sL        sC
                    =    ·   ·   = RL ·                 ·       ·                             (11)
                 Vi   I o I i Vi        1 + gm (R||rbe ) RL + sL 1 + sCrrbebe
                                                                         β0 + R||r
                                                                                     be


Questa funzione di trasferimento presenta due zeri nell’origine e due poli che valgono:
                                              rbe
                                        β0 + R||r be
                                p1 =                   = 1.65 Mrad/s                          (12)
                                             Crbe
                                        RL
                                p2 =       = 627 Mrad/s                                       (13)
                                        L
I diagrammi di Bode dei moduli delle funzioni di traferimento trovate sono i seguenti:
 Io/Ii                                              Vo/Vi




                              p2        ω                          p1            p2       ω
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
                 Soluzione del compito di Fondamenti di Elettronica
                                  21 giugno 2017
1. Il transistore pnp opera chiaramente in regione normale. Il punto di lavoro é individuato dalle
   equazioni:
                                            VCC − VEB
                                     IR =                                                             (1)
                                                R
                                     IR   = ID + IB                                                   (2)
                                    VEB = VD                                                          (3)
                                           IS        VEB
                                                        
                                     IB =      exp                                                    (4)
                                          βF         V
                                                    th
                                                     VD                  VD
                                                                          
                                     ID = IS exp          − 1 ≃ IS exp                                (5)
                                                     Vth                 Vth

   Semplificando alcune grandezze otteniamo il seguente sistema non lineare di due equazioni in due
   incognite:
                                                    VCC − VEB
                                             IR =                                                     (6)
                                                          R
                                                                 IR βF
                                                                         
                                           VEB    = Vth ln                                            (7)
                                                             IS (βF + 1)
                                                                    (0)
   la cui soluzione si trova per via iterativa a partire da VEB = 0 V porta ad ottenere i seguenti valori:

                                                VEB         IR
                                                 0V       80 µA
                                              0.6524 V   66.95 µA
                                              0.6477 V   67.04 µA
                                              0.6478 V   67.04 µA

   che puó considerarsi con ottima approssimazione la soluzione del problema. Pertanto si ottiene
   VEB,0 = 0.6478 V e IR,0 = 67.04 µA, ID,0 ≃ IC,0 = 66.21 µA.
   La potenza dissipata pertanto vale

                                 P = VCC (ID,0 + IE,0 ) = VCC (IR,0 + IC,0 ) ≃ 533 µW                 (8)

2. Il circuito equivalente ai piccoli segnali è mostrato in Fig.1.
                                                   Zi
                        ii                                                        vc


                                                         rbe              gmvbe
                                                  vbe
                             R                                 ve
                                             rd
                                                                                  Lc

                                                                    Le




                                                   FIGURA 1
   I parametri differenziali del BJT sono rbe = βF Vth /IC,0 ≃ 31.4 kΩ e gm = IC,0 /Vth = 2.55 mS,
   mentre per il diodo ho rd = Vth /ID,0 ≃ 393 Ω.
3. Indicando con Zi la resistenza di ingresso del doppio carico realizzato dal BJT, le funzioni di
   trasferimento possono essere facilmente calcolate come segue:

                                                                               rd ||R
               VC (s) = −sLC gm VBE (s) = −sLc β0 IB (s) = −sLC β0                        Ii (s)
                                                                          rd ||R + Zi (s)
                                                                   rd ||R
               VE (s) = sLE (β0 + 1)IB (s) = sLE (β0 + 1)                     Ii (s)
                                                              rd ||R + Zi (s)

  dove Zi (s) = rbe + (β0 + 1)sLE .

4. Nella condizione Lc β0 = Le (β0 + 1), si trova facilmente che VC = −VE e quindi si ottiene:

                       VE (s) − VC (s)       2VE (s)                   rd ||R
                                         =           = 2sLC β0                                      (9)
                            Ii (s)            Ii (s)           rd ||R + rbe + sLC β0
                       VE (s) + VC (s)
                                         = 0                                                       (10)
                            Ii (s)

  La funzione di trasferimento (Ve (s) − Vc (s))/Ii (s) presenta dunque uno zero nell’origine ed un polo
  alla frequenza
                                              rd ||R + rbe
                                        fp =               ≃ 9 kHz                                  (11)
                                                2πβ0 LC
  mentre a centro banda la funzione vale 2R||rd = 780 Ω. Il diagramma di Bode del modulo della
  funzione considerata é il seguente


                   |(Ve−Vc)/Ii|

                          2R||rd




                                                        fp                    f

                                             FIGURA 2
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
                 Soluzione del compito di Fondamenti di Elettronica
                                   13 luglio 2017
1. Per il calcolo delle correnti e tensioni nel circuito, ipotizziamo i transistori accesi e funzionanti in
   regione normale. Inoltre assumiamo trascurabile la corrente di base (IB2 ) del transitore T2 rispetto
   alla corrente di emettitore (IE1 ) di T1 . Cosı́ facendo é possibile scrivere le seguenti equazioni:


                    VCC      = R1 IB1 + VEB1 + R3 IE1 = IB1 [R1 + (βF + 1)R3 ] + VEB1
                                        βF IB1
                                              
                   VBE1      = Vth ln
                                          IS

   dove IB1 é la corrente di base di T1 . Il sistema é non lineare e si risolve in maniera iterativa:
                                            VEB1              IB1
                                             0V            28.84 µA
                                          0.7279 V         24.64 µA
                                          0.7238 V         24.67 µA
                                          0.7238 V         24.67 µA

   Dai dati ottenuti si ricava IC1 = βF IB1 = 1.23 mA e IE1 = 1.26 mA. A questo punto possiamo
   considerare la maglia di ingresso del transistore T2 e scrivere che:
                             R3 IE1 = VEB2 + R5 IE2 = VEB2 + R5 (βF + 1)IB2
                                              βF IB2
                                                    
                              VEB2 = Vth ln
                                                IS
   che é un’altro sistema non lineare da risolvere iterativamente:
                                            VEB2              IB2
                                             0V              21 µA
                                          0.7197 V         6.888 µA
                                          0.6907 V         7.457 µA
                                          0.6928 V         7.416 µA
                                          0.6926 V         7.420 µA
                                          0.6926 V         7.420 µA

   da cui si nota che IB1 ≪ IE1 , verificando l’ipotesi fatta in precedenza. Ottengo IC2 = 371 µA e
   IE2 = 378 µA.
   La tensione di uscita infine vale: VO = R4 IC2 ≃ 0.74 V, mentre la tensione di collettore di T1 é
   pari a VC1 = R2 IC1 = 1.23 V. Questi valori permetto di calcolare VBC1 = R1 IB1 − VC1 = 1.98 V e
   VBC2 = VCC − R3 IE1 − V0 = 3 V, le quali confermano che i transistori lavorano in regione normale.
2. Il circuito equivalente ai piccoli segnali per il funzionamento a centro banda (C visto come corto
   circuito) è mostrato in Fig.1.
                        vi     ib1 rbe1               vx     ib2                 vo

                                                            rbe2
                               R1           betaib1                              R4
                                                           R3          betaib2
                                            R2
                                                                      R5
                                              FIGURA 1
   dove i parametri differenziali valgono: rbe1 = IVB1
                                                    th
                                                       = 1.05 kΩ, rbe2 = IVB2
                                                                           th
                                                                              = 3.5 kΩ, gm1 = 47.6 mS e
   gm2 = 14.3 mS.

3. A centro banda, essendo C un condensatore di disaccoppiamento, puó essere considerato come un
   corto circuito e il circuito equivalente utile al calcolo del guadagno di tensione é quello in Fig.1.
   Possiamo, ora, calcolarci le tensioni di ingresso e uscita in funzione delle correnti:

                                     vo = −R4 βib2
                                     vi = rbe1 ib1 + rbe2 ib2 + R5 (β + 1)ib2
                                                  vx           rbe2+(β+1)R5
                             (β + 1)ib1 = ib2 +      = ib2 +                ib2
                                                  R3                R3

   Grazie a questo sistema é possibile scrivere vi in funzione della sola ib2 ed ottenere:
                             rbe1          rbe2+(β+1)R5
                                                         
                      vi =         ∗ 1+                     ib2 + rbe2 ib2 + R5 (β + 1)ib2
                            β+1                 R3
                     vo                          βR4
                          = −                               h              i = −1.79                 (1)
                     vi       rbe1
                                   + [rbe2 + (β + 1)R 5 ] ·  1 +    rbe1
                              β+1                                 (β+1)R3


4. Il condensatore di disaccoppiamento C si comporta come un lato aperto in condizioni statiche,
   mentre ha un’impedenza via via sempre pi bassa man mano che la frequenza del segnale di ingresso
   aumenta. Indi per cui, il comportamento del circuito é di tipo passa alto, che taglia a basse
   frequenze, mentre ha un guadagno di tensione pari a vo /vi = −1.79 ad alta frequenza.
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
            Soluzione del compito di Fondamenti di Elettronica Analogica
                                 14 settembre 2017
1. Visto che la tensione di uscita deve valere VO = 5 V, otteniamo subito la corrente di collettore
   richiesta come IC = VO /RC = 5 mA. Ora, supponendo in regione normale il bipolare e tenendo
   conto dell’effetto Early, si puó scrivere il seguente sistema di equazioni:
                                                   IC
                                         IB =
                                                   βF
                                                             VBC
                                                                
                                         βF = βF 0 1 +
                                                              VA
                                       VBC = VB − VC = RB IB − VO
  da cui si ottiene
                                                  2         VA I C
                                             RB I B + (VA − VO )IB −
                                                                   =0                             (1)
                                                             βF 0
  un’equazione di secondo grado in IB con due soluzioni. L’unica soluzione corretta é quella che da
  una corrente di base positiva e quindi si ottiene IB = 65 µA, βF = 76.8 e VB = 7.8 V. Quest’ultimo
  dato, verifica l’ipotesi fatta perché VBC > 0.
  Ora si puó calcolare la tensione VEB come
                                                                              
                                                                      IC
                                       VEB = Vth ln                           = 0.671 V                                (2)
                                                                IS 1 + VVBC
                                                                          A

  la quale fissa la tensione di emettitore, che é anche la tensione di source del MOSFET, a VE =
  VS = VB + VEB = 8.471 V.
  La corrente di drain vale ID = IE = (βBJT  p + 1)IB = 5.065 mA. Supponendo in saturazione il
  MOSFET, otteniamo quindi VGS = VT + 2ID /βM OS = 2.591 V. Quindi Vref = VS + VGS =
  11.06 V, la quale verifica che il MOSFET é saturo.
2. Il circuito equivalente ai piccoli segnali per il funzionamento a centro banda (C visto come corto
   circuito) è mostrato in Fig.1.
                                              rce                                                            rce

                      vg=0
                C       vs                   beta ib                                                        beta ib
                                                           vo                      vs                                 vo
                                 ib                                                              ib
         R                             rbe                 Rc                                         rbe             Rc


       vi               gmvgs                                                             gm
                                        Rb                                                            Rb




                        FIGURA 1                                                        FIGURA 2
  dove i parametri differenziali valgono: rbe = VIth
                                                  B
                                                     = 385 Ω, rce = VICA = 5.8 kΩ e gm = βM OS (VGS −
  VT ) = 6.364 mS.
3. Si deve calcolare la matrice ammettenze del blocco circuitale di Fig.2. Si nota subito che gm e RC
   cadono in parallelo alla porta di ingresso e di uscita, rispettivamente, mentre rce collega ingresso
   ed uscita. L’inclusione di questi elementi nella matrice |h| é quindi molto semplice in quanto
   quest’ultima sará del tipo:
                                                                 ′ +g + 1                       ′ − 1
                                                                                                          
                                       y11 y12                  y11  m  rce                    y12  rce
                             |h| =                    =                                                                 (3)
                                                                                                          
                                                                                                             
                                                                 ′ − 1
                                                                y21                      ′ + 1 + 1
                                                                                        y22
                                       y21 y22                       rce                    RC   rce
   Dove i termini yii′ sono i termini della matrice del circuito rimanente, cioé delle resistenze RB e rbe
   e del generatore comandato β0 ib. Queste componenti si calcolano facilmente come:

                                        i1          −(β0 + 1)ib    β0 + 1
                              y11
                               ′
                                  =              =              =                                       (4)
                                        v1 v2 =0 −(RB + rbe )ib   RB + rbe
                                        i1
                              y12
                               ′
                                  =              =0                                                     (5)
                                        v2 v1 =0
                                        i2            −β0 ib         β0
                              y21
                               ′
                                  =              =              =                                       (6)
                                        v1 v2 =0 −(RB + rbe )ib   RB + rbe
                                        i2
                              y22
                               ′
                                  =              =0                                                     (7)
                                        v2 v1 =0

   per cui la matrice ammettenze del blocco in Fig.2 risulta:
                                             β0 +1          1
                                                                    − r1ce
                                                                            
                                            RB +rbe + gm + rce
                                  |h| =                                                                (8)
                                                                            
                                                                             
                                              β0       1          1    1
                                            RB +rbe − rce        RC + rce


4. Il guadagno di tensione puó essere calcolato sfruttando la matrice |h|, cioé come:

                                 VO       VO VS    y21      Ri
                                    (s) =   ·   =−     ·         1                                      (9)
                                 Vi       VS Vi    y22 Ri + R + sC
                                                                                         −1
   dove Ri é la resistenza di ingresso del blocco di Fig.2 e che vale Ri = y11 − y12y22y21 . Sostituendo
   i valori delle componenti della matrice nelle formule si trova l’espressione del guadagno di tensione.

5. Il condensatore di disaccoppiamento C si comporta come un lato aperto in condizioni statiche,
   mentre ha un’impedenza via via sempre piú bassa man mano che la frequenza del segnale di ingresso
   aumenta. Indi per cui, il comportamento del circuito é di tipo passa alto, cioé taglia a basse
   frequenze.
