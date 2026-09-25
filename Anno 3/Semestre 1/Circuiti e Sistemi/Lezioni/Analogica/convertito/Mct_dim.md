---
fonte: "Mct_dim.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

DIMOSTRAZIONE DEL METODO DELLE COSTANTI DI TEMPO DI CORTO
                      CIRCUITO (SCTC) E DI CIRCUITO APERTO (OCTC)
                                                       (G.Spiazzi)


Consideriamo una generica rete lineare composta da resistenze, condensatori e generatori
comandati. Essa può rappresentare un generico amplificatore di cui si vuole analizzare il
comportamento in bassa frequenza (in tal caso i condensatori considerati saranno di accoppiamento
e di bypass), oppure il comportamento in alta frequenza (in questo caso le capacità considerate sono
relative ai modelli validi in un intervallo esteso di frequenze dei dispositivi attivi, più eventuali
capacità esterne aggiunte con l’intento di limitare la risposta in alta frequenza). E’ da notare che la
rete è priva di generatori indipendenti, e rappresenta così il circuito a riposo, con ingressi annullati.
Inoltre la rete si considera essere ridotta (i condensatori in serie o in parallelo sono sostituiti dal
condensatore equivalente) e connessa (esiste una funzione di trasferimento non nulla fra le tensioni
sui condensatori e la tensione di uscita dell’amplificatore). Per la necessità di queste ipotesi vedere
il documento sugli approfondimenti del metodo delle costanti di tempo.


Le frequenze proprie della rete a riposo rappresentano i poli del sistema e coincidono con le radici
del polinomio caratteristico della rete (polinomio a denominatore di qualsiasi funzione di
trasferimento la cui rete a riposo abbia la stessa topologia). Di questa rete si mettano in evidenza
tutte le porte a cui fanno capo i condensatori (supponiamo siano N), così come raffigurato in
figura 1.
                                                            C3
                                                  i3
                                                         + v3 -
                                  i2
                                           +
                                 C2       v2
                                           -
                                                                              iN
                                  i1                    R ,G
                                           +                            +
                                C1        v1                            vΝ         CΝ
                                           -                             -


 Figura 1 – Rete lineare generica, composta da resistenze e generatori comandati, con i condensatori posti in evidenza


E’ possibile esprimere le tensioni a ciascuna porta in funzione delle correnti di tutte le N porte
mediante una matrice di resistenze R di dimensione NxN (o, analogamente, di conduttanze G):
v = Ri ⇒ i = Gv                                                                                                 (1)
dove le matrici R e G hanno la seguente forma:
  ⎡ R 11          R 12         L      R 1N ⎤               ⎡ G11    G12      L   G 1N ⎤
  ⎢                                         ⎥              ⎢                           ⎥
  ⎢ R 21          R 22         L       L ⎥              −1
                                                           ⎢ G 21   G 22     L    L ⎥
R=⎢                                         ⎥,       G=R =⎢                            ⎥        (2)
  ⎢ M              M           M        M ⎥                ⎢ M        M      M     M ⎥
  ⎢                                         ⎥              ⎢                           ⎥
  ⎢⎣ R N1          L           L      R NN ⎥⎦              ⎢⎣G N1    L       L   G NN ⎥⎦

dove l’invertibilità delle matrici è assicurata dall’ipotesi di rete connessa.
Gli elementi delle matrici R e G hanno il seguente significato:
         vk
R kh =                 ,   j = 1L N , j ≠ h                                                    (3.a)
         ih   i j =0


         ik
G kh =                 ,   j = 1L N , j ≠ h                                                    (3.b)
         vh   v j =0

In particolare, Rkk rappresenta la resistenza vista alla porta k-esima con tutte le altre porte aperte,
mentre Gkk rappresenta la conduttanza vista alla porta k-esima con tutte le altre porte
cortocircuitate.
Le equazioni costitutive dei condensatori possono essere raggruppate nella seguente equazione
matriciale:
         dv                    −1       dv
i = −C         ⇒ −C i =                                                                         (4)
         dt                             dt
dove C è una matrice diagonale contenente i valori degli N condensatori della rete:
                                                     ⎡1                  ⎤
  ⎡C1         0            L        0 ⎤              ⎢C    0    L    0 ⎥
  ⎢                                     ⎥            ⎢ 1                 ⎥
  ⎢0                               L⎥                ⎢0    1
              C2           L                      −1            L   L⎥
C=⎢                                     ⎥,       C =⎢      C2            ⎥                     (4.a)
  ⎢M          M            O        M ⎥              ⎢ M    M   O    M ⎥
  ⎢                                     ⎥            ⎢                   ⎥
  ⎢⎣ 0        L            L       C N ⎥⎦            ⎢0              1 ⎥
                                                           L    L
                                                     ⎢⎣             C N ⎥⎦

La (2) e la (4) possono essere combinate tra loro per ricavare l’equazione differenziale che esprime
il comportamento delle grandezze della rete a riposo:
     dv
RC      +v=0                                                                                   (5.a)
     dt
oppure
dv   −1
   +C Gv = 0                                                                                   (5.b)
dt
Tali equazioni, nel dominio delle Laplace trasformate diventano:
(s R C + I )v = 0                                                                              (6.a)
oppure
(s + C G I )v = 0
        −1
                                                                                                          (6.b)
dove I è la matrice identità (matrice diagonale con tutti uno sulla diagonale principale). Il polinomio
caratteristico della rete si ricava dal determinante della matrice
det (s R C + I ) = 0                                                                                      (7.a)
oppure, in modo analogo,
    (        −1
det sI + C G = 0    )                                                                                     (7.b)
Tali matrici sono di seguito riportate:
           ⎡sR 11C1 + 1         sR 12 C 2       L      sR 1N C N ⎤
           ⎢                                                       ⎥
           ⎢ sR 21C1          sR 22 C 2 + 1 L             L        ⎥
sR C + I = ⎢                                                       ⎥                                      (8.a)
           ⎢     M                     M        M          M       ⎥
           ⎢                                                       ⎥
           ⎢⎣ sR N1C1                  L        L    sR NN C N + 1⎥⎦

           ⎡ G11               G12                 G 1N ⎤
           ⎢s + C               C1
                                            L
                                                   C1 ⎥
           ⎢ G 1                 G                        ⎥
      −1
           ⎢ 21              s + 22         L      L ⎥
sI + C G = ⎢ C 2                  C2                      ⎥                                               (8.b)
           ⎢ M                   M          M       M     ⎥
           ⎢                                              ⎥
           ⎢ G N1               L           L
                                                    G
                                                s + NN ⎥
           ⎢⎣ C N                                    C N ⎥⎦


Dimostrazione del metodo delle costanti di tempo di circuito aperto
Il calcolo del determinante della matrice (8.a) dà luogo ad un polinomio caratteristico il cui termine
noto è unitario, mentre il determinante della matrice (8.b) produce lo stesso polinomio caratteristico
ma espresso in forma monomia, avente cioè il coefficiente del termine in s di grado superiore
unitario. Il determinante di una generica matrice A si può calcolare nel seguente modo (sviluppo
secondo una riga della matrice):

                               ( )
             N
det (A ) = ∑ (− 1) j+i a ji det T ji                                                                       (9)
             i =1

dove a sono gli elementi della matrice, j è un intero scelto nell’intervallo [1,N] e Tji è la
sottomatrice ottenuta dalla matrice A eliminando la riga j-esima e la colonna i-esima. Per esempio,
scegliendo j=1, dalla (8.a) si ottiene:
det (s R C + I ) = (sR 11C1 + 1)det (T11 ) − sR 12 C 2 det (T12 ) + ....(− 1)      sR 1N C N det (T1N )
                                                                            1+ N
                                                                                                          (10)
Per semplicità analizziamo il caso N = 3.
                   ⎡sR 11C1 + 1      sR 12 C 2        sR 13C 3 ⎤
                   ⎢                                             ⎥
det (s R C + I ) = ⎢ sR 21C1      sR 22 C 2 + 1       sR 23C 3 ⎥ =
                   ⎢                                             ⎥                                                   (11)
                   ⎢⎣ sR 31C1        sR 32 C 2      sR 33C 3 + 1⎥⎦
                 = (sR 11C1 + 1)det (T11 ) − sR 12 C 2 det (T12 ) + sR 13C 3 det (T13 )

                  ⎡sR 22 C 2 + 1              sR 23 C 3 ⎤
det (T 11 ) = det ⎢                                        ⎥ = (sR 22 C 2 + 1)(sR 33 C 3 + 1) − s R 23 R 32 C 2 C 3 =
                                                                                                 2

                  ⎣⎢ sR 32 C 2               sR 33 C 3 + 1⎦⎥                                                          (12.a)
             = 1 + s (R 22 C 2 + R 33 C 3 ) + s 2 (R 22 R 33 − R 23 R 32 )C 2 C 3

                 ⎡sR 21C1           sR 23C 3 ⎤
det (T12 ) = det ⎢                              ⎥ = sR 21C1 (sR 33C 3 + 1) − s R 23 R 31C1C 3 =
                                                                              2

                 ⎢⎣sR 31C1         sR 33C 3 + 1⎥⎦                                                                  (12.b)
             = sR 21C1 + s 2 (R 21 R 33 − R 23 R 31 )C1C 3

                 ⎡sR 21C1            sR 22 C 2 + 1⎤
det (T13 ) = det ⎢                                ⎥ = s R 21R 32 C1C 2 − sR 31C1 (sR 22 C 2 + 1) =
                                                       2

                 ⎢⎣sR 31C1            sR 32 C 2 ⎥⎦                                                                 (12.c)
             = −sR 31C1 + s 2 (R 21R 32 − R 22 R 31 )C1C 2

                                    (
det (s R C + I ) = (sR 11C1 + 1) 1 + s(R 22 C 2 + R 33C 3 ) + s 2 (R 22 R 33 − R 23 R 32 )C 2 C 3 −)
                         (                          )
                  − sR 12 C 2 sR 21C1 + s 2 (R 21 R 33 − R 23 R 31 )C1C 3 +                                          (13)
                  + sR C (− sR C + s (R R − R R )C C )
                          13   3        31   1
                                                  2
                                                       21   32    22   31   1   2

In definitiva, il polinomio caratteristico è, in questo caso, un polinomio del terzo ordine i cui
coefficienti sono dati dalle seguenti espressioni:
det (s R C + I ) = 1 + a 1s + a 2 s 2 + a 3s 3 = D(s )                                                               (14)

a 1 = R 11C1 + R 22 C 2 + R 33C 3                                                                                    (15)

a 2 = (R 11 R 22 − R 12 R 21 )C1C 2 + (R 11 R 33 − R 13 R 31 )C1C 3 + (R 22 R 33 − R 23 R 32 )C 2 C 3                (16)

a 3 = [R 11 (R 22 R 33 − R 23 R 32 ) − R 12 (R 21 R 33 − R 23 R 31 ) + R 13 (R 21 R 32 − R 22 R 31 )]C1C 2 C 3       (17)
Come si può osservare, il coefficiente a1 relativo al termine di grado unitario risulta somma di
costanti di tempo. In particolare, possiamo scrivere:
       N              N
a 1 = ∑ R ii C i = ∑ R io C i                                                                                        (18)
      i =1           i =1

dove con la notazione R io si intende la resistenza vista alla porta i-esima con le altre porte aperte.
Allo stesso modo, le costanti di tempo nella sommatoria (18) vengono dette costanti di tempo di
circuito aperto.
Il coefficiente a2, relativo al termine di secondo grado, dalla (16) risulta invece dato dalla somma di
prodotti di costanti di tempo. Al fine di capire il significato fisico di tali costanti di tempo,
consideriamo la figura 2, che evidenza due porte della rete di cui una è cortocircuitata, mentre tutte
le altre porte si considerano aperte. Le equazioni alle due porte danno le seguenti due relazioni:

⎧ v k = R kk i k + R kh i h
⎪
⎨ v = R i + R i = 0 ⇒ i = − R hk i                                                                   (19)
⎪⎩ h      hk k       hh h   h
                              R hh k
Sostituendo la seconda equazione nella prima si ottiene:

      ⎛ R R − R kh R hk ⎞
v k = ⎜ kk hh           ⎟i k                                                                         (20)
      ⎝     R hh        ⎠
Dalla (20) si osserva che
R kk R hh − R kh R hk v k
                     =                                                                               (21)
        R hh           ik                v h =0

rappresenta la resistenza vista alla porta k-esima con la porta h-esima cortocircuitata e tutte le altre
porte aperte. Nel seguito indicheremo tale resistenza con il simbolo R hs
                                                                       k . In modo analogo:

R kk R hh − R hk R kh v h
                     =                                                                               (22)
        R kk           ih                v k =0

rappresenta la resistenza vista alla porta h-esima con la porta k-esima cortocircuitata e tutte le altre
porte aperte. Confrontando le (21) e (22) si osserva che vale la seguente relazione:

R kk R hh − R hk R kh = R ok R ks
                               h = Rk Rh
                                    hs o
                                                                                                     (23)
Possiamo, quindi, scrivere:
       N −1 N                    N −1 N
a2 =   ∑∑       R i R j Ci C j =
                  o is
                                       ∑∑   R ijs R oj C i C j                                       (24)
     i =1 j=i +1                 i =1 j=i +1

Nell’ipotesi di polo dominante in alta frequenza (polo a frequenza minore di tutti gli altri poli e zeri
della funzione di trasferimento valida in alta frequenza), la frequenza di taglio superiore può essere
approssimata dalla seguente espressione:
       ωH    1                       1
fH =      ≈       =                                                                                  (25)
       2 π 2 πa 1                N
                            2 π∑       R io C i
                                i =1



                                                  ik                                      ih
                                                       +                                  +
                                                       vk                                     vh=0
                                                       -                                  -
                                                                     R



                                                                                           hs
                                                       Figura 2 – Rete per il calcolo di R k
Dimostrazione del metodo delle costanti di tempo di cortocircuito
Per la dimostrazione del metodo delle costanti di tempo di cortocircuito risulta più semplice partire
dalla matrice (8.b) calcolandone il determinante (caso N = 3):
                   ⎡ G11                 G12       G13 ⎤
                   ⎢s + C                 C1        C1 ⎥
                   ⎢ G 1                           G 23 ⎥⎥
   (            )
det sI + C G = det ⎢ 21
          −1
                   ⎢ C2
                                           G
                                       s + 22
                                           C2       C2 ⎥
                                                           =
                   ⎢ G 31                G 32        G ⎥                                     (26)
                   ⎢ C                           s + 33 ⎥
                   ⎣    3                 C3         C3 ⎦
                      ⎛ G ⎞
                    = ⎜ s + 11 ⎟ det (T11 ) − 12 det (T12 ) + 13 det (T13 )
                                             G               G
                      ⎝    C1 ⎠              C1              C1

                 ⎡ G 22             G 23 ⎤
                 ⎢s + C              C 2 ⎥ ⎛ G 22 ⎞⎛ G 33 ⎞ G 32 G 23
det (T11 ) = det ⎢                           = ⎜s +     ⎟⎜ s +    ⎟−      =
                                      G ⎥
                         2
                    G
                                  s + 33 ⎥ ⎝
                 ⎢    32                            C 2 ⎠⎝     C3 ⎠ C3 C2
                                                                                             (27)
                 ⎣⎢ C 3               C 3 ⎦⎥
                   ⎛G    G ⎞ G G        G G
          = s 2 + s⎜ 22 + 33 ⎟ + 22 33 − 32 23
                   ⎝ C2  C3 ⎠ C2 C3     C3 C2

                 ⎡ G 21       G 23 ⎤
                 ⎢C            C 2 ⎥ G 21 ⎛ G 33 ⎞ G 31 G 23
det (T12 ) = det ⎢ 2                   =    ⎜s +    ⎟−       =
                 ⎢ G 31         G 33 ⎥⎥ C 2 ⎝    C3 ⎠ C3 C2
                             s+                                                              (28)
                 ⎣⎢ C 3         C 3 ⎦⎥
             ⎛G ⎞ G G        G G
          = s⎜ 21 ⎟ + 21 33 − 31 23
             ⎝ C2 ⎠ C2 C3    C3 C2

                 ⎡ G 21        G 22 ⎤
                 ⎢C          s+
                                C 2 ⎥ G 21 G 32 G 31 ⎛ G 22 ⎞
det (T13 ) = det ⎢ 2                  =        −     ⎜s +    ⎟=
                 ⎢ G 31       G 32 ⎥⎥ C 2 C 3    C3 ⎝     C2 ⎠
                                                                                             (29)
                 ⎢⎣ C 3       C 3 ⎥⎦
              ⎛G ⎞ G G        G G
          = −s⎜ 31 ⎟ + 21 32 − 31 22
              ⎝ C3 ⎠ C2 C3    C3 C2

   (       −1
                )
                ⎛ G ⎞⎛              ⎛G    G ⎞ G G        G G ⎞
det s I + C G = ⎜ s + 11 ⎟⎜⎜ s 2 + s⎜ 22 + 33 ⎟ + 22 33 − 32 23 ⎟⎟ −
                ⎝    C1 ⎠⎝          ⎝ C2  C3 ⎠ C2 C3     C3 C2 ⎠
                                                                                                (30)
 G ⎛ G       G G     G G ⎞ G ⎛ G             G G     G G ⎞
− 12 ⎜ s 21 + 21 33 − 31 23 ⎟ + 13 ⎜ − s 31 + 21 32 − 31 22 ⎟ = s 3 + b 2 s 2 + b1s + b 0
 C1 ⎝ C 2    C2 C3   C 3 C 2 ⎠ C1 ⎝     C3   C2 C3   C3 C2 ⎠

I coefficienti del polinomio caratteristico sono dati dalle seguenti espressioni:
       a 2 G11 G 22 G 33
b2 =      =   +    +                                                                         (31)
       a 3 C1   C2   C3
        a 1 G 22 G 33 G 32 G 23 G11 ⎛ G 22 G 33 ⎞ G12 G 21 G13 G 31
b1 =       =         −         +    ⎜     +     ⎟−        −         =
        a 3 C2 C3      C3 C2     C1 ⎝ C 2   C 3 ⎠ C1 C 2    C1 C 3
                                                                                                    (32)
       1
   =       (G11G 22 − G12 G 21 ) + 1 (G11G 33 − G13G 31 ) + 1 (G 22 G 33 − G 32 G 23 )
     C1C 2                        C1C 3                    C2C3

        a 0 G 11 ⎛ G 22 G 33 G 32 G 23 ⎞ G 12 ⎛ G 21 G 33 G 31 G 23 ⎞ G 13 ⎛ G 21 G 32 G 31 G 22 ⎞
b0 =       =     ⎜          −          ⎟−     ⎜          −          ⎟+     ⎜          −          ⎟=
        a 3 C1 ⎝ C 2 C 3      C 3 C 2 ⎠ C1 ⎝ C 2 C 3       C 3 C 2 ⎠ C1 ⎝ C 2 C 3       C3 C2 ⎠

    =
           1
                 [G (G G − G 32 G 23 ) − G12 (G 21G 33 − G 31G 23 ) + G13 (G 21G 32 − G 31G 22 )]
        C1C 2 C 3 11 22 33
                                                                                                    (33)
Osserviamo che il coefficiente b2 è espresso mediante somma di inversi di costanti di tempo di
cortocircuito. In generale risulta:
           a n −1 N G ii N 1
                 =∑
                       Ci ∑
b n −1 =                 =        s
                                                                                                    (34)
            an    i =1     i =1 R i C i


dove con R si si intende la resistenza vista dal condensatore i-esimo con tutti gli altri cortocircuitati.
Il coefficiente b1, invece, risulta composto dalla somma di inversi di prodotti di costanti di tempo.
Per capire il loro significato si faccia riferimento alla figura 3 che riporta due porte generiche della
rete in cui una è lasciata aperta, mentre tutte le altre sono cortocircuitate.


                                          ik                                       ih=0
                                                +                             +
                                               vk                             vh
                                                -                             -
                                                              G



                                                                                   ho
                                               Figura 3 - Rete per il calcolo di G k

Le equazioni alle due porte risultano, quindi:

⎧i k = G kk v k + G kh v h
⎪
⎨i = G v + G v = 0 ⇒ v = − G hk v                                                                   (35)
⎪⎩ h     hk k       hh h   h
                             G hh k
Sostituendo la seconda equazione nella prima si ottiene:

      ⎛ G G − G kh G hk ⎞
i k = ⎜ kk hh           ⎟v k                                                                        (36)
      ⎝     G hh        ⎠
Dalla (36) si osserva che
G kk G hh − G kh G hk i k
                     =                                                                              (37)
        G hh           vk        i h =0
rappresenta la conduttanza vista alla porta k-esima con la porta h-esima aperta e tutte le altre porte
cortocircuitate. Nel seguito indicheremo tale conduttanza con il simbolo G ho
                                                                           k . In modo analogo:

G kk G hh − G hk G kh i h
                     =                                                                        (38)
        G kk           vh         i k =0

rappresenta la conduttanza vista alla porta h-esima con la porta k-esima aperta e tutte le altre porte
cortocircuitate. Confrontando le (37) e (38) si osserva che vale la seguente relazione:

G kk G hh − G hk G kh = G sk G ko
                               h = Gk Gh
                                    ho s
                                                                                              (39)
In generale, quindi, il coefficiente bn-2 risulta dato dalla seguente espressione:

           a n −2 N −1 N G i G j N −1 N G i G j N −1 N
                               s io                jo s
                                                                           1
b n −2 =         =∑∑                 =∑∑                = ∑ ∑ jo s                            (40)
            an    i =1 j=i +1
                              Ci C j  i =1 j=i +1
                                                  CiC j   i =1 j=i +1 R i R j C i C j

Nell’ipotesi di polo dominante in bassa frequenza (polo a frequenza maggiore di tutti gli altri poli e
zeri della funzione di trasferimento valida in bassa frequenza), la frequenza di taglio inferiore può
essere approssimata dalla seguente espressione:
       ωL b n −1   1 N 1
            2π 2π ∑
fL =      ≈      =                                                                            (41)
       2π                   s
                     i =1 R i C i




NOTE: ….
