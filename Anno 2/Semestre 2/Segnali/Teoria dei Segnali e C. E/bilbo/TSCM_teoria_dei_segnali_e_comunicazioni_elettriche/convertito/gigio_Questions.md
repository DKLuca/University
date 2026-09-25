---
fonte: "gigio_Questions.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Comunicazioni Elettriche

      Analisi spettrale nei filtri: densità spettrale dell’uscita y(t) di un filtro con risposta in frequenza H(f ) e ingresso
  x(t), processo aleatorio stazionario con densità spettrale Rx(f ). Derivazione del risultato nel caso x(t) sia un processo
  a tempo continuo.


    Supponiamo x(t) processo aleatorio stazionario in senso lato con media mx , correlazione rx (t) e densità spettrale Rx (f )
allora abbiamo y(t) stazionario in senso lato con
                                                x(t)                   y(t)
                                                           h(t)

   • my = mx area[ h(t))] = mx · H(0)
   • Ry (f ) = Rx (f ) · |H(f )|2 = Rx (f )H(f ) · H ∗ (f )
Calcoliamo la correlazione mutua tra uscita ed ingresso
                             Z                              Z                                Z
     E[y(t + τ ) · x(t)] = E    dτ1 x(τ1 )h(t + τ − τ1 )x(t) = E [x(τ1 )x(τ )] h(t + τ − τ1 ) = rx (t − τ1 )h(t + τ − τ1 )
                           Z I                                 I                                I

                         = dτ1 rx (τ1 )h(τ − τ1 ) = rx ∗ h(τ )
                               I

Calcoliamo la correlazione della uscita
                                  Z                     Z                                   Z
 E [y(t + τ ) · y(t)] = E y(t + τ ) dτ1 x(τ1 )h(t − τ1 ) = dτ1 h(τ1 )E [y(t + τ )x(t − τ1 )] = dτ1 h(τ1 )ryx (t + τ − t + τ1 )
                                    I                      I                                   I
                        Z                        Z
                      = dτ1 h(τ1 )ryx (τ + τ1 ) = h(−τ1 )ryx (τ − τ1 ) = h ∗ ryx (τ )
                           I                                    I

Calcoliamo la media
                  Z                  Z
     E [y(t)] = E    x(τ1 )h(t − τ1 ) = dτ1 h(τ − τ1 )E [x(τ1 )] = mx area h(t) = mx · H(0)
                       I                             I

    Riassumendo il processo di uscita di un filtro con ingresso stazionario risulta anch’esso stazionario in senso lato quindi
ry (τ ) dipende solamente dalla differenza dei tempi.


      Analisi spettrale nei filtri interpolatori Z(T ) → R con ingresso stazionario. Calcolare la densità spettrale media
  dell’uscita x(t), t ∈ R, di un filtro interpolatore Z(T ) → R con risposta impulsiva

                                                              h(t) = −triangle(t/T ) t ∈ R.

  e ingresso un processo aleatorio a simboli indipendenti ed equiprobabili a(kT ) ∈ {0, 1}.


   Sia a(kT ) processo aleatoria a tempo discreto, stazionario in senso lato con media ma e correlazione ra (ht).
Al uscita del filtro interpolatore otteniamo un processo aleatorio ciclostazionario in senso lato con periodo T
                                               a(kT )      x           x(t)
                                                          1
                                                          T g(t)

                   +∞
                   X                                                    ∞
                                                                        X
      mx (t) = T           E[a(kt)]g(t − KT ) = ma T                        g(t − KT )
                   k=−∞                                             k=−∞
                                                                    |        {z         }
                                                                    periodicizzazione in T
                                                          +∞
                                                          X                                  +∞
                                                                                             X
      rx (t, t + τ ) = E[x(t + τ )x(t)] = T · T                  E[a(kT )]g(t − kt)                 E[a(hT )]g(t + τ − hT )
                                                         k=−∞                                h=−∞
                                   +∞
                                   X                     +∞
                                                         X
                   = m2a T 2            g(t − kT )              g(t + τ − hT )
                               k=−∞                  h=−∞
                               |                         {z                       }
                                           periodicizzazione in T

Dove abbiamo dimostrato che l’uscita x(t) è un processo ciclostazionario di periodo T .



                                                                                  1
Possiamo definire quindi due nuove grandezze, quali media periodica
                   Z Tp
              1
      m̃x =               mx (t) dt
              Tp    0

e la correlazione media
                   Z Tp                       Z Tp
                 1                          1
      r¯x (τ ) =        rx (t, t + τ ) dt =        Mx (t) dt
                 Tp 0                       Tp 0

Mentre la densità spettrale media non è altro che la trasformata di Fourier della correlazione media

                                                              R¯x (f ) = F [r¯x (τ )]

Nel caso di filtri interpolatori possiamo dimostrare anche che
   • m̄x = ma · area[h(t)] = ma · H(0)

   • R̄x (f ) = Ra (f ) · |H(f )|2
Con Ra periodica di periodo 1/T e H(f ) non periodica.



      Analisi spettrale nella modulazione. Sia x(t), t ∈ R, un processo aleatorio stazionario e y(t) = x(t) cos(2πf0 t + φ0 ),
  con φ0 costante. Dire se y(t) è stazionario in senso lato o ciclostazionario in senso lato e calcolarne la densità spettrale
  (eventualmente media).
      Sia invece z(t) = x(t)cos(2πf0 t + φ + φ0 ), con φ v.a. uniforme in [0, 2π) indipendente da x(t) e φ0 costante. Dire se
  z(t) è stazionario in senso lato o ciclostazionario in senso lato e calcolarne la densità spettrale (eventualmente media).



   Se x(t) è un processo aleatorio stazionario in senso lato e y(t) è dato dalla relazione

      y(t) = x(t) cos(2πf0 t + φ) φ ∈ U(0, 2π)

Allora y(t) risulta essere stazionario in senso lato

          E[y(t)] = E[x(t) · cos(2πf0 t + φ)] = mx E[cos(2πf0 t + φ)] = 0
                     Z +∞                            Z 2π
                                                           1
E[cos(2πf0 t + φ)] =      cos(2πf0 t + a)fa (a) da =         cos(2πf0 t + φ) da = 0           integrale di un coseno in un periodo
                      −∞                              0   2π
    E[y(t + τ )y(t)] = E[x(t + τ ) · x(t) cos(2πf0 (t + τ ) + φ) · cos(2πf0 t + φ)
                                   1                 1                             1
                     = rx (τ ) · E[ cos(2πf0 τ ) + cos(2πf0 2t + 2πf0 τ + 2φ) ] = rx (τ ) cos(2πf0 t) = ry (τ )
                                   2                |2             {z            } 2
                                                       integrale conseno in due periodi = 0

In generale possiamo dire che, dato un processo aleatorio ciclostazionario in senso lato con periodo Tp , il processo di
uscita dalla modulazione risulta stazionario in senso lato e

      y(t) = x(t + θ)       con       θ ∈ U(0, Tp )

e y(t) è indipendente dal processo x(t). Inoltre osserviamo che

   • my = m̃x
   • ry (τ ) = r̃x (τ )
Quindi per y(t) = x(t) cos(2πf0 t+φ) è un processo ciclostazionario , mentre y(t) = x(t) cos(2πf0 t+φ+φ0 ) è un processo
stazionario in senso lato e la sua densità spettrale vale
                                1
      Rx (f ) = F[ry (τ )] =      Rx (f ) · cos(2πf0 t + φ)
                                2



     Dare la definizione di processo ciclostazionario in media e in correlazione, e definire la densità spettrale media.
  Dire se il processo y(t) = x(t)V0 cos(2πf0 t) , con V0 v.a. Uniforme in [−V, V ] e f0 costante, è ciclostazionario in media



                                                                        2
  e in correlazione: nel caso di ciclostazionarietà , calcolare la densità spettrale media del processo.



    Un processo x(t) aleatorio si dice ciclostazionario in senso lato con periodo Tp se sono verificate contemporaneamente
le due condizioni con periodo T0 soddisfa le seguenti relazioni.

   • mx (t + Tp ) = mx (t)
   • rx (t, t + τ ) = rx (t + Tp , t + τ + Tp )

Dato che la correlazione è periodica di periodo Tp allora possiamo andare a definire la correlazione media come
                         Z Tp                              Z Tp
                    1                                 1
       r¯x (τ ) =               rx (t, t + τ ) dt =               Mx (t) dt
                    Tp    0                           Tp    0

Mentre la densità spettrale media non è altro che la trasformata di Fourier della correlazione media

       R¯x (f ) = F [r¯x (τ )]

Andando a calcolare la media di x(t) otteniamo

       my (t) = E[x(t)] cos(2πf0 t)

Mentre la correlazione
       ry (t, t + Tp ) = E[x(t + Tp ) cos(2πf0 t + Tp ) x(t) cos(2πf0 t + Tp )] = E[x(t)2 ]cos(2πf0 t + Tp ) cos(2πf0 t)
                         Mx
                       =    [cos(2πf0 (2t + Tp )) + cos(2πf0 Tp )]
                          2
Applicando la definizione otteniamo
                         Z Tp
                    1
       r˜x (τ ) =               rx (t, t + τ ) dt
                    Tp    0
                         Z Tp
                1               Mx                                             Mx
              =                    [cos(2πf0 (2t + Tp )) + cos(2πf0 Tp )] dt =    · cos(2πf0 Tp )
                Tp        0      2                                              2

La densità spettrale media è
                                     Mx
       R̃x (f ) = F[r̃x (τ )] =         · cos(2πf0 Tp )δR/Z(Tp )
                                      2



       Rumore termico e calcolo simbolico per l’analisi spettrale nelle reti elettriche.



   In un sistema di telecomunicazioni ci sono tre tipi di rumore ineliminabili

   • rumore termico
   • rumore shot
   • rumore flicker

Nel caso del rumore termico un buon modello presuppone che abbia caratteristiche di tipo gaussiano. Questo tipo di
rumore è causato dal moto degli elettroni al interno dei mezzi trasmissivi i quali hanno velocità costante a tratti. Quindi
ogni resistore è sede di rumore termico ed è modellabile nel seguente modo.

                                                                         Rv (f ) = 2kT R

dove
   • k costante di Boltzman
   • T temperatura ambiente




                                                                               3
Maggiore è la temperatura più velocemente si muovono gli elettroni ma a parità di condizioni c’è stazionarietà Rv (f ) ⇒
rumore bianco gaussiano Il rumore bianco gaussiano a tempo continuo è inaccettabile dal punto di vista fisico poiché
presuppone una potenza infinita, in conpenso nostri sistemi di applicazioni usuali si trovano in una banda tale che Rv (f )
è costante.
Modelliamo il nostro conduttore rumoroso come due possibili circuiti equivalenti

                                                    rv (τ )                          v(t + τ ) v(τ )
                                        ri (τ ) =       2
                                                            = E[i(t + τ )i(τ )] = E[          ·      ]
                                                     R                                  R       R
Solamente i vari componenti resistivi sono sede di rumore.
Se i vari componenti sono alla stessa temperatura possiamo applicare il teorema di Nyquist, il quale dice che trovata
l’inpedenza equivalente

      Z(f ) = R(f ) + jI(f )

La densità spettrale del rumore sarà pari a

      Rv (f ) = 2kT · R(f )

Se invece le temperature sono diverse avremmo che v1 (t) e v2 (t) sono due processi aleatori indipendenti e stazionari
singolarmente quindi ⇒ sono congiuntamente stazionari in senso lato con correlazione mutua e densità spettrale mutua
uguali a zero. Sapendo che la tensione in uscita vu (t)è combinazione lineare delle tensioni v1 , v2 opportunamente filtrate
dalla risposta in frequenza della rete.
                                                   vu (t) = y1 (t) + y2 (t)
Avendo supposto che v1 e v2 sono congiuntamente stazionari in senso lato

      E[vu (t + τ )vu (τ )] = E[(y1 (t + τ ) + y2 (t + τ ) · (y1 (t) + y2 (t))]
                           = E[y1 (t + τ )y1 (t)] + E[y2 (t + τ )y2 (t)] + E[y1 (t + τ )y2 (t)] + E[y2 (t + τ )y1 (t)]

   Otteniamo

      Rvu (f ) = |H1 (f )|2 Rv1 (f ) + |H2 (f )|2 Rv2 (f ) + H1 (f )H2∗ (f )Rv1 v2 (f ) + H2 (f )H1∗ (f )Rv2 v1 (f )

Dato che sono indipendenti sono anche incorrelati le gli ultimi due termini si annullano.
Usando il calcolo simbolico
     (
       Vu = H1 (f )V1 + H2 (f )V2
       Vu · Vu∗ = |H1 (f )|2 V1 V1∗ + |H2 (f )|2 V2 V2∗ + H1 (f )H2∗ V1 V2∗ + H2 (f )H1∗ (f )V1∗ V2




      Modulazione DSB: derivazione esplicita del rapporto segnale/rumore complessivo, con dimostrazione dei risultati.


    Supponiamo che il nostro segnale s(t) sia un processo aleatorio stazionario in senso lato limitato in banda con banda
B, allora è facile dimostrare che il filtro Q(f ) è irrilevante in quanto l’uscita è uguale al ingresso con probabilità 1. In
altre parole ingresso e uscita sono uguali in media quadratica
      E[(s1 (t) − s(t))2 ] = 0
Successivamente il segnale vine moltiplicato per la portante dove otteniamo sm (t) uguale a
      sm (t) = s1 (t) cos(2πf0 t + φ)
In seguito sm viene ”filtrato” tramite l’amplificatore di trasmissione HT il quale è costruito in modo tale da non modificare
la banda andando ad amplificare soltanto il segnale di un fattore AT
      sm1 (t) = s1 (t)AT cos(2πf0 t + φ)
Il mezzo trasmissivo è supposto come un filtro a densità spettrale costante quindi non va a modificare la banda del segnale
      sm2 (t) = s1 (t)AT AM cos(2πf0 t + φ)
In uscita al mezzo trasmissivo nel diagramma a blocchi troviamo il rumore n(t), il quale è additivo; dato che vale la
sovrapposizione degli effetti possiamo analizzare separatamente segnale e rumore.
In uscita al nostro amplificatore di ricezione troviamo
      sm3 (t) = s1 AT AM AR cos(2πf0 t + φ)



                                                                       4
Per recuperare il segnale trasmesso dobbiamo andare a demodulare il segnale ricevuto sm3 andandolo a moltiplicare per
la portante e filtrare il risultato con un filtro di tipo passa-basso Q(f ) simile a quello in ingresso
                 1                                    1                 1
     s̃1 (t) =     AT AR AM s1 (t) cos2 (2πf0 t + φ) = AT AM AR s1 (t) + AT AM AR s1 (t) cos(4πf0 t + 2φ)
                 2                                    2                 2
La potenza del segnale ricevuto è calcolabile come
                    1 2 2 2
     E[s̃2 (t)] =    A A A · Ms
                    4 T M R
Per l’analisi del rumore, supponiamo un rumore bianco con densità spettrale Rn (f ) = R0 = costante. Andando a calcolare
la densità spettrale della componente rumorosa all’uscita del filtro HR

     Rn1 (f ) = |HR (f )|2 · Rn (f )

Otteniamo cosı̀
                                                                 1
                                            Mñ = E[ñ2 (t)] = 2B A2R R0 = BR0 A2R
                                                                 2
E il rapporto segnale rumore diventa
                                                       E[s̃2 (t)]   1/4A2T A2M A2R Ms
                                               Λ=                 =
                                                       E[ñ2 (t)]       BR0 A2R
La potenza trasmessa è uguale a
                                                            Z ∞
                                                                               1        1
                                 Mv = MT = E[v 2 (t)] =          Rv (f ) df = 2 A2T Ms = A2T Ms
                                                              −∞               4        2

Definiamo inoltre il rapporto segnale rumore convenzionale Λc che è la differenza tra la potenza del segnale prima
dell’amplificatore di ricezione e la potenza del rumore nella banda del segnale in banda base B che è 2BR0 perché il
segnale ha lunghezza di banda 2B
                                                          Mr      A2 M T
                                               Λ = Λc =         = M
                                                         2R0 B    2R0 B



       Si disegni lo schema di un sistema di modulazione SSB . Si calcolino il rapporto segnale/rumore complessivo e
  l’efficienza del sistema, giustificando i risultati.


          s(t)
                        Q(f )                HT (f )            HM (f )                   HR (f )            Q(f )        s̃(t) + ñ(t)

                                         cos(2πf0 t + φ)                           n(t)                 cos(2πf0 t + φ)
Nei sistemi a SSB abbiamo
   • Banda richiesta B
   • Efficienza unitaria Λ = Λc
   • L’amplificatore di ricezione HT è critico da realizzare, poiché la banda di trasmissione è molto stretta
Quindi avremo
     
              1
     s̃(t) = 4 AT AM AR s(t)
     
              1
       Ms̃ = 16 A2T A2M A2R MS
       Mñ = 2B 14 R0 A2R = 12 BR0 A2R
     
     

Il rapporto segnale rumore Λ

           1/16A2T A2M A2R MS   1/4A2T A2M MS
     Λ=                       =
              1/2BR0 A2R           2BR0

Mentre la potenza trasmessa MT

             MR   A2 M T
     Λc =        = M     =Λ
            2BR0   2BR0




                                                                  5
     La formula di Carson nella modulazione di argomento



   Formule di Carson per la modulazione di Fase
   • ∆Φ = max|∆φv (t)| = maxKΦ |x(t)|

   • Bv ≈ 2B(1 + ∆Φ)
Formule di Carson per la modulazione di frequenza
   • ∆F = max|∆fv (t)| = maxKF |x(t)|
   • Bv ≈ 2(B + ∆F )



      Definire l’interferenza di intersimbolo in un sistema di trasmissione numerica PAM. Enunciare e dimostrare il
  criterio di Nyquist per l’assenza di interferenza di intersimbolo. Dire se l’impulso

                                                               c(t) = c0 sinc3 (t/(2T ))

  è un impulso di Nyquist per una trasmissione a 1/T simboli/s, giustificando la risposta.



    In telecomunicazioni con interferenza intersimbolica (ISI) si intende un particolare fenomeno indesiderato che si mani-
festa nei ricevitori degli apparati di trasmissione digitale sulla base del quale i simboli o forme d’onda analogiche trasmesse
in sequenza sul canale di comunicazione ad onde continue si sovrappongono temporalmente e parzialmente tra di loro
producendo una distorsione del simbolo in questione con degrado della qualità dell’informazione


      a(kT )              x         v(t)                                                                                             ã(kT )
                     1
                     T g(t)                   l(t)                         h(t)                                   Elem di decisione
                                                                                                    y
          Z(T )                      R                                                   R               Z(T )
                                                n(t)
Dove assumiamo che ak sia a simboli equiporbabili con alfabeto binacito M-ario, v(t) corrisponde a
                 +∞
                 X
     v(t) =               ak g(t − kT )
                k=−∞

Possiamo ora definire un impulso equivalente tale che c(t) = g ∗ l ∗ h(t)

                                                     a(kT )           x           v(t)                 ã(kT )
                                                                     1
                                                                     T c(t)
                                                                                             y
                                                            Z(T )                 R                 Z(T )

                   +∞
                   X
     vR (t) =                 ah c(t − hT )
                 h=−∞

Per semplificare ulteriormente lo schema possiamo considerare il semplice filtro equivalente


                                                      a(kT )          x               vRk (t)
                                                                     1
                                                                     T c(kT)
                                                             Z(T )                  R

Dove c(KT ) è la versione campionata del impulso equivalente quindi in questo caso possiamo scrivere
                                   +∞
                                   X
     vRK = ak · c(0) +                   ah · c(kT − hT )     con h 6= k
                                  h=−∞
                      0
              = ak V0 + i.s.i.
          0                                                                                     0
Dove ak V0 è la componente proporzionale al campione trasmesso, con V0 ampiezza dell’impulso equivalente nell’origine.
Per eliminare l’i.s.i. Dobbiamo avere un segnale che rende i campioni c(kT − hT ) più piccoli possibili con k 6= h



                                                                              6
   Prima del elemento di decisione avremo
                     ∞
                0    X
     rk = ak V0 +          ah ck−h + nk
                    h=−∞




                                                                                      0
                                                             
                                          c(t)               y               ck = V0 T δ(kT )
                                                     R               Z(T )


   Con c(t) ad estensione (−T, T ) quindi C(f ) ha banda infinita. È sufficiente che i campioni nei multipli di T salvo
quello nell’ origine, siano nulli.
Nel dominio del tempo                                  ( 0
                                                        V0 per k = 0
                                              c(KT ) =
                                                        0     altrimenti
Nel dominio della frequenza
                                                 ∞
                                                 X           k       0
                                                     C(f −     ) = V0 T      costante
                                                             T
                                             k=−∞

In particolare c(t) deve essere un impulso di Nyquist per non dare ISI, l’impulso di Nyquist a banda minima ha banda
pari a
                                                    1
                                             B=           Frequenza di Nyquist
                                                   2T
In un sistema reale il campinatore può commetter errori nel periodo di simbolo detto errore di gitter introducendo inter-
ferenza di intersimbolo. Perciò si possono utilizzare impulsi con caratteristiche migliori detti Impulsi a smorzamento
rapido. Preso C(f ) continuo fino alla derivata di ordine k − 1 e ha derivata kesima discontinua allora c(t) tende a zero
per t → ∞ come 1/tk+1



     Modulazione numerica in banda passante QAM: schema del sistema e valutazione della occupazione di banda
  minima, in Hz, per la trasmissione, con un sistema 16-QAM, di un flusso dati di 320 kbit/s.




     s̃n1 (t) = AT AM AR [s1 (t) cos(2πf0 t + φ) + s2 (t) sin(2πf0 t + φ)] cos(2πf0 t + φ + ∆φ)
                1
              = AT AM AR [s1 (t) cos(∆φ) + s1 (t) cos(4πf0 t + 2φ + ∆φ) + s2 (t) sin(−∆φ) + s2 (t) sin(4πf0 t + 2φ + ∆φ)]
                2
                1                                                1
              = AT AM AR [s1 (t) cos(∆φ) − s2 (t) sin(∆φ)] = AT AM AR s1 (t)
                2                                                2
Modulazione QAM o Quadrature Amplitude Modulation. Abbiamo che ak e bk hnno lo stesso alfabeto e possno assumere
tutti i valori dell’alfabeto indipendentemente l’una dall’altra. Tutti i possibili valori vengono definiti costallazione. Ogni
modulazione M-QAM trasmette
                                                   log2 M bit/simbolo
E la banda minima richiesta è uguale alla DSB 1/T = 2fn . In ricezione ricevo la stessa costellazione scalata per gli
opportuni guadagni.
La probabilità di decisione corretta è pari a
                                                                                  0
                                                                                      !!2
                                                     2      2N − 2              V0                    √
                       Pc = PCI · PCQ = (PCP AM ) =      1−        ·Q                       con N =       M
                                                              N                 σ

Posso avere M non dispari, in questo caso si prende una costellazione più grande e non se ne trasmette una parte.
La potenza dipende da seconda del simbolo questo implica un realizzazione più difficile del circuito di trasmissione.



     Quantizzazione uniforme, con valutazione del rapporto segnale/rumore di quantizzazione ad elevati bit-rate.



   Consideriamo un quantizzatore uniforme con L livelli ed L pari. E supponiamo x(nT ) processo aleatorio a media nulla.
Supponiamo inoltre che x(nT ) assuma probabilità unitaria nel intervallo [−V, V ].



                                                                 7
Indichiamo con ∆ = 2V /L il passo di quantizzazione, e se x(nT ) appartiene a [ak , ak+1 ] dove ak = −V + k∆ con
k = 0 . . . L − 1 essa viene quantizzata come bk = ak + ∆/2. Si ottiene il processo aleatorio y(nT ) = Q(x(nT )) dato che gli
intervalli coprono interamente [−V, V ] non abbiamo errore di sovraccarico |e(nT )| ≤ ∆/2.
Allora la potenza del errore sarà pari a
                                    Z ∞                             L−1
                                                                    X                   Z ak +1                    L−1
                                                                                                                   X
              Me = E[e2 (nT )] =          [Q(a) − a]2 fx (a) da =           fx (āk )             (bk − a)2 da =         fx (ak )∆3 /12
                                     −∞                             k=0                  ak                        k=0

Dove approssimiamo la densità di probabilità fx (a) con un valore costante fx (¯(a)k ) al interno del intervallo [ak , ak+1 ].
Quindi
                                             L−1
                                             X                 Z ∞
                                                  ∆fx (āk ) ≈     fx (a) = 1
                                                    k=0                  −∞

Otteniamo M e = ∆2 /12 pari alla potenza di una variabile uniformemente distribuita in [−∆/2, ∆/2].
Quindi σe2 = Me = ∆2 /12.
L’errore di quantizzazione risulta essere un rumore bianco a media nulla e varianza σe2

                                                                     E[x2 (nT )]
                                                           SNR =
                                                                     E[e2 (nT )]



Teoria Dei Segnali

     Dare la definizione di trasformazione lineare.
     • Dire se la trasformazione x(t) → x(−t) t ∈ R , è una trasformazione lineare, e in caso affermativo calcolarne il
       nucleo;
     • dire se la trasformazione x(t) → x∗ (−t) t ∈ R è una trasformazione lineare, e in caso affermativo calcolarne il
       nucleo.



   Una trasformazione è lineare se
   • È omogenea x(τ ) → y(t), se α ∈ C ⇒ αx(τ ) → αy(t)

   • È additiva x1 (τ ) → y1 (t), x2 (τ ) → y2 (t) ⇒ x1 (τ ) + x2 (τ ) → y1 (t) + y2 (t)
Quindi se una trasformazione è lineare vale la sovrapposizione degli effetti

                                               α1 x1 (τ ) + α2 x2 (τ ) → α1 y1 (t) + α2 y2 (t)

Una trasformazione è tempo invariante se e solo se

                                     ∀t0 ∈ I0 , x(τ − t0 ) → y(t − t0 ) , t0 ∈ U0 , I0 ⇒ U0 ⊃ I0



     Enunciare e dimostrare il teorema del campionamento R → Z(T ). Trovare la minima frequenza di campionamento
  per la rappresentazione del segnale x(t) = sinc(2t − 4), t ∈ R.


   Hp: x(t) Reale, a banda limitata B

   Th: x(t) è esattamente ricostruibile dai suoi campioni x(KT ) purché Fc > 2B e la formula di ricostruzione è
                                                     ∞                      
                                                    X                t − KT
                                            x(t) =      x(KT )sinc
                                                                        T
                                                          k=−∞

                                        x(t)                      xc (t)               x               x̂(t)
                                                                                   1
                                                                                   T g(t)
                                                       y
                                               R                   Z(T )                            R
Possiamo ridisegnare lo schema come



                                                                     8
                                      x(t)                       xc (t)            x                                       x̂(t)
                                                                                                         1
                                                                                                         T g(t)
                                                  y                                 
                                             R                    Z(T )                        R                        R
Passando in frequenza
                                  X(f )                           Xc (f )                                                   X̂(f )
                                                  →                                 ←                    |Q(f )|
                                             R                     R                           R                        R
                                                                  Z(T )




         Dare la definizione di trasformazione duale. Dire qual è la trasformazione duale di un filtro, dimostrando il
     risultato.


  La trasformazione duale di φ è la trasformazione che lega le trasformate di Fourier di ingresso e uscita
          ˆ Y (f ), f ∈ Û Il suo nucleo è
X(λ), λ ∈ I,
                                                      Z    Z
                                            H(f, λ) =   dτ   dtej2πλτ h(t, τ )e−j2πf t
                                                                    I       U

Ricordando la regola della convoluzione Y (f ) = X(f ) · G(f ) otteniamo
Z                           Z Z                                   Z                Z
                 −j2πf0 t                          −j2πf (t−u+u)             −j2πf u
  dt (x ∗ g(t))e          =      du x(u)g(t − u) e                = du x(u)e           dt g(t − u)e−j2πf (t−u) = X(f )G(f )
 I                                I      I                                               I                         I

Dove abbiamo usato l’invarianza rispetto alla traslazione e
     Z
       dt g(t)e−j2πf t = Y (f ) ∀u
          I

                                   x(t)                           y(t)                  X(f )                               Y (f )
                                                 g(t)                                                    |G(f )|
                                             I                I            Iˆ             Iˆ
È immediato verificare che la finestra è una trasformazione lineare a a tempi uguali con nucleo

        h(t, τ ) = p(τ )δI (t − τ )

Infatti
                 Z
        y(t) =       dτ x(τ )p(τ )δI (t − τ ) = x(t) · p(t)
                 I

Poichè y(t) = x(t) · p(t), allora possiamo vedere che è lineare

        α1 x1 (t) + α2 x2 (t) → (α1 x1 (t) + α2 x2 (t)) · p(t) = α1 x1 (t)p(t) + α2 x2 (t)p(t)



       Dimostrare che un filtro su Z(T ), è una trasformazione 1) lineare, 2) tempo invariante. Determinare, con di-
     mostrazione, la trasformazione data dalla cascata di due filtri h1 (kT ) e h2 (kT ) su Z(T ).


    La cascata di trasformazioni lineari è data
                                          x1 (t1 )                    x2 (t2 )                               x3 (t3 )
                                                        h1 (t2 , t1)                     h2 (t3 , t2 )
                                                   I1                   I2                                 I3
La cascata di trasformazioni lineari è una trasformazione lineare
                                                         x1 (t1 )                            x3 (t3 )
                                                                     h(t3 , t1)
                                                                  I1                    I3
Il suo nucleo è
                    Z
      h(t3 , t1 ) =   dt2 h1 (t2 , t1 ) · h2 (t2 , t3 )
                        I2

Dimostrazione
           Z                                Z       Z                                            Z                Z                                
x3 (t3 ) =     dt2 x2 (t2 )·h2 (t3 , t2 ) =     dt2      dt1 x1 (t1 )h1 (t2 , t1 ) h2 (t3 , t2 ) =     dt1 x1 (t1 )     dt2 h1 (t2 , t1 )h2 (t3 , t2 )
            I2                               I2       I1                                            I1                I
                                                                                                                    | 2          {z                    }
                                                                                                                                     h(t3 ,t1 )



                                                                                9
         Dare la definizione di trasformazione duale e dimostrare che la trasformazione duale del campionamento R → Z(T )
    è la periodicizzazione R → R/Z(1/T )


  Il duale del campionamento è la periodicizzazione
                          x(τ )                 y(t)                                                 X(λ)                      Y (f )
                                       y                                                                               →
                                I              U                                                             Î            Û
Andando a calcolare il nucleo otteniamo


                          Z         Z                                    Z         Z
       H(f, λ) =               dτ       ej2πλτ e−j2πf t δI (t − τ ) =         dt       dτ ej2πλτ e−j2πf t δI (t − τ )
                           I        U                                     U        I
                          Z
                  =            dte−j2π(f −λ)t = δÛ (f − λ)
                           U




       Enunciare e dimostrare il teorema di Parseval. Calcolare l’area del segnale x(t) = sinc4 (t) t ∈ R.



     Dati due funzioni X(f ) e Y (f ) integrabili in L2 con
               Z
      X(f ) = dt x(t)e−j2πf0 t
                      I

e
                  Z
       Y (f ) =           dt y(t)e−j2πf0 t
                  I

Allora vale                                                     Z                        Z
                                                                    dtx(t)y ∗ (t) =                df X(f )Y ∗ (f )
                                                                I                            Iˆ

Ed inoltre se x(t) = y ∗ (t)                                        Z                     Z
                                                                         dt|x(t)|2 =               df |X(f )|2
                                                                     I                        Iˆ
Dimostrazione
    Z               Z                  Z           Z                    Z
       dt y ∗ (t) ·    df X(f )ej2πf0 t = df X(f ) ·    dt y ∗ (t)ej2πf0 t = df X(f )Y ∗ (f )
         I                     Iˆ                          Iˆ                  I                                  Iˆ




       Uscita di un filtro ad un esponenziale complesso x(t) = V0 e−j2πf0 t , t ∈ I , con derivazione del risultato. Si
    deduca quindi l’espressione dell’uscita di un filtro reale ad un ingresso sinusoidale x(t) = V0 sin(2πf0 t + φ), t ∈ I , con
    derivazione del risultato.


     Gli esponenziali complessi sono autofunzioni dei filtri quindi siamo in presenza di linearità
                                                          x(t) = Aej2πf0 t → y(t) = Aej2πf0 t H(f0 )
In particolare con un filtro h(t) reale al qui ingresso applichiamo una sinusoide otteniamo x(t) = cos(2πf0 t + φ)
                ej2πf0 t ejφ + e−j2πf0 t e−jφ
       x(t) = A0
                              2
Allora in uscita otteniamo
            A0                      A0 −jφ
      y(t) = ejφ H(f0 )ej2πf0 t +         e   H(f0 )e−j2πf0 t
             2                      2               
                  A0
           =2R       |H(f0 )|ej∠H(f0 ) · ejφ ej2πf0 t = A0 |H(f0 )| cos(2πf0 t + φ + ∠H(f0 ))
                  2


                                                                                        10
Si ottiene in uscita la stessa sinusoide con ampiezza moltiplicata per il modulo della risposta in frequenza del filtro alla
frequenza della sinusoide



     Supponendo che x(t), t ∈ I, abbia trasformata X(f ), f ∈ Iˆ , dare l’espressione delle trasformate di Fourier dei
  segnali seguenti, dimostrando i risultati in forma unificata
     • y1 (t) = x(t) e−j2πf0 t , t ∈ I.

     • y2 (t) = x(t) sin(2πf0 t), t ∈ I.
     • y3 (t) = x− ∗ x(t), t ∈ I dove x− (t) = x(−t).




      Dare la definizione di stabilità in senso BIBO di un filtro numerico e dire se il filtro causale con funzione di
  trasferimento
                             T
        Hz (z) =                         .
                   1 − 3.5z −1 + 1.5z −2
  è stabile in senso BIBO.



   Un filtro sui tempi discreti caratterizzato dalla risposta impulsiva h(t), t ∈ (T ) è stabile in senso BIBO se e solo se
                                                       ∞
                                                       X
                                                              T |h(KT )| < +∞
                                                       k=−∞

Dunque, un filtro risulta stabile in senso BIBO se la sua risposta impulsiva decade in maniera sufficientemente rapida, per
nT che tende a pi‘u o meno infinito, in modo che valga la
                                                        ∞
                                                        X
                                                              T |h(kT )| < +∞
                                                       k=−∞

Consideriamo il filtro a tempo discreto con risposta impulsiva causale h(nT ) = pn 10 (nT ). Il filtro ‘e stabile in senso BIBO
se risulta |p| < 1. In tali ipotesi, la risposta in frequenza è una funzione razionale e risulta

                                                             T
                                             H(f ) =                       f ∈ R/Z(1/T )
                                                       1 − pe−j2πf T
e la trasformata zeta vale
                                                                        T
                                                          Hz (z) =
                                                                     1 − pz −1



     Trasformazione duale della cascata


   La    trasformazione       duale   delle trasformazioni       elementari         è   ancora     una   trasformazione   elementare
                                        x(τ )                    x1 (τ1 )                   y(t)
                                                 h(τ1 , τ )                      k(t, τ1 )
Il nucleo della trasformazione
                                                  x(τ )                          y(t)
                                                               N (t, τ )
Cascata dei duali
                                          X(λ)                   X1 (ζ)                    Y (f )
                                                  H(ζ, λ)                        K(t, ζ)
Nucleo dei duali
                                                 X(λ)                            Y (f )
                                                               N̂ (f, λ)




                                                                  11
                   Z        Z
      H(ζ, λ) =        dτdτ1 ej2πλτ h(τ1 , τ )e−j2πζτ1
                ZI     I
                       Z
      K(f, ζ) =    dτ1     dt ej2πζτ h(t, τ1 )e−j2πf t
                    I1          U

Il nucleo dei duali
      Z                         Z      Z      Z                                  Z              Z                               
            H(ζ, λ) · K(f, ζ) =     dζ      dτ dτ1 ej2πλτ h(τ1 , τ )e−j2πζτ1 ·               dτ1       dt ej2πζτ h(t, τ1 )e−j2πf t
        Iˆ1                       ˆ
                                ZI1 Z I Z I Z                  Z                          I1         U

                                                                       j2πf t                        −j2πf t
                                                                                                             
                              =     dζ dτ        dτ1     dτ1      dt e        h(τ1 , τ )k(t1 , τ1 )e
                                 Iˆ     I     I
                                Z1 Z         Z1      ZI1        U

                                                               j2πλt
                                                                     N (t, τ )e−j2πf t
                                                                                        
                              =     dζ dτ        dτ1     dt e
                                 Iˆ     I     I1      U
                                Z1 Z
                                               j2πλτ
                                                     N (t, τ )e−j2πf t = N̂ (f, λ)
                                                                      
                              = dτ        dt e
                                    I     U




                                                                       12
