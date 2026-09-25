---
fonte: "esame_svolto08_09_14.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Prova Teoria dei Segnali e Comunicazioni Elettriche                                                      A.A. 2013/2014
laurea triennale

Cognome e Nome                                                                               Matricola


Esercizi

   1. Calcolare l’area e l’energia del segnale a tempo discreto x(kT ) = ( 1)k e 2|k|T , kT 2 Z(T ).

   2. Calcolare la trasformata di Fourier del segnale a tempo continuo
                                            +1
                                            X                           ✓                    ◆
                                                       |k|          2       t + (k + 0.5)T
                                   x(t) =          2         sinc                                .
                                            k= 1
                                                                                   T

   3. Si consideri un processo aletorio stazionario gaussiano a tempo discreto a(kT ) a simboli indipen-
      denti con media nulla e varianza unitaria. Il processo viene filtrato con un filtro con funzione di
      trasferimento Hz (z) = T /(1 0.1 z 1 ). Calcolare la potenza del processo di uscita.

   4. Si consideri un sistema di trasmissione in quadratura. I segnali di ingresso x1 (t) e x2 (t) nei canali
      in fase (canale 1) e in quadratura (canale 2) sono modellati come processi aleatori stazionari a
      media nulla con densità spettrale Rx (f ) = R0 triangle(f T ). Si suppongano i filtri di trasmissione
      e ricezione ideali, con guadagno AT = AR = A, e un mezzo trasmissivo che determina una
      attenuazione AM , con A2 AM = 2. Si supponga che le portanti in ricezione abbia un errore di
      fase     rispetto alle portanti in trasmissione. In ciascuno dei due canali, ad esempio il canale 1, si
      identifichi il segnale utile su (t) come la componente del segnale ricevuto proporzionale al segnale
      trasmesso x1 (t), e la distorsione d(t) come la componente del segnale ricevuto proporzionale al
      segnale x2 (t). Sia inoltre nr (t) la componente del segnale ricevuto dovuta al rumore. Calcolare
      il rapporto segnale rumore complessivo

                                                         E[s2u (t)]
                                             ⇤=                           .
                                                   E[d2 (t)] + E[n2r (t)]

   5. In un sistema PAM con simboli a(kT ) 2 {0, ±1}, P[a(kT ) = 1]=P[a(kT ) = 1], P[a(kT ) =
      0]=1/2, l’impulso in trasmissione g(t) e la risposta impulsiva dell’amplificatore di ricezione h(t)
      hanno, rispettivamente, un andamento in frequenza a radice di coseno rialzato, con fattore di
      roll-o↵ pari a ↵ = 0.2, mentre il mezzo trasmissivo introduce un’attenuazione costante AM . Sia
      G(0) = V0 T e H(0) = AR . Anche se i simboli non sono equiprobabili, l’elemento di decisione
      è a soglia con soglia a metà dei simboli ricevuti in assenza di rumore. Il rumore all’ingres-
      so dell’amplificatore di ricezione è gaussiano, bianco, con densità spettrale R0 . Calcolare la
      probabilità di errore del sistema.
