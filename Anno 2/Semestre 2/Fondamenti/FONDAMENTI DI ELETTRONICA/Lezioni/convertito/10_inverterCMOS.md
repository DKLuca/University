---
fonte: "10_inverterCMOS.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Inverter CMOS

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                                     Inverter CMOS
• L’utilizzo combinato di n-MOSFET e p-MOSFET per la realizzazione di circuiti
  digitali ha portato allo sviluppo della tecnologia Complementary-MOS (CMOS)
• L’inverter CMOS è la porta logica più semplice à utilizza un n-MOSFET e un p-
  MOSFET
                                 OFF              VGSn < VTn à VI < VTn
                                 VI > VTn
                           Mn
                                 TRIODO           VDn < VGn - VTn à VO < VI - VTn
                 Mp
                                 SATURO           VDn > VGn - VTn à VO > VI - VTn

                                 OFF              VGSp > VTp à VI > VDD + VTp
                 Mn
                                 VI < VDD + VTp
                           Mp
                                 TRIODO           VDp > VGp - VTp à VO > VI - VTp
                                 SATURO           VDn < VGn - VTn à VO < VI - VTp
      VTn > 0; VTp < 0;

               se Mn OFF à IDSn = ISDp = 0 à MP in TRIODO con VSDp = 0 à VO = VDD
IDSn = ISDp
               se Mp OFF à ISDp = IDSn = 0 à Mn in TRIODO con VDSn = 0 à VO = 0
                  Inverter CMOS con MOSFET saturi
Hp.: entrambi i MOSFET in saturazione
Hp.: trascuro l’effetto di modulazione di lunghezza di canale (l = 0)
                                          𝛽#                         𝛽'
                                 𝐼!"# =      (𝑉$"# −𝑉%# )& = 𝐼"!' =     (𝑉$"' −𝑉%' )&
                                          2                           2
                                            𝛽#               𝛽'
                                               (𝑉( −𝑉%# )& =    (𝑉( −𝑉!! − 𝑉%' )&
                                             2               2
                                                   )!                        )!
                                𝑉( − 𝑉%# =              𝑉( − 𝑉!! − 𝑉%' =          (𝑉!! + 𝑉%' − 𝑉( )
                 Mp                             )"                           )"



                                                             𝛽'
                                              𝑉%# +             (𝑉 + 𝑉%' )
                                                             𝛽# !!
                 Mn                    𝑉( =                                         per qualunque VO
                                                            𝛽'                    anche quando VI = VO
                                                         1+
                                                            𝛽#

      VTn > 0; VTp < 0;
                                              𝛽'
                                     𝑉%# +       (𝑉 + 𝑉%' )
                                              𝛽# !!                     Tensione
                             𝑉*% =                                      di soglia
                                                        𝛽'              logica
                                              1+
                                                        𝛽#
                     Inverter CMOS con MOSFET triodo
(1) Mn saturo; Mp triodo
         $!                                                    )
𝐼!"# =        (𝑉&"# −𝑉'# )% = 𝐼"!( = 𝛽( (𝑉&"( −𝑉'( )𝑉!"( − 𝑉!"( %
          %                                                    %
$!                                                     )
     (𝑉* −𝑉'# )% = 𝛽( (𝑉* −𝑉!! − 𝑉'( ) 𝑉+ − 𝑉!! −           𝑉+ − 𝑉!! %
 %                                                     %

à relazione quadratica tra VI e VO


(2) Mn triodo; Mp saturo
                                   )                   $"
𝐼!"# = 𝛽# (𝑉&"# −𝑉'# )𝑉!"# − % 𝑉!"# % = 𝐼"!( = % (𝑉&"( −𝑉'( )%
                      )       $"
𝛽# (𝑉* −𝑉'# )𝑉+ − 𝑉+ % =           (𝑉* −𝑉!! − 𝑉'( )%
                      %        %

à relazione quadratica tra VI e VO
              Caratteristica statica inverter CMOS
                                               VI < VTn
                                               Mn OFF à VO = VDD

               (1)                             VI > VDD + VTp = VDD - |VTp|
                                               Mp OFF à VO = 0


                                               VO > VI - VTn
                                               VO < VI - VTp
                     (2)                       Mn e Mp saturi à VI = VLT

VT,P

                     VLT


(1) Mn saturo; Mp triodo à relazione quadratica tra VI e VO
(2) Mn triodo; Mp saturoà relazione quadratica tra VI e VO
             Prestazioni inverter CMOS
                •   Caratteristica tipica di una porta NOT
                •   Altissima pendenza nella zona
                    centrale à proprietà rigenerativa
                •   MOSFET ideali: AV=∞ per VI = VLT
                •   MOSFET reali: effetto modulazione
                    lunghezza di canale à abbassa AV


                         •   VOH = VDD
                         •   VOL = 0
                         •   VIH e VIL molto vicini a VLT
VT,P
       VLT               à Alti NOISE MARGIN
                         à Ottime prestazioni
                           dell’inverter CMOS
                              Dimensionamento MOSFET
                                        Tipicamente si progettano i MOSFET
                                        per avere: VTn = |VTp| = VT

                                                             𝛽(
                                                        𝑉' +    (𝑉 − 𝑉' )
                                                             𝛽# !!
                                                𝑉,' =
                                                                    𝛽(
                                                              1+
                                                                    𝛽#


                                                                𝛽(   𝛽(
                                                        𝑉'   1−    +    𝑉
                                                                𝛽#   𝛽# !!
                                                𝑉,' =
                                                                         𝛽(
 VT,P                                                          1+
                                                                         𝛽#
                      VLT
                                     𝑊( - 𝑊# -              𝛽#-
Vogliamo VLT = VDD/2 à bp = bn         𝛽 =  𝛽           𝑆( = - 𝑆#
                                     𝐿( ( 𝐿# #              𝛽(
                            𝛽#-     mobilità lacune è metà di quella degli elettroni
Se Ln = Lp = Lmin à     𝑊( = - 𝑊#
                            𝛽(      tendenzialmente i p-MOSFET larghi il doppio
                                        Tempi di commutazione
Parametro molto importante perché impatta sulla frequenza massima di funzionamento
Hp.:     - transizioni/commutazioni istantanee in ingresso (gradini di tensione)
         - considero l’inverter caricato con una capacità in uscita (unico carico)
         - trascuro l’effetto di modulazione di lunghezza di canale (l = 0)
Transitorio di DISCESA (dell’uscita)




              p
                                  • A t = 0- à Mn OFF à VOUT = VDD
                                  • A t = 0+ à Mn ON; Mp OFF à CL si scarica
                  In
                                    attraverso Mn
              n
                                  • A t = 0+ à VDSn = VDD > VIN – VTn à Mn saturo

                                    𝛽#        %
                                                     𝑑𝑉+.'              scarica di CL a
                               𝐼# =    (𝑉 −𝑉 ) = −𝐶,
                                    2 !! '#           𝑑𝑡              corrente costante !
                                                      Tempo di discesa
CL si scarica a corrente costante fino a che Mn rimane saturo à VOUT > VDD – VTn
tSAT à tempo corrispondente all’uscita dalla saturazione di Mn
                                           0#$%                              0#$%
     𝛽#               𝑑𝑉+.'                       𝛽#                              𝑑𝑉+.'
𝐼# =           %
        (𝑉 −𝑉 ) = −𝐶,                    1           (𝑉!! −𝑉'# )% 𝑑𝑡 = −𝐶, 1            𝑑𝑡
     2 !! '#           𝑑𝑡                 /       2                         /      𝑑𝑡

                                                          0#$%            1'(% (0#$% )
                                        𝛽#
                                           (𝑉!! −𝑉'# )% 1      𝑑𝑡 = −𝐶, 1              𝑑𝑉+.'
                                        2                /               1&&

                                                                             𝑉!"# (𝑡$%# ) = VDD – VTn

                                𝛽#
              p                    (𝑉!! −𝑉'# )% 𝑡"4' = −𝐶, 𝑉!! − 𝑉'# − 𝑉!! = 𝐶, 𝑉'#
                                2
                                                               2𝐶, 𝑉'#
                  In                              𝑡"4' =
                                                           𝛽# (𝑉!! −𝑉'# )%
              n
                                      Scarica in regione triodo
se t > tSAT à CL si scarica a corrente variabile perchè Mn è in regione triodo

                            1    %      𝑑𝑉+.'
  𝐼# = 𝛽# (𝑉&"# −𝑉'# )𝑉!"# − 𝑉!"# = −𝐶,
                            2            𝑑𝑡

                      1    %      𝑑𝑉+.'
  𝛽# (𝑉!! −𝑉'# )𝑉+.' − 𝑉+.' = −𝐶,
                      2            𝑑𝑡

     𝛽#               −𝑑𝑉+.'
         𝑑𝑡 =                                             𝑉6 = 2(𝑉!! −𝑉'# )
     2𝐶,      2(𝑉!! −𝑉'# )𝑉+.' − 𝑉+.' %

           1             1          1
                    =       +
    𝑉6 𝑉+.' − 𝑉+.' % 𝑉6 𝑉+.' 𝑉6 (𝑉6 − 𝑉+.' )
                                                          𝑉#$%&' : tensione massima riconosciuta
                                                                      come uno “0” in uscita

      𝛽# 0)         1'*+,-
                               1             1
         1 𝑑𝑡 = − 1                 +                 𝑑𝑉+.'
      2𝐶, 0#$%     1&& 51%! 𝑉6 𝑉+.'   𝑉6 (𝑉6 − 𝑉+.' )
                                       Scarica in regione triodo
tTR = tf - tSAT à tempo per il quale CL si scarica con Mn in regione triodo
VOLmax à tensione per la quale possiamo considerare concluso il transitorio di discesa

𝛽#        1     𝑉!! − 𝑉'#        𝑉6 − 𝑉+,89:
    𝑡'7 =    ln           + ln
2𝐶,       𝑉6     𝑉+,89:        𝑉6 − 𝑉!! + 𝑉'#


            𝐶,           2 𝑉!! − 𝑉'# − 𝑉+,89:
𝑡'7 =                 ln
      𝛽# (𝑉!! − 𝑉'# )           𝑉+,89:




                           2𝐶, 𝑉'#           𝐶,           2 𝑉!! − 𝑉'# − 𝑉+,89:
     𝑡; = 𝑡"4' + 𝑡'7 =                +                ln
                       𝛽# (𝑉!! −𝑉'# )% 𝛽# (𝑉!! − 𝑉'# )           𝑉+,89:


                               2𝐶,          𝑉'#    1 2 𝑉!! − 𝑉'# − 𝑉+,89:
     𝑡; = 𝑡"4' + 𝑡'7 =                            + ln
                         𝛽# (𝑉!! − 𝑉'# ) 𝑉!! − 𝑉'# 2        𝑉+,89:
                                                 Transitorio di salita
Quando la tensione di ingresso commuta da VDD a 0 à tempo di salita della VOUT
• A t = 0- à Mp OFF à VOUT = 0
• A t = 0+ à Mp ON; Mn OFF à CL si carica attraverso Mp


                 Ip          Calcoli del tutto
            p                analoghi al caso
                              precedente !



             n
                            VOHmin à tensione per la quale possiamo considerare
                                             concluso il transitorio di salita
                                      (tensione minima in uscita riconosciuta come un «1»)




                          2𝐶,         −𝑉'(    1 2 𝑉!! + 𝑉'( − (𝑉!! − 𝑉+=8># )
  𝑡< = 𝑡"4' + 𝑡'7 =                          + ln
                    𝛽( (𝑉!! + 𝑉'( ) 𝑉!! + 𝑉'( 2         𝑉!! − 𝑉+=8>#
                                       Tempi di salita e discesa
Durante i transitori di discesa e di salita le tensioni di uscita non possono mai arrivare a
0 e VDD, rispettivamente à VDS = 0 à MOSFET OFF

se VOLmax = 0 e VOHmin = VDD à tf e tr = ∞

                            Considero concluso il transitorio quando è stato completato
                  Ip         il 90% dell’escursione massima della tensione di uscita
              p
                               • VOHmin = 0.9 VDD
                               • VOLmax = 0.1 VDD

              n
                                                      1   𝑟  1
                                              𝐹(𝑟) =        + ln(19 − 20𝑟)
                                                     1−𝑟 1−𝑟 2




                  2𝐶"     𝑉%#                          2𝐶"     |𝑉%' |
            𝑡! =        𝐹                        𝑡& =        𝐹
                 𝛽# 𝑉$$   𝑉$$                         𝛽' 𝑉$$    𝑉$$
                                             Tempo di propagazione
                                              𝑉'
 Tipicamente VTn = |VTp| = VT           𝑟=
                                             𝑉!!

tpr: tempo di propagazione in salita
tpf: tempo di propagazione in discesa

           𝑡'! + 𝑡'&
      𝑡' =
               2

Se le transizioni/commutazioni agli
ingressi sono istantanee i tempi di
propagazione e i tempi di salita e
discesa sono essenzialmente gli
stessi



           𝑡! + 𝑡&    𝐶" 1   1    𝑉%
      𝑡' =         =       +   𝐹
              2      𝑉$$ 𝛽# 𝛽'   𝑉$$
                                      Tempo di propagazione
• F(r) aumenta con r                                                            𝑉'
                                                                          𝑟=
                                                                               𝑉!!
• Per r costante tp inversamente proporzionale a VDD
• Se caliamo VDD, tp aumenta molto à bisogna abbassare VT e aumentare bn e bp

            1   𝑟  1                                   𝑡0 + 𝑡1    𝐶* 1   1    𝑉%
    𝐹(𝑟) =        + ln(19 − 20𝑟)                𝑡' =           =       +   𝐹
           1−𝑟 1−𝑟 2                                      2      𝑉!! 𝛽# 𝛽'   𝑉!!
                                              Consumo di potenza
POTENZA STATICA (ingressi costanti, senza commutazioni)
VIN = 0           à Mn OFF          àI=0 àP=0
                                                                             p
VIN = VDD         à Mp OFF          àI=0 àP=0
à teoricamente è nulla
Intervengono le non idealità del MOSFET:                                     n
• Correnti di sottosoglia (transistore non completam. OFF)
  à IOFF > 0
• Corrente inversa delle giunzioni à IS > 0

• Correnti di leakage: ossido molto sottile à corrente di perdita del gate
POTENZA DINAMICA (ingressi commutano) à già vista in precedenza
          ?              ?                         1'.
                               𝑑𝑉+.'                                           %
𝐸 = 1 𝑉!! 𝐼!! (𝑡)𝑑𝑡 = 1 𝑉!! 𝐶,       𝑑𝑡 = 𝑉!! 𝐶, 1 𝑑𝑉+.' = 𝑉!! 𝐶, 𝑉@A>#B = 𝐶, 𝑉!!
     /                 /        𝑑𝑡                1'*

              >
   𝑃9:; = 𝐶< 𝑉== 𝑓?→A               𝑓?→A      frequenza media con cui
                                              avvengono le commutazioni 0à1
                                         (o VDD e 0) ma assumerà tutto i valori intermedi.
                                         Mentre        e   c     e a ac            a   e,     ce
                                     
                                                  Ingressi graduali
                                         tensioni sia il PMOS che lo NMOS sono accesi e si stab
                                         cortocircuito (temporaneo) fra alimentazione e massa.

a Setensione              di ingresso
      la transizione dell’ingresso  è istantanea àpuò
                                     
                                                   almeno capitare
                                         Questo a e e a d
                                                          un
                                           Vtn<Vin<VDD-|Vtp|      che i due
                                                                       e    è:

   MOSFET OFF à non c’è mai corrente da V a massa
 oNella
     accesi            contemporaneamente                      dando origin
                                         DD

          realtà però c’è sempre una transizione GRADUALE !

 i Es.:
    cortocircuito
        inverter pilotato da altro(I
                                    short) che dissipa potenza
                                  inverter a monte


                         VDD
             VDD + VTp

                                                                VI < VTn à Mn OFF
              VTn
                                                                VI > VDD + VTpà Mp OFF
      0                                                         Ishort = 0 à P = 0

                                                                VTn < VI < VDD + VTp
                                                                Mn Mp ON
                                                                Ishort > 0 à P > 0
                                     Potenza di corto circuito
La potenza spesa per effetto di Ishort > 0 è detta
POTENZA DI CORTO CIRCUITO                                                   Ip
                                                                        p
Il calcolo della potenza di corto circuito è ulteriormente
complicata dal fatto che c’è anche la corrente di
carica/scarica della capacità di carico
                                                                            In
                                                                        n
                   𝑑𝑉()%
      𝐼' − 𝐼# = 𝐶"
                    𝑑𝑡
à troppo complesso da calcolare !!
à la potenza di corto circuito è potenza persa (corrente non utilizzata)
à posso valutare il caso peggiore: CL piccola, corrente di carica/scarica
  trascurabile à In ≅ Ip = Ishort
à In ≅ Ip è la condizione utilizzata per calcolare la caratteristica statica VO=f(VI)
                                                     (o VDD e 0) ma assumerà tutto i valori intermedi.
                                                     Mentre        e   c     e a ac            a   e,     ce
                                        Potenza di corto circuito
                                                
                                                     tensioni sia il PMOS che lo NMOS sono accesi e si stab
                                                     cortocircuito (temporaneo) fra alimentazione e massa.
                                                    Questo a e e a d              e    è:
                                     VTn < VI < V
                                                 LT
                                                   V <V <V -|V |
                                                          tn   in   DD   tp

                                     Mn saturo, Mp triodo
                                     (t1 < t < t2)


                                     VI = VLT
                                     Mn saturo, Mp saturo
                                     (t = t2)


                                     VLT < VI < VDD + VTp
             VLT                     Mn triodo, Mp saturo
                                     (t2 < t < t3)
        #0                #1                    #0
                                                                              Hp.: VTn = |VTp| = VT
𝐸!" = 1 𝑉$$ 𝐼!" (𝑡)𝑑𝑡 = 1 𝑉$$ 𝐼% (𝑡)𝑑𝑡 + 1 𝑉$$ 𝐼& (𝑡)𝑑𝑡
       #/                #/                 #1                                         bp = bn
              #1                #1
                                 𝛽%                                                      l=0
𝐸!" = 2𝑉$$ 1 𝐼% (𝑡)𝑑𝑡 = 2𝑉$$ 1      (𝑉'% −𝑉( )) 𝑑𝑡
            #/                #/ 2
                                               (o VDD e 0) ma assumerà tutto i valori intermedi.
                                               Mentre        e   c     e a ac            a   e,     ce
                                      Potenza di corto circuito
                                           
                                               tensioni sia il PMOS che lo NMOS sono accesi e si stab
                                               cortocircuito (temporaneo) fra alimentazione e massa.
                                              Questo a e e a d              e    è:
               #1
                𝛽%                               Vtn<Vin<VDD-|Vtp|
 𝐸!" = 2𝑉$$ 1      (𝑉'% −𝑉( )) 𝑑𝑡
             #/ 2


Hp.: Vin cresce (0 à VDD) linearmente
         nel tempo tra 0 e tR
        𝑉(%                 𝑉,( 𝑡+               𝑡
𝑡* = 𝑡+             𝑡) = 𝑡+     =     𝑉'% = 𝑉$$
        𝑉$$                 𝑉$$   2             𝑡+


               #2                                    /
                                )
                )           𝑡         𝛽% 𝑡+ 𝑉$$                       Per la salita di Vin
𝐸!"- = 𝑉$$ 𝛽% 1         𝑉$$ − 𝑉( 𝑑𝑡 =           − 𝑉(
                 .
               #2 %!       𝑡+          3     2                        à discesa di VOUT
                 .&&



                      /
       𝛽% 𝑡1 𝑉$$
𝐸!"0 =           − 𝑉(                 Per la discesa di Vin
        3     2
                                      à salita di VOUT
Potenza dinamica
          Potenza di cortoda    cor
                           circuito                    
                                                           (o VDD e 0) ma assumerà tutto i valori intermedi.
                                                           Mentre        e   c     e a ac            a   e,     ce
                                                           tensioni sia il PMOS che lo NMOS sono accesi e si stab
                                                           cortocircuito (temporaneo) fra alimentazione e massa.
                                                          Questo a e e a d              e    è:
La corrente di corto circuito massima si ottiene per
                                                  VtnV    = DD
                                                       inin<V
                                                      <V      V-|V
                                                                LT tp|

                                         )
            𝛽%               𝛽% 𝑉$$
    𝐼&234 =    (𝑉,( −𝑉( )) =        − 𝑉(
            2                2 2
     Al variare della tensione di ingresso può capi
                                   /
    𝐸 dispositivi
                − 𝑉 siano 𝐼 accesi
                                − 𝑉 contemporaneamente
         𝛽 𝑡 𝑉
             % +     $$2𝑡    𝑉         +          $$
       =
     !"-             =         (           &234            (
           3  2         3     2
      una2𝑡 corrente
              1 𝑉       di cortocircuito (Ishort) che dissip
                          $$
    𝐸!"0 =        𝐼&234        − 𝑉(
             3            2
                                                                      VDD
                                                       VDD + VTp
    𝑃!" = 𝐸!"- + 𝐸!"0 D 𝑓
                                                           VTn
f à frequenza di commutazione
                                              0
inoltre, se tC = tF = tR

           4𝑡"       𝑉$$
 𝑃!" =         𝐼&234     − 𝑉( D 𝑓
            3         2
                                                 Impatto di CL su PSC
• La capacità CL riduce la potenza di corto circuito perché
  assorbe corrente dall’alimentazione à minore corrente                  Ip
  persa verso massa !!                                               p
à CL più alto migliora le cose a prima vista
à attenzione che però ho impatto su tp
                                                                         In
à la variazione di VOUT rallenta !!                                  n

à l’eventuale stadio a valle vede un ingresso che varia più
  lentamente !! à tP1 = tC2 (tempo di propagazione stadio 1
  diventa tempo di commutazione ingresso stadio 2)

à transizione più lenta peggiora potenza di corto circuito
  dello stadio successivo !!                                    1             2


                     4𝑡"       𝑉$$
             𝑃!" =       𝐼&234     − 𝑉( D 𝑓
                      3         2

Progetto ed ottimizzazione di porte CMOS à tC in ingresso e tP in uscita simili
à PSC = 10% Pdin
                     Impatto dell’ingresso graduale su tP
                                                 I ea
                                                                e               a a ae        a a ea e e
                                                 (o VDD e 0) ma assumerà tutto i valori intermedi.
•   Nel calcolo del tempo di salita e discesa  avevamo
                                                 Mentre        e   c     e a ac            a    e,      ce
    ipotizzato transizioni istantanee dell’ingresso
                                                 tensioni sia il PMOS che lo NMOS sono accesi Ip e si stabilis
                                                 cortocircuito (temporaneo) fra alimentazione e massa.
                                                                                            p
•   Con ingresso graduale le cose peggiorano   Questo a      e e a d          e    è:
                                                        Vtn<Vin<VDD-|Vtp|
                              𝑑𝑉()%
                 𝐼' − 𝐼# = 𝐶"                                                                    In
                               𝑑𝑡
                                                                                             n
• La carica/scarica di CL rallenta (ho meno corrente
    utile; parte se ne perde)
• La porta logica diventa più lenta à tempi di
  propagazione del dato più lunghi !                                                                        Co



• La soluzione analitica del problema è troppo
  complessa à simulatori circuitali
                     Stima di tP con ingresso graduale
                                          I ea            e               a a ae        a a ea e e
                                           (o VDD e 0) ma assumerà tutto i valori intermedi.
                                          Mentre        e   c     e a ac            a    e,      ce
                                           tensioni sia il PMOS che lo NMOS sono accesi Ip e si stabilis
                                           cortocircuito (temporaneo) fra alimentazione e massa.
                                                                                      p
                                          Questo a e e a d              e    è:
                                             Vtn<Vin<VDD-|Vtp|


                                                                                         In
                                                                                     n




                                                                  𝑡' = 𝑡'&* + 𝜂 0 𝑡+,
                                                                                                     Co




                                                        𝑡&          tempo di propagazione
                                                        𝑡&05        tempo di propagazione
• Il simulatore predice un tempo di propagazione                    con ingresso istantaneo
  che aumenta circa linearmente con il tempo di         𝜂           parametro empirico
  salita dell’ingresso
                                                        moderne tecnologie CMOS
à Modello empirico
                                                        à 𝜂 = 0.25
                                       Capacità inverter CMOS
• Tempi di commutazione e di ritardo dipendono dagli effetti reattivi del circuito
• Potenza dinamica spesa dipende dal valore di capacità di carico
• Importante valutare le capacità in ingresso e in uscita dell’inverter CMOS


                                 Capacità vista al gate dei MOSFET
                                 Hp.: 𝐶$"2 = 𝐶$!2 (capacità di fringing e overlap identiche
                                 dalla parte del source e del drain, sia per n- che p-MOSFET)
                 Mp

                                    𝐶-# ≅ 𝑊# 𝐿# 𝐶(. + 2𝑊# 𝐶-/*

                 Mn                 𝐶-' ≅ 𝑊' 𝐿' 𝐶(. + 2𝑊' 𝐶-/*

                             Hp.: 𝐿% = 𝐿& = 𝐿678 à MOSFET a lunghezza minima


 Capacità di ingresso dell’inverter CMOS

  𝐶,#0 = 𝐶-# + 𝐶-' = 𝑊# + 𝑊' 𝐿123 𝐶(. + 2(𝑊# + 𝑊' )𝐶-/*
                 Capacità di ingresso dell’inverter
  𝐶,#0 = 𝐶-# + 𝐶-' = 𝑊# + 𝑊' 𝐿123 𝐶(. + 2(𝑊# + 𝑊' )𝐶-/*


                            𝑊#             𝑊'             𝑆' 𝑊'
                      𝑆# =           𝑆' =              𝛼=   =
                           𝐿123           𝐿123            𝑆# 𝑊#
            Mp
                        𝐶,#0 = 𝑆# 1 + 𝛼 𝐿123 4 𝐶(. + 2𝐿123 𝐶-/*

            Mn
                              𝐶6* = 𝐿678 ) 𝐶9: + 2𝐿678 𝐶;!5

                      𝐶6* à capacità di MOSFET ad area minima
                              (dipende solo da parametri tecnologici)

                               𝐴678 = 𝑊678 𝐿678 = 𝐿678 )

𝐶,#0 = 𝑆# 1 + 𝛼 𝐶15      𝐴'%< = 𝑊% 𝐿678 + 𝛼𝑊% 𝐿678 = 𝑆% 1 + 𝛼 𝐿678 )

                        𝐴'%< = 𝑆% 1 + 𝛼 𝐴678   [𝑆% 1 + 𝛼 numero di quadri]
                           Capacità di uscita dell’inverter
Per la capacità vista all’uscita dall’inverter dobbiamo tenere presente tutti i possibili
Calcolo            di    tp:     capacità              in gioco
contributi capacitivi sul nodo di uscita à ipotizziamo un secondo inverter come carico
à contributo di capacità costante sul nodo di uscita 𝐶   =𝑆 1+𝛼 𝐶
                                                             '%<)   %)   )   6*




                                                                                  secondo
                                                                                  inverter
                                                                                  come
                                                                                  carico




 VSB = 0
                    C = ca ac de           ec    e      e a c a
                    del primo inverter e ingresso del secondo
alcolo di tp: capacità in gioco
                           Capacità di giunzione
                                                                                                          𝐶7*
                                                                                         𝐶$6 = 𝑊𝐿/
                                                                                                           |𝑉$6 |
                                                                                                      1+
                                                                                                            Φ7

                                                                                         𝑉$= = 𝑓(𝑉9>( )




          C = ca ac de           ec    e      e a c a
          del primo inverter e ingresso del secondo
                                                           Courtesy of Massimo Barbaro

                                                                              1               𝑑𝑉9>(
  es.: Vin = VDD e n-MOSFET triodo à                      𝛽% (𝑉$$ −𝑉(% )𝑉9>( − 𝑉9>( ) = −𝐶$=%
                                                                              2                𝑑𝑡


        𝑊𝐿! 𝐶?5 .')                                     𝑑𝑉9>(
  𝑡(+ =        1                                                                            à troppo complicato !!
         𝛽%     .'3                           1                                  |𝑉9>( |
                             (𝑉$$ −𝑉(% )𝑉9>( − 𝑉9>( )                     1+
                                              2                                    Φ?
                     Capacità di giunzione equivalente
• Il calcolo sarebbe molto più semplice se CDB fosse costante
• CDBeq à capacità equivalente; valore medio di CDB durante il transitorio di
  carica/scarica
es: transitorio di scarica à scarica scambiata:
                                              A              .') 𝑊𝐿 𝐶
                                                𝑑𝑉9>(               ! ?5
                                    Δ𝑄? = 1 𝐶$=       𝑑𝑡 = 1             𝑑𝑉9>(
                                           5     𝑑𝑡         .'3      𝑉
                                                                 1 + 9>(
                                                                      Φ?

            Δ𝑄?             .') 𝑊𝐿 𝐶
                     1            ! ?5
   𝐶$=2@ =      =         1             𝑑𝑉9>(
           Δ𝑉9>( 𝑉9- − 𝑉9' .'3
                                   𝑉9>(
                                1+ Φ
                                              ?



                                      .')
            𝑊𝐿! 𝐶?5          𝑉9>(             2Φ? 𝑊𝐿! 𝐶?5      𝑉9-      𝑉9'
   𝐶$=2@ =           2Φ? 1 +                =               1+     − 1+
           𝑉9- − 𝑉9'          Φ?               𝑉9' − 𝑉9-       Φ?       Φ?
                                      .'3
                   Capacità di giunzione equivalente
          2Φ? 𝑊𝐿! 𝐶?5      𝑉9-      𝑉9'                       )B4           .')          .'3
  𝐶$=2@ =               1+     − 1+           def.: 𝐾2@ =              1+         − 1+
           𝑉9- − 𝑉9'       Φ?       Φ?                      .') C.'3        B4           B4



                                                                2Φ?         𝑉$$
• Nell’inverter CMOS à VOH = VDD; VOL = 0              𝐾2@ =           1+       −1
                                                                𝑉$$         Φ?
• Keq < 1
• Keq e CDBeq definiti da parametri tecnologici e dalla tensione di alimentazione

 𝐶$689 = 𝐾89 𝑊𝐿/ 𝐶7*

• Identica per n-MOSFET e p-MOSFET
                                            es.: VDD = 5 V, Φ? = 1 V à Keq = 0.6


• Sostituisco tutte le CDB con CDBeq costante !!
• Contributo di capacità costante sul nodo di uscita
alcolo di tp: capacità in gioco
                           Capacità di gate-drain
                                                                          Le capacità CGDp e CGDn:
                                                                          • non hanno terminali a massa!
                                                                          • connesse a Vin e Vout
                                                                          • vedono la tensione (Vin – Vout)
                                                                          • dipendono dal punto di lavoro
                                                                          • sono in parallelo

                                                                                     𝐶;$ = 𝐶;$% + 𝐶;$&

         C = ca ac de           ec    e      e a c a
         del primo inverter e ingresso del secondo
                                                       Courtesy of Massimo Barbaro



    contributo di carica sull’uscita:
               A                                    A
                              𝑑(𝑉DE# − 𝑉'% )                          𝑑𝑉DE# 𝑑𝑉'%
    Δ𝑄9 = 1 𝐶;$ (𝑉'% , 𝑉DE# )                𝑑𝑡 = 1 𝐶;$ (𝑉'% , 𝑉DE# )      −     𝑑𝑡
           5                       𝑑𝑡              5                   𝑑𝑡    𝑑𝑡

    dipende dall’evoluzione temporale di Vin e Vout à complicato (devo semplificare)
   c    e a ac           a    e,     ce range di
PMOS che lo NMOS sono accesi e si stabilisce quindi un
emporaneo) fra alimentazione e massa.Capacità tra ingresso e uscita
 e a d        e    è:
 -|Vtp|
  Hp. semplificativa: transitori di Vin e Vout disgiunti à Vout varia dopo che Vin si è stabilizzata
                                        Courtesy of Massimo Barbaro


                              A) 0 < t < tRi à Vin varia e Vout = VDD
                              B) tRi < t < ∞ à Vin = VDD e Vout varia

     𝑉DE#                     A1) Vin < VTn à Mn OFF; Mp triodo con VSD = 0
                 𝑡+'                     Courtesy of Massimo Barbaro

<Vin<VDD-|Vtp|
                                                                *
 a e e a d            e     è:         𝐶;$% = 𝑊% 𝐶;!5 ; 𝐶;$& = ) 𝑊& 𝐿678 𝐶9: + 𝑊& 𝐶;!5
cuito (temporaneo) fra alimentazione e massa.
i sia il PMOS che lo NMOS sono accesi e si stabilisce quindi un
       e   c    e a ac             a   e,    ce range di
                                       A2) VTn < Vin < VDD + VTpà Mn saturo con VDS = VDD; Mp triodo
e 0) ma assumerà tutto i valori intermedi.
         e          Mpa a a e a a ea e e f a 0 e VDD
                                                                       *
                              𝐶;$% = 𝑊% 𝐶;!5 ; 𝐶;$& = ) 𝑊& 𝐿678 𝐶9: + 𝑊& 𝐶;!5
za dinamica
       M    da cortocircuito
                       n

                              A3) Vin > VDD + VTp à Mn saturo con VDS = VDD; Mp OFF


                              𝐶;$% = 𝑊% 𝐶;!5 ; 𝐶;$& = 𝑊& 𝐶;!5
   c    e a ac           a    e,     ce range di
PMOS che lo NMOS sono accesi e si stabilisce quindi un
                                  Transitorio di salita dell’ingresso
emporaneo) fra alimentazione e massa.
 e a d        e    è:
 -|Vtp|
  Hp. semplificativa: transitori di Vin e Vout disgiunti à Vout varia dopo che Vin si è stabilizzata
                                          Courtesy of Massimo Barbaro
                                            A
                                                                            𝑑𝑉DE# 𝑑𝑉'%
                                  Δ𝑄9 = 1 𝐶;$ (𝑉'% , 𝑉DE# )                      −     𝑑𝑡                 A) + B)
                                           5                                 𝑑𝑡    𝑑𝑡
                                                #23                              A
                                                                     𝑑𝑉'%                       𝑑𝑉DE#
                                  Δ𝑄9 = − 1           𝐶;$ 𝑉'% , 𝑉DE#      𝑑𝑡 + 1 𝐶;$ 𝑉'% , 𝑉DE#       𝑑𝑡
     𝑉DE#                                      5                      𝑑𝑡        #23              𝑑𝑡
                 𝑡+'                       Courtesy of Massimo Barbaro
                                                                   *
<Vin<VDD-|Vtp|                    A1) e A2) à 𝐶;$ = 𝑊& 𝐿678 𝐶9: + (𝑊% + 𝑊& )𝐶;!5
                                                                     )
 a e e a d            e     è:
cuito (temporaneo) fra alimentazione e massa.
i sia il PMOS che lo NMOS sono accesi A3)e sià    𝐶;$quindi
                                             stabilisce   = (𝑊 un + 𝑊 )𝐶
                                                                  %    & ;!5
       e   c    e a ac             a   e,      ce range di
e 0) ma assumerà tutto i valori intermedi.
         e            #23
                        a a ae        a a ea 𝑑𝑉 e e'% f a 0 e VDD    .&&
      Δ𝑄9F = − 1 𝐶;$ 𝑉'% , 𝑉DE#                          𝑑𝑡 = − 1 𝐶;$ (𝑉'% , 𝑉DE# )𝑑𝑉'%
                     5                           𝑑𝑡                 5

zaΔ𝑄dinamica
      = −1F  da1 𝑊cortocircuito
                   𝐿
                       .&& G.%"
                       𝐶 + (𝑊 + 𝑊 )𝐶
                                                                                         .&&
                                                                                  𝑑𝑉'% − 1          (𝑊% + 𝑊& )𝐶;!5 𝑑𝑉'%
          9                           & 678 9:              %           &   ;!5
                       5          2                                                      .&& G.%"
                                               A1) A2)                                                   A3)

              1
      Δ𝑄9F = − 𝑊& 𝐿678 𝐶9: (𝑉$$ + 𝑉(& ) − (𝑊% + 𝑊& )𝐶;!5 𝑉$$
              2
   c    e a ac           a    e,     ce range di
PMOS che lo NMOS sono accesi e si stabilisce quindi un
emporaneo) fra alimentazione e massa.Transitorio di discesa dell’uscita
 e a d        e    è:
 -|Vtp|
  Hp. semplificativa: transitori di Vin e Vout disgiunti à Vout varia dopo che Vin si è stabilizzata
                                                Courtesy of Massimo Barbaro


                          B) 𝑉'% = 𝑉$$ à Mp OFF; Mn ON
                          B1) 𝑉DE# > 𝑉$$ − 𝑉(% à Mn saturo à 𝐶;$ = (𝑊% + 𝑊& )𝐶;!5
                                                                                      *
                          B2) 𝑉DE# < 𝑉$$ − 𝑉(% à Mn triodo à 𝐶;$ = 𝑊% 𝐿678 𝐶9: + (𝑊% + 𝑊& )𝐶;!5
                                                                                      )
     𝑉DE#
                 𝑡+'                           ACourtesy of Massimo Barbaro
                                                           𝑑𝑉           5
                                                             DE#
<Vin<VDD-|Vtp|                    Δ𝑄9FF = 1 𝐶;$ 𝑉'% , 𝑉DE#       𝑑𝑡 = 1 𝐶;$ (𝑉'% , 𝑉DE# )𝑑𝑉DE#
 a e e a d             e      è:           #23              𝑑𝑡         .&&
cuito (temporaneo) fra alimentazione e massa.
i sia il PMOS che lo
                  .&&NMOS
                        C.%!  sono accesi e si stabilisce quindi un  5
       e FFc    e a ac               a   e,      ce range di                   1
     Δ𝑄9 = 1                     (𝑊% + 𝑊& )𝐶;!5 𝑑𝑉DE# + 1                        𝑊𝐿   𝐶 + (𝑊% + 𝑊& )𝐶;!5 𝑑𝑉DE#
e 0) ma assumerà   tutto i valori intermedi.
                 .&&                                                .&& C.%!   2 % 678 9:
         e               a a ae         a B1)
                                            a ea e e f a 0 e VDD                          B2)

                                  1
     Δ𝑄9FF = −(𝑊% + 𝑊& )𝐶;!5 𝑉$$ − 𝑊% 𝐿678 𝐶9: (𝑉$$ − 𝑉(% )
za dinamica da cortocircuito      2


     Δ𝑄9 = Δ𝑄9F + Δ𝑄9FF
                         Capacità equivalente sull’uscita
Con la variazione di carica sul nodo di uscita calcolo una capacità equivalente
sul nodo di uscita
    Δ𝑄9 = Δ𝑄9F + Δ𝑄9FF                    Hp.: VTn = |VTp| = VT

                                1
    Δ𝑄9 = −2(𝑊% + 𝑊& )𝐶;!5 𝑉$$ − (𝑊% + 𝑊& )𝐿678 𝐶9: (𝑉$$ − 𝑉( )
                                2

           Δ𝑄9     Δ𝑄9        Δ𝑄9                   1                   𝑉$$ − 𝑉(
 𝐶;$2@ =        =          =−     = 2 𝑊% + 𝑊& 𝐶;!5 + (𝑊% + 𝑊& )𝐿678 𝐶9:
           Δ𝑉DE# 𝑉9- − 𝑉9'    𝑉$$                   2                     𝑉$$


 le componenti parassite costanti vengono raddoppiate                   𝑉$$ − 𝑉(
                                                                  𝑅$$ =
 à EFFETTO MILLER à agisce su componenti connessi                         𝑉$$
    tra ingresso e uscita à Ceq = (1-AV) ∙ C
 à inverter: AV medio è pari a -1 à Ceq = 2 ∙ C

                                         1
                 𝐶;$2@ = 2 𝑊% + 𝑊& 𝐶;!5 + (𝑊% + 𝑊& )𝐿678 𝐶9: 𝑅$$
                                         2
alcolo di tp: capacità in gioco
            Capacità totale in uscita all’inverter


                                                                           𝐶, = 𝐶;$2@ + 𝐶$=2@ + 𝐶H + 𝐶'%<)



                                                                                                     CARICO

                                                                                  SELF LOADING !!
                                                                                  L’inverter carica se stesso !

          C = ca ac de           ec    e      e a c a
          del primo inverter e ingresso del secondo
                                                        Courtesy of Massimo Barbaro



 CAPACITA’ TOTALE SUL NODO DI USCITA (costante)
  𝐶, = 𝐶;$2@ + 𝐶$=2@ + 𝐶H + 𝐶'%<) =
                                  1
    = 2 𝑊% + 𝑊& 𝐶;!5 +              𝑊 + 𝑊& 𝐿678 𝐶9: 𝑅$$ + 𝐾2@ 𝑊% + 𝑊& 𝐿! 𝐶?5 + 𝐶H +
                                  2 %
    + 2 𝑊%) + 𝑊&) 𝐶;!5 + 𝑊%) + 𝑊&) 𝐿678 𝐶9:
alcolo di tp: capacità in gioco
              Ritardo minimo tecnologia CMOS
                                                                          Qual è il tempo di ritardo minimo
                                                                          che ci può garantire la tecnologia
                                                                          CMOS ?

                                                                          à Due inverter identici in cascata
                                                                                Wn=Wn2; Wp=Wp2
                                                                          à MOSFET a lunghezza minima
                                                                          à VTn = |VTp| = VT

                                                                                𝑊%           𝑊&        𝑆'
                                                                          𝑆% =         𝑆& =         𝛼=
         C = ca ac de           ec    e      e a c a                           𝐿678         𝐿678       𝑆#
         del primo inverter e ingresso del secondo
                                                       Courtesy of Massimo Barbaro


                      1
 𝐶, = 2 𝑊% + 𝑊& 𝐶;!5 + 𝑊% + 𝑊& 𝐿678 𝐶9: 𝑅$$ + 𝐾2@ 𝑊% + 𝑊& 𝐿! 𝐶?5 + 𝐶H +
                      2

    + 2 𝑊% + 𝑊& 𝐶;!5 + 𝑊% + 𝑊& 𝐿678 𝐶9:
                       Ritardo degli inverter in cascata
                        1
𝐶, = 2 𝑊% + 𝑊& 𝐶;!5 +     𝑊 + 𝑊& 𝐿678 𝐶9: 𝑅$$ + 𝐾2@ 𝑊% + 𝑊& 𝐿! 𝐶?5 + 𝐶H +
                        2 %
   + 2 𝑊% + 𝑊& 𝐶;!5 + 𝑊% + 𝑊& 𝐿678 𝐶9:                             𝑉$$ − 𝑉(      𝑉(
                                                             𝑅$$ =          =1−
                                                                     𝑉$$        𝑉$$

        1                                                1
𝐶, = 1 + 𝑅$$ 𝑊% 𝐿678 𝐶9: + 4𝑊% 𝐶;!5 + 𝐾2@ 𝑊% 𝐿! 𝐶?5 + 1 + 𝑅$$ 𝑊& 𝐿678 𝐶9: +
        2                                                2

                                                           + 4𝑊& 𝐶;!5 + 𝐾2@ 𝑊& 𝐿! 𝐶?5 + 𝐶H
                  Cn


𝐶" = 1 + 𝛼 𝐶# + 𝐶:

Hp.: transizione istantanea dell’ingresso à sfrutto i calcoli che ho già fatto !

      𝑡! + 𝑡&    𝐶" 1   1    𝑉%   1 + 𝛼 𝐶# + 𝐶: 1   1    𝑉%
 𝑡' =         =       +   𝐹     =                 +   𝐹
         2      𝑉$$ 𝛽# 𝛽'   𝑉$$        𝑉$$      𝛽# 𝛽'   𝑉$$
                                Dipendenza dai parametri
                                                                𝑆'
𝐶" = 1 + 𝛼 𝐶# + 𝐶:                                           𝛼=
                                                                𝑆#
     1 + 𝛼 𝐶# + 𝐶: 1   1    𝑉%
𝑡' =                 +   𝐹
          𝑉$$      𝛽# 𝛽'   𝑉$$

à aumenta con l’aumentare della capacità dell’interconnessione
à diminuisce con l’aumentare della tensione di alimentazione
à Cn, bn dipendono da Sn à dimensionamento
à come dipende da a ?                             𝛽# ′ 𝜇#        𝛽' 𝑆' 𝛽' ′ 𝛼
                                             𝜀=       =            =       =
                                                  𝛽' ′ 𝜇'        𝛽# 𝑆# 𝛽# ′ 𝜀
     1 + 𝛼 𝐶# + 𝐶: 1   𝜀     𝑉%
𝑡' =                 +    𝐹                                      𝛼
          𝑉$$      𝛽# 𝛼𝛽#   𝑉$$                              𝛽' = 𝛽#
                                                                 𝜀
       1 + 𝛼 𝐶# + 𝐶:    𝜀    𝑉%
𝑡' =                 1+   𝐹
          𝛽# 𝑉$$        𝛼   𝑉$$             à se aumenta a, tp cosa fa?
                                                   aumenta bp, ma anche CL !!
                                  Dimensionamento ottimo
        1 + 𝛼 𝐶# + 𝐶:    𝜀    𝑉%                                  𝛽# ′      𝑆'
   𝑡' =               1+   𝐹                               𝜀=            𝛼=
           𝛽# 𝑉$$        𝛼   𝑉$$                                  𝛽' ′      𝑆#

 𝜕𝑡'            𝜕𝑡'          𝜀                 𝜀
     =0             ∝ 𝐶# 1 +   − 1 + 𝛼 𝐶# + 𝐶: 4 = 0
 𝜕𝛼             𝜕𝛼           𝛼                𝛼

                  𝐶:
  𝛼;'< =     𝜀 1+           à interconnessione breve: 𝐶H ≪ 𝐶% à      𝛼WXY = 𝜀
                  𝐶#


                          1 + 𝜀 4 𝐶#    𝑉%
  𝐶H ≪ 𝐶% à      𝑡' ;'< =            𝐹
                            𝛽# 𝑉$$     𝑉$$

             1+ 𝜀 4          𝑉%           1
𝑡' ;'< =                  𝐹     0 𝑊#   1 + 𝑅$$ 𝐿123 𝐶(. + 4𝐶-/* + 𝐾89 𝐿/ 𝐶7*
            𝑊#              𝑉$$           2
               𝜇 𝐶 𝑉
           𝐿123 # (. $$

  à 𝑾𝒏 si semplifica !! à NON DIPENDE DAL DIMENSIONAMENTO !!
                           Ritardo minimo inverter CMOS
Se l’effetto dell’interconnessione è trascurabile à l’effetto del self-loading è dominante !

  𝛼WXY = 𝜀

              𝐿123 1 + 𝜀 4    𝑉%              1             𝐶-/*          𝐶7*
     𝑡' ;'< =              𝐹     0         1 + 𝑅$$ 𝐿123 + 4      + 𝐾89 𝐿/
                  𝜇# 𝑉$$     𝑉$$              2             𝐶(.           𝐶(.

Il ritardo non dipende da quanto facciamo grandi i transistori (dimensionamento):
• se aumento 𝑊# aumenta proporzionalmente la corrente di carica/scarica
• se aumento 𝑊# aumenta proporzionalmente la capacità
à gli effetti si annullano !
à SCELGO DI FARE I MOSFET AD AREA MINIMA (minor consumo di spazio)
à 𝑡' ;'< dipende da LMIN

        𝐶;!5          𝐶?5                                      Tecnologie CMOS
se
        𝐶9:
             ≪1
                      𝐶9:
                          ≪1         𝑡X WXY ∝ 𝐿>Z[\
                                                            scalate sono più veloci !!
                   Applicazione: oscillatore ad anello
Catena di N inverter tutti uguali, con N numero dispari, connessi ad anello
• non c’è configurazione stabile delle tensioni sui vari nodi
• circuito INSTABILE à OSCILLA à OSCILLATORE AD ANELLO




                                                 1          0           1     0

Genera una forma d’onda periodica
                                                  0          1          0     1
• generatore di onda quadra
• ogni inverter caratterizzato da un tempo di
  ritardo tp
• se N ≥ 5 si dimostra che Tosc ≅ 2Ntp
à posso misurare facilmente tp dalla
frequenza si oscillazione à circuito di test
per le tecnologie CMOS !
                            Scaling della tecnologia CMOS
𝑡& D&# dipende da LMIN à scaling delle dimensioni ha guidato lo sviluppo delle
tecnologie CMOS
Inizialmente: scaling a VDD costante (5 V) à compatibilità con tecnologie precedenti
Hp.: µ costante
Parametro         = f(…)    VDD costante     VDD/U
                                                         s: fattore di scaling delle
 W, L, TOX         LMIN         1/s           1/s        dimensioni
  VDD, VT                        1            1/U
                                                         Ad un certo punto la densità di
     A            W LMIN        1/s2          1/s2
                                                         potenza ha raggiunto valori che
   COX            1/TOX          s             s         compromettevano l’affidabilità dei
    CG        COXW LMIN         1/s           1/s        circuiti à scaling congiunto delle
                                                         tensioni (dagli anni ‘90 in poi)
     b       COXW / LMIN         s             s
    ION           b VDD2         s            s/U2       U: fattore di scaling delle tensioni
     tp           LMIN2         1/s2          U/s2       à limita i campi elettrici
    Pdin      CLVDD2 / tp        s            s/U3       à s=U scaling a campo costante
   Pdin/A                        s3          s3/U3

                                       molto male !!! affidabilità !!!
                                          Velocità di saturazione
Analisi precedente fatta per µ costante ! à v = µ E
Nei transistor ultra-corti la velocità raggiunge il valore di saturazione!!
es.: MOSFET in saturazione 𝐼$! ≅ 𝑊𝐶9: 𝑣I3# 𝑉;! − 𝑉( à la relazione diventa lineare !

Parametro      = f(…)      VDD costante   VDD/U
                                                      s: fattore di scaling delle
 W, L, TOX      LMIN           1/s         1/s        dimensioni
  VDD, VT                       1          1/U
                                                      U: fattore di scaling delle tensioni
    A          W LMIN          1/s2        1/s2
                                                      à limita i campi elettrici
   COX         1/TOX            s           s
                                                      à s=U scaling a campo costante
    CG       COXW LMIN         1/s         1/s
    b             -             -           -
    ION      COXW VDD           1          1/U
    tp            -            1/s         1/s
   Pdin      CLVDD2 / tp        1          1/U2
  Pdin/A                        s2        s2/U2
                                   Scaling a campo costante
• Fino agli anni ’90, scaling a tensione costante (VDD e VT fisse)
• Successivamente, scaling a campo costante à VDD e VT scalano concordemente
• Negli ultimi anni la riduzione di VDD si è fermata à VT non può scalare più !!
à VT è troppo vicina alla tensione di spegnimento del MOSFET (VGS = 0)
• Non posso ridurre troppo il gate overdrive, cioè (VDD - VT) à cala troppo la corrente
                  1990                2000




                                                             Nonostante lo sviluppo
                            [µm]                             della tecnologia VDD non
                                                             scende sotto 1 V !!
