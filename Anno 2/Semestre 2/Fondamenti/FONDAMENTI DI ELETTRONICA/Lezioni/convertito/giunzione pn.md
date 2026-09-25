---
fonte: "giunzione pn.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Giunzione pn
                    e Diodi

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi
                   Francesco Driussi – 2020
                           giunzione.
                                              Giunzione
                         • Il dispositivo elettronico        pn a
                                                      è il diodo
Il dispositivo elettronico più semplice
si basa sulla giunzione pn:
• una regione n-Si e una p-Si
    vengono messe in contatto                         A

• tra le due zone si crea
    un’interfaccia chiamata giunzione
                                   Il diodo a giunzio
                                               A: area della giunzione
Il dispositivo elettronico è chiamato diodo:
• bipolo (due terminali)
• componente non lineare (caratteristica
  corrente-tensione non lineare)
• interruttore pilotato in tensione
                                                   Diodo
  Nel diodo, convenzionalmente:
  •   la corrente ID scorre da anodo a catodo
  •   la tensione VD è quella tra anodo e catodo

                    ID
                                   Il diodo a giunzio
                              VD

o più semplice realizzato con u
 La caratteristica corrente-tensione del
 diodo ideale è qui a destra:

-n è il diodo. Il terminale colleg
 •
 •
      la corrente è sempre positiva
      il diodo si accende per una determinata

 drogata p è il terminale positiv
      tensione V𝛾 detta di «soglia»
 E’ possibile realizzare i diodi con strutture
 diverse: la più semplice è la giunzione pn
 ello collegato alla regione drog
                                                                                     
                                Creazione della giunzione pn
   Cosa succede se metto in contatto n-Si con p-Si?
                                                                    Idiff




                                                   Gli enormi gradienti di concentrazione
       p ≃ NA                                      innescano la diffusione di:
                                 n ≃ ND
                                                   • lacune da p-Si a n-Si
          𝑛!"                       𝑛!"
       𝑛≃                        𝑝≃                • elettroni da n-Si a p-Si
          𝑁#                        𝑁$
                                                   Corrente di diffusione non nulla

VRORXQ  DQWHSULPD
   • Ma il processo non può durare all’infinito altrimenti la giunzione sparirebbe
     • Giunzione all’equilibrio termodinamico à energia costante (VD=0, ID=0)
PRVWUDWHVXWRWDOL
  • All’equilibrio, la corrente deve essere nulla !!
     • Cosa auto-limita il processo evitando che la giunzione sparisca?
                                            Cariche fisse e mobili
• Nel silicio drogato gli ioni di drogante donore (accettore) rilasciano elettroni
  (lacune) à carica mobile (portatori maggioritari liberi)
• Gli atomi di drogante si ionizzano à carica fissa (bloccata nel reticolo cristallino)
• Normalmente il materiale è neutro à carica fissa e mobile si compensano !!
• Se la carica fissa se ne va dal materiale, la carica fissa non è più compensata
  e il materiale risulta carico
• Nella giunzione pn, la diffusione dei portatori liberi lascia scoperta la carica
  fissa in prossimità della giunzione
                                       Regione di svuotamento
La regione a ridosso della giunzione si svuota di portatori liberi
à regione di svuotamento (svuotata dalle cariche mobili) o regione di
  carica spaziale (è presente carica fissa non compensata)
•   Nella zona p-Si è presente carica fissa negativa
•   Nella zona n-Si è presente carica fissa positiva
                                             Si-p          RCS            Si-n
•   Materiale neutro: la carica TOTALE
    deve continuare ad essere nulla         RQN                           RQN
    (non ho né aggiunto né tolto carica)
•   L’estensione nel p-Si e n-Si dipende
    dai livelli di drogaggio NA e ND                    U(x)              qND
Ipotesi di svuotamento a completo:                                   B
         A = B à qNAxP = qNDxn                                                x
                                                       A
•   La reg. di svuot. si estende di più                          qNA
    nella regione con meno drogante
                                              -xp       E(x)
                   𝒙𝒑 𝑵𝑫                                                 xn
                     =
                   𝒙𝒏 𝑵𝑨
                                Giunzione pn all’equilibrio
La carica spaziale crea un campo elettrico (E) !!
•
                                  La giunzione pn all’equi
    Il campo elettrico muove le cariche libere inducendo una corrente di deriva
•   La corrente di deriva va in verso opposto a quella di diffusione

                                                     Ideriva                      Si
                                                                                  un
• Si raggiunge l’equilibrio
  termodinamico quando la          deriva                                         di
  corrente totale è nulla                               E                         di
           Itot = 0                                                               qu
                                        Si-p                           Si-n       co
• Si instaura un equilibrio
  dinamico in cui le correnti
                                                                                  co
  di diffusione e deriva si                                                       bi
  compensano                                                                      qu
         Idiff = Ideriva
                                 diffusione
                                                       Idiff
                      Campo elettrico nella giunzione
Per trovare quanto vale il campo elettrico posso usare la legge di Gauss:
       𝑑𝐸   𝜌
          =                                Si-p         RCS                                      Si-n
       𝑑𝑥 𝜀%!
                                          RQN                                                     RQN
            1                                                                                                      R
     𝐸 𝑥 =     , 𝜌 𝑥 𝑑𝑥
           𝜀%!
                                                     U(x)                                         qND

• Se assumiamo lo svuotamento                                         B
  completo (nessuna carica libera),
                                                                                                       x
  E ha un andamento lineare                         A
                                                                  qNA
• Il campo elettrico è massimo in
  corrispondenza della giunzione            -xp     E(x)
                                                                                            xn
• Il valore massimo dipende dalla
  quantità di carica fissa nella zona
  di svuotamento (drogaggio)                                                   qNAxp
                                                    E                   E(0) =
                                                                                HSi
                                                                           
                                                                 
    RQN                                Potenziale nella giunzione
     L’equazione di Poisson ci consente di calcolare il profilo di potenziale:
                    Usando l’eq. di
xn                                           Si-p           RCS                   Si-n
                    Poisson:
                    GI                       RQN                                  RQN
                       = -E(x)
                    Gx
                                               -xp      E(x)                     xn
           Barriera di
           potenziale
    • Il profilo di potenziale
                           V0 ha andamento
        parabolico
                     kT    N N
                          D A
    • E’   =
       Vl’unione
         0
                 diln(
                    due parabole   )  con
              q
      concavità verso     n
                       l’altoi
                               2e verso il basso
                                                                  E(0)
                  del n-Si
                                                                                         B
  • Il potenziale
                E(0)    (xn emaggiore
                              xp )     di
          V0del p-Si à differenza di
     quello
ttrico=
                                                                                         p
     potenziale Fj
 
                         2



    • Fj è il potenziale di barriera                                                  V0𝒋 =
                                                                                      𝜱
        (o di built-in) à nel Si è 0.5÷1 V
                                             Potenziale di built-in

                                                   pnla giunzione
Il potenziale di built-in fa da barriera di potenziale e si oppone alla
diffusione delle cariche à mantieneGiunzione
                                         in equilibrio  regione di
                                                                    svuota
Il campo elettrico è noto à RisolvendoGiunzione      pn
                                      l’equazione di Poisson
                                                     W dep
                                                            regione     di
                                                             posso calcolare
                                                                    W  dep
il potenziale di barriera                      xp              xn svuotam
                                                       N               N
                                𝑥% + 𝑥           pn,  1   𝑥   + 𝑥          1 
                                                             A                    D
                                   Giunzione
                                       &                Wregione
                                                            %     & di W
             Φ$ = 𝐸 𝑥 = 0                 = 𝑞𝑁     ' 𝑥 %   N
                                                           dep                  NA
                                                                                dep
                                   2            xp           D
                                                               2 xnsvuotament
              Giunzione pn regione
                                                        W NA                    ND
                                           p-Si di    1                    1
                                                                        dep
                                                                       n-Si
La larghezza della zona di svuotamento (depletion)    è Se
                                                        WN  NDA>>N D, allora
                                                               =xp+x  nRQN xN   p<<x
                                          svuotamento
                                          RQN              dep                    A n
                                          (la regione di svuotamento si estende quas
   𝑥% 𝑁(                       Wdep              Wdep               nella regione n)
     =                   xp               xn      -xp      Se   N  A>>ND, nallora xp<<xn
                                                                             x
   𝑥& 𝑁'                         NA                 ND di svuotamento
                                           (la regione                        si estende
                                                                                   x       quas
                              1                1               0
                                                           Se NA<<ND, allora xp>>xn
                                 ND                 NA              nella regione n)
                                          (la regione  di svuotamento
                                                            2H s § 1      1 si· estendexn quas
                                                                                            NA
                                          Wdep xp  xn                 
                                                                 ¨ nella regioneV
                                                                              ¸ 0     p)
                                                             q     N
                                                           Se N© <<N     N D, ¹allora xx>>x ND
                2𝜀+, 1          1Se NA>>ND, allora xp<<xn         A  A
                                                                        D         p     np

    𝑊)*% =       (la regione+        𝛷$ (la
                             di svuotamento     regionequasi
                                            si estende  di svuotamento
                                                             interamente si estende quas
                                                                                  
                                                                          
                                                                                                 
                                                                                         


                 𝑞 𝑁' 𝑁( nella regione       Hs = 1.04
                                                   n) 10 F/cm nella
                                                        -12         0.1Pregione  d 1P m
                                                                        m d Wdep p)
                                                                         
                                                               

                                                                                                  
                                Componenti della corrente
Il potenziale di built-in fa da barriera di potenziale e si oppone alla diffusione
delle cariche à mantiene in equilibrio la giunzione (I = 0)
Equilibrio à Non solo la corrente totale è nulla, ma anche quelle dei soli
elettroni e delle sole lacune !!

  ̅
 𝐽&,./.    ̅
        = 𝐽&,)0,1.    ̅
                   + 𝐽&,),11 = 𝑞𝜇& 𝑛𝐸2 + 𝑞𝐷& ∇𝑛 = 0

  ̅
 𝐽%,./.    ̅
        = 𝐽%,)0,1.    ̅
                   + 𝐽%,),11 = 𝑞𝜇% 𝑝𝐸2 − 𝑞𝐷% ∇𝑝 = 0

Il campo elettrico e il potenziale sono noti à equazioni differenziali nelle
concentrazioni di elettroni e lacune à soluzioni in forma esponenziale
                         𝑞Φ
   𝑝 Φ = 𝑝 Φ = 0 0 𝑒𝑥𝑝 −
                         𝑘& 𝑇
                                                          𝑁' 𝑁(
   𝑝 Φ = 0 = 𝑁#                                Φ$ = 𝑉.2 ln 3
                                                           𝑛,
            𝑛!"
   𝑝 Φ'   =
            𝑁$
      Concentrazioni di equilibrio
                                       𝑞Φ
                      𝑝 Φ = 𝑁# 0 𝑒𝑥𝑝 −
                                       𝑘& 𝑇
                            𝑛!"       𝑞Φ
                      𝑛 Φ =     0 𝑒𝑥𝑝
                            𝑁#        𝑘& 𝑇
                                               𝑛()
                      𝑝 Φ = 0 = 𝑁&   𝑝 Φ'    =
                                               𝑁*
                              𝑛()
                      𝑛 Φ=0 =        𝑛 Φ' = 𝑁*
                              𝑁&




             𝛷 = 𝛷!
        𝛷$
𝛷=0
                                   Giunzione fuori equilibrio

 • L’applicazione di una tensione al diodo/giunzione porta fuori equilibrio il
   sistema e una corrente può scorrere nel dispositivo
Polarizzazione                         della
à Sbilancio delle correnti di diffusione e deriva! giunzione p-
                                                   (non sono più uguali)

                                                      ID
 VD > 0 à POLARIZZAZIONE DIRETTA


 VD < 0 à POLARIZZAZIONE INVERSA

                                                                   D



 La tensione esterna modifica il potenziale lungo il dispositivo
 à Cambia il campo elettrico ai capi della giunzione !!
 à Modifica la corrente di drift
                                                 Polarizzazione inversa
                            Polarizzazione della giunzione p
 VD < 0 à Aumenta il potenziale della zona n-Si rispetto alla zona p-Si

 All’equilibrio la zona n-Si è già a potenziale maggiore
 rispetto a p-Si à VD aumenta la differenza di potenziale
                                                                                             D

      inversa
                                        (Φ' − 𝑉$ )
      equilibrio
                                                 •   La giunzione pn in inversa vede
                                                     aumentare il potenziale di barriera
                                                 •  Se aumenta il salto di potenziale,
                                 Φ'
olarizzazione della giunzione p-n
                        •
                                                    aumenta anche il campo elettrico
                            La giunzione p-n in inversa vede aumentare il potenziale di barriera, aumenta
                                                    sullail giunzione
                            cariche fisse all’interfaccia,  passaggio di corrente è trascurabile: capacità
                             –   Diodi Varicap
                        •   La giunzione p-n •in diretta
                                                   Chi vede
                                                         produce     il campo
                                                              diminuire            elettrico?
                                                                        il potenziale di barriera, le cariche f
                            all’interfaccia diminuiscono per cui è permesso il passaggio di portatori       cor
                            conduzione         à Le cariche fisse all’interfaccia
one p-n in inversa vede aumentare
                            à Ho più caricailfissa
                                               potenziale di ba
sse all’interfaccia, il passaggio
                            à Zona di  corrente èpiùtrascurab
                                    di svuotamento     larga !!
                              Corrente inversa di saturazione
                                   Polarizzazione della giunzione p
VD < 0 à Aumenta il campo elettrico sulla giunzione
                                                                                        ID
•   Incentiva la corrente di deriva rispetto alla diffusione
•   La diffusione vede una barriera di potenziale alta
           Idrift > Idiff                                                                         D


La corrente di deriva è dovuta ai portatori                        La giunzione pn all’eq
minoritari !!
                                                                                       Ideriva
•   Lacune dalla zona n-Si
•   Elettroni dalla zona p-Si                                       deriva
Concentrazioni bassissime, poche cariche                                                  E
                               •   La giunzione p-n in inversa vede aumentare il potenziale di barriera, aumenta
                                                                            Si-p
                                   cariche fisse all’interfaccia, il passaggio                             Si-n
                                                                               di corrente è trascurabile: capacità
à DENSITA’ CORRENTE–MOLTO       PICCOLA
                     Diodi Varicap
                               •
                            La giunzione p-n in diretta vede diminuire il potenziale di barriera, le cariche f
    (trascurabile e praticamente
                            conduzione
                                      costante)
                            all’interfaccia diminuiscono per cui è permesso il passaggio di portatori      cor

Densità di corrente inversa di saturazione JS
Corrente inversa di saturazione IS =AJS (≪ pA) diffusione ID = - IS < 0
                                                                                         Idiff
                                                      Polarizzazione diretta
                             Polarizzazione della giunzione p
  VD > 0 à Aumenta il potenziale della zona p-Si rispetto alla zona n-Si

  All’equilibrio la zona n-Si è a potenziale maggiore
  rispetto a p-Si à VD riduce la differenza di potenziale
                                                                                              D

       diretta
       equilibrio
                                     Φ'           •   La giunzione pn in diretta vede
                                                      diminuire il potenziale di barriera
                                                  •  Se diminuisce il salto di potenziale,
                             (Φ' − 𝑉$ )
                                                     cala anche il campo elettrico sulla
della giunzione p-n      •   La giunzione p-n in inversa vede aumentare il potenziale di barriera, aumenta
                                                     giunzione
                             cariche fisse all’interfaccia,
                              –   Diodi Varicap
                                                            il passaggio di corrente è trascurabile: capacità

                         •   La giunzione p-n •in diretta
                                                    Cosa     riduce
                                                          vede        il campo
                                                               diminuire            elettrico?
                                                                         il potenziale di barriera, le cariche f
                             all’interfaccia diminuiscono per cui è permesso il passaggio di portatori       cor
 potenziale di barriera, aumentano le
                             conduzione         à Le cariche fisse all’interfaccia
 ente è trascurabile: capacità
                           à Ho più meno fissa
                                                  à Zona di svuotamento più stretta !!
                      Corrente in polarizzazione diretta
                              Polarizzazione della giunzione p
VD > 0 à Riduce il campo elettrico sulla giunzione
                                                                                     ID
•   Riduce la corrente di deriva rispetto alla diffusione
•                                               La
    La diffusione vede una barriera di potenziale piùgiunzione
                                                      bassa    pn all’equ
         Idrift < Idiff                                                           Ideriva                  D


La corrente di diffusione è dovuta ai portatori deriva
maggioritari !!                                                                      E
•   Lacune dalla zona p-Si                                         Si-p                                           Si-n
•   Elettroni dalla zona n-Si
Concentrazioni alte, alti gradienti
                          •   La giunzione p-n in inversa vede aumentare il potenziale di barriera, aumenta
                              cariche fisse all’interfaccia, il passaggio di corrente è trascurabile: capacità
à DENSITA’ CORRENTE– MOLTO        ALTA
                      Diodi Varicap
                                                            diffusione
                          •   La giunzione p-n in diretta vede  diminuire il potenziale di barriera, le cariche f
                                                                                    Idiff di portatori cor
                              all’interfaccia diminuiscono per cui è permesso il passaggio
                              conduzione
                 ID >> 0                                                                     
                                                                                     
                                                                                                            
                                                                                                    
                                                  Modello della corrente
   Hp: assumo che valgano le concentrazioni di equilibrio anche fuori equilibrio

                          𝑞Φ                                   𝑛!"       𝑞Φ
         𝑝 Φ = 𝑁# 0 𝑒𝑥𝑝 −                                𝑛 Φ =     0 𝑒𝑥𝑝
                          𝑘& 𝑇                                 𝑁#        𝑘& 𝑇


                                                 Posso calcolare i gradienti di concentrazione
                                   Φ'
                                                          Jtot ≅ Jdiff
                              (Φ' − 𝑉$ )

                                                                 𝐷-    𝐷.         𝑞𝑉*
                                                 𝐽+(,, = 𝑞𝑛()        +      > 𝑒𝑥𝑝      −1
e il potenziale di barriera, aumentano le                       𝐿- 𝑁& 𝐿. 𝑁*       𝑘/ 𝑇
 orrente è trascurabile: capacità
                               𝑉(                                                        𝑘& 𝑇
        𝐼( = 𝐴 = 𝐽+ = 𝑒𝑥𝑝             −1               JS                          𝑉() =
 potenziale di barriera, 𝑉le.2cariche fisse                                               𝑞
sso   il passaggio di portatori            corrente di
   Modello teorico della corrente nella giunzione          Ln: lunghezza di diffusione degli elettroni
           A: area della giunzione                         Lp: lunghezza di diffusione delle lacune
           JS: densità di corrente saturazione
                                                          Corrente nel diodo
                       ID                                    Vth = 25.6 mV a T = 300 K

                                                             n : fattore di idealità (1.0÷1.1)
                                VD
o più semplice           𝑉     realizzato
                                    $             𝑉      con una
                                                             $
     𝐼 = 𝐴 0 𝐽 0 𝑒𝑥𝑝
          $        %          − 1 = 𝐼 0 𝑒𝑥𝑝       %     −1
 -n è il diodo. Il terminale collegato
                        𝑛𝑉          ()           𝑛𝑉          ()


  drogata          p è il terminale positivo
     es.: A = 100 µm ; J = 1 nA/cm à I = 1 fA (cmq dipende da N e N )
                            2
                                S
                                              2
                                                      S                          A    D



uello collegato alla regione drogata n
     1. V = 0 à I = 0
               D            D


     2. V < 0 à I ≅ -I
 e negativo (catodo).
               D            D  (trascurabile; descrive bene la polarizzazione inversa)
                                    S


         3. VD > 0 à ID > 0                                       In polarizzazione diretta la
                                                       𝑉$         corrente cresce
              se VD > 3 Vth à            𝐼$ ≅ 𝐼% 0 𝑒𝑥𝑝            esponenzialmente con la
                                                       𝑉()
                                                                  tensione !!
                     Caratteristica statica del diodo
              ID                           Vth = 25.6 mV a T = 300 K
                                           n = 1.0


                    VD                                 𝑉$
                                         𝐼$ = 𝐼% 0 𝑒𝑥𝑝     −1
                                                       𝑉()
o più semplice realizzato con una
 -n è il diodo. Il terminale
                      • Il diodo è un collegato
                                       elemento che fa
                        passare la corrente solo in un verso
  drogata p è il terminale           positivo
                                ID ≥ 0
uello collegato alla regione              drogata
                      • La caratteristica somiglia a quella
                                                              n
 e negativo (catodo).del     diodo ideale introdotta all’inizio
                         delle slide !
                                 • Interruttore pilotato in tensione
                                   Caratteristica statica in diretta
                    ID                                       VD > 3Vth ≅ 75 mV
                                                             n = 1.0

                                                                           𝑉$
                              VD                             𝐼$ ≅ 𝐼% # 𝑒𝑥𝑝
                                                                           𝑉()
o più semplice realizzato          con una
                        • La corrente ha dipendenza
 -n è il diodo. Il terminale        collegato
                          esponenziale dalla corrente
                        • In scale semilogaritmiche la curva
  drogata p è il terminale positivo
                          diventa una retta


uello collegato alla regione drogata n
 e negativo (catodo).
             𝑉         𝑉       *                        *
  log 𝐼* = log 𝐼0 + log 𝑒𝑥𝑝         = log 𝐼0 + 2.3 >
                              𝑉12                      𝑉12

    La corrente aumenta di un ordine di
    grandezza ogni 60 mV
                       Dipendenza da IS e temperatura
                ID                                         𝑉$
                                             𝐼$ = 𝐼% # 𝑒𝑥𝑝     −1
                                                           𝑉()

                      VD
                                            • La corrente nel diodo dipende
o più semplice realizzato con una             chiaramente dal valore di IS
  • La corrente nel diodo dipende dalla        I = AJ
      è il diodo.
 -ntemperatura                Il terminale
                 di funzionamento             collegato
                                        à dipende
                                                       S       S

                                                  da area e drogaggio
    attraverso due termini:
  drogata      𝑘 𝑇 p è il terminale positivo
                &
  1.     𝑉 =
           ()           à T riduce I
uello collegato alla regione
                𝑞                   D
                                          𝐼 = 𝐴𝑞𝑛drogata
                                               0
                                                     𝐷
                                                    𝐿 𝑁
                                                        +
                                                           𝐷
                                                           )
                                                           (
                                                          𝐿 𝑁  - &
                                                                  n-     .

                                                                        . *

 e2.negativo
       I dipende da T à
       S                 (catodo).
                           T aumenta I  S                        +,+"
                                                     𝐼% = 𝐼%* # 2 -*
                                                   IS raddoppia ogni 10 K
   Chi domina? à domina la
                 dipendenza di IS
                      Dipendenza dalla temperatura
              ID                                    𝑉$
                                      𝐼$ = 𝐼% # 𝑒𝑥𝑝     −1
                                                    𝑉()

                    VD
o più semplice realizzato con una
          il diodo.
 -n• Laècorrente                Il terminale
                  nel diodo aumenta     con la    collegato
     temperatura di funzionamento!!
  drogata            p    è    il
   Fissiamo un valore di corrente
                                   terminale     positivo
uello     collegato
   à all’aumentare                alla
                      di T la tensione
                              D            regione
                                        V sul
   diodo utile ad ottenere quel livello di
                                                   drogata  n
 e corrente
    negativo              (catodo).
             cala linearmente    con T !
           𝑑𝑉$
               = −1.8 𝑚𝑉/𝐾
           𝑑𝑇
                                           Diodo in inversa
               ID                    Con tensioni negative possiamo
                                     considerare il diodo come SPENTO
                                     e la sua corrente trascurabile
                        VD                        𝐼( ≅ 0
o più semplice realizzato      Questo valecon       una V < 0?
                                            per qualunque      D


 -n è il diodo. Il terminale               collegato
                               NO à tensione     massima negativa
                               detta tensione di breakdown, altre la
  drogata p è il terminale               positivo
                               quale il diodo si «rompe» e la
                               corrente aumenta drammaticamente
uello collegato alla regione drogata n
 e negativo    (catodo).
         V o V tensione di breakdown = 2 ÷ 200 V
              BK    Z


            valori molto diversi, da cosa dipende? NA, ND
                                                 Breakdown del diodo
  • Con basso drogaggio à VBK elevata                          > 5.6 V

  Tensioni elevate che accelerano le cariche che sbattono contro i legami del reticolo
      Polarizzazione                    inversa
  e creano ulteriori coppie elettrone-lacuna à Moltiplicazione a valanga
  Evento distruttivo à il diodo si rompe definitivamente             (ma VBK elevata; difficile)

La corrente nella struttura è molto
   • Con
debole,  in quanto      cariche libereà VBK bassa
                altoledrogaggio                                     < 5.6 V
disponibili per la conduzione sono solo
i portatori minoritari nelle rispettive
   La regione
regioni,           svuotata è stretta à campo elettrico molto alto anche con bassa
         in concentrazione
estremamente limitata. Tali portatori
   tensione
generano        à una
            quindi  si creano      coppie elettrone-lacuna per effetto tunnel à Effetto Zener
                         piccolissima
corrente
   Evento      non ISdistruttivo à il diodo non si rompe, anzi può funzionare in
           inversa
Se si aumenta la tensione inversa
   questo
applicata      regime
           al diodo,  in corrispondenza di
un certo valore si verifica il fenomeno
del breakdown del diodo, che
   à DIODI
consiste          ZENER
          in un aumento       notevolissimo
della corrente inversa che scorre nel
diodo rispetto al valore IS della
   • caratteristica
corrente  di saturazionemolto inversa.Tale
                                    ripida
valore di tensione VZ viene detto
   • VDtensione
appunto               di breakdown del
            = -VBK praticamente          costante
diodo.
   à Zener:
Diodi  generatore
               sfruttanodi iltensione
                               breakdowncostante
per generare un riferimento di tensione
                                                    Diodo Zener
VBK < 5.6 V



DIODI ZENER utilizzati per generare tensioni di riferimento costanti
à lavorano nella regione di breakdown
à valore stabile che non dipende dalla tensione di alimentazione
