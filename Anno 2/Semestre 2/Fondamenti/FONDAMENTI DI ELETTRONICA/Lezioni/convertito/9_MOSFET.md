---
fonte: "9_MOSFET.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Transistore MOSFET

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                                      MOSFET vs. BJT
Transistore Bipolare
•   Presenta una corrente di base IB
•   Nell’inverter RTL ho corrente di ingresso à consumo di potenza alla porta di
    ingresso = VI IB
•   Inoltre, IB impatta su fan out e direttività !!


MOSFET: Metal-Oxide-Semiconductor Field-Effect-Transistor

                               struttura                  funzionamento

•   Anche se storicamente è stato inventato prima, il suo sviluppo è avvenuto
    dopo il BJT per motivi tecnologici
•   Nelle porte logiche permette di annullare la corrente di ingresso (vantaggio!)
•   Consente una miniaturizzazione (scaling) più spinta
à riduzione di costi e aumento complessità sistemi digitali
à aumento velocità e prestazioni
    struttura                                   Struttura MOS
     Il transistor si basa sulla struttura Metal-Oxide-Semiconductor
a
                                                gate

Si                                             substrato
o                                              (n-Si o p-Si)




) Somiglia ad un condensatore à Metal-Insulator-Metal (MIM)
                                   Condensatore MIM
Analisi elettrostatica del condensatore à legge di Gauss
                                s densità superficiale di carica sul
                                  piatto del condensatore

                                E campo elettrico à costante
                                      dentro l’isolante

                                Y potenziale à legge di Poisson
                                       (integro il campo elettrico)
                                à La carica si distribuisce sulla
                                  faccia del metallo: campo nullo e
                                  potenziale costante dentro il
                                  metallo
         Y                      à Il potenziale varia linearmente
                                  all’interno dell’ossido (E costante)
     𝑑                          à capacità per unità d’area C = e / d
 𝑉=𝜎
     𝜀                          à C costante, indipendente dalla
                  d      x        tensione applicata V
                                              Condensatore MOS



• Tensione applicata tra gate e substrato induce carica sulle due armature
• Il semiconduttore ha carica libera limitata !
• Neutralità nel semiconduttore garantita dalla carica fissa del drogante
                                                                    13
                                                                          !
Come accumulo carica nel substrato?
à Carica libera dipende dal potenziale nel materiale !
All’equilibrio abbiamo:
                                    n0, p0: concentrazioni dove 𝜓 = 0
                    𝜓
      𝑛 = 𝑛! 𝑒𝑥𝑝
                   𝑉"#             Ilpongo
                                       sistema
                                           𝜓 = 0 MOS    a duenel
                                                 in profondità terminali
                                                                 substrato, lontano
                                                      dall’ossido
                   𝜓
     𝑝 = 𝑝! 𝑒𝑥𝑝 −
                  𝑉"#               es.: substrato p-Si à n0 = ni2/NA; p0 = NA


• Analisi elettrostatica del condensatore à legge di Gauss/Poisson
istema MOS a due terminali
                                        Tensione di flat-band
          GATE                         z = 0 à interfaccia ossido-semiconduttore
z=-Tox
                                       z = -Tox à interfaccia ossido-metallo
                                       Tox à spessore dell’ossido
z=0                         V
      z                                Metallo e semiconduttore sono materiali
                                       diversi:
                                       à hanno funzioni lavoro diverse
          BULK
                                       à si crea un dipolo tra metallo e substrato
                                       à condensatore già carico per V = 0

Esiste una tensione V per la quale la carica nel condensatore è nulla
à TENSIONE DI FLAT-BAND VFB (tensione di banda piatta)
Substrato p-Si à VFB < 0
Substrato n-Si à VFB > 0

Carica per unità d’area sul condensatore Q = f(V - VFB)
à condensatore anomalo
istema MOS a due terminali
                                 Carica nel condensatore MOS
              GATE                    Q = f(V - VFB) à condensatore anomalo
z=-Tox

                                      V > VFB à metallo carico positivamente
z=0                               V           à substrato (bulk) carico negativam.
      z
                                      V < VFB à metallo carico negativamente

              BULK
                                               à substrato (bulk) carico positivam.


                                      poniamo Y = 0 in profondità nel substrato
          carica nel substrato        substrato p-Si à n0 = ni2/NA; p0 = NA

      𝜌 = 𝑞(𝑝 − 𝑛 − 𝑁'()
                                      V > VFB à n cresce; p cala à Y aumenta
                       𝜓              V < VFB à n cala; p cresce à Y cala
           𝑛 = 𝑛! 𝑒𝑥𝑝
                      𝑉"#
                                      ANCHE NEL SUBSTRATO HO UNA CADUTA
                         𝜓            DI POTENZIALE !!
           𝑝 = 𝑝! 𝑒𝑥𝑝 −
                        𝑉"#           (non solo nell’ossido come nel MIM)
istema MOS a due terminali
                          Carica positiva nel substrato
uiti Elettronici                                                      Il sistema MOS
                   GATE                 carica nel substrato
  z=-Tox
                                       𝜌 = 𝑞(𝑝 − 𝑛 − 𝑁'()

  z=0                         Per V < VFB la carica positiva nel substrato è data
                          V   dall’aumento del numero di lacune
        z                     à accumulo di lacune in prossimità dell’interfaccia
                                 Regione di accumulo
                                ossido-semiconduttore
                   BULK       à incremento delle lacune dato dai fenomeni di
                                generazione/ricombinazione delle coppie
                                elettrone-lacuna
                              à comportamento simile al MIM
                              à ma è necessaria una variazione del potenziale
                                nel substrato (p dipende da Y)
                                                                       𝜓
                                                         𝑝 = 𝑝! 𝑒𝑥𝑝 −
                                                                      𝑉"#
                              à caduta di potenziale anche nel semiconduttore

                                        Il MOS è in ACCUMULAZIONE
istema MOS a due terminali
uiti Elettronici   Carica negativa nel substrato
                                             Il sistema


                                  carica nel substrato
 z=-Tox
                                 𝜌 = 𝑞(𝑝 − 𝑛 − 𝑁'()

 z=0                    Per V > VFB n cresce; p cala
                    V   • p cala à lascia scoperti ioni di drogante carichi
       z
                         Regione      di svuotamento
                          negativamente
                        • la carica negativa nel substrato è data da
                          - carica mobile       𝜌$%& = −𝑞𝑛

                          - carica fissa      𝜌' = 𝑞(𝑝 − 𝑁())

                               𝜌(𝑧) = 𝜌-./ (𝑧) + 𝜌0 (𝑧)

                        à zona svuotata di lacune vicino all’interfaccia
                           ossido-semiconduttore: REGIONE SVUOTATA
                        se rINV << rD à il MOS è in SVUOTAMENTO !!
                        non c’è carica libera vicino all’interfaccia ossido-Si
                      Potenziale nel condensatore MOS

• Nell’ossido caduta di potenziale con
  profilo lineare (come nel MIM)
• Caduta di potenziale nel substrato
• n e p dipendono esponenzialmente da Y
Per VG > VFB
• n e p variano fortemente
à n cresce esponenzialmente all’interfac.
     (elettroni schiacciati all’interfaccia)
à p cala esponenzialmente nella regione
   di svuotamento
Hp.: NA costante nel substrato à carica
fissa costante nella zona di svuotamento
WD = estensione della zona svuotata
YS = Y(z=0) à potenziale all’interfaccia
                                            Carica totale nel MOS
Quanta è la carica totale accumulata sulle armature del condensatore MOS ?
• QM carica per unità d’area sul metallo
• QS carica per unità d’area nel semiconduttore
Per VG > VFB                                             𝑄* = −𝑄+ = −𝑄' − 𝑄$%&
• QD carica fissa nel semiconduttore à densità di carica di svuotamento
• QINV carica mobile nel semiconduttore à densità di carica di inversione
          %             %                                 %                 %
   𝑄$ = 2 𝜌$ 𝑑𝑧 = 𝑞 2 (𝑝 − 𝑁& )𝑑𝑧                 𝑄'() = 2 𝜌'() 𝑑𝑧 = −𝑞 2 𝑛𝑑𝑧
         !             !                                 !                  !

Nell’ossido ho campo elettrico costante (legge di Gauss) e potenziale lineare lungo z

         𝑄,     𝑄-
   𝐹*+ =     =−
         𝜀*+    𝜀*+
        𝑉*+ 𝑉. − 𝑉/0 − 𝜓-
  𝐹*+ =     =
        𝑇*+      𝑇*+

                    𝑄-      𝑄-
  𝑉. − 𝑉/0 − 𝜓- = −    𝑇 =−
                    𝜀*+ *+  𝐶*+
                                                Capacità dell’ossido
COX capacità per unità d’area dell’ossido à parametro tecnologico molto importante!
à dipende da TOX (dipende da quanto sottile riesco a farlo)                 𝜀*+
                                                                      𝐶*+ =
                                                                            𝑇*+
à eOX= er,SiO2 ∙ e0 = 3.9 e0
                                         𝑄- = −𝐶*+ (𝑉. − 𝑉/0 − 𝜓- )

La carica nel semiconduttore dipende da VG e da COX
à Fissata VG, maggiore è COX, maggiore è la carica indotta nel semiconduttore
à Fissata COX, la carica nel semiconduttore dipende da VG (𝜓- dipende da VG)


V < VFB (𝜓- < 0) à accumulo lacune all’interfaccia ossido semiconduttore à QS > 0
                   à MOS in accumulazione


V > VFB (𝜓- > 0) à si forma carica negativa nel
                            substrato
• carica di svuotamento (fissa) distribuita
         uniformemente su WD
• carica di inversione à elettroni all’interfaccia
                                                              Svuotamento
 V > VFB (𝜓- > 0) à si forma carica negativa nel substrato


 (a) QD >> QINV à MOS in svuotamento
 Quanto vale la carica di svuotamento?
 Hp: rD costante lungo WD; rD = 0 oltre WD


            𝑄' = −𝑞𝑁( 𝑊'


                                                  𝑄-     𝑄$                     𝑞𝑁& 𝑊$
 à Nell’ossido ho F = FOX costante      𝐹*+ = −       ≅−     à   𝐹(𝑧 = 01 ) ≅
                                                  𝜀*+    𝜀*+                      𝜀-2 68
                                          𝑞𝑁&
 à Nella regione svuotata          𝐹(𝑧) ≅     (𝑊$ − z)
                                          𝜀-2
                                                               𝑞𝑁& 3
 se integro trovo il potenziale e in particolare ho       𝜓- =     𝑊
                                                               2𝜀-2 $


di Torino                2𝜀-2 𝜓-
                𝑊$ =                                     𝑄' = − 2𝑞𝑁( 𝜀+, 𝜓+
                          𝑞𝑁&
                                                                    Inversione
V >> VFB (𝜓- > 0) à si forma carica negativa nel substrato


(b) carica di inversione diventa significativa ! non trascurabile
à vicino all’interfaccia ho tanti elettroni e pochissime lacune à come se fosse n-Si
à INVERSIONE del substrato (era p-Si; è diventato n-Si) à MOS in INVERSIONE

All’interfaccia:                          𝜓-                                         𝜓-
                    𝑛- = 𝑛 𝑧 = 0 = 𝑛! 𝑒𝑥𝑝                  𝑝- = 𝑝 𝑧 = 0 = 𝑝! 𝑒𝑥𝑝 −
                                          𝑉"#                                        𝑉"#

Qual è la condizione di passaggio tra SVUOTAMENTO e INVERSIONE ?
Per definizione, il passaggio all’inversione si ottiene quando la concentrazione ns di
elettroni all’interfaccia è pari al valore del doping nel substrato
à nel substrato dovrei avere p = NA, invece trovo ns = NA
In questa condizione il potenziale all’interfaccia vale:

              𝑛,-     𝜓+                                       𝑁(
         𝑁( =     𝑒𝑥𝑝                          𝜓+ = 2 2 𝑉"# ln
              𝑁(      𝑉"#                                      𝑛,
                                                     Tensione di soglia
Concentrazione ns di elettroni all’interfaccia è pari al valore del doping nel substrato
In questa condizione il potenziale all’interfaccia vale:
                                                            per definizione
                                  𝑁(                        quantità che dipende da
                  𝜓+ = 2 2 𝑉"# ln    = 2 2 𝜓.
                                  𝑛,                        parametri tecnologici


Qual è la tensione da applicare per passare da SVUOTAMENTO a INVERSIONE ?
Hp.: 𝑄- ≅ 𝑄$ à ragionevole perchè rINV = rD solo all’interfaccia

                                         𝑄+ ≅ 𝑄' = − 2𝑞𝑁( 𝜀+, 2𝜓. = −𝛾𝐶/0 2𝜓.

                                                                             2𝑞𝑁& 𝜀-2
                                                                       𝛾=
                                                                              𝐶*+

                                          TENSIONE DI SOGLIA
                   𝑄$          𝑄$                                            Dipende da
 𝑉! − 𝑉"# − 𝜓$ = −     𝑇%& = −         𝑽𝑻 = 𝑽𝑭𝑩 + 𝟐𝝍𝑭 + 𝜸 𝟐𝝍𝑭               VFB, NA, COX
                   𝜀%&         𝐶%&                                       parametri di design
                                                     MOS: Regione
                                        Regione di accumulo       di svuot
                                                            riassunto
La tensione VG applicata carica il condensatore MOS (con substrato p-Si)
    ACCUMULAZIONE                       SVUOTAMENTO                  INVERSIONE




                                                                                   VG > VT
      strato di lacune               carica fissa negativa        carica fissa negativa
       all’interfaccia              nella regione svuotata         + strato di elettroni
                                       no carica mobile               all’interfaccia
                                                                37
    𝑉4 = 𝑉/0 + 2𝜓/ + 𝛾 2𝜓/
                                             Nel condensatore MOS con substrato n-Si:
                 𝑁&            2𝑞𝑁& 𝜀-2
   𝜓/ = 𝑉"# ln           𝛾=                  • tensioni con valori opposti
                 𝑛2             𝐶*+
                                             • ruolo di elettroni e lacune scambiati
         Progettabile; dipende da            • carica fissa positiva nella zona svuotata
      parametri tecnologici (NA, COX)
                                              Transistor MOSFET
Il transistor si ottiene aggiungendo al MOS due terminali di SOURCE (S) e DRAIN (D)
con drogaggio opposto al substrato
• Gate (G) controlla corrente tra S e D
• Substrato detto anche bulk o body (B)
• Tra source e bulk e tra drain e bulk ci
  sono due giunzioni pn
• Le due giunzioni non devono essere
   mai mandate in diretta !!
es.: Substrato p-Si; source e drain n-Si
à struttura n-MOSFET
à VSB, VDB ≥ 0 !!
tipicamente:
• VB = 0, VSB = 0 (VS = VB = 0)
• VD utilizzata per indurre una corrente
  nel transistor à VDB ≥ 0, VDS ≥ 0
• tutte le tensioni riferite al substrato e
  source
à VSB, VDS, VGS
                                  MOSFET in accumulazione
Condizioni di funzionamento tipiche nMOSFET: VB = 0, VSB = 0 (VS = VB = 0)
• VGS ≤ VFB, VDS > 0 (per indurre corrente
   IDS tra drain e source)
• Giunzione S-B all’equilibrio, giunzione
  D-B in inversa à corrente IDS = 0 !!

    S                             D
                       B
• La corrente è nulla qualunque sia VDS
• non è come il BJT, perché non mando
  mai in diretta una delle due giunzioni !

• A cavallo delle giunzioni c’è sempre una regione di carica spaziale che induce un
  campo che si oppone alla diffusione
• Se VGS << VFB à accumulo di lacune all’interfaccia ossido-Si à non cambia
  niente ! Il campo blocca la diffusione !!


                                  à MOSFET OFF
                                         MOSFET in svuotamento
Condizioni di funzionamento tipiche nMOSFET: VB = 0, VSB = 0 (VS = VB = 0)


VFB < VGS < VT


• La tensione di gate svuota il substrato
  vicino all’interfaccia ossido-Si
• La regione di svuotamento si estende a
  tutto il silicio che sta tra source e drain !!
• Non c’è carica libera tra S e D !!




 VDS > 0 à La corrente è nulla qualunque sia VDS


                                    à MOSFET OFF
                                            MOSFET in inversione
Condizioni di funzionamento tipiche nMOSFET: VB = 0, VSB = 0 (VS = VB = 0)

VGS > VT


• La tensione di gate è sufficientemente alta
  per invertire il Si all’interfaccia
• Si forma uno strato di elettroni liberi
  all’interfaccia à CANALE
• Si forma un canale n tra S e D !!
• Non ci sono più le giunzioni à connessione
  elettrica tra source e drain


 VDS > 0 à La corrente IDS può scorrere ed in generale dipende da VDS
 à MOSFET ON

    Substrato p-Si à il canale che si forma è fatto da elettroni à canale n
                        MOSFET a canale n à n-MOSFET
    Substrato n-Si à S e D sono p-Si à MOSFET a canale p à p-MOSFET
                                 Effetto valvola nel MOSFET
Condizioni di funzionamento tipiche nMOSFET:
VB = 0, VSB = 0 (VS = VB = 0)

VGS > VT à Inversione à canale tra S e D


• Se aumenta VGS, aumenta anche YS
• Maggiore è la tensione VGS, maggiore è il
  numero di elettroni all’interfaccia
à il canale è più conduttivo
à a parità di VDS, la corrente IDS aumenta !



 La corrente IDS dipende da VGS

 à Effetto valvola nel MOSFET
                                                                      Effetto Body
Condizioni di funzionamento tipiche nMOSFET: VB = 0, VSB = 0 (VS = VB = 0)

    𝑉4! = 𝑉/0 + 2𝜓/ + 𝛾 2𝜓/          (tensione tra gate e substrato che manda in inversione il canale)

VGS = VT à Inversione à canale, source e drain elettricamente connessi !
VDS = 0 à all’interfaccia il potenziale è legato a quelli di source e drain! (YS segue VS)
 Cosa succede se VSB > 0 ?
• Aumenta YS à aumenta la caduta nel semiconduttore
• Si può dimostrare che 𝜓- = 2𝜓/ + 𝑉-0
• La carica di svuotamento e l’estensione della regione di svuotamento aumentano

    𝑄$ = −𝛾𝐶*+ 𝜓- = −𝛾𝐶*+ 2𝜓/ + 𝑉-0                                2𝜀-2 (2𝜓/ + 𝑉-0 )
                                                         𝑊$ =
                                                                          𝑞𝑁&
à Cambia anche la tensione di soglia !!

  𝑉.0,4 = 𝑉/0 + 2𝜓/ + 𝑉-0 + 𝛾 2𝜓/ + 𝑉-0 = 𝑉4! − 𝛾 2𝜓/ + 𝑉-0 + 𝛾 2𝜓/ + 𝑉-0

 𝑉.0,4 − 𝑉-0 = 𝑉4! + 𝛾    2𝜓/ + 𝑉-0 − 2𝜓/ = 𝑉.-,4             ß tensione di soglia riferita al source
                                                             Effetto Body
Tensione di soglia quando VSB = 0 (VS = VB = 0, riferimento S e B identico)

   𝑉4! = 𝑉/0 + 2𝜓/ + 𝛾 2𝜓/

Tensione di soglia quando VSB > 0 (VS > VB = 0)
Effetto Body
• Aumenta la caduta nel semiconduttore 𝜓- = 2𝜓/ + 𝑉-0
• Aumenta la carica di svuotamento e la regione di svuotamento
• Aumenta la tensione di soglia (riferita al source; necessaria per formare il canale)

                    𝑉4 = 𝑉4! + 𝛾       2𝜓. + 𝑉+5 − 2𝜓.


g fattore di Effetto Body (0.3 ÷ 0.5   𝑉)
à può aumentare molto la soglia del MOSFET
à VT dipende da VSB
                                               Carica nel MOSFET
La conducibilità nel MOSFET dipende da quanta carica libera ho nel canale
à IDS dipende da QINV


Come dipende QINV da VGS?
Hp.: VSB =0 à In svuotamento (VFB < VGS < VT0) à QD >> QINV


  𝑄$ = − 2𝑞𝑁& 𝜀-2 𝜓- = −𝛾𝐶*+ 𝜓-                         QINV dipende molto fortemente da YS
                                                        QD dipende più blandamente da YS
       𝑛23     𝜓-                          𝜓-
  𝑛- =     𝑒𝑥𝑝                  𝑄'() ∝ 𝑒𝑥𝑝
       𝑁&      𝑉"#                         𝑉"#



In inversione (VGS > VT) à QINV diventa significativa, confrontabile con QD
Piccole variazioni di YS inducono alte variazioni di QINV à YS inizia a variare poco
à 𝜓- ≅ 2 G 𝜓/ fissato ! à 𝑄$ ≅ −𝛾𝐶*+ 2𝜓/ (costante; WD fisso)
                        Carica di inversione nel MOSFET
                       𝑄$     𝑄'() + 𝑄*
  𝑉!# − 𝑉"# − 𝜓$ = −       =−
                       𝐶%&       𝐶%&

  se VSB = 0

                     𝑄* 𝑄'()                       𝑄'()         𝑄'()
 𝑉!$ = 𝑉"# + 2𝜓" −      −    = 𝑉"# + 2𝜓" + 𝛾 2𝜓" −      = 𝑉+, −
                     𝐶%& 𝐶%&                       𝐶%&          𝐶%&




     𝑄'() = −𝐶*+ 𝑉.- − 𝑉4!


In inversione (VGS > VT)
à QINV è linearmente dipendente da VGS
à QD è costante


si deriva facilmente che se VSB > 0

      𝑄'() = −𝐶*+ 𝑉.- − 𝑉4
                                           Corrente nel MOSFET
VGS < VT à MOSFET OFF
VGS ≥ VT à MOSFET ON
Quanto vale la corrente quando il transistor è acceso? à Dipende dalla carica di canale
• Se il canale è conduttivo è
  elettricamente connesso a S e D
• In inversione, se VS = VD
      𝜓- ≅ 2 G 𝜓/ + 𝑉-0 = 2 G 𝜓/ + 𝑉-
• se VS ≠ VD à YS è legato a VS e VD
à 𝜓- (𝑥 = 0) = 2 G 𝜓/ + 𝑉-0
à 𝜓- (𝑥 = 𝐿) = 2 G 𝜓/ + 𝑉$0
à YS dipende da x !!

       𝜓+ = 2𝜓. + 𝑉+5 + 𝑉(𝑥)

• V(x=0) = 0
• V(x=L) = VDS
• V(x) andamento monotono
à Approssimazione di canale graduale
                             Carica nel canale del MOSFET
YS dipende da x à varia lungo il canale à serie di tanti condensatori MOS con carica
di canale dipendente da x à QINV(x)

                      𝑄'() + 𝑄*
 𝑉!# − 𝑉"# − 𝜓$ = −                                𝐻𝑝. : 𝑄* ≅ −𝛾𝐶%& 2𝜓" + 𝑉$#
                         𝐶%&

                            𝑄* 𝑄'()                                   𝑄'()
 𝑉!$ = 𝑉"# + 2𝜓" + 𝑉 𝑥 −       −    = 𝑉"# + 2𝜓" + 𝑉 𝑥 + 𝛾 2𝜓" + 𝑉$# −
                            𝐶%& 𝐶%&                                   𝐶%&

                     𝑄'()
  𝑉!$ = 𝑉+ + 𝑉 𝑥 −                      𝑄'() (𝑥) = −𝐶*+ 𝑉.- − 𝑉4 − 𝑉(𝑥)
                     𝐶%&



VS < VD à V(x) ≥ 0 à la carica si riduce vicino al drain à canale meno conduttivo !!


In generale: J = - Q(x) ∙ v(x)
• J à corrente per unità di larghezza
• Q à densità di carica per unità d’area
• v à velocità degli elettroni
                                         Modello per la corrente
      𝐼$-
𝐽$- =     = −𝑄'() 𝑥 G 𝑣(𝑥)
      𝑊

𝑄'() (𝑥) = −𝐶*+ 𝑉.- − 𝑉4 − 𝑉(𝑥)

                  𝑑𝑉
𝑣 𝑥 = −𝜇6 𝐸7 = 𝜇6
                  𝑑𝑥
                              𝑑𝑉
𝐼$- = 𝑊𝜇6 𝐶*+ 𝑉.- − 𝑉4 − 𝑉(𝑥)
                              𝑑𝑥

bn‘ = 𝜇6 𝐶*+ à conducibilità intrinseca del MOSFET (indipendente dalle dimensioni L e W)



    8                8                             )!"
                                    𝑑𝑉
   2 𝐼$- 𝑑𝑥 = 𝑊𝛽69 2 𝑉.- − 𝑉4 − 𝑉 𝑥    𝑑𝑥 = 𝑊𝛽69 2     𝑉.- − 𝑉4 − 𝑉 𝑥          𝑑𝑉
    !               !               𝑑𝑥            !


                                     𝛽69                    3
                         𝐼$- G 𝐿 = 𝑊     2(𝑉.- − 𝑉4 )𝑉$- − 𝑉$-
                                     2
                                            Modello per la corrente
          𝑊 𝛽69                    3
     𝐼$- = G    2(𝑉.- − 𝑉4 )𝑉$- − 𝑉$-
          𝐿 2
:
    = 𝑆 à FATTORE DI FORMA
8
bn = bn‘ ∙ S à conducibilità del MOSFET
    (dipende dalle dimensioni del MOSFET)

                             1 -
     𝐼'+ = 𝛽6 (𝑉7+ −𝑉4 )𝑉'+ − 𝑉'+
                             2


• VGS costante à parabola in VDS
• VDS costante à lineare in VGS


      CARATTERISTICA DI USCITA              à


• Punto di massimo in VDS = VGS – VT
• Poi la corrente cala (????)
                     Carica di inversione vicino al drain
Cosa succede in VDS = VGS – VT ? E’ vero che la corrente cala ?

     𝑄'() 𝐿 = −𝐶*+ 𝑉.- − 𝑉4 − 𝑉$- = −𝐶*+ 𝑉.- − 𝑉4 − 𝑉.- − 𝑉4 = 0


In fondo al canale sono alla soglia dell’inversione
à Poca carica! Nel modello 𝑄'() 𝐿 = 0


se VDS > VGS – VT
• Il modello mi dà addirittura una carica
  che cambia segno
• QINV è la carica di inversione (elettroni)
• Non può cambiare segno !!
• Il modello non è corretto !!


                           8 -                        Il MOSFET lavora in
   𝐼'+ = 𝛽6 (𝑉7+ −𝑉4 )𝑉'+ − 𝑉'+
                           -                           regione TRIODO
   valida solo per 𝑉'+ ≤ 𝑉7+ − 𝑉4                     o regione LINEARE
                                            Strozzatura del canale
per 𝑉$- > 𝑉.- − 𝑉4 il canale si “strozza”
vicino al drain à PINCH OFF del canale
à pochissima carica libera (elettroni)
à alta resistività
à alte cadute di potenziale
à VDS cade tutta vicino al drain
à EX(x=L) molto elevato; v(x=L) molto alta


POCA CARICA MA ALTA VELOCITA’
à la corrente rimane pressoché costante


                         1 -    𝛽6
 𝐼'+ = 𝛽6 (𝑉7+ −𝑉4 )𝑉'+ − 𝑉'+ =    (𝑉7+ −𝑉4 )-
                         2      2
                                                     Il MOSFET lavora in
                                                   regione di SATURAZIONE
 Dipendenza quadratica da VGS !
                                                        o PINCH OFF
                  Caratteristiche statiche MOSFET
TRIODO: dipendenza lineare da VGS           𝐼$-
                          1 -                            SATURO
  𝐼'+ = 𝛽6 (𝑉7+ −𝑉4 )𝑉'+ − 𝑉'+
                          2                       OFF


SATURAZIONE: dipendenza quadratica da VGS                            TRIODO

             𝛽6
       𝐼'+ =    (𝑉7+ −𝑉4 )-
             2                                          𝑉4   (𝑉! + 𝑉"# )
                                                                              𝑉.-


                               Linear
                                                              Luogo dei punti
                                                              di transizione da
                                                              triodo a saturo:
                                                                      𝛽6
                                                                𝐼'+ =    𝑉'+ -
                                                                      2
                      Modulazione lunghezza di canale
per 𝑉$- > 𝑉.- − 𝑉4 il canale si “strozza” vicino
al drain à PINCH OFF del canale
à Maggiore è VDS, maggiore è la porzione di
  canale che si strozza
à Il punto di Pinch off si sposta a sinistra
à Il modello è derivato dalla approssimazione
  di canale graduale

       𝛽6           -
                       𝑊 𝛽6 ′
 𝐼'+ =    (𝑉7+ −𝑉4 ) =        (𝑉7+ −𝑉4 )-
       2               𝐿 2

à la porzione di canale su cui è valida
  l’approssimazione di canale graduale è
  minore à è come se L si riducesse !!
                      L’ < L                   à Teoricamente in saturazione la corrente
                                                 è costante, ma in effetti non lo è
à IDS dipende da L’
                                               à IDS cresce linearmente con VDS
                                                     (come l’effetto Early nel BJT)
Effetto di Modulazione di lunghezza di canale
                      Modulazione lunghezza di canale




Sperimentalmente si vede che IDS cresce linearmente con VDS (come effetto Early nel BJT)
                                                     𝛽6
Correggo il modello in saturazione à         𝐼'+ =      (𝑉7+ −𝑉4 )- (1 + 𝜆𝑉'+ )
                                                     2
l à fattore di mod. lunghezza di canale
Le formule in reg. triodo e in saturazione devono collegarsi nel punto di transizione
Correggo anche il modello in reg. triodo:                            1 3
                                             𝐼$- = 𝛽6 (𝑉.- −𝑉4 )𝑉$- − 𝑉$-    (1 + 𝜆𝑉$- )
                                                                     2
                                Regioni di funzionamento




• MOSFET OFF à VGS < VT
• MOSFET ON à VGS > VT
   • TRIODO à VDS < VGS - VT
   • SATURAZIONE à VDS ≥ VGS - VT        𝑉$ − 𝑉- ≥ 𝑉. − 𝑉- − 𝑉4


     𝑉$ ≥ 𝑉. − 𝑉4   𝑉$. ≥ −𝑉4       Dipende solo da gate e drain !!
                                                              n-MOSFET
      Simboli elettrici del n-MOSFET


                                                                       D
                                             VDS          G
                                       IDS                                 VDS ≥ 0

                          VGS
                                                                       S

                                                              IG = 0
                                                   (almeno a livello statico)
• MOSFET OFF à VGS < VT
• MOSFET ON à VGS > VT
   • TRIODO à VDS < VGS - VT
   • SATURAZIONE à VDS ≥ VGS - VT             𝑉$ − 𝑉- ≥ 𝑉. − 𝑉- − 𝑉4


     𝑉$ ≥ 𝑉. − 𝑉4    𝑉$. ≥ −𝑉4           Dipende solo da gate e drain !!
                                                                p-MOSFET
      Simboli elettrici del p-MOSFET


                                                                         D
                             VGS
                                                 VSD        G
                                          ISD                                VSD ≥ 0


                                                                         S




Transistor p-MOSFET è complementare al n-MOSFET:
• Substrato n-Si
• VGB > VFB à accumulazione: accumulo di elettroni all’interfaccia
• VT < VGB < VFB à svuotamento: regione svuotata di carica spaziale positiva
• VGB < VT à inversione: carica spaziale positiva + carica di inversione (lacune)
• Canale di tipo p che connette source e drain
                   Tensione di soglia del p-MOSFET
VGB < VT à inversione: carica spaziale positiva + carica di inversione (lacune)
                                        𝑄'() + 𝑄*
                   𝑉!# − 𝑉"# − 𝜓$ = −
                                           𝐶%&

• Tendenzialmente VGB è negativa à cambia il verso del campo elettrico
• Anche YS è negativo !
• Cambia il segno della carica à carica nel substrato è positiva
• Alla soglia dell’inversione à 𝑄- ≅ 𝑄$
• Hp.: carica spaziale uniforme à rD = qND à QD = qNDWD
                                                                   𝑁$
   𝑄- ≅ 𝑄$ =    2𝑞𝑁$ 𝜀-2 2𝜓/ = 𝛾𝐶*+ 2𝜓/              𝜓/ = 𝑉"# ln      >0
                                                                   𝑛2

   𝜓- = −2 G 𝜓/                                             2𝑞𝑁$ 𝜀-2
                                                      𝛾=
                                                             𝐶*+
   𝑉4! = 𝑉/0 − 2𝜓/ − 𝛾 2𝜓/


• La tensione di soglia del p-MOSFET è tipicamente negativa !!
                                Effetto body nel p-MOSFET
VGB < VT à inversione: carica spaziale positiva + carica di inversione (lacune)


• Le giunzioni S-B e D-B non devono essere mandate in diretta à VSB, VDB ≤ 0
• Substrato alla tensione più alta nel dispositivo !
• Effetto body cambia il potenziale superficiale e la tensione di soglia

       𝜓- = −2 G 𝜓/ + 𝑉-0 = −2 G 𝜓/ − 𝑉0-              VBS ≥ 0


       𝑉4 = 𝑉4! − 𝛾    2𝜓/ + 𝑉0- − 2𝜓/                 Diventa più negativa !




• VGB < VT à inversione: si forma il canale, il MOSFET conduce corrente (ON)
• Funzionamento tipico con VSB = 0; VDB < 0 à VDS < 0
• La corrente scorre dal source al drain à ISD > 0 (IDS < 0)
                                   Regioni di funzionamento
• p-MOSFET OFF à VGS > VT
• p-MOSFET ON à VGS < VT
    • TRIODO à VDS > VGS – VT

                            1 -                bp = bp‘ ∙ S = bp‘ ∙ W / L
    𝐼+' = 𝛽9 (𝑉7+ −𝑉4 )𝑉'+ − 𝑉'+
                            2
                                               bp‘ = 𝜇; 𝐶*+ à conducibilità intrinseca



    • SATURAZIONE à VDS ≤ VGS - VT


           𝛽9
     𝐼+' =    (𝑉7+ −𝑉4 )-
           2


 VGS, VDS, (VGS - VT) tutte tensioni negative !! à il loro prodotto da un valore positivo
                                    Regioni di funzionamento
Se volessi lavorare con tensioni positive, devo girare i riferimenti di tensione

• MOSFET OFF à VSG < |VT|
• MOSFET ON à VSG > |VT|
     • TRIODO à VSD < VSG – |VT|

                                     1 -
           𝐼+' = 𝛽9 (𝑉+7 −|𝑉4 |)𝑉+' − 𝑉+' (1 + 𝜆𝑉+' )
                                     2

                                                            Effetto modulazione
                          Attenzione!! Modulo!!
                                                            lunghezza di canale

     • SATURAZIONE à VSD ≥ VSG - |VT|


                𝛽9
          𝐼+' =    (𝑉+7 −|𝑉4 |)- (1 + 𝜆𝑉+' )
                2
                     Tecnologia Complementary-MOS
Lo sviluppo dei transistor MOSFET ha dato la possibilità di ottenere dispositivi con
performance elevate con due strutture duali/complementari (nMOSFET e pMOSFET)
à n- e p-MOSFET lavorano su tensioni opposte in maniera simile
à Sviluppo della tecnologia COMPLEMENTARY-MOS (CMOS)
à Enorme boost all’elettronica digitale
à Le prestazioni dipendono fortemente dalla lunghezza minima (LMIN) con
  cui posso fabbricare i MOSFET
es.: LMIN = 0.35 µm, TOX = 4 nm (SiO2), NA = ND = 6∙1017 cm-3


COX = 8.63 fF/µm2,        2YF = 0.93 V,     VFBn = -1 V,      g = 0.52 𝑉


bn’ = COX µn = 388 µA/V2,           bp’ = COX µp = 194 µA/V2,


VT0n = 0.43 V,   VT0p = -0.43 V,    l = 0.05 V-1
                                 Effetti reattivi del MOSFET
Il fatto che il MOSFET sia basato sul condensatore MOS rende esplicita la presenza
di effetti reattivi nella struttura à Condensatore ANOMALO
QINV, QD dipendono da VGS, VDS e VSB in maniera NON LINEARE
Le capacità che descrivono gli effetti reattivi nel MOSFET dipendono dal
punto di lavoro !! (non sono costanti)


•   Effetti reattivi INTRENSECI
à legati al fatto che nella struttura c’è un condensatore MOS
à legate alla carica indotta nel substrato dal terminale di gate


•   Effetti reattivi PARASSITI
à legati alle non idealità della struttura e ad effetti di bordo
                           Carica di canale del MOSFET
Carica nel canale quando n-MOSFET è ON             𝑄'() (𝑥) = −𝐶*+ 𝑉.- − 𝑉4 − 𝑉(𝑥)
Hp.: regione TRIODO à VDS piccola << VGS – VT
à il canale n risulta avere una carica libera uniforme tra drain e source
à considero la resistività dello strato invertito costante lungo il canale
à la caduta di potenziale è lineare tra source e drain                        :
                                                               V(𝑥) ≅ 𝑉'+ 3
                                                                              ;


                 ;
                                                                    𝑉'+
    |𝑄<= | = 𝑊 6 𝐶/0 𝑉7+ − 𝑉4 − 𝑉 𝑥      𝑑𝑥 = 𝑊𝐿𝐶/0      𝑉7+ − 𝑉4 −
                !                                                    2
                                              𝑉7+ 𝑉7'                  dipende da
  𝑉'+ = 𝑉'7 + 𝑉7+           |𝑄<= | = 𝑊𝐿𝐶/0       +    − 𝑉4
                                               2   2                   VGS e VGD

              𝜕|𝑄<= | 1
       𝐶7+< =        = 𝑊𝐿𝐶/0
               𝜕𝑉7+   2                 Capacità differenziali tra i
                                           terminali G-S e G-D
                𝜕|𝑄<= | 1              Valide in regione TRIODO !
       𝐶7'< =          = 𝑊𝐿𝐶/0
                 𝜕𝑉7'   2
                              Carica di canale del MOSFET
Carica nel canale quando n-MOSFET è ON             𝑄'() (𝑥) = −𝐶*+ 𝑉.- − 𝑉4 − 𝑉(𝑥)
Hp.: regione SATURAZIONE à VDS > VGS – VT
à il canale n risulta avere una carica libera non uniforme tra drain e source
à Pinch off del canale: vicino al drain ho molta meno carica
à la caduta di potenziale è molto maggiore vicino al drain
                                                                          &-.
Hp1.: V(x) ha profilo PARABOLICO in x con vertice in x = 0      V(𝑥) ≅      / 3 𝑥-
                                                                           ;
Hp2.: ai limiti della saturazione VDS = VGS – VT

              ;
                                         2
 |𝑄<= | = 𝑊 6 𝐶/0 𝑉7+ − 𝑉4 − 𝑉 𝑥     𝑑𝑥 = 𝑊𝐿𝐶/0 𝑉7+ − 𝑉4           dipende solo
             !                           3                            da VGS

              𝜕|𝑄<= | 2
       𝐶7+< =        = 𝑊𝐿𝐶/0
               𝜕𝑉7+   3                    Capacità differenziali tra i
                                              terminali G-S e G-D
                 𝜕|𝑄<= |               Valide in regione SATURAZIONE
       𝐶7'< =            =0
                  𝜕𝑉7'
                                      Carica di svuotamento
Carica di svuotamento quando n-MOSFET è ON
à la carica di svuotamento è praticamente costante
à indipendente dalle tensioni applicate
à non induce effetti reattivi
capacità tra G-B? NO, se MOSFET ON à cambia solo |𝑄<= | (dip. da VGS e VDS)


Carica di svuotamento quando n-MOSFET è OFF                  𝑄$ (𝑥) = −𝛾𝐶*+ 𝜓-
à Il potenziale superficiale è pari alla caduta nel substrato
à Le due giunzioni S-B e D-B isolano il substrato da S e D
à La caduta nel substrato dipende da VGB

           𝜕|𝑄' |                                𝜕|𝑄' |
  𝐶75 = 𝑊𝐿        ≅ 𝑊𝐿𝐶/0                 𝐶7+' =        =0        Capacità
           𝜕𝑉75                                  𝜕𝑉7+            differenziali
                                                 𝜕|𝑄' |           quando il
          Complicata !!                   𝐶7'' =        =0      MOSFET è OFF
   Hp. di caso peggiore = COX
                                                 𝜕𝑉7'
               Capacità intrinseche del MOSFET

Reg. funzion.             CGS               CGD              CGB

      OFF                  0                 0             𝑊𝐿𝐶UV

                       1                 1
   TRIODO                𝑊𝐿𝐶UV             𝑊𝐿𝐶UV              0
                       2                 2

                       2
SATURAZIONE              𝑊𝐿𝐶UV               0                0
                       3

Le capacità da considerare dipendono dal punto di lavoro del MOSFET !!
                        Capacità parassite del MOSFET
Legate a non idealità ed effetti di bordo !
•   Capacità di OVERLAP
•   Capacità di FRINGING

      𝐶7+9 = 𝑊(𝑋> 𝐶/0 + 𝐶?@ )


à parametri che dipendono dalla tecnologia
      (misurati sperimentalmente)

      𝐶7+! = 𝑋> 𝐶/0 + 𝐶?@ [𝐹/𝑚]


           𝐶7+9 = 𝑊𝐶7+!

           𝐶7'9 = 𝑊𝐶7+!

        Indipendenti dalle tensioni !!
                  Capacità di giunzione del MOSFET
Le giunzioni S-B e D-B sono polarizzate in
inversa à capacità di giunzione

                     1
       𝐶A = 𝐶A!                 [F/𝑚- ]
                       |𝑉+5 |
                  1+
                        ΦA

   Φ< potenziale di built-in
   𝐶<! capacità di giunzione all’equilibrio
                                                        LS
   𝐶WX = 𝐶0X = 𝑊𝐿W 𝐶Y [𝐹]


es.:     NA = 1018 cm-3               à       Cj0 = 3 fF/µm2    capacità di
                                                                giunzione non
          TOX = 2 nm (SiO2)           à       COX = 10 fF/µm2   trascurabile
                                        Capacità del MOSFET
Il MOSFET presenta diverse capacità

       𝐶7+ = 𝐶7+< +𝐶7+9

      𝐶7' = 𝐶7'< +𝐶7'9

       𝐶75

       𝐶+5 = 𝐶'5



Stessa cosa per n-MOSFET e p-MOSFET
•   Nei circuiti con i MOSFET il gate è il terminale di ingresso che viene
    pilotato dai circuiti a monte
•   Gli altri terminali spesso sono mantenuti a tensione costante
à MOLTO IMPORTANTE LA CAPACITA’ CHE VEDO SUL GATE
              Capacità totale al gate del MOSFET
Sul gate del MOSFET vedo:

   𝐶7 = 𝐶7+ +𝐶7' + 𝐶75

   𝐶7 = 𝐶7+< +𝐶7'< + 𝐶75 + 2𝑊𝐶7+!

𝐶7+< , 𝐶7'< e 𝐶75 dipendono dal punto di lavoro


   Reg. funzion.            CG

       OFF           𝑊𝐿𝐶*+ + 2𝑊𝐶.-!


     TRIODO          𝑊𝐿𝐶*+ + 2𝑊𝐶.-!           Approssimazione cautelativa:


                     2                            𝐶7 ≅ 𝑊𝐿𝐶/0 + 2𝑊𝐶7+!
  SATURAZIONE          𝑊𝐿𝐶*+ + 2𝑊𝐶.-!
                     3
                    Risoluzione circuiti con i MOSFET
• Per il MOSFET abbiamo derivato un modello che permette di calcolare la
  corrente date le tensioni applicate
MOSFET OFF                                      à IDS = 0
                                                                          1 1
MOSFET ON TRIODO             |VDS| < |VGS - VT| à 𝐼*$ = 𝛽0 (𝑉!$ −𝑉+ )𝑉*$ − 𝑉*$ (1 + 𝜆𝑉*$ )
                                                                             2
                                                          𝛽0
MOSFET ON SATURO             |VDS| > |VGS - VT| à 𝐼*$ =      (𝑉!$ −𝑉+ )1(1 + 𝜆𝑉*$ )
                                                          2


• Per la soluzione di circuiti con transistori MOSFET:
– se si conoscono tutte le tensioni ai terminali, utilizzo la formula corrispondente alla
  regione di funzionamento
– se non si conoscono tutte le tensioni, occorre fare un’ipotesi sul funzionamento di
  ogni transistore MOSFET (spento, in pinch off, oppure triodo)
– risolvere il circuito usando le relazioni della regione di funzionamento ipotizzata;
– verificare che la soluzione trovata sia compatibile con l’ipotesi fatta.
• Si osservi che le equazioni che esprimono le relazioni tra tensione e corrente nel
  transistore MOS sono di secondo grado rispetto alle tensioni; questo può dar
  luogo a più soluzioni numeriche, delle quali una sola è fisicamente accettabile.
                         Amplificatore a source comune
                              • Il circuito è l’analogo dell’amplificatore ad emettitore
                                comune fatto con il BJT
                              • Il source è tensione di riferimento sia per la maglia di
                                ingresso, che per la maglia di uscita
                              • Amplificatore a source comune
                              Hp. semplificativa: trascuro eff. modulaz. lunghezza canale (l=0)
                              Hp.: MOSFET OFF à IDS = 0
                                        VIN = VGS < VT ; VOUT = VDS = VDD


                              Hp.: MOSFET SATURO VIN = VGS > VT               VDS > VGS - VT

                                                                  𝛽0
                                 𝑉%2+ = 𝑉** − 𝑅* 𝐼*$ = 𝑉** − 𝑅*      (𝑉'( −𝑉+ )1 > 𝑉!$ − 𝑉+
                                                                  2

Hp.: MOSFET TRIODO VIN = VGS > VT           VDS < VGS - VT
                                                  1 1
𝑉%2+ = 𝑉** − 𝑅* 𝐼*$ = 𝑉** − 𝑅* 𝛽0 (𝑉'( −𝑉+ )𝑉%2+ − 𝑉%2+
                                                  2
   𝑅* 𝛽0 1
        𝑉%2+ − 1 + 𝑅* 𝛽0 (𝑉'( −𝑉+ ) 𝑉%2+ + 𝑉** = 0   Due soluzioni di cui solo una è valida!
    2
                                                  Caratteristica statica
                                 VIN = VGS < VT ; VOUT = VDS = VDD
                                 VIN = VGS > VT
                                                                   𝛽0
                                  𝑉%2+ = 𝑉** − 𝑅* 𝐼*$ = 𝑉** − 𝑅*      (𝑉'( −𝑉+ )1 > 𝑉'( − 𝑉+
                                                                   2


                                 oppure
                                    𝑅* 𝛽0        𝑉**
                                          𝑉%2+ +      = 1 + 𝑅* 𝛽0 (𝑉'( −𝑉+ )     𝑉%2+ < 𝑉'( − 𝑉+
                                     2           𝑉%2+


                                                       Vout
• Caratteristica statica simile a quella
                                                        Vdd
  dell’emettitore comune
• Alta pendenza della caratteristica con il
  MOSFET in regione di saturazione
  (applicazioni analogiche)
• Applicazioni digitali: Porta NOT à                                               Vin-Vt
  MOSFET OFF oppure in regione TRIODO
esercizio: VDD=5 V, RD=5 kW, VIN=2 V, VT=1 V,
           bn=2 mA/V2
                                                                 Vt                         Vin
                                                                                Esercizio
                                  VD = VGS = VDS           à Il MOSFET diventa un bipolo

                                  𝑉*$ > 𝑉!$ − 𝑉+        Se acceso sicuramente saturo!

                                  MOSFET ON se VD > VT
                                  Hp. semplificativa: trascuro eff. modulaz. lunghezza canale (l=0)

                                                                        𝛽0
                                            𝑉* = 𝑉** − 𝑅𝐼* = 𝑉** − 𝑅*      (𝑉* −𝑉+ )1
                                                                        2

                                  • Se VD > VT à corrente ID positiva               MOSFET
                                                                                    connesso
                                  • Se VD < VT à ID = 0
                                                                                    a diodo

esercizio: VT=0.6 V, ID=0.08 mA, bn’=200 µA/V2, W/L=5
à progettare R
                                                   2𝐼* 𝐿
       𝑉* = 𝑉** − 𝑅𝐼*                𝑉* = 𝑉+ ±           > 𝑉+
                                                   𝛽03 𝑊                 𝑉** − 𝑉*
                                                                    𝑅=            = 25 𝑘Ω
                                                                            𝐼*
              𝑊 𝛽0 ′
       𝐼* =          (𝑉* −𝑉+ )1             𝑉* = 1 𝑉
              𝐿 2
                     Specchio di corrente a MOSFET
                                    • Sul ramo di sinistra Q1 come bipolo
                                      à connessione a diodo (MOSFET saturo)
                                    • Corrente IREF fissata
                                    • Stessa VGS sui due MOSFET
                                    Hp: transistor identici; Q2 ON e saturo
                                    Hp. semplificativa: trascuro eff. modulaz. lunghezza
                                    canale (l=0)

                                                𝛽6
                                           𝐼* =    (𝑉.- −𝑉4 )3 = 𝐼$= = 𝐼>?/
                                                2

Il circuito «specchia» la corrente IREF sul ramo di destra !!
• Il circuito funziona se Q2 è saturo VO > VGS – VT
• IO = IREF se non considero l’effetto di modulazione di lunghezza di
  canale à dipendenza di IO da VO
• In questo caso non ho impatto delle correnti di ingresso dei transistori
à nello specchio a BJT c’è una differenza tra le correnti dovute alle IB
                                                                               Esercizio
                                    MOSFET di destra e di sinistra hanno source e drain allo
    VG1=               VG2
                                    stesso potenziale VX.
                  Vx                Il MOSFET di destra è connesso a diodo à saturazione:
                                                    =                    =
                                    Eq.(1)     𝐼+ = 𝛽6 (𝑉.-3 −𝑉4 )3 = 𝛽6 (𝑉.3 −𝑉+ − 𝑉4 )3
                                                    3                    3
   Parametro        n-MOSFET
   VTO [V]                  1       dove VG2 è la tensione di gate del transistore di destra.
   b [µA/V2]             300
   g [V1/2]                 0       Per essere acceso    à VX<VG2-VT=2.0 V
   l [V-1]                  0
   LMIN [µm]              0.2                            à VG2> VX+ VT

VG1 è la tensione di gate del MOSFET di sinistra.
VG1 =VG2> VX+ VT
VX è anche la tensione di drain del MOSFET di sinistra. Questo garantisce che il MOSFET di
sinistra sia in regione triodo:
                                          =                                        =
Eq.(2)         𝐼+ = 𝛽6 ((𝑉.-= −𝑉4 )𝑉$-= − 𝑉$-= 3 ) = 𝛽6 ((𝑉.-= −𝑉4 )(𝑉+ −𝑉-= ) − (𝑉+ −𝑉-= )3 )
                                          3                                        3



Eguagliando Eq.(1) e (2) otteniamo VX =1.29 V che da luogo ad una corrente di IX =75 µA.
2.
                                                      Esercizio                        Esercizio
                          • Progettare il circuito affinché ID = 0,4 mA e
                            VD = 0,5 V. Siano VT = 0,7 V, β’ = µCOX = 100
                            µA/V2, W/L = 32.
                                Hp. semplificativa: trascuro eff. modulaz. lunghezza canale (l=0)


                                                                          𝑉** − 𝑉*
                                      𝑉* = 𝑉** − 𝑅* 𝐼*             𝑅* =            = 5 𝑘Ω
                                                                             𝐼*


                               VD > VG - VT à MOSFET saturo

                                      𝑊 𝛽0 ′               𝑊 𝛽0 ′               𝑊 𝛽0 ′
                               𝐼* =          (𝑉!$ −𝑉+ )1 =        (−𝑉$ −𝑉+ )1 =        (−𝑉$$ −𝑅$ 𝐼* − 𝑉+ )1
                                      𝐿 2                  𝐿 2                  𝐿 2
         2𝐼* 𝐿
     ±         = −𝑉$$ − 𝑅$ 𝐼* − 𝑉+ > 0
         𝛽03 𝑊                                                            𝑉$$ 𝑉+    2𝐿
                                                                 𝑅$ = −      − −         = 3.25 𝑘Ω
                                2𝐼* 𝐿                                     𝐼*  𝐼* 𝛽03 𝑊𝐼*
         𝑅$ 𝐼* = −𝑉$$ − 𝑉+ −
                                𝛽03 𝑊
                                                        EsercizioEsercizio
                                • Risolvere il circuito sapendo che VT = 1 V,
                                  β = 1 mA/V2.
                                                                Hp. semplificativa: l=0

                                      Hp.: MOSFET saturo à VD > VG - VT

                                                  𝑅!1
                                        𝑉! =            𝑉 =5𝑉
                                               𝑅!4 + 𝑅!1 **

                                      𝛽0               𝛽0                   𝛽0
                               𝐼* =      (𝑉!$ −𝑉+ )1 =    (𝑉! −𝑉$ − 𝑉+ )1 =    (𝑉! −𝑅$ 𝐼* − 𝑉+ )1
                                      2                2                    2

                                𝛽0 1 1                                     𝛽0
                                  𝑅 𝐼 − 𝐼* 1 + 𝛽0 𝑅$ 𝑉! − 𝑉+           +      (𝑉! −𝑉+ )1 = 0
                                2 $ *                                      2

                                          𝐼*4 = 0.5 𝑚𝐴 à 𝑉$4 = 𝑅$ 𝐼* = 3 𝑉 < 𝑉!           OK

                                          𝐼*1 = 0.888 𝑚𝐴 à 𝑉$1 = 𝑅$ 𝐼* = 5.3 𝑉 > 𝑉! NO!
𝑉!$ = 2 𝑉 > 𝑉+

𝑉* = 𝑉** − 𝑅* 𝐼*4 = 7 𝑉   VD > VG – VT à Hp. OK !
                      del medesimo. (punti 4)

                  3. Determinare l’espressione della funzione di trasferimento VO (s)/VGS (s). (10 punti)                             Esercizio
                  4. Calcolare il valore della frequenza del polo della funzione di trasferimento VO (s)/VGS (s). (4 punti)
      Vth = 25 mV, R1 = 30 kΩ, R2 = 20 kΩ, IS = 10−15 A, β0,npn = β0,pnp = 60, βF,npn = βF,pnp = 60,
      VCC = 5 V, βM OS = 200 · 10−6 A/V2 , VT = 1 V, λM OS = 0.1 V−1 , C = 1 nF.
                                                                                                                      Vcc


                                            R1                   IBp
                                                                  Ib                            Ri2            ICn
                                                                                     Tp

                                                                                                               Tn

                                                                       Rf             Vx
                                                                                              IBn                              Vo
                                     Prova scritta di Fondamenti di Elettronica
                                                   26 gennaio
                                                      MOS     2010              C
                                            R2                                                     Ro
ome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Cognome: . . . . . . . . . . . . . . . . . . . . . . . . . . . Matricola: . . . . . . . . . . . .
                                                                                     IDS
unti Assegnati: . . . . . . /. . . . . . / . . . . . . / . . . . . . / . . . . . . / . . . . . . / = . . . . . . . . .

on riferimento al circuito di Figura, si risponda ai seguenti quesiti utilizzando i valori assegnati dei
 rametri:
        Vth = 25 mV, R1 = 30 kΩ, R2 = 20 kΩ, IS = 10−15 A, β0,npn = β0,pnp = 60, βF,npn = βF,pnp = 60,
 1. Determinare  Roβ,MR
        VCC = 5 V,     F =e 200
                      OS     VO· 10
                                 in−6modo
                                      A/V2tale che
                                          , VT =    siaλMVOS
                                                 1 V,     X == 0.1
                                                                VCC /2, C
                                                                   V−1  e che la potenza statica dissipata
                                                                          = 1 nF.
      dall’ultimo stadio contenente il transistore Tn sia P = 1 mW. (8 punti)
                      4. Calcolare il valore della frequenza del polo della funzione di trasferimento VO (s)/VGS (s). (4 punti)

                                                                                                               Soluzione
                                                                                               Vcc


                                        R1              IIbBp                Ri2
                                                                      Tp                 ICn
                                                                                        Tn

                                                            Rf         Vx
                                                                            IBn                      Vo


                                        R2                      MOS                                   C
                                                                               Ro


                                             IDS
                  Soluzione del compito di Fondamenti di Elettronica
                                   26 gennaio 2010
                  BJT  npn (Tn) lavora chiaramente in regione normale e il suo consumo di potenza vale
1. Il transistore n-MOSFET
                   Vth = 25 mV, R1 = 30 kΩ, R2 = 20 kΩ, IS = 10−15 A, β0,npn = β0,pnp = 60, βF,npn = βF,pnp = 60,
   P = ICn VCC V+CCI=Bn5 VV,XβM=   IBn
                                OS = 200(β     nV
                                         · 10F−6  CC2 , +
                                                 A/V    VT V
                                                           =X1 ),
                                                               V, λda
                                                                   M OScui
                                                                        = 0.1ricavo
                                                                              V−1 , C =IBn
                                                                                        1 nF.= 3.31µA, ICn = 198.6µA e
   VBEn = Vth ln (ICn /IS ) = 0.676 V.
   Ora VO = VX − VBEn = 1.824 V e RO = VO /(βF + 1)IBn = 9034Ω.
   La tensione VGS = R1R+R
                         2
                           2
                             VCC = 2 V, da cui otteniamo I DS = 0.5βM OS (VGS − VT )2 (1 + λV
                                                                                             DS ) =
   125µA.
   Inoltre, IBp (βF p + 1) = IDS + IBn = 128.3µA.
   Per cui IIBn
              Bp = 2.1µA e VEBp = Vth ln (βF p IBn
                                                 p /IS ) = 0.639 V.
   Ricavo quindi RF = (VCC − VEBp − VX )/IBp = 886 kΩ.
                                                                       Esercizio
                     Esercizio
    • Risolvere il circuito          Per Vi = 0 à polarizzazioni uguali ed opposte
      con Vi=
       –0
                                     à le tensioni VGS sono uguali ed opposte
       – 2,5                         Hp.: MOSFET in saturazione
       – -2,5

o   • sapendo che
       – VTN = -VTP = 1 V,
                                      𝐼*( =
                                              𝛽0
                                              2
                                                 (𝑉!$( −𝑉+( )1     𝐼*5 =
                                                                           𝛽6
                                                                           2
                                                                              (𝑉!$5 −𝑉+5 )1

       – βN = βP = 1 mA/V2.
                                     essendo i parametri identici ottengo IDP = IDN e
                                     quindi la corrente sulla resistenza è nulla à Vo = 0
                                     OK l’ipotesi di saturazione (VG=VD)

                                     Per Vi = 2.5 à p-MOSFET OFF, n-MOSFET ON
                                     Hp.: n-MOSFET in saturazione
                                         𝛽0
                                 𝐼*( =      (𝑉!$( −𝑉+( )1 = 8 𝑚𝐴     𝑉7 = −𝑅* 𝐼*( = −80 𝑉
                                         2
                                                                               NO!
                                     MOSFET in TRIODO
                                                               1
                              𝐼*( = 𝛽0 (𝑉!$( −𝑉+( )(𝑉7 + 2.5) − (𝑉7 + 2.5)1       𝑉7 = −𝑅* 𝐼*(
                                                               2
