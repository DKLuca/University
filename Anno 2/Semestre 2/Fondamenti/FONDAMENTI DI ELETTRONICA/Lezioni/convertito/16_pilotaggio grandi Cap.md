---
fonte: "16_pilotaggio grandi Cap.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Pilotaggio di grandi capacità

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                          Alta capacità di carico
• Le performance delle porte logiche sono affette dalle capacità di carico collegate al
  nodo di uscita à aumentano il tempo di ritardo

                                Es.: inverter che pilota una capacità di carico CL
               p                • il circuito è caratterizzato da:
                                1. Capacità di carico (trascuro effetto di self-loading)
                                2. Capacità di ingresso: 𝐶!" = 𝑆" 1 + 𝛼 𝐶#$
                                CM1: capacità di gate del transistor di area minima
               n
                                à Dimensionamento tale per avere tempi uguali di
                                  salita e di discesa à 𝛼 = 𝜀



              2𝐶&       𝑉)   𝐶&     2𝐶!"       𝑉)   𝐶& 2 1 + 𝛼 𝐶#$    𝑉)
   𝑡% =              𝐹     =    ,           𝐹     =     ,          𝐹
          𝛽"' 𝑆" 𝑉((   𝑉((   𝐶!" 𝛽"' 𝑆" 𝑉((   𝑉((   𝐶!"   𝛽"' 𝑉((    𝑉((


          2 1 + 𝛼 𝐶#$    𝑉)
  𝑡%* =               𝐹        à tempo di propagazione di un inverter caricato da un
             𝛽"' 𝑉((    𝑉((
                               inverter identico (non dipende dal dimensionamento)
                                          Alta capacità di carico
• Le performance delle porte logiche sono affette dalle capacità di carico collegate al
  nodo di uscita à aumentano il tempo di ritardo

                                                  𝐶!" = 𝑆" 1 + 𝛼 𝐶#$
              p                                            𝐶&
                                                      𝑡% =    ,𝑡
                                                           𝐶!" %*
                               • Il tempo di ritardo della porta dipende linearmente
                                         +
                                 da 𝑋 = + !
                                           "#
              n
                               • Cin diventa il termine di paragone per capire se la
                                 capacità di carico CL è grande o meno
                               • Se l’inverter è connesso ad una lunga linea di
                                 interconnessione oppure ad un pin di uscita del
                                 circuito integrato à 𝑋 = 1000 ÷ 10000

 à eventualmente è necessario inserire un BUFFER (dimensionamento grande,
   correnti alte)

 Quanto grande deve essere il buffer ?
                               Dimensionamento del buffer
• Il tempo di ritardo totale dipende dal dimensionamento del buffer

                                           • Il primo inverter lo consideriamo ad
                                             area minima
                                                 𝐶!" = 𝑆" 1 + 𝛼 𝐶#$ = 1 + 𝜀 𝐶#$
                                           • Il secondo inverter è il buffer con
                                               dimensionamento del n-MOSFET pari
                                               ad S
                                            𝐶!", = 𝑆" 1 + 𝛼 𝐶#$ = 𝑆 1 + 𝜀 𝐶#$ = 𝑆𝐶!"

Il ritardo totale può essere approssimato con la somma dei ritardi dei singoli inverter

                   𝐶!",      𝐶&             𝐶!",   𝐶&             𝐶& 𝐶!"
  𝑡% = 𝑡%$ + 𝑡%, =      ,𝑡 +    , 𝑡 = 𝑡%* ,      +    = 𝑡%* , 𝑆 +    ,
                   𝐶!" %* 𝐶!", %*           𝐶!" 𝐶!",              𝐶!" 𝐶!",
                 𝑋
  𝑡% = 𝑡%* , 𝑆 +             Il tempo di ritardo è contribuito da due termini:
                 𝑆
                             • il primo aumenta con S (cresce 𝐶!", )
       𝐶&
  𝑋=                         • il secondo diminuisce con S (aumenta la corrente di
      𝐶!"
                               carica/scarica per 𝐶& )
                                          Dimensionamento ottimo
 Esiste S che ottimizza tp ?
                                                • Faccio la derivata di tp rispetto a S
                                                        𝜕𝑡%               𝑋
                                                            = 𝑡%* , 1 − , = 0
                                                         𝜕𝑆              𝑆
                                                à il dimensionamento ottimo è pari a
                                                               𝑆-%. = 𝑋

                                                                                  𝐶&
                                                     𝑡% -%. = 2𝑡%* , 𝑋 = 2𝑡%* ,
                                                                                  𝐶!"


Il dimensionamento ottimo garantisce tempi di ritardo uguali per i due inverter: 𝑡%$ = 𝑡%,
à il tempo di ritardo dipende linearmente da 𝑋 (non più da X )
à conviene inserire il buffer se 𝑋 > 4
à se X è molto grande comunque il ritardo può essere elevato
à possibilità di inserire ulteriori buffer !!


Quanti buffer metto ?
                                                        Cascata di buffer




• Tra l’inverter n.1 e la capacità di carico metto altri (N-1) buffer
• I buffer hanno un dimensionamento crescente: le dimensioni del successivo sono U
   volte quello del precedente à il rapporto tra le capacità di uscita e di ingresso è
   sempre pari a U
         𝐶!/$
  𝑡%! =       , 𝑡%* = 𝑈 , 𝑡%*   con 𝑖 = 1, … , 𝑁 − 1 (tutti i tempi di ritardo sono 𝐮𝐠𝐮𝐚𝐥𝐢 ‼)
          𝐶!
                    𝐶&           𝐶&
            𝑡%0 =      , 𝑡%* = 01$      , 𝑡%* (tempo di ritardo dell' ultimo buffer)
                    𝐶0        𝑈      𝐶$
Si dimostra facilmente che il caso ottimo è quando tutti i tempi di ritardo sono uguali:
                                                                            𝐶&
                          𝐶&                                            ln        ln 𝑋
                                                                            𝐶!"
      𝑡%! = 𝑡%0 → 𝑈 = 01$         → 𝐶& = 𝑈 0 𝐶$ = 𝑈 0 𝐶!" → 𝑁-%. =              =
                       𝑈       𝐶$                                         ln 𝑈    ln 𝑈
                                                     Cascata di buffer




        ln 𝑋                                              ln 𝑋
 𝑁-%. =                   𝑡% = U 𝑡%! = 𝑁-%. , 𝑈 , 𝑡%* =        , 𝑈 , 𝑡%*
        ln 𝑈                                              ln 𝑈

 Come dimensiono i buffer ? à ricerco il ritardo ottimo !

 𝜕𝑡%         ln 𝑋              ln 𝑋           ln 𝑋         1
     = 𝑡%* ,      − 𝑡%* , 𝑈           = 𝑡%* ,      , 1 −      = 0 ⇒ 𝑈-%. = 𝑒
 𝜕𝑈          ln 𝑈           𝑈 (ln 𝑈),         ln 𝑈       ln 𝑈
                                                                                        𝐶&
                                 𝐶&                                  𝑁-%. = ln 𝑋 = ln
 𝑡% -%. = 𝑁-%. , 𝑈-%. , 𝑡%* = ln     , 𝑒 , 𝑡%*                                          𝐶!"
                                 𝐶!"

Attenzione: Nopt deve essere un numero intero !! U = e non è banale da realizzare !!
à approssimo! es.: U = 3 (comunque la dipendenza da U è limitata; ritardi simili)
                Singolo buffer vs. cascata di buffer
                            Senza buffer       Singolo buffer     Cascata di buffer
X = CL / Cin     Nopt
                                [tp0]               [tp0]               [tp0]

     10         2.3 ≈ 2           10                  6.3                6.3

    102         4.6 ≈ 5          100                  20                12.5

    103         6.9 ≈ 7         1000                  63                18.8

    104         9.2 ≈ 9         10000                200                25.0

                                 ∝𝑋                 ∝ 𝑋                ∝ ln 𝑋


• L’utilizzo dei buffer riduce notevolmente il tempo di ritardo
• Anche catene lunghe di buffer, comunque presentano vantaggi notevoli se le
  capacità di carico sono elevate !!
