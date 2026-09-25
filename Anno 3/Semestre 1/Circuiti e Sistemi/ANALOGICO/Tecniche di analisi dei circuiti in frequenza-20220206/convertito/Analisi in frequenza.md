---
fonte: "Analisi in frequenza.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

UNIVERSITY OF UDINE

Department DIEG
Via delle scienze 206
33100 Udine (UD), Italy




                      ANALISI IN FREQUENZA
                      Stefano Saggini
                      Complementi di circuiti e sistemi
Introduction
¨   Calculus of
    ¤ Voltage or current gain
    ¤ Impedance or transimpedance

    ¤ Conductance or transconductance

                            C1     Ck

          Vin(s)   Iin(s)                    Iout(s)   Vout(s)


                             Network




                            Ck+1        Cn
Soluzione del problema
¨ Calcolo della funzione di trasferimento tramite la
  soluzione del circuito lineare ottenuto sostituendo
  alle capacità la loro impedenza ZCk=1/(s Ck)
¨ Tecnica semplificata che cerca di determinare la

  funzione di trasferimento attraverso le proprietà.
                            NZ


              Y (s)
                            ∏ (1+ sτ )
                                    zi
                    = G(0) Ni=1
              U (s)           P

                            ∏ (1+ sτ )
                                    pj
                            j=1
Determinazione di NP
¨   Nel caso ci siano solo capacità nello schema il
    numero di poli è dato dal numero di capacità
    indipendenti (le loro tensioni non sono vincolate da
    generatori di tensioni pilotati e ne da equazioni di
    maglia con altre capacità)
                                C1     Ck

              Vin(s)   Iin(s)                    Iout(s) Vout(s)


                                 Network




                                Ck+1        Cn
  Determinazione di NZ
  ¨      Se per s è∞ il trasferimento è ≠ da 0 allora
         NZ=NP

                      x      Tensione sulle capacità
                      C1          Ck                              ⎧ x! = x A + B u
         u                                             y          ⎨
Vin(s)       Iin(s)                         Iout(s)   Vout(s)     ⎩y = x C + D u

                          Network                               Y (s)
                                                                      = C(sI − A)−1 B + D
                                                                X (s)


                      Ck+1             Cn
     Cancellazione poli zeri
     ¨        Caso di non osservabilità delle variabili di stato
         Considerando la funzione Zin                      C
         la capacità C è non osservabile

                             Zin




     ¨        Caso di non raggiungibilità delle variabili di stato
                 R1
                                      Considerando la funzione amplificazione di tensione
                                      Av c’è solo una variabile di stato e se
                             C2              C2 R1        La variabile è osservabile ma non
         C1
Vin(s)          R2                             =          raggiungibile
                                   Vout(s)   C1 R2
   Determinazione di alcuni zeri
   ¨      Certe configurazioni circuitali portano sempre degli
          zeri
Vin(s)    Iin(s)                                 Iout(s)   Vout(s)

                                   R
                     Network           Network                       τ z = RC
                                   C

                               R
 Vin(s)     Iin(s)                               Iout(s)   Vout(s)


                                       Network                       τ z = RC
                     Network   C
Capacità interagenti
¨   Le capacità Ci e Cj sono interagenti se la tensione
    VCi influenza la corrente di carica ICj e viceversa.

⎧ x! = x A + B u                Esempio
⎨
⎩y = x C + D u                  C1 e C2
                                                        C2
In altre parole i termini       Non sono interagenti


aij ≠ 0        e     a ji ≠ 0


                                                   C1
Proprietà
¨   I poli delle capacità non interagenti possono essere
    calcolate indipendentemente l’una dall’altra.


                                   τ p1 = R1C1
                      R2      C2

                                   τ p2 = R2C2


         Iin(s) R
                  1
                       C1
Metodo delle costanti di tempo
¨   Considerando una rete con capacità indipendenti e
    interagenti
                  NP         NP

                 ∑τ = ∑ RʹC
                        pi         i   i
                  i=1        i=1
                  NP         NP
                              1
                 ∑ω pi = ∑ RʹʹC
                 i=1     i=1 i i

Dove τi (ωi =1/τi) sono le costanti di tempo della rete e Ri’ sono le
resistenze calcolate ai morsetti di connessione delle capacità Ci con le
altre capacità scollegate e Ri’’ sono le resistenze calcolate ai morsetti
di connessione delle capacità Ci con le atre capacità cortocircuitate
Miller Theorem
The impedance Z(s) connected between V1 e V2 can be
  substituted with two impedances:
¨ Z'(s) connected between V1 and ground

¨ Z"(s) connected between V2 and ground

                                          Z(s)
            Z (s)
  Z ʹ( s ) =
          1 − K (s)
           K (s)Z (s)        V1          K(s)             V2
  Z (s) =
   ʹʹ
           1 − K (s)
          V2 ( s )
  K (s) =
          V1 ( s )           V1 Z’(s)    K(s)     Z’’(s   V2
                                                  )
