---
fonte: "18_logiche dinamiche.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Logiche dinamiche CMOS

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
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
                                    Logiche dinamiche CMOS
• Per distinguere le due fasi (precarica e valutazione) è necessario un segnale di
  controllo detto clock (F)
• La funzione F è definita dal solo PD (o in alternativa dal solo PU)
• La realizzazione del PD segue le stesse regole del caso delle logiche statiche CMOS:
    Ø ingressi connessi ai gate dei MOSFET
    Ø reti di MOSFET in serie o parallelo
    Ø PD realizzato tramite n-MOSFET (nel caso del PU si utilizzano p-MOSFET)



        F                             • Se la funzione è realizzata dal PD si parla
                                        di blocco Fn (realizzato tramite n-MOSFET)
                                      • Se la funzione è realizzata dal PU si parla
                                        di blocco Fp (realizzato tramite p-MOSFET)
                                      • N ingressi è (N+2) MOSFET (più efficiente
                                        delle logiche statiche CMOS)
        F         n
                              blocco Fn
                                          Precarica e valutazione
• Il segnale di clock (F) determina:
    Ø F = 0 à la fase di PRE-CARICA (blocco Fn) o di PRE-SCARICA (blocco Fp)
    Ø F = 1 à la fase di VALUTAZIONE degli ingressi

• se F = 0 à Mn OFF; Mp ON
                                         F
• se F = 1 à Mn ON; Mp OFF

                                                                          t


                                       PRE-CARICA             VALUTAZIONE
       F
                                       Mn OFF; Mp ON          Mn ON; Mp OFF
                             F
                                       il p-MOSFET carica     • se il PD è spento
                                       la capacità CL a VDD     l’uscita rimane a VDD
                                       àF=1                   àF=1
                                       à questo viene         • se il PD è acceso
                                         fatto prima di         l’uscita si scarica a
       F         n
                                         ogni valutazione       massa
                                         degli ingressi       àF=0
                                          Precarica e valutazione
• se F = 0 à Mn OFF; Mp ON
• se F = 1 à Mn ON; Mp OFF
à non c’è mai un percorso conduttivo tra VDD e massa à Potenza statica nulla; no
  corrente di corto circuito
PRE-CARICA à F = 1
L’uscita in questa fase non è significativa perchè sempre uguale (in questa fase gli
ingressi possono variare senza influenzare il funzionamento della porta)
VALUTAZIONE à F dipende dallo stato di conduzione del PD
𝑭(𝑰𝒏𝟏 , 𝑰𝒏𝟐 , … ) = 𝑷𝑫 à l’uscita viene letta solo in questa fase !! (ad ingressi fermi)
        F

                            F
                                        se il PD è spento l’uscita rimane al valore
                                        precaricato di VDD
                                        à nella realtà l’uscita rimane un nodo
                                          ISOLATO
        F                               à la sua tensione dipende dalle correnti
               n
                                          di perdita del circuito !!
                                                               Blocco Fp
                      • se F = 1 à Mn ON; Mp OFF
                      PRE-SCARICA à F = 0
    F                 L’uscita in questa fase non è significativa perchè è sempre
                      portata a massa (in questa fase gli ingressi possono variare
                      senza influenzare il funzionamento della porta)
                      • se F = 0 à Mn OFF; Mp ON
                      VALUTAZIONE degli ingressi à F dipende dallo stato di
                      conduzione del PU
    F             F
                       𝑭(𝑰𝒏𝟏 , 𝑰𝒏𝟐 , … ) = 𝑷𝑼 à l’uscita viene letta solo in questa
                      fase !! (ad ingressi fermi)

                                   • se il PU è acceso l’uscita si carica a VDD
                                   àF=1
                                   • se il PU è spento l’uscita rimane a 0
PRE-SCARICA                        àF=0
              VALUTAZIONE          à nella realtà l’uscita rimane un nodo
F                                    ISOLATO
                                   à la sua tensione dipende dalle correnti di
                               t     perdita del circuito !!
                                        Caratteristiche generali
Le caratteristiche generali delle porte dinamiche CMOS sono:
• N ingressi à (N+2) MOSFET (< 2N delle statiche CMOS)
• La sintesi del PU o del PD segue le stesse regole delle logiche statiche
• VOL = 0; VOH = VDD
• Minore immunità ai disturbi rispetto alle logiche statiche (quando il nodo di uscita
  è un nodo isolato)
à mitigare questo problema si possono definire dei margini di immunità diversi
es.: blocco Fn à F = 1 è nodo isolato
• Per accendere il PD della porta successiva mi basta una tensione di ingresso
  leggermente superiore a VTn
• Inoltre non devo spegnere nessun PU à anche una tensione leggermente
  superiore a VTn è letta come “1”
à NMH = VDD – VTn
                               NMH > NML à comunque mi rimangono problemi
à NML = VTn
                                           legati al nodo isolato (CL si scarica)
                                                        Tempi di ritardo
Il funzionamento si basa su due fasi à somma dei tempi di ritardo:
• Tempo di precarica / prescarica (come il tempo di salita / discesa di un inverter)
• Tempo di valutazione:
   1. se F = 1 à tr = 0     (CL è già carico !!)
   2. se F = 0 à tf calcolato come per le logiche statiche CMOS à dimensionamento
                                                                 equivalente del PD
   ATTENZIONE: c’è un transistor n-MOSFET in più !!

• Il tempo di precarica/prescarica è sempre necessario
         (ma è un tempo morto)
                                                           F
• Tipicamente è minore del tempo di valutazione
         (ho un solo transistor !)
• Durante il tempo di precarica si possono fare altre
   operazioni accessorie per il sistema digitale
à prevede un progetto di SISTEMA
                                                           F
Meno MOSFET à minore Cin, meno self-loading !!
à LE PORTE DINAMICHE SONO PIU’ VELOCI !!
                    Consumo di potenza gate dinamici
• L’alternanza delle fasi di precarica e valutazione elimina la potenza di corto circuito
à anche se gli ingressi variano lentamente, lo fanno durante il tempo di precarica
à n-MOSFET comunque spento, quindi non c’è mai corrente tra VDD e massa
• Rimane la potenza dinamica
           (
𝑃#$% = 𝐶& 𝑉'' 𝑓)* 𝑃+→- dove 𝑃+→- = 𝑃+ 0 𝑃-
                                                                       (
à la precarica mi porta l’uscita sempre a “1” !! à 𝑃- = 1 à 𝑃#$% = 𝐶& 𝑉'' 𝑓)* 𝑃+
es.: NOR a due ingressi
              .                                    .
𝑃+→- = 𝑃+ =       (nelle logiche statiche 𝑃+→- =        )
              /                                    -0
la switching activity nelle porte dinamiche è maggiore !
                                                                       F
à problema principale delle logiche dinamiche:
    ALTA POTENZA DINAMICA

es.: NOR a tre ingressi
              1                                             1
𝑃+→- = 𝑃+ =       mentre nelle logiche statiche 𝑃+→- =
              2                                             0/
à fattore 8 sulla switching activity !!                                F
                                     3                           3 3
N ingressi à dinamiche: 𝑃+→- = ("! ; statiche: 𝑃+→- = (!$"#
e la netlist spice per l’analisi in transitorio, supponendo che gli ingressi A, B
no costanti e commuti il segnale di clock fn.                                   Porte in cascata
                                                               Il collegamento di porte dinamiche in cascata
                                                               è problematico:
    F                           F
                                                               à Gli ingressi devono essere STABILI nella
                                                                 fase di valutazione
                                                               à Eventualmente un blocco Fn potrebbe
                                                                 accettare anche una variazione 0 à 1 in
                                                                 ingresso (mentre un blocco Fp potrebbe
                                                                 accettare la transizione 1 à 0)
                                                               à L’uscita Z1 invece fa esattamente
    F                           F                                l’opposto (o resta sempre alta oppure c’è
                                                                 una transizione 1 à 0)
                        C=0                                à Se l’uscita Z1 deve valere 0, la sua
1    F      Z1= (AB)’
2             Z2 = ((AB)’+C)’ = ABC’
                                                             tensione deve essere nulla all’inizio
e in  cascata
                                                             della fase di valutazione della seconda
   A,B
 ema che si verifica, ad         Non esiste problema perché: porta, altrimenti il nodo Z2 si scarica
a combinazione                                               durante la transizione 1 à 0 del nodo Z1
 B=1            C=0
 fattoZ1
       che l’uscita Z2 dovrebbe                            à Con i blocchi Fp avviene l’opposto: la
  1 (ABC’=1),
      VTn         però, siccome
  valutazione sia Z1 che Z2
                                                             transizione 0 à 1 carica parzialmente
causa Z2 della precarica), un                                l’uscita della porta successiva
a 1 sul MOS M6 potrebbe                               DV
ricare di Z2 che non potrebbe
                               Logiche dinamiche domino
Il blocco Fn
• accetta transizioni lente 0 à 1 in ingresso è inducono solo un tempo di
  propagazione maggiore
• produce in uscita transizioni 1 à 0 (non possono essere ingresso di blocco Fn)
Il blocco Fp
• accetta transizioni lente 1 à 0 in ingresso è inducono solo un tempo di
  propagazione maggiore
• produce in uscita transizioni 0 à 1 (non possono essere ingresso di blocco Fp)
Come faccio ?
Inverto le transizioni in uscita con un inverter CMOS statico ! à LOGICHE DOMINO


                                              • L’inverter aggiunge ritardo
                                              • L’inverter può essere sfruttato come
                                                buffer per pilotare grandi capacità
                                              • Sintetizza funzioni non invertenti
                                                      (es.: AND; OR)
                             Logiche dinamiche np-CMOS
Il blocco Fn
• accetta transizioni lente 0 à 1 in ingresso è inducono solo un tempo di
  propagazione maggiore
• produce in uscita transizioni 1 à 0 (non possono essere ingresso di blocco Fn)
Il blocco Fp
• accetta transizioni lente 1 à 0 in ingresso è inducono solo un tempo di
  propagazione maggiore
• produce in uscita transizioni 0 à 1 (non possono essere ingresso di blocco Fp)
à L’uscita di un blocco Fn è buona per un blocco Fp e viceversa
à Se alterno i blocchi non mi serve inserire l’inverter CMOS !!
à Evito che l’inverter aggiunga ritardo
ATTENZIONE: la valutazione deve avvenire nello stesso lasso temporale à non posso
valutare mentre l’uscita precedente è in fase di precarica/prescarica !!
                                       "
à ho bisogno di due clock opposti: Φ e Φ
                            Logiche dinamiche np-CMOS
Alterno i blocchi Fn e Fp


                                          2
                                          Φ
          F




                                           2
                                           Φ
          F




I PU fatti con i p-MOSFET sono tipicamente più lenti à dimensionamento maggiore
per compensare ed avere tempi di ritardo simili tra le porte
à svantaggio rispetto a fare tutti i blocchi di tipo Fn
                                Confronto degli stili circuitali
Famiglia
                        VANTAGGI                                  SVANTAGGI
 logica

             • Robustezza (PU + PD)
                                                  • 2N MOSFET (+ area)
             • Swing di tensione = VDD
 CMOS                                             • Lente in caso di Fan-In alto
             • Margini di immunità simmetrici
 statica     • Tempi di salita e discesa uguali
                                                  • Alta capacità di ingresso
                                                  • Alto effetto di self-loading
             • Gestiti bene da T-CAD


                                                • Caratteristiche statiche non simmetriche
             • Implementazioni molto efficienti
                                                  (layout non simmetrico)
               (pochi MOSFET; es.: XOR, MUX)
  Pass-                                         • Margini di immunità non simmetrici
             • Vswing = VDD con pass-transistor
transistor                                      • Segnali «deboli» con pass-transistor singolo
               complementari o transistor di
                                                • Tanti MOSFET con pass-transistor
               ripristino
                                                  complementari (+ area; + capacità)

                                                  • Vulnerabili ai disturbi quando il nodo di
             • Vswing = VDD
                                                    uscita è isolato:
             • (N+2) MOSFET (- area)
 CMOS                                               o Correnti di perdita
             • Capacità di ingresso bassa
dinamica                                            o Accoppiamenti capacitivi
             • Basso self-loading
                                                  • Connessione in cascata non banale
             • Porte logiche veloci
                                                  • Alta switching activity à alta Pdin
                      Famiglie logiche vs. applicazioni
• Per scegliere lo stile circuitale bisogna valutare le principali FIGURE di
  MERITO della famiglia logica:

    • IMMUNITA’ AI DISTURBI
    • VELOCITA’
    • CONSUMO DI POTENZA
    • OCCUPAZIONE D’AREA

• Per scegliere lo stile circuitale più adatto bisogna anche valutare l’applicazione
  a cui siamo interessati
à il peso delle varie FIGURE di MERITO cambia in funzione dell’applicazione


Un aspetto importante è anche legato al grado di automatizzazione del progetto
à l’utilizzo dei Technology-CAD (T-CAD) è fondamentale nel design dei circuiti
  digitali
à Logiche CMOS statiche sono PREDOMINANTI nei sistemi digitali
 (anche per la compatibilità con la riduzione della tensione di alimentazione !!)
