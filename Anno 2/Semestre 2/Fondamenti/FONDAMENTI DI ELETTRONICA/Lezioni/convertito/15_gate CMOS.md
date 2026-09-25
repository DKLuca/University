---
fonte: "15_gate CMOS.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Porte logiche statiche CMOS

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                                         Inverter CMOS
• L’utilizzo combinato di n-MOSFET e p-MOSFET per la realizzazione di circuiti digitali
  ha portato allo sviluppo della tecnologia Complementary-MOS (CMOS)
• L’inverter CMOS è il gate più semplice à utilizza un n-MOSFET e un p-MOSFET

                             VTn > 0; VTp < 0;

                 Mp



                 Mn



• Se il p-MOSFET conduce (nMOSFET OFF),
  l’uscita viene connessa alla tensione di
  alimentazione à «1» logico (logica positiva)
• Quando il n-MOSFET conduce (pMOSFET            VT,P
  OFF), l’uscita viene connessa alla tensione
  di massa à «0» logico (logica positiva)                         VLT
                           Porte logiche statiche CMOS
• Questo schema di connessione all’alimentazione e al riferimento di massa
  può essere generalizzato a qualunque tipo di funzione logica F(I1, I2, …, In):
1. Rete di PULL-UP (PU) à connette l’uscita alla tensione di alimentazione
   quando F = 1
2. Rete di PULL-DOWN (PD) à connette l’uscita alla tensione di massa
   quando F = 0
•   Le reti di PU e di PD devono essere complementari, in modo che l’uscita
    sia collegata a solo una delle due tensioni di riferimento (VDD o massa)
Reti complementari à Sfrutto dispositivi complementi (n-MOSFET e p-MOSFET)
à Complementary-MOS (CMOS)
1. PULL-UP formato da p-MOSFET
2. PULL-DOWN formato da n-MOSFET
es.: inverter CMOS: PU con 1 p-MOSFET, PD con 1 n-MOSFET
               Schema delle porte logiche CMOS
   Inverter CMOS                    Generica porta statica CMOS




Le porte logiche così costruite prendono il nome di STATICHE perché il loro
funzionamento si basa sul comportamento statico del circuito
                  Schema delle porte logiche CMOS
Complementary-MOS (CMOS) à schema generale:
1. PULL-UP formato da p-MOSFET
2. PULL-DOWN formato da n-MOSFET
3.   I1, I2, …, In ingressi à pilotano direttamente SOLO i gate dei MOSFET
4. MOSFET visti come INTERRUTTORI à ON/OFF
• n-MOSFET: ON quando pilotato da «1» logico / OFF quando pilotato da «0»
• p-MOSFET: ON quando pilotato da «0» logico / OFF quando pilotato da «1»
• Quando il MOSFET è ON à VDS = 0 per consentire all’uscita di portarsi alle
  tensioni di riferimento à funzionamento in regime TRIODO
5. PRODOTTO BOOLEANO tra le variabili di ingresso à SERIE di MOSFET
        à due transistor in serie conducono solo se entrambi sono ON
6. SOMMA BOOLEANA tra le variabili di ingresso à PARALLELO di MOSFET
         à due transistor in parallelo conducono se almeno uno è ON
                               Reti di Pull-Up e di Pull-Down
Generica funzione logica 𝐹(𝐼! , 𝐼" , … , 𝐼# )
PULL-UP (PU) à responsabile di generare F = 1
•   Deve connettere l’uscita con VDD.
•   Formato da p-MOSFET à conducono quando l’ingresso 𝐼$ connesso al
    loro gate è basso («0» logico) à «0» ≡ ON à conduzione descritta da 𝐼'$
•   Se descrivo la sua conducibilità attraverso una funzione booleana
    (PU=1 à conduce): 𝑃𝑈(𝐼'! , 𝐼'" , … , 𝐼'# ) = 𝐹(𝐼! , 𝐼" , … , 𝐼# )

PULL-DOWN (PD) à responsabile di generare F = 0
•   Deve connettere l’uscita con massa.
•   Formato da n-MOSFET à conducono quando l’ingresso 𝐼$ connesso al
    loro gate è alto («1» logico) à «1» ≡ ON à conduzione descritta da 𝐼$
•   Se descrivo la sua conducibilità attraverso una funzione booleana
    (PD=1 à conduce): 𝑃𝐷(𝐼! , 𝐼" , … , 𝐼# ) = 𝐹(𝐼! , 𝐼" , … , 𝐼# )

Le reti di PU e PD sono incorrelate tra loro à 𝑃𝐷(𝐼! , 𝐼" , … , 𝐼# ) = 𝑃𝑈(𝐼'! , 𝐼'" , … , 𝐼'# )
                           Esempio: porta logica NAND
Funzione logica NAND: 𝐹 𝐴, 𝐵 = 𝐴 . 𝐵

                                       PULL-UP (PU)       𝑃𝑈 𝐴,̅ 𝐵& = 𝐹 𝐴, 𝐵
                                       responsabile di
                                       generare F = 1



                                       PULL-DOWN (PD)
                                       responsabile di
                                                          𝑃𝐷 𝐴, 𝐵 = 𝐹 𝐴, 𝐵
                                       generare F = 0

Implementazione à PRODOTTO ≡ SERIE di MOSFET
                 à SOMMA ≡ PARALLELO di MOSFET

𝑃𝐷 𝐴, 𝐵 = 𝐹 𝐴, 𝐵 = 𝐴 . 𝐵 à serie di n-MOSFET

𝑃𝑈 𝐴,̅ 𝐵0 = 𝐹 𝐴, 𝐵 = 𝐴 . 𝐵 à questa funzione non è direttamente
implementabile tramite serie e parallelo di transistori
                       Esempio: porta logica NAND
Funzione logica NAND: 𝐹 𝐴, 𝐵 = 𝐴 . 𝐵

                           𝑃𝐷 𝐴, 𝐵 = 𝐴 . 𝐵 à serie di n-MOSFET

                           𝑃𝑈 𝐴,̅ 𝐵0 = 𝐹 𝐴, 𝐵 = 𝐴 . 𝐵 = 𝐴̅ + 𝐵0
                           à sfrutto le leggi di De Morgan
                           à questa è una funzione nelle variabili 𝐴̅ e
                              𝐵0 che sono quelle che descrivono la
                              conducibilità dei p-MOSFET
                           𝑃𝑈 𝐴,̅ 𝐵0 = 𝐴̅ + 𝐵0 à parallelo di p-MOSFET
                           pilotati da A e B !!
                              Esempio: porta logica NOR
Funzione logica NOR: 𝐹 𝐴, 𝐵 = 𝐴 + 𝐵

                                    𝑃𝑈 𝐴,̅ 𝐵0 = 𝐹 𝐴, 𝐵 = 𝐴 + 𝐵 = 𝐴̅ . 𝐵0
                                    à serie di p-MOSFET pilotati da A e B

                                    𝑃𝐷 𝐴, 𝐵 = 𝐹 𝐴, 𝐵 = 𝐴 + 𝐵
                                    à parallelo di n-MOSFET




PU e PD sono duali rispetto a
funzionamento, ma anche per                     𝐹
                                                                    𝐹
implementazione (serie/parallelo)
Entrambi pilotati dai segnali A e B !
                            Sintesi ed analisi dei gate CMOS
•    L’implementazione di funzioni logiche con circuito digitale è detta SINTESI
FUNZIONE à CIRCUITO
1.    𝑃𝐷(𝐼! , 𝐼" , … , 𝐼# ) = 𝐹(𝐼! , 𝐼" , … , 𝐼# )
2. Somma ≡ parallelo di MOSFET; prodotto ≡ serie di MOSFET
3.    PU è duale rispetto al PD à serie di MOSFET trasformata in parallelo;
      parallelo di MOSFET trasformato in serie
oppure:
1.    𝑃𝑈(𝐼'! , 𝐼'" , … , 𝐼'# ) = 𝐹(𝐼! , 𝐼" , … , 𝐼# )
2. Somma ≡ parallelo di MOSFET; prodotto ≡ serie di MOSFET
3.    PD è duale rispetto al PU à serie di MOSFET trasformata in parallelo;
      parallelo di MOSFET trasformato in serie


ANALISI di una porta logica à estrazione della funzione logica implementata
                              Esempio: porte AND e OR

                                 𝑃𝐷 𝐴, 𝐵 = 𝐹 𝐴, 𝐵 = 𝐴 . 𝐵 = 𝐴̅ + 𝐵0
                                 à non è esprimibile in prodotti o somme di 𝐴 e 𝐵

                                 𝑃𝑈 𝐴,̅ 𝐵0 = 𝐹 𝐴, 𝐵 = 𝐴 + 𝐵
                                 à non è esprimibile in prodotti o somme di 𝐴̅ e 𝐵&

                                 𝑃𝐷 𝐴, 𝐵 = 𝐹 𝐴, 𝐵 = 𝐴 + 𝐵 = 𝐴̅ . 𝐵0
                                à non è esprimibile in prodotti o somme di 𝐴 e 𝐵

                                 𝑃𝑈 𝐴,̅ 𝐵0 = 𝐹 𝐴, 𝐵 = 𝐴 . 𝐵
                                à non è esprimibile in prodotti o somme di 𝐴̅ e 𝐵&

•   Le logiche statiche CMOS sono intrinsecamente invertenti à non riesco
    a sintetizzare la AND e la OR à Utilizzo NAND e NOR + un inverter !!
•   Inverter è molto importante per le logiche CMOS
                                           Esempio: porta XOR
Funzione logica XOR (OR esclusivo) 𝐹 𝐴, 𝐵 = 𝐴̅ . 𝐵 + 𝐴 . 𝐵0 = 𝐴 ⊕ 𝐵

    𝐴   𝐵   𝐴⊕𝐵
                           𝑃𝑈 𝐴,̅ 𝐵0 = 𝐹 𝐴, 𝐵 = 𝐴̅ . 𝐵 + 𝐴 . 𝐵0 = 𝐴̅ . 𝐵0 + 𝐴̅ . 𝐵0
                          à non è esprimibile in prodotti o somme di 𝐴̅ e 𝐵&
                          à ho bisogno anche degli ingressi negati

                           𝑃𝐷 𝐴, 𝐵 = 𝐹 𝐴, 𝐵 = 𝐴̅ . 𝐵 + 𝐴 . 𝐵0 = 𝐴̅ . 𝐵 . 𝐴 . 𝐵0
                                          0 . (𝐴̅ + 𝐵)
                           𝑃𝐷 𝐴, 𝐵 = (𝐴 + 𝐵)
                          à non è esprimibile in prodotti o somme di 𝐴 e 𝐵
                          à ho bisogno anche degli ingressi negati



•   Per produrre gli ingressi negati ho bisogno di inverter
•   Inverter è molto importante per le logiche CMOS
                                 Esempio: porta XOR
                                                 :KDW¶VWKH)XQFWLRQ
Funzione logica XOR (OR esclusivo) 𝐹 𝐴, 𝐵 = 𝐴̅ . 𝐵 + 𝐴 . 𝐵0 = 𝐴 ⊕ 𝐵
                                                 &0261HWZRUN"
                                                  9GG




                                                           &𝐹




 𝑃𝑈 𝐴,̅ 𝐵0 = 𝐴̅ . 𝐵0 + 𝐴̅ . 𝐵0

                0 . (𝐴̅ + 𝐵)
 𝑃𝐷 𝐴, 𝐵 = (𝐴 + 𝐵)



                                  
                                                                                                    .QIKP £


                      5GCTEJ                     Esempio: porta XOR                    5GCTEJ


                                                  :KDW¶VWKH)XQFWLRQ
 Funzione logica XOR (OR esclusivo) 𝐹 𝐴, 𝐵 = 𝐴̅ . 𝐵 + 𝐴 . 𝐵0 = 𝐴 ⊕ 𝐵
                                                  &0261HWZRUN"
                                                 0 . (𝐴̅ + 𝐵)
• I due circuiti                  <HW$QRWKHU;25&0261HWZRUN
                                  𝑃𝐷 𝐴, 𝐵 = (𝐴 + 𝐵)  9                            GG

  sono equivalenti                       9GG                          $       %        &
                                                                                     =
• Più reti                                                3XOO8S
                                                                                     
  equivalenti                                             1HWZRUN
                                                                                     
  implementano la
                                                                                     =
  stessa funzione!!
                                                                      $       %        &            &𝐹
• Traduzione di                                                                      
                                                     &    3XOO'RZQ
  somma e                                            𝐹
                                                          1HWZRUN                    =
  prodotto con                                                                       =
  serie e parallelo                                                                  
  non porta
                                                                      $       %        &
  sempre a rete
                                                                                     
  MINIMA                                                  &RPELQHG
                                                          &026                            )XQFWLRQ ;25
                                                                                                        ;25
• PU e PD non                                  un collegamento
                                                          1HWZRUN                    
  sono duali !!                                in meno!                              
                                                     
          ([DPSOH
              ([DPSOH
               Esempio: funzione generica             9GG
                                                  9GG
                                     $                &                 $
                                     $            &             $
 1. Parto da PU à 𝑃𝑈 = 𝐹
6WDUWIURPWKHLQQHUPRVWWHUP
     6WDUWIURPWKHLQQHUPRVWWHUP
 2. Devo   evidenziare gli
                                         %%                     '
                                                                        '
    ingressi negati !!
 3. Faccio il PD duale
 oppure
                                                            '
 1. Parto da PD à 𝑃𝐷 = 𝐹0                 $$                        '
 2. Devo negare la funzione
 3. Faccio il PU duale                        $
                                          $                 %
                                              &                     %
                                          &

                                                                  ++6/HH
                                                    Analisi di una rete
H
                                                     ([DPSOH
              9GG                   1.      Analizzo il PU à 𝑃𝑈 = 𝐹
      (             '               2.      p-MOSFET rappresentati dagli ingressi
                                            in forma negata
P                                  3XOO8S
      $       &     $              1HWZRUN
                                                                               (
          %         '
                               )       6WDUWIURPWKHLQQHUPRVWWHUP
                                    oppure
                                    1.      Analizzo il PD à 𝑃𝐷 = 𝐹&           $
          $         '   (
                                    2.      n-MOSFET rappresentati dagli
                                   3XOO'RZ
                                         ingressi in forma vera
                                   1HWZRUN                                         %
          $
                    %   '           3.      Inverto la funzione ottenuta
          &
                                                       & + (𝐴 + 𝐷
                                    𝑃𝐷 𝐴, 𝐵 = 𝐹 𝐴, 𝐵 = 𝐸𝐷               ̅ + 𝐵)
                                                                / ) 1 (𝐴𝐶    $
                            ++6/HH
                            ++6
                            ++ 6/HH
                                      /HH

                                                     & + (𝐴 + 𝐷
                                            𝐹 𝐴, 𝐵 = 𝐸𝐷               ̅ + 𝐵)
                                                              / ) 1 (𝐴𝐶
                                                                                    $
                Proprietà generali delle porte CMOS
• PU e PD duali (come nell’inverter) à riesco a sfruttare quello che ho calcolato
  per l’inverter
• Se PU=ON à PD=OFF
                                  𝑉!" = 𝑉## ; 𝑉!$ = 0 (indipendentemente da
• Se PD=ON à PU=OFF                                dimensionamenti e topologia)
                                                   à in condizioni statiche
• Consumo di potenza statico nullo!
• Funzione con N ingressi à almeno 2N transistori (N n-MOSFET + N p-MOSFET)
• Commutazioni avvengono in regime di TRANSITORIO
                 Porte FCMOS: implementazione di
à dipende dalle capacità in gioco (le quali si caricano e scaricano) e dalla
                               funzioni generiche
   CONDUCIBILITA’ di PU e PD !!
                   •Ogni funzione logica implementata con
à posso vedere PU eporte
                      PD FCMOS
                          come dei   prevede una rete
                                       transistor     di pull –
                                                   equivalenti
                    up e una di pull – down
  che si accendono
                 • Le e due
                        spengono
                             reti sono à  creo unsolo
                                       composte   circuito
                                                      da MOS a
                    canale p e MOS a canale n,
  equivalente che è un  INVERTER
                    rispettivamente
                 • La topologia delle due reti è duale: a un
                    parallelo in PU corrisponde una serie in
                    PD e viceversa
                 • Conviene ragionare guardando solo il PD
mentazione di                                      Inverter equivalente
 iche

                                                        Mp
                         𝐹                𝐹&                  𝐹

                                                        Mn




   Una volta che ho fatto questa trasformazione posso utilizzare tutte le formule
   ottenute per l’inverter (es.: tempo di ritardo, consumo di potenza, etc.)

   à devo trovare il dimensionamento del transistor equivalente !!

   à dipende da dimensionamenti e topologia del PU e PD originali

   à si parla di DIMENSIONAMENTO EQUIVALENTE
                                                  Parallelo di MOSFET
          𝑉#                  Transistor equivalente: deve funzionare come un
     𝑇&         𝑇'            MOSFET à soddisfare tutte le relazioni che
                              abbiamo introdotto per i MOSFET


                                𝐼 = 𝐼#%& + 𝐼#%'
          𝑉%

se A=1 e B=0 à T1 ON, T2 OFF à caso banale (1 solo transistor)
se A=0 e B=1 à T1 OFF, T2 ON à caso banale (1 solo transistor)
se A=1 e B=1 à T1 ON, T2 ON à 2 transistor in parallelo con stessa tensione di gate,
                                di drain e di source

esempio: regione TRIODO
                                          1                              1
 𝐼 = 𝐼#%& + 𝐼#%' = 𝑆& 𝛽( ′ (𝑉)% −𝑉* )𝑉#% − 𝑉#% ' +𝑆' 𝛽( ′ (𝑉)% −𝑉* )𝑉#% − 𝑉#% '
                                          2                              2

                                   1
 𝐼 = (𝑆& + 𝑆' )𝛽( ′ (𝑉)% −𝑉* )𝑉#% − 𝑉#% '         UNICO MOSFET con 𝑺𝒆𝒒 = (𝑺𝟏 + 𝑺𝟐 )
                                   2
 à il risultato è identico se i MOSFET sono in saturazione!!
 di quello dei singoli transistori1.             Una volta determinate le caratteristiche del MOSFE
                                              Il caso dei MOSFET in serie
                                                 iterativamente la Serie
                                                                   procedura di
                                                                             a unMOSFET
                                                                                  numero arbitrario d
                                                 traccia in modo duale, dimostrare la proprietà trova
                                              Premessa
            𝑉#                         Nei circuiti logici è frequente il caso in cui diversi MOSFET dello stesso t
                       𝐼 = 𝐼#%& = 𝐼#%'      Due
                                       stesso       nMOSFET
                                              potenziale               ininserie:
                                                           e con i canali   serie. interdizione
                                       In questi casi farebbe comodo poter considerare i dispositivi come un unic
      A                se A=1 e B=0 à MNel  Riprendendo
                                        2 ON,
                                            caso M     OFF
                                                 in 1cui      àlacaso
                                                         i MOSFET   Figura
                                                                     hanno  la1,
                                                                          banale  siàabbiano
                                                                               stessa   serie di
                                                                                      tensione   due
                                                                                                 soglianMOSFET
                                                                                               spenta   VTn, si può dim
                                            costruzione,
                                       possibile               secondo
                                                 e che il valore            quanto
                                                                  del coefficiente     stabilito
                                                                                   equivalente    per ilnell'espressio
                                                                                               da usare    singolo
                       se A=0 e B=1 à Mall'inverso
                                           OFF,   M     ON    à  caso     banale   à    serie  spenta
                                                      1 somma degli inversi dei kn di quello dei singoli transistori1
      B
                                        2
                                              V della
                                                   V   D   V X      S
                       se A=1 e B=1 à M2 ON, M1 ON à le
                                          Esaminiamo 2 transistor in serie
                                                        possibili zone  di con stessa 𝑉) e del
                                                                           funzionamento   la
                       stessa tensione 𝑉/
            𝑉%                                     terminali. Nel caso in cui
                                                      V GS V Tn
  La tensione VSB dei MOSFET è diversa à l’effetto
 nMOSFET con la stessa tensione di gate e canali inentrambi
                                                    serie.    i MOSFET sono sicuramente interdetti ed
  body induce tensioni di soglia diverse !!
                                                      I DS =0
  Hp. MOSFET
o due  semplificative:  g =n 0
                 a canale      (nocondizioni
                             nelle effetto body)  à stessa 𝑉*(
                                             descritte,
ra 1.                   l = 0 (no effetto mod.
                                            Zona lung.   canale)
                                                     triodo
 MOSFET equivalente, è immediato estendere
  Caso A) M1 e M2 einugualmente,
bitrario di MOSFET
                         regione TRIODO     Selaora
                                     seguendo        invece consideriamo le due condizioni
                                                  stessa
età trovata anche per i MOSFET a canale p. V GS V  Figura 1: Circuito
                                                         Tn            GD V Tn
                                                               e Vcomposto da due nMOSFET con la stessa tensione di g

                                             allora sicuramente
                                        Per dimostrare    l'affermazione,entrambi
                                                                          consideriamoi due
                                                                                         MOSFET
                                                                                              MOSFET sono
                                                                                                        a canaleinn zon
                                                                                                                    nelle
                                       &chiarite' ulteriormente dallo schema in Figura 1.
     𝐼#%0 = 𝑆0 𝛽( ′ (𝑉)%0 −𝑉*( )𝑉#%0 − 𝑉#%0  determinate
                                                      con 𝑗 =dalle1; 2 relazioni per la zona triodo
                                       '
MOSFET in serie, con la stessa tensioneUna
                                         di soglia    VTn. Per le caratteristiche del MOSFET equivalente, è imme
                                              volta determinate
 singolo MOSFET, si ha                  iterativamente la procedura a un numero arbitrario di MOSFET e ugualme
                                        traccia
                                             1 inOperativamente,
                                                    modo duale, dimostrare    la proprietà
                                                                       si tratta           trovata
                                                                                 della stessa      anche per iper
                                                                                               espressione     MOSFET
                                                                                                                  il cal
      𝑉)%0 = 𝑉)/0 − 𝑉%/0                𝑉#%0 = 𝑉#/0 − 𝑉%/0
 ento della serie in funzione delle tensioni
                                          Dueapplicate
                                               nMOSFET ai in serie: interdizione
                                       possibile e che il valore del coefficiente equivalente da usare nell'espressio
                                       all'inverso della somma degli inversi dei kn di quello dei singoli transistori1
                                                                     Serie di MOSFET
Caso A) M1 e M2 in regione TRIODO

𝑉)%0 = 𝑉)/0 − 𝑉%/0              𝑉#%0 = 𝑉#/0 − 𝑉%/0


                                                   1
𝐼#%0 = 𝑆0 𝛽( ′ (𝑉)/0 − 𝑉%/0 − 𝑉*( )(𝑉#/0 − 𝑉%/0 ) − (𝑉#/0 − 𝑉%/0 ) '
                                                   2
                                                    Figura 1: Circuito composto da due nMOSFET con la stessa tensione di g

                                         1       ' l'affermazione, consideriamo due1MOSFET
𝐼#%0 = 𝑆0 𝛽( ′ (𝑉)/0 𝑉#/0 − 𝑉*( 𝑉#/0Per
                                      − dimostrare
                                           𝑉#/0   )  −  (𝑉 )/0 𝑉%/0 −  𝑉*( 𝑉 %/0 −   𝑉%/0
                                                                                          ' a canale n nelle
                                                                                           )
                                         2 ulteriormente dallo schema in Figura 1. 2
                                   chiarite
                                     Una volta determinate le caratteristiche del MOSFET equivalente, è immed
                                     iterativamente la procedura a un numero arbitrario di MOSFET e ugualmen
                                                         &   '
 definizione à 𝑔 𝑉& , 𝑉'      = 𝛽 ′(𝑉traccia
                                  (    𝑉 −in𝑉modo
                                       & '       𝑉 duale,
                                                 *( ' − 𝑉dimostrare
                                                               )        la proprietà trovata anche per i MOSFET
                                                           ' '
                                       Due nMOSFET in serie: interdizione

 𝐼#%0 = 𝑆0 𝑔 𝑉)/0 , 𝑉#/0 − 𝑔 𝑉)/0Riprendendo
                                  , 𝑉%/0     la Figura 1, si abbiano due nMOSFET in serie, con la stessa t
                                  costruzione, secondo quanto stabilito per il singolo MOSFET, si ha
                                    V D V X V S
 𝐼#%& = 𝑆& 𝑔 𝑉)/ , 𝑉1/ − 𝑔 𝑉)/ , 𝑉Esaminiamo
                                   %/
                                               le possibili
                                                    𝐼#%' =zone
                                                             𝑆' di𝑔funzionamento
                                                                    𝑉)/ , 𝑉#/ −della𝑔 𝑉serie  in funzione dell
                                                                                        )/ , 𝑉1/
                                  terminali. Nel caso in cui
                                    V GS V Tn
                                  entrambi i MOSFET sono sicuramente interdetti ed è
                                    I DS =0
                                       possibile e che il valore del coefficiente equivalente da usare nell'espressio
                                       all'inverso della somma degli inversi dei kn di quello dei singoli transistori1
                                                                    Serie di MOSFET
Caso A) M1 e M2 in regione TRIODO

         𝐼 = 𝐼#%& = 𝐼#%'

𝑆& 𝑔 𝑉)/ , 𝑉1/ − 𝑔 𝑉)/ , 𝑉%/        = 𝑆' 𝑔 𝑉)/ , 𝑉#/ − 𝑔 𝑉)/ , 𝑉1/

                    𝑆& 𝑔 𝑉)/ , 𝑉%/ + 𝑆' 𝑔 𝑉)/ ,Figura
                                               𝑉#/ 1: Circuito composto da due nMOSFET con la stessa tensione di g
    𝑔 𝑉)/ , 𝑉1/   =
                                 𝑆& + 𝑆'
                                  Per dimostrare l'affermazione, consideriamo due MOSFET a canale n nelle
                                  chiarite ulteriormente dallo schema in Figura 1.
         𝑆& 𝑔 𝑉)/ , 𝑉%/ + 𝑆' 𝑔 𝑉)/Una
                                   , 𝑉#/volta determinate le caratteristiche del MOSFET equivalente, è immed
  𝐼 = 𝑆&                                   − 𝑔 𝑉la)/procedura
                                  iterativamente      , 𝑉%/ a un numero arbitrario di MOSFET e ugualmen
                      𝑆& + 𝑆'     traccia in modo duale, dimostrare la proprietà trovata anche per i MOSFET

        𝑆&                      Due nMOSFET in 𝑆    serie:  interdizione
                                                     & 𝑆'
  𝐼=         𝑆 𝑔 𝑉)/ , 𝑉#/ − 𝑆' 𝑔 𝑉)/ , 𝑉%/ la =              𝑔 𝑉)/due
                                                                    , 𝑉#/ − 𝑔 𝑉in , 𝑉%/con la stessa t
     𝑆& + 𝑆' '                  Riprendendo    Figura
                                                  𝑆& +1, 𝑆
                                                         si abbiano
                                                          '
                                                                       nMOSFET )/serie,
                                     costruzione, secondo quanto stabilito per il singolo MOSFET, si ha
                                       V D V X V S
         𝑺𝟏 𝑺𝟐                       Esaminiamo le possibili zone di funzionamento della serie in1funzione
                                                                                                        ' dell
𝑺𝒆𝒒 =                 𝐼 = 𝑆23 𝑔 𝑉)/ ,terminali.
                                      𝑉#/ − Nel 𝑔 𝑉caso
                                                    )/ , 𝑉%/
                                                         in cui = 𝑆23 𝛽 ( ′ (𝑉  )% −𝑉  *( )𝑉#% −   𝑉 #%
        𝑺𝟏 + 𝑺𝟐                                                                                  2
                                       V GS V Tn
                                     entrambi i MOSFET sono sicuramente interdetti ed è
                        come la corrente     in un unico transistor in regione TRIODO !!
                                       I DS =0
                                     possibile e che il valore del coefficiente equivalente da usare nell'espressio
                                     all'inverso della somma degli inversi dei kn di quello dei singoli transistori1
                                                                  Serie di MOSFET
Caso A) M1 e M2 in regione TRIODO
                                                                                                     𝑉#%
                              1
 𝐼 = 𝑆23 𝛽( ′ (𝑉)% −𝑉*( )𝑉#% − 𝑉#% '
                              2
                                                                                  𝑉)%
        𝑺𝟏 𝑺𝟐
 𝑺𝒆𝒒 =               • Verificato attraverso simulatore circuitale
       𝑺𝟏 + 𝑺𝟐
                     • Considerando l e g Figura
                                            la corrente
                                                 1: Circuitonella serie
                                                            composto da dueènMOSFET
                                                                             minorecon la stessa tensione di g
                     • Dimensionamento     perl'affermazione,
                                Per dimostrare  eccesso consideriamo due MOSFET a canale n nelle
                          chiarite ulteriormente dallo schema in Figura 1.
Caso B) SATURAZIONE dei MOSFET
                          Una volta determinate le caratteristiche del MOSFET equivalente, è immed
                          iterativamente la procedura a un numero arbitrario di MOSFET e ugualmen
                          traccia in modo duale, dimostrare la proprietà trovata anche per i MOSFET
• Se entrambi i MOSFET sono in saturazione: regione triodo e regione di
  saturazione di entrambi si toccano,  quindi rimane
                               Due nMOSFET      in serie: valido   quello che abbiamo
                                                           interdizione
                                                             %!%"
  trovato per i MOSFET in regione             Figura𝑆23
                                    triodo,lacioè
                               Riprendendo           1, si=abbiano
                                                            % 4%
                                                                   due nMOSFET in serie, con la stessa t
                                                                     !   "
                             costruzione, secondo quanto stabilito per il singolo MOSFET, si ha
                                   V X 𝑉
Ma quando vanno in saturazioneV?D per    # >
                                        V  S
                                               𝑉) − 𝑉*( quindi quando:
M1: 𝑉1 > 𝑉) − 𝑉*(            Esaminiamo le possibili zone di funzionamento della serie in funzione dell
                             terminali. Nel caso in cui
M2: 𝑉# > 𝑉) − 𝑉*( à M2 acceso VseGS V
                                    𝑉)1Tn> 𝑉*( à 𝑉) − 𝑉1 > 𝑉*( à 𝑉1 < 𝑉) − 𝑉*(
                             entrambi i MOSFET sono sicuramente interdetti ed è
à M1 SEMPRE IN REGIONE TRIODO  I DS =0 !
                                        possibile e che il valore del coefficiente equivalente da usare nell'espressio
                                        all'inverso della somma degli inversi dei kn di quello dei singoli transistori1
                                                                      Serie di MOSFET
Caso B) M1 in regione TRIODO e M2 in regione SATURAZIONE
                                                                                                           𝑉#%
  𝑉# > 𝑉) − 𝑉*(

 Hp. semplificativa: g = 0; l = 0                                                      𝑉)%
                       5#                5
 M2 à 𝐼 = 𝐼#%' =          (𝑉)%' −𝑉*( )' = # (𝑉)1 −𝑉*( )'
                        '                 '
 à dipende solo da (𝑉)1 − 𝑉*( )                      Figura 1: Circuito composto da due nMOSFET con la stessa tensione di g
 à se cambia 𝑉% la corrente non cambia ! (𝑉1 rimane fisso)
                                  Per dimostrare l'affermazione, consideriamo due MOSFET a canale n nelle
 Per semplicità assumiamo VS =chiarite
                                     0 ulteriormente dallo schema in Figura 1.
                                  Una volta determinate le caratteristiche del MOSFET equivalente, è immed
             𝑆' 𝛽( ′              iterativamente la procedura a un numero 1 arbitrario di MOSFET e ugualmen
                                                                               '
                                ' traccia in modo duale, dimostrare la proprietà
  𝐼 = 𝐼#%' =         (𝑉)1 −𝑉*( ) = 𝐼#%& = 𝑆& 𝛽( ′ (𝑉) −𝑉*( )𝑉1 − 𝑉1 trovata anche per i MOSFET
                   2                                                              2
                                        Due nMOSFET in serie: interdizione
 𝑆'                   𝑆'                                                                      1 '
    (𝑉) −𝑉1 − 𝑉*( )' = [(𝑉) −𝑉*( )' + 𝑉1 ' −
                               Riprendendo      2(𝑉) −𝑉
                                             la Figura         )𝑉1 ] =due
                                                       1, si*(abbiano   𝑆&nMOSFET
                                                                           (𝑉) −𝑉*(in)𝑉   −
                                                                                      serie,
                                                                                        1
                                                                                             con𝑉la
                                                                                                 1
                                                                                                    stessa t
 2                    2        costruzione, secondo quanto stabilito per il singolo MOSFET,2si ha
                                       V D V X V S
                                     Esaminiamo le possibili zone di funzionamento della serie in funzione dell
           𝑉1 '                                  𝑆' caso in cui '
                                     terminali. Nel
   𝑆& + 𝑆'      −      𝑆& + 𝑆' (𝑉) −𝑉*(V)𝑉V  +
                                            1 Tn    (𝑉 −𝑉 ) = 0
            2                            GS      2 ) *(
                                     entrambi i MOSFET sono sicuramente interdetti ed è
                                       I DS =0
                                         possibile e che il valore del coefficiente equivalente da usare nell'espressio
                                         all'inverso della somma degli inversi dei kn di quello dei singoli transistori1
                                                                         Serie di MOSFET
Caso B) M1 in regione TRIODO e M2 in regione SATURAZIONE
                                                                                                              𝑉#%
  𝑉# > 𝑉) − 𝑉*(

                               𝑉1 '  𝑆'                                                   𝑉)%
     𝑆& + 𝑆'    (𝑉) −𝑉*( )𝑉1 −      = (𝑉) −𝑉*( )'
                                2    2

                                                        Figura 1: Circuito composto da due nMOSFET con la stessa tensione di g
                                1 '                                 𝐼#%&     𝑆'
   𝐼#%& = 𝑆& 𝛽( ′ (𝑉) −𝑉*( )𝑉1 − 𝑉1                      𝑆& + 𝑆 '          =    (𝑉) −𝑉*( )'
                                                                   𝑆& 𝛽( ′
                                2 Per dimostrare l'affermazione, consideriamo 2
                                                                              due MOSFET a canale n nelle
                                        chiarite ulteriormente dallo schema in Figura 1.
                                        Una volta determinate le caratteristiche del MOSFET equivalente, è immed
                          𝑆& 𝑆'      𝛽( iterativamente
                                        ′traccia in modola procedura a un numero𝑺arbitrario
                                                                                   𝟏 𝑺𝟐
                                                                                            di MOSFET e ugualmen
    𝐼 = 𝐼#%& = 𝐼#%' =              1       (𝑉 −𝑉 )' duale, dimostrare  𝑺𝒆𝒒la=proprietà trovata anche per i MOSFET
                         𝑆& + 𝑆'     2       )     *(                               𝑺𝟏 + 𝑺𝟐
                                         Due nMOSFET in serie: interdizione
                                  Riprendendo la Figura 1, si abbiano due nMOSFET in serie, con la stessa t
       𝑆23 𝛽( ′                   costruzione,
                               come             secondoin
                                         la corrente    quanto stabilitotransistor
                                                           un unico       per il singolo MOSFET, si ha
   𝐼=           (𝑉) −𝑉*( )'         V D V X V S
         2                     in regione      di SATURAZIONE !!
                                  Esaminiamo le possibili zone di funzionamento della serie in funzione dell
                                  terminali. Nel caso in cui
                                    V GS V Tn
 Gli stessi calcoli e gli stessi risultati    possono essere ottenuti per i p-MOSFET !!
                                  entrambi i MOSFET sono sicuramente interdetti ed è
                                    I DS =0
                         Prestazioni dinamiche gate CMOS
La generica porta logica che implementa la generica funzione può essere descritta
utilizzando l’approccio del dimensionamento equivalente à PU e PD sostituiti con
un transistore equivalente à utilizzo le formule/risultati dell’inverter
Esempio: NOR a due ingressi
• Carica e scarica del nodo di uscita seguono diversi percorsi conduttivi
• Le specifiche di progetto vanno garantite anche nel caso peggiore
• Qual è il caso peggiore ?


SCARICA di CL à attraverso 2 MOSFET in parallelo
à il caso peggiore è quando la scarica è attraverso
         1 solo MOSFET
à identico al caso dell’inverter
                                                                                    𝐶$
                   2𝐶$              𝑉*
   𝑡6,8!9 =                    𝐹
              𝛽(: 𝑆(,8!9 𝑉##       𝑉##

    𝑆(,8!9 à dimensionamento n-MOSFET
                         Prestazioni dinamiche gate NOR
CARICA di CL à attraverso 2 MOSFET accesi in serie (unico caso)
à utilizzo il dimensionamento equivalente à formule dell’inverter
          𝑆& 𝑆'
   𝑆23 =               à uso due p-MOSFET uguali con dimensionamento 𝑆<,8!9
         𝑆& + 𝑆'
         𝑆<,8!9                        2𝐶$        𝑉*         4𝐶$         𝑉*
   𝑆23 =                𝑡;,8!9 =               𝐹     =                𝐹
            2                      𝛽<: 𝑆23 𝑉##   𝑉##   𝛽<: 𝑆<,8!9 𝑉##   𝑉##

          %$,&'(
 𝛼8!9 =            à dimensionamento relativo
          %#,&'(
                      tra n- e p-MOSFET

               4𝐶$            𝑉*
𝑡;,8!9 = :                 𝐹
        𝛽< 𝛼8!9 𝑆(,8!9 𝑉##   𝑉##
                                                                              𝐶$
Tipicamente vogliamo 𝑡;,8!9 = 𝑡6,8!9

 1       2                       𝜷:𝒏
    =                    𝜶𝑵𝑶𝑹 = 𝟐 : = 𝟐𝜺
 𝛽(: 𝛽<: 𝛼8!9                    𝜷𝒑
                        Prestazioni dinamiche gate NOR
La porta NOR potenzialmente può avere lo stesso ritardo dell’inverter
à tempi di ritardo paragonabili con transistori n-MOSFET simili

ottengo 𝑡;,8!9 = 𝑡6,8!9 = 𝑡B(C se:
• 𝑆(,8!9 = 𝑆B(C
                                         𝛼8!9 = 2𝜀
• 𝑆<,8!9 = 2𝜀 1 𝑆(,8!9 = 2𝜀 1 𝑆B(C
à p-MOSFET molto più grandi !

CAPACITA’ DI INGRESSO
• Ogni ingresso vede un n-MOSFET e un p-MOSFET                                       𝐶$

        𝐶B( = 𝑆(,8!9 1 + 𝛼8!9 𝐶D& = 𝑆(,8!9 1 + 2𝜀 𝐶D&

OCCUPAZIONE D’AREA
𝐴 = 2𝑊( 𝐿DE8 + 2𝑊< 𝐿DE8 = 2𝐿'DE8 𝑆(,8!9 + 𝑆<,8!9 = 𝐿'DE8 𝑆(,8!9 2 + 4𝜀
 𝐴                                                       𝛼8!9 = 𝑁𝜀
        = 𝐴∎,8!9 = 𝑆(,8!9 2 + 4𝜀
𝐿'DE8                                     N ingressi à   𝐶B( = 𝑆(,8!9 1 + 𝑁𝜀 𝐶D&
                                                         𝐴∎,8!9 = 𝑆(,8!9 𝑁 + 𝑁 ' 𝜀
                         Prestazioni dinamiche gate NAND
Esempio: NAND a due ingressi
• Carica e scarica del nodo di uscita seguono diversi percorsi conduttivi
• Le specifiche di progetto vanno garantite anche nel caso peggiore
• Qual è il caso peggiore ?

CARICA di CL à attraverso 2 MOSFET in parallelo
à il caso peggiore è quando la scarica è attraverso
         1 solo MOSFET
à identico al caso dell’inverter                                            𝐶$

                 2𝐶$               𝑉*          2𝐶$             𝑉*
𝑡;,8G8# =                     𝐹       = :                   𝐹
            𝛽<: 𝑆<,8G8# 𝑉##       𝑉##  𝛽< 𝛼8G8# 𝑆(,8G8# 𝑉##   𝑉##


𝑆<,8G8# à dimensionamento p-MOSFET

𝑆(,8G8# à dimensionamento n-MOSFET
            %$,&)&*
𝛼8G8# =               à dimensionamento relativo tra n- e p-MOSFET
            %#,&)&*
                       Prestazioni dinamiche gate NAND
SCARICA di CL à attraverso 2 MOSFET accesi in serie (unico caso)
à utilizzo il dimensionamento equivalente à formule dell’inverter
          𝑆& 𝑆'
   𝑆23 =               à uso due n-MOSFET uguali
         𝑆& + 𝑆'
         𝑆(,8G8#                   2𝐶$        𝑉*        4𝐶$         𝑉*
   𝑆23 =               𝑡6,8G8# = :         𝐹     = :             𝐹
            2                   𝛽( 𝑆23 𝑉##   𝑉##  𝛽( 𝑆(,8G8# 𝑉##   𝑉##

Tipicamente vogliamo 𝑡;,8G8# = 𝑡6,8G8#

 2        1                       𝜷:𝒏   𝜺
    =                     𝜶𝑵𝑨𝑵𝑫 =     =
 𝛽(: 𝛽<: 𝛼8G8#                    𝟐𝜷:𝒑 𝟐

ottengo prestazioni simili all’inverter (𝑡;,8G8# = 𝑡6,8G8# = 𝑡B(C )      𝐶$
se:
• 𝑆(,8G8# = 2 1 𝑆B(C
              𝜺
• 𝑆<,8G8# = 1 𝑆(,8G8# = 𝜺 1 𝑆B(C
              𝟐

à n-MOSFET e p-MOSFET molto più simili che nel caso NOR !
                      Prestazioni dinamiche gate NAND
CAPACITA’ DI INGRESSO
• Ogni ingresso vede un n-MOSFET e un p-MOSFET
                                               𝜀
   𝐶B( = 𝑆(,8G8# 1 + 𝛼8G8# 𝐶D& = 𝑆(,8!9 1 +      𝐶
                                               2 D&

OCCUPAZIONE D’AREA

  𝐴 = 2𝑊( 𝐿DE8 + 2𝑊< 𝐿DE8 = 2𝐿'DE8 𝑆(,8G8# + 𝑆<,8G8# = 𝐿'DE8 𝑆(,8G8# 2 + 𝜀
    𝐴
          = 𝐴∎,8G8# = 𝑆(,8G8# 2 + 𝜀
  𝐿'DE8
                            𝜀
                    𝛼8G8# =
                            𝑁
                                        𝜀
 N ingressi à       𝐶B( = 𝑆(,8G8# 1 +     𝐶
                                        𝑁 D&
                     𝐴∎,8G8# = 𝑆(,8G8# 𝑁 + 𝜀

Nella NAND l’area del PU e del PD sono più simili in quanto la minore conducibilità dei
p-MOSFET è compensata dagli n-MOSFET in serie, i quali quindi conducono meno
                     Confronto porte NOT, NOR, NAND
Tipicamente si vuole lo stesso tempo di ritardo nelle diverse porte logiche
à assumiamo 𝜀 = 2; 𝑡; = 𝑡6

     Gate               NOT              NOR – 2 ingressi        NAND – 2 ingressi
      𝑆(                𝑆B(C                    𝑆B(C                    2𝑆B(C
      𝐶B(            3𝑆B(C 𝐶D&               5𝑆B(C 𝐶D&                4𝑆B(C 𝐶D&
      𝐴∎               3𝑆B(C                  10𝑆B(C                    8𝑆B(C

• Tutte le porte logiche hanno le stesse prestazioni dinamiche se i transistori
  equivalenti del PU e del PD sono dimensionati come quelli dell’inverter
• NAND è migliore di NOR perché consuma meno area !!
• Abbiamo trascurato:
ü EFFETTO BODY
ü EFFETTO DI MODULAZIONE DI LUNGHEZZA DI CANALE
ü SELF-LOADING à CL indipendente dal dimensionamento dei transistor à analisi
  valida se le capacità a valle della porta sono grandi rispetto a quelle interne dei
  MOSFET !!
                                              Effetto del self-loading
Se volessimo tenere conto dell’effetto del self-loading dovremmo considerare tutti i
contributi capacitivi sul nodo di uscita
Es.: NAND a m ingressi che pilota k ingressi a valle
• FAN IN = m
• FAN OUT = k
• Tutti i gate a valle caratterizzati dalla stessa Cin,v
• CW = capacità dell’interconnessione (costante)


Hp.: transizione istantanea di tutti gli ingressi «0» à «1»
         (cioè la loro tensione VG salta da 0 à VDD)
à Uscita commuta da «1» à «0» (cioè VD salta da VDD à 0)
à Tutti i MOSFET connessi all’uscita vedono una VGD che
   cambia da -VDD à VDD, quindi il salto di tensione è 2VDD
à La capacità CGD di ogni singolo MOSFET vede un salto di tensione doppio
à Equivale a caricare a VDD una capacità di valore doppio (2CGD)
                                            Effetto del self-loading
Capacità sul nodo di uscita contribuita dalle k
capacità di ingresso dei gate a valle, dalla capacità
CW, da un n-MOSFET e da m p-MOSFET:

                             1
𝐶$ = 𝑘𝐶B(,C + 𝐶K + 𝑊( 2𝐶)%L + 𝐿DE8 𝐶!1 𝑅## + 𝐾23 𝐿% 𝐶0L
                             2
                      1
       +𝑚𝑊< 2𝐶)%L + 𝐿DE8 𝐶!1 𝑅## + 𝐾23 𝐿% 𝐶0L
                      2

                 M+                K         K$
con 𝑅## = 1 −       , inoltre 𝑆( = # , 𝑆< =      = 𝛼8G8# 𝑆(
                M**               $,-&      $,-&



         𝐶$ = 𝑘𝐶B(,C + 𝐶K + 𝑆( (1 + 𝑚𝛼8G8# )𝐶<&

                          &
dove 𝐶<& = 𝐿DE8 2𝐶)%L + 𝐿DE8 𝐶!1 𝑅## + 𝐾23 𝐿% 𝐶0L
                          '
à capacità sul nodo di uscita dovuta ad un
  transistore di area minima (𝑊 = 𝐿 = 𝐿DE8 )
                                             Effetto del self-loading
Per il calcolo del tempo di discesa considero gli m
n-MOSFET connessi in serie:

            2𝐶$        𝑉*                    𝑆(
𝑡6,8G8# = :         𝐹                𝑆23 =
         𝛽( 𝑆23 𝑉##   𝑉##                    𝑚

          2𝐶$ 𝑚       𝑉*
𝑡6,8G8# = :        𝐹
         𝛽( 𝑆( 𝑉##   𝑉##

               𝑉*
           2𝐹
              𝑉## 𝑚
𝑡6,8G8# =         1 1 𝑘𝐶B(,C + 𝐶K + 𝑆( (1 + 𝑚𝛼8G8# )𝐶<&
          𝛽(: 𝑉## 𝑆(

               𝑉*
           2𝐹       𝑚
              𝑉##
𝑡6,8G8# =         1    1 𝑘𝐶B(,C + 𝐶K + 𝑚 1 (1 + 𝑚𝛼8G8# )𝐶<&
          𝛽(: 𝑉##   𝑆(


                EFFETTO DEL CARICO           EFFETTO DEL SELF-LOADING
                dipende dal FAN OUT !!       dipende dal FAN IN ! non dipende da Sn !
                                             Effetto del self-loading
               𝑉
            2𝐹 𝑉 *       𝑚
                 ##
𝑡6,8G8# =              1    1 𝑘𝐶B(,C + 𝐶K + 𝑚 1 (1 + 𝑚𝛼8G8# )𝐶<&
             𝛽(: 𝑉##     𝑆(

EFFETTO DEL SELF-LOADING
• dipende dal FAN IN
• se 𝜶𝑵𝑨𝑵𝑫 fosse costante dipende da m2
                                          𝜺
• realisticamente avrò che 𝜶𝑵𝑨𝑵𝑫 =
                                          𝒎
à dipende linearmente da m !
• non dipende da Sn
à valore che non riesco a ridurre con il
  dimensionamento !
à la porta sarà più lenta dell’inverter !!

ATTENZIONE: abbiamo trascurato gli effetti reattivi degli (m-1) n-MOSFET
à anche questi aumentano il ritardo !!
à queste capacità crescono di numero con m e di valore con Sn (se
  aumenta m devo aumentare Sn)
à tf aumenta linearmente con il Fan-out e più che linearmente con il Fan-in
                   Riduzione del ritardo in gate CMOS
Abbiamo visto che se la porta logica è complessa i tempi di ritardo possono diventare
elevati à necessità di una strategia di riduzione del ritardo
• Se il Fan-in è alto à il self-loading domina e l’aumento delle dimensioni dei
  MOSFET non aiuta !

1. DIMENSIONAMENTO PROGRESSIVO
es.: su M1 scorre la corrente di scarica di C1, C2, C3, CL
su M2 scorre la corrente di scarica di C2, C3, CL
su M3 scorre la corrente di scarica di C3, CL
su M4 scorre solo la corrente di scarica di CL
à M1 è il collo di bottiglia à utilizzo un dimensionamento
maggiore in modo che porti più corrente
à S1 > S2 > S3 > S4
2. ORDINAMENTO DEI SEGNALI DI INGRESSO
A volte è possibile individuale il percorso «critico» (segnale di ingresso più lento a
commutare) à stabilisce il caso peggiore nella definizione del ritardo
à viene connesso al MOSFET più vicino all’uscita (mai al MOSFET collo di bottiglia)
permette di cominciare a scaricare le capacità C1, C2, C3 prima della scarica di CL
                    Riduzione del ritardo in gate CMOS
Abbiamo visto che se la porta logica è complessa i tempi di ritardo possono diventare
elevati à necessità di una strategia di riduzione del ritardo
• Se il Fan-in è alto à il self-loading domina e l’aumento delle dimensioni dei
  MOSFET non aiuta !
3. STRUTTURAZIONE SU PIU’ LIVELLI DI
   LOGICA
FAN-IN mai troppo grande à FAN-IN ≤ 4
à se la funzione ha tanti ingressi la divido
  su più porte

4. SEPARAZIONE TRA GRANDI FAN-IN E
   GRANDI CAPACITA’ DI CARICO
Le strategie per ridurre il ritardo dovuto alle
grosse capacità di carico e quello dovuto al
self-loading sono diverse !!
es.: dimensioni maggiori aiutano per
il carico ma non per il self-loading
à meglio separare i due problemi
à utilizzo dei buffer
                    Consumo di potenza in gate CMOS
• La potenza statica consumata è nulla
                                                                        '
• La potenza dinamica dipende dalle commutazioni à inverter: 𝑃NB( = 𝐶$ 𝑉## 𝑓L→&
𝑓L→& è la frequenza media delle transizioni 0 → 1 sul nodo di uscita

                                                                               '
 𝑓B(                                                   𝑓L→& = 𝑓B( → 𝑃NB( = 𝐶$ 𝑉## 𝑓B(


Per una generica porta logica:
• 𝑓PQ è la frequenza di clock (frequenza con cui possono variare gli ingressi, legata
  alla velocità della porta) à è la frequenza di lavoro del circuito

• 𝑓+→! = 𝑓-. 𝑃+→! dove 𝑃+→! è detta ATTIVITA’ DI COMMUTAZIONE oppure
   SWITCHING ACTIVITY
   (probabilità di avere una transizione 𝟎 → 𝟏 sul nodo di uscita)
Come si calcola 𝑃L→& ?
                     𝑃+→! = 𝑃+ . 𝑃! = 1 − 𝑃! . 𝑃! = 𝑃+ . 1 − 𝑃+
𝑃+ : probabilità di avere un «0» in uscita     Dipendono dalla funzione logica
𝑃! : probabilità di avere un «1» in uscita     implementata e dagli ingressi !!
                          Esempio: inverter e NOR CMOS
Calcoliamo la switching activity per l’inverter
Hp.: se le probabilità di avere in ingresso uno «0» o un «1»
sono uguali:
                                                  &
𝑃+ : probabilità di avere un «0» in uscita = 0.5 = '
                                                  &
𝑃! : probabilità di avere un «1» in uscita = 0.5 = '
                      𝑃L→& = 𝑃L 1 𝑃& = 0.25
Se le probabilità di avere in ingresso uno «0» o un «1» non sono uguali, devo tenere
conto anche di questo nel calcolo: 𝑃L = 𝑃E(R& ; 𝑃& = 𝑃E(RL

Calcoliamo la switching activity per la porta NOR
Hp.: se le probabilità di avere in ingresso uno «0» o un «1»
sono uguali:
                                                       S
𝑃+ : probabilità di avere un «0» in uscita = 0.75 = T
                                                       &
𝑃! : probabilità di avere un «1» in uscita = 0.25 = T
                                           3
                  𝑃L→& = 𝑃L 1 𝑃& = 0.188 =
                                           16
                              Esempio: NOR e NAND CMOS
Se le probabilità di avere in ingresso uno «0» o un «1» non sono uguali, devo tenere
conto anche di questo nel calcolo:
𝑃/ : probabilità di avere un «1» sull’ingresso A        Assunte
𝑃0 : probabilità di avere un «1» sull’ingresso B        incorrelate !

𝑃! = (1 − 𝑃/ )(1 − 𝑃0 )
𝑃+ = 1 − 𝑃! = 1 − (1 − 𝑃/ )(1 − 𝑃0 )
𝑃+→! = 𝑃+ . 𝑃!

Calcoliamo la switching activity per la porta NAND
Se ho probabilità uguale di avere in ingresso uno «0» o un «1»:
                                                    &
𝑃+ : probabilità di avere un «0» in uscita = 0.25 = T
                                                   S
𝑃! : probabilità di avere un «1» in uscita = 0.75 = T
                                                       3
                               𝑃L→& = 𝑃L 1 𝑃& = 0.188 =
                                                      16
Se ho probabilità diverse di avere in ingresso uno «0» o un «1»:
𝑃+ = 𝑃/ 𝑃0
                                                                 𝑃+→! = 𝑃+ . 𝑃!
𝑃! = 1 − 𝑃+ = 1 − 𝑃/ 𝑃0
                           Switching activity generico gate
• Analizziamo un generico gate con n ingressi
• La tabella di verità è formata da 2n combinazioni possibili degli ingressi
N1: numero di «1» in uscita nella tabella di verità
N0: numero di «0» in uscita nella tabella di verità
• Se le probabilità di avere sugli ingressi uno «0» o un «1» sono uguali: 𝑃EB = 0.5


                   𝑁!                                    𝑁+                𝑁!
               𝑃! = #                             𝑃+ =      = 1 − 𝑃! = 1 −
                   2                                     2#                2#


                                                  𝑁+ . 𝑁!
                                 𝑃+→! = 𝑃+ . 𝑃! =
                                                   2"#


Nota: il calcolo è valido se gli ingressi sono incorrelati !
