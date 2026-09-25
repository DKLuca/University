---
fonte: "trasfelementari.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Corso di Teoria dei Segnali Comunicazioni Elettriche - Università di Udine
    Prof. R. Rinaldo


1     Trasformazioni elementari
Le trasformazioni elementari sono particolari trasformazioni lineari che operano una ristruttura-
zione del dominio I → U di un segnale, e il cui nucleo è l’impulso ideale δD (t − u), t ∈ U , u ∈ I,
con D definito opportunamente. Le trasformazioni elementari sono quattro e in particolare sono
il campionamento, l’interpolazione ideale, la periodicizzazione e la deperiodicizzazione.
    Indicato con I = I1 /I2 il generico dominio del segnale di ingresso, in cui I1 = R oppure
I1 = Z(T ) per segnali a tempo continuo o discreto, mentre I2 = Z(Tp ) indica la periodicità,
ciascuna trasformazione elementare trasforma un segnale x(u), u ∈ I in un segnale y(t), t ∈ U .
Indicato con U = U1 /U2 il dominio di uscita, si ha in particolare
    1. campionamento (vedi Fig. 1): in questo caso I2 = U2 (non cambia la periodicità del
       segnale), mentre I1 ⊃ U1 (trasformazione in discesa). L’impulso ideale è definito sul
       dominio di ingresso D = I1 /I2 . Formalmente si ha
                                        Z
                               y(t) =       du x(u) δI (t − u) = x(t),   t ∈ U.
                                        I
      Nella relazione precedente, abbiamo sfruttato la proprietà rivelatrice dell’impulso. Il se-
      gnale di uscita è dunque uguale all’ingresso, però limitatamente agli istanti del dominio di
      uscita. Il caso più semplice è il campionamento R → Z(T ), in cui l’uscita è un segnale a
      tempo discreto ottenuto dal segnale a tempo continuo prendendone i valori negli istanti
      multipli di T . La trasformazione è dunque il modello di un convertitore analogico/digitale,
      trascurando la quantizzazione dei valori del segnale. Se il segnale di ingresso fosse periodi-
      co, il campionamento R/Z(Tp ) → Z(T )/Z(Tp ) avrebbe senso solamente se Tp fosse multiplo
      di T , ma in ogni caso la relazione ingresso uscita risulterebbe y(t) = x(t), t ∈ U .
      Il campionamento Z(T ) → Z(N T ) preleva invece i valori dell’ingresso passando da un
      dominio temporale discreto più fitto a uno meno fitto (in questo caso si parla anche di deci-
      mazione). Se abbiamo a che fare con segnali periodici, nel campionamento Z(T )/Z(Tp ) →
      Z(N T )/Z(Tp ) è necessario che i domini siano compatibili, ovvero che Tp sia multiplo di
      NT.
    2. interpolazione (vedi Fig. 2): anche in questo caso I2 = U2 (non cambia la periodicità del
       segnale), mentre I1 ⊂ U1 (trasformazione in salita). I casi possibili sono Z(T )/Z(Tp ) →
       R/Z(Tp ), oppure Z(T )/Z(Tp ) → Z(T /N )/Z(Tp ). Si passa in ogni caso da un dominio
       temporale meno fitto a uno più fitto, mentre la periodicità non cambia.
      L’impulso ideale è definito sul dominio di uscita D = U1 /U2 . Formalmente si ha
                                             Z
                                   y(t) =         du x(u) δU (t − u) t ∈ U.
                                              I


                                                      1
 40                                                                 40


 30
                                                                    30

 20


                                                                    20
 10


  0
                                                                    10

−10

                                                                     0
−20


−30                                                             −10


−40

                                                                −20
−50


−60                                                             −30
      0         50       100     150           200        250            0          50        100      150       200   250




                 Figura 1: Campionamento R → Z(20), e decimazione Z(20) → Z(40).



          Si noti che non possiamo applicare come nel caso del campionamento la proprietà rivelatrice
          dell’impulso, in quanto l’integrale è sul dominio I, mentre l’impulso è definito nel dominio
          U . Si ha, esplicitando l’espressione dell’integrale,

           (a) interpolazione Z(T ) → R. In questo caso
                                                            +∞
                                                            X
                                               y(t) = T                      x(kT ) δR (t − kT ).
                                                          k=−∞

               L’uscita è un segnale matematico a tempo continuo, costituito da un treno di impulsi
               ideali, posizionati negli istanti kT del dominio di ingresso e la cui area è T x(kT ).
          (b) interpolazione Z(T )/Z(N T ) → R/Z(N T ), Tp = N T . In questo caso
                                     N
                                     X −1                                                +∞
                                                                                         X
                          y(t) = T          x(kT ) δR/Z(Tp ) (t − kT ) = T                      x(kT ) δR (t − kT ).
                                     k=0                                                 k=−∞

               La relazione è la stessa del caso precedente, a causa della periodicità del segnale e
               dell’impulso sul dominio R/Z(N T ).
           (c) interpolazione Z(T ) → Z(T /N ). In questo caso
                                                       +∞
                                                       X
                                     y(hT /N ) = T                  x(kT ) δZ(T /N ) (hT /N − kT ).
                                                      k=−∞



                                                                2
        Si verifica immediatamente che il segnale y(hT /N ) è ovunque nullo, eccetto che negli
        istanti di ingresso multipli di T , dove vale N x(kT ). Il segnale interpolato viene dunque
        ottenuto aggiungendo N − 1 zeri negli istanti intermedi a quelli su cui è definito
        l’ingresso, e moltiplicando i valori x(nT ) per il rapporto N dei quanti temporali dei
        domini di ingresso e uscita.
   (d) interpolazione Z(T )/Z(KT ) → Z(T /N )/Z(KT ). In questo caso
                                         K−1
                                         X
                         y(hT /N ) = T            x(kT ) δZ(T /N )/Z(KT ) (hT /N − kT )
                                         k=0

                                       +∞
                                       X
                                 =T           x(kT ) δZ(T /N ) (hT /N − kT ).
                                      k=−∞

        La relazione è la stessa del caso precedente, a causa della periodicità del segnale e del-
        l’impulso sul dominio Z(T /N )/Z(KT ). Come prima, il segnale y(hT /N ) è ovunque
        nullo, eccetto che negli istanti di ingresso multipli di T , dove vale N x(kT ), mentre la
        periodicità si conserva.

3. periodicizzazione (vedi Fig. 3): in questo caso I1 = U1 , mentre I2 ⊂ U2 (la trasformazione
   modifica solamente il periodo del segnale e si tratta di una trasformazione in salita). I casi
   possibili sono I1 → I1 /Z(Tp ), oppure I1 /Z(Tp ) → I1 /Z(Tp /N ). Si passa in ogni caso da
   un segnale non periodico (a tempo continuo o discreto) ad uno periodico, oppure da un
   segnale periodico ad uno con un periodo più piccolo.
   L’impulso ideale è definito sul dominio di uscita D = U1 /U2 . Formalmente si ha
                                         Z
                                y(t) =       du x(u) δU (t − u) t ∈ U.
                                         I


   Esplicitando l’espressione dell’integrale, si ottiene

    (a) periodicizzazione R → R/Z(Tp ). In questo caso, osservando che
                                                         +∞
                                                         X
                                    δR/Z(Tp ) (t) =           δR (t − kTp ),
                                                       k=−∞

        possiamo scrivere

                                         Z +∞
                             y(t) =               x(u) δR/Z(Tp ) (t − u) du
                                             −∞



                                                   3
        x(kT )


      ···                               ···
                   T
                        2T                             t

            y(t)
                       T x(2T )
      ···                               ···
                   T
                        2T                             t

      y(kT /2)
                       2x(2T )

      ···                               ···
                   T
                        2T                             t




Figura 2: Interpolazione di x(kT ), Z(T ) → R, e Z(T ) → Z(T /2).




                                  4
                                      +∞
                                      X    Z +∞
                              =                      x(u) δR (t − u − kTp ) du
                                  k=−∞ −∞
                                   +∞
                                   X
                              =            x(t − kTp ).
                                  k=−∞

    L’uscita è un segnale periodico a tempo continuo, ottenuto sommando le repliche del
    segnale x(t) nei multipli di Tp .
(b) periodicizzazione Z(T ) → Z(T )/Z(N T ). In questo caso, osservando che
                                                  +∞
                                                  X
                        δZ(T )/Z(N T ) (kT ) =            δZ(T ) (kT − iN T ),
                                                 i=−∞

    possiamo scrivere

                                  +∞
                                  X
                 y(hT ) = T             x(kT ) δZ(T )/Z(N T ) (hT − kT ) du
                               k=−∞
                                +∞
                                X +∞X
                         = T                    x(kT ) δZ(T ) (hT − kT − iN T ) du
                               i=−∞ k=−∞
                              +∞
                              X
                         =            x(hT − iN T ).
                              i=−∞

    L’uscita è un segnale periodico a tempo discreto, ottenuto sommando le repliche del
    segnale x(kT ) nei multipli di Tp = N T .
(c) periodicizzazione R/Z(Tp ) → R/Z(Tp /N ). In questo caso, osservando che
                                               N
                                               X −1
                         δR/Z(Tp /N ) (t) =           δR/Z(Tp ) (t − kTp /N ),
                                               k=0
    possiamo scrivere
                               Z Tp
                     y(t) =           x(u) δR/Z(Tp /N ) (t − u) du
                                0
                               N
                               X −1 Z Tp
                          =                x(u) δR/Z(Tp ) (t − u − kTp /N ) du
                               k=0 0
                               N
                               X −1
                          =           x(t − kTp /N ).
                               k=0

    L’uscita è un segnale periodico a tempo continuo, con periodo più piccolo Tp /N ,
    ottenuto sommando N repliche del segnale di ingresso.

                                           5
   (d) periodicizzazione Z(T )/Z(Tp ) → Z(T )/Z(Tp /N ). Si osservi che per la compatibilità
       dei domini deve essere Tp /N = KT . Come nel caso precedente, osservando che
                                                      N
                                                      X −1
                           δZ(T )/Z(Tp /N ) (kT ) =          δZ(T )/Z(Tp ) (kT − iTp /N ),
                                                      i=0

       possiamo scrivere
                                   NX
                                    K−1
                  y(hT ) = T              x(kT ) δZ(T )/Z(Tp /N ) (hT − kT ) du
                                    k=0
                                   N
                                   X −1 NX
                                         K−1
                            = T                 x(kT ) δZ(T )/Z(Tp ) (hT − kT − iTp /N ) du
                                    i=0   k=0
                                 N
                                 X −1
                            =          x(hT − iTp /N ).
                                 i=0

       L’uscita è un segnale periodico a tempo discreto, con periodo più piccolo Tp /N ,
       ottenuto sommando N repliche del segnale di ingresso.

                                       x(t)




                                                                                t
                                       y(t)


                     ···                                                      ···


                                                        Tp                      t

                       Figura 3: Periodicizzazione R → R/Z(Tp ).


4. deperiodicizzazione: in questo caso I1 = U1 , mentre I2 ⊃ U2 (trasformazione in discesa).
   Si passa da un segnale periodico a uno non periodico, oppure da un segnale con periodo

                                                 6
Tp a uno con periodo N Tp più grande. L’impulso ideale è definito sul dominio di ingresso
D = I1 /I2 . Formalmente si ha
                                 Z
                        y(t) =       du x(u) δI (t − u) = x(t),   t ∈ U.
                                 I

Nella relazione precedente, abbiamo sfruttato la proprietà rivelatrice dell’impulso. La
deperiodicizzazione non modifica dunque i valori del segnale, ma ne ridefinisce semplice-
mente il periodo. L’utilità della deperiodicizzazione risulta evidente nell’interpretazione
delle trasformazioni duali delle trasformazioni elementari.

Riassunto
Riassumendo le trasformazioni elementari sono particolari trasformazioni lineari con nucleo
δD (t − u), con D uguale al dominio di ingresso per le trasformazioni in discesa (campio-
namento e deperiodicizzazione) e al dominio di uscita per quelle in salita (interpolazione
e periodicizzazione). In particolare

(a) la relazione ingresso-uscita del campionamento è y(t) = x(t), e l’uscita si ottiene
    prelevando i valori dell’ingresso in un dominio temporale meno fitto;
(b) nell’interpolazione Z(T )/I2 → R/I2 un segnale a tempo discreto viene trasformato
    in un segnale matematico a tempo continuo costituito da un treno di impulsi delta di
    Dirac localizzati negli istanti kT e con area T x(kT ). Nell’interpolazione Z(T )/I2 →
    Z(T /N )/I2 il segnale di uscita si ottiene inserendo N − 1 zeri negli istanti intermedi
    a quelli su cui è definito l’ingresso, e moltiplicando per N i valori x(kT );
 (c) nella periodicizzazione di un segnale (a tempo continuo o discreto) non periodico, per
     ottenere un segnale periodico con periodo Tp si sommano infinite repliche del segnale
     traslate nei multipli di Tp . Nella periodicizzazione di un segnale (a tempo continuo o
     discreto) periodico con periodo Tp per ottenerne uno periodico con periodo Tp /N , si
     sommano N repliche del segnale di ingresso traslate nei multipli di Tp /N ;
(d) nella deperiodicizzazione, il periodo del segnale di ingresso viene ignorato, oppure
    ridefinito come N volte più grande, senza modificare i valori del segnale.


2    Duali delle Trasformazioni Elementari

Nella sezione precedente, abbiamo inquadrato le trasformazioni elementari come particolari
trasformazioni lineari. Risulta quindi immediato calcolare la trasformazione duale di cia-
scuna delle trasformazioni elementari, utilizzando la relazione che ci permette di calcolare
il nucleo della trasformazione duale.


                                             7
Consideriamo ad esempio il caso importante della trasformazione duale del campionamento
R → Z(T ). La trasformazione duale opera sui domini R → R/Z(1/T ) ed il nucleo risulta
                              Z         Z
                 H(f, λ) =         du           dt ej2πλu e−j2πf t δR (t − u)
                               R        Z(T )
                                   +∞       Z +∞
                                                    ej2πλu e−j2πf kT δR (kT − u) du
                                   X
                          = T
                                  k=−∞ −∞
                                   +∞
                                   X
                                       j2π(λ−f )kT
                          = T               e
                                  k=−∞
                          = δR/Z(1/T ) (f − λ).

Si vede che la trasformazione duale è la trasformazione elementare da R → R/Z(1/T ),
in particolare una periodicizzazione. Il risultato trovato per il campionamento può essere
facilmente generalizzato, e vale il seguente teorema.

Teorema 1 La trasformazione duale di una trasformazione elementare I → U è la tra-
sformazione elementare Iˆ → Û .

Da semplici considerazioni sui domini coinvolti, utilizzando il teorema precedente, possia-
mo concludere che le trasformazioni duali della trasformazioni elementari possono essere
elencate come in Tabella 1.

            Tabella 1: Trasformazioni elementari e trasformazioni duali

                              tf                          tf duale
                      campionamento                  periodicizzazione
                       interpolazione               deperiodicizzazione
                      periodicizzazione              campionamento
                     deperiodicizzazione              interpolazione




                                                8
