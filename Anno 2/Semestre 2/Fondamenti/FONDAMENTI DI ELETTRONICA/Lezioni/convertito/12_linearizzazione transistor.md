---
fonte: "12_linearizzazione transistor.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Linearizzazione dei transistor

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                               Transistor BJT e MOSFET
I transistor BJT e MOSFET sono componenti non lineari con effetti reattivi
à per l’analisi dinamica è necessario passare ai piccoli segnali e alle
trasformate di Laplace

à LINEARIZZAZIONE DEL COMPONENTE
•   BJT è un tripolo à doppio bipolo
•   MOSFET ha 4 terminali, ma il bulk è polarizzato con tensione fissa
à 3 terminali sui quali agisco à tripolo (doppio bipolo)
Descritti da matrici e circuiti equivalenti !!
                                       Transistore bipolare npn
Al grande segnale, il BJT è descritto dal modello di Ebers-Moll a 3 parametri:
1.   IS corrente inversa del BJT
                                                      𝐼!
2.   bF (10 ÷ 300)
3.   bR (1 ÷ 3)

𝐼! = 1 + 𝛽" 𝐼#! − 𝛽$ 𝐼#% = 𝐼& + 𝐼#!

 𝐼% = 𝛽" 𝐼#! − 1 + 𝛽$ 𝐼#% = 𝐼& − 𝐼#%

𝐼& = 𝛽" 𝐼#! − 𝛽$ 𝐼#%

               𝑉#$       𝑉#&
 𝐼! = 𝐼" 𝑒𝑥𝑝       − 𝑒𝑥𝑝
               𝑉!%       𝑉!%
                    Linearizzazione del modello di E-M
 Linearizzare il BJT significa linearizzare il suo modello matematico che viene
 rappresentato da un circuito equivalente con 3 componenti:
 •   due diodi
                                                già studiati !
 •   un generatore comandato
                                 𝜕𝐼'                       𝜕𝐼'     𝐼') + 𝐼*    1
 Per il diodo à           𝑖' =       ( 𝑣            𝑔' =       ( =          =
                                 𝜕𝑉' ( '                   𝜕𝑉' (     𝑉&+      𝑟'



                                      𝜕𝑄'        𝜕𝐼'                                       1
                                 𝐶' =     ( = 𝜏,     ( = 𝜏 , 𝑔'              𝐶- = 𝐶-)
                                      𝜕𝑉' (      𝜕𝑉' (                                      𝑉
                                                                                        1 − Φ')
                                                                                               -



Punto di lavoro Q: VBE0, VCB0, IB0, IC0

                              .!"
Giunzione BE à 𝑟#! =                   ;   𝐶#! = 𝐶' + 𝐶- (in diretta 𝐶!" ≅ 𝐶# ; in inversa 𝐶!" ≅ 𝐶$ )
                          /#$%0/#$,'

                             .!"
Giunzione BC à 𝑟#% = /                ;    𝐶#% = 𝐶' + 𝐶- (in diretta 𝐶!% ≅ 𝐶# ; in inversa 𝐶!% ≅ 𝐶$ )
                           #(% 0/#(,'
                         Linearizzazione del generatore
                                           𝑉%#
𝐼& = 𝛽" 𝐼#! 𝑉#! − 𝛽$ 𝐼#% 𝑉#% = 𝛽") 1 +         𝐼 𝑉   − 𝛽$ 𝐼#% 𝑉#%
                                            𝑉1 #! #!
Ci interessa la configurazione ad emettitore comune: ingresso sulla base, uscita sul
collettore, emettitore terminale comune à tensione di uscita VCE

      𝜕𝐼&       𝜕𝐼&
𝑖& =      ( 𝑣 +     ( 𝑣 = 𝑎 𝑣#! + 𝑏 𝑣#% = 𝑎 𝑣#! + 𝑏 𝑣#! + 𝑣!%
     𝜕𝑉#! ( #! 𝜕𝑉#% ( #%

𝑖& = 𝑎 𝑣#! + 𝑏 𝑣#! − 𝑏 𝑣%! = 𝑎 + 𝑏 𝑣#! − 𝑏 𝑣%!

       𝜕𝐼&        𝜕𝐼#!        𝜕𝐼#%        𝜕𝐼#!         1
 𝑎=        ( = 𝛽"      ( − 𝛽$      ( = 𝛽"      ( = 𝛽"
      𝜕𝑉#! (      𝜕𝑉#! (      𝜕𝑉#! (      𝜕𝑉#! (      𝑟#!

       𝜕𝐼&     𝜕𝛽"             𝜕𝐼#%          𝐼#!)       1
 𝑏=        ( =     ( 𝐼#!) − 𝛽$      ( = −𝛽")      − 𝛽$
      𝜕𝑉#% ( 𝜕𝑉#% (            𝜕𝑉#% (         𝑉1       𝑟#%

 𝑔2 ≜ 𝑎 + 𝑏        trans-conduttanza
                                                           3
 𝑔%! ≜ −𝑏          conduttanza di uscita          𝑟%! =         resistenza di uscita
                                                          4($
                             Circuito di Giacoletto-Johnson
                               .!"
Giunzione BE à 𝑟#! =                     ;   𝐶#! = 𝐶' + 𝐶- (in diretta 𝐶!" ≅ 𝐶# ; in inversa 𝐶!" ≅ 𝐶$ )
                            /#$%0/#$,'

                               .!"
Giunzione BC à 𝑟#% =                     ;   𝐶#% = 𝐶' + 𝐶- (in diretta 𝐶!% ≅ 𝐶# ; in inversa 𝐶!% ≅ 𝐶$ )
                            /#(%0/#(,'

                                        1        𝐼#!)       1                           𝐼#!)       1
𝑖& = 𝑔2 𝑣#! + 𝑔%! 𝑣%!          𝑔2 ≜ 𝛽"     − 𝛽")      − 𝛽$                  𝑔%! ≜ 𝛽")        + 𝛽$
                                       𝑟#!        𝑉1       𝑟#%                           𝑉1       𝑟#%

𝑟#! , 𝐶#! , 𝑟#% , 𝐶#% , 𝑔2 , 𝑔%! sono i parametri differenziali del BJT definiti nel punto di lavoro

                                                                 𝑟#%

                                             B                                                 C



                                                              𝐶#%                                    𝑣%!
                                  𝑣#!                                              𝑔2 𝑣#!      𝑟%!
                                                 𝑟#!    𝐶#!
                       𝐼&

                                                                  E
                                     CIRCUITO EQUIVALENTE (ai piccoli segnali) DEL BJT
                                               DI GIACOLETTO-JOHNSON
                                          Matrice ammettenza del BJT
                              𝑟#%

        B                                                          C           Il circuito di Giacoletto-
                                                                               Johnson è un circuito a p
                                                                               à posso ottenere
                            𝐶#%                                          𝑣%!   immediatamente la
𝑣#!                                                     𝑔2 𝑣#!     𝑟%!
              𝑟#!     𝐶#!                                                      matrice ammettenza
                                                                               del circuito equivalente

                              E
                                                                 • 𝑌3 è in parallelo alla porta 1
      𝑦5            𝑦6   𝑌3 + 𝑌9            −𝑌9                  • 𝑌: è in parallelo alla porta 2
  𝑌 = 𝑦             𝑦8 =
       7                 𝑔2 − 𝑌9          𝑌: + 𝑌9                • 𝑌9 è tra la porta 1 e la porta 2

         3                        3                 3
 𝑌3 =         + 𝑠𝐶#! ; 𝑌: =           ;    𝑌9 =         + 𝑠𝐶#%
        6#$                   6($                 6#(

                                    1            1                                  1
                                       + 𝑠𝐶%& +     + 𝑠𝐶%'                       −     − 𝑠𝐶%'
                        𝑦!    𝑦"   𝑟%&          𝑟%'                                𝑟%'
                    𝑌 = 𝑦     𝑦$ =
                         #                   1                                  1     1
                                       𝑔( −     − 𝑠𝐶%'                             +    + 𝑠𝐶%'
                                            𝑟%'                                𝑟'& 𝑟%'
                            Funzionamento in regione normale

        B                                                 C
                                                                       Il BJT è utile per
                                                                       realizzare amplificatori se
                             𝐶#%                                       lavora in regione normale
                                                               𝑣%!
𝑣#!                                            𝑔2 𝑣#!    𝑟%!
            𝑟#!       𝐶#!                                              à giunzione BC spenta
                                                                              𝒓𝑩𝑪 → ∞
                               E

                              1
                                 + 𝑠𝐶%& + 𝑠𝐶%'          −𝑠𝐶%'          giunzione BE in diretta
          𝑦!          𝑦"     𝑟%&
      𝑌 = 𝑦           𝑦$ =                                                    𝐼#!) ≫ 𝐼#!,*
           #                                          1
                                   𝑔( − 𝑠𝐶%'             + 𝑠𝐶%'             inoltre 𝑉1 ≫ 𝑉&+
                                                     𝑟'&

                   1        𝐼#!)       1        1        𝐼#!)      𝐼#!) + 𝐼#!,*       𝐼#!)
      𝑔2 ≜ 𝛽"         − 𝛽")      − 𝛽$     ≅ 𝛽"     − 𝛽")      = 𝛽"              − 𝛽")
                  𝑟#!        𝑉1       𝑟#%      𝑟#!        𝑉1           𝑉&+             𝑉1

              𝐼#!)       𝐼#!)      𝐼#!)   𝛽"                                    𝛽) à guadagno
      𝑔2 ≅ 𝛽"      − 𝛽")      ≅ 𝛽"      ≅               𝑔2 𝑟#! = 𝛽) ≅ 𝛽"        di corrente di
               𝑉&+        𝑉1        𝑉&+   𝑟#!
                                                                                piccolo segnale
                                    Regime quasi-stazionario
         𝐼#!)
 𝑔2 = 𝛽"                     𝐼%)              Modello di Ebers-Moll
          𝑉&+           𝑔2 =                  in regione normale
                             𝑉&+
 𝐼% = 𝐼& = 𝛽" 𝐼#!                 𝐼#!)       1        𝐼#!) 𝐼%)
                        𝑔%! = 𝛽")      + 𝛽$     = 𝛽")     ≅
                                   𝑉1       𝑟#%        𝑉1   𝑉1

Se la frequenza dei segnali è bassa (regime quasi-stazionario),                 1
gli effetti reattivi possono essere trascurati !                                     0
                                                                               𝑟%&
                                          In regione normale à           𝑌 =
                                                                                      1
                                                                               𝑔(
       𝑖#!                                                                           𝑟'&

                                                    CIRCUITO EQUIVALENTE
                𝑟#!                 𝑟%!             DEL BJT A 3 PARAMETRI
                          𝛽) 𝑖#!
                                                           𝑔2 𝑟#! = 𝛽)
                                                 𝑔2 𝑣#! = 𝑔2 𝑟#! 𝑖#! = 𝛽) 𝑖#!

Il generatore di corrente comandato in tensione può essere trasformato in generatore
di corrente comandato in corrente !
                     Modello a 3 e a 2 parametri del BJT
In regione normale, in regime quasi statico à modello a 3 parametri
                                                                                      1
       𝐼%)                𝑉1                    𝑉&+       𝑉&+   𝑉&+                        0
  𝑔2 =              𝑟%! =           𝑟#! =               ≅     =                      𝑟%&
       𝑉&+                𝐼%)               𝐼#!) + 𝐼#!,* 𝐼#!) 𝐼#)            𝑌 =
                                                                                            1
      𝑖#                                                                             𝑔(
                                                                                           𝑟'&

                                              I parametri differenziali dipendono dal punto
              𝑟#!                   𝑟%!
                           𝛽) 𝑖#!             di lavoro (dalle correnti)

                                              La resistenza di uscita 𝑟%! è dovuta all’effetto
                                              Early (dipende da VA) à se lo trascuro sparisce


                                     CIRCUITO EQUIVALENTE                       1
                                                                                      0
                                     DEL BJT A 2 PARAMETRI                 𝑌 = 𝑟#!
             𝑟#!                      (trascuro l’effetto Early)               𝑔2     0

                        𝛽) 𝑖#!       In regione normale, rimane vero che le tre correnti
                                     del dispositivo rimangono proporzionali tra loro !!
                                               𝑖% = 𝛽) 𝑖#       𝑖! = (𝛽) + 1)𝑖#
                                                            Transistor pnp
Nel transistor pnp le due giunzioni sono rovesciate (correnti e tensioni opposte):

               𝑉!#                                  𝑉%#                          IE
𝐼!# = 𝐼!#* 𝑒𝑥𝑝     −1                𝐼%# = 𝐼%#* 𝑒𝑥𝑝     −1
               𝑉&+                                  𝑉&+

𝐼& = 𝛽" 𝐼!# − 𝛽$ 𝐼%#

• La linearizzazione dei due diodi porta sempre a circuiti         IB
  equivalenti con una resistenza ed una capacità differenziali
• Linearizziamo 𝐼& rispetto alle tensioni VEB e VEC

                               𝑟#%                                               IC

          B                                            C



                             𝐶#%                            𝑣!%
   𝑣!#                                      𝑔2 𝑣!#    𝑟%!
              𝑟#!      𝐶#!


                               E
                                  Circuito equivalente BJT pnp
                          𝑟#%
       B                                      C                 𝑣!% = − 𝑣%!

                                                                𝑣!# = − 𝑣#!
 𝑣!#                    𝐶#%                         𝑣!%
                                     𝑔2 𝑣!#   𝑟%!              𝑔2 𝑣!# = −𝑔2 𝑣#!
            𝑟#!   𝐶#!

                              E
• Posso vedere il generatore di corrente come comandato dalla tensione − 𝑣#!
• Il segno meno può essere eliminato se giro il verso del generatore !
                          𝑟#%
                                                          E’ uguale al circuito equivalente
       B                                      C                    del BJT npn !!
                                                          à il circuito equivalente ai piccoli
                        𝐶#%                         𝑣%!     segnali lavora sulle variazioni
𝑣#!                                 𝑔2 𝑣#!    𝑟%!           rispetto al punto di lavoro
           𝑟#!    𝐶#!
                                                          à tali variazioni possono essere
                          E                                 positive o negative
                                                          à non conta il valore assoluto
 Al piccolo segnale pnp e npn SONO IDENTICI !!              delle correnti !!
                                 Linearizzazione del MOSFET
 La corrente statica ha dipendenza non lineare dalle tensioni (es.: n-MOSFET)

                          0  1
𝐼+, = 𝛽- (𝑉., −𝑉/ )𝑉+, − 𝑉+, (1 + 𝜆𝑉+, )               Regione triodo 𝑉'* ≤ 𝑉<* − 𝑉,
                             0


      𝛽-
𝐼+, =    (𝑉., −𝑉/ )0 (1 + 𝜆𝑉+, )                 Regione saturazione 𝑉'* > 𝑉<* − 𝑉,
      2

   𝑉/ = 𝑉/2 + 𝛾     2𝜓3 + 𝑉,% − 2𝜓3             Effetto Body: ulteriore dipendenza
                                                non lineare

  Linearizzo la corrente rispetto alle tensioni ai 3 terminali (gate, drain, source)

         𝜕𝐼'*       𝜕𝐼'*       𝜕𝐼'*
   𝑖'* =      ( 𝑣 +      ( 𝑣 +      ( 𝑣            𝑔2# dovuta all’effetto Body !
         𝜕𝑉<* ( <* 𝜕𝑉'* ( '* 𝜕𝑉*# ( *#

                                               𝑖'* = 𝑔2 𝑣<* + 𝑔'* 𝑣'* + 𝑔2# 𝑣*#
          𝑔2           𝑔'*          𝑔2#
                        Circuito equivalente del MOSFET
   𝑖'* = 𝑔2 𝑣<* + 𝑔'* 𝑣'* + 𝑔2# 𝑣*#

A livello statico IG = 0, quindi iG = 0                                               𝑔'*
                                                                            𝑔&! 𝑣'!

𝑔2# dovuta all’effetto Body
                                                   = −𝑣*#
      𝜕𝐼'*     𝜕𝐼'*     𝜕𝑉,
𝑔2# =      ( =      ( D     (
      𝜕𝑉*# ( 𝜕𝑉, ( 𝜕𝑉*# (


                         1 :
 𝐼'* = 𝛽= (𝑉<* −𝑉, )𝑉'* − 𝑉'*                                           𝜕𝐼'*      𝜕𝐼'*
                         2                     In entrambi i caso ho:        ( =−      (
                                                                        𝜕𝑉, (     𝜕𝑉<* (
       𝛽=
 𝐼'* =    (𝑉<* −𝑉, ):
       2
                                                         𝜕𝐼'*     𝜕𝑉,
                © 2005 Politecnico di Torino   𝑔2# = −        ( D     ( = −𝑔2 D 𝛼
                                                         𝜕𝑉<* ( 𝜕𝑉*# (
       𝜕𝑉,        𝛾
  𝛼=       ( =
       𝜕𝑉*# ( 2 2𝜓" + 𝑉*#)
                      Circuito equivalente del MOSFET
    𝑖'* = 𝑔2 𝑣<* + 𝑔'* 𝑣'* + 𝑔2# 𝑣*#


    𝑔2# = −𝑔2 D 𝛼                                                          𝛼𝑔& 𝑣'!        𝑔'*

  se 𝑣*# = 0 à un generatore in meno
                                                 = −𝑣*#


          Regione triodo                              Regione saturazione

                        1 :                                  𝛽=
𝐼'* = 𝛽= (𝑉<* −𝑉, )𝑉'* − 𝑉'* (1 + 𝜆𝑉'* )             𝐼'* =      (𝑉<* −𝑉, ): (1 + 𝜆𝑉'* )
                        2                                    2

     𝜕𝐼'*
𝑔2 =      ( = 𝛽= (1 + 𝜆𝑉'*) )𝑉'*)                    𝑔2 = 𝛽= (𝑉<*) −𝑉, )(1 + 𝜆𝑉'*) )
     𝜕𝑉<* (
      𝜕𝐼'*    © 2005 Politecnico di Torino                  𝛽=                𝜆𝐼'*)
                                                                        :
                                                     𝑔'* = 𝜆 (𝑉<*) −𝑉, ) =
𝑔'* =      ( = 𝛽= (𝑉<*) −𝑉, − 𝑉'* 0)(1 + 𝜆𝑉'*) ) +
      𝜕𝑉'* (                                                2              (1 + 𝜆𝑉'*) )
                         𝜆𝐼'*)
                   +
                     (1 + 𝜆𝑉'*) )
                   Circuito equivalente semplificato

• se 𝑣*# = 0 à un generatore in meno

• se trascuriamo l’effetto di modulazione di
                                                                              𝑔'*
  lunghezza di canale à l = 0




      Regione triodo                            Regione saturazione


       𝑔2 = 𝛽= 𝑉'*)                            𝑔2 = 𝛽= (𝑉<*) −𝑉, ) =   2𝛽= 𝐼'*)

      𝑔'* = 𝛽= (𝑉<*) −𝑉, − 𝑉'*) )              𝑔'* = 0


                                               BENE !
             0         0
        𝑌 =
            𝑔(        𝑔+,
                        Circuito equivalente p-MOSFET
                            1 :
  𝐼*' = 𝛽> (𝑉*< −|𝑉, |)𝑉*' − 𝑉*' (1 + 𝜆𝑉*' )
                            2
      𝛽>                                                                           𝑔'*
 𝐼*' = (𝑉*< −|𝑉, |): (1 + 𝜆𝑉*' )
      2                                                             𝑔& 𝑣')


  𝑉, = 𝑉,) − 𝛾   2𝜓" + 𝑉#* − 2𝜓"


Corrente da source a drain à generatore comandato da 𝑔2 𝑣*< diretto verso il drain !
Ma 𝑔2 𝑣*< = −𝑔2 𝑣<* à generatore verso il basso comandato da 𝑔2 𝑣<* (come prima!)

    Al piccolo segnale n–MOSFET e p–MOSFET SONO IDENTICI !!

Per 𝑔2 e 𝑔'* ho espressioni analoghe al caso n-MOSFET (attenzione ai segni !)
     Regione triodo                             Regione saturazione

      𝑔2 = 𝛽> |𝑉'*) |                          𝑔2 = 𝛽> |𝑉<*) − 𝑉, | =   2𝛽> 𝐼*')
      𝑔'* = 𝛽> |𝑉<*) − 𝑉, − 𝑉'*) |             𝑔'* = 0
                                   Effetti reattivi del MOSFET
Gli effetti reattivi del MOSFET li abbiamo già studiati !

• Considero il MOSFET acceso (se è spento non è interessante come amplificatore)

• Capacità al terminale di gate à 𝐶<* e 𝐶<' (𝐶<# = 0 se MOSFET ON)

• Se VSB = 0 à la capacità 𝐶*# è cortocircuitata

• Capacità al terminale di drain à 𝐶<' e 𝐶'#



  Basta aggiungere queste capacità al circuito equivalente ai piccoli segnali !
                                        Confronto BJT - MOSFET
• Per entrambi i transistor abbiamo estratto un circuito equivalente che prevede un
  generatore di corrente comandato in tensione sulla porta di uscita à gmv1
• Il ruolo della trans-conduttanza gm è fondamentale (componente 21 della matrice |Y|)
  à regola il trasferimento di segnale dalla porta di ingresso a quella di uscita (amplificatore)


          BJT (in regione normale)                  MOSFET (in saturazione)
                        𝐼%)
                 𝑔2 =                                   𝑔2 =    2𝛽= 𝐼'*)
                        𝑉&+

             proporzionale alla                   proporzionale alla radice quadrata
           corrente nel transistor                   della corrente nel transistor



   • A parità di corrente, gm del BJT > gm del MOSFET
   • BJT migliore del MOSFET per applicazioni analogiche, ma ho il problema della IB
     (potenza spesa alla porta di ingresso)
                                         MOSFET in sottosoglia
Per applicazioni analogiche:
• MOSFET ha lo svantaggio di una gm minore
• BJT ha lo svantaggio di avere IB > 0
Esiste una soluzione che mi porti ad alte gm e corrente nulla di ingresso ?
à MOSFET in SOTTOSOGLIA: VGS lievemente minore di VT
idealmente il MOSFET dovrebbe essere spento, ma nella realtà rimane una
piccola carica di canale che consente di far circolare la corrente

• Il modello per la corrente in sottosoglia è complesso da derivare
• La corrente dipende in maniera esponenziale da VGS


                                           𝑉<* − 𝑉,
     con VGS < VT à          𝐼'* = 𝑘 D 𝑒𝑥𝑝
                                              𝑉&+

          𝜕𝐼'*     𝑘       𝑉<*) − 𝑉,   𝐼'*)           • Espressione simile al BJT
     𝑔2 =      ( =   D 𝑒𝑥𝑝           =
          𝜕𝑉<* ( 𝑉&+          𝑉&+       𝑉&+           • Potenzialmente gm elevata
