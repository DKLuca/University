---
fonte: "14_Amplificatori elementari.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Analisi di piccolo segnale
     degli amplificatori elementari

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi
                   Francesco Driussi – 2020
                                  Analisi di piccolo segnale
Lo scopo finale dell’analisi di piccolo segnale è calcolare le funzioni di rete:
1. Calcolo del punto di lavoro di un amplificatore
2. Linearizzazione del circuito ed disegno del circuito equivalente ai
   piccoli segnali
3. Calcolo dei parametri differenziali del circuito equivalente
4. Estrazione della matrice descrittiva del circuito
5. Calcolo delle FUNZIONI DI RETE




                                                   𝑦!!    𝑦!"   𝑦#    𝑦$
                                               𝑌 = 𝑦      𝑦"" = 𝑦%    𝑦&
                                                    "!
                               Esempio: BJT connesso a diodo
      𝐼'                          1. Calcolo del punto di lavoro:
                                  • VCB = 0 à limite della regione attiva, effetto Early nullo
                                  • VBE = VCE à ho un’unica tensione e un’unica corrente
𝐼)               𝐼*
                                  • punto di lavoro 𝑄 ≡ (𝐼'( , 𝑉)'( )
                          𝑉)'
                                                                   𝐼*(      1         𝑉)'(
                                         𝐼'( = 𝐼*( + 𝐼)( = 𝐼*( +       = 1+    𝐼, 𝑒𝑥𝑝
                                                                   𝛽+       𝛽+         𝑉-.
      𝐼'                          2. Estrazione del circuito equivalente di piccolo segnale:
                                  • Il BJT viene sostituito dal suo circuito equivalente ai
                                    piccoli segnali (trascuro gli effetti reattivi)
                                  3. Calcolo parametri differenziali
            𝑖'                                                        𝑉-.   𝑉-. 1 + 𝛽+       (ordine
                                                             𝑟)' =        =                  del kW)
                                                                     𝐼)'(       𝐼'(
                                  • Senza effetto Early, 𝑟*' sparisce !
𝑖)'   𝑟)'              𝑔/ 𝑣)'                                           𝑣)'   1 + 𝛽(
                                        𝑖' = 1 + 𝛽( 𝑖)' = 1 + 𝛽(            =        𝑣)'
                      𝛽( 𝑖)'                                            𝑟)'     𝑟)'
                                 𝑣)'             𝑣)'     𝑟)'
           𝑖'                               𝑅0 =     =                   (molto piccola; dell’ordine
                                                  𝑖'   1 + 𝛽(            delle decine di W)
       Ɣ DalƔpunto
               Dal di vistadidella
                    punto     vistasorgente,     il doppio
                                    della sorgente,            bipolo bipolo
                                                           il doppio   può essere
                                                                               può ess
         rappresentatoEsempio:
                        da unada
               rappresentato        unaSpecchio
                                 resistenza      equivalente
                                          resistenza            diRcorrente
                                                                          Rininche,
                                                                    in che,
                                                          equivalente           genera
                                                                                     in g
         dipende dalla resistenza
               dipende               di carico
                         dalla resistenza         RL
                                              di carico     RL
                                à Q1 e Q2 lavorano in regione normale
𝐼1'+
       Ɣ DalƔpunto
               Dal di vistadidel
                    punto        carico,
                              vista       il doppio
                                    del carico,         bipolo bipolo
                                                    il doppio    può essere     rappre
                                                                         può essere
         mediante  un circuito  à inoltre VBE1 =diVBE2
                                equivalente         tipo= VThévenin     o Norton,   i cu
               mediante   un circuito   equivalente       diBEtipo Thévenin     o Norto
         parametri, in generale,
               parametri,       à trascuro
                                   dipendono
                           in generale,     l’effetto Earlyresistenza
                                                   dalla
                                           dipendono                     del generato
                                                             dalla resistenza    del ge
                                                            𝑉)'(                        𝛽+
            𝐼)!    𝐼)"               𝐼*!( = 𝐼*"( = 𝐼, 𝑒𝑥𝑝                   𝐼*"( =          𝐼
                                                             𝑉-.                      𝛽+ + 2 1'+


                  𝑉)'
                                              Circuito equivalente di piccolo segnale

                                       𝑖1'+
                                                     𝑖)'"                                   𝑖*"
Q1 è connesso a diodo à lo posso
sostituire con la sua resistenza                                           𝑔! 𝑣"#
differenziale                            𝑅0          𝑣)'        𝑟)'"        𝛽! 𝑖"#$    𝑟$#% 𝑣$#%
                         𝑟)'!
                 𝑅0 =
                        1 + 𝛽(

Calcolo parametri differenziali
à i BJT sono polarizzati con la stessa corrente               𝑉-.         𝑉-. 𝛽+
                                                     𝑟)'" =           =          = 𝑟)'! = 𝑟)'
                                                              𝐼)'"(        𝐼*"(
à parametri differenziali identici se BJT uguali
                                     Esempio: Specchio di corrente
 𝑖1'+
                   𝑖)'"                                𝑖*"       Estrazione delle funzioni di rete
                                                                 dello specchio di corrente
                                      𝑔! 𝑣"#
                                                                 à non ci sono effetti reattivi à
  𝑅0                𝑣)'        𝑟)'     𝛽! 𝑖"#$    𝑟$#% 𝑣$#%      posso fare i calcoli nel dominio del
                                                                 tempo
                                                                                  𝑣)'
                                                                          𝑖1'+ =       + 𝑖)'"
                                                                                   𝑅0
    𝑣2 𝑣)'      𝑣)'           1       1             70      70
                                                             1           𝑟)'
𝑅2 = =      =𝑣           =        =       = 𝑅0 ∥ 𝑟)' =               =
    𝑖2 𝑖1'+   )'
                 + 𝑖       1 𝑖)'"   1   1              1 + 𝛽(     1    2 + 𝛽(
             𝑅0      )'"     +        +                        +
                           𝑅0 𝑣)' 𝑅0 𝑟)'                 𝑟)'     𝑟)'
        𝑣*'"
𝑅3 =         <            = 𝑟*'"                                         𝑣*'"             𝑣*'"
         𝑖*" #                                          𝑖*" = 𝑔/ 𝑣)' +        = 𝛽( 𝑖)'" +
                 !"# 4(
                                                                         𝑟*'"             𝑟*'"
                                                 se trascuro l’effetto Early (𝑟*'" = ∞): 𝑖*" ≅ 𝛽( 𝑖)'"

    𝑖3  𝑖*"    𝛽( 𝑖)'"        𝛽( 𝑖)'"           𝛽( 𝑖)'"       𝛽(
𝐴2 = =      =          =                    =             =
    𝑖2 𝑖1'+ 𝑣)' + 𝑖)'"   1 + 𝛽( 𝑣)'           2 + 𝛽( 𝑖)'"   2 + 𝛽(
              𝑅0                     + 𝑖)'"
                            𝑟)'
 Se 𝛽( è grande, anche al piccolo segnale 𝑖*" ≅ 𝑖1'+ à specchia il segnale di corrente !
                                            Emettitore comune (E. C.)
                                      Vce

                                      Vcc


                                                   Q
                                  t



                                Vce,sat

                                                                 Vbe

                                                   t


• L’emettitore comune è uno stadio amplificatore elementare à amplifica l’ampiezza
  del segnale di ingresso à quanto amplifica ?
• Il circuito è non lineare à difficile l’analisi dinamica !!
• Funziona bene se il BJT lavora in regione normale (alta pendenza della caratteristica)
1. Calcolo del punto di lavoro:
                                              5$"                                              5$"
• In regione attiva/normale 𝐼* = 𝐼, 𝑒𝑥𝑝                ; 𝑉*' = 𝑉** − 𝑅* 𝐼* = 𝑉** − 𝑅* 𝐼, 𝑒𝑥𝑝
                                               5%&                                             5%&
• punto di lavoro 𝑄 ≡ (𝐼)( , 𝑉)'( , 𝐼*( , 𝑉*'( )
                                                                             in
  dipende dalla resistenza
        dipende               di carico
                  dalla resistenza        RL
                                       di carico   RL
Ɣ DalƔpunto
        Dal di vistadidel
             punto     vista
                               Circuito
                          carico,  il doppio
                             del carico,
                                                 equivalente
                                                bipolo bipolo
                                            il doppio  può essere
                                                                         E.   C.
                                                                       rappresenta
                                                               può essere      rappr
  mediante  un circuito
        mediante         equivalente
                   un circuito           di tipo di
                                 equivalente      Thévenin    o Norton,
                                                    tipo Thévenin          i cui i c
                                                                      o Norton,
                        2. Estrazione del circuito equivalente di piccolo segnale:
  parametri, in generale,
        parametri,          dipendono
                    in generale,           dalla resistenza
                                    dipendono                  del generatore
                                                   dalla resistenza     del genera RS
                              • Il BJT viene sostituito dal suo circuito equivalente ai
                                piccoli segnali
                              • Trascuro gli effetti reattivi (studio il circuito all’interno
                                della banda passante dell’amplificatore)
                              • Studio del comportamento quasi-stazionario
                              • VCC costante à vCC = 0 (massa)
                                               𝑖)'                                𝑖*
                                                                  𝑔! 𝑣"#
 3. Calcolo parametri differenziali            𝑣)'                  𝛽! 𝑖"#   𝑟*' 𝑣*'
                                                          𝑟)'                                   𝑅6*

            𝑉-.   𝑉-. 𝛽+
     𝑟)' =      =
           𝐼)'(    𝐼*(

            𝐼*(               𝑉7                Ora il circuito equivalente ai piccoli
     𝑔/ =             𝑟*' =
            𝑉-.               𝐼*(               segnali è completamente definito
                                        Funzioni di rete E. C.
𝑖)'                            𝑖*
                                            Estrazione delle funzioni di rete
                 𝑔! 𝑣"#                     dell’amplificatore ad emettitore comune
𝑣)'        𝑟)'    𝛽! 𝑖"#   𝑟*' 𝑣*'    𝑅6*   à non ci sono effetti reattivi à posso
                                            fare i calcoli nel dominio del tempo

                                                        𝑣2 𝑣)'
                                                    𝑅2 =   =      = 𝑟)'
                                               70       𝑖
                                                       702   𝑖 )'



     𝑣3 𝑣*' − 𝑅* ∥ 𝑟*' 𝑔/ 𝑣)'                              • AV è negativo
𝐴5 =   =    =                 = −𝑔/ 𝑅* ∥ 𝑟*'               à amplificatore invertente
     𝑣2 𝑣)'        𝑣)'
                                                           (sfasa di 180∘ il segnale)
                                                           • AV dipende da RC


       𝑖3   𝑖*   𝑟*'     𝑔/ 𝑣)'      𝑟*'
𝐴2 =      =    =       ?        =         ?𝛽               • se rCE è grande rispetto
       𝑖2 𝑖)' 𝑟*' + 𝑅*    𝑖)'     𝑟*' + 𝑅* (
                                                             a RC à 𝐴2 = 𝛽(
                                                               Funzioni di rete E. C.
 𝑖)'                                        𝑖*                 𝑖3 ′
                                                                      La definizione della resistenza di
                       𝑔! 𝑣"#                                         uscita dipende dal fatto se considero:
 𝑣)'             𝑟)'    𝛽! 𝑖"#       𝑟*' 𝑣*'                          • RC appartenente all’amplificatore
                                                        𝑅*              (interna al doppio bipolo)
                                                                      • RC come resistenza di carico
                                                                         all’amplificatore (esterna al doppio
                                                                               70
                                                                      70 bipolo)
                                     𝑅3                 𝑅3 ′
                                                                      In ingresso annullare il segnale
                                                                      comunque significa annullare sia 𝑣)'
                                                                      che 𝑖)' visto che sono legate da 𝑟)'

        𝑣3        𝑣*'                    𝑟*' 𝑖*
𝑅3 =       <    =     <              =          = 𝑟*'
        𝑖3 , 4(    𝑖* 8                    𝑖*
             '               $" 4(



        𝑣3          𝑣*'                 𝑣*'        1       1
𝑅39 =       <     =     <          =      𝑣*' = 𝑖*     =       = 𝑟*' ∥ 𝑅*
        𝑖3 ′ , 4(   𝑖3 ′ 8           𝑖* +            1   1   1
                             $" 4(        𝑅*       +       +
             '
                                               𝑣*' 𝑅* 𝑟*' 𝑅*
                      Amplificatore di tensione a E. C.
                                Vce

                                Vcc                          L’emettitore comune è un
                                                             buon amplificatore di
                                        Q                    tensione?
                           t
                                                             Dobbiamo valutare AV, RI, RO
                          Vce,sat

                                                   Vbe

                                        t



                               à può raggiungere anche valori elevati
  𝐴5:; = −𝑔/ 𝑅* ∥ 𝑟*'          à attenzione che se collego altri carichi in uscita, questi
                                 entrano nella formula

  𝑅2 = 𝑟)'         à 𝑟)' è dell’ordine del kW (non particolarmente elevata)
                   à amplificatore di tensione ideale 𝑅2 = ∞

                   à 𝑟*' è dell’ordine delle decine/centinaia di kW
  𝑅39 = 𝑟*' ∥ 𝑅*
                   à amplificatore di tensione ideale 𝑅3 = 0
                   à se riduco troppo 𝑟*' ∥ 𝑅* il guadagno crolla !! à TRADE OFF

L’emettitore comune ha buona amplificazione ma RI e RO non sono ideali à BUFFER !
ROOHWWRUHFRPXQH
                                            Collettore comune (C. C.)
                                  1. Calcolo del punto di lavoro:
                                                                                   5$"
                                  • In regione attiva/normale 𝐼* = 𝐼, 𝑒𝑥𝑝                 ;
                                                                                    5%&
                                                    <# =!            5$"(
                                  𝑉3 = 𝑅' 𝐼' = 𝑅'           𝐼, 𝑒𝑥𝑝          ;   𝑉)'( = 𝑉2 − 𝑉3
                                                     <#              5%&
                                  • punto di lavoro 𝑄 ≡ (𝐼)( , 𝑉)'( , 𝐼*( , 𝑉*'( )

                                  2. Estrazione del circuito equivalente di piccolo segnale:
                                  $PSOLILFDWRUHDFROOHWWRUHFRPXQ
                                  • Il BJT viene sostituito dal suo circuito equivalente
                                  • Trascuro gli effetti reattivi à comportamento quasi-
                                    stazionario
HJQDOLODWHQVLRQHGLXVFLWDFRLQFLGH          $QDOLVLSHUSLFFROLVHJQDOL
                                   • VCC costante à vCC = 0 (massa)

   3. Calcolo parametri differenziali
                                       

               𝑉-.   𝑉-. 𝛽+
      𝑟)' =        =
              𝐼)'(    𝐼*(

              𝐼*(                𝑉7
      𝑔/ =               𝑟*' =
              𝑉-.                𝐼*(
                                                                                                     $QDOLVLSHUSLFFROLVHJ
      $QDOLVLSHUSLFFROLVHJQDOL
$QDOLVLSHUSLFFROLVHJQDOL         Funzioni di rete C. C.
        $PSOLILFDWRUHDFROOHWWRUHFRPXQH                                  $QDOLVLSHUSLFFROLVHJQDOL


                                  $QDOLVLSHUSLFFROLVHJQDOL
                                                                                  Estrazione delle funzioni di rete
                                                                                  dell’amplificatore a collettore comune
                                                                                  à non ci sono effetti reattivi à posso
                                                                                  fare i calcoli nel dominio del tempo
                                       vR                     rFH                                      v                       r                    vR
                     iR     iH    
                                       R(
                                                E
                                              iL iRE   iE
                                                            r R
                                                                                        iiL iE i
                                                                                          R      H     R        ER   iE iRFH iH            
                                                                                                                                                    R(
                                                               FH      (                               R(                  rFH  R(
   rFH R(                                                                vr R                       r              r R
        i i          vi     rEHiE  vR      rEHviE iR EER iH  iiE RrFHFH R(( ER   iE vvR FHrEiR v iE rFH i ( E   i virFH RrEH
                                                                                                                                           ( iE  vR
 rFH  RL( E                                vR   R        R            E
                                                                         rFHFH(  R(( rFH
                                                                         R
                                                                         r       R             ri   R
                                                                                                      EH  E   R  r   
                                                                                                                    EH ER   R     E
                                                                                                                                    rFH  R(
                            iH                      ER   iE
                                                                                                 FH     (         FH     (
                    iR
            𝑣#           rFH R(   R                              rFH  R(i rFH R(
     𝑅v2R = ER = 𝑟i)'                           iE  vRß rèEHipiù
                          + (1 + 𝛽( )(𝑅v'i ∥ r𝑟EH*'             E  E
                                                                    grande  E di r
                                                                                    R( à più grande che nell’E. C.
                     E                                                R
            𝑖#         rFH  R(                                             rFH  BE                          

                                                r R
(
           vi rEHiE𝑟*'  vR rEHiE  ER   iE FH (
R( 𝐴2 = −(1 + 𝛽( ) 𝑟*' + 𝑅'
SOLILFDWRUHDFROOHWWRUHFRPXQH               rFH rispetto
                                ß se rCE è grande    R( $PSOLILFDWRUHDFROOHWWR
                                                            a RE à 𝐴2 = −(1 + 𝛽( )
                                $PSOLILFDWRUHDFROOHWWRUHFRPXQH
 HQVLRQH                     Ɣ *XDGDJQRGLWHQVLRQH                                Ɣ *XDGDJQRGLWHQVLRQH
                $PSOLILFDWRUHDFROOHWWRUHFRPXQH
                 (1 + 𝛽 ) 𝑅 ∥ 𝑟
                                        • AV è positivo à amplificatore non invertente
ER   R(  rFH                                                                                v          ER   R(  rFH
                                                              • EA
                                                                 R 
                        (    '   *'     vR                             R(  rFH    R
     𝐴5 =                          A                               V dipende daAYRE
        R𝑟()'
               r+
                  FH (1 + 𝛽( ) 𝑅' ∥ 𝑟*' v
 ƔER *XDGDJQRGLWHQVLRQH           Y
                                                             rEH  ER   R(  rFH             vL     rEH  ER   R(  rFH
                                                       L
                                                              • AV è sempre minore di 1 !!
FRUUHQWH       vR         ER   R( ƔrFH*XDGDJQRGLFRUUHQWH                     Ɣ *XDGDJQRGLFRUUHQWH
      A
$QDOLVLSHUSLFFROLVHJQDOL                       Funzioni di rete C. C.
                                                    La definizione della resistenza di uscita
                                                    dipende dal fatto se considero:
                                                    • RE appartenente all’amplificatore
                                                      (interna al doppio bipolo)
                                                    • RE come resistenza di carico
                                                      all’amplificatore (esterna al doppio
                                                      bipolo)

                                    𝑅3              In ingresso annullare il segnale di
     𝑣)' = 𝑣# − 𝑣& = 𝑟)' 𝑖)                         ingresso à se lo alimento in tensione:
                            vR                      rFH
            iR   iH              ER   iE                          𝑣# = 0
                            R(                  rFH  R(
         𝑣3              −𝑟)' 𝑖)              −𝑟)' 𝑖)               𝑟)'
     𝑅3 = <      =                   =                       =
         𝑖3 8 4( −(1 + 𝛽( )𝑖) + 𝑣3 −(1 + 𝛽rFH     R   −𝑟)' 𝑖) (1 + 𝛽 ) + 𝑟)'
(
          vi ) rEHiE  vR rEHiE 𝑟*'ER   iE ( )𝑖) + 𝑟*'
                                                    (                (   𝑟*'
R(                                                 rFH  R(
     Tipicamente 𝑟)' < 𝑟*'

               𝑟)'                                              
     𝑅3 ≅                   ß molto piccola ordine delle decine di W
            (1 + 𝛽( )
ROOHWWRUHFRPXQH
                        Amplificatore di tensione a C. C.

                              Il collettore comune è un buon amplificatore di tensione?
                              Dobbiamo valutare AV, RI, RO

                                             (1 + 𝛽( ) 𝑅' ∥ 𝑟*'
                                   𝐴5 =                            <1
                                          𝑟)' + (1 + 𝛽( ) 𝑅' ∥ 𝑟*'

                              à non amplifica
                              à 𝑟)' è dell’ordine del kW; 𝛽( può essere un centinaio;
                                basta che 𝑅' sia alcune centinaia di W à 𝐴5 ≅ 1

   𝑅2 = 𝑟)' + (1 + 𝛽( ) 𝑅' ∥ 𝑟*' à può essere elevata !!
HJQDOLODWHQVLRQHGLXVFLWDFRLQFLGH
                                à amplificatore di tensione ideale 𝑅2 = ∞

          𝑟)'
  𝑅3 =               à è dell’ordine
                                   delle decine di W
       (1 + 𝛽( )     à amplificatore di tensione ideale 𝑅3 = 0

  Il collettore comune non guadagna niente (ma può avere guadagno molto vicino a 1)
  però ha RI e RO che permettono un buon interfacciamento con sorgente e carico
  à STADIO SEPARATORE (BUFFER)
                                                         Stadio separatore
   I blocchi (sistemi) a monte e a valle si influenzano
               6WDGLRVHSDUDWRUH               %XIIHUl’uno con l’altro
   es.: due blocchi in cascata descritti con i circuiti equivalenti di Thevenin

                                                    à La tensione trasferita al carico
                                     𝑅6               dipende dal valore relativo di RL e RS
                            𝑣3 =          𝑣
                                   𝑅6 + 𝑅, ,          e può essere molto minore di vs
                                                    à Spesso non possiamo progettare RL
SDUDWRUH %XIIHU                                      e RS per massimizzare il partitore
6LFRQVLGHUDXQJHQHUDWRUHFRQUHVLVWHQ]DLQWHUQDR6 FROOHJDWRDXQD
HVLVWHQ]DGLFDULFRR/
$OGLPLQXLUHGLR/ ODWHQVLRQHvR                      𝑅6           𝑅2
                                               𝑣3 =          𝐴5:;        𝑣      𝐴5:; ≅ 1
  GLYLHQHSLFFRODULVSHWWRDv6                    𝑅6 + 𝑅3       𝑅, + 𝑅2 ,
  qIRUWHPHQWHGLSHQGHQWHGDR/
                                                       𝑅6        𝑅2
6HVLLQWURGXFHXQEXIIHUFRQHOHYDWDLPSHGHQ]DGLLQJUHVVR
                                               𝑣3 ≅          ? RLQ !!𝑣R
 RQUHVLVWHQ]DLQWHUQDR6 FROOHJDWRDXQD          𝑅6 + 𝑅3 𝑅, + 𝑅2 , 6
  ODWHQVLRQHvL DOO¶LQJUHVVRGHOEXIIHUqFLUFDXJXDOHDv6 H
     SUDWLFDPHQWHLQGLSHQGHQWHGDOODUHVLVWHQ]DGLFDULFR
 vR L’inserimento di un buffer intermedio con alta RI e bassa RO permettono di migliorare il
  ,OJHQHUDWRUHqSUDWLFDPHQWHQHOODFRQGL]LRQHGLIXQ]LRQDPHQWRD
     trasferimento di tensione al carico
 v6 YXRWR
GDR à/ inserisco un collettore comune prima e dopo l’emettitore comune per «proteggerlo»
                                                                          
HOHYDWDLPSHGHQ]DGLLQJUHVVRR !! R
                                       Catena di amplificazione
Con degli stadi separatori, l’amplificazione totale del sistema in cascata migliora

                   C.C.                      E.C.                         C.C.




                                                                                 𝑣#@? = 𝑣>"
                                                                                 𝑣#@" = 𝑣>!



            𝑣>?   𝑣>? 𝑣#@? 𝑣#@"           𝑅#@?              𝑅#@"
  𝐴5-&- =       =    ?    ?     = 𝐴? ?            ? 𝐴" ?           ?𝐴
            𝑣#@! 𝑣#@? 𝑣#@" 𝑣#@!        𝑅#@? + 𝑅&"        𝑅#@" + 𝑅&! !
           𝑟)'                                                        Ai guadagno a vuoto
  𝑅&! =           ≪ 𝑅#@" = 𝑟)'        𝐴? = 𝐴! ≅ 1                     dei singoli blocchi
        (1 + 𝛽( )

  𝑅&" = 𝑟*' ∥ 𝑅* ≪ 𝑅#@? = 𝑟)' + (1 + 𝛽( ) 𝑅' ∥ 𝑟*'             𝐴5-&- ≅ 𝐴" = 𝐴5:; '.*.
                             VHJQDOLODWHQVLRQHGLXVFLWDFRLQFLGH
HFRPXQH                     FRQODWHQVLRQHGLR&  Base comune (B. C.)
                                 1. Calcolo del punto di lavoro:
                                                                V((𝐼, 𝑒𝑥𝑝
                                                        V6 t 𝐼* =
                                 • In regione attiva/normale
                                                                               5
                                                                        vV t $" ;
                                                                                5%&
                                                          5$"(                        B5'
                                  𝑉3 = 𝑉** − 𝑅* 𝐼, 𝑒𝑥𝑝           = 𝑉** − 𝑅* 𝐼, 𝑒𝑥𝑝
                                                          5%&                         5%&
                                 • punto di lavoro 𝑄 ≡ (𝐼)( , 𝑉)'( , 𝐼*( , 𝑉*'( )

                                 2. Estrazione del circuito equivalente di piccolo segnale:
                                 • Il BJT viene sostituito dal suo circuito equivalente
                                         $PSOLILFDWRUHDEDVHFRPXQH
                                 • Trascuro  gli effetti reattivi à comportamento quasi-
                                   stazionario
                                 • VCC costante à$QDOLVLSHUSLFFROLVHJQDOL
                                                  vCC = 0 (massa)

   3. Calcolo parametridifferenziali

           𝑉-.   𝑉-. 𝛽+
HFRPXQH
    𝑟)' =
          𝐼)'(
               =
                  𝐼*(
HJQDOL          𝐼*(             𝑉7
         𝑔/ =           𝑟*' =
                𝑉-.             𝐼*(
DOLVLSHUSLFFROLVHJQDOL
                                                               Funzioni di rete B. C.
                                                       Estrazione delle funzioni di rete
                                                       dell’amplificatore a base comune
                                                       à no effetti reattivi à dominio del tempo
                                                       à risoluzione del circuito complessa
                         𝑔! 𝑣"#                        à matrice |Y|
                                                       à 𝑅* in parallelo in uscita; 𝑟)' in parallelo in
                                                         ingresso; 𝑟*' tra ingresso e uscita

        Contributo del generatore: 𝑖# = −𝑔/ 𝑣)' = 𝑔/ 𝑣# ; 𝑖& = 𝑔/ 𝑣)' = −𝑔/ 𝑣#
                            rEH  ER rFH        ER rFH
& R i       iR     iF                 1 iE | 1          1iE  𝛽( + 1    1             1
                             R𝑔& /+rFH + R&  −     rFH             +             −
               𝑦#    𝑦$               𝑟)' 𝑟*'       𝑟*'        𝑟)'     𝑟*'           𝑟*'
           𝑌 = 𝑦     𝑦& =                                  =
                %                          1    1      1          𝛽(   1          1     1
     ER   rFH                   −𝑔 −         E  r
                                                   +   R      −      −               +
&
                    iE            vR / R&𝑟*'
                                           iR 𝑟*'R FH 𝑅*& iE    𝑟)' 𝑟*'         𝑟*' 𝑅*
        R&  rFH                                    R&  rFH
                                        1 𝛽(     1            𝛽(                          Se trascuro
                  𝑦% 𝑦$ 𝛽( + 1    1           +      𝛽( 
                                                        +1                               l’effetto Early
                                       𝑟*' 𝑟)' 𝑟*'            𝑟
        𝑌2 = 𝑦# −      =       +     −             ≅       − )'𝑟
                   𝑦&    𝑟)'     𝑟*'       1   1      𝑟)'   1 + *'                               𝛽( + 1
                                             +                  𝑅*                         𝑌2 ≅
                                          𝑟*' 𝑅*                                                  𝑟)'
DOLVLSHUSLFFROLVHJQDOL
                                                          Funzioni di rete B. C.
                                                                 𝛽( + 1    1              1
                                                                        +               −
                                                                  𝑟)'     𝑟*'            𝑟*'
                                                             𝑌 =
                                                                     𝛽(   1            1    1
                                                                 −      −                +
                                                                    𝑟)' 𝑟*'           𝑟*' 𝑅*
                         𝑔! 𝑣"#
                                                               𝑟)'
                                                         𝑅2 ≅                 (molto bassa !)
                                                              𝛽( + 1


                 𝛽(    1                𝑟)'
            𝑦% 𝑟    +              1 +
                      𝑟*'E r 𝛽(        𝛽( 𝑟r*'    𝛽(
    𝐴5 = − = )' rEH      =      ?     E       ≅     ? 𝑅* ∥ 𝑟*' = 𝑔/ 𝑅* ∥ 𝑟*'
 i
& R      i 𝑦
           R& Fi  1    1
                          R FH
                            𝑟  i   | 1
                                         R FH
                                            1   i 𝑟
                    +R  r )'E        R+  r E )'
                 𝑟*' 𝑅& * FH       𝑟*' & 𝑅* FH
                                                             • AV è positivo
   E  r                                                   à amplificatore non invertente
                                                  ER rFH R&
&      R       FH
                    iE            vR    R&iR              iE           • |AV| uguale al caso E. C.
    R&  rFH                                      R&  rFH
                   𝛽(   1
            𝑦%       −−          𝛽(
                  𝑟)' 𝑟*'
     𝐴2:: =    =            ≅−                            |𝐴2:: | <1
            𝑦# 𝛽( + 1 + 1      𝛽( + 1
                 𝑟)'    𝑟*'
DOLVLSHUSLFFROLVHJQDOL
                                                       Funzioni di rete B. C.


                                                                𝛽( + 1    1           1
                                                                       +           −
                                                                 𝑟)'     𝑟*'         𝑟*'
                                                            𝑌 =
                       𝑔! 𝑣"#
                                                                    𝛽(   1         1    1
                                                                −      −             +
                                                                   𝑟)' 𝑟*'        𝑟*' 𝑅*


                                             𝑅3

                         𝑦  𝑦r$EH  ER rFH        ER rFH
& R i      
           𝑌3 = i𝑦R& −iF
                          %                iE |• Sorgente iE di tensione ideale à 𝑌 = ∞ à 𝑌 = 𝑦
                       𝑦# + 𝑌R  C &  rFH        R&  rFH                          C       3   &



     ER   rFH                               ER rFH R&
                          1 vR  R&iR        
&
                  1 iE                                   iE
        R&                                     & uguale
                                               Rß     rFH al caso E. C.
           𝑅3rFH=    =        = 𝑅* ∥ 𝑟*'
                  𝑦&    1   1
                          +
                       𝑟*' 𝑅*
                                                               
  &RQIURQWRWUDOHFRQILJXUD]LRQLIRQGDPHQWDOL
             Funzioni di rete stadi elementari
              (PHWWLWRUH                 &ROOHWWRUH                   %DVH
               FRPXQH                     FRPXQH                     FRPXQH

                 ER                    ER   R(  rFH            ER
  AY                R&  rFH                                         R&  rFH
                 rEH               rEH  ER   R(  rFH          rEH
                     rFH                           rFH                ER rFH
  AL          ER                       ER                    
                 rFH  R&                      rFH  R(           R&  ER   rFH
                                                                         &  rFH
                                                                   rEH R𝑟#"
  RLQ               rEH            rEH  ER   R(  rFH
                                                                  R& 𝛽$E+R 
                                                                            1  rFH

                                         R6 𝑟#"
                                               rEH           §    ER R6 ·
 RRXW            𝑅!r∥FH 𝑟!"                         rFH    ¨¨  𝑅! ∥¸¸𝑟r!"
                                                                           FH  rEH  R6
                                          ER𝛽$+1            © rEH R6 ¹
• Queste funzioni di rete sono indipendenti dalla frequenza del segnale (costanti)
  perché sono calcolate all’interno della banda passante del BJT !!
• A frequenze maggiori, le funzioni di rete dipendono dalla frequenza del segnale !! 
  &RQIURQWRWUDOHFRQILJXUD]LRQLIRQGDPHQWDOL
                     Funzioni di rete stadi elementari
             (PHWWLWRUH                &ROOHWWRUH                %DVH
              FRPXQH                    FRPXQH                  FRPXQH

            PRGXOR!!                 SRFR                  !!
  AY         QHJDWLYR                   SRVLWLYR                 SRVLWLYR

                !!                  PRGXOR!!           PRGXORSRFR
  AL           SRVLWLYR                QHJDWLYR                QHJDWLYR

                PHGLD                    JUDQGH                  SLFFROD
 RLQ           a :                a :              a :

                PHGLD                    SLFFROD                 JUDQGH
 RRXW        a :              a :              a:

                                   YDORULWLSLFL
P.S.: Il base comune sembra essere particolarmente svantaggiato, ma ha        
funzionamento migliore ad altissime frequenza à banda passante più larga !!
                                       Connessione Darlington
Le funzioni di rete dipendono fortemente dai parametri differenziali dei BJT
à connessione Darlington migliora i parametri e quindi le funzioni di rete !!




                                                     𝑟)'!


                                         𝑣)'
                                                            𝑟)'"
         𝑉)'



          𝑣)' = 𝑣)'! + 𝑣)'" = 𝑟)'! 𝑖)! + 𝑟)'" 𝑖)" = 𝑟)'! 𝑖)! + 𝑟)'" (𝛽(! + 1)𝑖)!

                𝑣)'
           𝑅2 =     = 𝑟)'! + 𝑟)'" (𝛽(! + 1) ≫ 𝑟)'"
                𝑖)!
HWWLWRUHFRPXQH
 HPHWWLWRUH                       Stadio a doppio carico (D. C.)
                                   Le funzioni di rete possono essere migliorate anche
                                   sviluppando la struttura del circuito à doppio carico
                                   1. Calcolo del punto di lavoro:
                                                                               5$"
                                   • In regione attiva/normale 𝐼* = 𝐼, 𝑒𝑥𝑝             ;
                                                                                5%&
                                                           5$"(                      <# =!            5$"(
                                    𝑉3 = 𝑉** − 𝑅* 𝐼, 𝑒𝑥𝑝          ; 𝑉)'( = 𝑉2 − 𝑅'           𝐼, 𝑒𝑥𝑝
                                                           5%&                        <#              5%&
                       $PSOLILFDWRUHDGHPHWWLWRUHFRPXQH
                              • punto di lavoro 𝑄 ≡ (𝐼)( , 𝑉)'( , 𝐼*( , 𝑉*'( )
                         FRQUHVLVWHQ]DGLHPHWWLWRUH
                                      2. Estrazione del circuito equivalente di piccolo segnale:
         Ɣ $SSOLFDQGROD/.9VLRWWLHQH
                                      • Il BJT viene sostituito dal suo circuito equivalente
               R( iH  rFH iR  ERiE  R&iR 
                                      • Trascuro gli effetti reattivi à comportamento statico
         Ɣ 'LUHJRODYDOHO¶DSSURVVLPD]LRQH
 PRGLILFDWRFRQO¶LQVHULPHQWR
  3. Calcolo
            iH parametri
                iE  iR | iR differenziali
         Ɣ 4XLQGL
               𝑉-.    𝑉-. 𝛽+
       𝑟)' =        = rFHER iE       
            i𝐼R)'(      𝐼*(
                   R(  R&  rFH
             𝐼*(                 𝑉7
      𝑔/Ɣ =,QROWUHVLKD 𝑟*' =
            𝑉-.                  𝐼*(
            i i
                                                     Funzioni di rete D. C.
                                                 Estrazione delle funzioni di rete
                                                 dell’amplificatore a doppio carico
              𝑔! 𝑣"#                             à no effetti reattivi à dominio del tempo
                                                 à risoluzione del circuito complessa
                                                 à matrice |Z|
                                                 à Emettitore comune + 𝑅* resistenza di carico
                                                   + 𝑅' in serie al terminale comune

   Per l’emettitore comune: 𝑣)' = 𝑟)' 𝑖) ; 𝑣*' = 𝑟*' 𝑖& − 𝛽( 𝑖) = −𝛽( 𝑟*' 𝑖) + 𝑟*' 𝑖&
                   §        R( rFHER ·
   rEHiE  R( iR ¨¨ rEH                ¸¸ iE
      𝑍 '.*. =
                𝑧    𝑧
                 # © $    R 𝑟 R  rFH0 ¹
                         = ( )' &                     𝑍 D.*. =
                                                                  𝑟)' + 𝑅'          𝑅'
               𝑧%   𝑧&      −𝛽( 𝑟*'   𝑟*'                        −𝛽( 𝑟*' + 𝑅'    𝑟*' + 𝑅'
                                            


              𝑧%     𝛽( 𝑟*' − 𝑅'                             Se trascuro l’effetto Early
HPHWWLWRUHFRPXQH
    𝐴2 = −        =                                                    𝐴2 ≅ 𝛽(
           𝑧& + 𝑅* 𝑟*' + 𝑅' + 𝑅*
DGLHPHWWLWRUH                                           (come nell’emettitore comune)
                                                 Funzioni di rete D. C.
                                                                     𝑧$ 𝑧%
               𝑟)' + 𝑅'           𝑅'                     𝑅2 = 𝑧# −
   𝑍 D.*.   =                                                      𝑧& + 𝑅*
              −𝛽( 𝑟*' + 𝑅'     𝑟*' + 𝑅'

                       𝛽( 𝑟*' − 𝑅' 𝑅'                 𝛽( 𝑟*' 𝑅'
   𝑅2 = 𝑟)' + 𝑅' +                    ≅ 𝑟)' + 𝑅' +
                       𝑟*' + 𝑅' + 𝑅*               𝑟*' + 𝑅' + 𝑅*

   se 𝑟*' ≫ 𝑅' , 𝑅* à        𝑅2 ≅ 𝑟)' + (1 + 𝛽( )𝑅'    (come nel collettore comune; bene!)
                                                      (maggiore che nell’emettitore comune)
         𝑧% 𝑅*      𝑅' −𝛽( 𝑟*' 𝑅*
  𝐴5 =           =
       𝐷E + 𝑧# 𝑅* 𝐷E + 𝑟)' + 𝑅' 𝑅*

                           𝑅# −𝛽) 𝑟$# 𝑅$                              −𝛽)𝑟$# 𝑅$
𝐴( =                                                     ≅
       𝑟"# + 𝑅#   𝑟$# + 𝑅# − 𝑅# −𝛽) 𝑟$# 𝑅# + 𝑟"# + 𝑅# 𝑅$   𝑟"# + 𝑅# 𝑟$# + 𝑅# + 𝑅$ +𝛽) 𝑟$# 𝑅#


                        −𝛽( 𝑅*                                                𝛽( 𝑅*
 𝐴5 ≅                                          se 𝑟*' ≫ 𝑅' , 𝑅* à 𝐴5 ≅ −
                          𝑅    𝑅                                         𝑟)' + 1 +𝛽( 𝑅'
         𝑟)' + 𝑅'     1 + ' + * +𝛽( 𝑅'
                          𝑟*' 𝑟*'

                                                                                      < 1
AV è negativo à amplificatore invertente; minore che nell’E. C.: 𝐴5 ≅ −𝑔/ 𝑅* = − $( *
                                                                                        $"
                                                   Funzioni di rete D. C.
              𝛽( 𝑅*    $PSOLILFDWRUHDGHPHWWLWRUHFRPXQH
  𝐴5 ≅ −                 se progetto l’amplificatore in modo che 1 +𝛽( 𝑅' ≫ 𝑟)'
                         FRQUHVLVWHQ]DGLHPHWWLWRUH
         𝑟)' + 1 +𝛽( 𝑅'
               Ɣ $SSOLFDQGROD/.9VLRWWLHQH𝛽( 𝑅*            𝑅!         INDIPENDENTE DAI
                                       𝐴 ≅−                ≅−
                   R( iH  rFH iR  ERiE 5 R&iR 1 +𝛽( 𝑅'    𝑅"        PARAMETRI DEL BJT !
               Ɣ 'LUHJRODYDOHO¶DSSURVVLPD]LRQH
             𝑟)' +iH 𝑅'iE  iR | i𝑅R '
 𝑍 D.*. =
            −𝛽( 𝑟*' + 𝑅' 𝑟*' + 𝑅'
               Ɣ 4XLQGL
                          rFHERiE
          𝑧$ 𝑧%    iR Sorgente
𝑅3 = 𝑧& −              R(  R& dirFHtensione ideale
           𝑧#         à 𝑍C = 0
               Ɣ ,QROWUHVLKD

                iL iE
                 𝑅' −𝛽( 𝑟*' 𝑅'                    𝛽( 𝑟*' 𝑅'                           𝑅3       𝑅3 ′
𝑅3 = 𝑟*' + 𝑅' −                 ≅  𝑟   +     𝑅  +
                                    FHE R iE
                                R& r*'                                §         R( rFHER ·
                                              '
                   𝑟   +  𝑅
                vȠ  R&iR                        𝑟)' + 𝑅'
                    )'     '                        vL rEHiE  R( iR ¨¨ rEH                ¸¸ iE
                               R(  R&  rFH                          ©       R(  R&  rFH ¹
Maggiore che nell’emettitore comune à male! à Buffer in uscita !
                                                                                                
 𝑅3 ′ = 𝑅3 ∥ 𝑅* ≅ 𝑅*         à dipende dal carico; 𝑅* non troppo bassa altrimenti AV cala
HWWLWRUHFRPXQH
                               
 HPHWWLWRUH           Caratteristiche del doppio carico
WWLWRUHFRPXQH                • Migliora la resistenza di ingresso
HPHWWLWRUH                   • Amplificatore invertente con uscita sul collettore del BJT
                              • Il guadagno cala ma può essere indipendente dal BJT
                              • Resistenza di uscita e guadagno di tensione molto
                                dipendenti dal carico

HPHWWLWRUHFRPXQH             à possibilità di un secondo terminale di uscita
DGLHPHWWLWRUH                 sull’emettitore del BJT à 𝑉3 ′
                              • La maglia di ingresso non cambia (stessa 𝑅2 )
            𝑉* ′
                              Hp. semplificativa: trascuro l’effetto Early à 𝑟*' = ∞
                                                                                       𝑣#
 PRGLILFDWRFRQO¶LQVHULPHQWR             𝑣39 = 𝑅' 𝑖' = 𝑅' 1 +𝛽( 𝑖) = 𝑅' 1 +𝛽(
                                                                                       𝑅2
 
                                                     1 +𝛽( 𝑅'
                                            𝐴5 =                   <1
PRGLILFDWRFRQO¶LQVHULPHQWR                   𝑟)' + (1 + 𝛽( )𝑅'
                             

                                           come il collettore comune !
                       𝑣* ′
                                    Ricordiamo che la RESISTENZA SULL’EMETTITORE
                               
                                    AUMENTA LA STABILITA’ DEL PUNTO DI LAVORO !!
                 Impatto del carico sull’amplificatore
                                Es.: amplificatore ad emettitore comune
                                à può raggiungere valori elevati di 𝐴5:;

                                          𝐴5:; = −𝑔/ 𝑅* ∥ 𝑟*'

                         se aumento 𝑅* è vero che 𝐴5:; aumenta sempre ??
                         Fino ad un certo punto !!
                         1. 𝐴5:; dipende da 𝑅* ∥ 𝑟*' à domina la più piccola !!
                         teoricamente il guadagno massimo è −𝑔/ 𝑟*'
                         2. 𝑅* ha impatto su 𝑔/ perché definisce il punto di lavoro !!
                                                                 𝐼*(
                                𝑉*'( = 𝑉** − 𝑅* 𝐼*(         𝑔/ =
                                                                 𝑉-.

Se RC aumenta troppo, IC deve calare, altrimenti vado in saturazione à gm cala !!
à AV cala !!
• Punto di lavoro e parametri differenziali sono legati tra loro
• Il carico impatta sia il punto di lavoro che le funzioni di rete à TRADE OFF !!
                                                                  Carico attivo
E’ possibile svincolare la definizione del punto di lavoro dalle funzioni di rete?
à devo usare un CARICO ATTIVO
                            à componente che ha un comportamento diverso a livello
                              statico e a livello di piccolo segnale
                            es.: generatore di corrente:
                            • Impone una corrente costante à definisce IC0
                            • A livello di piccolo segnale diventa iC = 0 à lato aperto
                            • Come se fosse 𝑅* = ∞



• Come lo realizzo ? à SPECCHIO DI CORRENTE
• Funziona bene se Q1 è in regione normale
à VCC - Vout > VEC,sat                                                       IC0
• Copia la corrente del ramo di sinistra sul ramo di
  destra à impone la corrente di collettore IC0 nel
  punto di lavoro
             Ɣ 1HOFLUFXLWRHTXLYDOHQWHSHUSLFFROLVHJQDOLODWHQVLRQHGLXVFLWDF
               FRQODWHQVLRQHGLR&
                          Guadagno di tensione massimo
                               Estrazione del circuito equivalente di piccolo segnale:
                               • Trascuro gli effetti reattivi à comportamento statico

                       𝑅3F:    • Il BJT viene sostituito dal suo circuito equivalente
                      $PSOLILFDWRUHDGHPHWWLWRUHFRPXQH
                               • Lo specchio di corrente lo posso descrivere con le sue
        IREF                     funzioni di rete:
                IC0
                               à IREF costante à iREF = 0
                                       $QDOLVLSHUSLFFROLVHJQDOL
                                                5
                               à 𝑅3F: = 𝑟*'! = 2 +
                                                *(




                                                                                    𝑟*'!
       𝑉-.   𝑉-. 𝛽+
𝑟)' =      =
      𝐼)'(    𝐼*(
       𝐼*(
𝑔/ =                                                           𝑟*'   𝐼*( 𝑉7         𝑉7
       𝑉-.                    𝐴5:; = −𝑔/ 𝑟*' ∥ 𝑟*'! = −𝑔/          =− r ?       =−
                                                                2    𝑉-.FH 2𝐼*(    2𝑉-.
      𝑉7                         iL   iE             iR   ic    ERiE
𝑟*' =
      𝐼*(
          = 𝑟*'!                                       FH ! &          r R
                         INDIPENDENTE DAL PUNTO DI LAVORO   𝐴5:; ≅ −500
                                                    Impatto dei carichi a valle
PDVVD
HPDVVD
                                               Finora abbiamo studiato gli amplificatori elementari
HQWHSHUSLFFROLVHJQDOLODWHQVLRQHGLXVFLWDFRLQFLGH
                                               nel loro funzionamento a vuoto
&
                                                  Cosa succede se collego qualcosa a valle ?
                                                         

                                                     Il collegamento di 𝑅6 ha un duplice impatto,
                                             𝑅6      perché modifica:
DWRUHDGHPHWWLWRUHFRPXQH                           1. Il PUNTO DI LAVORO: sul nodo in uscita ho
                                                        una corrente in più che circola su RL.
$QDOLVLSHUSLFFROLVHJQDOL                             Cambiano quindi anche i parametri
                                                        differenziali
                                                     2. Il GUADAGNO DI TENSIONE/CORRENTE:
                                                        RL deve essere inclusa nelle formule
                                                    𝑅6        es.: 𝐴5 = −𝑔/ (𝑟*' ∥ 𝑅* ∥ 𝑅6 )



                           r
        • Anche
             iR se
                ic possiamo
                   ERiE    FH
                                includere nelle funzioni di rete il nuovo componente non
                        FH  R& valori dei parametri differenziali
          conosciamo i rnuovi
        • Ricalcolare          r R
                      il punto di lavoro per ogni possibile carico a valle è troppo complicato !!
rEHiE        v  R i E i FH &
               R     & R    R E
                                  rFH  R&
                   Condensatori di disaccoppiamento

                                     Per evitare di modificare il punto di lavoro ogni
                                     volta che inseriamo un carico a valle si utilizzano i
                                     condensatori di disaccoppiamento
                                     à il condensatore evita che in condizioni
                                       statiche il punto di lavoro sia influenzato
                            𝐶          dalla presenza del carico RL
                                     à La tensione di uscita viene definita su 𝑅6
                           𝑅6   𝑉3
                                     à il condensatore introduce uno zero nell’origine
                                       in 𝐴5 (𝑠) = 𝑉3 /𝑉)' à 𝑉3 = 0 a livello statico
                                     à Se la frequenza del segnale è abbastanza
                                                                                    !
                                       elevata, l’impedenza del condensatore (𝑍* = F* )
                                       risulta trascurabile rispetto al carico 𝑅6

I condensatori di disaccoppiamento hanno tipicamente valori di capacità molto
alta in modo che la loro impedenza sia trascurabile già a bassissime frequenze

Equivale a dire che la frequenza di taglio inferiore di AV(s) è molto bassa
PDVVD
                            Condensatori di disaccoppiamento
HPDVVD
                                              L’amplificatore ha una banda passante limitata dal
QWHSHUSLFFROLVHJQDOLODWHQVLRQHGLXVFLWDFRLQFLGH
                                        condensatore C a bassa frequenza e dalle capacità
                                        del BJT ad alta frequenza à PASSA-BANDA
                                                
                                   𝐶
                                                     |AV|
                       𝑅6 𝑉
 WRUHDGHPHWWLWRUHFRPXQH 3                                        banda
                                                                   passante
$QDOLVLSHUSLFFROLVHJQDOL
                                                                                        log 𝜔
                                                     Lavoro a centro banda (in banda passante)
                                                     dove l’amplificazione è massima:
                                           𝑅6        à C è un corto circuito; le capacità del
                                                       BJT sono un circuito aperto

   Il circuito equivalente
                         rFH quindi non presenta capacità e posso comunque trattarlo
          iR ic E
   nel dominio    R iE tempo
                 del   r R
                       FH    &
     Inserisco le capacità solo per valutare le pulsazioni di taglio inferiore e superiore (𝜔6 ,
                                    rFH R&
  i  𝜔  G ) che
              vR   R i
                     & R  E
                 definiscono  i
                             R Ela  banda passante (dove valgono le funzioni di rete calcolate con
 H E
                                  rFH  R&
     il circuito equivalente senza capacità)
DORULGHLFRQGHQVDWRULCC HC VRQRVFHOWLLQPRGRFKHODORUR
SHGHQ]DDOOHIUHTXHQ]HGHOVHJQDOHGLLQJUHVVRVLDWUDVFXUDELOH
                           Condensatori di disaccoppiamento
JOLDPSOLILFDWRULDHPHWWLWRUHHEDVHFRPXQHLOWHUPLQDOHFRPXQHq
   &RQILJXUD]LRQLIRQGDPHQWDOL
OHJDWRDPDVVDPHGLDQWHXQFRQGHQVDWRUHFKHDOOHIUHTXHQ]DGHO
   La sorgente di segnale fa parte della maglia di ingresso(à se cambia la sorgente,
JQDOHDJLVFHFRPHXQFRUWRFLUFXLWRLQSDUDOOHORULVSHWWLYDPHQWHDR
 Rcambia
    %       il punto di lavoro à condensatore di disaccoppiamento !
OO¶DPSOLILFDWRUHDFROOHWWRUHFRPXQHYLHQHHOLPLQDWDODUHVLVWHQ]DR&
SUHVHQ]DGHLFRQGHQVDWRULOLPLWDLQIHULRUPHQWHODEDQGDSDVVDQWH
    (PHWWLWRUH                                         C1 e C2: condensatori di disaccoppiamento
     FRPXQH
JOLDPSOLILFDWRUL
                                                         che impediscono a sorgente e carico di
EDQGDSDVVDQWHLQROWUHqOLPLWDWDVXSHULRUPHQWHGDJOLHIIHWWLUHDWWLYL
                                                         spostare il punto di lavoro
WUDQVLVWRU TXLQGLFRPSOHVVLYDPHQWHJOLDPSOLILFDWRULKDQQRXQ
PSRUWDPHQWRGLWLSRSDVVDEDQGD                          à il punto di lavoro è definito da R1, R2,
                                                             RC e RE (stadio a doppio carico à più
                                                             stabilitàdel punto di lavoro;
                                                             polarizzazione a 4 resistenze)
                                   C3 è detta capacità di by-pass: ad alta
   $PSOLILFDWRUHDGHPHWWLWRUHFRPXQH       %DVH  frequenza cortocircuita la resistenza RE
                                                          FRPXQH
         &LUFXLWRHTXLYDOHQWHSHUSLFFROLVHJQDOL à trasforma il doppio carico in emettitore
                                                     comune à aumenta il guadagno !!

                                                                        Per il circuito equivalente di
                                                                        piccolo segnale trascuro tutte
                                                                        le capacità (centro banda)
                                                                        à C di disaccoppiamento e by-
                                                                                
         𝑅) = 𝑅! ∥ 𝑅"                                                   pass come dei corto circuiti
    $PSOLILFDWRUHDGHPHWWLWRUHFRPXQH
                              Funzioni          di
          &LUFXLWRHTXLYDOHQWHSHUSLFFROLVHJQDOL
                                                   rete stadi elementari

                                                                         Per il calcolo di AV ho due strade:
                                                                         1. Soluzione del circuito
                                                                         2. Sfrutto le funzioni di rete degli
                                                                            stadi elementari già studiate
                                                                                   𝐴5:; = −𝑔/ 𝑅* ∥ 𝑟*'
OFLUFXLWRHTXLYDOHQWHSHUSLFFROLVHJQDOLO HPHWWLWRUHSXzHVVHUH
             𝑣&             𝑅6                                 𝑅6
     𝐴5! =      = 𝐴5:;              = −𝑔/ 𝑅TXLQGLQRQFRPSDUH
QVLGHUDWRSUDWLFDPHQWHFROOHJDWRDPDVVD      *  ∥ 𝑟*'
                                                                    R(               𝑅2 = 𝑟)'
             𝑣#          𝑅6 + 𝑅3                          𝑅6 + 𝑅* ∥ 𝑟*'
 LQGLFDQRFRQAcYAcLRcLQRcRXW LJXDGDJQLHOHUHVLVWHQ]HGLLQJUHVVR
GLXVFLWDGHOO¶DPSOLILFDWRUHFRPSOHWRHFRQAYALRLQRRXWLJXDGDJQL           𝑅3 = 𝑅* ∥ 𝑟*'
     𝐴5! = −𝑔/ 𝑅* ∥ 𝑟*' ∥ 𝑅6
HUHVLVWHQ]HGLLQJUHVVRHGLXVFLWDGHOO¶DPSOLILFDWRUHHOHPHQWDUH
 FFKLXVRGDOODOLQHDWUDWWHJJLDWD

             𝑣#   𝑅) ∥ 𝑟)'                                                
     𝐴5" =      =
             𝑣F 𝑅, + 𝑅) ∥ 𝑟)'


                  𝑣& 𝑣& 𝑣#                                  𝑅) ∥ 𝑟)'
     𝐴5-&- =        = ? = 𝐴5! ? 𝐴5" = −𝑔/ 𝑅* ∥ 𝑟*' ∥ 𝑅6 ?
                  𝑣F 𝑣# 𝑣F                                𝑅, + 𝑅) ∥ 𝑟)'
                                 Source comune (S. C.)
                • E’ possibile realizzare amplificatori anche con i MOSFET
                es.: Amplificatore a source comune
                • Caratteristica statica simile a quella dell’emettitore comune
                • Alta pendenza con il MOSFET in regione di saturazione
                1. Calcolo del punto di lavoro:
                                                       𝛽@
                  𝑉3HI = 𝑉DD − 𝑅D 𝐼D,( = 𝑉DD − 𝑅D         (𝑉2J −𝑉I )" > 𝑉2J − 𝑉I
                                                       2
                • punto di lavoro 𝑄 ≡ (𝑉C,( , 𝐼D,( , 𝑉D,( )
                2. Estrazione del circuito equivalente di piccolo segnale:
                • Il MOSFET è sostituito dal suo circuito equivalente
    Vout        • Trascuro gli effetti reattivi (lo studio nella banda passante
     Vdd          dell’amplificatore) à comportamento quasi-stazionario



                                                  𝑔$%


Vin−Vt

           Vt   Vin
                                                             Funzioni di rete S. C.
                                                     3. Calcolo parametri differenziali
                                                                                                 K2
                                                                                                ,-(
                                                     𝑔/ = 𝛽@ (𝑉C,( −𝑉I )(1 + 𝜆𝑉D,( ); 𝑔D, = (!=K5   ) ,-(
𝑣+                     𝑔$%
                                                     4. Estrazione delle funzioni di rete
                                                     dell’amplificatore a source comune
                                                     à no effetti reattivi à dominio del tempo
                                          𝑅3
          8
     𝑅2 = ' = ∞ à ideale come amplificatore di tensione
          #'
                                                                              con 𝑟D, = 1/𝑔D,
          𝑣3 𝑣D, − 𝑅D ∥ 𝑟D, 𝑔/ 𝑣C,                                            • AV è negativo
 𝐴5 =        =     =               = −𝑔/ 𝑅D ∥ 𝑟D,
          𝑣2   𝑣C,     𝑣C,                                                    à amplificatore invertente
          à formula identica al caso dell’ E.C.                               (sfasa di 180∘ il segnale)
                                                                              • AV dipende da RD
          𝑣3        𝑣D,                        𝑣D,             1              1
 𝑅3 =        <    =     <            =            𝑣     =               =            = 𝑟D, ∥ 𝑅D (come E.C.)
          𝑖3 , 4(    𝑖3 8                𝑔D, 𝑣D, + D,              1         1   1
               '             .- 4(                 𝑅D       𝑔D, + 𝑅            +
                                                                            𝑟D, 𝑅D
                                                                    D

     Il S. C. ha prestazioni simili all’E. C., ma migliora RI (attenzione che gm è minore)
                                               Drain comune (D. C.)
                             1. Calcolo del punto di lavoro:
                                                                    </
                             • In regione di saturazione 𝐼D, =           (𝑉C, −𝑉I )" ;
                                                                    "
                                                  <
                             𝑉3HI = 𝑅, 𝐼D,( = 𝑅, / (𝑉C,( −𝑉I )" ;        𝑉C,( = 𝑉2J − 𝑉3HI
                                                   "
                             • punto di lavoro 𝑄 ≡ (𝑉C,( , 𝐼D,( , 𝑉D,( )

                             2. Estrazione del circuito equivalente di piccolo segnale:
                             • Il MOSFET viene sostituito dal suo circuito equivalente
                             • Trascuro gli effetti reattivi à comportamento quasi-
                               stazionario
                             • VDD costante à vDD = 0 (massa)


3. Calcolo parametri differenziali
𝑔/ = 𝛽@ (𝑉C,( −𝑉I )(1 + 𝜆𝑉D,( )                                             𝑔&" 𝑣%"
                                                                                         𝑔$%
          K2,-(
𝑔D, =
        (!=K5,-()
𝑔/) = −𝑔/ ? 𝛼
                                                     Funzioni di rete D. C.
                                                     𝑖-.
                                                              4. Estrazione delle funzioni di rete
                                               𝑔$%            dell’amplificatore a drain comune
                                    𝑔&" 𝑣%"
                                                              à no effetti reattivi à dominio del
                                                                tempo
                                                                             𝑣C, = 𝑣#@ − 𝑣&>-
                                                                                𝑣,) = 𝑣&>- = −𝑣D,
       8
  𝑅2 = # )/ = ∞ à ideale come amplificatore di tensione
        )/


𝑣&>- = 𝑅, 𝑖D, = 𝑅, 𝑔/ 𝑣C, + 𝑔/) 𝑣,) + 𝑔D, 𝑣0F = 𝑅, 𝑔/ 𝑣#@ − 𝑔/ 𝑣&>- − 𝑔/ 𝛼𝑣&>- − 𝑔D, 𝑣&>-

                       𝑅, 𝑔/                            𝑣&>-             𝑅, 𝑔/
   𝑣&>- =                              𝑣         𝐴5 =        =                            <1
             1 + 𝑅, [𝑔/ (1 + 𝛼) + 𝑔D, ] #@              𝑣#@    1 + 𝑅, [𝑔/ (1 + 𝛼) + 𝑔D, ]


 Se trascuriamo l’effetto body 𝛼 ≅ 0
                                          𝑅
                  𝑅, 𝑔/            𝑔/ 1 + 𝑅, 𝑔               𝑔/ (𝑅, ∥ 𝑟D, )
   𝐴5 ≅                      =                , D,
                                                      =                           à formula identica
           1 + 𝑅, 𝑔/ + 𝑅, 𝑔D, 1 + 𝑔       𝑅,               1 + 𝑔/ (𝑅, ∥ 𝑟D, )     al caso dell’ C.C.
                                       /1+𝑅 𝑔
                                           , D,
                                                     Funzioni di rete D. C.
                                                     𝑖-.
                                                            4. Estrazione delle funzioni di rete
                                               𝑔$%          dell’amplificatore a source comune
                                     𝑔&" 𝑣%"
                                                            à no effetti reattivi à dominio del
                                                              tempo
                             𝑖*                                            𝑣C, = 𝑣#@ − 𝑣&>-
                                                                          𝑣,) = 𝑣&>- = −𝑣D,
    𝑣2                𝑅3
𝑅2 = = ∞
    𝑖2
         𝑔/ 𝑅, ∥ 𝑟D,                                 𝑖D, = 𝑔/ 𝑣#@ − 𝑔/ 𝑣&>- − 𝑔/ 𝛼𝑣&>- − 𝑔D, 𝑣&>-
𝐴5 ≅                   <1
       1 + 𝑔/ 𝑅, ∥ 𝑟D,
       𝑣&>-        𝑣&>-                    𝑣&>-
𝑅3 =        <    =         =
        𝑖3 8 4( −𝑖D, + 𝑣&>- 𝑔/ 𝑣&>- + 𝑔/ 𝛼𝑣&>- + 𝑔D, 𝑣&>- + 𝑣&>-
              )/        𝑅,                                   𝑅,
                1                          1        1
𝑅3 =                             ≅               ≅       (bassa; bene!)
                            1              1   1   𝑔/
       𝑔/ (1 + 𝛼) + 𝑔D, +            𝑔/ +    +
                            𝑅,            𝑟D, 𝑅,      (solitamente 𝑔/ ≫ 𝑔D, )

Il D. C. ha prestazioni simili al C. C., ma migliora RI (attenzione che gm è minore)
                                                Gate comune (G. C.)
                             1. Calcolo del punto di lavoro:
                                                                     </
                             • In regione di saturazione 𝐼D, =            (𝑉C, −𝑉I )" ;
                                                                      "
                                                                 <
  𝑉C                         𝑉3HI = 𝑉DD − 𝑅D 𝐼D,( = 𝑉DD − 𝑅D / (𝑉C − 𝑉2J − 𝑉I )" ;
                                                                  "
cost.                        • punto di lavoro 𝑄 ≡ (𝑉C,( , 𝐼D,( , 𝑉D,( )

                             2. Estrazione del circuito equivalente di piccolo segnale:
                             • Il MOSFET viene sostituito dal suo circuito equivalente
                             • Trascuro gli effetti reattivi à comportamento quasi-
                               stazionario
                             • VDD costante à vDD = 0 (massa)


3. Calcolo parametri differenziali
 𝑔/ = 𝛽@ (𝑉C,( −𝑉I )(1 + 𝜆𝑉D,( )                                            𝑔&" 𝑣%"   𝑔$%

           K2,-(
 𝑔D, =
         (!=K5,-()
 𝑔/) = −𝑔/ ? 𝛼
                                                Funzioni di rete G. C.
                                                      4. Estrazione delle funzioni di rete
                               𝑔&" 𝑣%"    𝑔$%
                                                      dell’amplificatore a source comune
                                                      à no effetti reattivi à dominio del
                                                        tempo

                                                           𝑣C, = −𝑣#@       𝑣,) = 𝑣#@
                                                                 𝑣D, = 𝑣&>- − 𝑣#@

𝑣/01 = −𝑅- 𝑖-. = −𝑅- 𝑔! 𝑣2. + 𝑔!" 𝑣." + 𝑔-. 𝑣-. = 𝑅- 𝑔! + 𝛼𝑔! + 𝑔-. 𝑣+3 − 𝑅- 𝑔-. 𝑣/01

       𝑅D 𝑔/ + 𝛼𝑔/ + 𝑔D,                                  𝑣&>-    𝑔/ + 𝛼𝑔/ + 𝑔D,
𝑣&>- =                   𝑣#@             𝑖D, = −𝑖#@ = −        =−                𝑣#@
           1 + 𝑅D 𝑔D,                                      𝑅D       1 + 𝑅D 𝑔D,


      𝑣#@   1 + 𝑅D 𝑔D,
 𝑅2 =     =
      𝑖#@ 𝑔/ + 𝛼𝑔/ + 𝑔D,
                                                (solitamente 𝑔/ ≫ 𝑔D, )

                                              1 + 𝑅D 𝑔D, 1 + 𝑅D 𝑔D,    1      (bassa; male!)
Se trascuriamo l’effetto body 𝛼 ≅ 0      𝑅2 ≅           ≅           ≅           come base
                                              𝑔/ + 𝑔D,      𝑔/        𝑔/         comune
                                           Funzioni di rete G. C.

                                              𝑖*
                                                   4. Estrazione delle funzioni di rete
                           𝑔&" 𝑣%"   𝑔$%
                                                   dell’amplificatore a source comune
                                                   à no effetti reattivi à dominio del
                                                     tempo

                                                      𝑣C, = −𝑣#@        𝑣,) = 𝑣#@

       𝑅D 𝑔/ + 𝛼𝑔/ + 𝑔D,                                    𝑣D, = 𝑣&>- − 𝑣#@
𝑣&>- =                   𝑣#@
           1 + 𝑅D 𝑔D,
                                           Se trascuriamo l’effetto body 𝛼 ≅ 0
       𝑣&>- 𝑅D 𝑔/ + 𝛼𝑔/ + 𝑔D,
𝐴5 =       =                              𝑅D 𝑔/ + 𝑔D,     𝑔/ 𝑅D
       𝑣#@      1 + 𝑅D 𝑔D,           𝐴5 ≅             ≅            = 𝑔/ 𝑅D ∥ 𝑟D,
                                           1 + 𝑅D 𝑔D,   1 + 𝑅D 𝑔D,
                                       (solitamente 𝑔/ ≫ 𝑔D, )          non invertente !
                                                                      come base comune

     𝑣&>-        𝑣&>-         𝑣&>-            1
𝑅3 =      <    =        =                =        = 𝑅D ∥ 𝑟D,
      𝑖3 8 4( 𝑖D, + 𝑣&>- 𝑔D, 𝑣&>- + 𝑣&>-    1
                                              +
                                                1
            )/       𝑅D              𝑅D    𝑟D, 𝑅D             (come base comune)
