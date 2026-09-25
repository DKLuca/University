---
fonte: "Figure di merito gate.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Figure di merito porte logiche

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                                       Porte logiche
•   Porte logiche trattano segnali digitali
•   Segnali di tensione a valori discreti à tipicamente binari
LOGICA POSITIVA: «1» logico = tensione alta; «0» logico = tensione bassa
LOGICA NEGATIVA: «0» logico = tensione alta; «1» logico = tensione bassa
à se non diversamente specificato noi lavoreremo con logica positiva


Porte logiche (gate): circuiti digitali che implementano l’aritmetica di Boole
es.:




Porta logica più semplice: NOT (INVERTER)
à ci riferiremo a questa per studiare le performance dei gate logici
                                                          Inverter (NOT)
INVERTER: inverte il segnale binario
•   ingresso alto (1) à uscita bassa (0)
•   ingresso basso (0) à uscita alta (1)


Es.: inverter RTL (emettitore comune)

                                                   Vce

                                                    Vcc

                                                                        SATURO




                                                          Reg. ATTIVA
                                              Vce,sat

•   ingresso basso à BJT OFF à uscita alta                                       Vbe
•   ingresso alto à BJT saturo à uscita bassa
•   regione attiva NON UTILIZZATA (se non durante le transizioni 1-0 o 0-1)
                            Transistore come interruttore
•   ingresso basso à BJT OFF à corrente IC nulla à non ho caduta sulla RC
•   ingresso alto à BJT saturo à tensione di uscita molto piccola
à il transistor deve comportarsi come un interruttore !




                                                ISW                 Interruttore ideale
                                                                    (switch):
                                                                    OFF à ISW = 0
                                                                    ON à VSW = 0
                                                            VSW




•   ingresso basso à BJT OFF à corrente IC nulla
•   ingresso alto à BJT saturo à tensione VCE molto piccola (VCE,sat)
à transistor può essere visto come un interruttore comandato in tensione !
                                           Interruttore non ideale

                                                                     Interruttore ideale
                                                                     (switch):
                                                                     OFF à ISW = 0
                                                                     ON à VSW = 0




Il BJT non è un interruttore ideale à VCE,sat > 0 (è accettabile?)

                                        𝑉!"                             𝑅!"
In generale possiamo definire:    𝑅!" =                      𝑉#$% =           𝑉
                                        𝐼!"                           𝑅!" + 𝑅& ''

Interruttore ideale ON à RSW = 0
Interruttore non ideale ON à RSW > 0 à è importante avere RL >> RSW
                                                 Porte logiche RTL




           NOT                     NAND                NOR

BJT visto come interruttore
Serie di interruttori à funzione booleana NAND
Parallelo di interruttori à funzione booleana NOR
          Figure di merito delle porte logiche

Come valuto le performance di una porta logica?
Figure di merito:
• Caratteristica statica
• Direttività
• Fan in / fan out
• Prestazioni dinamiche
• Consumo di Potenza

à permettono un confronto tra schemi circuitali e
  tecnologie diverse
à ci riferiremo alla porta più semplice (NOT)
                             Caratteristica statica

Inverter (porta NOT)
• 1 ingresso
• 1 uscita

Caratteristica statica
à no effetti reattivi !

        VO=f(Vin)
In generale può dipendere
da ciò che viene collegato
a valle del circuito
Hp.: funzionamento a vuoto
(assenza di carico oppure
ciò che sta a valle non
assorbe corrente)
                             Tensioni nominali
Definizioni:
VOH: tensione nominale
corrispondente a «1»
VOL: tensione nominale
corrispondente a «0»
1. VOH = f(VOL)
2. VOL = f(VOH)
à vanno definite
  contestualmente !
1. VOH = f(VOL)
2. VOH = f -1(VOL)
dove f -1 è l’inversa di f
à posso ottenere i valori
  per via grafica
à specchio f sulla
  bisettrice del quadrante
                                Soglia logica e swing logico
VLT: tensione di soglia
logica (ingresso = uscita)
         VLT = f(VLT)
Vswing: swing logico
Vswing = VOH - VOL

Detta Valim la tensione di
alimentazione, nella porta
logica ideale:
à VOH = Valim
à VOL = 0
à Vswing = Valim

Sorgenti di non idealità:
• rumore
• accoppiamenti capacitivi
• disturbi sull’alimentazione
                               Margini di immunità ai disturbi
Definizioni:
VIH: minima tensione di
ingresso riconosciuta
dalla porta come «1»
VIL: massima tensione di
ingresso riconosciuta
dalla porta come «0»
à definite nei punti dove
           𝑑𝑓
               = −1
          𝑑𝑉()
    (proprietà rigenerativa)
Definiscono il margine di
immunità ai disturbi
NML = VIL - VOL
NMH = VOH - VIH
                                           Immunità ai disturbi
Voglio NML e NMH grandi à porta robusta ai disturbi !!
VIL < VI < VIH à fascia proibita !! La porta logica non riconosce l’ingresso !!
à cosa succede all’uscita ??




                                Figure di merito
                                 porte logiche
                               Proprietà rigenerativa
Definiamo il guadagno
di tensione                                     OK !

          𝑑𝑉#
     𝐴* =
          𝑑𝑉()
E’ importante che nella
fascia

VIL < VI < VIH

sia |AV| > 1 (vedi caso (a))

à proprietà
  rigenerativa dei gate                         NO !
à se metto inverter in
  cascata il segnale si
  rigenera (VI2=VO1)
   𝛿+ > 𝛿, > 𝛿-
I segnali si allontanano
da VLT !
                              Proprietà rigenerativa
se |AV| > 1 (vedi caso (a))
                                               OK !
lungo la catena di
inverter i segnali
vengono spinti verso le
tensioni nominali
à il segnale si rigenera

se |AV| < 1 (vedi caso (b))

lungo la catena di
inverter i segnali
vengono spinti verso VLT
à male !                                       NO !


Cmq bisogna fare
attenzione che il
disturbo non sposti
troppo il primo segnale
à convergenza verso il
dato sbagliato
                        Caratteristica ideale e direttività
|AV| >> 1 nella zona proibita ! à proprietà rigenerativa

                          VO
                                              Caratteristica ideale




                                       VLT           VI


 DIRETTIVITA’: circuito unidirezionale à uscita non condiziona l’ingresso
                            à migliora anche l’immunità ai disturbi


 • Nella realtà il circuito non è mai perfettamente unidirezionale
 • Direttività cala con la frequenza di funzionamento à a causa degli accoppiamenti
   capacitivi
                                                  FAN IN e FAN OUT
FAN OUT: massimo numero di gate che si possono connettere a valle di un inverter
• Nella realtà i circuiti a valle consumano potenza
• Corrente assorbita non nulla
à gate ideale: corrente di ingresso nulla (parametro importante)
• Circuiti a valle modificano la caratteristica statica


FAN IN: numero di ingressi della porta logica (es.: AND a molti ingressi)
• modifica e determina le caratteristiche statiche della porta
• più ingressi = più transistor à complessità ed effetti reattivi !!


FAN IN e FAN OUT: influenzano le prestazioni dinamiche !!
à le porte rallentano, alti tempi di ritardo


Come valuto le prestazioni dinamiche ?
à metriche per misurare i tempi di ritardo
à tempi di commutazione, di propagazione, di attraversamento
                                       Prestazioni dinamiche
tpr: tempo di propagazione in salita     tR: tempo di salita
tpf: tempo di propagazione in discesa    tF: tempo di discesa
tp: tempo di propagazione

      𝑡!" + 𝑡!#
 𝑡! =
          2
                                                    Potenza dissipata
La potenza dissipata nel circuito può essere genericamente calcolata come
P = VCC ICC
                                                                        Vcc
ICC: corrente assorbita dall’alimentazione

                                                                   RL    Icc
POTENZA STATICA (assenza di commutazioni)
IN = 0 (switch OFF) à ICC = 0 à P = 0

                                                     ,
                                                                   IN          CL
                             𝑉''                    𝑉''
IN = 1 (switch ON) à 𝐼'' =                   𝑃=
                           𝑅!" + 𝑅&               𝑅!" + 𝑅&

POTENZA DINAMICA (legata alle commutazioni)
es.: VOUT: 0 à 1    ICC(t): corrente di carica della capacità CL
      /                 /                          *!#
                               𝑑𝑉#$%
𝐸 = / 𝑉'' 𝐼'' (𝑡)𝑑𝑡 = / 𝑉'' 𝐶&       𝑑𝑡 = 𝑉'' 𝐶& / 𝑑𝑉#$%
     .                 .        𝑑𝑡                *!"

𝐸 = 𝑉'' 𝐶& 𝑉#0 − 𝑉#& = 𝑉'' 𝐶& 𝑉12()3

Metà energia è dissipata su RL e metà è immagazzinata su CL
VOUT: 1 à 0 la capacità si scarica à perdo l’energia immagazzinata in precedenza
                                                  Potenza dinamica
POTENZA DINAMICA (legata alle commutazioni)
In un ciclo (0à1à0) perdo tutta l’energia spesa per caricare la capacità
                                                                           Vcc
𝐸 = 𝑉$$ 𝐶% 𝑉&' − 𝑉&% = 𝑉$$ 𝐶% 𝑉()*+,
                                                                     RL     Icc
Potenza media spesa nel ciclo

𝑃-*+ = 𝑉$$ 𝐶% 𝑉&' − 𝑉&% 𝑓.→0
                                                                    IN            CL
𝑓4→6 frequenza con cui avvengono le commutazioni

                                                <
Nel caso ideale di Vswing = VCC      𝑃789 = 𝐶: 𝑉;; 𝑓4→6

Pdin è una potenza media à la potenza istantanea può essere molto più alta !!
à picchi di potenza alla commutazione
à transizioni veloci à picchi maggiori
à circuiti veloci à potenza istantanea molto elevata !
DESIGN à trade off tra velocità e consumo à POWER-DELAY PRODUCT (fig. di merito)
                                             Corrente di ingresso
Funzionamento a VUOTO                                       Vcc
IN = 0 à VOUT = VCC
                                                       RL    Icc
                     𝑅!"
IN = 1 à 𝑉#$% =            𝑉             𝑅% ≫ 𝑅45
                   𝑅!" + 𝑅& ''
                                                       IN          CL


Funzionamento SOTTO CARICO                                  Vcc
IG: corrente di ingresso porta a valle
                                                       RL    Icc
IN = 0 à       𝑉&12 = 𝑉$$ − 𝑅% 𝐼3                                   Porta
                                                                   logica
                                                             IG
Se RL elevata à VOUT CALA MOLTO !!                     IN          CL
Se FAN OUT è elevato à la corrente assorbita aumenta

 𝑉&12 = 𝑉$$ − 𝑅% 𝑛𝐼3

VOUT CROLLA !! à MOLTO IMPORTANTE AVERE IG = 0
