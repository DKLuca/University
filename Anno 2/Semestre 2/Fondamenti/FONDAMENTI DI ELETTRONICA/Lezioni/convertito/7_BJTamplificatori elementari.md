---
fonte: "7_BJTamplificatori elementari.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Amplificatori elementari a BJT

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                      Circuiti a un transistore
• I transistori permetto di realizzare circuiti analogici o digitali
• I circuiti più semplici utilizzano un solo transistore
• BJT ha tre terminali: emettitore, collettore, base
à un ingresso, un uscita, un terminale di riferimento
à DA RICORDARE: la corrente di collettore è frutto dell’effetto valvola à è
  una corrente indotta da altre correnti à non può mai essere l’ingresso !!
à tre possibili configurazioni ELEMENTARI
à tre possibili amplificatori :
1. Emettitore comune à ingresso sulla base, uscita sul collettore,
   emettitore terminale di riferimento
2. Base comune à ingresso sull’emettitore, uscita sul collettore, base
   terminale di riferimento
3. Collettore comune à ingresso sulla base, uscita sull’emettitore,
   collettore terminale di riferimento
à STADIO AMPLIFICATORE ELEMENTARE
                                                  Emettitore comune
                                    Hp.: Regione normale; no effetto Early

                                    𝑉!" = 𝑉#$ + 𝑅# 𝐼#
                                   𝑉%&' = 𝑉(( − 𝑅( 𝐼(                    𝛽# 𝑉$% 𝛽# 𝑅(
                                                 𝑉#$       𝐼! = 𝐼" 𝑒𝑥𝑝         −      𝐼
                                    𝐼( = 𝐼) 𝑒𝑥𝑝                           𝑉&'    𝑉&' !
                                                 𝑉*+
                                        𝐼( = 𝛽, 𝐼#           - no soluzione analitica
                                                             - soluzione numerica

   𝑉)*+
    Vce

      Vcc

                          SATURO
                                              Per ottenere la caratteristica statica
            Reg. ATTIVA




                                              devo risolvere numericamente il sistema
                                              moltissime volte à praticamente
                                              impossibile
Vce,sat
                                              à SIMULATORE CIRCUITALE

                                    Vbe
                                    𝑉$%
   Emettit. comune: modello a soglia
                  1. BJT OFF à 𝑉%&' = 𝑉(( ; 𝑉!" < VBE,g

                  2. BJT ON in regione attiva
                                                             𝑉$% − 𝑉(5,6
                                          𝑉)*+ = 𝑉!! − 𝑅! 𝛽#
                                                                 𝑅(

                  3. BJT ON saturo à VOUT = VCE,SAT

                                    regione normale à AMPLIFICATORE
                                    se la caratteristica è molto pendente,
                                    una piccola escursione su VIN da
                                    grande escursione su VOUT !!
BJT OFF       regione attiva
                                                   𝑅! 𝛽#
                                                         >1
                                                    𝑅(
                      saturazione       Se VIN aumenta VOUT cala !!
                                    à AMPLIFICATORE INVERTENTE
                                    Applicazioni digitali: Porta logica NOT
      VBE,g
base comune                                                   Base comune
                                Ingresso sull’emettitore, uscita sul collettore

                            𝑉! + 𝑅$ 𝐼$ + 𝑉#$ = 0         Hp.: Regione normale; no effetto Early
                              𝑉( = 𝑉(( − 𝑅( 𝐼(
                                          𝑉#$                          𝑉$%     𝛽# 𝑅5
                              𝐼( = 𝐼) 𝑒𝑥𝑝                𝐼! = 𝐼" 𝑒𝑥𝑝 −     −           𝐼
                                          𝑉*+                          𝑉&' 𝑉&' (𝛽# + 1) !
                                       𝛽,
                                𝐼( =       𝐼                      - no soluzione analitica
                                     𝛽, + 1 $                     - soluzione numerica
                          Per ottenere la caratteristica statica devo risolvere
                          numericamente il sistema moltissime volte à praticamente
                          impossibile à SIMULATORE CIRCUITALE
                          à uso il modello a soglia

1. VBE < VBE,g BJT OFF à IB, IC, IE = 0 à 𝑉! = 𝑉!! ; 𝑉$ = −𝑉(5 > -VBE,g

                                                     𝑉) + 𝑉*(,+                          𝛽-
2. BJT ON in regione attiva à VBE = VBE,g à 𝐼( = −       𝑅(
                                                                       𝑉, = 𝑉,, − 𝑅,         𝐼
                                                                                       𝛽- + 1 (


3. BJT ON saturo à VBE = VBE,g; VCE = VCE,SAT à 𝑉, = −𝑉*(,+ + 𝑉,(,./0 = 𝑐𝑜𝑠𝑡𝑎𝑛𝑡𝑒
base comune
        Base comune: caratteristica statica
                           1. 𝑉$ > -VBE,g à BJT OFF à             𝑉! = 𝑉!!
                           2. BJT ON in regione attiva
                                                                   𝑅, 𝛽-
                                                    𝑉, = 𝑉,, +            (𝑉 + 𝑉*(,+ )
                                                                 𝑅( 𝛽- + 1 )1

                           3. BJT ON saturo à      𝑉, = −𝑉*(,+ + 𝑉,(,./0 = 𝑐𝑜𝑠𝑡𝑎𝑛𝑡𝑒

                                                                   Vc

                                                                    Vcc

                                                                             BJT OFF
                                            regione attiva

• Per tensioni Vi alte ottengo VC alte
• Per tensioni Vi basse (negative) ottengo VC
  basse
à no applicazioni digitali                                   −Vbe, γ                    Vi
à applicazioni analogiche: AMPLIFICATORE
                                                                          −Vbe, γ +Vce,sat
                                           saturazione
base comune
         Base comune come amplificatore
                                                     Vc

                                                      Vcc




                                                −Vbe, γ                   Vi

                                                            −Vbe, γ +Vce,sat




se la caratteristica è molto pendente,
una piccola escursione su VIN da
grande escursione su VOUT !!             Se VIN aumenta VOUT aumenta !!
   𝑅! 𝛽#                                 à AMPLIFICATORE NON INVERTENTE
           > 1 à DVC > DVi
 𝑅5 𝛽# + 1
                         Amplificatori invertenti e non
       EMETTITORE COMUNE                            BASE COMUNE

                                                         Vc
       Vce
                                                          Vcc
       Vcc


                  Q
   t



 Vce,sat                                                                      Vi
                                                    −Vbe, γ
                               Vbe
                                                                −Vbe, γ +Vce,sat
                  t

AMPLIFICATORE INVERTENTE               AMPLIFICATORE NON INVERTENTE
• cambia la fase dell’onda periodica   • non cambia la fase dell’onda periodica
• sfasa di 180°
                                                       Collettore comune
                                          Ingresso sulla base, uscita sull’emettitore
                                                                         Hp.: Regione normale;
                                   𝑉! = 𝑅$ 𝐼$ + 𝑉#$ + 𝑅# 𝐼#              no effetto Early
,                                          𝑉- = 𝑅$ 𝐼$
                                                    𝑉#$              - no soluzione analitica
                                       𝐼( = 𝐼) 𝑒𝑥𝑝
e                                                   𝑉*+              - soluzione numerica
                                            𝛽,
                                    𝐼( =         𝐼 = 𝛽, 𝐼#
                                          𝛽, + 1 $
       Per ottenere la caratteristica statica devo risolvere numericamente il sistema
       moltissime volte à praticamente impossibile à SIMULATORE CIRCUITALE
       à uso il modello a soglia


    1. VBE < VBE,g BJT OFF à IB, IC, IE = 0 à 𝑉) = 0; 𝑉$ = 𝑉(5 < VBE,g

                                                              𝑉) − 𝑉*(,+
    2. BJT ON in regione attiva à VBE = VBE,g à     𝐼* =                     𝑉2 = 𝑅( (𝛽- + 1)𝐼*
                                                           𝑅* + (𝛽- + 1)𝑅(


    3. BJT ON saturo à VBE = VBE,g; VCE = VCE,SAT à 𝑉3 = 𝑉,, − 𝑉,(,./0 = 𝑐𝑜𝑠𝑡𝑎𝑛𝑡𝑒
                      Collettore comune: caratteristica
                                1. 𝑉$ < VBE,g à BJT OFF à 𝑉) = 0
                                2. BJT ON in regione attiva
                                                                  𝑅( (𝛽- + 1)
,                                                       𝑉3 =                   (𝑉 − 𝑉*(,+ )
                                                                𝑅* + (𝛽- + 1)𝑅( )1


e                               3. BJT ON saturo à 𝑉3 = 𝑉,, − 𝑉,(,./0 = 𝑐𝑜𝑠𝑡𝑎𝑛𝑡𝑒


                                                  Vo                      saturazione
                                          Vcc−Vce,sat


    • Per tensioni Vi alte ottengo VO alte
    • Per tensioni Vi basse ottengo VO basse
    à no applicazioni digitali
    à applicazioni analogiche: AMPLIFICATORE ??                          regione attiva
                                                  BJT OFF

                                                            Vbe, γ                   Vi
                      Collettore comune: amplificatore?

                                          Vo
                                   Vcc−Vce,sat

,

e


                                                    Vbe, γ                    Vi


    Ho amplificazione del segnale solo se la
    caratteristica è molto pendente, in
    particolare deve essere maggiore di uno

                                                 Se VIN aumenta VOUT aumenta
               𝑅5 (𝛽# + 1)
                             <1                  à AMPLIFICATORE NON INVERTENTE
             𝑅( + (𝛽# + 1)𝑅5
                                                 à MA L’AMPIEZZA DEL SEGNALE NON
                                                   AUMENTA
              à DVO < DVi
                                                 à ha comunque applicazioni (vedremo in seguito)
                                        Stabilità del punto di lavoro

                                                  Polarizzazione nei B
Il punto di lavoro stabilisce anche le applicazioni del circuito
Es.: emettitore comune: amplificatore, porta logica, etc.
              Vcc = 3 V             •   Esistono sostanzialmente   tre modi per polarizzare i BJT
                                                                BJT OFF
                                         – Applicando una tensione nota Vbe regione
                                                                            tramite partitore
                                                                                     attiva resisti
                                         – Collegando una resistenza tra collettore e base
                                         – Utilizzando un generatore di corrente che forzi la corrente
                                               • Specchio di corrente
                                                                                    saturazione
                                    •   Il primo metodo si stabilizza mettendo una resistenza o
                                        all’emettitore (degenerazione di emettitore)
                                    •   Il terzo metodo è più stabile alle variazioni
                                                                         VBE,g

IL PUNTO DI LAVORO DEVE ESSERE STABILE !!
non deve cambiare con il tempo: la sensibilità alla variabilità dei parametri con
invecchiamento, temperatura, sostituzione dei componenti, etc. vanno limitate


TECNICHE DI STABILIZZAZIONE DEL PUNTO DI LAVORO !!
•   utilizzo di generatori di corrente per fissare la corrente
•   utilizzo di una resistenza sull’emettitore
                                   Amplificatore a doppio carico
T: emettitore
  Ingresso sulla base, uscita sul collettore (simile all’emettitore comune), ma non c’è riferimento di
oppio    carico
  tensione sul terminale di emettitore
                                                                      Hp.: Regione normale;
                                                                      no effetto Early
                                  𝑉! = 𝑉#$ + 𝑅$ 𝐼$
                                  𝑉( = 𝑉(( − 𝑅( 𝐼(
                                                                    - no soluzione analitica
                                              𝑉#$
                                  𝐼( = 𝐼) 𝑒𝑥𝑝                       - soluzione numerica
                                              𝑉*+                   - modello a soglia
                                           𝛽,
                                    𝐼( =        𝐼$
                                         𝛽, + 1



                        1. VBE < VBE,g BJT OFF à IB, IC, IE = 0 à 𝑉! = 𝑉!! ; 𝑉$ = 𝑉(5 < VBE,g

                                                  𝑉) − 𝑉*(,+                                   𝛽-
                                              𝐼
  2. BJT ON in regione attiva à VBE = VBE,g à ( =                              𝑉, = 𝑉,, − 𝑅,       𝐼
                                                      𝑅(                                     𝛽- + 1 (

                                                                  𝑉) − 𝑉*(,+
  3. BJT ON saturo à VBE = VBE,g; VCE = VCE,SAT à          𝐼( =
                                                                      𝑅(

                                                        𝑉, = 𝑉,(,./0 + 𝑅( 𝐼( = 𝑉) − 𝑉*(,+ + 𝑉,(,./0
JT: emettitore                 Caratteristica del doppio carico
doppio carico
                                1. 𝑉$ < VBE,g à BJT OFF à 𝑉! = 𝑉!!
                                2. BJT ON in regione attiva
                                                                             𝑅, 𝛽-
                                                              𝑉, = 𝑉,, −            (𝑉 − 𝑉*(,+ )
                                                                           𝛽- + 1 𝑅( )

                                3. BJT ON saturo à 𝑉, = 𝑉) − 𝑉*(,+ + 𝑉,(,./0

                                                  Vc
                                                 Vcc
                                                    BJT OFF            regione attiva

   Applicazioni digitali: NO
   Applicazioni analogiche: AMPLIFICATORE
   INVERTENTE (come emettitore comune)

   Vantaggi?
   Pendenza in regione normale:
                                                                                     saturazione
      𝑅! 𝛽#    𝑅!          Se bF grande
             ≅             indipendente da
    𝛽# + 1 𝑅5 𝑅5           parametri BJT !!
                                                              Vbe, γ                          Vi
JT: emettitore                            Stabilità del doppio carico
doppio carico
                              Nello stadio amplificatore a doppio carico i disturbi che
                              potrebbero far variare il punto di lavoro vengono limitati
                              Es.: VI fissato per lavorare in regione attiva; variazione di
                              temperatura à disturbo
                              • L’aumento di temperatura aumenta la corrente nel BJT
                                (cambia il punto di lavoro)
                              • L’aumento di IE aumenta la caduta su RE
                              • Si riduce VBE                                           𝑉(5
                                                                            𝐼! = 𝐼" 𝑒𝑥𝑝
                              • Cala la corrente nel BJT                                𝑉&'
                              à la corrente si autolimita !!
                              à l’effetto del disturbo viene compensato
                              à retroazione negativa (vedrete il prossimo anno)

    LA RESITENZA SULL’EMETTITORE AUMENTA LA STABILITA’ DEL PUNTO DI LAVORO !!

    Il doppio carico è migliore rispetto all’emettitore comune riguardo la stabilità del circuito
                                          BJT connesso a diodo
• Nel circuito VCB = 0; la giunzione BC è in equilibrio à limite della regione attiva,
  ma le equazioni derivate per questa regione sono ancora valide
• Inoltre VBE = VCE à ho un’unica tensione che pilota il dispositivo e un’unica
  corrente (IE) à bipolo

          𝐼5                                  𝐼! = 𝛽# 𝐼(
                                                           𝑉(5
                                             𝐼! = 𝐼" 𝑒𝑥𝑝
  𝐼(               𝐼!                                      𝑉&'
                         𝑉(5
                                                       𝐼!      1         𝑉(5
                                 𝐼5 = 𝐼! + 𝐼( = 𝐼! +      = 1+    𝐼" 𝑒𝑥𝑝
                                                       𝛽#      𝛽#        𝑉&'
          𝐼5

• La corrente nel bipolo dipende esponenzialmente dalla tensione applicata
• Caratteristica simile al diodo
• Se ho processo tecnologico per fabbricare BJT non serve sviluppare quello per
  fare i diodi à uso un BJT per creare un diodo
• Diodi e BJT hanno stesse dipendenze dai paramentri (es.: temperatura)
                                               Specchio di corrente
• Utilizziamo due transistor uguali à stessi parametri (bF, IS)
• Fissiamo la corrente di riferimento (IREF) nel ramo di sinistra del circuito

𝐼95#                                     à Q1 lavora in regione normale (connesso a
                                         diodo; VCB=0)
                                         à inoltre VBE1 = VBE2 = VBE
                                         Hp.: Q2 lavora anch’esso in regione normale
            𝐼(7     𝐼(8
                                                                                𝑉(5
                                          𝐼! = 𝛽# 𝐼(         𝐼!7 = 𝐼!8 = 𝐼" 𝑒𝑥𝑝
                                                                                𝑉&'
                   𝑉(5
                                                                 𝐼!7 𝐼!8      2
                                  𝐼95# = 𝐼!7 + 𝐼(7 + 𝐼(8 = 𝐼!7 +    +    = 1+    𝐼
                                                                 𝛽# 𝛽#        𝛽# !8

               𝛽#
       𝐼!8 =       𝐼             se bF >> 2            𝐼(. ≅ 𝐼/$,
             𝛽# + 2 95#


 IL CIRCUITO SPECCHIA LA CORRENTE DI SINISTRA SUL LATO DI DESTRA !!
 à se trascuro l’effetto Early, IC2 indipendente da VCE2 à generatore di corrente !!
                                             Specchio di corrente
• Il circuito realizzato è in grado di assorbire una corrente fissa indipendentemente
  dalla tensione al nodo da cui assorbe la corrente (generatore di corrente)
• Il circuito funziona correttamente se Q2 è in REGIONE NORMALE à VCE2 > VCE,sat
𝐼95#


                           𝐼(. ≅ 𝐼/$,                𝐼95#     Il circuito può solo
                                                              assorbire la corrente !




             𝑉5(
Q1                      Q2                                    Se uso i BJT pnp, il
                                                              circuito può erogare
                                                              una corrente !
                                                                               𝑉5(
      𝐼95#                                                  𝐼!7 = 𝐼!8 = 𝐼" 𝑒𝑥𝑝
                                                                               𝑉&'
                                  Specchio con aree diverse
Possiamo usare transistor con aree diverse à IS scala con l’area (stessi JS e bF)
                                    à Q1 lavora in regione normale (connesso a
𝐼95#                                diodo; VCB=0)
                                    à inoltre VBE1 = VBE2 = VBE
                                    Hp.: Q2 lavora anch’esso in regione normale
             𝐼(7    𝐼(8                              𝑉(5
                                     𝐼!7 = 𝐴7 𝐽" 𝑒𝑥𝑝                      𝐴7
                                                     𝑉&'          𝐼!7 =      𝐼
                                                     𝑉(5                  𝐴8 !8
                   𝑉(5               𝐼!8 = 𝐴8 𝐽" 𝑒𝑥𝑝
                                                     𝑉&'

                                                         𝐼!7 𝐼!8   𝐴7   𝐴7   1
                          𝐼95# = 𝐼!7 + 𝐼(7 + 𝐼(8 = 𝐼!7 +    +    =    +    +   𝐼
                                                         𝛽# 𝛽#     𝐴8 𝐴8 𝛽# 𝛽# !8
                                            𝐴.
       se bF grande e A2 > A1       𝐼(. ≅      𝐼/$,
                                            𝐴0

à Creo un fattore di scala tra IREF e IC2
à Posso parallelizzare e creare tante correnti (anche diverse) proporzionali a IREF
                                                   Banco di corrente
Possiamo usare transistor con aree diverse à IS scala con l’area (stessi JS e bF)




à Creo un fattore di scala tra IREF e IC2
à Posso parallelizzare e creare tante correnti (anche diverse) proporzionali a IREF
                              Connessione Darlington
                       Tre terminali à ottengo un transistore equivalente


                       • TR2: se è acceso, lavora in regione attiva (tra
                          collettore e base c’è TR1 che lavora con VCE1 > 0)
                       • TR1: il suo funzionamento dipende dalle tensioni
                         esterne à se VCB > 0 è in regione attiva


𝑉(5                    Hp.: entrambi accesi in regione attiva; BJT uguali

                       𝐼! = 𝐼!7 + 𝐼!8 = 𝛽# 𝐼(7 + 𝛽# 𝐼(8 = 𝛽# 𝐼(7 + 𝛽# (𝛽# + 1)𝐼(7

                       𝐼! = (𝛽#8 + 2𝛽# )𝐼(7    proporzionalità tra le correnti !



      se bF >> 2   𝐼( ≅ 𝛽,. 𝐼#0 = 𝛽,,23 𝐼#       𝛽,,23 = 𝛽,.

                                         (es.: bF=100 à bF,eq=10000)
                                    Connessione Darlington
                                            𝐼( ≅ 𝛽,. 𝐼#0 = 𝛽,,23 𝐼#           se bF >> 2

                             Ma posso veramente considerarlo come un unico BJT?
                                                               𝐼!7      𝐼!8
                               𝑉(5 = 𝑉(57 + 𝑉(58 = 𝑉&' ln          + ln
                                                                𝐼"       𝐼"

                                           𝐼!7 𝐼!8     𝛽# 𝐼(7 𝛽#8 𝐼(7         𝛽#: 𝐼(7
                                                                                   8

   𝑉(5                         𝑉(5 = 𝑉&' ln 8 ≅ 𝑉&' ln                = 𝑉&' ln 8
                                             𝐼"             𝐼"8                 𝐼"

                                             𝐼!8            𝐼!8
                               𝑉(5 = 𝑉&' ln        = 𝑉&' ln 8            𝐼),23 = 𝐼) 𝛽,
                                            𝛽# 𝐼"8         𝐼",;<

                 𝐼!
𝑉(5 = 2𝑉&' ln
                𝐼",;<

                𝑉(5     à Si comporta come un unico BJT in regione normale
𝐼! = 𝐼",;< 𝑒𝑥𝑝
               2 𝑉&'    à C’è un fattore 2 nella tensione !!
                        à Ho bisogno di almeno 2 VBE,g per accenderlo !!
are il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali
nsistori nel punto
  riferimento    al dicircuito
                        lavoro didicuiFigura,
                                       al quesito
                                               si precedente.
                                                  risponda ai(punti 4)
                                                               seguenti   quesiti utilizzando i valori assegnati dei
ametri:                                                      Esercizio: Darlington
nendo di poter iniettare nel nodo B del circuito (base del transistore T1) una corrente di
  segnale avente trasformata di Laplace Ii (s), determinare l’espressione della funzione di
.mento
   Assumendo        βF(V!
        Vo (s)/Ii (s)    o =1Vper  entrambiil corrispondente
                              C ), tracciare   i transistori, determinare
                                                              diagramma di iBode
                                                                             valori
                                                                                                       T1
                                                                                    di RB ed RC che consentono di
                                                                                 e determinare
 spondente   frequenza
   polarizzare     il circuito  a Ia −3=10
                         di taglio
                               E,1
                                         dB. (10
                                             µA punti)
                                                C  e V =3 V essendo V la tensione di collettore dei transistori.
                                                                    C
                                                                                                                       T
  (6 punti)

. Assumendo βF ! 1 per entrambi i transistori, Vcc determinare le relazioni IC (VBE ) ed IC (IB ) che
  consentono di modellizzare la coppia di transistori T 1 e T 2 come un unico transistore avente IC =
  IC,1 + IC,2 , VBE = VBE,1 + VBE,2 e IB = IB,1 . Dedurre da tali relazioni i valori efficaci del guadagno
  di corrente RBβF,e e della corrente di saturazioneVIγ,BE  =0.65 V, V
                                                       S,e . (6 punti) CC
                                                                          = 6 V, βF 1 = βF 2 = βF = 100, β0,1
                                          Rc
. Disegnare il circuito equivalente per piccolo segnale e calcolare il valore dei parametri differenziali
  dei transistori nel punto di lavoro di cui al quesito precedente. (punti 4)
                            T1 nel nodo B del circuito
. Supponendo di poter iniettare                            C (base del transistore T1) una corrente di
  piccolo segnale avente trasformataT2    di Laplace Ii (s), determinare l’espressione della funzione di
  trasferimento Vo (s)/Ii (s) (Vo = VC ), tracciare il corrispondente diagramma di Bode e determinare
                  Soluzione
  la corrispondente  frequenza del   compito
                                di taglio       di Fondamenti
                                           a −3 dB.  (10 punti)    di Elettronica
                                             15 febbraio 2011
   1. I transistori lavorano in regione normale di funzionamento. Essendo per ipotesi βF ! 1 otteniamo
                                                                   Vcc
V, VCC = 6 V, βF 1 = βF 2 = βF = 100, β0,1 = β0,2 = β0 = 100, Vth = 25 mV, C = 1 pF.
      immediatamente:
                                        VCC − VB
                            RB "                     = (6 − 1.3)/(10−5 /101) " 47M Ω                (1)
                                      IE,1 /(βF + 1)
                                      VCC − VC
                            RB
                            RC "
                                        βF IE,1
                                                 " 3 kΩ      Rc                                     (2)
circuito in figura (β = 100)                                 Esercizi
                          Hp.: Regione normale (da verificare poi !!)

                                       𝑉( − 𝑉(5,6 4 − 0.7
                                𝐼5 =             =        = 1 𝑚𝐴
                                          𝑅5       3.3 𝑘

                     𝐼!                𝛽#
                                𝐼! =       𝐼 = 0.99 𝑚𝐴
                                     𝛽# + 1 5
        𝐼(
                          𝑉! = 𝑉!! − 𝑅! 𝐼! = 10 − 4.7 𝑘 A 0.99 𝑚 = 5.3 𝑉
                     𝐼5
                          𝑉5 = 𝑉( − 𝑉(5,6 = 4 − 0.7 = 3.3 𝑉
rcizi
                          𝑉!5 = 𝑉! − 𝑉5 = 5.3 − 3.3 = 2 𝑉 > 𝑉!5,=>&
gura (β = 100)
                          Ipotesi verificata; soluzione corretta !!
     VBE,g = 0.7 V
ircuito in figura (β = 100)                                  Esercizi
                          Hp.: Regione normale (da verificare poi !!)

                                       𝑉? − 𝑉5(,6 10 − 0.7
                                𝐼5 =             =         = 4.65 𝑚𝐴
                     𝐼5                   𝑅5        2𝑘

         𝐼(                            𝛽#
                                𝐼! =       𝐼 = 4.6 𝑚𝐴
                                     𝛽# + 1 5


                          𝑉! = 𝑉@ + 𝑅! 𝐼! = −10 + 1 𝑘 A 4.6 𝑚 = −5.35 𝑉
                     𝐼!

                          𝑉5 = 𝑉( + 𝑉5(,6 = +0.7 𝑉
rcizi
                          𝑉5! = 𝑉5 − 𝑉! = 0.7 + 5.35 = 6.05 𝑉 > 𝑉5!,=>&
gura (β = 100)
                          Ipotesi verificata; soluzione corretta !!
     VEB,g = 0.7 V
ircuito in figura (β = 100)
                                                           Esercizi
                         Hp.: Regione normale (da verificare poi !!)

                         𝑉? = 𝑅( 𝐼( + 𝑉5(,6 + 𝑅5 (𝛽# + 1)𝐼(
             𝐼5

      𝐼(                          𝑉? − 𝑉5(,6       5 − 0.7
                        𝐼( =                  =                 = 39 𝜇𝐴
                               𝑅( + (𝛽# + 1)𝑅5 10 𝑘 + 101 A 1 𝑘


                         𝐼! = 𝛽# 𝐼( = 3.9 𝑚𝐴

             𝐼!
                         𝑉! = 𝑉@ + 𝑅! 𝐼! = −5 + 10 𝑘 A 3.9 𝑚 = 34 𝑉


rcizi                    NO !! Soluzione assurda. Va oltre le
                         alimentazioni à ipotesi iniziale sbagliata

gura (β = 100)
                     Hp.: Regione di saturazione (da verificare poi !!)
     VEB,g = 0.7 V
                     à rifare i calcoli con la nuova ipotesi
rcuito in figura (β = 100)                                Esercizi
                        Hp.: Regione normale (da verificare poi !!)

                       𝑉? − 𝑅(7 𝐼( + 𝐼8 = 𝑅(8 𝐼8

                       𝑉(5,6 + 𝑅5 (𝛽# + 1)𝐼( = 𝑅(8 𝐼8

                        𝐼( = 12.9 𝜇𝐴       𝐼8 = 92 𝜇𝐴

                        𝐼7 = 𝐼( + 𝐼8 = 104.9 𝜇𝐴

                        𝐼! = 𝛽# 𝐼( = 1.29 𝑚𝐴

                       𝑉! = 𝑉? − 𝑅! 𝐼! = 15 − 5 𝑘 A 1.29 𝑚 = 8.75 𝑉
rcizi                  𝑉( = 𝑅(8 𝐼8 = 50 𝑘 A 92𝜇 = 4.6 𝑉

gura (β = 100)         𝑉!( = 𝑉! − 𝑉( = 4.15 𝑉 > 0

     VBE,g = 0.7 V     Ipotesi verificata; soluzione corretta !!
re il circuito in figura (β = 100)                              Esercizi
                                 Per risolvere l’esercizio, devo:
                                 •   scrivere tutte le equazioni di Kirchhoff alle
                                     maglie e ai nodi per tensioni e correnti
                                 •   utilizzare il modello a soglia per descrivere i
                                     due BJT à ipotesi sullo stato di conduzione
                                     di entrambi i transistor (OFF/attiva/saturaz.)
                                 à molte incognite e molte equazioni
                                 Nota: la parte di sinistra del circuito è quella
                                 dell’esercizio precedente.
                                 Posso riutilizzarne i risultati?
                                 •   In generale no, dovrei rifare i calcoli anche
                                     per la parte di sinistra del circuito
                                 •   Esiste un caso in cui posso riutilizzare il
                                     calcolo à quando Q1 non risente della
rcizi                                presenza di Q2 (considero Q1 come
                                     separato da Q2)
                                 •   Questo avviene quando IB2 << IC1
gura (β = 100)
                                 •   Trascuro IB2 nell’equazione di Kirchhoff alle
                                     correnti sul nodo cerchiato in rosso
     VBE,g = 0.7 V
                                 E’ giustificato?
re il circuito in figura (β = 100)                                  Esercizi
                                      Posso sempre fare un’ipotesi (che poi andrò a
                                      verificare !!) à IB2 << IC1 (Hp1)
                                      à considero Q1 come separato da Q2
                                      à IC1 = 1.29 mA, VC1 = 8.75 V (risultati precedenti)

                                        (Hp2: Q2 ON in reg. attiva)
                                         𝑉? = 𝑉!7 + 𝑉5(,6 + 𝑅5 𝐼58

                                                𝑉? − 𝑉5(,6 − 𝑉!7
                                         𝐼58 =                   =
                                                      𝑅5
                                                15 − 0.7 − 8.75
                                              =                  = 2.77 𝑚𝐴
                                                      2𝑘
izi
                                    𝛽#                               𝐼58
                          𝐼!8 =         𝐼 = 2.75 𝑚𝐴        𝐼(8 =          = 27.5 𝜇𝐴
                                  𝛽# + 1 58                        𝛽# + 1
a (β = 100)
                                                            IB2 << IC1 à Hp1 OK !
  VBE,g = 0.7 V
                     𝑉!8 = 𝑅!8 𝐼!8 = 2.7 𝑘 A 2.75 𝑚 = 8.5 𝑉

                     𝑉!(8 = 𝑉!8 − 𝑉(8 = 𝑉!8 − 𝑉!7 = −0.25 𝑉 < 0          à Hp2 OK !
