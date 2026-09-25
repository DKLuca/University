---
fonte: "4_modelli e applicazioni diodi.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Modelli per il diodo

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                  IlDiodo
                                      diodo     a   giunzion
                                          ideale e diodo reale
    Nel diodo ideale la caratteristica è a squadra

                 ID

                        VD
o più semplice realizzato con una
 -n è il diodo. Il terminale collegato
  drogata    • Perpè       il terminale
                       la maggior               positivo
                                     parte dei problemi pratici, la caratt
  • Diodo reale à giunzione pn; il modello
uello
    dellacollegato
                 esponenziale allapuò regione
         corrente è di tipo esponenziale           drogatadanuna ca
                                         essere approssimata
             • è chiaramente
                 ID = 0 se VNON    Vγ “off”! (spento)
                                 < LINEARE
 e negativo (catodo).
  • Il modello                 D
              • ID > 0 se VD = Vγ “on” (acceso)
                         𝑉!
              • 𝐼" dove
           𝐼! =    # 𝑒𝑥𝑝 Vγ è 1 tensione di soglia (circa 0.7 V per u
                            − la
                          𝑉#$
                             Modello esponenziale del diodo
  •    Il modello è chiaramente NON LINEARE !

                  ID

                          VD
o più semplice       𝑉
                         realizzato con una
                               !
       𝐼 = 𝐼 # 𝑒𝑥𝑝       −1
 -n è il diodo. Il terminale collegato
             !    "
                    𝑉         #$

  drogata      p è il terminale positivo
        approssimazioni:
        V < 0 à I ≅ -I alla regione drogata n
uello collegato
              D          D         S

        V > 0 à I ≅ I exp(V / V )
 e negativo (catodo).
              D          D     S       D   th



      COMPONENTE NON LINEARE CHE INSERITO IN UN CIRCUITO IN GENERALE
      DA LUOGO A SISTEMI DI EQUAZIONI NON LINEARI !!
      à spesso non risolubile analiticamente (equazioni trascendenti)
singola semionda
                                 Esempio di circuito con diodo
                                   ID
                                            𝑉% = 𝑉& + 𝑉! = 𝑅𝐼! + 𝑉!
                                                          𝑉!
                                            𝐼! = 𝐼" # 𝑒𝑥𝑝     −1
                                                          𝑉#$
                        VD
                                                         𝑉!
                                          𝑉% = 𝑅𝐼" # 𝑒𝑥𝑝     − 1 + 𝑉!
                                                         𝑉#$
                                            equazioni trascendente

funzione       di  trasferimento              statica
  Circuito molto semplice, ma soluzione analitica non c’è!

     Come risolvo il circuito?
a)   1. Metodo grafico
     2. Metodo di Newton
     3. Metodo iterativo
singola semionda
                                             Metodo grafico
                               ID
                                        𝑉% = 𝑉& + 𝑉! = 𝑅𝐼! + 𝑉!
                                                      𝑉!
                                        𝐼! = 𝐼" # 𝑒𝑥𝑝     −1
                                                      𝑉#$
                         VD

                                         Retta di carico


funzione        di   trasferimento
  Disegno le curve corrispondenti a
                                    statica
   •   retta di carico
   •   modello del diodo
a)Soluzione = punto di incrocio delle
   due curve à PUNTO DI LAVORO Q
   Metodo poco pratico !!
singola semionda
                                                 Metodo di Newton
                                  ID
                                                                𝑉!
                                            0 = −𝑉% + 𝑅𝐼" # 𝑒𝑥𝑝     − 1 + 𝑉!
                                                                𝑉#$
                         VD
                                                                    𝑉!
                                         𝑓(𝑉! ) = −𝑉% + 𝑅𝐼" # 𝑒𝑥𝑝       − 1 + 𝑉!
                                                                    𝑉#$

  Dobbiamo trovare 𝑓(𝑉! ) = 0
funzione       di trasferimento statica
  à metodo di Newton
  à soluzione iniziale di tentativo
                                                              𝑓(𝑉! # )
  à metodo ricorsivo                          𝑉! #$% = 𝑉! # −
                                                              𝑓′(𝑉! # )
a) 𝑉   ! %() − 𝑉! %   < 𝑡𝑜𝑙𝑙𝑒𝑟𝑎𝑛𝑧𝑎 à STOP

   •     Metodo utilizzato nelle soluzioni numeriche à calcolatore, simulatori
   •     Convergenza lenta
singola semionda
                                              Metodo iterativo
                                ID
                                           𝑉% = 𝑉& + 𝑉! = 𝑅𝐼! + 𝑉!
                                                         𝑉!
                                           𝐼! = 𝐼" # 𝑒𝑥𝑝     −1
                                                         𝑉#$
                     VD
                                               converge molto velocemente!
 • Prevede di partire con una soluzione
    di tentativo
 • Proiezione alternata sulle due curve
funzione di trasferimento statica
 • Rotazione in senso orario
 1. ID su retta di carico !!
 2. VD su modello diodo !!
 à mettere l’equazione del diodo in
 forma logaritmica (altrimenti il metodo
a)
 non converge!)
                         𝑉% − 𝑉!
                   𝐼! =
                             𝑅
                              𝐼!
               𝑉! = 𝑉#$ # ln      +1
                               𝐼"
singola semionda
                                                Metodo iterativo
                                ID
                                           𝑉% = 𝑉& + 𝑉! = 𝑅𝐼! + 𝑉!
                                                         𝑉!
                                           𝐼! = 𝐼" # 𝑒𝑥𝑝     −1
                                                         𝑉#$
                     VD

 • Prevede di partire con una soluzione
    di tentativo                             start: VD0 soluzione di tentative
 • Proiezione alternata sulle due curve               es.: VD0 = 0 V

funzione di trasferimento statica
 • Rotazione in senso orarioI da (1)
 1. ID dalla retta di carico !!
                                     V da (2)     D              D

 2. VD dal modello diodo !!                           ID1            VD1
 à mettere l’equazione del diodo in
 forma logaritmica (altrimenti il metodo              ID2            VD2
a)
 non converge!)
                         𝑉% − 𝑉!                      ID3            VD3
                   𝐼! =
                             𝑅
                              𝐼!
               𝑉! = 𝑉#$ # ln      +1       𝑉! #$% − 𝑉! # < 𝑡𝑜𝑙𝑙𝑒𝑟𝑎𝑛𝑧𝑎 à STOP
                               𝐼"
Esempio numerico
                                     Approssimazione lineare
•       Il modello non lineare complica la soluzione       I
        dei circuiti
•       Se ho tanti diodi il calcolo diventa troppo
        complicato à solutori
                       • Il dispositivo
                                 numerici, simulatoripiù semplice V
                                                                  realizz
        circuitali
                      giunzione p-n è il diodo. Il termin
                      alla semplificata
Spesso ha senso un’analisi   regioneà drogata        p lineare
                                        approssimazione è il termina
Quale usare?          (anodo); quello collegato alla reg
                      è il ideale
à Caratteristica del diodo  terminale negativo (catodo).
                      𝑉
        𝐼 = 𝐼" # 𝑒𝑥𝑝     −1
                     𝑉#$

    •    MODELLO A SOGLIA
             à modello lineare a tratti
    •    TENSIONE DI SOGLIA à V𝛾
                        Modello a soglia del diodo
               D                                    ID


           • Il dispositivo più semplice Vrealizz       D
             giunzione p-n è il diodo. Il termin
             alla regioneD drogata p è il termina
             (anodo); quello       collegato alla reg
                          Modello lineare a tratti formato da
             è il terminale
                          due negativo
                              semirette:        (catodo).
TENSIONE DI SOGLIA à V𝛾
• unico parametro del       (a) Diodo OFF: 𝐼! = 0 𝑝𝑒𝑟 𝑉! < 𝑉1

  modello                     (non consente di calcolare VD à resto del circuito)

• quanto vale?
                            (b) Diodo ON:       𝑉! = 𝑉1 𝑝𝑒𝑟 𝐼! > 0
                               (non consente di calcolare ID à resto del circuito)
                              Tensione di soglia del diodo
                    D                                          ID


                      • Il dispositivo più semplice Vrealizz     D
                        giunzione p-n è il diodo.          𝑉! Il termin
                                            𝐼! = 𝐼" # 𝑒𝑥𝑝
                        alla regione drogata          p è𝑉#$il −termina
                                                                 1
                                         D
                        (anodo); quello collegato alla reg
• Nel modello esponenziale
                        è   non
                           il   esiste un
                              terminale    negativo       (catodo).
  valore di soglia !!
• In scale logaritmiche à retta
• La corrente aumenta di un ordine di
  grandezza ogni 60 mV
Es.:    IS = 10-15 A
        VD = 0.59 à ID = 10 µA
        VD = 0.65 à ID = 100 µA         Il diodo può considerarsi acceso per VD ≅ 0.6 V
        VD = 0.71 à ID = 1 mA           TENSIONE DI SOGLIA à V𝛾 = 0.6 – 0.7 V
                             Tensione di soglia del diodo
                    D                                       ID


                  • Il dispositivo più semplice Vrealizz    D
                      giunzione p-n è il diodo.      𝑉! Il termin
                                       𝐼! = 𝐼" # 𝑒𝑥𝑝
                      alla regione drogata       p è𝑉#$il −termina
                                                            1
                                    D
                      (anodo); quello collegato alla reg
   La tensione di soglia
                      èviene scelta
                         il terminale negativo (catodo).
 spesso in base al livello di corrente a
       cui siamo interessati !!


Es.:    IS = 10-15 A
        VD = 0.59 à ID = 10 µA
        VD = 0.65 à ID = 100 µA      Il diodo può considerarsi acceso per VD ≅ 0.6 V
        VD = 0.71 à ID = 1 mA        TENSIONE DI SOGLIA à V𝛾 = 0.6 – 0.7 V
                                     Uso del modello a soglia
    (a) Diodo OFF: 𝐼! = 0 𝑝𝑒𝑟 𝑉! < 𝑉1                        ID

    (b) Diodo ON:   𝑉! = 𝑉1 𝑝𝑒𝑟 𝐼! > 0
                  • Il dispositivo più semplice Vrealizz             D
                       giunzione
• Il modello a soglia NON               p-n è
                            INTEGRA il modello     il diodo. Il termin
                                                esponenziale
                       alla regione
• Il modello a soglia (lineare)           drogata
                                SOSTITUISCE               p è il termina
                                             il modello esponenziale (non
  lineare)             (anodo); quello collegato alla reg
Come lo uso?
                       è il terminale negativo (catodo).
•   Utilizzo (a) oppure (b) al posto della formula esponenziale
•   Presuppone di sapere se il diodo è acceso o spento
•   Necessario FARE UN’IPOTESI INIZIALE !!
•   Successivamente l’ipotesi va VERIFICATA !!
•   Se la soluzione non è consistente con il funzionamento del diodo l’ipotesi
    iniziale era sbagliata à devo formulare l’ipotesi alternativa e rifare i calcoli
Es.: Hp: Diodo ON à la soluzione deve garantire 𝐼! > 0 altrimenti è sbagliata
                     Considerazioni ed errori comuni
  (a) Diodo OFF: 𝐼! = 0 𝑝𝑒𝑟 𝑉! < 𝑉1                 ID

  (b) Diodo ON:    𝑉! = 𝑉1 𝑝𝑒𝑟 𝐼! > 0
                  • Il dispositivo più semplice Vrealizz                D
                      giunzione p-n è il diodo. Il termin
1. L’ipotesi iniziale va sempre
                      alla      verificata àdrogata
                              regione         se non verificop
                                                             rischio
                                                                è ill’errore
                                                                      termina
2. La soluzione tramite il modello a soglia è migliore quanto più scegliamo
                      (anodo); quello collegato alla reg
   una V𝛾 vicina al valore VD che si ottiene con il mod. exp.
3. Il modello a sogliaèSOSTITUISCE
                          il terminale         negativo
                                        il modello esponenziale(catodo).
       à sono modelli alternativi !!
       à mischiare i due modelli !!

                                𝑉>
                  𝐼< = 𝐼= # 𝑒𝑥𝑝
                                𝑉?@
                                    −1             NO !!
Esempio: modello a soglia
Circuiti con diodi: esercizio 1
Soluzione esercizio 1
Soluzione esercizio 1
Circuiti con diodi: esercizio 2
                            Esempio
                         Circuiti con diodi: esercizio 3


                                                 R1 1 k :
                                                 R2     3k :
                                                 R3     2k:
                                                 R4     6k:
                                                 VG1    6V
                                                 VG 2   12 V



Ɣ Utilizzando il modello a soglia con VJ   0.7 V, determinare la tensione
  di uscita vo per vi 9 V


                                                                            16
                                Esempio
                             Circuiti con diodi: esercizio 3
 Ɣ Ipotesi 1: D1 e D2 in conduzione (¨ iD1 ! 0, iD2 ! 0)
                                                                        io
Diodi come gen. tensione Vg e applico sovrapp.
degli effetti per il calcolo della corrente io

         VG1  VJ VG 2  VJ vi
                          
            R1       R2      R3
  vo                                 6.78 V
            1    1    1    1
                   
            R1 R2 R3 R4
                   ¨




         VG1  VJ  vo               ¨ Non compatibile con le ipotesi
  iD1                     1.48 mA
              R1                     ¨ La soluzione non è accettabile
         VG 2  VJ  vo
  iD 2                    1.51 mA
              R2
                                                                             17
                              Esempio
                          Circuiti con diodi: esercizio 3
Ɣ Ipotesi 2: D1 interdetto, D2 in conduzione (¨ vD1  VJ , iD2 ! 0)


         VG 2  VJ vi
                  
            R2      R3
  vo                      8.27 V
          1     1   1
              
         R2 R3 R4
                   ¨




  vD1 VG1  vo      -2.27
                      0.78 VV
                                    ¨ Soluzione accettabile
         VG 2  VJ  vo
  iD 2                    1.01 mA
              R2

                                                                      18
           Applicazioni dei diodi

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
            Raddrizzatore a semionda singola

                                      ID

                                           Il diodo consente solo ID > 0
                                           à otteniamo Vout > 0



Se applichiamo il modello a soglia:
•   Diodo OFF
                 𝑉%* = 𝑅𝐼! + 𝑉!               𝑉%* = 𝑉! < 𝑉+
                     𝐼! = 0                      𝑉&,# = 0
•   Diodo ON
                                                  𝑉%* − 𝑉+
                 𝑉%* = 𝑅𝐼! + 𝑉!              𝐼! =          >0
                                                     𝑅
                     𝑉! = 𝑉+                  𝑉&,# = 𝑉%* − 𝑉+
                 Raddrizzatore a semionda singola

                             ID

                                  1. se Vin > V𝛾 à Vout > 0
                                  2. se Vin < V𝛾 à Vout = 0



Es.: Vin forma d’onda
sinusoidale
                     Raddrizzatore a semionda singola
             Ɣ Una delle applicazioni fondamentali del diodo è il circuito raddrizzatore,
               che permette di ottenere una tensione unidirezionale a partire da una
               tensione alternata
                                        ID si ottiene che
             Ɣ Utilizzando il modello a soglia
                                                   1. se Vin < V𝛾 à Vout = 0
                  per vi d VJ il diodo è interdetto, quindi vo 0
                                                  2. se
                  per vi ! VJ il diodo è in conduzione,   Vin v> Vv𝛾  à
                                                         quindi         VJ Vout = Vin - V𝛾 > 0
                                                                 o   i




                                          Raddrizzatore a singola semionda
                               Ɣ Se l’ingresso è sinusoidale il diodo conduce durante le semionde
Es.: Vin forma d’onda            positive e rimane interdetto durante le semionde negative
sinusoidale
                                                                                       19

Trasforma una forma
d’onda a valor medio
nullo in una a valorRaddrizzatore a singola semionda
medio non nullo
         Ɣ Se l’ingresso è sinusoidale il diodo conduce durante le semionde
à Convertitoripositive
                AC/DC  e rimane interdetto durante le semionde negative
cazioni tipiche:
           R C   raddrizzatore
assume che i valori di e siano
                                a con filtro
                      Raddrizzatore
mensionati in modo che la costante
tempo sia molto grande rispetto al
ola Tsemionda con filtro d’uscita
riodo della tensione di ingresso

                                                              Si 31desidera che il carico R sia
                                                              percorso da una corrente il più
                                                              costante possibile (es. carica
    Raddrizzatore con capacità di filtro                      batterie)
                                                              •   Il condensatore C fornisce
uindi si può assumere che
  La variazione della tensione di uscita sia molto piccola nell’intervallo
                                                                          la corrente al carico quando
  in cui il diodo è interdetto                                            D è OFF
  Il diodoche
 dera      conduca per intervalli
               il carico    R sia di tempo molto brevi
                                       percorso     darispetto T • Ripple (Vr): variazione
                                                         unaacorrente
ostante possibile (es. carica batterie)                            indesiderata dell’uscita ∆Vo
ensatore C fornisce la corrente al carico nella
nda in cui D è OFF
: variazione indesiderata dell’uscita ∆Vo
 sionamento di C alla lavagna)
        doppia     semionda
          Raddrizzatore a doppia semionda




   I diodi permettono alla corrente di scorrere solo in un senso !!
sso sinusoidale (ad es. trasformator
      doppia     semionda
        Raddrizzatore a doppia semionda




          1) se V > 2V à V > 0
sso sinusoidalein
                   (ad es. trasformator
                    𝛾   out
      doppia     semionda
        Raddrizzatore a doppia semionda




          2) se V < -2V à V > 0
sso sinusoidalein
                   (ad es. trasformator
                    𝛾    out
cazioni tipiche: raddrizzatore a
                   ¨ Quindi la tensione di uscita è
             Raddrizzatore
    doppia semionda  v v  2V
                                        a doppia semionda
 a doppia semionda                             o      i     J


                                           Ɣ Per |vi| < 2VJ i diodi sono tutti interdetti e quindi la tensione vo è nu
onda (o ad onda intera) consentono di                             •    In ogni semiperiodo,
e della tensione alterata in ingresso
mente per realizzare un raddrizzatore a
                                                                       conducono solo due diodi !
 (detto anche ponte di Graetz)                                    •
                                                               La tensione sulla resistenza
                                                      Raddrizzatore  a doppia
                                                               è sempre  positivasemionda
                                           Ɣ Se la tensione in ingresso è sinusoidale, l’andamento della tension
                                             uscita è il seguente
sso sinusoidale (ad es. trasformatore)
ni semiperiodo conduce una coppia di diodi
= (alla lavagna)
      • Sfrutto anche la
er |vi| > 2VJ , una delle copie di diodi
e mentre semionda          negative
           l’altra è interdetta
    • Il valor medio della  21
      forma d’onda generate
      è doppio rispetto al
 a doppia   semionda
      raddrizzatore  con un
      diodo
no in conduzione mentre D e D sono
ppia semiondaRaddrizzatore
              con filtrocond’uscita
                             filtro




condensatore C fornisce la corrente al carico
ell’intervallo in cui le coppie di diodi
 rnirebbero Vo < VM-2Vγ
 pple: variazione indesiderata dell’uscita ∆Vo
 imensionamento di C alla lavagna)
 pplicazioni tipiche:picco rilevatore
                            Rivelatore didi
                                          picco

 Vo<                  picco
      VγVi-Vo <DVγèD è OFF,
   • Se
   = -0,IVo<
  Vi        = 0,Vγ
          D Vo   Vresta
                   o restaD ècostante
 eF, •IdSe = 0, Vo>resta
             Vi-Vo      Vγ D è ON, il
stante   condensatore si carica e
 Vo>
  Vi - si  Vγ
         Vo>    Vγal D
            porta         DèèVM-Vγ
                      limite
 ondensatore
N,  il• condensatore
         Successivamente   sisi Vo
eica     rimane
   si eporta      aalVal
           si porta    M -Vγ
                        limite
                           limite
m - Vγ
 ccessivamente Vo
 sivamente
  ane a Vm - VγVo
  a
  soVm limite- del
               Vγ
mite       del con filtro
  drizzatore
n R ∞ con filtro
zatore
                    Clamper
             clamping (negativo)                Clamper (negativo)
   Si assume
esidera              che il condensatore
                aggiungere          un   valor inizialmente sia scarico che il diodo
      Aggiungere
   possa      essere    un   valor medio ideale
                          considerato
 io negativo
      negativo a un     a segnale
                           un segnalea      a
 r Inizialmente
    medio       nulloilnullo
      valor medio          diodo va in conduzione e il condensatore si carica finché
   la sua tensione raggiunge il valore VM
Vi –• Vc   Se<Vi–Vc
                  Vγ < Vγ    D DèèOFF,
                                    OFF, Vo
–InVc  seguito
           Vo =Viil–condensatore
                        Vc                rimane carico von tensione VM e il diodo è
Viinterdetto
     –• Vc Se>Vi–Vc
                  Vγ > Vγ    D DèèON,
                                    ON, Vo
           Vosi= Vγ,
                  ha C siacarica
 ,Quindi
    il C asiVc carica
                  = Vm - Vγ
                               Vc = Vm -
               vi (t ) ViVcala
    vo•(t )Quando           M    la
 ndo Vi        decresce
           corrente     non può si
 derebbe   invertirsi   e non valela
                  di invertire       più
ente ma    l’ipotesi
                 nonONvale  e quindi
                                  più C
  esi ON   restae carico
                    quindi C resta
co • Vo “segue” Vi traslata di
           Vγ-VM
 segue” Vi traslata di Vγ -
            clamping  (positivo)
                           Clamper
            clamping (positivo)    (positivo)
 dera
 idera   aggiungere
         aggiungere
     Aggiungere           un
                         un
                  un valor  medio
medio
medio    positivo
          positivo
     positivo        aa un
                        un a valor
              a un segnale
 e
 le aa valor   medio nullo
       valornullo
     medio    medio      nullo
mente
mente     (C scarico)
                 è girato se
              scarico)
     • il diodo            seVi
                          per  Vi la
                              cui
e D    Dcorrente
          è OFF,
            OFF,può Id=0,
                       solo Vo
                     Id=0,  Vo==
      scaricare il condensatore,
do
 o Vi Vc
   Vi –  è negativa
      – Vc
        Vc  << -Vγ
               -Vγ DDèè
oo ==• -Vγ,
       -Vγ,  ilil C
        Vo “segue”C si
                    si carica
                       Vi       aadi
                          traslata
                        carica
 Vm ++VVγ,
Vm        Vγ,
          M - Vγ
                 Vo
                 Vo == -Vγ
                        -Vγ
doo  Vi cresce
    Vi   cresce di   di nuovo
                        nuovo    sisi
erebbe di invertire la
 rebbe
nte  ma nondi invertire
                   vale piùla
 te  ma enon
 si ON       quindivaleCpiù
                          resta
si ON e quindi C resta
egue” Vi traslata di Vm -
 gue” Vi traslata di Vm -
uplicatore di tensione  (positivo)
                 Duplicatore di tensione
a cascata
    E’ la cascata  didiun
                        un clamper
 uito   clamping
    positivo             positivo
               e di un rivelatore di
  unpicco:
       rilevatore di picco
    • Il primo condensatore
è visto     che
        trasla     ai capi (valore
                la sinusoide   di
        massimo a 2VM)
 c’è una       sinusoide che
    • il rivelatore di picco trova
da -Vγ      a 2Vm
        il picco  a 2VM -- Vγ
                           Vγ
 api di C2 vi sarà il
co di tale sinusoide,
 ero +2Vm - Vγ
nsione conRegolatore
           diodo          Zen
                     di tensione




   Se Vi*RL/(R+RL)>Vz à D ON (in breakdown) à Vo = Vz

 L /(R+R L ) < -Vγ D ON   Vo =
< Vi*R /(R+R ) < Vz    D OFF
            Looking forward…
                         Porte logiche

• OR: E1 ed E2 segnali
  logici a due livelli (ad
  es. 0 e +5V)
  assimilabili e “0” e “1”
  logici
   – Vo = E1 (OR) E2
   – (Boole) Vo = E1+E2
• NOR:
  AND
   – !Vo = E1 + E2
   – Vo = E1 E2
              .
                                              Diodi reali
     Caratteristiche dei diodi reali




•   Vf: tensione in diretta
•   BV: breakdown voltage in inversa
•   Ir: corrente in inversa
•   Cr: capacità di giunzione in inversa
•   Trr: Recovery time, tempo necessario
    alla formazione della zona svuotata nel
    passaggio da diretta e inversa
                             Effetti reattivi nella giunzione
Caratteristiche statiche (I, V costanti) à Effetti reattivi non vengono considerati
Nella giunzione ci sono diversi tipi di cariche (elettroni, lacune, ioni fissi)
à queste cariche inducono effetti reattivi nella giunzione
à con tensioni e correnti tempo varianti spesso questi effetti non possono
  essere tralasciati
Es.: regione di svuotamento modulata da VD à Q = f(VD) con f non lineare !
        à CONDENSATORE NON LINEARE


• Polarizzazione inversa à molta carica spaziale
• Polarizzazione diretta à molte cariche libere in movimento

Effetti reattivi sostanzialmente diversi nei due casi
à due modelli diversi
                                             Capacità di giunzione
 Polarizzazione inversa à molta carica spaziale
                                                        Si-p       RCS                                      Si-n
    A: area del diodo                               RQN                                                      RQN
                                                                                                                              Regi

   𝑄* = 𝑞𝑁! 𝑥* 𝐴
                                                                U(x)                                         qND               Ca
    𝑊/0. = 𝑥* + 𝑥.                                                               B                                             nu
    𝑁! 𝑥* = 𝑁- 𝑥.                                              A                                                  x            usa
                                                                             qNA                                               Poi
           𝑁! 𝑁-
   𝑄* = 𝑞         𝐴𝑊/0.                                         E(x)                                                             G
          𝑁! + 𝑁-                                        -xp                                           xn
                                                                                                                                 G

   𝑊/0. =
               2𝜀"% 1
                      +
                        1
                          (𝛷1 −𝑉! )
                                                        𝑑𝑄4          1
                𝑞 𝑁- 𝑁!                            𝐶3 =   E = 𝐶35 E(0) = qNAxp =
                                                        𝑑𝑉!
                                                                        𝑉! HSi
                                                                   1−Φ
                                                                                      
                                                                            


          𝑄* = 𝑓(𝑉! )                                                                                         3
funzione non lineare à difficile !
linearizzo (serie di Taylor) à capacità differenziale      CAPACITA’ DI GIUNZIONE
                                           Capacità di diffusione
Polarizzazione diretta à molta carica libera in transito
La carica libera che passa (diffonde) attraverso la giunzione è la principale
responsabile degli effetti reattivi à dipendono dal livello di corrente

      𝑄! = 𝐼! 𝜏 6               𝜏 J à tempo di transito attraverso la giunzione
                    𝑉!
      𝐼! ≅ 𝐼7 6 𝑒𝑥𝑝
                    𝑉89
                                  funzione non lineare à difficile !
      𝑄! = 𝑓(𝑉! )                 linearizzo (serie di Taylor) à capacità differenziale

           𝑑𝑄! 𝜏 6 𝑑𝐼! 𝜏 6 𝐼7       𝑉!    𝜏 6 𝐼!
      𝐶! =     =      =       6 𝑒𝑥𝑝     =
           𝑑𝑉!   𝑑𝑉!    𝑉89         𝑉89    𝑉89
                     CAPACITA’ DI DIFFUSIONE

  Capacità di diffusione e capacità di giunzione hanno impatto sui tempi di
  accensione e spegnimento dei diodi !! à caricare e scaricare capacità !!
