---
fonte: "17_pass transistor.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Topologie circuitali alternative al CMOS

                  Francesco Driussi

       Corso di Laurea in Ingegneria Elettronica
 Dipartimento Politecnico di Ingegneria ed Architettura


              francesco.driussi@uniud.it
              www.diegm.uniud.it/driussi


                    Francesco Driussi – 2020
                                                     Famiglie logiche
• Negli anni sono state sviluppate diverse “famiglie” logiche (stili circuitali)
• Storicamente le prime porte logiche si basavano sui diodi
• Successivamente, l’introduzione dei transistor ha spinto lo sviluppo di logiche
  sempre più performanti:
1. Logiche a rapporto (le prime con i transistor: RTL, TTL):
    i. basate su un transistor per ingresso
    ii. realizzate con BJT o con MOSFET
    iii. caratterizzate solo dal pull-up o solo dal pull-down
    iv. consumo di potenza statico non nullo
2. Logiche statiche CMOS:
    i. basate su n-MOSFET e p-MOSFET
    ii. PU e PD complementari
    iii. consumo statico nullo
    iv. alto numero di transistor (N ingressi à 2N transistor)
    v. tempi di ritardo elevati (comportamento dinamico limitato)
3. Logiche alternative ai gate statici CMOS
                Topologie alternative ai gate CMOS
• Sono stati sviluppati anche stili circuitali alternativi per sopperire ai limite delle
  porte logiche statiche CMOS:
1. Logiche a PASS-TRANSISTOR :
    i. abbastanza diffuse
    ii. transistor visto come interruttore
    iii. il segnale passa attraverso il MOSFET (non è più connesso solo al gate del
         transistor)
    iv. eliminano la ridondanza tra PU e PD à minor numero di MOSFET


2. Logiche DINAMICHE CMOS:
    i. eliminano la ridondanza tra PU e PD à minor numero di MOSFET
    ii. mantengono un consumo statico nullo
    iii. si evidenziano due fasi distinte nell’elaborazione del segnale:
         • fase di PRECARICA o PRESCARICA
         • fase di VALUTAZIONE DELL’INGRESSO
                                   Logiche a Pass-transistor
  • Non c’è più il concetto di PU e PD
  • Rete di interruttori + BUFFER (es.: inverter CMOS)




ATTENZIONE: gli ingressi I1,..., In NON SONO CONNESSI SOLO ai gate dei MOSFET
à alcuni ingressi pilotano i gate per accendere i MOSFET e far “passare” altri ingressi
Esempio: schema tipico è quello del MULTIPLEXER (MUX)

                                           Due ingressi + uno di selezione
                                           à solo A oppure B può raggiungere il buffer
                                           à non devono essere mai in competizione
                                             sul nodo di ingresso del buffer
                                     F
                                                         𝐹 = 𝐴 $ 𝑆 + 𝐵 $ 𝑆̅
                             Esempi: XOR, NAND e NOR
                  𝐵
                                           𝐹 = 𝐴 ' 𝐵 + 𝐴̅ ' 𝐵" = 𝐴𝐵 ' 𝐴̅𝐵"

                                   F       𝐹 = 𝐴̅ + 𝐵" ' 𝐴 + 𝐵 = 𝐴̅ ' 𝐵 + 𝐴 ' 𝐵"
                  𝐵"

  𝐴̅                                       𝐹 =𝐴⊕𝐵

Per realizzare la porta XOR bastano 4 MOSFET à molto più efficiente del CMOS in
cui erano necessari 8 MOSFET (4 per il PU e 4 per il PD)

             𝐵

                               F           𝐹 = 𝐴 ' 𝐵 + 0 ' 𝐵" = 𝐴 ' 𝐵
             𝐵"
 0                                                porta NAND

             𝐵"

                               F            𝐹 = 𝐴 ' 𝐵" + 𝐵 ' 𝐵 = 𝐴 ' 𝐵" + 𝐵 = 𝐴 + 𝐵
             𝐵
                                                  porta NOR
                                  Funzionamento delle porte
                𝐵

                                                      𝐹 =𝐴'𝐵+𝐵'0=𝐴'𝐵
                𝐵"                     F
                                                              porta NAND
  0

• Il valore della funzione F dipende dal dato che
  raggiunge l’ingresso dell’inverter, cioè dal valore di X
                                                                              𝑋
• I segnali non devono “competere” per pilotare
  l’inverter
• Il valore di X deve essere determinato da un solo
  percorso alla volta
• Percorsi attivati in modo MUTUAMENTE
  ESCLUSIVO !!
                                                                 Es.: B = 1
à per ogni combinazione di ingressi ho solo un percorso
attivo nella determinazione del valore di X à per studiare
il circuito posso analizzare solo il percorso conduttivo !!
                  Analisi con un solo pass-transistor
            𝐺                            • Il nodo X è caratterizzato da una
                                           capacità CX

            𝐵"                 F         • Se G = “0” à X rimane un nodo isolato

             𝐶!                          • Se G = “1” à trasferisco il dato A su X
                                         • Se A = X = VDD oppure A = X = 0 allora
                                           non succede niente
                                         • I casi interessanti sono con A = VDD e
                                           X = 0 oppure con A = 0 e X = VDD
Caso 1) A = 0 e X = VDD                           G
                                       Vdd
CX si scarica attraverso il
                                                                                 t
MOSFET à esattamente                              A
come nel calcolo di tf dell’       I         Cx
inverter CMOS                                                                    t
                                                  X
à I = 0 quando X = 0
                                                                                 t
                       Analisi con un solo pass-transistor
                 𝐺
                 Vdd
                                       Caso 2) A = VDD e X = 0
Vdd                                    CX si carica attraverso il MOSFET
                 𝐵"            F
           I I                         à caso molto DIVERSO da prima !!
                 𝐶!    Cx
                                       à I = 0 quando VGS ≤ VT à VX = VDD - VT
      Cx
                                       à trasferisco un “1” DEBOLE

                                       1. minore immunità ai disturbi !!

                                       2. effetto body:
 G
                                       𝑉! = 𝑉!" + 𝛾       2𝜓# + 𝑉$% − 2𝜓# =
                                t
 A                                        = 𝑉!" + 𝛾       2𝜓# + 𝑉& (𝑡 = ∞) − 2𝜓#

                                       à nell’inverter ho CONSUMO STATICO di
                                t
 X                                       POTENZA con VX ≤ VDD - VT < VDD - |VTp0|

                                                (p-MOSFET ON !!)
                                   t
                        Pass-transistor complementare
Il trasferimento del “1” debole è un problema non da poco:
• Dovrei usare un pass-transistor con soglia minore di quella dei MOSFET
  dell’inverter CMOS
à soluzione NON OTTIMALE ! (maggiori costi tecnologici; cmq trasferisco “1” debole)
•   Potrei usare un p-MOSFET come pass-transistor à trasferisco uno “0” debole !!

à il problema si ripropone con X = 0

SOLUZIONE: utilizzo dei PASS-TRANSISTOR COMPLEMENTARI



                                                • p-MOSFET si occupa di
                                                  trasferire l’ “1” forte
       𝐴
                                                • n-MOSFET si occupa di
                                                  trasferire lo “0” forte
                           Pass-transistor complementare
Es.: trasferimento del “1” forte:
1. VX ≤ |VTp0| à entrambi i MOSFET sono in saturazione
2. |VTp0| < VX ≤ VDD – VTn(X) à n-MOSFET in saturazione e p-MOSFET in regione triodo
3. VX > VDD – VTn(X) à n-MOSFET spento e p-MOSFET in regione triodo

                                              B


                                                                                t
       𝐷𝑛            𝑆𝑛                       A

   𝐴
                                                                                t
        𝑆𝑝          𝐷𝑝
                                              X
                                             VDD
                                          VDD-VTn                        3

                                                                2
                                         VDD-|VTp|

                                                          1
                           Pass-transistor complementare
Es.: trasferimento dello “0” forte:
1. VX > VDD – VTn0 à entrambi i MOSFET sono in saturazione
2. |VTp(X)| < VX ≤ VDD – VTn0 à p-MOSFET in saturazione e n-MOSFET in regione triodo
3. VX ≤ |VTp(X)| à p-MOSFET spento e n-MOSFET in regione triodo

                                              B


                                                                                t
        𝑆𝑛           𝐷𝑛                       A

   𝐴
                                                                                t
       𝐷𝑝           𝑆𝑝                        X
                                             VDD           1
                                          VDD-VTn
                                                                  2
                                         VDD-|VTp|                          3
MOS + Transmission
Gates:              Gates:
          Pass-transistor complementare
 2-input    multiplexer
   Esempio: MULTIPLEXER           Esempio: XOR

 Gates should be restoring
                                         B



                                     B
                                 !
                                 A

                                         B
                                Utilizza 6 MOSFET
                         28(meglio della soluzione CMOS
                              che utilizza 8 MOSFET)
                           ma c’è una soluzione ancora
                                  più semplice !
                XOR a pass-tran. complementare

                                                     Utilizza solo 4 MOSFET
                                            (molto meglio della soluzione CMOS)




                                       • se A = 1:
                                           • inverter di sinistra realizza 𝑌 = 𝐵"
                                           • pass-transistor di destra spento !

• se A = 0:
   • pass-transistor di destra fa
      passare B à 𝑌 = 𝐵
   • inverter di sinistra non genera                      ̅ + 𝐴𝐵" = 𝐴 ⊕ 𝐵
                                                     𝑌 = 𝐴𝐵
      conflitto !!
                                                 Tempi di commutazione
• L’analisi dinamica nelle logiche a pass-transistor è più complicata rispetto alle
  logiche statiche CMOS
• E’ necessario un approccio approssimato che sia almeno in grado di dare
  indicazioni sui trend:
      • rispetto al dimensionamento                                            𝐵 = 𝑉""
      • in funzione del numero di transistor
Esempio: A = B = VDD                                                                        𝑉#$&
à Tre fasi con n-MOSFET / p-MOSFET:
                                                              𝐴 = 𝑉""
1. saturo / saturo
2. saturo / triodo
3. OFF / triodo
                                                                      𝑉#$%
                                                                                                     𝑉!
FASE 2) |VTp0| < VX ≤ VDD – VTn(VX)                                             𝐵. = 0

                                             *
                                                                                                    𝐶!
     𝑑𝑉&                              𝑉)$'           𝛽+
𝐶!         = 𝛽'   𝑉($' − 𝑉!' 𝑉)$' −              +        𝑉($+ − 𝑉!+ *
     𝑑𝑡                                2             2

     𝑑𝑉&                                          (𝑉& − 𝑉)) )*        𝛽+
𝐶!         = 𝛽'   −𝑉)) − 𝑉!'" (𝑉& − 𝑉)) ) −                       +        𝑉)) − 𝑉& − 𝑉!+ (𝑉& ) *
     𝑑𝑡                                                   2           2
                                             Resistenza equivalente
     𝑑𝑉&                                          (𝑉& − 𝑉)) )*       𝛽+
𝐶!         = 𝛽'       −𝑉)) − 𝑉!'" (𝑉& − 𝑉)) ) −                  +        𝑉)) − 𝑉& − 𝑉!+ (𝑉& ) *
      𝑑𝑡                                               2             2
• Equazione troppo complicata (c’è anche l’effetto Body !)
• Solamente 1 delle 3 fasi da considerare !!
                                                                             𝐵 = 𝑉""
à soluzione approssimata:
SOSTITUISCO IL PASS-TRANSISTOR con una                                                   𝑉#$&
RESISTENZA EQUIVALENTE indipendente
dalle tensioni dei nodi A e X !!                           𝐴 = 𝑉""

              𝑉""
                                                                 𝑉#$%
                                                                                                    𝑉!
                        𝐼+                                                    𝐵. = 0
𝑉""                          𝑉!                                                                    𝐶!

                        𝐼'                    𝑅'(
                                                             1   𝐼& + 𝐼%
                                                               =
                                                            𝑅'( 𝑉"" − 𝑉!
                  0
                                              Resistenza equivalente
• Si può dimostrare che Req dipende poco da VX à Req ≈ costante
à la calcolo quindi nel caso più semplice (𝑉& = 0) à 2 MOSFET saturi (Hp.: l = 0)

                      𝑉))                          𝑉))
  𝑅'( 𝑉! = 0 =                 =
                     𝐼+ + 𝐼'       𝛽+                 𝛽'             *      𝑉""
                                      𝑉($+ − 𝑉!+" * +    𝑉($' − 𝑉!'"
                                   2                   2                           𝑉#$&
                            2𝑉))                                                  𝐼+
  𝑅'( =                                           *
            𝛽+ 𝑉)) − 𝑉!+" * + 𝛽' 𝑉)) − |𝑉!'" |                      𝑉""                0

      𝑉""                                                                         𝐼'
                                                                     𝑉#$%

𝑅'(                 Carica di una capacità tramite una resistenza            0
                    à transitorio esponenziale di carica
        𝑉&                                              𝑡
                               𝑉& = 𝑉)) 1 − exp −
              𝐶!                                      𝑅,- 𝐶&
                    à tempo di carica al 90% dell’escursione vale
                            𝑡.,& = ln 10 ' 𝑅,- 𝐶& ≅ 2.3 ' 𝑅,- 𝐶&
                                          Pass-transistor in serie
In porte logiche complesse spesso troviamo pass-transistor in serie
à il calcolo dei tempo di propagazione sarebbe ancora più complicato à devo
  usare l’approccio approssimato e trovare Req
à tipicamente i pass-transistor sono tutti uguali à stessa Req
à Anche la capacità vista in fondo al pass-transistor è tipicamente la stessa

     𝑅'(       𝑅'(                  𝑅'(
                                                 à Rete di RC distribuite
        𝐶       𝐶                                à posso usare la FORMULA DI
                                     𝐶
                                                   ELMORE
                                                         +         0             +

                                                   𝜏+ = P 𝐶0 ' P 𝑅3 = 𝑅,- 𝐶 ' P 𝑖
                                                         012      312            012
                       2𝑉))
𝑅'( =                                        *
                                                                      𝑛(𝑛 − 1)
        𝛽+ 𝑉)) − 𝑉!+" * + 𝛽' 𝑉)) − |𝑉!'" |               𝜏+ = 𝑅,- 𝐶 '
                                                                         2
                                                          è circa proporzionale a n2
                                                               𝑡.,& ≅ 2.3 ' 𝜏+
                        Dimensionamento pass-transistor
               +(+52)
𝜏+ = 𝑅,- 𝐶 '            con 𝑅,- e C che dipendono dalle dimensioni dei transistor
                 *
          2
à 𝑅,- ∝        e 𝐶 ∝ 𝑊 à 𝑅,- ' 𝐶 circa COSTANTE
          7
à 𝜏+ indipendente dal dimensionamento !! à Scelgo dimensionamento minimo !
Es.: Sn = 1, Sp = e per avere stessa conducibilità di p-MOSFET e n-MOSFET
à stessi tempi di salita e discesa dei nodi

                                +(+52)
𝑡' ≅ 2.3 ' 𝜏+ = 2.3 ' 𝑅,- 𝐶 '      *
                                         à aumenta molto con il numero di MOSFET in serie
es.: con 4 pass-transistor in serie, tp aumenta di 6 volte
• Con n molto alto, il ritardo è molto elevato
à bisogna evitare di avere tanti MOSFET in serie (no percorsi lunghi)
Come lo posso evitare ?
à bisogna spezzare i percorsi lunghi inserendo dei BUFFER !!
es.: percorso da n transistor in serie da spezzare in blocchi da m transistor
à (n/m) blocchi da m transistor + (n/m -1) buffer
                                                      Utilizzo dei buffer
es.: percorso da n transistor in serie da spezzare in blocchi da m transistor
à (n/m) blocchi da m transistor + (n/m -1) buffer
                                             𝑚(𝑚 − 1)
                                𝜏8 = 𝑅,- 𝐶 '
                                                  2

                  𝑛  𝑛                             𝑚(𝑚 − 1) 𝑛  𝑛
   𝑡' ≅ 2.3 ' 𝜏8 ' +   − 1 𝑇9:;;,. = 2.3 ' 𝑅,- 𝐶 '         ' +   − 1 𝑇9:;;,.
                  𝑚  𝑚                                2     𝑚  𝑚

                                          𝑛(𝑚 − 1)   𝑛
                       𝑡' = 2.3 ' 𝑅,- 𝐶 '          +   − 1 𝑇9:;;,.
                                             2       𝑚

                          𝜕𝑡'                𝑛  𝑛
                              = 2.3 ' 𝑅,- 𝐶 ' − * ' 𝑇9:;;,. = 0
                          𝜕𝑚                 2 𝑚


                                              2𝑇9:;;,.
                                    𝑚<'= =
                                              2.3 ' 𝑅,- 𝐶

Si dimostra che in tutti i casi pratici mopt è circa 3 (blocchi al più di 3 MOSFET in serie)
                     Svantaggi dei p.-t. complementari
• L’utilizzo dei pass-transistor complementari è necessario per evitare di trasferire
  segnali «deboli» all’inverter
• Il loro utilizzo però porta anche degli svantaggi:
a. maggior numero di transistor (maggior consumo d’area)
b. è necessario avere tutti i segnali anche in forma negata (devo pilotare i p-MOSFET)
c. aumentano le capacità in gioco (maggior numero di transistor) à aumenta la
   potenza dinamica spesa !!

SOLUZIONE ALTERNATIVA à TRANSISTOR DI RIPRISTINO (elimina il problema
dei segnali «deboli»)
Carica del nodo X:
• a t = 0- à A = VDD; G = 0; X = 0 à F = 1 (VDD)                𝐺
à p-MOSFET spento !                                                 𝑉($
• per t > 0 à G = VDD à il nodo X si carica                               𝑋             𝐹
                                                        𝐴
• Quando 𝑉& > 𝑉>! à F = 0
                                                                              𝐶!
à p-MOSFET si accende ! à aiuta nella carica del nodo X

à carica X anche quando n-MOSFET si spegne !! à 𝑉& = 𝑉)) («1» forte !)
                                           Transistor di ripristino
• L’utilizzo del pass-transistor singolo in combinazione al transistor di ripristino:
a. risolve il problema del «1» debole
b. limita il numero di transistor (meno consumo d’area)
c. non è necessario avere tutti i segnali anche in forma negata
d. teoricamente ho minori capacità in gioco (meno transistor) à meno potenza
   dinamica spesa !!

SVANTAGGIO à il transistor di ripristino funziona anche durante la scarica del
nodo X !!
es.: a t = 0 à A = 0; G = VDD; X = VDD à F = 0
à p-MOSFET acceso !
                                                                   𝐺
à si oppone alla scarica di X
                                                                       𝑉($
à rallenta la scarica                                                        𝑋          𝐹
                                                          𝐴
ATTENZIONE AI DIMENSIONAMENTI !!
                                                                                 𝐶!
à n-MOSFET deve essere più conduttivo del p-MOSFET
altrimenti VX non scende à Sn >> Sp
ma Sn = 1 quindi Sp < 1 à Lp > LMIN à aumenta CX à più potenza spesa (c’è vero vantaggio?)
