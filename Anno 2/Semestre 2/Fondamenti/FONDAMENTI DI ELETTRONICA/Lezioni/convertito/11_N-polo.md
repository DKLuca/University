---
fonte: "11_N-polo.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Linearizzazione N-polo

                 Francesco Driussi

      Corso di Laurea in Ingegneria Elettronica
Dipartimento Politecnico di Ingegneria ed Architettura


             francesco.driussi@uniud.it
             www.diegm.uniud.it/driussi


                   Francesco Driussi – 2020
                           Circuiti con transistor e diodi
• I dispositivi a semiconduttore (transistor, diodi) presentano forti non
  linearità ed effetti reattivi rilevanti
• La presenza di transistor e diodi rende i circuiti non lineari
• Gli effetti reattivi non possono essere trascurati in regime dinamico
• Già semplici circuiti con pochi transistor rendono difficile la loro analisi
es.: inverter CMOS à 2 transistor à analisi statica e dinamica non banale
• La risoluzione di reti non lineari in regime di segnali tempo varianti è un
  problema, soprattutto quando il numero di dispositivi a semiconduttore è
  elevato
• Anche la soluzione numerica (simulatori circuitali) può essere troppo
  onerosa
à Necessità di una strategia che possa rendere fattibile lo studio quantitativo
  di circuiti con centinaio/migliaia/milioni di transistor e diodi
à TEORIA PER L’ANALISI DI N-POLI
                                                                   N-polo
• n terminali
• Elementi a parametri concentrati
• n + n grandezze elettriche (Ik; Vk)
                                                           n
• Problema con 2n variabili
• Le condizioni al contorno (tensioni o
                                                              Vn
  correnti imposte ai terminali del
  circuito) impongono n equazioni
• Altre n equazioni derivano dai modelli
  descrittivi del circuito à mettono in             $

  relazione tra loro le tensioni e le              ! 𝐼! = 0
  correnti ai morsetti del circuito                !"#

• Ulteriori due equazioni dalle leggi di            $
  Kirchhoff !!                                     ! (𝑉!%# − 𝑉! ) = 0
                                                   !"#
• 2n variabili + (2n+2) equazioni
• Non tutte le variabili sono indipendenti   à Rappresentazione INDEFINITA
                                                                  Bipolo
• Esempio: bipolo                                                IA

• 4 grandezze elettriche (IA, IB, VA, VB)                         VA

à rappresentazione INDEFINITA
• Però solo 2 di queste grandezze sono indipendenti !
• Legge di Kirchhoff per le correnti à       𝐼! + 𝐼" = 0          VB
• Legge di Kirchhoff per le tensioni à       𝑉!" + 𝑉"! = 0
                                                                  IB
• Per risolvere il circuito mi basta un sistema di 2 equazioni
  in 2 incognite
à rappresentazione DEFINITA (uso solo variabili indipendenti)
es.: resistenza à incognite (IA, VAB)
•   1 condizione al contorno (es.: IA = …)
•   legge di Ohm à VAB = R ∙ IA
                               Rappresentazione definita
• Per ottenere una rappresentazione definita basta definire
  uno dei terminali come riferimento
es.: terminale j-esimo preso come riferimento
• Vj = 0 (diventa riferimento di tensione)
• 𝐼! = − ∑"#! 𝐼" (corrente sul terminale si ottiene dalle
    altre)
•   Nel bipolo ho due terminali à posso ottenere due
    rappresentazioni definite distinte
à La rappresentazione definita non è unica !!


N-polo à una sola rappresentazione indefinita
         à N possibili rappresentazioni definite
         (una per ogni terminale preso come riferimento)
                                               Tipi di componenti
I componenti (n-poli) possono avere caratteristiche diverse:
•   Componente NORMALE
à relazioni lineari tra le (2n - 2) grandezze elettriche indipendenti
•   Componente ANOMALO
à relazioni NON lineari tra le (2n - 2) grandezze elettriche indipendenti
        𝐹 𝑉, 𝐼 = 0
•   Componente con EFFETTI REATTIVI
à relazioni DIFFERENZIALI tra le (2n - 2) grandezze elettriche indipendenti
        𝐹 𝑉, 𝑉,̇ 𝑉,̈ … , 𝐼, 𝐼,̇ 𝐼,̈ … = 0
gli effetti reattivi si possono trascurare solo in condizioni statiche
à 𝐹 𝑉, 𝐼 = 0 mi da le caratteristiche statiche del componente
                                    Caratteristiche statiche
A) La caratteristica statica sta solo nel primo e terzo quadrante del grafico
   corrente-tensione à COMPONENTE PASSIVO
                         I
                                                           P = V∙I > 0
                                                  La potenza è sempre positiva
                                             V         à Assorbe potenza



B) La caratteristica statica passa anche nel secondo e quarto quadrante del
   grafico corrente-tensione à COMPONENTE ATTIVO
                         I                                   P = V∙I
                                                   La potenza assume anche
                                                         valori negativi
                                                      à Eroga potenza !!
                                             V    Asintoticamente la curva deve
                                                    rientrare nel primo e terzo
                                                 quadrante à NO energia infinita
                                             Componente anomalo
 •   Componente ANOMALO in regime stazionario
 à relazioni NON lineari tra le (2n - 2) grandezze elettriche indipendenti
 es.: bipolo anomalo à 𝐹 𝑉, 𝐼 = 0

                           I
                           I0            Q




                                    V0                 V



Caratteristica statica formata da tutti i punti di lavoro Q ≡ (I0,V0) che soddisfano F = 0
Hp.: siamo riusciti a risolvere F(Q) = 0
à ogni volta che ci spostiamo anche di poco da Q dobbiamo risolvere di nuovo F = 0
  à diventa difficile e lungo
à necessità di trovare una relazione lineare FL che approssima la funzione F
                Linearizzazione del comp. anomalo
Qual è la migliore approssimazione lineare della funzione F ?
à Retta tangente nel punto Q à linearizzazione della funzione F
à ovviamente dipende da Q
à quindi la funzione FL che ci serve dipende da Q
à FL è la migliore approssimazione di F nell’intorno di Q
La LINEARIZZAZIONE VALE IN UN DOMINO LIMITATO à piccole variazioni delle
grandezze rispetto ai valori I0 e V0 à REGIME DEI PICCOLI SEGNALI

                         I

                         I0            Q
                                                     𝐹 𝑉, 𝐼 = 0 à 𝐹# 𝑉, 𝐼 = 0



                                  V0                 V
                           Linearizzazione bipolo anomalo
 • Espansione in serie di Taylor intorno al punto di lavoro Q (I0, V0)
 • Tronco l’espansione al primo ordine

                    𝜕𝐹         𝜕𝐹         𝜕(𝐹                 V − 𝑉& ( 𝜕 ( 𝐹   I − 𝐼& (
𝐹 𝐼, 𝑉 = 𝐹 𝐼& , 𝑉& + * V − 𝑉& + * I − 𝐼& + ( /                        + (/              +⋯
                    𝜕𝑉 '       𝜕𝐼 '       𝜕𝑉                     2     𝜕𝐼         2
                                                          '                '

                        𝜕𝐹           𝜕𝐹         𝜕𝐹         𝜕𝐹
𝐹) 𝐼, 𝑉 = 𝐹 𝐼& , 𝑉& +      * V − 𝑉& + * I − 𝐼& = * V − 𝑉& + * I − 𝐼& = 0
                        𝜕𝑉 '         𝜕𝐼 '       𝜕𝑉 '       𝜕𝐼 '

                   =0

𝑣 = V − 𝑉& à tensione di piccolo segnale      (variazione rispetto al punto di lavoro)
𝑖 = I − 𝐼& à corrente di piccolo segnale

  𝜕𝐹     𝜕𝐹                • La linearizzazione ha trasformato il bipolo anomalo in un
     * 𝑣+ * 𝑖=0
  𝜕𝑉 '   𝜕𝐼 '                componente normale !
                           • La trasformazione dipende dal punto di lavoro Q !!
                           𝑏                              𝑏
 𝑎𝑣+𝑏𝑖 =0           𝑣=−      𝑖 à Legge di Ohm         −     = resistenza DIFFERENZIALE
                           𝑎                              𝑎
                                                        Esempio: DIODO
• Il diodo è un bipolo anomalo                                            𝑉$
• Analisi statica à effetti reattivi si annullano         𝐼$ = 𝐼% + 𝑒𝑥𝑝       −1
                                                                          𝑉&'
             𝜕𝐼*                                  𝜕𝐼*                      𝜕𝐼*
𝐼* = 𝐼*& +       * 𝑉 − 𝑉*&           𝐼* − 𝐼*& =       * 𝑉 − 𝑉*&       𝑖* =     * 𝑣
             𝜕𝑉* ' *                              𝜕𝑉* ' *                  𝜕𝑉* ' *

                                      𝑣* = 𝑉* − 𝑉*&      à tensione di piccolo segnale
                                      𝑖* = 𝐼* − 𝐼*&      à corrente di piccolo segnale
              ID0
                                        𝜕𝐼*     𝐼+       𝑉*&   𝐼*& + 𝐼+
                                            * =    9 𝑒𝑥𝑝     =          = 𝑔*
                                        𝜕𝑉* ' 𝑉,-        𝑉,-     𝑉,-
                    VD0
                                                  𝑔* conduttanza DIFFERENZIALE
                                             (in generale ho parametri differenziali)
          𝑖* = 𝑔* 𝑣*

    con 𝑔* che dipende da Q !!            Nel regime dei piccolo segnali il diodo è
   se VD sale, ID sale, 𝑔* sale !!        diventato una conduttanza/resistenza !!
                                       Effetti reattivi non lineari
• Se gli effetti reattivi (es: capacitivi) sono lineari à descrivo tramite capacità lineare
  (costante)
• Se gli effetti reattivi sono NON lineari à condensatore ANOMALO à Q = f(V)
à LINEARIZZAZIONE

            𝜕𝑄                     𝑞 = 𝑄 − 𝑄&             𝜕𝑄                   𝜕𝑄
 𝑄 = 𝑄& +      *  𝑉 − 𝑉&                             𝑞=      * 𝑣        𝐶* =      *
            𝜕𝑉 .)                  𝑣 = 𝑉 − 𝑉&             𝜕𝑉 .)                𝜕𝑉 .)

                                                            𝐶* capacità DIFFERENZIALE
     𝑑𝑞 𝑑(𝐶* 𝑣) 𝑑𝐶*        𝑑𝑣   𝑑 𝜕𝑄                      𝑑𝑣
𝑖=      =      =    𝑣 + 𝐶*    =      *             𝑣 + 𝐶*
     𝑑𝑡   𝑑𝑡     𝑑𝑡        𝑑𝑡 𝑑𝑡 𝜕𝑉 .)                    𝑑𝑡


      𝑑 𝜕𝑄     𝑑𝑉&        𝑑𝑣 𝑑𝐶* 𝑑𝑉&        𝑑𝑣
𝑖=         *       𝑣 + 𝐶*   =   9    𝑣 + 𝐶*
     𝑑𝑉& 𝜕𝑉 .) 𝑑𝑡         𝑑𝑡 𝑑𝑉& 𝑑𝑡         𝑑𝑡


se il punto di lavoro (PL) è stabile nel tempo il primo termine è nullo !!
           /0
à 𝑖 = 𝐶*        à al piccolo segnale ho la stessa relazione di un condensatore lineare
           /,
                                                        Esempio: DIODO
• Il diodo è un bipolo anomalo con effetti reattivi                         𝑉$
• Analisi statica à linearizzazione della F(I, V)=0        𝐼$ = 𝐼% + 𝑒𝑥𝑝        −1
                                                                            𝑉&'
          𝜕𝐼*                   𝜕𝐼*     𝐼*& + 𝐼+    1
     𝑖* =     * 𝑣          𝑔* =     * =          =
          𝜕𝑉* ' *               𝜕𝑉* '     𝑉,-      𝑟*

 𝑣* = 𝑉* − 𝑉*&                     𝐼*&
                            𝑔* ≅           à polarizzazione in diretta
 𝑖* = 𝐼* − 𝐼*&                     𝑉,-

                            𝑔* ≅ 0         à polarizzazione in inversa      𝑟* → ∞

In regione diretta gli effetti reattivi sono essenzialmente dati dalla carica di diffusione !

 𝑄$ = 𝐼$ 𝜏 (      𝜏 G à tempo di transito attraverso la giunzione

                                                                            CIRCUITO
        𝜕𝑄*        𝜕𝐼*
 𝐶* =       * = 𝜏1     * = 𝜏 1 𝑔*                                         EQUIVALENTE
        𝜕𝑉* '      𝜕𝑉* '
                                                                        (al piccolo segnale)
                                                                           DEL DIODO
                                                           Esempio: DIODO
• Il diodo è un bipolo anomalo con effetti reattivi                         𝑉$
• Analisi statica à linearizzazione della F(I, V)=0         𝐼$ = 𝐼% + 𝑒𝑥𝑝       −1
                                                                            𝑉&'
          𝜕𝐼*                      𝜕𝐼*     𝐼*& + 𝐼+    1
     𝑖* =     * 𝑣             𝑔* =     * =          =
          𝜕𝑉* ' *                  𝜕𝑉* '     𝑉,-      𝑟*

 𝑣* = 𝑉* − 𝑉*&                       𝐼*&
                              𝑔* ≅          à polarizzazione in diretta
 𝑖* = 𝐼* − 𝐼*&                       𝑉,-

                              𝑔* ≅ 0        à polarizzazione in inversa     𝑟* → ∞

In regione inversa gli effetti reattivi sono essenzialmente dati dalla carica spaziale !

                    1
      𝐶) = 𝐶)*
                        𝑉$*
                  1−                                                        CIRCUITO
                        Φ)
                                                                          EQUIVALENTE
  𝐶* = 𝜏 1 𝑔* ≅ 0 polarizzazione                                      (al piccolo segnale)
    𝑟* → ∞          in inversa                                              DEL DIODO
                                           Effetti reattivi complessi
Effetti reattivi complessi à funzioni differenziali non lineari con ordine di derivata elevato
es.: bipolo anomalo reattivo à 𝐹 𝑉, 𝑉,̇ 𝑉,̈ … , 𝐼, 𝐼,̇ 𝐼,̈ … = 0
• Posso vederla come una funzione su più variabili à 𝐹 𝑋# , 𝑋( , … , 𝑋$ = 0
• Funzione non lineare à LINEARIZZO à regime dei piccoli segnali

 𝑎* 𝑣 + 𝑎+ 𝑣̇ + 𝑎, 𝑣̈ + ⋯ + 𝑏* 𝑖 + 𝑏+ 𝑖̇ + 𝑏, 𝑖̈ + ⋯ = 0 (dove aj, bj sono le derivate parziali
                          rispetto alle variabili Xj, siano esse dipendenti dalla tensione o corrente)

• Funzione differenziale lineare à comunque è complicata da risolvere !
à DOMINIO DELLE TRASFORMATE DI LAPLACE (di Fourier)
                     ℒ 9 = 𝑡𝑟𝑎𝑠𝑓𝑜𝑟𝑚𝑎𝑡𝑎 𝑑𝑖 𝐿𝑎𝑝𝑙𝑎𝑐𝑒
         𝑣(𝑡) à 𝑉 𝑠 = ℒ 𝑣(𝑡)
        𝑖(𝑡) à 𝐼 𝑠 = ℒ 𝑖(𝑡)
à Proprietà delle trasformate di Laplace à trasformata della derivata
         𝑣(𝑡)
          ̇    à ℒ 𝑣(𝑡)
                    ̇     =𝑠9𝑉 𝑠 −𝑣 𝑡 =0
         𝑖̇ (𝑡) à ℒ 𝑖̇ (𝑡) = 𝑠 9 𝐼 𝑠 − 𝑖 𝑡 = 0
à applicando ricorsivamente la proprietà: ℒ 𝑣(𝑡)
                                             ̈   = 𝑠 ℒ 𝑣(𝑡)
                                                        ̇   − 𝑣̇ 0
         ℒ 𝑣(𝑡)
            ̈   = 𝑠 𝑠𝑉 𝑠 − 𝑣 0 − 𝑣̇ 0 à ℒ 𝑣(𝑡)
                                           ̈   = 𝑠 ( 𝑉 𝑠 − 𝑠 𝑣 0 − 𝑣̇ 0
                                   Dominio delle trasformate
Equazione differenziale nel dominio del tempo à Equazione algebrica (polinomiale)
nel dominio delle trasformate di Laplace (di Fourier)

  𝑎* 𝑣 + 𝑎+ 𝑣̇ + 𝑎, 𝑣̈ + ⋯ + 𝑏* 𝑖 + 𝑏+ 𝑖̇ + 𝑏, 𝑖̈ + ⋯ = 0


  𝑎* 𝑉(𝑠) + 𝑎+ 𝑠𝑉 𝑠 − 𝑣 0 + 𝑎, 𝑠 , 𝑉 𝑠 − 𝑠 𝑣 0 − 𝑣̇ 0 + ⋯ +

  + 𝑏* 𝐼 𝑠 + 𝑏+ 𝑠𝐼 𝑠 − 𝑖 0 + 𝑏, 𝑠 , 𝐼 𝑠 − 𝑠 𝑖 0 − 𝑖̇ 0 + ⋯ = 0


  𝑉 𝑠 𝑎* + 𝑎+ 𝑠 + 𝑎, 𝑠 , + ⋯ − 𝑎+ 𝑣 0 + 𝑎, 𝑠𝑣 0 + 𝑎, 𝑣̇ 0 + ⋯ +

   + 𝐼 𝑠 𝑏* + 𝑏+ 𝑠 + 𝑏, 𝑠 , + ⋯ − 𝑏+ 𝑖 0 + 𝑏, 𝑠𝑖 0 + 𝑏, 𝑖̇ 0 + ⋯ = 0


                 𝐴 𝑠 𝑉 𝑠 + 𝐵 𝑠 𝐼 𝑠 = 𝐴* 𝑠 + 𝐵* (𝑠)

   A(s), B(s), A0(s), B0 (s) à polinomi in s
   A0(s), B0 (s) à polinomi in s di grado inferiore a A(s) e B(s), rispettivamente
                                 Impedenza ed ammettenza
                        𝐴 𝑠 𝑉 𝑠 + 𝐵 𝑠 𝐼 𝑠 = 𝐴* 𝑠 + 𝐵* (𝑠)

A(s), B(s), A0(s), B0 (s) à polinomi in s
A0(s), B0 (s) à contengono le condizioni iniziali à 𝑣 0 , 𝑣̇ 0 , … , 𝑖 0 , 𝑖̇ 0 , …
Considerando tutte le condizioni iniziali NULLE (stato zero)
A0(s) = 0, B0 (s) = 0


  𝐴 𝑠 𝑉 𝑠 +𝐵 𝑠 𝐼 𝑠 =0


         𝐵 𝑠                         𝐵 𝑠
  𝑉 𝑠 =−     𝐼 𝑠              𝑍 𝑠 =−            à IMPEDENZA GENERALIZZATA
         𝐴 𝑠                         𝐴 𝑠


         𝐴 𝑠                         𝐴 𝑠
  𝐼 𝑠 =−     𝑉 𝑠              𝑌 𝑠 =−            à AMMETTENZA GENERALIZZATA
         𝐵 𝑠                         𝐵 𝑠
                                                                 Linearizzazione N-polo
 • n-polo in rappresentazione indefinita
 • 2n grandezze elettriche (Ik; Vk)
 • n condizioni al contorno
                                                                                                    n
 • n equazioni descrittive del circuito
 à se è anomalo e con effetti reattivi le
                                                                                                    Vn
 equazioni sono differenziali non lineari

 𝐹# 𝑉# , 𝑉#̇ , … , 𝑉( , 𝑉(̇ , … , 𝑉$ , 𝑉$̇ , … , 𝐼# , 𝐼#̇ , … , 𝐼( , 𝐼(̇ , … , 𝐼$ , 𝐼$̇ , … , = 0
 …
 …
 𝐹$ 𝑉# , 𝑉#̇ , … , 𝑉( , 𝑉(̇ , … , 𝑉$ , 𝑉$̇ , … , 𝐼# , 𝐼#̇ , … , 𝐼( , 𝐼(̇ , … , 𝐼$ , 𝐼$̇ , … , = 0

𝑋W = 𝑉# , 𝑉#̇ , … , 𝑉( , 𝑉(̇ , … , 𝑉$ , 𝑉$̇ , … , 𝐼# , 𝐼#̇ , … , 𝐼( , 𝐼(̇ , … , 𝐼$ , 𝐼$̇ , … , à vettore delle variabili

𝑋W& = 𝑉#& , 𝑉#&̇ , … , 𝑉(& , 𝑉(&
                               ̇ , … , 𝑉$& , 𝑉$&
                                               ̇ , … , 𝐼#& , 𝐼#&̇ , … , 𝐼(& , 𝐼(&̇ , … , 𝐼$& , 𝐼$&̇ , … , à valore nel

punto di lavoro
                                   𝐹! 𝑋W& = 0            ∀𝑘
                                                Linearizzazione N-polo
 Linearizziamo la generica funzione Fk
                   𝜕𝐹!              𝜕𝐹!                     𝜕𝐹!              𝜕𝐹!
    " = 𝐹! 𝑋/" +
 𝐹! 𝑋                  2 𝑉# − 𝑉#" +     2  𝑉#̇ − 𝑉#"̇ + ⋯ +     2 𝐼& − 𝐼&" +      2 𝐼&̇ − 𝐼&"̇ + ⋯
                   𝜕𝑉# %$             ̇
                                    𝜕𝑉# %$                  𝜕𝐼& %$              ̇
                                                                             𝜕𝐼& %$
                        !                   !                      !                  !



 𝐹! 𝑋W& = 0 quindi dobbiamo risolvere:

𝜕𝐹!              𝜕𝐹!                                 𝜕𝐹!              𝜕𝐹!
    * 𝑉# − 𝑉#& +     *            𝑉#̇ − 𝑉#&̇ + ⋯ +       * 𝐼$ − 𝐼$& +      *       𝐼$̇ − 𝐼$&̇ + ⋯ = 0
𝜕𝑉# 32             ̇
                 𝜕𝑉# 32                              𝜕𝐼$ 32              ̇
                                                                      𝜕𝐼$ 32
     '                        '                           '                    '


 Utilizzando ora i piccoli segnali, per la k-esima equazione abbiamo:

  𝑎!#& 𝑣# + 𝑎!## 𝑣#̇ + 𝑎!#( 𝑣#̈ + ⋯ + 𝑎!(& 𝑣( + 𝑎!(# 𝑣(̇ + ⋯ + 𝑎!$& 𝑣$ + 𝑎!$# 𝑣$̇ + ⋯
  + 𝑏!#& 𝑖# + 𝑏!## 𝑖#̇ + ⋯ + 𝑏!$& 𝑖$ + 𝑏!$# 𝑖$̇ + ⋯ = 0

 Passiamo ora al dominio delle trasformate di Laplace:


 𝑉4 𝑠 = ℒ 𝑣4 (𝑡)            ℒ 𝑣4̇ (𝑡) = 𝑠𝑉4 𝑠 − 𝑣4 0          ℒ 𝑣4̈ (𝑡) = 𝑠 ( 𝑉4 𝑠 − 𝑠𝑣4 0 − 𝑣4̇ 0
                                        Dominio delle trasformate
 𝑎!#& 𝑉# + 𝑎!## 𝑠𝑉# − 𝑎!## 𝑠𝑣# 0 + ⋯ + 𝑎!(& 𝑉( + 𝑎!(# 𝑠𝑉( − 𝑎!(# 𝑣( 0 + ⋯ + 𝑏!#& 𝐼#
 + 𝑏!## 𝑠𝐼# − 𝑏!## 𝑖# 0 + ⋯ + 𝑏!$& 𝐼$ + 𝑏!$# 𝑠𝐼$ − 𝑏!$# 𝑖$ (0) + ⋯ = 0

Raccolgo ora tutti i termini in V1, V2, … , I1, I2, … , inoltre separo tutti i termini che
contengono le condizioni iniziali 𝑣4 0 e 𝑖4 0
à raccogliendo scompare il contatore sul grado delle derivate (indicato comunque dal
   grado della potenza di s)

    𝐴!# 𝑠 𝑉# + 𝐴!( 𝑠 𝑉( + ⋯ + 𝐴!$ 𝑠 𝑉$ + 𝐴&,!# 𝑠 + 𝐴&,!( 𝑠 + ⋯ + 𝐴&,!$ 𝑠
    + 𝐵!# 𝑠 𝐼# + 𝐵!( 𝑠 𝐼( + ⋯ + 𝐵!$ (𝑠)𝐼$ + +𝐵&,!# 𝑠 + 𝐵&,!( 𝑠 + ⋯ + 𝐵&,!$ 𝑠 = 0


 Akj(s), Bkj (s), A0,kj(s), B0,kj (s) à polinomi in s
 A0,kj(s), B0,kj (s) à polinomi in s che contengono le condizioni iniziali
 L’operazione di linearizzazione e di passaggio al domino delle trasformate
 va fatta per tutte le funzioni Fk con che va k da 1 a n
                                     Rappresentazione matriciale
Le n equazioni differenziali non lineari sono state trasformate in n equazioni algebriche
à sistema di n equazioni polinomiali in s
à le metto in forma matriciale

             𝐴++ 𝑠       ⋯        𝐴+9 𝑠    𝑉+   𝐴*,++ 𝑠 + … + 𝐴*,+9 𝑠
               ⋮         ⋱           ⋮      ⋮ +           ⋮
             𝐴9+ 𝑠       ⋯        𝐴99 𝑠    𝑉9   𝐴*,9+ 𝑠 + … + 𝐴*,99 𝑠


              𝐵++ 𝑠           ⋯    𝐵+9 𝑠     𝐼+   𝐵*,++ 𝑠 + … + 𝐵*,+9 𝑠
            +    ⋮            ⋱       ⋮       ⋮ +           ⋮             = 0D
              𝐵9+ 𝑠           ⋯    𝐵99 𝑠     𝐼9   𝐵*,9+ 𝑠 + … + 𝐵*,99 𝑠

Considerando tutte le condizioni iniziali NULLE (stato zero)
A0,kj(s) = 0, B0,kj (s) = 0

                                    𝐴̿ + 𝑉, + 𝐵/ + 𝐼 ̅ = 0,
                        Matrici ammettenza e impedenza
                                   𝐴̿ + 𝑉, + 𝐵/ + 𝐼 ̅ = 0,
𝐼 ̅ è il vettore delle trasformate delle correnti di piccolo segnale (variazione
rispetto alla corrente nel punto di lavoro)

𝑉D è il vettore delle trasformate delle tensioni di piccolo segnale (variazione
rispetto alla tensione nel punto di lavoro)

𝐴̿ e 𝐵G sono matrici le cui componenti sono polinomi in s

se 𝐵G è invertibile à    𝐼 ̅ = −𝐵/ \] + 𝐴̿ + 𝑉, = 𝑌/ + 𝑉,
se 𝐴̿ è invertibile à    𝑉, = −𝐴̿\] + 𝐵/ + 𝐼 ̅ = 𝑍̿ + 𝐼 ̅
   𝑌G è la matrice ammettenza del n-polo (le componenti hanno le dimensioni di una
                                                                          conduttanza)

    𝑍̿ è la matrice impedenza del n-polo (le componenti hanno le dimensioni di una
                                                                            resistenza)
                       Matrici ammettenza e impedenza
                                                            G = −𝐵G ;+ + 𝐴̿
se 𝐵^ è invertibile allora 𝑌^ (matrice ammettenza) esiste à 𝑌

𝐼 ̅ = 𝑌G + 𝑉D à sistema di equazioni lineari à 𝐼! 𝑠 = ∑$4"# 𝑌!4 𝑉4 (𝑠)

Legge di Kirchhoff per le correnti à ∑$!"# 𝐼! = 0

∑9<=+ ∑9)=+ 𝑌<) 𝑉) (𝑠) = 0 à ∑9)=+ ∑9<=+ 𝑌<) 𝑉) (𝑠) = ∑9)=+ 𝑉) (𝑠) + ∑9<=+ 𝑌<) = 0

à questa relazione è valida qualunque sia il vettore delle tensioni 𝑉W !!

à ∑$!"# 𝑌!4 = 0 à la somma delle componenti di ciascuna colonna j-esima è nulla

à una riga della matrice 𝑌^ è linearmente dipendente dalle altre (n-1) righe !!

à la matrice 𝑌G è singolare e quindi non è invertibile !!

LA MATRICE IMPEDENZA 𝑍̿ NON ESISTE !!
                       Matrici ammettenza e impedenza
Inoltre, se cambio sistema di riferimento alle tensioni (traslazione rigida di tutte le
tensioni), le correnti non devono cambiare nel sistema !

a = 𝑉W + Δ (sommo la stessa quantità a tutte le componenti)
𝑉′

                     I à 𝑌^ 9 𝑉W − 𝑌^ 9 𝑉 6 = 𝑌^ 9 𝑉W − 𝑉 6 = 0 à ∑$ 𝑌!4 Δ = Δ 9 ∑$ 𝑌!4 = 0
𝐼 ̅ = 𝑌G + 𝑉D = 𝑌G + 𝑉′                                            4"#            4"#


∑$4"# 𝑌!4 = 0 à somma sulla riga nulla à una colonna è linearmente dipendente dalle

altre (n-1) colonne à la matrice ammettenza è singolare e non invertibile !!

LA MATRICE IMPEDENZA 𝑍̿ NON ESISTE !!

Calcoli analoghi possono essere fatti dimostrando che se esiste 𝑍̿ allora non esiste 𝑌^

Partendo dalla rappresentazione indefinita di un n-polo ci possiamo ricavare la matrice

ammettenza oppure la matrice impedenza (ma solo una delle due esiste)
                                      Rappresentazione definita
• Se ho un n-polo, posso usare la rappresentazione definita per studiarlo
• Prendo il terminale k-esimo come riferimento à Vk = 0
• (2n – 2) variabili indipendenti à (2n – 2) equazioni = (n – 1) condizioni al contorno
   + (n – 1) equazioni descrittive del componente
Hp.: 𝐼 ̅ = 𝑌^ 9 𝑉W dalla rappresentazione indefinita
à Per ottenere la matrice relativa alla rappresentazione definita basta cancellare la
   k-esima riga e k-esima colonna !! à matrice (n – 1) x (n – 1)
à Chiaramente posso ottenere n distinte nuove matrici (n – 1) x (n – 1) facendo
   variare k da 1 a n à ho n diverse rappresentazioni definite


Dalla matrice della rappresentazione definita posso eventualmente ricostruire anche
la matrice della rappresentazione indefinita perché so che nella sua matrice vale:
à Vk = 0 e ∑$!"# 𝐼! = 0 (LKC)
à ∑$4"# 𝑌!4 = 0 e ∑$!"# 𝑌!4 = 0 à       ricostruisco la riga e la colonna mancanti !
                                                                  Quadripolo
Un caso di interesse è il quadripolo: 4 terminali à 4 tensioni e 4 correnti nella
rappresentazione indefinita
• Se è lineare ne possiamo dare una descrizione tramite sistema lineare
• Se è anomalo, lo possiamo linearizzare à sistema lineare
• Se ci sono effetti reattivi à Dominio delle trasformate di Laplace à sistema lineare
                                                            𝑉#         𝐼#
es.: esiste la matrice impedenza                            𝑉(         𝐼
                                                               = 𝑍 (
                                                            𝑉7         𝐼7
                                                            𝑉8         𝐼8
Per la rappresentazione definita ci bastano 3 tensioni e
                                                                    𝑉#       𝐼#
3 correnti à un morsetto di riferimento (es.: terminale n. 4)       𝑉( = 𝑍 𝐼(
à nella matrice elimino la 4a riga e la 4a colonna                  𝑉7       𝐼7


Un caso particolare di quadripolo è il DOPPIO BIPOLO (DUE PORTE)

                                                                𝑉#                      𝑉(
         I1 = -I3    Solo 2 correnti sono indipendenti         porta 1              porta 2
         I2 = -I4    à solo 2 tensioni indipendenti
                                                               𝑉7                       𝑉8
                                                                Doppio bipolo
 Nel DOPPIO BIPOLO (DUE PORTE) à I1 = -I3            I2 = -I4                 𝑉#           𝐼#
                                                                              𝑉(           𝐼(
 𝑉# = 𝑍## 𝐼# + 𝑍#( 𝐼( + 𝑍#7 𝐼7 + 𝑍#8 𝐼8 = 𝑍## − 𝑍#7 𝐼# + (𝑍#( − 𝑍#8 )𝐼(          = 𝑍
                                                                              𝑉7           𝐼7
                                                                              𝑉8           𝐼8
  𝑉7 = 𝑍7# − 𝑍77 𝐼# + (𝑍7( − 𝑍78 )𝐼(
                                                                    𝑉#                          𝑉(
𝑉# −𝑉7 = 𝑍## − 𝑍#7 − 𝑍7# + 𝑍77 𝐼# + (𝑍#( − 𝑍#8 − 𝑍7( + 𝑍78 )𝐼(     porta 1                 porta 2

                                                                    𝑉7                          𝑉8
  𝑉# ′                 6                        6
                      𝑍##                      𝑍#(

  𝑉#6 = 𝑍##
         6        6
            𝐼# + 𝑍#( 𝐼(
                                                         Nel doppio bipolo, bastano 2
  𝑉(6 = 𝑍(#
         6        6
            𝐼# + 𝑍(( 𝐼(                                  equazioni per studiare il circuito
                                                         (2 incognite + 2 condizioni al contorno)

                          Descrizione                             Descrizione
     𝑉#          𝐼#       attraverso la       𝐼#         𝑉#       attraverso la
        = 𝑍                                      = 𝑌
     𝑉(          𝐼(       matrice             𝐼(         𝑉(       matrice
                          impedenza                               ammettenza

Nella maggior parte dei casi, gli amplificatori sono DOPPIO BIPOLI !!
                                                                Matrici ibride
 Esistono altre matrici per la descrizione dei doppi bipoli à diverse scelte delle variabili
 di ingresso (condizioni al contorno imposte)


 Matrice ibrida «h»

   𝑉# = ℎ## 𝐼# + ℎ#( 𝑉(   Le componenti della matrice hanno
                          dimensioni diverse: h11 resistenza,
   𝐼( = ℎ(# 𝐼# + ℎ(( 𝑉(   h22 conduttanza, h12 e h21 numeri puri

 Matrice ibrida «g»

   𝐼# = 𝑔## 𝑉# + 𝑔#( 𝐼(   Le componenti della matrice hanno
                          dimensioni diverse: g11 conduttanza,
   𝑉( = 𝑔(# 𝑉# + 𝑔(( 𝐼(   g22 resistenza, g12 e g21 numeri puri



Posso descrivere il doppio bipolo in maniera del tutto equivalente con la matrice
impedenza, la matrice ammettenza o con le matrici ibride, a patto che queste esistano !!
                                                           Matrice a catena
Una matrice interessante è la matrice a catena (o di trasmissione) à utile quando ho
sistemi in cascata

                                                 A                            B
Matrice a catena blocco A

  𝑉(9 = 𝑚##
         9 9      9 9
            𝑉# − 𝑚#( 𝐼#
                                            9         9                    :       :
                                      9    𝑚##       𝑚#(             :    𝑚##     𝑚#(
  𝐼(9 = 𝑚(#
         9 9      9 9
            𝑉# − 𝑚(( 𝐼#           𝑚       = 9         9          𝑚       = :       :
                                           𝑚(#       𝑚((                  𝑚(#     𝑚((

Matrice a catena blocco B           𝑉(9     9         𝑉#9        𝑉(:    :         𝑉#:
                                        = 𝑚                       : = 𝑚
                                    𝐼(9               −𝐼#9       𝐼(               −𝐼#:
  𝑉(: = 𝑚##
         : :      : :
            𝑉# − 𝑚#( 𝐼#
                                                     𝑉(9 = 𝑉#:   𝐼(9 = −𝐼#:
   𝐼(: = 𝑚(#
          : :      : :
             𝑉# − 𝑚(( 𝐼#


 𝑉(: = 𝑚##
        : 9      : 9
           𝑉( + 𝑚#(       :
                    𝐼( = 𝑚##  9 9
                             𝑚##       9 9
                                 𝑉# − 𝑚#(       :
                                          𝐼# + 𝑚#(  9 9
                                                   𝑚(#       9 9
                                                       𝑉# − 𝑚(( 𝐼# =
       :   9 9      :   9 9      :   9 9      :   9 9
    = 𝑚## 𝑚## 𝑉# + 𝑚#( 𝑚(# 𝑉# − 𝑚## 𝑚#( 𝐼# − 𝑚#( 𝑚(( 𝐼# =
       :   9     :   9
    = 𝑚## 𝑚## + 𝑚#( 𝑚(# 𝑉#9 − (𝑚##
                                :   9
                                   𝑚#(    :
                                       + 𝑚#(  9
                                             𝑚(( )𝐼#9
                                                           Matrice a catena
Una matrice interessante è la matrice a catena (o di trasmissione) à utile quando ho
sistemi in cascata

   𝑉(9 = 𝑚##
          9 9      9 9
             𝑉# − 𝑚#( 𝐼#                         A                        B
   𝐼(9 = 𝑚(#
          9 9      9 9
             𝑉# − 𝑚(( 𝐼#

                                            9         9                  :       :
                                           𝑚##       𝑚#(                𝑚##     𝑚#(
  𝑉(: = 𝑚##
         : :      : :
            𝑉# − 𝑚#( 𝐼#           𝑚   9
                                          = 9         9        𝑚   :
                                                                       = :       :
                                           𝑚(#       𝑚((                𝑚(#     𝑚((
   𝐼(: = 𝑚(#
          : :      : :
             𝑉# − 𝑚(( 𝐼#
                                                                              𝑉(9 = 𝑉#:
 𝑉(: = 𝑚##
        :   9
           𝑚##    :
               + 𝑚#(  9
                     𝑚(# 𝑉#9 − (𝑚##
                                 :   9
                                    𝑚#(    :
                                        + 𝑚#(  9
                                              𝑚(( )𝐼#9                        𝐼(9 = −𝐼#:

               𝑚##                        𝑚#(                      𝑉(:          𝑉#9
                                                                       = 𝑚
                                                                   𝐼(:          −𝐼#9
 𝐼(: = 𝑚(#
        :   9
           𝑚##    :
               + 𝑚((  9
                     𝑚(# 𝑉#9 − (𝑚(#
                                 :   9
                                    𝑚#(    :
                                        + 𝑚((  9
                                              𝑚(( )𝐼#9

                                                               𝑉(:    :                𝑉#9
               𝑚(#                        𝑚((                   : = 𝑚          𝑚9
                                                               𝐼(                      −𝐼#9
                                                      Passaggi tra matrici
Le descrizioni sono tutte equivalenti à posso passare da una matrice all’altra
es.: esiste la matrice ammettenza à come ricavo la matrice impedenza?
   𝐼# = 𝑦## 𝑉# + 𝑦#( 𝑉(              𝑦##        𝑦#(
                                 𝑌 = 𝑦          𝑦((
                                      (#
   𝐼( = 𝑦(# 𝑉# + 𝑦(( 𝑉(


          1       𝑦(#                         𝑦#(      𝑦#( 𝑦(#
  𝑉( =       𝐼( −     𝑉       𝐼# = 𝑦## 𝑉# +       𝐼( −         𝑉
         𝑦((      𝑦(( #                       𝑦((       𝑦(( #

         𝑦#(            𝑦#( 𝑦(#                          𝑦((                 𝑦#(
  𝐼# −       𝐼( = 𝑦## −         𝑉#       𝑉# =                         𝐼# −       𝐼
         𝑦((             𝑦((                      𝑦## 𝑦(( − 𝑦#( 𝑦(#          𝑦(( (

         𝑦((      𝑦#(                                                 𝐷; = 𝑦## 𝑦(( − 𝑦#( 𝑦(#
    𝑉# =     𝐼# −     𝐼
         𝐷;       𝐷; (
                                        𝑧##     𝑧#(    La matrice impedenza esiste se la
           𝑦(#     𝑦##                  𝑧(#     𝑧((    matrice ammettenza non è singolare !
    𝑉( = −     𝐼 +     𝐼
           𝐷; # 𝐷; (
                                                       à se esistono, tutte le matrici sono
                                                         equivalenti !!
Passaggi tra matrici

    Possiamo passare da una
    matrice all’altra se le matrici
    non sono singolari


    à tabella di passaggio tra
    matrici disponibile sulla
    pagina e.learning del corso
                                                                          Tripolo
• I transistor sono dei tripoli
• Alcune considerazioni interessanti possono essere fatte per i tripoli
à I TRIPOLI SONO DEI DOPPI BIPOLI
• un terminale come ingresso
• un terminale come uscita
• un terminale comune


• Sul terminale comune scorre la somma di I1 e I2
• Fittiziamente sdoppiando il terminale comune, possiamo considerare che I1 si
  chiuda sulla porta di ingresso, mentre I2 si chiuda sulla porta di uscita
(è un «trucco» puramente matematico, ma ci mostra come i tripoli soddisfino la
condizione per essere considerati doppi bipoli)


à Possiamo descrivere i tripoli (transistor e circuiti che li impiegano) con le matrici 2x2
  che abbiamo appena visto
                                                𝑦## 𝑦#(         𝑦< 𝑦=
                                         𝑌 = 𝑦              = 𝑦 𝑦
                                                  (# 𝑦((         >   ?
                                            Generatori dipendenti
• Un tipico circuito che ha un ingresso e un’uscita è il generatore dipendente

es.: 𝑉@ = 𝐹 𝑉A ∀ 𝐼@ , 𝐼A

se F è una funzione non lineare la posso linearizzare à 𝑉@ = 𝑘 𝑉A

𝑉( = 𝑘 𝑉# à matrice ibrida «g» (𝑉( = 𝑔(# 𝑉# + 𝑔(( 𝐼( ) à 𝑔(# = 𝑘 ; 𝑔(( = 0

𝐼# = 𝑔## 𝑉# + 𝑔#( 𝐼( à se il generatore non assorbe corrente dalla porta di ingresso ho
ovviamente che 𝑔## = 𝑔#( = 0                     0 0
                                           𝑔 =
                                                𝑘 0


• 𝐼@ = 𝐹 𝑉A ∀ 𝑉@ , 𝐼A à 𝐼@ = 𝑦(# 𝑉A à 𝑦(# trans-conduttanza

• 𝑉@ = 𝐹 𝐼A ∀ 𝐼@ , 𝑉A à 𝑉@ = 𝑧(# 𝐼A à 𝑧(# trans-resistenza

• 𝐼@ = 𝐹 𝐼A ∀ 𝑉@ , 𝑉A à 𝐼@ = ℎ(# 𝐼A

Tutte queste matrici sono SINGOLARI à non esistono le altre matrici !!
                      Calcolo delle componenti matrici
Come si estrae la matrice descrittiva del circuito ? à metodo pratico e veloce che
deriva dalla definizione delle componenti

es.: estrazione della matrice ibrida «h»                                 ℎ

       𝑉+
  ℎ++ ≜ M                                                       𝑉# = ℎ## 𝐼# + ℎ#( 𝑉(
       𝐼+ > =*
             !
                                                                 𝐼( = ℎ(# 𝐼# + ℎ(( 𝑉(

       𝑉+
  ℎ+, ≜ M                                        +

       𝑉, ? =*                                   -
                                                        Metodo pratico che può
             "
                                                        essere utilizzato anche
                                                        sperimentalmente per
       𝐼,                                               misurare le componenti
  ℎ,+ ≜ M                                               della matrice
       𝐼+ > =*
             !
                                                        In presenza di effetti reattivi
       𝐼,                                               il calcolo va fatto nel dominio
  ℎ,, ≜ M                                         +     delle trasformate !!
       𝑉, ? =*                                    -
             "
              condizioni di funzionamento in cui una delle variabili indipendenti
              viene azzerata (mentre l’altra assume un valore arbitrario z 0)
                          Calcolo
                      Significato      delle componenti
                                  dei parametri di resistenza matrici
                                                              7


Se il circuito non ha effetti reattivi, posso fare il calcolo nel dominio del tempo
                 Significato
In maniera del tutto              dei parametri
                      analoga si possono     calcolare ledicomponenti
                                                              resistenza
                                                                       di qualunque matrice
                  v1                 v2
             r11
es: matrice impedenza          r21 ci sono
                         (se non             effetti reattivi à impedenza = resistenza)
                  i1 i 0              i1 i 0
                         2                     2


                    v1                  v2
              r                    r
           ¨ r1111 resistenza di ingresso
                                    21     a vuoto alla porta 1
                    i1 i 0               i1 i 0
           ¨ r21      resistenza
                          2      di trasferimento
                                               2  a vuoto dalla porta 1 alla porta 2

           ¨ r11 resistenza di ingresso a vuoto alla porta 1
                 Significato
                   v
                                   dei vparametri di conduttanza
           ¨ rr21 resistenza di trasferimento
                     2
                                  r      1    a vuoto dalla porta 1 alla porta 2
               22                     12
                       i2 i 0               i2 i 0
                    Significato dei parametri di conduttanza
                          1                    1


                      vi2                     vi1
es: matrice  r                           r
          ¨ ammettenza            (se   non
                                          12 ci 2a
                                                 sono effetti      reattivi  à ammettenza = conduttanza)
                         1
            rg222211 resistenza
                       iv2 i 0    di    g
                                     ingresso
                                          21  iv2 ivuoto    alla porta  2
                          1 v12 0                1 v12 00
          ¨ r12 resistenza        di trasferimento       a vuoto dalla porta 2 alla porta 1
                        i1                     i2
             g
          ¨ rg2211
                 11 resistenza          g                                                   8
                        v1 v 0 di di  ingresso v1a vvuoto    alla porta alla
                                                                        2 porta 1
                      conduttanza         21
                                         ingresso    in cortocircuito
                              2                    2    0
           ¨ rg1221 resistenza
                    conduttanzadi di
                                  trasferimento  a in
                                     trasferimento vuoto  dalla porta
                                                      cortocircuito   2 alla
                                                                    dalla    porta
                                                                          porta     1 porta 2
                                                                                1 alla
            ¨ g11 conduttanza di ingresso in cortocircuito alla porta 1                  8

                   i2
            ¨ g21 conduttanza           i1
                              di trasferimento in cortocircuito dalla porta 1 alla porta 2
               g 22                   g12
                       v2 v 0               v2 v 0
                              1                    1
                                Proprietà matrice ammettenza
• Consideriamo un tripolo (due porte) descritto dalla                         𝐼# = 𝑦< 𝑉# + 𝑦= 𝑉(
  matrice ammettenza
• Supponiamo di collegarlo a 3 componenti esterni come                        𝐼( = 𝑦> 𝑉# + 𝑦? 𝑉(
  nello schema:
                                                                          𝑦##       𝑦#(   𝑦<       𝑦=
                                                                      𝑌 = 𝑦         𝑦(( = 𝑦>       𝑦?
                                                                           (#
                                Y3
      I1’                                              I2’




            𝐼#6 = 𝐼# + 𝑌# 𝑉# + 𝑌7 𝑉# − 𝑉( = 𝑦< 𝑉# + 𝑦= 𝑉( + 𝑌# 𝑉# + 𝑌7 𝑉# − 𝑌7 𝑉(

            𝐼#6 = 𝑦< + 𝑌# + 𝑌7 𝑉# + 𝑦= − 𝑌7 𝑉( = 𝑦< ′𝑉# + 𝑦= ′𝑉(
                              Proprietà matrice ammettenza
                              Y3                                             𝐼# = 𝑦< 𝑉# + 𝑦= 𝑉(
        I1’                                          I2’                     𝐼( = 𝑦> 𝑉# + 𝑦? 𝑉(

                                                                         𝑦##       𝑦#(   𝑦<       𝑦=
                                                                     𝑌 = 𝑦         𝑦(( = 𝑦>       𝑦?
                                                                          (#




𝐼#6 = 𝑦< + 𝑌# + 𝑌7 𝑉# + 𝑦= − 𝑌7 𝑉( = 𝑦< ′𝑉# + 𝑦= ′𝑉(

𝐼(6 = 𝐼( + 𝑌( 𝑉( − 𝑌7 𝑉# − 𝑉( = 𝑦> 𝑉# + 𝑦? 𝑉( + 𝑌( 𝑉( − 𝑌7 𝑉# + 𝑌7 𝑉(

                                                           • L’ammettenza 𝑌# in parallelo alla porta
𝐼(6 = 𝑦> − 𝑌7 𝑉# + 𝑦? + 𝑌( + 𝑌7 𝑉( = 𝑦> ′𝑉# + 𝑦? ′𝑉(
                                                             1 si somma alla componente 𝑦$
                                                           • L’ammettenza 𝑌% in parallelo alla porta
      𝑦< ′ 𝑦= ′   𝑦< + 𝑌# + 𝑌7           𝑦= − 𝑌7             2 si somma alla componente 𝑦&
 𝑌′ =           =    𝑦> − 𝑌7          𝑦? + 𝑌( + 𝑌7
      𝑦> ′ 𝑦? ′
                                                           • L’ammettenza 𝑌' tra porta 1 e porta 2
                                                             si somma sulla diagonale principale e
ATTENZIONE: vale solo per la matrice ammettenza !!           si sottrae sull’altra diagonale
                                 Proprietà matrice impedenza
• Consideriamo un tripolo (due porte) descritto dalla                      𝑉# = 𝑧< 𝐼# + 𝑧= 𝐼(
  matrice impedenza
• Supponiamo di collegarlo a 3 componenti esterni come                     𝑉( = 𝑧> 𝐼# + 𝑧? 𝐼(
  nello schema:
                                                                        𝑧##    𝑧#(   𝑧<         𝑧=
                                                                    𝑍 = 𝑧      𝑧(( = 𝑧>         𝑧?
                                                                         (#



                    V1                   V2                     L’equazione di Kirchhoff per
     V1’                                               V2’      le correnti impone che su Z3
                                3                               scorre (I1 + I2)




   𝑉#6 = 𝑉# + 𝑍# 𝐼# + 𝑍7 𝐼# + 𝐼( = 𝑧< 𝐼# + 𝑧= 𝐼( + 𝑍# 𝐼# + 𝑍7 𝐼# + 𝑍7 𝐼(

   𝑉#6 = 𝑧< + 𝑍# + 𝑍7 𝐼# + 𝑧= + 𝑍7 𝐼( = 𝑧< ′𝐼# + 𝑧= ′𝐼(

  𝑉(6 = 𝑉( + 𝑍( 𝐼( + 𝑍7 𝐼# + 𝐼( = 𝑧> 𝐼# + 𝑧? 𝐼( + 𝑍( 𝐼( + 𝑍7 𝐼# + 𝑍7 𝐼(

   𝑉(6 = 𝑧> + 𝑍7 𝐼# + 𝑧? + 𝑍( + 𝑍7 𝐼( = 𝑧> ′𝐼# + 𝑧? ′𝐼(
                               Proprietà matrice impedenza
                                                                            𝑉# = 𝑧< 𝐼# + 𝑧= 𝐼(

                                                                            𝑉( = 𝑧> 𝐼# + 𝑧? 𝐼(
                    V1                 V2
      V1’                                           V2’                𝑧##      𝑧#(   𝑧<         𝑧=
                                                                   𝑍 = 𝑧        𝑧(( = 𝑧>         𝑧?
                               3                                        (#



                                                              L’equazione di Kirchhoff per
                                                              le correnti impone che su Z3
  𝑉#6 = 𝑧< + 𝑍# + 𝑍7 𝐼# + 𝑧= + 𝑍7 𝐼( = 𝑧< ′𝑉# + 𝑧= ′𝐼(        scorre (I1 + I2)
  𝑉(6 = 𝑧> + 𝑍7 𝐼# + 𝑧? + 𝑍( + 𝑍7 𝐼( = 𝑧> ′𝑉# + 𝑧? ′𝐼(

                                                         • L’impedenza 𝑍# in serie alla porta 1 si
        𝑧< ′ 𝑧= ′   𝑧< + 𝑍# + 𝑍7        𝑧= + 𝑍7            somma alla componente 𝑧$
   𝑍′ =           =    𝑧> + 𝑍7       𝑧? + 𝑍( + 𝑍7
        𝑧> ′ 𝑧? ′                                        • L’impedenza 𝑍% in serie alla porta 2 si
                                                           somma alla componente 𝑧&
                                                         • L’impedenza 𝑍' in serie al terminale
                                                           comune si somma su tutte le
ATTENZIONE: vale solo per la matrice impedenza !!          componenti della matrice
                                                                                      37

                                                  Circuiti equivalenti
        Circuiti equivalenti di doppi bipoli lineari
Le equazioni che descrivono il doppio bipolo al piccolo segnale (eventualmente nel
domino delle trasformate) possono essere associate a dei circuiti EQUIVALENTI
es.: matrice ammettenza
à I1 è la somma di due componenti di corrente                    𝐼# = 𝑦< 𝑉# + 𝑦= 𝑉(

à I2 è laMatrice
         somma dididue
                    resistenza
                       componenti di corrente                    𝐼( = 𝑦> 𝑉# + 𝑦? 𝑉(
à possono essere
            v1 r11viste
                    i1  r12come
                             i2 due componenti su
due rami in parallelo
            v2   r21i1  r22i2
             𝐼] = 𝑦l 𝑉] + 𝑦m 𝑉n


componente di corrente
sulla porta 1 dipendente
       Matrice   di conduttanza
dalla tensione sulla porta 1
à ammettenzai1 g11v1  g12 v2
                                             𝑦<     𝑦= 𝑣(          𝑦> 𝑣#    𝑦?
         i2 g 21di
     componente     g 22 v2
                v1 corrente
     sulla porta 1 dipendente
     dalla tensione sulla porta 2
     à generatore dipendente
 Circuiti equivalenti di doppi bipoli lineari
                                                                  Circuiti equivalenti
 Matricediimpedenza                                𝑧<            𝑧?
 Matrice   resistenza

         r11i1𝑧< 𝐼#r12+
    v1𝑉# =             i2 𝑧= 𝐼(
                                              𝑧= 𝑖(              𝑧> 𝑖#
    v2      r21i1  r22i2                                                             ATTENZIONE: SONO
        𝑉( = 𝑧> 𝐼# + 𝑧? 𝐼(                                                            CIRCUITI EQUIVALENTI
  Circuiti equivalenti di doppi bipoli lineari                                        à non hanno nulla a che
                                                                                        fare con il circuito
                                                                                        reale !!
 Matricediibrida
Matrice          «h»
           conduttanza                                                                à E’ un modello
        Matrice H
                H                              ℎ##
    i gMatrice
    1     v g v
            11 1       12 2
                                                                                        matematico !!
        𝑉v# =hℎi##𝐼#h +v ℎ#( 𝑉(                                                      à per ogni matrice ho
   i2 v11 g 21hv11
                 11  11 
                  1 i    gh2212
                               vv2 22
                              12
                                                                         ℎ%%            ricavato un circuito
      𝐼ii(22 =hh21  i11 𝐼 hh22
                ℎ21i(#         +vv22ℎ(( 𝑉(
                           # 22                                                         equivalente
                                                                                      à Diversi circuiti per lo
                                                                                 38     stesso componente !!
 Matrice ibridaHc«g»                                                                  à Sono tutti equivalenti !
       Matrice                                                        𝑔%%

             c v11  h12
        i11 h11       ci
        𝐼# =11𝑔##   𝑉#12+22 𝑔#( 𝐼(           𝑔##        𝑔!" 𝑖"           𝑔%#𝑣#
               c        c
              21v11  h22
        v22 h21         22 i22
        𝑉( = 𝑔(# 𝑉# + 𝑔(( 𝐼(
                                                                      Circuito a p
   E’ di nostro interesse anche il seguente circuito (tripolo)

co                      𝑌'
                                                        • L’ammettenza 𝑌# in parallelo alla porta 1
                                                        • L’ammettenza 𝑌% in parallelo alla porta 2
             𝑌#         𝑔( 𝑣#             𝑌%            • L’ammettenza 𝑌' fa da ponte tra porta 1
                                                          e porta 2
                                                        à conviene descriverlo con matrice Y


   Oltre a 𝑌# , 𝑌( e 𝑌7 , l’unico altro componente è un
                                                     41 generatore dipendente (I = gmV1)
   à matrice |Y|                 0    0
                          𝑌 =
                                𝑔B    0
esentazione dei doppi bipoli                                        𝑌7 = −𝑦= ′
   à matrice completa |Y’|
                                                                    𝑌# = 𝑦<6 + 𝑦= ′
zione comandata in corrente
          𝑦< ′ 𝑦= ′   𝑌 + 𝑌7           −𝑌7                          𝑌( = 𝑦?6 + 𝑦= ′
     𝑌′ =           = #
          𝑦> ′ 𝑦? ′  𝑔B − 𝑌7         𝑌( + 𝑌7
mato da componenti resistivi lineari e                              𝑔B = 𝑦>6 − 𝑦= ′
 denti
iti equivalenti di doppi bipoli lineariCircuito a p
                                                          𝑌7 = −𝑦= ′
           𝑦< ′ 𝑦= ′   𝑌# + 𝑌7    𝑌7
      𝑌′ =Circuiti = equivalenti
           𝑦> ′ 𝑦? ′   𝑔B − 𝑌7 𝑌( +a𝑌7Ȇ                   𝑌# = 𝑦<6 + 𝑦= ′

polo reciproco                                             𝑌( = 𝑦?6 + 𝑦= ′

                                                          𝑔B = 𝑦>6 − 𝑦= ′
 v  g12 v2
1 1

 v g v     2 matrice |Y| è possibile rappresentarla con un circuito a p
12 1 Data22una




lo non reciproco                          − 𝑦* ′

 v  g12 v2
1 1
                           𝑦$) + 𝑦* ′   (𝑦+) − 𝑦* ′)𝑣$     𝑦&) + 𝑦* ′
 v  g 22 v2
1 1




                                                                        41
