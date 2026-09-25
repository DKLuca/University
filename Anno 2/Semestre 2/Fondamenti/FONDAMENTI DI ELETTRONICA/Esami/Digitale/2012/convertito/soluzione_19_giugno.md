---
fonte: "soluzione_19_giugno.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione del compito di Fondamenti di Elettronica
                                 19 giugno 2012
                                  parte digitale
1. il modo piú semplice di procedere é scrivere F in funzione di A, B, C, cioé: F = A B + C. Nel
   pull-up abbiamo quindi un pMOS pilotato da C in parallelo alla serie di due pMOS pilotati da A e
   B. Il pull-down é il duale, quindi un nMOS pilotato da C in serie al parallelo di due nMOS pilotati
   da A e B.

2. Nel caso peggiore il transitorio da salita avviene tramite la serie dei transistori pMOS pilotati da
   A e B, quindi con un Seq = Sp /2. Il ritardo al 90% é dato da:

                                      2CL                      4CL
                           τr =               F (VT /VDD ) = 0        F (VT /VDD )                   (1)
                                  βp0 Seq VDD               βp Sp VDD

   che invertita e sostituendo i valori numerici fornisce S p =4.6.
   Il transitorio di discesa di caso paggiore avviene attraverso la serie del nMOS pilotato da C ed uno
   dei due nMOS pilotati da A e B, quindi S eq = Sn /2. Essendo del tutto equivalente al caso del
   dimensionamento dei pMOS, basta considerare che β n0 = 2βp0 , quindi Sn = Sp /2=2.3.

3. ogni ingresso (A, B o C) va sul gate di un nMOS e di un pMOS, quindi

                                  Cin = (Sn + Sp )(L2M IN Cox + 2CGSO LM IN )                        (2)

   Sostituendo i valori numerici si ottiene C in =3.7fF.

4. Il modo piú semplice é cercare S eq per ogni configurazione e quindi in base al rapporto tra questo
   e quello di caso peggiore (Sp /2 o Sn /2) sappiamo quanto il tempo sará pi´ corto dei 300ps del caso
   peggiore. Il tutto si puó riassumere in una tabella:
     A B C                     Seq     τ [ps]
     0 0 0 discesa (2/3)Sn              225
     0 0 1        salita       Sp       150
     0 1 0 discesa           0.5Sn      300
     0 1 1        salita       Sp       150
     1 0 0 discesa           0.5Sn      300
     1 0 1        salita       Sp       150
     1 1 0        salita     0.5Sp      300
     1 1 1        salita     1.5Sp      100

5. La potenza dinamica é pari a:
                                                     2
                                             P = CL VDD fc P0→1                                      (3)
   dato che nella tabella della varitá abbiamo 5 ’1’ e 3 ’0’, P 0→1 = (3/8)(5/8) = 15/64. Sostituendo i
   valori numerici, si trova P =13.7µW.
