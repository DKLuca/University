---
fonte: "5_bipolare.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Transistore bipolare

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                  Struttura del transistore bipolare
Transistore Bipolare – Bipolar Junction Transistor (BJT)
à Si basa su una struttura divisa in tre zone che alternano n-Si e p-Si

                                          Es.: struttura n-p-n
                                          Le tre regioni prendono il nome di:
                                          •   Emettitore (E)
                                          •   Base (B, regione centrale)
                                          •   Collettore (C)


•   La struttura forma due giunzioni pn
•   Se le due giunzioni sono troppo lontane non ho un transistor ma
    semplicemente due diodi
•   Nel BJT le due giunzioni devono essere vicine per poter interagire !!
à LA BASE DEVE ESSERE STRETTA !!
                             BJT: due possibili strutture
Le strutture possibili sono due:

                          transistor npn    transistor pnp




                                 IC
                                                    IC
                            IB                 IB
Simboli elettrici
(la freccia corrisponde
sempre all’emettitore)           IE
                                                    IE
                           BJT: struttura reale e utilizzo
Tipicamente le regioni di collettore, base ed emettitore vengono
realizzate verticalmente

• L’area attiva del dispositivo è
  definita dall’area di emettitore
• Il BJT funziona polarizzando le due
  giunzioni:
    • giunzione base-emettitore (BE)
    • giunzione base-collettore (BC)
                                                  area attiva


                                     A seconda del valore e polarità delle
                                     tensioni applicate avremo diverse
                                     modalità (regioni) di funzionamento:
                                     à 4 possibili combinazioni per le
                                              tensioni VBE e VBC
Per far “funzionare” il transistor occorre polarizzare le due giunzioni base-emettitore e base-
collettore;
                                 BJT: regioni di funzionamento
 Vi sono quattro possibili modi di realizzare queste polarizzazioni:


                                                                      o
                                                                   Regione
                                                                                     circuiti analogici
                                                                                 Amplificatore
                                                                                     Interruttore
                                                                                       circuiti digitali
                                                                                     (elec. digitale)

                                                                                 In realtà non si usa


                             • Come
Le tensioni da applicare al BJT  pervedremo,     il principio di funzionamento
                                       la polarizzazione           in una delle del BJT  prevede
                                                                                     regioni   di
                               che l’emettitore “emetta” elettroni e il collettore li “raccolga”;
funzionamento dipende dalla struttura       (verso) delle giunzioni BE e BC
                        • il principio costruttivo di un transistor planare permette di
                          ottimizzare la raccolta degli elettroni da parte del collettore;
                        • Questo però comporta che i ruoli dell’emettitore e del
Transistor npn à es.: regione    attiva
                          collettore  non (normale)       VBE > 0, V
                                          siano più interscambiabili,    BC <il 0
                                                                       quindi     (VCB > 0)
                                                                                modo
                          “attivo-inverso” non è il modo più efficiente di utilizzare il BJT
      Transistor planare

Transistor
    Claudio Luci –pnp     àdi es.:
                  Laboratorio Segnali regione      attiva
                                      e Sistemi– Capitolo 3 (normale) VBE < 0 (VEB > 0), VBC > 10
                                                                                                0
                                                              Polarizzazione attiva: VBE > 0 ; VCB > 0 (BJT n
                                        Regione             attiva         o   normale
                                      Ipotesi (accademica): base “larga” e con drogaggio simile a quello
                               Non sidihanno
La tipicità del transistor è •quella           interazioni
                                         generare          tra levalvola,
                                                     l’effetto    due giunzioni;
                                                                          il quale si
                             • il dispositivo
ottiene polarizzandolo in regione             si comporta come una coppia di diodi; il diodo ba
                                       normale/attiva
                            direttamente ed il diodo base-collettore polarizzato inversamen
Es.: npn à VBE > 0, VBC•< Gli0 (V CB > 0)
                                elettroni iniettati dall’emettitore nella regione di base si rico
                            contribuendo alla corrente di base, mentre in prossimità della g
• Se la base del transistor fosse  larga, ledidue
                            concentrazione           giunzioni
                                                elettroni        non interagirebbero!
                                                          è praticamente   nulla.
• il BJT si comporta come una
  coppia di diodi;
à BE polarizzata direttamente
à BC polarizzata inversamente
1.Elettroni diffondono da E in B
  e ricombinano con le lacune                                    n                       p      n
2.Lacune diffondono da B in E
  e ricombinano con gli elettroni
                                                                     >0                                     >0
3.Vicino alla giunzione BC, la                            -      +                                  -   +
  carica libera è praticamente
  nulla.                              Claudio Luci – Laboratorio di Segnali e Sistemi– Capitolo 3

         IE = IB; IC ≅ 0                         NON HO UN TRANSISTOR !
                                    • la giunzione BC è polarizzata inversamente (campo elet
                                                                          Effetto valvola
                                       quindi gli elettroni presenti nella base (cariche minorita
                                       e arrivano al collettore
L’effetto valvola si ottiene quando •laBase
                                        base    è «stretta»
                                              poco  drogata à (<quasi µm)tutti gli elettroni provenien
                                       collettore (per minimizzare l’effetto Early, il collettore ha un droga
à le due giunzioni interagiscono !

a) BE polarizzata direttamente
à IE elevata
à inietta elettroni da E a B
b) BC polarizzata inversamente
à c’è un forte campo elettrico ai
  capi della giunzione BC che
  spinge i minoritari di B e C
à elettroni iniettati da E in B
  catturati dal campo e sparati
  dentro il collettore !                               Claudio Luci – Laboratorio di Segnali e Sistemi– Capitolo 3

TRANSISTOR IDEALE à tutti                     Effetto valvola: BE pilotata attraverso i
gli elettroni iniettati da E                  terminali B e E à ottengo una corrente sul
                                              terzo terminale C à VBE pilota IC
raggiungono C à IE ≅ IC
                                                               HO IL TRANSISTOR !
                            • la giunzione BC è polarizzata inversamente (campo elet
                              quindi gli elettroni presenti nella base (cariche minorita
                             Corrente di base e sua origine
                              e arrivano al collettore
                            • Base poco drogata à quasi tutti gli elettroni provenien
TRANSISTOR IDEALE à IE costituita da soli
                              collettore (perelettroni
                                              minimizzareche     raggiungono
                                                          l’effetto Early, il collettore tutti
                                                                                         ha un C
                                                                                               droga
IE = IC ⇒ IB = 0

TRANSISTOR REALE:
1. BE polarizzata in diretta:
•   elettroni diffondono da E a B
•   lacune diffondono da B a E
à le lacune non partecipano
  all’effetto valvola à corrente IB
à EFFICIENZA DI EMETTITORE


2. elettroni iniettati in B possono               Claudio Luci – Laboratorio di Segnali e Sistemi– Capitolo 3

   ricombinare!                                               IB > 0 ⇒ IC < IE
à genera un moto di lacune che                              IC = aF IE , aF < 1
  che contribuisce a IB
à FATTORE DI TRASPORTO IN
                                                        aF guadagno di corrente
  BASE                                                          di base comune
                            • la giunzione BC è polarizzata inversamente (campo elet
                              quindi gli elettroni presenti nella base (cariche minorita
                         Riduzione della corrente di base
                              e arrivano al collettore
                            • Base poco drogata à quasi tutti gli elettroni provenien
IB à corrente indesiderata à collettore
                              come ridurla?
                                         (per minimizzare l’effetto Early, il collettore ha un droga


1. Limitare il flusso di lacune che
   diffondono da B a E
à base con basso drogaggio !
à cresce l’efficienza di emettitore


     ND(E) ≫ NA(B) ≫ ND(C)

                  (vedremo poi perchè)

2. Limitare la ricombinazione
                                                  Claudio Luci – Laboratorio di Segnali e Sistemi– Capitolo 3
   degli elettroni in base
à base molto stretta !
                                                         aF = 0.98 ÷0.995
à aumenta il fattore di trasporto
  in base
                                                            Effetto di VCB
cosa fa VCB?                            3/3          Click
                                                       BJT:to edit Mas
                                                            relazione tr
à VCB > 0, BC in inversa
à Nella giunzione BC il campo
  elettrico va sempre da C a B
à la modulazione del campo                                  !
                                                            E
  elettrico con VCB non ha                                             !                  t
                                                                       E
  effetto visto che comunque                                                              t
  tutti (o quasi tutti) gli elettroni                                                     L
  raggiungono il collettore
à IC indipendente da VCB
à IC dipende solo da IE e quindi
  da VBE                                       •   Ricaviamo IC in funzione di IB:

                                                                + IC )I = −(1− α F )I E
                                                   I B =I −(I=E a
                                                        C         F E
                                                             IB
                                              →aIFE ==−0.98 ÷0.995
                                                        1− α F
                                          Modello di Ebers-Moll
Serve un modello per quantificare le correnti nel BJT e capirne il funzionamento
• Le due giunzioni viste come due diodi
• La corrente di collettore è proporzionale a quella nella giunzione BE

          IC = aF IE
• La strutture è teoricamente simmetrica (npn) à possibilità eventuale di
  funzionare con polarizzazioni opposte à regione attiva inversa (non utilizzata)
• Modello completo che funzioni per ogni regione di funzionamento

                                                           In realtà, drogaggi di
                                                           E, B e C molto diversi
                                                           à struttura non
                                                              simmetrica
                                                           à parametri molto
                                                              diversi
                                                                 aR < aF

                                                           aR ≪ 1 (0.1 ÷ 0.4)
         Modello di Ebers-Moll


                                        IR



IF   Modello di Ebers-Moll a 4 parametri:
     1. IES corrente inversa di saturazione BE
     2. ICS corrente inversa di saturazione BC
                             3. aF
                             4. aR

                              IB = IE - IC
                              Dipendenza dalle tensioni




Tendenzialmente le correnti dipendono da entrambe le tensioni
applicate
IE = f(VBE, VBC)
                                                           IB = IE - IC
IC = f(VBE, VBC)
à in regione normale/attiva IR = 0 àIE = IF ; IC = aFIF à dipendono
  solo da VBE

       COMUNQUE IL MODELLO FUNZIONA PER
      QUALUNQUE REGIONE DI FUNZIONAMENTO
                                          Caratteristiche statiche
In regione normale/attiva (VCB > 0):            In regione di saturazione (VCB < 0):
IE = IF                                         IE = IF - aRIR
IC = aFIF = aFIE                                IC = aFIF - IR = aFIE - (1- aRaF)IR

                                                   Caratteristica di uscita


Trans-caratteristica in regione normale
                                            Modello semplificato
       𝛼!                     𝛽!
𝛽! =                   𝛼! =             bF guadagno di corrente di emettitore comune
     1 − 𝛼!                 1 + 𝛽!
          𝛼"                    𝛽"
𝛽" =                   𝛼" =                                  IB = IE - IC
        1 − 𝛼"                1 + 𝛽"

            𝛽"      1 + 𝛽!     𝛽"
𝐼# = 𝐼! −       𝐼 =        𝐼 −    𝐼 = 1 + 𝛽! 𝐼$# − 𝛽" 𝐼$%
          1 + 𝛽" " 1 + 𝛽! ! 1 + 𝛽" "

         𝛽!               𝛽!        1 + 𝛽"
𝐼% =          𝐼! − 𝐼" =        𝐼! −        𝐼 = 𝛽! 𝐼$# − 1 + 𝛽" 𝐼$%
       1 + 𝛽!           1 + 𝛽!      1 + 𝛽" "

          𝐼!     𝐼#&      𝑉$#                𝑉$#
𝐼$# =         =       𝑒𝑥𝑝     − 1 = 𝐼$#& 𝑒𝑥𝑝     −1
        1 + 𝛽! 1 + 𝛽!     𝑉'(                𝑉'(

        𝐼"     𝐼%&      𝑉$%                𝑉$%
𝐼$% =       =       𝑒𝑥𝑝     − 1 = 𝐼$%& 𝑒𝑥𝑝     −1
      1 + 𝛽" 1 + 𝛽"     𝑉'(                𝑉'(

                                    𝑉$#                  𝑉$%
𝐼' = 𝛽! 𝐼$# − 𝛽" 𝐼$% = 𝛼! 𝐼#& 𝑒𝑥𝑝       − 1 − 𝛼" 𝐼%& 𝑒𝑥𝑝     −1
                                    𝑉'(                  𝑉'(
                                          Modello a 3 parametri
                                     𝑉$#                  𝑉$%
 𝐼' = 𝛽! 𝐼$# − 𝛽" 𝐼$% = 𝛼! 𝐼#& 𝑒𝑥𝑝       − 1 − 𝛼" 𝐼%& 𝑒𝑥𝑝     −1
                                     𝑉'(                  𝑉'(
𝛼! 𝐼"# = 𝛼$ 𝐼%# = 𝐼#      à Condizione di reciprocità
                                                        𝐼&
            𝑉'"       𝑉'%
𝐼& = 𝐼# 𝑒𝑥𝑝     − 𝑒𝑥𝑝
            𝑉&(       𝑉&(

𝐼# = 1 + 𝛽! 𝐼$# − 𝛽" 𝐼$% = 𝐼' + 𝐼$#

𝐼% = 𝛽! 𝐼$# − 1 + 𝛽" 𝐼$% = 𝐼' − 𝐼$%

𝐼' = 𝛽! 𝐼$# − 𝛽" 𝐼$%

 Modello di Ebers-Moll a 3 parametri:
 1.    IS corrente inversa del BJT
 2.    bF (10 ÷ 300)
 3.    bR (1 ÷ 3)
                Configurazione ad emettit. comune
Spesso usato in configurazione emettitore comune:
•   Base terminale di ingresso
•   Collettore terminale di uscita
•   Emettitore riferimento di tensione (terminale comune ad ingresso ed uscita)
Regione NORMALE/ATTIVA à BC in inversa; IBC = 0

𝐼" = 𝐼& + 𝐼'" = 1 + 𝛽! 𝐼'" = 1 + 𝛽! 𝐼'

𝐼% = 𝐼& = 𝛽! 𝐼'" = 𝛽! 𝐼'

𝐼' = 𝐼" − 𝐼% = 𝐼'"

Le tre correnti sono tutte PROPORZIONALI !!
            𝑉./                       𝐼,                 𝛽2 + 1
𝐼, = 𝐼- 𝑒𝑥𝑝                      𝐼. =               𝐼/ =        𝐼,
            𝑉01                       𝛽2                   𝛽2

Corr. di uscita >> corrente di ingresso (cmq correlate) à AMPLIFICATORE
           Caratteristiche statiche E comune
            𝑉./
𝐼, = 𝐼- 𝑒𝑥𝑝
            𝑉01
     𝐼,
𝐼. =
     𝛽2


                             La tensione del terminale
                             di uscita adesso è riferita
                             all’emettitore à VCE

                               𝑉,/ = 𝑉,. + 𝑉./
                         BJT ON: BE in diretta à VBE ≅ 0.6 V

                           Caratteristica di uscita IC = f(VCB)
                                traslata di circa 0.6 V
                                Regioni di funzionamento
Regione INTERDIZIONE à Giunzioni spente; correnti nulle !! BJT OFF

                               𝐼,
BJT ON à Definizione:    ℎ2/ =
                               𝐼.

Regione NORMALE/ATTIVA à Le tre correnti sono PROPORZIONALI !!
                                            𝐼,
  𝐼% = 𝐼& = 𝛽! 𝐼'" = 𝛽! 𝐼'             ℎ2/ = = 𝛽2
                                            𝐼.
Regione SATURAZIONE à Giunzioni in diretta; IBE > 0, IBC > 0 !!

 𝐼% = 𝛽! 𝐼'" − 1 + 𝛽$ 𝐼'% = 𝐼& − 𝐼'%
                                          Rispetto alla regione normale,
 𝐼' = 𝐼'" + 𝐼'%                               IC cala e IB cresce !!

                                  𝐼,
                             ℎ2/ = < 𝛽2
                                  𝐼.
                                        Regione di saturazione
        𝐼,                   Regione normale à Amplificazione del segnale
   ℎ2/ = < 𝛽2
        𝐼.                  Quantitativamente quando entro in saturazione?
                                       Di quanto deve calare hFE?
Regione normale à s = 1                             ℎ2/
                                                 𝜎=
Regione saturazione à s < 1                         𝛽2
Si può imporre un criterio
                                                                 1 + 𝛽"        𝑉
es.: s ≤ sSAT = 0.8 à in saturazione                   𝛽! 1 −           𝑒𝑥𝑝 − %#
                                                  𝐼%               𝛽"          𝑉'(
                                             ℎ!# = =
                                                  𝐼$             𝛽         𝑉
                                                              1 + ! 𝑒𝑥𝑝 − %#
                                                                 𝛽"        𝑉'(
                    𝜎&*+ 𝛽! + 𝛽" + 1
 𝑉%#,&*+ = 𝑉'( ln
                      (1 − 𝜎&*+ )𝛽"                         1 + 𝛽"       𝑉
                                                         1−        𝑒𝑥𝑝 − %#
                                                              𝛽"         𝑉'(
                                                    𝜎=
Non dipende dal livello di corrente !!                        𝛽        𝑉
                                                          1 + ! 𝑒𝑥𝑝 − %#
Quando VCE cala sotto VCE,SAT il BJT è saturo                 𝛽"       𝑉'(


         𝑽𝑪𝑬,𝑺𝑨𝑻 ≅ 𝟎. 𝟏 ÷ 𝟎. 𝟐 𝑽
      Effetti di non idealità del BJT

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                             Effetto Early
BJT ideale in regione normale à IC dipende
solo da IB (non da VCB)
                               𝐼, = 𝛽2 𝐼.


In realtà, lieve dipendenza lineare
di IC da VCE

 EFFETTO EARLY
                                        Origine dell’Effetto Early
Qual è l’origine dell’Effetto Early?                                         WB

Hp: sfrutto le concentrazioni di portatori per le
giunzioni all’equilibrio:
à nella base, n dipende dal potenziale
                     𝑛!"     𝑉$%
             𝑛 𝑥=0 =     𝑒𝑥𝑝
                     𝑁#      𝑉&'
                                                                                           x
                         𝑛!"     𝑉$(                                   x=0        x=WB
            𝑛 𝑥 = 𝑊$   =     𝑒𝑥𝑝
                         𝑁#      𝑉&'                ipotizzo calo lineare di n lungo la base !
                                                    à CORRENTE DI DIFFUSIONE
                𝑑𝑛
    𝐼' = −𝑞𝐴𝐷,      =
                 𝑑𝑥
             𝑛-.        𝑉$#       𝑉$%
    = 𝑞𝐴𝐷,          𝑒𝑥𝑝     − 𝑒𝑥𝑝
           𝑊$ 𝑁*        𝑉'(       𝑉'(
                           𝑛-.                      La corrente di saturazione del BJT è uno
                𝐼& = 𝑞𝐴𝐷,
                          𝑊$ 𝑁*                     dei parametri del modello di Ebers-Moll
                                                    à dipende dalla larghezza della base
                                                    à base più stretta, corrente più alta
                                       Origine dell’Effetto Early
               𝑑𝑛                                          WB
   𝐼' = −𝑞𝐴𝐷,      =
                𝑑𝑥
            𝑛-.        𝑉$#       𝑉$%
   = 𝑞𝐴𝐷,          𝑒𝑥𝑝     − 𝑒𝑥𝑝
          𝑊$ 𝑁*        𝑉'(       𝑉'(
                         𝑛-.
              𝐼& = 𝑞𝐴𝐷,
                        𝑊$ 𝑁*
                                                     x=0        x=WB   x




L’aumento della tensione VCB
allarga la regione svuotata della
giunzione BC
à si “mangia” parte della base
à la base diventa più stretta
à il profilo di n diventa più ripido
à aumenta la corrente di diffusione
à Nella formula WB è più basso,
  quindi IS è più alto
                                        Modellare l’Effetto Early
Come includo l’effetto Early nel modello di Ebers-Moll?
• Dipendenze di IS da WB e di WB da VCB sono complicate
• Sperimentalmente, le caratteristiche in regione lineare dipendono linearmente da
  VCB (e quindi da VCE)
• Le caratteristiche a varie IB hanno un’unica intercetta sull’asse x à -VA
• VA è detta tensione di Early (= 10 ÷ 200 V)
                    𝑉./            𝑉,.          𝑉./                  𝑉,/
        𝐼, = 𝐼- 𝑒𝑥𝑝             1+     ≅ 𝐼- 𝑒𝑥𝑝                   1+
                    𝑉01             𝑉A          𝑉01                   𝑉A

Di solito VCB ≫ VBE
à VCE ≅ VCB
Se VCE è piccolo
à saturazione;
l’effetto Early non è
importante
                              Proporzionalità tra le correnti
In regione normale, le correnti sono ancora proporzionali?
• Se cresce VCB, aumenta IC ma non IB
• Se fisso la tensione VCB (o VCE) lo sono ancora.
• A vari valori di VCB il coefficiente di proporzionalità cambia

                 𝑉./              𝑉,.          𝑉./                    𝑉,/
     𝐼, = 𝐼- 𝑒𝑥𝑝               1+     ≅ 𝐼- 𝑒𝑥𝑝                     1+
                 𝑉01               𝑉A          𝑉01                     𝑉A

                                                                     𝐼% 𝑎 𝑉%$ = 0
 Definiamo bF0 il guadagno di corrente a VCB=0
 à quando non c’è effetto Early
 à 𝐼% = 𝛽!/ 𝐼'

                  𝑉,.
  𝐼, = 𝐼. 𝛽2E 1 +
                   𝑉A

                            𝜷𝑭
                                          Limitare l’Effetto Early
• L’effetto Early è un effetto di non idealità, sgradito
• Vorrei che IC dipendesse solo da VBE e non da VCB
Come limitarlo?
• Devo limitare l’estensione della regione di svuotamento nella base
• L’estensione della regione di svuotamento dipende dal drogaggio
à Alto drogaggio di base riduce Wdep
E per il collettore?
La giunzione BC lavora in inversa, tensione di breakdown deve essere alta
à Basso drogaggio di collettore aumenta VBK
à Drogaggi asimmetrici, giunzione asimmetrica
                                         Ottimizzazione del BJT
  • Drogaggio di emettitore (es: ND=1020 cm-3) ≫ drogaggio di base (es: NA=1018 cm-3)
    à migliora efficienza di emettitore
  • Base stretta à migliora fattore di trasporto in base à IB bassa; IS alta
  • Drogaggio di base ≫ drogaggio di collettore à limita effetto Early; mantiene alta
    la tensione di breakdown
  • Basso drogaggio di collettore può aumentare le resistenze serie à strati sepolti
    ad alto drogaggio (limitano le cadute di tensione nel substrato)


Tale schema permette di
realizzare l’emettitore per
ultimo à più drogato
Substrato di tipo p-Si
à Si crea anche una
                                                                               ND=1020 cm-3
  giunzione tra C e substrato
à mantenuta all’equilibrio
                                                              NA=1015 cm-3
à garantisce isolamento della
  struttura
                                  Effetti reattivi del BJT
Come per i diodi, le giunzioni del BJT presentano effetti reattivi
à impattano le prestazioni dinamiche del BJT à accensione e
spegnimento non istantanei à carica e scarica di capacità

1. Giunzione BC polarizzata in inversa à Capacità di giunzione

Capacità non lineare dovuta alla carica spaziale à capacità
differenziale                            Si-p     RCS       Si-n

                                          RQN                   RQN
          𝑑𝑄G             1
    𝐶., =      = 𝐶HE
          𝑑𝑉,.
                           𝑉,.                    U(x)          qND
                        1− Φ                              B
                             H
                                                                    x
                                                 A
                                                         qNA

                                           -xp    E(x)
                                                               xn
                            Tempo di transito in base

2. Giunzione BE polarizzata in diretta à Capacità di diffusione

Capacità non lineare dovuta alla carica mobile dentro la base à
capacità differenziale                           𝑑𝑄.
                                          𝐶./ =
     WB                                         𝑑𝑉./
                       𝑊' 𝑛01     𝑉'"       𝑉'%
               𝑄' = 𝑞𝐴        𝑒𝑥𝑝     − 𝑒𝑥𝑝
                       2 𝑁2       𝑉&(       𝑉&(
                                                           𝑄' = 𝜏! 𝐼&
                          𝑛01      𝑉'"       𝑉'%
               𝐼& = 𝑞𝐴𝐷3       𝑒𝑥𝑝     − 𝑒𝑥𝑝
                         𝑊' 𝑁2     𝑉&(       𝑉&(

                                                       𝑊'1    𝑊'1
            𝜏3 à tempo di transito in base        𝜏! =     =
                                                       2 𝐷3 2 𝑉&( 𝜇3

       𝑑𝑄.   𝜏2 𝑑𝐼0 𝜏2 𝐼0   𝜏2 𝐼,
 𝐶./ =     =       ≅      ⟹       IN REGIONE NORMALE/ATTIVA
       𝑑𝑉./ 𝑑𝑉./     𝑉01     𝑉01
                                                       Transistore pnp
Struttura pnp duale rispetto alla struttura npn:
• Regioni di funzionamento definite dalle stesse tensioni ma
   con polarità opposta (es.: regione attiva à VBE<0, VBC>0)
• Funzionamento: lacune iniettate da E raggiungono C
• Versi delle correnti convenzionalmente opposti !!
• Modello di Ebers-Moll: giro i versi dei diodi, delle tensioni e
  delle correnti
                                                                         IC
                                                                    IB



                                                                         IE
               Transistore pnp in regione normale


Struttura pnp duale rispetto alla struttura npn:
• Regione attiva à VBE<0, VBC>0
• Correnti proporzionali tra loro
• Nei modelli utilizzo le tensioni opposte: VEB>0,
  VCB<0, VEC
                                                                   IC
                                                              IB



                                                                   IE

            𝑉/.          𝑉.,          𝑉/.               𝑉/,
𝐼, = 𝐼- 𝑒𝑥𝑝           1+     ≅ 𝐼- 𝑒𝑥𝑝                1+
            𝑉01           𝑉A          𝑉01                𝑉A
                               I!"
   𝐼, = 𝛽2 𝐼. = 𝛽2E𝐼.       1+
                               I#
/4      Clickdati
      Alcuni  to edit  Master del
                  caratteristici title2N2222A
                              Data     style
                                    sheet del BJT
                        Se li superate rompete il transistor




     (IS)




            hFE ≅ β F

            hFE ≠ hfe
