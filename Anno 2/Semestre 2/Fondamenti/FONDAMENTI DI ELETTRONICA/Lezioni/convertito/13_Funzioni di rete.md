---
fonte: "13_Funzioni di rete.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Funzioni di rete

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                                                         Amplificatori
• Gli amplificatori sono circuiti in grado di trattare segnali analogici tempo
  varianti e trasformarli in un segnale di uscita corrispondente
• I segnali possono essere sia di tensione e di corrente
• Tipicamente gli amplificatori hanno comportamento non lineare e
  presentano effetti reattivi, in quanto realizzati sfruttando dei transistor
à Linearizzazione + trasformate di Laplace
à Assumo il dispositivo come un doppio bipolo (nella maggioranza dei casi
  si tratta di tripoli)
à Amplificatore descritto tramite matrici e circuiti equivalenti

                                                   𝑦!!     𝑦!"   𝑦#   𝑦$
                                               𝑌 = 𝑦       𝑦"" = 𝑦%   𝑦&
                                                    "!



Come valuto le prestazioni degli amplificatori ?
à tramite le FUNZIONI DI RETE
                                                         Funzioni di rete
Una FUNZIONE di RETE è un qualsiasi rapporto tra grandezze elettriche nel
circuito
Alcune funzioni di rete sono più interessanti di altre:
                                        $! (&)
• Guadagno di tensione à 𝐴$ =
                                        $" (&)
                                                               𝑖(              𝑖'
                              (! (&)
• Guadagno di corrente à 𝐴( =                                  𝑣(                   𝑣'
                              (" (&)
                                          $" (&)
• Impedenza di ingresso à 𝑍() =
                                          (" (&)
                               $! (&)
• Impedenza di uscita à 𝑍*+, =       $                    dove 𝑆( è il segnale di ingresso
                               (! (&) - ./
                                                   "


à Amplificatore descritto tramite matrici e circuiti equivalenti
à Se ho la matrice descrittiva, mi posso disinteressare di come è fatto realmente il
  circuito e utilizzare il circuito equivalente per calcolare le funzioni di rete !!
                            Utilizzo dei circuiti equivalenti
• Linearizzo l’amplificatore
• Se ci sono effetti reattiviDoppi
                             passo al bipoli
                                      dominio delle trasformate
                                              terminati
• Descrivo l’amplificatore attraverso una matrice ed un circuito
  equivalente


                         Sorgente            Doppio
                                                                 Carico
                                             bipolo




        Ɣ Nellesarà
L’amplificatore  applicazioni
                      connesso pratiche si incontra
                                   ad una   sorgentespesso  il casoall’ingresso
                                                      di segnale    in cui le porteeddiad
                                                                                        un
           doppio all’uscita
un «utilizzatore»  bipolo sonoàcollegate
                                 li possoadescrivere
                                             due bipoli come   mostratodei
                                                          attraverso     nella  figura
                                                                             circuiti
equivalenti  attraverso
        Ɣ Il primo bipolo il teoremaladisorgente
                           costituisce      Thevenin:
                                                    del segnale in ingresso al doppio
           bipolo e può rappresentare il circuito equivalente di Thévenin o Norton
•   Sorgente   = stati
           degli generatore     di tensione + impedenza in serie
                       precedenti
•   Carico
        Ɣ Il=secondo
              impedenza      equivalente
                        bipolo costituisce il carico e può rappresentare l’impedenza
           equivalente degli stati successivi
à Ottengo il circuito equivalente del sistema da studiare
                                   Esempio: matrice «h»
•   Amplificatore descritto
    tramite matrice «h» nel
    dominio s
•   Sorgente e carico
    sostituiti con circuiti
    equivalenti di Thevenin

à 1) Calcolo il GUADAGNO
    DI CORRENTE

                                                Se vogliamo che AI
                                                caratterizzi solo
                                                l’amplificatore
                                                indipendentemente dal
                                                carico dobbiamo usare
                                                ZC=0 à Guadagno di
                                                corto circuito AIcc
Il guadagno di corrente dipende dal carico ZC
                                           Esempio: matrice «h»
2) Calcolo l’IMPEDENZA DI
INGRESSO
       𝑉( ℎ# 𝐼( + ℎ$ 𝑉' ℎ# 𝐼( − ℎ$ 𝑍) 𝐼'
𝑍( =      =            =
       𝐼(       𝐼(             𝐼(
               𝐼'
𝑍( = ℎ# − ℎ$ 𝑍) = ℎ# − ℎ$ 𝑍) 𝐴(
               𝐼(
           ℎ% ℎ$ 𝑍)         ℎ% ℎ$
𝑍( = ℎ# −           = ℎ# −
          1 + ℎ& 𝑍)        1
                              + ℎ&
                           𝑍)
L’impedenza di ingresso dipende dal carico ZC

Se vogliamo che ZI caratterizzi solo l’amplificatore indipendentemente dal carico
dobbiamo usare:
                                                                   %! %"       &$
ZC=∞ à Impedenza di ingresso di circuito aperto 𝑍!"# = ℎ$ −                =
                                                                    %#         %#
ZC=0 à Impedenza di ingresso di corto circuito        𝑍!"" = ℎ$
Se l’amplificatore è unilatero hr = 0 à 𝑍( = ℎ#
                                            Esempio: matrice «h»
3) Calcolo il GUADAGNO DI
TENSIONE




          𝑍) ℎ%             1
 𝐴* = −           ;
        1 + ℎ& 𝑍)           ℎ% ℎ$ 𝑍)
                      ℎ# −
                           1 + ℎ& 𝑍)

            𝑍) ℎ%         1 + ℎ& 𝑍)               𝑍) ℎ%    1 + ℎ& 𝑍)       𝑍) ℎ%
 𝐴* = −            ;                         =−          ;           =−
          1 + ℎ& 𝑍) ℎ# + ℎ# ℎ& 𝑍) − ℎ% ℎ$ 𝑍)    1 + ℎ& 𝑍) ℎ# + 𝐷+ 𝑍)    ℎ# + 𝐷+ 𝑍)

                                   Il guadagno di tensione dipende dal carico ZC

Se vogliamo che AV indipendente dal carico dobbiamo usare:
                                                                   %!
ZC=∞ à Guadagno di tensione di circuito aperto          𝐴'"# = −
                                                                   &$
                                          Esempio: matrice «h»
4) Calcolo l’IMPEDENZA DI
USCITA
Devo annullare il segnale di
ingresso !! à VG = 0




          1                ℎ# + 𝑍,         ℎ# + 𝑍,       L’impedenza di uscita
𝑍' =              =                      =
           ℎ% ℎ$    ℎ& ℎ# + ℎ& 𝑍, − ℎ% ℎ$ 𝐷+ + ℎ& 𝑍,     dipende dall’impedenza
     ℎ& −
          ℎ# + 𝑍,                                        del generatore ZG
                                                                                +!
                                                           es.: ZG = 0 à 𝑍' =
                                                                                -"
Se l’amplificatore è unilatero hr = 0
             =# >?$      @
à 𝑍* =                 =                 hr responsabile del fatto che monte e valle
          =% =# >=% ?$   =%
                                         si «vedano» !!
                                                  Amplificatore unilatero
   • Se l’amplificatore è unilatero (hr = 0), i segnali vanno
                                                          69 solo dall’ingresso verso
     l’uscita e non viceversa !
   • Monte e valle non si «vedono»
 • Caratterizziamo l’amplificatore con le sue funzioni di rete
quivalenti      del doppio
                       %     !   %
                                    bipolo
                                        !           *
   à 𝐴!"" = ℎ( , 𝐴'"# = −        =−           , 𝑍! = ℎ$ , 𝑍) =
                            &$        %% %#                      %#
  la sorgente, il doppio bipolo può essere
                                 L’amplificatore
 a resistenza equivalente Rin che,    in generale,è lineare (o per lo meno è stato
 nzasedi𝐼'carico R               linearizzato!) à vale la sovrapposizione degli effetti
            = 0 à 𝑉L' = 𝐴*./ 𝑉(
                                     𝑉' =rappresentato
   carico, il doppio bipolo può essere     𝐴*./ 𝑉( + 𝑍' 𝐼'
      se 𝑉( = 0 à
  equivalente   di𝑉tipo
                    ' = Thévenin
                        𝑍' 𝐼'    o Norton, i cui
 e, dipendono dalla resistenza delinoltre   vale che:R 𝑉( = 𝑍( 𝐼(
                                       generatore       S


                                                Circuito equivalente di Thevenin della
                            𝑍'                  porta di ingresso e della porta di uscita
                𝑍(       𝐴*./ 𝑉(
                                                à Circuito equivalente dell’amplificatore
                                                  in base alle sue funzioni di rete
                         Amplificatore unilatero
quivalenti del doppio bipolo
   • Se l’amplificatore è unilatero (hr = 0), i segnali vanno solo dall’ingresso verso
ella l’uscita e non
      sorgente,      viceversa
                 il doppio     ! può essere
                           bipolo
na•resistenza   equivalente
     Monte e valle           Rin che, in generale,
                     non si «vedono»
enza   di carico RL l’amplificatore con le sue funzioni di rete
   • Caratterizziamo
el carico, il doppio bipolo%può
                             !   essere
                                     %!     rappresentato*
   à  𝐴 !"" =
o equivalente ℎ , 𝐴
               (di tipo = −    =
                    '"# Thévenin −        ,
                                  o %Norton,𝑍! =i cui
                                                  ℎ$ , 𝑍) =
                            &$       % %#                   %#
ale, dipendono dalla resistenza del generatore RS
                                     L’amplificatore è lineare (o per lo meno è stato
                                     linearizzato!) à vale la sovrapposizione degli effetti
     se 𝑉' = 0 à 𝐼' = 𝐴(.. 𝐼(
                                                        𝑉'
                      *
     se 𝐼( = 0 à 𝐼' = 0#               𝐼' = 𝐴(.. 𝐼( +                                 *$
                                                        𝑍'   inoltre vale che: 𝐼( =
                       #                                                              0$




                                            Circuito equivalente di Northon della
                                            porta di ingresso e della porta di uscita
                𝑍(              𝑍'
                                            à Circuito equivalente dell’amplificatore
                                              in base alle sue funzioni di rete
                     𝐴(.. 𝐼(
                        Amplificatore ideale di tensione
                       Circuiti equivalenti del doppio bipo
• Assumiamo di studiare un amplificatore di tensione unilatero
            Ɣ Dal
• Caratterizzato    punto
                 dalle sue di vista della
                           funzioni di retesorgente, il doppio bipolo può essere
              %! rappresentato
                      %!         da una resistenza
                                          *          equivalente Rin che, in gene
à 𝐴'"# = −        =−     , 𝑍! = ℎ$ , 𝑍) =
              & dipende
                $    % % dalla resistenza
                           % #            % di carico R
                                              #             L
Hp. semplificativa:
           Ɣ Dal non    ci sono
                    punto  di vistaeffetti
                                      delreattivi
                                           carico,àil impendenza   di ingresso
                                                       doppio bipolo   può essere e dirapp
uscita sono delle resistenze
               mediante          𝑍! = 𝑅$+equivalente
                           un !!circuito   , 𝑍) = 𝑅,-. (lavoriamo
                                                         di tipo Thévenin
                                                                  nel dominioodel
                                                                               Norton,
                                                                                  tempo) i
à alimentiamoparametri,     in generale,
               il circuito con           dipendono
                               un generatore          dalla
                                             di tensione    resistenza deladgenera
                                                          e colleghiamolo
una resistenza di carico RL

Qual è il guadagno di
tensione del circuito in
                                                                    𝐴*./ 𝑣!
esame ?

            𝑅1
  𝑣" =            ;𝐴 𝑣                   𝑣/ 𝑣/ 𝑣*    𝑅1           𝑅$+
         𝑅1 + 𝑅&23 *./ !            𝐴' =   =  ( =          (𝐴  (
                                         𝑣0 𝑣* 𝑣0 𝑅1 + 𝑅,-. '"# 𝑅2 + 𝑅$+
           𝑅#4
  𝑣! =           ;𝑣          Amplificatore di tensione IDEALE à 𝑅#4 = ∞, 𝑅&23 = 0
         𝑅5 + 𝑅#4 6
                             Il guadagno è massimo ed indipendente da sorgente e carico !
                     Ɣ Dal punto di vista della sorgente, il doppio bipolo può essere
                         Amplificatore ideale di corrente
                        rappresentato da una resistenza equivalente Rin che, in gener
                        dipende dalla resistenza di carico RL
                     Ɣ Dalun
• Assumiamo di studiare     punto  di vista deldicarico,
                              amplificatore              il doppio
                                                  corrente         bipolo può essere rappr
                                                              unilatero
                        mediante un circuito equivalente di tipo Thévenin o Norton, i c
• Caratterizzato dalle sue  funzioni
                        parametri, in di rete
                                      generale,   dipendono dalla resistenza del generat
                                 *
à 𝐴!"" = ℎ( , 𝑍! = ℎ$ , 𝑍) = %
                                 #

Hp. semplificativa: non ci sono effetti reattivi à impendenza di ingresso e di
uscita sono delle resistenze !! 𝑍! = 𝑅$+ , 𝑍) = 𝑅,-. (lavoriamo nel dominio del tempo)
à alimentiamo il circuito con un generatore di corrente e colleghiamolo ad una
resistenza di carico RL

Qual è il guadagno di corrente
del circuito in esame ?                     𝑅5              𝑅#4             𝑅&23     𝑅1

        𝑅&23
 𝑖" =          ;𝐴 𝑖                                               𝐴(.. 𝑖!
      𝑅1 + 𝑅&23 (.. !
                                         𝑖/ 𝑖/ 𝑖*   𝑅,-.           𝑅2
                                     𝐴! = = ( =            (𝐴 (
          𝑅5                             𝑖0 𝑖* 𝑖0 𝑅1 + 𝑅,-. !"" 𝑅2 + 𝑅$+
𝑖! =           ;𝑖
       𝑅5 + 𝑅#4 6
                         Amplificatore di corrente IDEALE à 𝑅#4 = 0, 𝑅&23 = ∞
                         Il guadagno è massimo ed indipendente da sorgente e carico !
                      Funzioni di rete e matrici

Le funzioni di rete
possono essere
calcolate dalle
componenti di una
qualunque delle
matrici descrittive
del doppio-bipolo
                           Guadagno di tensione inverter
                                        Avevamo definito il guadagno di
                                        tensione dell’inverter come:
                                                                𝑑𝑉'
                                                        𝐴* =
               (1)                                              𝑑𝑉(

                                         Caratteristica statica dell’inverter

                                                    VO=f(Vin)
                                                                        𝑑𝑉'
                                            Linearizzo à         𝑣' =       E 𝑣
                                                                        𝑑𝑉( 7 (
                     (2)
                                           A livello statico non ho effetti reattivi
VT,P

                     VLT                                𝑣' 𝑑𝑉'
                                                           =    E = 𝐴*
                                                        𝑣(   𝑑𝑉( 7

  La definizione che abbiamo dato del guadagno di corrente è congruente con
  quella data a suo tempo !
                   Guadagno di tensione per VLT
                          Considerando i MOSFET come ideali
                          (privi di effetto di modulazione di
                          lunghezza di canale), il guadagno di
                          tensione alla soglia logica è 𝐴* = ∞
       (1)

                           Quanto vale se l > 0 ?

                                     𝑣' 𝑑𝑉'
                                        =    E = 𝐴*
                                     𝑣(   𝑑𝑉( 7


                             Lo posso ottenere dal circuito
             (2)
                             equivalente ai piccoli segnali
VT,P

             VLT
                       Circuito equivalente dell’inverter
                                      Sostituiamo ogni transistor con il suo
                                      circuito equivalente ai piccoli segnali




            vdd=0
            Sp
     vgsp
            gmp vgsp                Dobbiamo sostituire la tensione di
                        gdsp        alimentazione Vdd con il suo valore di piccolo
vi                             vo   segnale (vdd variazione rispetto al valore nel
            Dp
            Dn
                                    punto di lavoro):

                        gdsn        se Vdd è costante à vdd = 0 (come se fosse un
            gm vgsn
     vgsn                           riferimento di massa!!)
             Sn
                                    vgs,n = vgs,p = vgs
                         Circuito equivalente dell’inverter
vi
                                                          vo
                 gm,n vgs                 gdsn                        𝑔8,4 𝑣:6 + 𝑔8,; 𝑣:6
                                                               𝑣& = −
                                                                        𝑔-5,4 + 𝑔-5,;
        vgs
                            gm,p vgs               gdsp               𝑔8,4 + 𝑔8,;
                                                               𝑣& = −              𝑣
                    Sn                                                𝑔-5,4 + 𝑔-5,; #


          𝑣'    𝑔8,4 + 𝑔8,;                        𝑔8,4 + 𝑔8,;
     𝐴* =    =−                         𝐴* G    =−               H
          𝑣(    𝑔-5,4 + 𝑔-5,;               *%&    𝑔-5,4 + 𝑔-5,;
                                                                  *%&


Alla soglia logica entrambi i MOSFET sono saturi

 𝑔8,4 = 𝛽4 (𝑉,54 −𝑉<4 )(1 + 𝜆4 𝑉-54 )              𝑔8,; = 𝛽; |𝑉,5; − 𝑉<; |(1 + 𝜆; 𝑉5-; )
           𝛽4                                               𝛽;
 𝑔-5,4 = 𝜆4 (𝑉,54 −𝑉<4 )"                         𝑔-5,; = 𝜆; (𝑉,5; −𝑉<; )"
           2                                                2
                         Circuito equivalente dell’inverter
                        𝑉1< = 𝑉( = 𝑉'    𝑉,54 = 𝑉-54 = 𝑉1<        𝑉,5; = 𝑉-5; = 𝑉1< − 𝑉==

                         Hp.: 𝑉<4 = −𝑉<; = 𝑉< ; 𝜆4 = 𝜆; = 𝜆 ; 𝛽4 = 𝛽; = 𝛽 à 𝑉1< = 𝑉== /2

                                                             𝑉==              𝑉==
                         𝑔8,4 = 𝛽(𝑉1< −𝑉< )(1 + 𝜆𝑉1< ) = 𝛽       − 𝑉<   1+𝜆
                                                              2                2
                                                                 𝑉==              𝑉==
                         𝑔8,; = 𝛽 𝑉1< − 𝑉== + 𝑉< 1 + 𝜆𝑉1<     =𝛽     − 𝑉<     1+𝜆
                                                                  2                2

                                      "
          𝛽                𝛽 𝑉==
 𝑔-5,4 = 𝜆 (𝑉1< −𝑉< )" = 𝜆       − 𝑉<
          2                2 2
                                            "
          𝛽                      𝛽 𝑉==
 𝑔-5,; = 𝜆 (𝑉1< −𝑉== + 𝑉< )" = 𝜆       − 𝑉<
          2                      2 2
                   𝑉==              𝑉==
              2𝛽    2  − 𝑉<   1 + 𝜆  2 = − 2 + 𝜆𝑉== = − 2 2 + 𝜆𝑉==
𝐴* G     =−
   *%&                  𝑉==       "         𝑉==        𝜆 𝑉== − 2𝑉<
                    𝜆𝛽      − 𝑉<          𝜆 2   − 𝑉<
                         2
                                                           se 𝜆 = 0 à 𝐴* = −∞
                                                Funzioni di rete del BJT
        B                                                 C
                                                                     Anche per il BJT
                                                                     possiamo calcolare delle
                            𝐶>)                                      funzioni di rete
                                                               𝑣)?
𝑣>?                                           𝑔8 𝑣>?     𝑟)?
            𝑟>?      𝐶>?                                             à regione NORMALE
                                                                            𝒓𝑩𝑪 → ∞
                             E

                             1                                              𝑌8 = 0
                                + 𝑠𝐶67 + 𝑠𝐶68          −𝑠𝐶68
      𝑦$           𝑦5       𝑟67
  𝑌 = 𝑦            𝑦, =                                               funzionamento a vuoto
       (                                             1
                                  𝑔9 − 𝑠𝐶68             + 𝑠𝐶68
                                                    𝑟87

                    𝑦$ 𝑦%         𝑦$ 𝑦%
      𝑌(@ = 𝑦# −           = 𝑦# −             Ammettenza di ingresso
                   𝑦& + 𝑌)         𝑦&

                       𝑦&                     𝐷B = 𝑦# 𝑦& − 𝑦% 𝑦$
      𝑍(@ = 𝑌(@ A! =
                       𝐷B
                           Impedenza di ingresso del BJT
                                                1
                   𝑦&                              + 𝑠𝐶>)
            A!                                𝑟)?
𝑍(@ = 𝑌(@        =    =
                   𝐷B      1                    1
                              + 𝑠𝐶>? + 𝑠𝐶>)        + 𝑠𝐶>) + 𝑔8 − 𝑠𝐶>) 𝑠𝐶>)
                          𝑟>?                  𝑟)?

Espressione complicata; dipende dalla frequenza del segnale
se 𝑦$ è piccolo à 𝐷B ≅ 𝑦# 𝑦&

                   1                     𝑟>?
𝑍(@ ≅                          =
         1                       1 + 𝑠𝑟>? 𝐶>? + 𝐶>)
            + 𝑠𝐶>? + 𝑠𝐶>)
        𝑟>?

                                                               !
Funzione passa-basso con un polo a pulsazione p = −
                                                          $'( )'( C)')

All’aumentare della frequenza l’impedenza di ingresso si abbassa
Va male per gli amplificatori di tensione !
                               Impedenza di uscita del BJT
              𝑦$ 𝑦%
 𝑌'D< = 𝑦& −                   Ammettenza di uscita; dipende anche dalla sorgente
             𝑦# + 𝑌,
Il BJT è un buon amplificatore di corrente in regione normale 𝐼) = 𝛽E 𝐼>
Hp.: generatore ideale di corrente in ingresso à 𝑌, = 0                         𝑦$ 𝑦%
                                                                  𝑌'D< = 𝑦& −
                                                                                 𝑦#
                                     1
               𝑦#                       + 𝑠𝐶>? + 𝑠𝐶>)
            A!                      𝑟>?
 𝑍'D< = 𝑌'D< =    =
               𝐷B    1                   1
                    𝑟>? + 𝑠𝐶>? + 𝑠𝐶>)   𝑟)? + 𝑠𝐶>) + 𝑔8 − 𝑠𝐶>) 𝑠𝐶>)

Espressione complicata; dipende dalla frequenza del segnale
se 𝑦$ è piccolo à 𝐷B ≅ 𝑦# 𝑦&
              1                𝑟)?
 𝑍'D< ≅                =
           1               1 + 𝑠𝑟)? 𝐶>)
          𝑟)? + 𝑠𝐶>)
                                                           !
Funzione passa-basso con un polo a pulsazione p = −
                                                        $)( )')

All’aumentare della frequenza l’impedenza di uscita si abbassa
                   Amplificazione di corrente del BJT
 Il BJT è un buon amplificatore di corrente in regione normale 𝐼) = 𝛽E 𝐼>

                𝑦%         𝑔8 − 𝑠𝐶>)            𝑔8 𝑟>? − 𝑠𝐶>) 𝑟>?      𝛽F − 𝑠𝐶>) 𝑟>?
𝑌) = ∞   𝐴(.. =    =                        =                     =
                𝑦#       1                    1 + 𝑠𝑟>? 𝐶>? + 𝐶>)    1 + 𝑠𝑟>? 𝐶>? + 𝐶>)
                            + 𝑠𝐶>? + 𝑠𝐶>)
                        𝑟>?
                                                      B                                     C
        𝐼" (𝑠) 𝐼) (𝑠)
 𝐴(.. =       =                                                       𝐶!#                        𝑣$#
        𝐼! (𝑠) 𝐼> (𝑠)                           𝑣!"
                                                          𝑟!"
                                                                                  𝑔! 𝑣"#   𝑟$#
                                                                𝐶!"

                                                                       E
                         𝐶 𝑟
                    1 − 𝑠 >) >?
                           𝛽F            Dipende dalla frequenza dei segnali !!
  𝐴(.. (𝑠) = 𝛽F
                1 + 𝑠𝑟>? 𝐶>? + 𝐶>)
                                         Espressione con un polo ed uno zero

             1                  𝛽F          𝑧          𝐶>?                  Tendenzialmente
p=−                        z=                 = 𝛽F 1 +     ≫1
      𝑟>? 𝐶>? + 𝐶>)           𝑟>? 𝐶>)       𝑝          𝐶>)                     |𝑧| ≫ |𝑝|

La stima di z non è affidabile; ad alte frequenze il modello di Ebers-Moll da cui
siamo partiti non è realistico !!
                            Comportamento in frequenza
• Dal guadagno di corrente di corto circuito possiamo studiare il comportamento in
  frequenza del BJT
à diagramma di Bode asintotico del modulo del guadagno di corrente di corto circuito
à passiamo al dominio delle trasformate di Fourier s = jw
                           𝐶 𝑟
                     1 − 𝑗𝜔 >) >?                                       1
                              𝛽F
 |𝐴(.. 𝑗𝜔 | = 𝛽F                                       𝜔> = |p| =
                 1 + 𝑗𝜔𝑟>? 𝐶>? + 𝐶>)                              𝑟>? 𝐶>? + 𝐶>)

                                                           Pulsazione di transizione
  𝐴(..                                                     (a volte chiamata di taglio)
  [dB]                                                     -3 dB sotto il valore massimo
   𝛽F                                -3 dB                            1
                                                                          = 0.707
                                                                       2
                                             20 dB/dec


                                             |z|
                                                   log 𝜔
                      𝜔> = |p|
                                    Pulsazione di cut-off del BJT
 𝐴(..
 [dB]                                                                                 1
                                                                  𝜔> = |p| =
  𝛽F                                                                           𝑟>? 𝐶>? + 𝐶>)
                                         -3 dB

        Banda passante                           20 dB/dec
                                                                   All’interno della banda
                                                                   passante (definita da 𝜔> ),
                                                 |z|                𝐴(.. è stabile

                                          𝝎𝑻           log 𝜔
                         𝜔> = |p|


• Il transistor guadagna fino a che 𝐴(.. > 1 à 𝝎𝑻 pulsazione di cut-off (o di taglio)
                                    𝝎𝑻
• Frequenza di cut-off 𝒇𝑻 =
                                    𝟐𝝅
                  𝛽F                                                             𝛽F
  𝐴(.. (𝑗𝜔) ≅               (trascuro lo zero)     à    𝐴(.. (𝑗𝜔 < ) = 1 =
                    𝜔                                                           𝜔< "
                1+𝑗                                                          1+ 𝜔
                    𝜔>                                                           >

   𝜔< "                  𝜔 < ≅ 𝛽F 𝜔>                                    𝛽F           𝑔8
        = 𝛽F " − 1 à                                       𝜔< =                 =
   𝜔>                                                             𝑟>? 𝐶>? + 𝐶>)   𝐶>? + 𝐶>)
                    prodotto banda-guadagno
                  Comportamento in banda passante
All’interno della banda passante posso trascurare gli                           1
                                                                   𝜔> =
effetti reattivi à comportamento quasi-stazionario                        𝑟>? 𝐶>? + 𝐶>)

      𝑖>
                                                     1
                                                            0
            𝑟>?                𝑟)?                  𝑟67
                                             𝑌 =
                      𝛽F 𝑖>?                                1
                                                     𝑔9
                                                           𝑟87


                                                           1
   𝐴!"" = 𝛽;                                 𝑍!< = 𝑅!< =      = 𝑟67
                                                           𝑦$

          𝑦(                                                     1
  𝐴'"# = − = −𝑔9 𝑟87                         𝑍)=> = 𝑅)=> =          = 𝑟87
          𝑦,                                                     𝑦,


                                                                               K'
 Funzioni di rete indipendenti dalla frequenza dei segnali (vale fino a 𝑓> =        )
                                                                               "L
                           Funzioni di rete del MOSFET
      G                                      D
                                                            Anche per il MOSFET
                                                            possiamo calcolare delle
                 𝐶,-
                                                   𝑣-5      funzioni di rete
𝑣,5                            𝑔8 𝑣,5        𝑔-5
          𝐶,5


                   S
                                       𝑦$          𝑦5   𝑠𝐶?2 + 𝑠𝐶?&             −𝑠𝐶?&
                                   𝑌 = 𝑦           𝑦, =
                                        (                𝑔9 − 𝑠𝐶?&            𝑔&2 + 𝑠𝐶?&

                                  𝐶,-
       𝑦%   𝑔8 − 𝑠𝐶,-         1−𝑠
                                  𝑔8               • 1 polo nell’origine (corrente statica nulla)
𝐴(.. =    =           = 𝑔8
       𝑦# 𝑠𝐶,5 + 𝑠𝐶,-      𝑠(𝐶,5 + 𝐶,- )           • 1 zero
                                                   (stima dello zero poco affidabile; cmq ad
                                                   alte frequenze)
            𝑔8
𝐴(.. ≅                                        𝑔8
       𝑠(𝐶,5 + 𝐶,- )
                          |𝐴(.. (𝑗𝜔)| ≅
                                          𝜔(𝐶,5 + 𝐶,- )
                     Pulsazione di cut-off del MOSFET
• Il transistor guadagna fino a che 𝐴(.. > 1 à 𝝎𝑻 pulsazione di cut-off (o di taglio)
                                 𝝎
• Frequenza di cut-off 𝒇𝑻 = 𝟐𝝅𝑻

                             𝑔8                                        𝑔8
   𝐴(.. (𝑗𝜔 < ) = 1 =                          à          𝜔< =
                      𝜔 < (𝐶,5 + 𝐶,- )                              𝐶,5 + 𝐶,-


• La pulsazione di cut-off ha definizione simile a quella del BJT
• Però 𝐶,5 e 𝐶,- ≫ 𝐶>? e 𝐶>) !! 𝑔8,M'5E?< < 𝑔8,>N< à 𝜔 <,M'5E?< ≪ 𝜔 <,>N<
• I BJT sono dispositivi tipicamente più veloci dei MOSFET


MOSFET: 𝐶,5 e 𝐶,- costanti à 𝜔 < ∝        𝐼-5F (dipende dal punto di lavoro)

                                         :+        :+         !
BJT: tipicamente 𝐶>? ≫ 𝐶>) à 𝜔 < =             =          =        (non dipende dal punto di lavoro)
                                         )'(       :+O,       O,

 𝜔<                                       • Dipende dal tempo di transito in base !
                                          • Base stretta à BJT veloci !
                                          (Larghezza della base < lunghezza di gate)
                               𝑉>?
