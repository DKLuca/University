---
fonte: "amod.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Indice

I    Principi della modulazione analogica                                                5
1 Introduzione                                                                            7

2 Modulazione di ampiezza                                                                 9
  2.1 Modulazione double side band suppressed carrier (DSB-SC) . . . . . .                9
  2.2 Modulazione double side band transmitted carrier (DSB-TC) . . . . . .              13
  2.3 Realizzazione di un modulatore di ampiezza . . . . . . . . . . . . . . .           16
  2.4 Realizzazione di un demodulatore di ampiezza . . . . . . . . . . . . . .           20
  2.5 Recupero della portante nei sistemi AM . . . . . . . . . . . . . . . . .           26
  2.6 Modulazioni di ampiezza lineari: schema generale . . . . . . . . . . . .           28
  2.7 Single side band trasmission carrier (SSB-TC) . . . . . . . . . . . . . .          37
  2.8 Quadrature amplitude modulation (QAM) . . . . . . . . . . . . . . . .              37
  2.9 Accesso multiplo a divisione di frequenza (FDM) . . . . . . . . . . . .            40
  2.10 Prestazioni . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   41

3 Modulazione angolare                                                                   47
  3.1 Definizioni e parametri associati . . . . . . . . . . . . . . . . . . . . . .      47
  3.2 Narrowband FM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          51
  3.3 Wideband FM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        53
  3.4 Modulatori . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       55
  3.5 Demodulatori . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       58
  3.6 Prestazioni . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    59
  3.7 Preenfasi e deenfasi nella FM . . . . . . . . . . . . . . . . . . . . . . .        64

4 Confronto tra i vari metodi di modulazione ed esempi di sistemi                        65
  4.1 Esempi di sistemi di trasmissione analogici . . . . . . . . . . . . . . . .        65
      4.1.1 Ricevitore supereterodina . . . . . . . . . . . . . . . . . . . . .          66
      4.1.2 Radio FM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         69
      4.1.3 Radio FM stereo . . . . . . . . . . . . . . . . . . . . . . . . . .          69
      4.1.4 Segnale televisivo . . . . . . . . . . . . . . . . . . . . . . . . . .       70


II   Esercizi sui filtri numerici e FFT                                                  73
5 Filtri numerici                                                                        75
  5.1 Stabilità BIBO di un filtro numerico . . . . . . . . . . . . . . . . . . .        75
  5.2 Risposta in frequenza razionale . . . . . . . . . . . . . . . . . . . . . .        76
  5.3 Equazioni alle differenze . . . . . . . . . . . . . . . . . . . . . . . . . .      79
  5.4 L’uso di MATLAB per il progetto dei filtri . . . . . . . . . . . . . . . .         82

                                             1
2                      INDICE

6 Esercizi sulla FFT       97

Bibliografia              103
Note sulla modulazione analogica e il progetto di filtri numerici. La parte
  relativa alla modulazione è a cura del prof. N. Benvenuto. La parte
         relativa ai filtri numerici è a cura del prof. R. Rinaldo.
         Parte I

Principi della modulazione
         analogica




            5
Capitolo 1

Introduzione

In questo capitolo riportiamo le tecniche di modulazione analogiche in cui il segnale
di informazione è continuo sia nel tempo che in ampiezza. Innanzitutto chiariamo il
significato del termine modulazione: essa è una trasformazione che elabora il segnale di
informazione, ad esempio voce o video, per renderlo atto ad essere inviato sul canale di
trasmissione. Di fatto il segnale di informazione prodotto dalla sorgente è tipicamente
di tipo passa basso mentre il canale, ad esempio radio, è di tipo banda passante.
Sorge allora la necessità di traslare in frequenza il segnale prima di inviarlo sul canale
trasmissivo. Il modello di un sistema di comunicazione è riportato in Figura 1.1 in cui
a(t) è il segnale di informazione o segnale modulante mentre s(t) è il segnale modulato
ottenuto come trasformazione di a(t).


                        modulatore                                  demodulatore
                 a(t)                  s(t)                  r(t)                   ao(t)
   Sorgente                MOD                    Canale              DEMOD



                Figura 1.1: Modello di un sistema di trasmissine analogico.

Il canale, in generale, distorce s(t) ed introduce del rumore. In queste note supporremo
il canale non distorcente per cui il segnale all’ingresso del ricevitore r(t) sarà dato da
                                r(t) = GCh,0 s(t) + w(t) ,                              (1.1)
in cui GCh,0 è il guadagno del canale mentre w(t) è un rumore AWGN con PSD Pw (f ) =
N0 /2. Più comunemente si esprime GCh,0 in termini dell’attenuazione di potenza ad del
canale, come
                                                1
                                      GCh,0 = √       ,                           (1.2)
                                                ad
per cui in dB risulta
                                  (GCh,0 )dB = −(ad )dB .                         (1.3)
    In base al segnale ricevuto r(t), il compito del ricevitore è di ripristinare il segnale
di informazione a(t) fornendo una replica ao (t).
    Le tecniche di modulazione analogiche fanno riferimento ad un segnale sinusoidale,
detta portante, del tipo
                              p(t) = A cos (2πf0 t + ϕ0 ) ,                             (1.4)

                                              7
8                                                                           Introduzione


e ne variano l’inviluppo istantaneo A, fase istantanea ϕ0 e frequenza istantanea f0 [1]
in modo proporzionale al segnale modulante a(t). Ciò corrisponde rispettivamente
alle modulazioni di ampiezza (amplitude modulation, AM), di fase (phase modula-
tion, PM) e di frequenza (frequency modulation, FM). Vedremo che in effetti le PM
e FM sono caratterizzazioni della modulazione angolare, per cui verranno analizzate
congiuntamente.
     Anticipiamo che la modulazione, oltre che per traslare in frequenza il segnale mo-
dulante, viene utilizzata anche per altri due motivi: 1) stabilire un trade-off tra la
banda richiesta al canale e potenza trasmessa e 2) semplificare la realizzazione del
demodulatore.
     Nel seguito assumeremo che il segnale modulante a(t), a valori reali, sia del tipo
banda passante con una banda B come illustrato in Figura 1.2. In effetti, tipicamente
la banda passante di a(t) va da una frequenza fa,1 ad fa,2 con fa,1 > 0. In altre parole
a(t) non ha un contenuto spettrale attorno la componente continua (DC). Un esempio
è fornito dal segnale voce che, per trasmissioni telefoniche ha una banda passante che
va da 300 a 3400 Hz. D’altra parte, poichè fa,1 ¿ fa,2 , assumeremo inoltre che la banda
di a(t) sia data da B = fa,2 − fa,1 ' fa,2 . In tutto questo capitolo assumeremo inoltre
che f0 > B per le modulazioni di ampiezze e f0 À B per le modulazioni angolari.


                                         (f)




        -fa,2                           -fa,1   fa,1                         fa,2 f



Figura 1.2: Andamento in frequenza di un tipico segnale modulante a(t). Essendo a(t) reale,
la trasformata di Fourier A(f ) risulta Hermitiana, con A(−f ) = A∗ (f ).

Iniziamo con l’illustrare il principio della tecnica di modulazione double side band
(DSB) che sta alla base di tutte le modulazioni di ampiezze.
Capitolo 2

Modulazione di ampiezza

2.1     Modulazione double side band suppressed car-
        rier (DSB-SC)
L’estensione suppressed carrier sarà chiarita in seguito. Il principio della modulazione
DSB è riportato in Figura 2.1 mentre le trasformazioni dei vari segnali nel dominio
della frequenza sono illustrate in Figura 2.2.


                                                                      LPF
          a(t)           s(t)                  s(t)          u(t)              ao(t)
                                                                       h

                                                                     Banda B

           cos(2 π f0t + ϕ0 )                  cos(2 π f0t + ϕ1 )


                  a)                                            b)


            Figura 2.1: Modulazione DSB: a) modulatore e b) demodulatore.


Modulatore

Il segnale modulato è dato dal prodotto, effettuato tramite un mixer, tra il segnale
modulante a(t) e la portante,

                                s(t) = a(t) cos (2πf0 t + ϕ0 ) .                       (2.1)

Nel dominio della frequenza avremo
                                 ejϕ0              e−jϕ0
                       S(f ) =        A(f − f0 ) +       A(f + f0 ) .                  (2.2)
                                  2                  2
    Questa trasformazione è riportata in Figura 2.2 utilizzando per A(f ) l’andamento
di Figura 1.2. Notiamo che la modulazione di a(t) con la portante oltre ad attenuare il

                                               9
10                                                             Modulazione di ampiezza


segnale di un fattore 12 ha traslato le frequenze di s(t) in su e giù della frequenza della
portante f0 . Inoltre ha sfasato le componenti a frequenze positive di s(t) di ϕ0 e quelle
a frequenze negative di −ϕ0 .
    Una prima conseguenza di questa operazione è che il segnale modulato s(t) ha
una banda 2B, doppia rispetto a quella del segnale modulante. Un primo beneficio
è di avere un segnale ad alta frequenza che può essere trasmesso in modo efficiente.
Ad esempio, nei sistemi radio, in cui l’antenna deve avere delle dimensioni legate alla
lunghezza d’onda del segnale, si può utilizzare una antenna di dimensioni ragionevoli.
    Un secondo beneficio della traslazione in frequenza è che più segnali possono con-
dividere lo spettro radio senza interferenza reciproca, utilizzando per ciascun segnale
una portante f0,i tale che i vari segnali modulati non si sovrappongano in frequenza.
La Figura 2.3 illustra il segnale complessivo nel caso di due segnali.
    Questo metodo di condividere il canale tra segnali di più utenti prende il nome di
multiplazione a divisione di frequenza (frequency division multiplexing, FDM) e verrà
approfondito in seguito.
    In Figura 2.4 riportiamo un esempio della trasformazione a → s dato dalla (2.1)
per un segnale a(t) del tipo,

     a(t) = sin (2πf1 t + ϕ1 ) + 0.5 sin (2πf2 t + ϕ2 ) + 0.25 sin (2πf3 t + ϕ3 ) ,   (2.3)

con f1 = 400 Hz, f2 = 500 Hz, f3 = 600 Hz, ϕ1 = π3 , ϕ2 = π, ϕ3 = π2 . La portante
è pari a f0 = 3500 Hz. Notiamo che a meno del segno il segnale a(t) è contenuto
nell’inviluppo del segnale s(t).


Demodulatore

Come illustrato in Figura 2.1 il demodulatore, tramite un mixer, effettua il prodot-
to tra il segnale modulato s(t) e la portante cos (2πf0 t + ϕ1 ) che deve avere la stessa
frequenza e fase di quella trasmessa. Comunque per analizzare gli effetti di una possi-
bile differenza di fase, assumeremo che la fase della portante in ricezione ϕ1 possa essere
diversa da quella in trasmissione. L’uscita del mixer viene filtrata da un filtro passa
basso di banda B, pari a quella di a(t), per fornire una stima di a(t) che indicheremo
con ao (t). Analiticamente, il segnale all’uscita del mixer è dato da

              u(t) = s(t) cos (2πf0 t + ϕ1 )
                   = a(t) cos (2πf0 t + ϕ0 ) cos (2πf0 t + ϕ1 )
                          ·                                           ¸
                     a(t)
                   =        cos (ϕ0 − ϕ1 ) + cos (2π2f0 t + ϕ0 + ϕ1 )   ,             (2.4)
                       2

utilizzando note identità trigonometriche. Riconosciamo che in (2.4) a(t)
                                                                       2
                                                                           cos (ϕ0 −ϕ1 ) è
                                             a(t)
proporzionale al segnale modulante mentre 2 cos (2π2f0 t + ϕ0 + ϕ1 ) rappresenta a(t)
traslato in frequenza attorno a ±2f0 . Utilizzando un filtro h del tipo passa basso con
banda passante (0, B), per non distorcere il primo termine in (2.4), e banda attenuata
(2f0 − B, 2f0 + B), per attenuare il secondo termine in (2.4), all’uscita del filtro, di
guadagno unitario, avremo

                                              cos (ϕ0 − ϕ1 )
                              ao (t) = a(t)                    .                      (2.5)
                                                    2
2.1 Modulazione double side band suppressed carrier (DSB-SC)                                                11




                                                    (f)




                                                    -B 0 B                                                  f

                                                    (f)
                                 - jϕ                                        jϕ
                               1 e 0 (f + f )                             1 e 0 (f - f )
                               2           0                              2           0




                          -f-B     -f       -f +B             0       f -B     f     f+B                    f
                           0            0    0                        0         0    0


                                                    (f)




                                                                                                            f

-2f -B    -2 f   2 f +B                             -B 0 B                                 2f -B 2 f     2f +B
  0          0       0                                                                      0       0       0

                                                    (f)
                                                              1
                                                                  1


                                                                                                                f

 -2 f - B    -2 f + B                               -B 0 B                                 2f - B      2f + B
      0          0                                                                              0       0


                                                    o
                                                        (f)




                                                    -B 0 B                                                  f



Figura 2.2: Illustrazione dei vari segnali nel dominio della frequenza in una modulazione
DSB.
12                                                                       Modulazione di ampiezza




                                                 (f) +   (f)
                                                 1       2




                  -f                  -f                       f                    f             f
                       0,2                 0,1                     0,1                  0,2




                  Figura 2.3: Principio della multiplazione a divisione di frequenza.




        1.5

         1

        0.5
a(t)




         0

       −0.5

        −1

       −1.5
              0              1   2           3       4             5        6       7         8
                                                         t                                    x 10
                                                                                                      −3




        1.5

         1

        0.5
s(t)




         0

       −0.5

        −1

       −1.5
              0              1   2           3       4             5        6       7         8
                                                         t                                    x 10
                                                                                                      −3




Figura 2.4: Esempio di segnale di informazione a(t) e corrispondente segnale modulato DSB.
2.2 Modulazione double side band transmitted carrier (DSB-TC)                                   13


In effetti, notiamo che il segnale modulante viene ricostruito a meno di una costante
pari a cos (ϕ20 −ϕ1 ) . Di conseguenza è molto importante che ϕ1 = ϕ0 , altrimenti il segnale
ricostruito risulta ulteriormente attenuato.


2.2         Modulazione double side band transmitted car-
            rier (DSB-TC)
Una formulazione generale della DSB porta ad avere un segnale modulato s(t) del tipo
                  s(t) = a(t) cos (2πf0 t + ϕ0 ) + A cos (2πf0 t + ϕ0 )
                         ¡         ¢
                       = a(t) + A cos (2πf0 t + ϕ0 ) ,                                       (2.6)
cioè oltre al segnale modulato per la portante viene trasmessa la portante stessa. Poichè
la trasformata di Fourier della portante comporta un paio di delta di Dirach alle fre-
quenze ±f0 , l’andamento in frequenza di un tipico segnale modulato in ampiezza con
portante trasmessa è riportato in Figura 2.5.


                                                   (f)
               1       -j ϕ                                             1   jϕ
                 Ae 0 δ(f +f0 )                                           Ae 0 δ(f -f0 )
               2                                                        2
                                1 e-j ϕ0 (f +f )                                      1 e j ϕ0 (f -f )
                                              0                                                     0
                                2                                                     2




      -f0 -B     -f0          -f0+B                      0       f0-B     f0        f0+B



Figura 2.5: Andamento in frequenza di un segnale modulato DSB con trasmissione della
portante.

    Come nella DSB-SC, la banda della DSB-TC è pari a 2B, doppia di quella del
segnale modulante. Una diversità tra DSB-SC e DSB-TC è che in quest’ultima la
trasformazione a → s non è più lineare.
    Introduciamo il valore minimo di a(t), in valore assoluto,
                                          am = − min a(t) .                                  (2.7)
                                                             t

    Se a(t) è un processo aleatorio con ampiezza non limitata, am viene definito tramite
la probabilità ε che il segnale assuma valori inferiori a −am ,
                                     £           ¤
                                   P a(t) < −am = ε ,                                (2.8)
con ε ¿ 1. Tipicamente ε ∈ {10−3 , 10−4 }. Ad esempio se a(t) è un processo aleatorio
gaussiano con media nulla e varianza σa2 risulta
                                           am = σa Q−1 (ε) ,                                 (2.9)
14                                                         Modulazione di ampiezza


dove Q−1 è la funzione inversa della funzione Q definita in [1]. Per ε = 10−3 si ha
che Q−1 (10−3 ) = 3.05 e quindi am ' 3.05 σa . In altre parole le ampiezze di a(t) sono
inferiori a −am = −3.05 σa con probabilità 10−3 .
    Nel dominio del tempo, per un segnale a(t) del tipo (2.3), riportiamo in Figura
2.6 il corrispondente segnale modulato DSB-TC nei due casi: i) per A < am e ii) per
A > am .




                1
  a(t)




                0


         −1

                    0   1             2   3   4   t    5         6         7         8
                                                                                         −3
                                                                                    x 10
                2
                            A = 0.5am
 s(t), A < am




                1

                0

         −1

         −2
                    0   1             2   3   4   t    5         6         7         8
                                                                                         −3
                                                                                    x 10
                4           A = 2am
s(t), A > am




                2

                0

         −2

         −4
                    0   1             2   3   4   t    5         6         7         8
                                                                                         −3
                                                                                    x 10



Figura 2.6: Andamento nel tempo del segnale modulante e corrispondente segnale modulato
in ampiezza con trasmissione della portante (DSB-TC): a) segnale modulante a(t), b) s(t)
per A < am , c) s(t) per A > am .


   Notiamo che nel caso A > am , denominata anche condizione per l’assenza di distor-
sione dell’inviluppo, l’inviluppo del segnale s(t) coincide con a(t) + A. Nel caso A < am
invece l’inviluppo di s(t) coincide con |a(t) + A|.
   In effetti è importante stabilire il rapporto tra am ed A che prende il nome di indice
di modulazione
                                              am
                                          m=        .                               (2.10)
                                              A
    Notiamo che m > 0 e la scelta A > am corrisponde ad un indice di modulazione
inferiore ad 1.
2.2 Modulazione double side band transmitted carrier (DSB-TC)                          15


   Introduciamo inoltre il segnale di informazione normalizzato in ampiezza
                                                 a(t)
                                       ā(t) =                .                    (2.11)
                                                 am
   Assumendo, come si verifica di solito, che maxt a(t) = − mint a(t), ā(t) risulta un
segnale con ampiezza limitata -1 e 1; in ogni caso il valore minimo è -1.
   Utilizzando la (2.10) e (2.11), una forma alternativa alla (2.6) è data da
                                ¡          ¢
                      s(t) = A 1 + m ā(t) cos (2πf0 t + ϕ0 ) .                  (2.12)

   Questa formulazione è quella più generale di un segnale AM.
   Introduciamo alcuni parametri associati al segnale (2.12).

POTENZA. Definiamo la potenza di un generico segnale x(t)
                                                 Z Tw
                                       1              2
                            Mx = lim                          x2 (t) dt .          (2.13)
                                Tw →∞ Tw          − T2w

    Questa£definizione
                 ¤     coincide con la potenza statistica di un processo aleatorio defini-
ta come E x2 (t) , atteso che il processo aleatorio sia ergodico.

FATTORE DI FORMA. Associato al segnale normalizzato ā(t), definiamo la sua
potenza come
                                     Ma
                         kf2 = Mā = 2 ,                              (2.14)
                                    am
dove l’ultima uguaglianza discende dalla (2.11). Ad esmpio se a(t) è un segnale sinu-
soidale risulta kf = √12 , mentre se a(t) ha una distribuzione di ampiezza uniforme tra
−am e am si ha che kf = √13 . Infine, se a(t) ha una distribuzione di ampiezza gaussiana
con media nulla allora kf = Q−11 (ε) .

EFFICIENZA DELLA MODULAZIONE. In base alla struttura della (2.6) o (2.12)
del segnale modulato, l’efficienza η della modulazione DSB-TC è definita dal rapporto
tra la potenza del termine desiderato che porta l’informazione a(t) cos (2πf0 t + ϕ0 )
e la potenza del segnale complessivo s(t). D’altra parte se f0 > B la potenza di
a(t) cos (2πf0 t + ϕ0 ) è pari a M2a per cui
                                                 Ma
                                                  2
                                         η=               .                        (2.15)
                                                 Ms
Ora sempre sotto l’ipotesi che f0 > B dalla (2.12) risulta
                                       A2 ¡           ¢
                                Ms =        1 + m2 Mā .                           (2.16)
                                       2
Utilizzando la (2.14) risulta
                                       A2 ¡           ¢
                                Ms =       1 + m2 kf2   ,                          (2.17)
                                       2
mentre dalla (2.11) si ha
                                       Ma = a2m kf2           .                    (2.18)
16                                                                       Modulazione di ampiezza


   Sostituendo (2.17) e (2.18) in (2.15) ed utilizzando la definizione di indice di mo-
dulazione (2.10), risulta
                                         m2 kf2
                                   η=               .                             (2.19)
                                       1 + m2 kf2
    Notiamo che più piccolo è l’indice di modulazione m minore è l’efficienza di modu-
lazione η. In particolare, essendo kf < 1, per m < 1 risulta η < 12 .


2.3      Realizzazione di un modulatore di ampiezza

                         a(t)               b(t)                 s(t)




                                    A           cos(2 π f0t + ϕ0 )



           Figura 2.7: Modulatore di ampiezza con trasmissione della portante.

    Uno schema che realizza la modulazione di ampiezza è riportato in Figura 2.7. Esso
fa uso di un oscillatore a frequenza f0 la cui uscita viene moltiplicata per il segnale
b(t) = a(t) + A tramite un mixer. Naturalmente per A = 0 abbiamo come caso
particolare la DSB-SC.
    Un’alternativa all’oscillatore che produce la portante è utilizzare un segnale perio-
dico di periodo T0 = f10 , ad esempio un treno di impulsi rect del tipo

                                         +∞
                                         X             µ             ¶
                                                           t − nT0
                                p(t) =          rect                      ,                (2.20)
                                         n=−∞
                                                             dT0



dove d, 0 < d < 1, esprime la durata del generico impulso normalizzata al periodo T0 di
p(t). Il segnale p(t) è illustrato in Figura 2.8 per d = 0.25. Notiamo che se f0 è molto
eleveta la durata del generico impulso rect può risultare molto corta. Utilizzando per
p(t) la espressione (2.20) il modulatore viene riportato in Figura 2.9. Il vantaggio di
utilizzare come impulso fondamentale un rect è che il prodotto di b(t) con p(t) viene
sostituito da un interrutore che “fa passare” il segnale b(t) ogni T0 secondi per una
durata di dT0 secondi.
    Tramite lo sviluppo in serie di Fourier di p(t) risulta
                                          ∞
                                          X
                      p(t) = d + 2d             sinc(kd) cos (2πkf0 t) .                   (2.21)
                                          k=1


    Come illustrato in Figura 2.10, il prodotto di p(t) con il segnale b(t) produce in
frequenza tante repliche di B(f ) attorno alle frequenze kf0 , k = 0, 1, 2, ..., di ampiezza
rispettivamente d sinc (kd).
2.3 Realizzazione di un modulatore di ampiezza                                                                           17



                                              p(t)



             ...                                                                                           ...

                     - 2T           -T                  0                     T                  2T              t
                         0               0    -dT           dT                0                   0
                                                    0           0
                                                2           2
                                                                     dT                dT
                                                                          0                  0
                                                            T-                    T+
                                                             0                    0
                                                                      2                  2


                         Figura 2.8: Treno di impulsi rect con d = 0.25.



                                                             PBF
                             b(t)            u(t)                                 s(t)
                                                                h
                                                                    PB




                                     p(t)


                 Figura 2.9: Modulatore di ampiezza a tenuta (gated modulator).




       (f)                                                                                        d = 0.5
                             2d sinc(d) (f - f )                                                  f0 = 3500
                                                0

 ...
                                                                                                      3f
                                                                                                           0

             0                       f                               2f                                          ...
                                         0                                0
                                                                                         2d sinc(3d) (f - 3f )
                                                                                                                     0



Figura 2.10: Andamento in frequenza del segnale u(t), prodotto di b(t) per un treno di
impulsi rect di durata normalizzata d = 21 .
18                                                             Modulazione di ampiezza


   Per selezionare la replica attorno a f0 è sufficiente utilizzare un filtro del tipo banda
passante hP B con centro banda f0 e banda 2B. Se il guadagno di hP B è unitario alla
sua uscita avremo

                         s(t) = b(t) 2d sinc (d) cos (2πf0 t)
                                     2
                              = b(t)    sin (πd) cos (2πf0 t) .                        (2.22)
                                     π

     Tipicamente d = 21 e
                                        2
                               s(t) =     b(t) cos (2πf0 t) .                          (2.23)
                                        π
Le varie trasformazioni dello schema di Figura 2.9 sono illustrate in Figura 2.11.
   Uno schema alternativo è rappresentato dal modulatore con legge quadratica (square-
law modulator), riportato in Figura 2.12. A partire dal segnale modulante b(t) e la
portante, si effettua la loro somma,

                             v(t) = b(t) + cos (2πf0 t + ϕ0 ) .                        (2.24)

     Ora si trasforma v(t) in modo non lineare, ad esempio tramite una legge quadratica

                                        u(t) = v 2 (t) ,                               (2.25)

che tra i vari termini conterrà il prodotto desiderato tra b(t) e cos (2πf0 t + ϕ0 ). Infatti
la (2.24) in (2.25) fornisce

              v 2 (t) = b2 (t) + cos2 (2πf0 t + ϕ0 ) + 2b(t) cos (2πf0 t + ϕ0 ) ,      (2.26)

con un contenuto attorno DC di banda 2B, una riga in ±2f0 e il segnale modulato
desiderato attorno a ±f0 . Per selezionare il termine desiderato si utilizza un filtro del
tipo banda passante centrato in f0 .
    Più in generale al posto della (2.25) è sufficiente utilizzare un elemento non lineare
avente legame ingresso-uscita con uno sviluppo in serie del tipo

                        u(t) = c1 v(t) + c2 v 2 (t) + c3 v 3 (t) + ... ,               (2.27)

dove il termine desiderato è in v 2 (t). Ebbene, se c’è un modo per isolare questo ter-
mine l’elemento non lineare (2.27) può essere utilizzato al posto di quello quadratico
(2.25). Ad esempio, un diodo a semicondutore fornisce tra i terminali di uscita e di
ingresso una legge non lineare data dai primi due termini della (2.27) e può quindi es-
sere usato come approssimazione della legge quadratica. Notiamo che se in (2.27) con
uno sviluppo fino al termine quadratico risulta c1 ' 0, allora possiamo utilizzare un
modulatore con legge quadratica per realizzare una DSB-SC. Nel caso c1 6= 0 avremo
anche una riga attorno a ±f0 dovuta al termine c1 v(t). Se nell’elemento non lineare
appaiono anche termini del terzo ordine che creano interferenza al termine desiderato,
si può utilizzare il metodo di cancellazione di Figura 2.13 per rimuovere i termini con
esponente dispari del tipo b(t) e b3 (t).
2.3 Realizzazione di un modulatore di ampiezza                                                     19




                                         (f)




                                        -B 0       B                                           f

                                         (f)


       2d sinc(d)       (f + f )                                2d sinc(d)      (f - f )
                              0                                                      0



    ...                                                                                  ...


      -f - B   -f       -f + B          -B 0 B                   f -B   f       f +B           f
          0         0     0                                       0         0   0


                                         (f)
                                       PB

                                               1




      -f - B   -f       -f + B                                   f -B   f       f +B           f
          0         0     0                                       0         0   0

                                         (f)




      -f - B   -f       -f + B                                   f -B   f       f +B           f
          0         0     0                                       0         0   0




  Figura 2.11: Illustrazione delle trasformazioni introdotte dallo schema di Figura 2.9.
20                                                                 Modulazione di ampiezza


                                                                    PBF
                    b(t)          v(t)   Elemento       u(t)                       s(t)
                                            non                     h PB
                                          lineare


                    cos(2 π f0t + ϕ0 )



         Figura 2.12: Modulatore di ampiezza con legge quadratica (square-law modulator).

         b(t)                      Elemento
                                      non
                                    lineare
                                                                               PBF
                                                               +                           s(t)
            cos(2 π f0t + ϕ0 )                                                 h
                                                                                   PB
                                                               -
         -b(t)                     Elemento
                                      non
                                    lineare



                 Figura 2.13: Modulatore di ampiezza bilanciato (balanced modulator ).


2.4              Realizzazione di un demodulatore di ampiezza
I demodulatori vengono suddivisi in due classi: coerenti e non coerenti. Nel caso
coerente il ricevitore fa uso della conoscenza sia della frequenza che della fase della
portante trasmessa1 . In altre parole, oltre alla forma d’onda della portante trasmessa
(individuata dalla frequenza f0 ) bisogna conoscere anche la temporizzazione (indivi-
duata dalla fase ϕ0 ) con cui arriva la portante all’ingresso del ricevitore. Schemi non
coerenti prescindono da queste conoscenze.


Demodulatori coerenti

Lo schema base di un demodulatore coerente è riportato in Figura 2.1b e consiste
nel rimodulare s(t) tramite la portante, o meglio una stima della portante, e filtrare il
prodotto tramite un filtro passa basso.
    Anche in questo caso il prodotto tra s(t) e la portante locale può essere effettuato
tramite uno degli schemi visti per il modulatore. Rivediamoli in dettaglio. Lo schema
gated demodulator è riportato in Figura 2.14 dove p(t) è un treno di impulsi sincroniz-
zati con quelli di trasmissione.


     1
   In effetti dovremo dire della portante trasmessa valutata però all’uscita del canale. Nel nostro
modello, essendo il canale ideale, le due locuzioni sono uguali.
2.4 Realizzazione di un demodulatore di ampiezza                                                   21


                                       gate                     LPF
                            s(t)                                             a (t)
                                                                                  o
                                                                    h



                                           p(t)


                                   Figura 2.14: Gated demodulator.

   Per p(t) del tipo (2.20) risulta

                                                         sin (πd)
                                            ao (t) =              b(t) ,                        (2.28)
                                                             π
dove b(t) = a(t) nel caso DSB-SC mentre b(t) = a(t) + A nel caso DSB-TC. In quest’ul-
timo caso per ottenere una replica di a(t) bisogna rimuovere la componente continua
di ao (t) tramite un filtro notch con guadagno nullo per f = 0 (DC). Naturalmente se
a(t) ha un contributo a DC il filtro notch introdurrà distorsione.
    Lo schema square-law demodulator, riportato in Figura 2.15, è invece scarsamente
utilizzato nei sistemi DSB-SC mentre si presta per sistemi DSB-TC con A > am (in tal
caso non serve la portante in ricezione e K = 0). Consideriamo la relazione generale

                                 c(t) = s(t) + K cos (2πf0 t + ϕ1 ) ,                           (2.29)

per un elemento non lineare di tipo quadratico,

                                                  d(t) = c2 (t) .                               (2.30)

Un segnale DSB-SC s(t) = a(t) cos (2πf0 t + ϕ0 ) per ϕ1 = ϕ0 porge
                        ¡       ¢2
            d(t) =    a(t) + K cos2 (2πf0 t + ϕ0 )
                     1 ¡           ¢2 1 ¡         ¢2
                   =     a(t) + K +      a(t) + K cos (2π2f0 t + 2ϕ0 ) .                        (2.31)
                     2                2




                                                              LPF
     s(t)        c(t)                             d(t)                     x(t)            a (t)
                                       2                                                    o
                             (     )                            h                     ()

                                                           Banda 2B

    K cos(2 π f0t + ϕ1 )



                     Figura 2.15: Square-law demodulator per DSB-SC.
22                                                                        Modulazione di ampiezza


   Ora il secondo termine può essere rimosso da un filtro passa basso, alla cui uscita
rimane
                       1 ¡         ¢2 1 ¡ 2                      ¢
                x(t) =     a(t) + K =      a (t) + 2K a(t) + K 2 .               (2.32)
                       2                 2
                                                                           2
    Purtroppo in (2.32) non è possibile isolare il termine
                                                        ¡ a(t) dal
                                                                ¢ termine a (t) poichè
i due termini si sovrappongono in frequenza. Solo se a(t) + K è non negativo2 , cioè
per K > am , allora prendendo la radice quadrata di (2.32) avremo
                              p           1 ¯        ¯    1 ¡       ¢
                  ao (t) =        x(t) = √ ¯a(t) + K ¯ = √ a(t) + K   ,                     (2.33)
                                           2               2

ottenendo un segnale legato ad a(t) a meno della DC.
    Notiamo che se in (2.29) utilizziamo una portante in ricezione con ϕ1 6= ϕ0 , allora
potremo ricorrere al quadrature demodulator di Figura 2.16, per ottenere in generale,
sia per DSB-SC che DSB-TC,

                                                          1 ¯¯     ¯
                                               ao (t) =        b(t)¯ .                      (2.34)
                                                          2




                                       LPF

                                           h                     (   )2



                             cos(2 π f0t + ϕ1 )

  s(t)                                                                                      a (t)
                                                                                             o
                - π                                                                    ()
                  2

                      sin(2 π f0t + ϕ1 )
                                       LPF

                                           h                     (   )2



                      Figura 2.16: Quadrature demodulator per DSB-TC.

Anche questo schema però è di scarsa qualità se non per una modulazione DSB-TC
con A > am .


Demodulatori non coerenti

Questi schemi prescindono dal recupero della portante in ricezione. L’incoveniente
     2
   Sottolineamo che in questa diseguaglianza K è una ampiezza generata localmente al ricevitore
mentre am è l’ampiezza minima del segnale ricevuto che spesso non è nota.
2.4 Realizzazione di un demodulatore di ampiezza                                          23


è che bisogna trasmettere la portante ad un livello sufficientemente elevato in modo
che
                                a(t) + A ≥ 0     ∀t ,                            (2.35)
cioè deve essere
                                          A ≥ am          ,                           (2.36)
dove am è definito in (2.7). Vediamo due schemi applicati¡alla DSB-TC.
                                                                   ¢    Lo square-law
demodulator viene riportato in Figura 2.17 in cui s(t) = a(t) + A cos (2πf0 t + ϕ0 ).


                                                LPF
          s(t)                   d(t)                           x(t)        a (t)
                             2                                                o
                     (   )                       h                     ()

                                         Banda 2B


                    Figura 2.17: Square-law demodulator per segnali AM.

   All’uscita¡ del filtro ¢h di tipo passa basso, di banda 2B per far passare ¡le armoniche
                                                                                         ¢2
                            2
del segnale a(t) + A , avremo solo il termine a bassa frequenza 21 a(t) + A .
Prendendo la radice quadrata avremo
                                           1 ¯       ¯
                                 ao (t) = √ ¯a(t) + A¯ .                              (2.37)
                                            2
Se A > am il segnale all’uscita risulta proporzionale al segnale di informazione a meno
di una componente continua, che al solito viene rimossa utilizzando un filtro notch,
                                           1 ¡      ¢
                                 ao (t) = √ a(t) + A .                                (2.38)
                                            2
    Per un segnale a(t) del tipo riportato in Figura 1.2, il filtro notch avrà le specifiche
riportate in Figura 2.18.



                                                     1




           -fa,2                        -fa,1            fa,1                fa,2



    Figura 2.18: Specifiche del filtro notch per rimuovere la componente continua.

   Al posto della funzione quadratica in Figura 2.17 si può utilizzare un raddrizzatore
a onda piena o a semionda le cui relazioni ingresso-uscita sono le seguenti.
24                                                                Modulazione di ampiezza



raddrizzatore a onda piena
                                            ½
                                 ¯    ¯          s(t) , s(t) > 0
                          d(t) = ¯s(t)¯ =                             ,                   (2.39)
                                                −s(t) , s(t) < 0

raddrizzatore a semionda
                                        ½
                                            s(t) , s(t) > 0
                               d(t) =                             .                       (2.40)
                                             0 , s(t) < 0

Consideriamo il primo caso per
                             ¯    ¯ ¯           ¯¯                   ¯
                      d(t) = ¯s(t)¯ = ¯a(t) + A¯ ¯ cos (2πf0 t + ϕ0 )¯ .                   (2.41)
                                     ¯        ¯
    Ora dalla (2.35) abbiamo che¯ ¯a(t) + A¯ = a(t)¯ + A. Inoltre, considerato lo sviluppo
in serie di Fourier della funzione ¯ cos (2πf0 t+ϕ0 )¯, periodica di periodo (2f10 ) , otteniamo
                                             ∞
                                             X
                 ¯                   ¯
                 ¯ cos (2πf0 t + ϕ0 )¯ = 2 +   ck cos (2π2kf0 t + ϕ0 ) .                  (2.42)
                                         π k=1

   Allora d(t) è dato dalla somma di repliche di b(t) = a(t) + A attorno DC, ±2f0 ,
±4f0 , ... . Se 2f0 − B > B, cioè per f0 > B, all’uscita del LPF h rimarrà solo il primo
termine e
                                          2 ¡         ¢
                                 ao (t) =     a(t) + A .                             (2.43)
                                          π
   Questo schema è riportato in Figura 2.19 e prende il nome di rectifier demodulator.


                                                           LPF
                   s(t)                                                   a (t)
                                                                           o
                                                              h




                                        Envelope detector


                    Figura 2.19: Rectifier demodulator per segnali AM.

   Nel dominio del tempo le trasformazioni introdotte da un raddrizzatore a onda
piena sono illustrate in Figura 2.20.
   È interessante osservare che tale operazione coincide con moltiplicare s(t) per un
treno di impulsi avente la stessa frequenza, T10 = f0 , e fase della portante in ricezione,
dato da                                           Ã           !
                                   +∞
                                   X                       T0
                                                    t  − k
                        pRc (t) =      (−1)k rect           2
                                                                   ,                 (2.44)
                                  k=−∞
                                                       dT 0

con T0 = f10 e d = 12 .
2.4 Realizzazione di un demodulatore di ampiezza                                            25




                  3.5

                  1.5
s(t)



          −0.5

          −2.5

          −4.5
                        0   1        2            3       4       t   5    6       7    8
                                                                                            −3
                                                                                       x 10
                   4
  d(t) = |s(t)|




                   3
                   2
                   1
                   0
                        0   1        2            3       4       t   5    6       7    8
                                                                                            −3
                                                                                       x 10
                   1

                  0.5
 p (t)




                   0
       Rc




          −0.5

                  −1
                        0   1        2            3       4       t   5    6       7    8
                                                                                            −3
                                T0                                                     x 10



Figura 2.20: Andamento segnale AM e corrispondente segnale all’uscita del raddrizzatore a
onda piena.




                                          Diodo




                            s(t)                      R       C            a (t)
                                                                               o




                                         Figura 2.21: Envelope detector.
26                                                                Modulazione di ampiezza


    La cascata del raddrizzatore e del filtro h prende il nome di rivelatore di inviluppo
o envelope detector poichè fornisce l’inviluppo del segnale s(t). Se f0 À B l’envelope
detector può essere realizzato tramite un semplice diodo seguito da un filtro RC, come
illustrato in Figura 2.21.
    In questo schema mentre il condensatore tende a caricare l’uscita ao (t) al valore
massimo di ingresso, la resistenza permette un discarica della tensione quando l’ingresso
s(t) è inferiore a ao (t). Le due operazioni sono illustrate in Figura 2.22. Naturalmente
deve essere
                                             1
                                      B¿        ¿ f0 .                               (2.45)
                                           RC




                         ao(t)


                                                                                t
                         s(t)




Figura 2.22: Illustrazione delle operazioni effettuate da un envelope detector nel dominio del
tempo.




2.5      Recupero della portante nei sistemi AM
Abbiamo evidenziato precedentemente come sia importante nei sistemi AM con de-
modulazione coerente fare in modo che la frequenza e fase della portante in ricezione
siano uguali a quelle della portante trasmessa. Per ottenere ciò è fondamentale derivare
(stimare) questi parametri dal segnale ricevuto.
    Per tutti i casi AM un primo schema è trasmettere assieme al segnale di informazione
anche la portante, per cui otteniamo un segnale DSB-TC

                  s(t) = a(t) cos (2πf0 t + ϕ0 ) + A cos (2πf0 t + ϕ0 ) .                 (2.46)

   Un metodo per estrarre la portante trasmessa è utilizzare un filtro a banda stretta,
avente una banda BN BF , sintonizato sul valore nominale di f0 . Come illustrato in
Figura 2.23, all’uscita del filtro hN BF , supposto ideale e con guadagno unitario, avremo
                                     Z f0 + BN BF
                                                2        £                        ¤
  pRc (t) = A cos (2πf0 t + ϕ0 ) +                   2 Re A(f − f0 ) ej(2πf t+ϕ0 ) df   . (2.47)
                                             BN BF
                                      f0 −     2
2.5 Recupero della portante nei sistemi AM                                               27


                     s(t)                          p (t)
                                                    Rc
                                     h                            Al demodulatore
                                     NBF



               Figura 2.23: Filtro a banda stretta per estrarre la portante.




    Se il filtro hN BF ha una banda sufficientemente stretta e/o il contenuto di a(t) è
piccolo attorno DC, il secondo termine in (2.47) può essere reso sufficientemente piccolo
rispetto al primo termine. Di conseguenza pRc (t) risulta una replica della portante
trasmessa.
    Una alternativa al filtro a banda stretta è utilizzare un phase locked loop (PLL),
come illustrato in Figura 2.24, il quale fa uso di un oscillatore controllato in tensione
(voltage controlled oscillator, VCO) la cui fase istantanea insegue quella della compo-
nente


                               Comparatore
                      s(t)       di fase

                                     PD                           Loop filter

                   v(t)
                                                                        u(t)
                                                    VCO


                             p (t)
                              Rc
                                         Al demodulatore


                 Figura 2.24: Phase locked loop per estrarre la portante.

periodica del segnale di ingresso s(t). Il recupero della portante, anche in presenza del
rumore introdotto dal canale, è analizzato in [1, cap. 14]. Qui richiamiamo solo la
relazione ingresso-uscita
                                         µ                  Z t               ¶
                     v(t) = A sin            2πf0 t + 2πK          u(τ ) dτ       .   (2.48)
                                                             −∞


   A regime l’errore di fase tra il segnale d’ingresso e v(t) sarà nullo e u(t) = 0. In tal
caso v(t) riprodurrà la portante a meno di uno sfasamento di π2 .
   In assenza di trasmissione della portante, in ricezione vengono utilizzate trasfor-
mazioni non lineari sul segnale per creare delle righe spettrali che successivamente
vengono estratte tramite un PLL.
28                                                                                Modulazione di ampiezza


2.6            Modulazioni di ampiezza lineari: schema gene-
               rale
Oltre alla DSB esistono altre due tecniche di modulazione di ampiezza lineari che
vengono spesso utilizzate.
     Lo schema generale di un modulatore di ampiezza lineare, cioè senza trasmissione
della portante, è illustrato in Figura 2.25 e consiste di un mixer, che effettua il prodotto
tra il segnale modulante a(t) e la portante cos (2πf0 t + ϕ0 ), seguito da un opportuno
filtro del tipo banda passante hP B . Prima di essere inviato sul canale il segnale viene
amplificato ad un opportuno livello.

                                   Amplificatore con           Amplificatore più
                                   guadagno A Tx               filtro elimina rumore

                         PBF                                                                                 LPF
    a(t)        ap (t)                           s(t)   r(t)                       r (t)                              ro (t)
                                                                                       Rc
                         h                                             h                                       h
                          PB                                             Rc
                                          A Tx
                                                                                                            Banda B

    cos(2 π f0t + ϕ0 )                                                                 cos(2 π f0t + ϕ 1)

                         a)                                                                   b)



Figura 2.25: Schema base di un modulatore di ampiezza lineare: a) trasmettitore, b)
ricevitore.

      Definito il segnale
                                    ap (t) = a(t) cos (2πf0 t + ϕ0 ) ,                                                (2.49)
l’espressione del segnale modulato è data da
                                          ¡       ¢
                             s(t) = AT x ap ∗ hP B (t) .                                                              (2.50)

      Nel dominio della frequenza queste relazioni diventano

                                         ejϕ0              e−jϕ0
                              Ap (t) =        A(f − f0 ) +       A(f + f0 ) ,                                         (2.51)
                                          2                  2
e
                                         S(t) = AT x Ap (f ) HP B (f ) .                                              (2.52)
    In ricezione, il segnale r(t) all’uscita del canale viene amplificato e filtrato mediante
un filtro hRc avente una banda passante uguale a quella del segnale desiderato s(t);
questa specifica porta ad eliminare il rumore introdotto dal canale al di fuori della
banda desiderata.
    Il ricevitore, utilizzando un mixer, prende il segnale filtrato rRc (t) e lo moltiplica
per una portante che deve avere la stessa frequenza e fase della portante all’uscita del
canale.
    Inizialmente ci poniamo nelle condizioni di canale ideale e assenza di rumore per
cui r(t) = s(t). Inoltre, con riferimento allo schema di Figura 2.25 cosidereremo solo
le trasformazioni introdotte dalla modulazione e demodulazione, come riportato in
Figura 2.26.
2.6 Modulazioni di ampiezza lineari: schema generale                                                   29


                                PBF                                                         LPF
   a(t)         ap (t)                        s(t)               s(t)           u(t)              a (t)
                                                                                                   o
                                    h                                                        h
                                     PB




    cos(2 π f0t + ϕ0 )                                            cos(2 π f0t + ϕ 1)


                         a)                                                            b)



Figura 2.26: Schema base di un modulatore di ampiezza lineare: a) modulatore, b)
demodulatore.

    Notiamo che in ricezione il filtro hRc è stato omesso poichè irrilevante in assenza del
rumore. È stato omesso anche l’amplificatore di trasmissione dal momento che il suo
effetto si manifesta semplicemente tramite un fattore di scala che però non modifica la
forma del segnale trasmesso s(t).
    La scelta del filtro hP B determina il tipo di modulazione di ampiezza. Vediamo tre
casi tipici.
    Il primo schema è la modulazione DSB-SC trattata in Sezione 2.1. Essa è ottenuta
omettendo il filtro hP B in Figura 2.26, come si può osservare dallo schema di Figura
2.1.


Single side band (SSB)

Modulatore con filtro in banda passante

La tecnica di modulazione a banda laterale unica prevede di trasmettere metà spettro
di a(t), ad esempio quello a frequenze positive
                                             ½
                      (+)                       A(f ) , f > 0
                    A (f ) = A(f ) 1(f ) =                      ,              (2.53)
                                                 0    , f <0
o quello a frequenze negative
                                                            ½
                              (−)                   0     , f >0
                         A          (f ) = A(f ) 1(−f ) =          .              (2.54)
                                                  A(f ) , f < 0
                                             £          ¤∗
   Poichè a(t) è reale risulta A(−) (f ) = A(+) (−f ) , per cui dato A(+) (f ) oppure
A(−) (f ) è immediato risalire al segnale complessivo dato da
                                          A(f ) = A(+) (f ) + A(−) (f ) .                         (2.55)
    Illustriamo in dettaglio il caso di trasmissione della banda laterale superiore (upper
side band ), o SSB+ . In questo caso la caratteristica del filtro hP B deve essere tale da
rimuovere le componenti di ap (t) nell’intervallo di frequenze (f0 − B, f0 ). Le specifiche
ideali di hP B in frequenza sono le seguenti
                                 
                                  1            , |f |²(f0 , f0 + B)
                     HP B (f ) =    0           , |f |²(f0 − B, f0 ) .               (2.56)
                                 
                                    irrilevante , altrove
30                                                                      Modulazione di ampiezza


    In pratica, sfruttando il fatto che a(t) non ha componenti vicino la continua, le
specifiche di HP B (f ) possono avere una banda di transizione tra (−fa,1 +f0 ) e (fa,1 +f0 ),
dove ricordiamo fa,1 è l’estremo inferiore della banda passante di a(t). L’introduzione
di questa banda di transizione rende il filtro realizzabile.
    In trasmissione viene inviato il segnale s(t) legato ad a(t) dalla relazione in frequenza

                                     S(f ) = Ap (f ) HP B (f ) ,                           (2.57)

dove Ap (f ) è dato dalla (2.51). Utilizzando la (2.56) in (2.57) e le (2.53) e (2.54) risulta

                    ejϕ0                         e−jϕ0
           S(f ) =       A(f − f0 ) 1(f − f0 ) +       A(f + f0 ) 1(−f − f0 )
                     2                             2
                    ejϕ0 (+)             e−jϕ0 (−)
                  =      A (f − f0 ) +          A (f + f0 ) .                              (2.58)
                     2                     2
Le varie trasformazioni sono illustrate in Figura 2.27 .
    Ora la banda di s(t) è B, pari a quella di a(t). Notiamo che la modulazione SSB
richiede metà banda rispetto alla DSB. Naturalmente ciò è possibile al costo di una
maggiore complessità realizzativa. Infatti è stato introdotto il filtro di trasmissione
hP B . Inoltre, per non introdurre distorsione, il recupero della frequenza e fase della
portante tramite il PLL deve essere alquanto accurato. Infatti vedremo che un offset
di fase tra la portante in trasmissione e quella in ricezione non si ripercuote solamente
in una attenuazione del segnale di informazione ma anche in una componente di dis-
torsione.


Modulatore con filtro in banda base

Un
¡ πmetodo
    ¢      alternativo per realizzare il modulatore SSB è tramite il filtro di Hilbert
 − 2 avente una risposta in frequenza data da
                                                                  ½
                    (h)                       −j π2 sgn(f )           −j , f > 0
                H         (f ) = −j sgn(f ) = e               =                    .       (2.59)
                                                                       j , f <0

    In altre parole il filtro di Hilbert sfasa le armoniche a frequenze positive del segnale
di ingresso di − π2 e quelle a frequenze negative di π2 . Ad esempio, per un segnale di
ingresso del tipo cos (2πf0 t + ϕ0 ) l’uscita del filtro di Hilbert è data da sin (2πf0 t + ϕ0 ).
    Riportiamo ora una propietà che verrà utilizzata in seguito: un segnale a(t) e il
corrispondente segnale trasformato secondo il filtro di Hilbert a(h) (t) sono ortogonali,

                                         < a , a(h) >= 0 .                                 (2.60)

     Infatti poichè nel dominio della frequenza

                                   A(h) (f ) = −j sgn(f ) A(f ) ,                          (2.61)

utilizzando il teorema di Parseval risulta
                   Z +∞                  Z +∞
          (h)                 (h)
                                                   ¡                 ¢∗
   < a , a >=           a(t) a (t) dt =       A(f ) − j sgn(f ) A(f ) df               .   (2.62)
                      −∞                          −∞
2.6 Modulazioni di ampiezza lineari: schema generale                                    31


                                            (f)




                                         -B 0 B                                        f

                                        p(f)
                        jϕ
                    1 -e 0 (f + f )                           jϕ
                                                           1 e 0 (f - f )
                    2            0                                     0
                                                           2



                    -f0-B -f0 -f0+B               0       f0-B f0 f0+B                 f
                                            (f)
                                        PB



                                                      1



                    -f0-B -f0 -f0+B               0       f0-B f0 f0+B                 f
                                            (f)




                    -f0-B -f0                     0            f0 f0+B                 f
                                            (f)




                                                                                        f
 -2f0-B -2f0                                -B 0 B                              2f0 2f0+B
                                            (f)
                                                  1




                                            -B 0 B                                     f
                                            (f)
                                        o




                                            -B 0 B                                     f



Figura 2.27: Illustrazione dei vari segnali nel dominio della frequenza in una modulazione
SSB+ .
32                                                                  Modulazione di ampiezza


     Allora                                  Z +∞
                                (h)
                      <a, a           >= j          |A(f )|2 sgn(f ) df = 0 ,         (2.63)
                                             −∞

dal momento che |A(f )|2 è una funzione pari mentre sgn(f ) è dispari. Un’altra relazione
semplice da provare è che
                                      Ma(h) = Ma .                                   (2.64)
     Utilizzando la relazione
                                                  1 + sgn(f )
                                        1(f ) =                 ,                     (2.65)
                                                       2
in (2.58), risulta

              ejϕ0              1 + sgn(f − f0 )
S(f ) =             A(f − f0 )
                2                      2
              e−jϕ0              1 + sgn(−f − f0 )
        +             A(f + f0 )
                 2(                      2
                     jϕ0                −jϕ0
              1     e    A(f − f0 ) + e      A(f + f0 )
        =                                                                        (2.66)
              2                      2
                               ¡                 ¢               ¡                ¢ )
              ejϕ0 A(f − f0 ) − j sgn(f − f0 ) − e−jϕ0 A(f + f0 ) − j sgn(f + f0 )
        −                                                                             ,
                                                   2j

in cui abbiamo utilizzato la relazione sgn(−f − f0 ) = −sgn(f + f0 ), essendo sgn una
funzione dispari. Ebbene, è facile constatare che la (2.67), nel dominio del tempo,
corrisponde alla relazione

                          a(t)                      a(h) (t)
                 s(t) =        cos (2πf0 t + ϕ0 ) −          sin (2πf0 t + ϕ0 ) ,     (2.67)
                           2                           2
    Lo schema del modulatore basato sulla precedente equazione è riportato in Figura
2.28.
    Ricordando che in pratica si riescea realizzare un filtro a meno di un ritardo tD ,
di conseguenza in (2.67) avremo a(h) (t − tD ) al posto di a(h) (t). Allora, il segnale s(t)
che viene moltiplicato per la portante, la portante stessa e cosı̀ quella in quadratura
devono essere ritardati di tD .
    È facile verificare che per realizzare un modulatore SSB a banda laterale inferiore,
in cui vengono trasmesse le componenti a frequene negative di a(t), il filtro hP B sarà
del tipo                          
                                   1            , |f |²(f0 − B, f0 )
                      HP B (f ) =    0           , |f |²(f0 , f0 + B) .              (2.68)
                                  
                                     irrilevante , altrove
     Utilizzando il filtro di Hilbert la (2.67) viene sostituita dalla relazione

                          a(t)                      a(h) (t)
                 s(t) =        cos (2πf0 t + ϕ0 ) +          sin (2πf0 t + ϕ0 ) .     (2.69)
                           2                           2
    Nello schema di Figura 2.28 è sufficiente non invertire di segno il segnale che proviene
dal ramo inferiore al sommatore.
2.6 Modulazioni di ampiezza lineari: schema generale                                           33




                                                             1
                                                               cos(2 π f0t + ϕ0 )
                                                             2
    a(t)                                                                            +   s(t)
                                                 - π
                                                   2                                -
                                                       1
                                                         sin(2 π f0t + ϕ0 )
                                                       2
                                         (h)
                            −π       a (t)
                             2
                     Filtro di Hilbert


Figura 2.28: Realizzazione di un modulatore SSB a banda laterale superiore utilizzando il
filtro di Hilbert.

Demodulatore

Con riferimento allo schema di Figura 2.26b, il segnale all’uscita del mixer nel dominio
della frequenza è dato da
                                     ejϕ1              e−jϕ1
                           U(f ) =        S(f − f0 ) +       S(f + f0 ) ,                (2.70)
                                      2                  2
per cui utilizzando la (2.58) risulta
                           ejϕ0 ejϕ1 (+)
             U(f ) =                    A (f − 2f0 )
                            2      2
                           e−jϕ0 ejϕ1 (−)
                       +                 A (f )
                             2       2
                           ejϕ0 e−jϕ1 (+)
                       +                 A (f )
                            2       2
                           e−jϕ0 e−jϕ1 (−)
                       +                  A (f + 2f0 )
                             2        2
                           ej(ϕ0 −ϕ1 ) (+)      e−j(ϕ0 −ϕ1 ) (−)
                       =               A (f ) +             A (f )
                               4                     4
                           ej(ϕ0 +ϕ1 ) (+)             e−j(ϕ0 +ϕ1 ) (−)
                       +               A (f − 2f0 ) +              A (f − 2f0 ) .        (2.71)
                               4                            4
     Mentre il terzo e quarto termine dell’equazione precedente vengono eliminati dal
filtro passa basso h, per ϕ0 = ϕ1 , il primo e secondo termine porgono, rispettivamente,
le componenti a frequenze positive e negative del segnale desiderato.
     Di conseguenza per ϕ0 = ϕ1 risulta
                                                          1
                                               ao (t) =     a(t) .                       (2.72)
                                                          4
34                                                          Modulazione di ampiezza


    In effetti se ϕ1 6= ϕ0 , ao (t) conterrà, oltre ad una componente proporzionale al
segnale desiderato a(t), anche una componente di distorsione. Vediamo di ricavarla
dalla (2.67). Dall’espressione
          u(t) = s(t) cos (2πf0 t + ϕ1 )
                    a(t)
                 =         cos (2πf0 t + ϕ0 ) cos (2πf0 t + ϕ1 )
                      2
                    a(h) (t)
                 −           cos (2πf0 t + ϕ0 ) cos (2πf0 t + ϕ1 )
                        2
                    a(t)                     a(t)
                 =         cos (ϕ0 − ϕ1 ) +       cos (2π2f0 t + ϕ0 + ϕ1 )
                      2                       2
                    a(h) (t)                   a(h) (t)
                 −           sin (ϕ0 − ϕ1 ) −           sin (2π2f0 t + ϕ0 + ϕ1 ) , (2.73)
                        2                         2
risulta che il secondo e quarto termine hanno componenti spettrali attorno a 2f0 , le
quali vengono eliminate dal filtro passa basso, per cui all’uscita avremo
                        a(t)                     a(h) (t)
                 ao (t) =      cos (ϕ0 − ϕ1 ) −            sin (ϕ0 − ϕ1 ) .          (2.74)
                          2                         2
    Ora ricordando la propietà (2.63), il segnale a(h) (t) non ha termini proporzionali ad
                                                            (h)
a(t) essendo ortogonale. Allora in (2.74) il termine a 2 (t) sin (ϕ0 − ϕ1 ) si manifesta
come un termine interferente nei confronti del termine utile a(t) cos (ϕ0 − ϕ1 ). È allora
molto importante che in un sistema SSB il PLL sia sufficientemente accurato in modo
che ϕ1 ' ϕ0 e rendere cosı̀ trascurabile la distorsione.


Vestigial side band (VSB)

Modulatore

In talune applicazioni e tipicamente in presenza di segnali video, il filtro hP B per
modulazioni SSB risulta molto selettivo, nel senso che il rapporto tra la larghezza del-
la banda di transizione e la larghezza della banda passante è molto piccola. In tali
casi soddisfare le caratteristiche di ampiezza del filtro comporta necessariamente una
notevole distorsione di fase. Si preferisce allora rilassare le specifiche del filtro hP B e
“richiedere” una banda maggiore al canale di trasmissione.
    Come vedremo in seguito il filtro hP B deve avere un andamento attorno alla portante
f0 tale che
                HP B (f + f0 ) + HP B (f − f0 ) = K   ,     per |f | ≤ B   ,         (2.75)
con K costante reale.
    Consideriamo il caso di trasmettere tutte le armoniche a frequenze positive di a(t) e
solo parte delle armoniche a frequenze negative: ciò da luogo alla modulazione VSB+ .
    Nelle illustrazioni che seguono assumeremo che il filtro hP B abbia una caratteristica
per frequenze positive del tipo
                    
                     1h
                    
                                 ³        ´i , f0 + ρB < f < f0 + B
                     1
         (+)               1 + sin π2 fρB
                                       −f0
                                              , f0 − ρB < f < f0 + ρB
       HP B (f ) =     2                                                   ,       (2.76)
                    
                      0                      , f   − B < f <  f   − ρB
                    
                    
                                                  0              0
                       irrilevante            , altrove
2.6 Modulazioni di ampiezza lineari: schema generale                                      35

                                                                        (−)
illustrata in Figura 2.29. Naturalmente essendo hP B a valori reali, HP B (f ) si ottiene per
              (−)       ¡ (+)     ¢∗
simmetria,HP B (f ) = HP B (−f ) . È facile verificare che tale caratteristica soddisfa la
(2.75) con K = 1. In (2.76) ρ è un parametro tra 0 e 1 e determina la banda richiesta
pari a B(1 + ρ). Per ρ = 0 otteniamo la modulazione SSB+ .
    Un approccio pratico alla progettazione di hP B è partire da un filtro del tipo banda
passante con banda di transizione che va da (f0 − ρB) a (f0 + ρB), banda passante
con guadagno unitario che si estende alla destra di di (f0 + ρB) e banda attenuata con
valore ideale nullo che si estende alla sinistra di (f0 − ρB). Ora è sufficiente variare
l’ordine del filtro fino a quando l’ampiezza del filtro vale 0.5 per f = f0 . Tipicamente
se il ripple in banda passante e quello in banda attenuata sono scelti uguali, il filtro
avrà un andamento che verifica la (2.75) con K = 1.
    In ogni caso il segnale modulato, nel dominio della frequenza, è dato da
                        · jϕ0                              ¸
                         e                 e−jϕ0
                S(f ) =       A(f − f0 ) +       A(f + f0 ) HP B (f ) .               (2.77)
                           2                 2




Demodulatore

Dalla relazione generale (2.70) e (3.58), risulta

                            ej(ϕ0 −ϕ1 )
                   U(f ) =              A(f ) HP B (f + f0 )
                                4
                            e−j(ϕ0 −ϕ1 )
                          +              A(f ) HP B (f − f0 )
                                 4
                            ej(ϕ0 +ϕ1 )
                          +             A(f − 2f0 ) HP B (f − 2f0 )
                                4
                            e−j(ϕ0 +ϕ1 )
                          +              A(f + 2f0 ) HP B (f + 2f0 ) .                (2.78)
                                 4

   Al solito gli ultimi due termini della precedente relazione vengono ottenuti dal filtro
passa basso h, alla cui uscita per ϕ1 = ϕ0 risulta

                              A(f ) h                                i
                    Ao (f ) =         HP B (f + f0 ) + HP B (f − f0 ) .               (2.79)
                               4

   Di conseguenza, se il filtro di modulazione hP B soddisfa la relazione (2.75) ed ha
un guadagno unitario, avremo che K = 1 e

                                                 a(t)
                                      ao (t) =          .                             (2.80)
                                                  4

     Complessivamente, in una modulazione VSB il filtro hP B essendo meno selettivo
rispetto al caso di modulazione SSB risulta più semplice da realizzare. La conseguenza
è che il sistema richiede una banda più larga.
36                                                            Modulazione di ampiezza


                                               (f)




                                            -B 0 B                                     f

                                           p(f)
                         jϕ
                     1 -e 0 (f + f )
                                                                 jϕ
                                                              1 e 0 (f - f )
                     2            0                                       0
                                                              2



                     -f0-B -f0 -f0+B                 0      f0-B f0 f0+B               f
                                               (f)
                                           PB


                                                     1

                                                     0.5


                   -f0-B    -f0   -f0+B              0     f0-B    f0 f0+B             f
                   - f0 - ρ B - f0 + ρ B       (f)          f0 - ρ B f0+ ρ B




                     -f0-B -f0    -f0+B              0     f0-B    f0 f0+B             f

                   - f0 - ρ B - f0 + ρ B       (f)          f0 - ρ B f0+ ρ B




                                                                                        f
 -2f0-B -2f0                                   -B 0 B                           2f0 2f0+B
                                               (f)
                                                     1




                                               -B 0 B                                  f
                                               (f)
                                           o




                                               -B 0 B                                  f



Figura 2.29: Illustrazione dei vari segnali nel dominio della frequenza in una modulazione
VSB+ .
2.7 Single side band trasmission carrier (SSB-TC)                                      37


2.7      Single side band trasmission carrier (SSB-TC)
È possibile utilizzare la tecnica di inviare la portante anche in una modulazione SSB.
Dalla (2.67) per una SSB+ -TC il segnale trasmesso è dato da

                         a(t)                      a(h) (t)
               s(t) =         cos (2πf0 t + ϕ0 ) −          sin (2πf0 t + ϕ0 )
                          2                           2
                       + A cos (2πf0 t + ϕ0 ) .                                    (2.81)

   Anche in questo caso possiamo introdurre l’efficienza della modulazione che in
analogia alla (2.15) è ora data da (vedi anche relazione (2.64))
                                     ³       M
                                                      ´
                                         Ma               1
                                          4
                                            + a4(h)       2
                                                                Ma
                                η=                            = 4    ,             (2.82)
                                              Ms                Ms
                  2
dove Ms = M4a + A2 .



2.8      Quadrature amplitude modulation (QAM)
Modulatore

Come illustrato in Figura 2.30 questo sistema è analogo alla modulazione di ampiezza
in quadratura per segnali dati. Siano a1 (t) e a2 (t) due segnali di informazione a valori
reali aventi una banda B. Moduliamo ora a1 (t) per la portante cos (2πf0 t + ϕ0 ) mentre
a2 (t) per la portante in quadratura sin (2πf0 t + ϕ0 ), e formiamo il segnale modulato

               s(t) = a1 (t) cos (2πf0 t + ϕ0 ) − a2 (t) sin (2πf0 t + ϕ0 ) .      (2.83)

Un modo alternativo per ricavare s(t) è introducendo il segnale complesso

                                  a(t) = a1 (t) + j a2 (t) .                       (2.84)

    Modulando a(t) per la portante complessa ej(2πf0 t+ϕ0 ) = cos (2πf0 t+ϕ0 )+j sin (2πf0 t+
ϕ0 ) e trasmettendo la sola parte reale si ottiene s(t). Analiticamente
                                        £                   ¤
                               s(t) = Re a(t) ej(2πf0 t+ϕ0 ) .                     (2.85)

    Notiamo che la banda di s(t) è pari a 2B, però il segnale porta due segnali di banda
B per cui risulta la stessa efficienza spettrale della SSB. La illustrazione dello spettro
dei vari segnali è riportata in Figura 2.31.


Demodulatore

Sia la fase della portante ricostruita uguale a quella ricevuta, cioè ϕ1 = ϕ0 . Formi-
amo due segnali u1 (t) e u2 (t) moltiplicando s(t) rispettivamente per cos (2πf0 t + ϕ0 )
38                                                                                 Modulazione di ampiezza


e sin (2πf0 t + ϕ0 ). Sia u1 (t) che u2 (t) vengono filtrati da un filtro passa basso h(t) di
banda B. L’espressione di u1 (t) sarà data da

          u1 (t) = s(t) cos (2πf0 t + ϕ0 )
                 = a1 (t) cos (2πf0 t + ϕ0 ) cos (2πf0 t + ϕ0 )
                 − a2 (t) sin (2πf0 t + ϕ0 ) cos (2πf0 t + ϕ0 )
                   a1 (t) a1 (t)                          a2 (t)
                 =        +       cos (2π2f0 t + 2ϕ0 ) −         sin (2π2f0 t + 2ϕ0 ) .(2.86)
                     2         2                            2


                                                                                              u (t)           LPF   a (t)
     a1(t)                                                                                     1                    o,1
                                                                                                               h


                        cos(2 π f0t + ϕ0 )                                                    cos(2 π f0t + ϕ0 )

                                             +       s(t)           s(t)
             - π                                                                   - π
               2                             -                                       2

                                                                                         sin(2 π f0t + ϕ0 )
                   sin(2 π f0t + ϕ0 )
                                                                                                              LPF
     a (t)                                                                                   u (t)                  a     (t)
      2                                                                                       2                     o,2
                                                                                                               h



                        a)                                                                           b)



              Figura 2.30: Schema base di un QAM: a)modulatore, b)demodulatore.

   Ora sia il secondo che il terzo termine vengono attenuati dal filtro h alla cui uscita
rimane
                                               a1 (t)
                                    ao,1 (t) =        .                            (2.87)
                                                 2
In modo analogo, il segnale all’uscita del secondo ramo è dato da

                                                                a2 (t)
                                                   ao,2 (t) =              .                                            (2.88)
                                                                  2
Un metodo alternativo per ricavare ao,1 (t) e ao,2 (t) è utilizzando la notazione complessa.
Sia
                    u(t) = s(t) e−j(2πf0 t+ϕ0 ) = u1 (t) + j u2 (t) ,                  (2.89)
che in frequenza porge
                                             U(f ) = S(f − f0 ) e−jϕ0          ,                                        (2.90)
                                ¡        ¢
e definendo ao (t) = u ∗ h (t), è facile verificare che risulta
                                                 £    ¤
                                  ao,1 (t) = Re ao (t) ,                                                                (2.91)

e                                                             £      ¤
                                                 ao,2 (t) = Im ao (t) .                                                 (2.92)
2.8 Quadrature amplitude modulation (QAM)                                               39



                                                     (f)
                                                 1




                                           -B              0   B                        f
                                                     (f)
                                                 2




                                           -B              0   B                        f
                               (f) =   (f) + j       (f)
                                       1         2




                                                           0   B                        f
                                                     (f)




                -f0-B    -f0       -f0+B                   0       f0-B   f0   f0+B     f
                                                     (f)




                                                                                        f
       -2f0                                -B              0   B
                                                     (f)
                                                           1




                                           -B              0   B                        f
                                                     (f)
                                                 o




                                           -B              0   B                        f



  Figura 2.31: Illustrazione dei vari segnali nel dominio della frequenza in una QAM.
40                                                                       Modulazione di ampiezza


   Notiamo che in questo schema i due segnali a1 (t) e a2 (t) vengono sovrapposti sia nel
tempo che in frequenza. In effetti essi sono ancora separabili poichè la moltiplicazione
per le funzioni cos (2πf0 t + ϕ0 ) e sin (2πf0 t + ϕ0 ) li rende ortogonali3 , sotto l’ipotesi
f0 > B. Il prezzo di questa ortogonalità è aver raddoppiato la banda richiesta da B a
2B.


2.9            Accesso multiplo a divisione di frequenza (FDM)
Riportiamo in Figura 2.32 il caso di N segnali modulati DSB-SC le cui portanti sono
separate di 2B Hz. Notiamo che questa è la minima separazione in frequenza, altrimenti
c’è interferenza tra due segnali. In pratica, per semplificare la realizzazione del filtro
h al ricevitore è opportuno che venga introdotta una banda di guardia tra i segnali.
Ciò si ottiene imponendo che la separazione tra le portanti sia maggiore di 2B. In
conclusione, tramite un certo spreco di banda si può ottenere un filtro h con una
banda di transizione non nulla e di conseguenza realizzabile.

  a1 (t)               s1 (t)                                                            f1   ~
               MOD                                                                            a     (t)
                                                                                              o,1
                f1                                                                     DEM
  a (t)                s (t)
     2         MOD      2                                                                f2
                f2                                                                            ~
                                                                                              a     (t)
                                           s(t)                 r(t)          r(t)            o,2
                   .                              Canale                               DEM
                   .

                                                                                       ...
                   .
                                                                                         fN
  a (t)                s (t)                                                                  ~
     N         MOD      N                                                                     a     (t)
                                                                                              o,N
                fN                                                                     DEM


                                a)                                                      b)




             (f)




                                                                   ...

                                     f1            f2                    fN
                                            2B
                                                           c)



Figura 2.32: Schema base del principio FDM per N segnali: a) modulatore, b) demodulatore
e c) illustrazione dello spettro occupato.

     3
         In effetti la TDM e FDM sono casi particolari di ortogonalità tra segnali.
2.10 Prestazioni                                                                           41


2.10       Prestazioni
Valutiamo ora le prestazioni dei vari schemi di modulazione di ampiezza per un canale
rumoroso però non distorcente in cui il segnale all’ingresso del ricevitore è dato dalla
(1.1).
    Introduciamo innanzitutto il il rapporto segnale-rumore di riferimento Γ all’uscita
del canale. Sia Ms la potenza del segnale trasmesso e B la banda del segnale modulante
a(t). Definiamo Γ come rapporto tra la potenza del segnale desiderato all’uscita del
canale e la potenza del rumore valutata su una banda convenzionale pari a B:

                                 Ms |GCh,0 |2      Ms
                              Γ = N0          =               ,                        (2.93)
                                    2
                                      2B        N0 B a d

dove ad è l’attenuazione di potenza introdotta dal canale (vedi (1.2)). Per un dato seg-
nale a(t) con banda B e prefissato canale con attenuazione ad , Γ dipende dal rapportov
tra la potenza del segnale trasmesso e la densità spettrale del rumore. Sottolineamo che
la banda di s(t) non coincide necessariamente con B, vedi ad esempio le modulazioni
DSB e VSB.
    D’ora in poi, per semplificare la notazione porremo C = GCh,0 .
    Analizzeremo distintamente i casi di ricevitore coerente e non coerente. In generale
indicheremo con ro (t) il segnale all’uscita del ricevitore. In assenza di distorsione, ro (t)
sarà composto da una componente utile ao (t) proporzionale al segnale di informazione
a(t), ao (t) = c a(t), e una componente addittiva rumorosa wo (t). In definitiva possiamo
scrivere
                          ro (t) = ao (t) + wo (t) = c a(t) + wo (t) .                (2.94)
   Le prestazioni del sistema vengono misurate dal rapporto tra la potenza del termine
desiderato c2 Ma e la potenza del rumore in uscita Mwo ,

                                              c 2 Ma
                                       Λo =            .                               (2.95)
                                              Mwo

Il nostro obiettivo sarà esprimere Λo in funzione di Γ per le diverse modulazioni.


Demodulatori coerenti

DSB-SC

Dalle (2.1) e (1.1), il segnale all’ingresso del ricevitore è dato da

                         r(t) = C a(t) cos (2πf0 t + ϕ0 ) + w(t) .                     (2.96)

    Dallo schema di Figura 2.25 all’uscita del filtro hRc , del tipo banda passante attorno
f0 e banda 2B,
                     rRc (t) = C a(t) cos (2πf0 t + ϕ0 ) + wRc (t) ,                 (2.97)
in cui, utilizzando la notazione [1]

        wRc (t) = wRc,I (t) cos (2πf0 t + ϕ1 ) − wRc,Q (t) sin (2πf0 t + ϕ1 ) ,        (2.98)
42                                                                        Modulazione di ampiezza


dove wRc,I (t) e wRc,Q (t) sono rumori incorrelati, del tipo banda base di banda B,
ciascuno con uno spettro
                                                                  µ ¶
                                                       2            f
              PwRc,I (f ) = PwRc,Q (f ) = N0 |HRc (f )| = N0 rect      .      (2.99)
                                                                   2B
     Di conseguenza le potenze di wRc,I e wRc,Q sono uguali e pari a

                               MwRc,I = MwRc,Q = N0 2B                .                    (2.100)

All’ingresso del filtro h il rumore è dato da
                                         ·
                                       1
      wRc (t) cos (2πf0 t + ϕ1 ) =         wRc,I (t) + wRc,I (t) cos (2π2f0 t + ϕ0 + ϕ1 )
                                       2
                                                                         ¸
                                 − wRc,Q (t) sin (2π2f0 t + ϕ0 + ϕ1 )         ,       (2.101)

di cui solo il primo termine passa attraverso il filtro e di conseguenza
                                              1
                                   wo (t) =     wRc,I (t) .                                (2.102)
                                              2
In base alla (2.100) la potenza di wo è pari a
                                        1         N0 B
                               Mw o =     N0 2B =                     .                    (2.103)
                                        4          2
    Utilizzando infine l’espressione (2.5) del segnale utile all’uscita, la quale a causa
dell’attenuazione C del canale porge in (2.94)
                                        C
                                 c=       cos (ϕ0 − ϕ1 ) .                                 (2.104)
                                        2
In definitiva per ϕ0 = ϕ1 il rapporto (2.95) è dato da
                                         C2
                                         4
                                             Ma   C 2 Ma
                                 Λo =    N0 B
                                                =             .                            (2.105)
                                            2
                                                  N0 2B

   Con riferimento al rapporto di riferimento Γ, dato dalla (2.93), poichè dalla (2.1)
Ms = M2a , avremo che
                                      Λo = Γ .                                  (2.106)
    È utile introdurre anche il rapporto segnale-rumore Λi all’uscita del filtro hRc dove
la potenza del rumore viene misurata con riferimento alla banda Bs del segnale s(t)

                                      C 2 Ms   C 2 Ms
                                Λi = N0      =                    .                        (2.107)
                                     2
                                         2Bs   N0 B s

Poichè Bs = 2B risulta
                                        Λo = 2 Λi    .                                     (2.108)
   Osserviamo che il processo di demodulazione ha raddoppiato il rapporto segnale-
rumore. Infatti le componenti del segnale desiderato a frequenza positiva e negativa
vengono a sommarsi coerentemente per dar luogo ad un raddoppio del segnale e quindi
2.10 Prestazioni                                                                        43


quadruplicando la potenza del segnale. Invece le componenti del rumore a frequenza
positiva sono incorrelate con quelle a frequenza negativa per cui sommandosi la poten-
za aumenta solo di un fattore 2: complessivamente c’è un guadagno di un fattore 2 nel
rapporto segnale-rumore.


SSB

Analizziamo il caso SSB+ . L’analisi è simile per una modulazione SSB− .

   Dalla (1.1) e (2.67) risulta
              ·                                                   ¸
           C                               (h)
    r(t) =      a(t) cos (2πf0 t + ϕ0 ) − a (t) sin (2πf0 t + ϕ0 ) + w(t) .        (2.109)
            2
Il filtro hRc , in base alla (2.56), avrà l’andamento ideale
                            Ã     ¡         ¢!        Ã       ¡      ¢!
                              f − f0 + B2               −f − f0 + B2
           HRc (f ) = rect                     + rect                      .       (2.110)
                                    B                         B

All’uscita di hRc , il segnale sarà dato da
               ·                                                   ¸
             C                               (h)
   rRc (t) =     a(t) cos (2πf0 t + ϕ0 ) − a (t) sin (2πf0 t + ϕ0 ) + wRc (t) .    (2.111)
             2
in cui wRc (t) ha uno spettro
                                              N0
                                PwRc (f ) =      |HRc (f )|2           ,           (2.112)
                                              2
e potenza
                                   N0 2B
                                MwRc =    = N0 B                   .               (2.113)
                                     2
Procedendo in modo analogo al caso DSB risulta
                                         1        N0 B
                                 Mwo =     MwRc =                  ,               (2.114)
                                         4         4
mentre dalla (2.72), per un canale con ampiezza C,

                                               C2
                                      Ma o =      Ma   .                           (2.115)
                                               16
In conclusione
                                         C2      C2
                                         16 a
                                             M   4
                                                    Ma
                                  Λo =   N0 B
                                               =               .                   (2.116)
                                            4
                                                 N0 B
    Utilizzando la relazione (2.67) e il fatto che a(t) e a(h) (t) sono segnali ortogonali,
abbiamo che
                                    1       1         Ma
                              Ms = Ma + Ma(h) =            ,                        (2.117)
                                    8       8          4
utilizzando la (2.64). Allora
                                        Λo = Γ .                                    (2.118)
44                                                         Modulazione di ampiezza


Inoltre poichè Bs = B, è facile verificare che

                                        Λo = Λi    .                              (2.119)

    Il risultato importante è che le modulazioni DSB-SC e SSB hanno le stesse prestazioni
in termini di rapporto segnale-rumore all’uscita del ricevitore, con Λo = Γ. La SSB
però richiede metà banda, a costo di una maggiore complessità realizzativa.


DSB-TC e SSB-TC

È facile verificare che per entrambi i sistemi DSB e SSB, quando oltre al segnale
di informazione viene trasmessa anche la portante, nel caso di demodulazione coeren-
te l’analisi del sistema segue le stesse linee esposte sopra. In particolare il rapporto
segnale-rumore all’uscita del ricevitore è dato dalle (2.106) e (2.118), rispettivamente
per DSB e SSB. Considerando ora che solo una frazione η (definita dalla (2.15)) della
potenza di s(t) è utilizzata per la trasmissione del segnale di informazione, in entrambi
i sistemi di modulazione avremo che

                                        Λo = Γ η   ,                              (2.120)

con ovviamente una perdita di prestazioni, a parità di potenza trasmessa, rispetto al
caso SC.


Demodulatori non coerenti

DSB-TC (AM)

Consideriamo la condizione per l’assenza di distorsione dell’inviluppo, A > am . Al-
l’uscita del filtro hRc , di tipo banda passante di banda 2B, avremo il segnale
                               ¡          ¢
            rRc (t) = C A 1 + m ā(t) cos (2πf0 t + ϕ0 )
                     + wRc,I (t) cos (2πf0 t + ϕ0 ) − wRc,Q (t) sin (2πf0 t + ϕ0 )
                          h      ¡          ¢          i
                     = C A 1 + m ā(t) + wRc,I (t) cos (2πf0 t + ϕ0 )
                   − wRc,Q (t) sin (2πf0 t + ϕ0 ) ,                               (2.121)

in cui wRc,I (t) e wRc,Q (t) definiti in 2.98.
    Introdotte le funzioni modulo e deviazione di fase di rRc (t),
                          ·³                            ´2          ¸ 21
                                 ¡         ¢                  2
               MrRc (t) =   C A 1 + m ā(t) + wRc,I (t) + wRc,Q (t)               (2.122)
                                  Ã                             !
                                             w Rc,Q (t)
              ∆ϕrRc (t) = − tan−1      ¡             ¢            ,               (2.123)
                                    C A 1 + m ā(t) + wRc,I (t)

possiamo scrivere rRc (t) nel seguente modo
                                         ¡                      ¢
                  rRc (t) = MrRc (t) cos 2πf0 t + ϕ0 + ∆ϕrRc (t) .                (2.124)
2.10 Prestazioni                                                                            45


    L’uscita di un demodulatore di inviluppo con ingresso rRc (t) porgerà propio MrRc (t),
utilizzando uno degli schemi illustrati in Sezione 2.4.

   Ora, per separare in (2.122) la parte desiderata da quella rumorosa bisogna intro-
durre qualche approssimazione. Posto
                                          ¡          ¢
                            sRc (t) = C A 1 + m ā(t) ,                      (2.125)
assumeremo che
                              wRc,Q (t) ¿ sRc (t) + wRc,I (t) .                        (2.126)
     Tale condizione è verificata con elevata probabilità se il rapporto segnale-rumore Γ
all’uscita del canale è sufficientemente elevato cioè se il segnale sR (t) = C s(t) = sRc (t)
all’ingresso del ricevitore ha una potenza sufficientemente più elevata della potenza del
rumore wRc (t) all’uscita di hRc . In base alla (2.126), la (2.122) diviene
                                    ¯     ¡          ¢             ¯
                                    ¯                              ¯
                         MrRc (t) = ¯C A 1 + m ā(t) + wRc,I (t)¯ ,                    (2.127)

che, sempre in base alla (2.126), può essere scritta come
                                       ¡            ¢
                       MrRc (t) = C A 1 + m ā(t) + wRc,I (t) .                        (2.128)
   Filtrando la componente DC della (2.128), rimane il segnale
                              ao (t) = C A m ā(t) + wRc,I (t)
                                     = C a(t) + wRc,I (t) ,                            (2.129)
dove abbiamo utilizzato le (2.10) e (2.11). Allora il rapporto segnale-rumore all’uscita
del ricevitore è dato da
                                             C Ma
                                      Λo =         .                            (2.130)
                                            N0 2B
    Utilizzando le (2.15) e (2.93), risulta
                                               m2 kf2
                                Λo = Γ η = Γ                 ,                         (2.131)
                                             1 + m2 kf2
dove nell’ultimo passaggio abbiamo utilizzato la (2.19). Ricordando che per l’assenza
di distorsione dell’inviluppo deve essere m < 1, allora risulta Λo < Γ2 ; in altre parole, a
parità di Γ, un demodulatore (non coerente) per DDS-TC ha almeno 3 dB di perdita
in Λo rispetto ad un demodulatore (coerente) per DSB-SC.
    Concludiamo ricordando che con rapporti Γ non sufficientemente elevati, la (2.131)
non vale più e Λo dipende da Γ con legge quadratica [3].


SSB-TC

In linea di principio si potrebbe utilizzare un demodulatore non coerente anche per una
modulazione SSB. In assenza del rumore, il segnale ricevuto è dato dalla (2.67) molti-
plicato per C, dovuto al canale, più il segnale dovuto alla portante C A cos (2πf0 t +
ϕ0 ):
          ·µ            ¶                                                 ¸
               a(t)                            a(h) (t)
        C           + A cos (2πf0 t + ϕ0 ) −            sin (2πf0 t + ϕ0 )  .   (2.132)
                2                                 2
46                                                             Modulazione di ampiezza


     L’inviluppo della (2.132) è dato da
                              ·µ             ¶2     µ (h) ¶2 ¸ 21
                                   a(t)              a (t)
                          C             +A        +                 .           (2.133)
                                    2                   2

    Notiamo che solo se A è molto elevato, allora il primo termine della somma nella
(2.133) prevale e l’inviluppo risulta proporzionale ad a(t). Sfortunatamente ciò com-
porta un sistema con una efficienza η molto bassa, per cui un tale sistema è raramente
utilizzato.
Capitolo 3

Modulazione angolare

3.1      Definizioni e parametri associati
L’espressione generale della portante modulata è data da (vedi 1.4)

                            s(t) = A cos(2πf0 t + ϕ0 + λ(t)) ,                        (3.1)

dove λ(t) = ∆ϕs (t) è la deviazione di fase istantanea [1]. Ricordiamo inoltre la relazione
tra deviazione di fase istantanea ∆ϕs (t) e deviazione di frequenza istantanea ∆fs (t),
                                               1 d
                                  ∆fs (t) =         λ(t) ,                            (3.2)
                                              2π dt
oppure, inversamente                       Z t
                               λ(t) = 2π           ∆fs (τ ) dτ .                      (3.3)
                                            −∞

    Ebbene, se il segnale modulante a(t) varia ∆fs (t) abbiamo la modulazione di fre-
quenza (frequency modulation, FM) mentre se a(t) varia λ(t) abbiamo la modulazione
di fase (phase modulation, PM). Entrambe le modulazioni vanno sotto il nome di mo-
dulazione angolare (angle modulation): analizziamole separatamente.

MODULAZIONE DI FREQUENZA

Sia KF una costante di proporzionalità. Nella FM risulta

                                   ∆fs (t) = KF a(t) .                                (3.4)

   Corrispondentemente la frequenza istantanea complessiva di s(t) è pari a

                                  fs (t) = f0 + KF a(t) ,                             (3.5)

mentre dalla (3.3) la deviazione di fase è data da
                                             Z t
                              λ(t) = 2πKF         a(τ ) dτ .                          (3.6)
                                                 −∞

Il segnale modulato ha la seguente espressione
                                                           Z t
                    s(t) = A cos(2πf0 t + ϕ0 + 2πKF                a(τ ) dτ ) .       (3.7)
                                                            −∞


                                              47
48                                                                                         Modulazione angolare


             E’ facile verificare che se f0 À B la potenza media di s(t) è
                                                           A2
                                                  Ms =                                                     (3.8)
                                                           2
indipendente da a(t).
D’altra parte dalla (3.6) la frequenza istantanea di s(t) varia da un valore minimo
                                              f0 + KF min a(t)                                             (3.9)
                                                           t

ad un valore massimo
                                             f0 + KF max a(t) .                                           (3.10)
                                                       t




                  1                                                                1
        a(t)




                                                                      a(t)
                  0                                                                0


                 −1                                                           −1

                       0   2    4        6        8                                    0   2    4     6      8
                                 t                −3
                                               x 10                                              t        x 10
                                                                                                              −3



                                                                                   5
λ(t), βF = 0.2




                 0.2
                                                                    λ(t), βF = 5




                  0                                                                0

           −0.2                                                               −5

                       0   2    4        6        8                                    0   2    4     6      8
                                 t                −3
                                               x 10                                              t        x 10
                                                                                                              −3

                  1                                                                1
s(t), βF = 0.2




                                                               s(t), βF = 5




                 0.5                                                          0.5

                  0                                                                0

           −0.5                                                          −0.5

                 −1                                                           −1
                       0   2    4        6        8                                    0   2    4     6      8
                                 t                −3
                                               x 10                                              t        x 10
                                                                                                              −3




Figura 3.1: Esempio di segnale di informazione a(t), corrispondente fase istantanea λ(t) e
segnale FM per f0 = 3500Hz, e due valori di KF = βaFMB : a) βF = 0.2 e b) βF = 5.

    Questi valori due valori non devono però esssere confusi con la banda passante di
s(t). Infatti, mentre la trasformata di Fourier di s(t) è un integrale nel tempo, la
frequenza istantanea non prende in considerazione la durata di ciascuna frequenza di
s(t).
    Considerando come segnale modulante il segnale (2.3) costituito dalla somma di
tre sinusoidi, riportiamo in Figura 3.1 l’andamento del segnale FM s(t) e della fase
istantanea λ(t) per f0 = 3500 Hz e due valori di KF .
3.1 Definizioni e parametri associati                                                          49


                0.9

                0.5

                0.1
        a(t)
               −0.3

               −0.7

               −1.1
                      0   1      2       3           4       5    6       7        8
                                                         t                        x 10
                                                                                       −3




                 1


                0.5
        s(t)




                 0


               −0.5


                −1
                      0   1      2       3           4       5    6       7        8
                                                         t                        x 10
                                                                                       −3




     Figura 3.2: Segnale FM per un segnale modulante a(t) del tipo costante a tratti.

     Un secondo esempio illustrativo di segnale FM è riportato in Figura 3.2 in cui a(t)
è costante a tratti.
     In effetti, nella FM l’informazione del segnale modulante è nella frequenza istan-
tanea del segnale modulato. In termini approssimati posssiamo dire che il numero di
attraversamenti per lo zero di s(t) nell’unità di tempo (cioè la densità degli zeri di s(t))
è proporzionale a a(t).

MODULAZIONE DI FASE (PM)

Sia KP una costante di proporzionalità. In questo caso la deviazione di fase è pro-
porzionale al segnale mudulante,

                                        λ(t) = KP a(t) .                                    (3.11)

Corrispondente
                              s(t) = A cos(2πf0 t + ϕ0 + KP a(t)) .                         (3.12)
CORRISPONDENZA TRA SEGNALI FM E PM

Per un segnale di informazione b(t), confrontando (3.7) e (3.12) abbiamo che un segnale
FM può essere interpretato come PM in cui
                                               Z t
                                      a(t) =         b(τ ) dτ .                             (3.13)
                                                −∞
50                                                                 Modulazione angolare


Viceversa un segnale PM può essere interpretato come FM in cui
                                                d
                                       a(t) =      b(t) .                         (3.14)
                                                dt
   Allora, come illustrato in Figura 3.3, a partire da uno schema di modulazione,
PM o FM, è possibile ottenere l’altro schema elaborando opportunamente il segnale di
ingresso.

                        Integratore
                b(t)                            a(t)                     s(t)
                                                            Modulatore
                                                             di fase            FM

         Segnale di
      informazione
                         Derivatore
                b(t)                            a(t)                     s(t)
                             d                              Modulatore
                                 dt                          di freq.           PM



        Figura 3.3: Generazione di un segnale FM utilizzando un PM e viceversa.

   In ogni caso la modulazione di argomento non è lineare rispetto al segnale modu-
lante.

INDICE DI MODULAZIONE

Per un segnale modulante a(t) di banda B sia

                                      aM = max |a(t)| .                           (3.15)
                                                t

Anche in questo caso, se a(t) ha ampiezza non limitata aM viene definita tramite la
probabilità
                                P [|a(t)| < aM ] = ε ,                       (3.16)
con ε sufficientemente piccolo.
   Per semplificare la notazione, supponiamo che am = aM , dove am è definito in (2.7).
Inoltre richiamiamo la definizione di fattore di forma kf2 dato della (2.14).
   Definiamo l’indice di modulazione β per una modulazione angolare:
                                                                 √
                                                                   Ma
                  P M : βP = max |∆ϕs (t)| = KP aM = KP
                                    t                             kf
                                                                                 (3.17)
                                                                  √
                                   maxt |∆fs (t)|   KF aM      KF Ma
                  F M : βF =                      =         =
                                         B            B         B kf

    In altre parole, mentre nella PM β è dato dal valore massimo della deviazione di
fase, nella FM β è dato dal valore massimo della deviazione di frequenza, diviso la
banda di a(t).
3.2 Narrowband FM                                                                      51


3.2      Narrowband FM
Per semplicità di scrittura poniamo
                                           Z t
                                  d(t) =         a(t) dτ ,                         (3.18)
                                            −∞

la quale, nel dominio della frequenza, porge
                                                 A(f )
                                    D(f ) =            .                           (3.19)
                                                 j2πf
   Il segnale modulato (3.7) può essere scritto nel seguente modo,


                     s(t) = A cos(2πf0 t + ϕ0 + 2πKF d(t))
                          = A cos(2πf0 t + ϕ0 ) cos(2πKF d(t))
                          − A sin(2πf0 t + ϕ0 ) sin(2πKF d(t)) .                   (3.20)

   E’ interessante esaminare l’espressione di s(t) nel caso in cui KF sia sufficientemente
piccolo in modo che l’angolo 2πKF d(t) sia sempre molto piccolo. In tal caso possi-
amo utilizzare le approssimazioni cos(2πKF d(t)) ' 1 e sin(2πKF d(t)) ' 2πKF d(t).
Corrispondentemente abbiamo

               s(t) = A cos(2πf0 t + ϕ0 ) − A2πKF d(t) sin(2πf0 t + ϕ0 ) .         (3.21)

    A parte il primo termine, la portante, ora il legame tra d(t) e s(t) è lineare. Alla
(3.21) corrisponde nel dominio della frequenza il segnale

                        A jϕ0
               S(f ) =    [e δ(f − f0 ) + e−jϕ0 δ(f + f0 )]
                        2      ·                                    ¸
                        A2πKF jϕ0 A(f − f0 )        −jϕ0 A(f + f0 )
                      +          e               −e                   .            (3.22)
                           4π          f − f0               f + f0
    Per un segnale a(t) a banda limitata B, il corrispondente segnale modulato ha uno
spettro attorno f0 di forma proporzionale ad A(f )/f , come illustrato in Figura 3.4.
    In tal caso, il segnale s(t), denominato FM a banda stretta, ha una banda pari a
2B, come nel caso DSB.
    Possiamo inoltre affermare che nel caso KF sia sufficientemente piccolo la modula-
zione FM è in grado di soddisfare gli obiettivi di un sistema di modulazione e cioè di
fornire un segnale modulato a frequenze opportunamnte elevate e di banda finita, in
modo che più segnali possano condividere lo spettro. Il terzo obiettivo su come ricavare
a(t) dato s(t) sarà esaminato in seguito.
    Considerazioni analoghe valgono per un segnale PM in cui invece di d(t) abbiamo
direttamente a(t).
    Analizziamo ora la forma del segnale modulato s(t) per il segnale a(t) di tipo
sinusoidale di frequenza B,
                                    a(t) = cos(2πBt) .                             (3.23)
Corrispondente
                                           sin(2πBt)
                                  d(t) =                   ,                       (3.24)
                                              2πB
52                                                                               Modulazione angolare


                                                         (f)




                                                               0   B                             f


                                                         (f)




               - f0 -B   - f0   - f0 +B                        0         f0 -B     f0    f0 +B   f



     Figura 3.4: Segnale FM nel dominio della frequenza per KF sufficientemente piccolo.

e sempre sotto l’ipotesi che 2πKF d(t) ¿ 1, ciò per KBF ¿ 1, dalla (3.21) risulta
                 ·                                                    ¸
                                      2πKF
         s(t) = A cos(2πf0 t + ϕ0 ) −      sin(2πBt) sin(2πf0 t + ϕ0 )                       .       (3.25)
                                       2B

     Utilizzando le relazioni trigonometriche
                                                     £               ¤
                                     cos(2πf0 t) = Re ej(2πf0 t+ϕ0 )                                 (3.26)
                                                   £                 ¤
                                   sin(2πf0 t) = Re −jej(2πf0 t+ϕ0 )                                 (3.27)

                                                          ej2πBt − e−j2πBt
                                    sin(2πBt) =                            ,                         (3.28)
                                                                 2j
abbiamo che
                                ½                    ·                                  ¸¾
                                     j(2πf0 t+ϕ0 )          KF j2πBt KF −j2πBt
                s(t) = A Re e                            1−    e    +    e                   .       (3.29)
                                                            2B        2B

   A parte il termine di fase che cresce linearmente nel tempo (in particolare compie
un angolo giro ogni 1/f0 secondi), dovuto alla frequenza della portante, il termine
                           ·                           ¸
                                KF j2πBt KF −j2πBt
                             1−     e      +     e         ,                     (3.30)
                                2B           2B

comporta una fase aggiuntiva che dipende dal segnale di informazione e si compone
come illustrato in Figura 3.5. Ricordiamo che in assenza di approssimazioni il modulo
di questo fasore dovrebbe essere unitario.
3.3 Wideband FM                                                                             53


        Im




                                                          1      2πBt


                                      K F j2πBt                              Re
                                  −      e
                                      2B                                   K F -j2πBt
                                                                              e
                                                                           2B




                      K F e j2πBt   K F -j2πBt
                 1−               +    e
                      2B            2B


Figura 3.5: Composizione del termine di fase in un segnale FM per un segnale modulante
sinusoidale di frequenza B.


3.3      Wideband FM
Nel caso generale in cui KF non sia sufficientemente piccolo, si parla di FM a banda
larga. In tal caso l’approssimazione (3.21) non è verificata e bisognerà riferirsi al segnale
modulato
                          s(t) = A cos(2πf0 t + ϕ0 + 2πKF d(t)) ,                        (3.31)
dove d(t) è definito in (3.18).
   Dal momento che il legame tra a(t) e s(t) è non lineare in generale non è possibile
esprimere in forma analitica la trasformata di Fourier di s(t) in funzione della trasfor-
mata di Fourier di a(t). Comunque, nelle PM e FM è consuetudine utilizzare come
banda di s(t) la formula di Carson,

                                       Bs = 2B(1 + β) ,                                 (3.32)

dove B è la banda del segnale modulante e β è l’indice di modulazione definito in
(3.17). In realtà la (3.32) dà solamente una indicazione della banda effettiva di s(t) ed
è opportuno ricorrere a simulazioni per una più precisa valutazione dello spettro del
segnale modulato.
    E’ interessante comunque ripercorrere l’analisi di Carson per la determinazione della
(3.32). Innanzitutto l’analisi è stata fatta per un segnale modulante di tipo sinusoidale
a frequenza B,
                                    a(t) = aM cos(2πBt) ,                            (3.33)
per il quale nella FM
                                 2πKF d(t) = βF sin(2πBt) .                             (3.34)
Nella PM invece
                                  KP a(t) = βP cos(2πBt) .                              (3.35)
54                                                                      Modulazione angolare


   In entrambi i casi (a parte la sostituzione della funzione sin(2πBt) con cos(2πBt)
passando da FM a PM),


                        s(t) = A cos(2πf0 t + ϕ0 + β sin(2πBt))
                                    £                           ¤
                             = A Re ej(2πf0 t+ϕ0 ) ejβ sin(2πBt) .                     (3.36)

   Utilizzando lo sviluppo in serie di Fourier della funzione ejβ sin(2πBt) , periodica di
periodo 1/B, risulta
                                          +∞
                                          X
                           jβ sin(2πBt)
                          e             =    Jk (β)ejk2πBt ,                        (3.37)
                                                k=−∞

dove                                       Z 2π
                                      1
                            Jk (β) =              ej(β sin u−ku) du ,                  (3.38)
                                     2π      0

è la funzione di Bessel di prima specie di ordine k [3] Otteniamo cosı̀

                                 +∞
                                 X
                      s(t) = A          Jk (β) cos(2π(f0 + kB)t + ϕ0 ) .               (3.39)
                                 k=−∞


    In altre parole, la trasformata di Fourier di un segnale FM modulato da un segnale
sinusoidale di frequenza B è composta da una sequenza infinita di righe attorno alla
portante, di ampiezze {Jk (β)}. In pratica, addottando il criterio di considerare solo i
termini entro gli indici [−kmax , kmax ] per i quali si ottiene una potenza superiore al 90%
di quella del segnale complessivo, il numero di termini significativi in (3.39) dipende
da β però è finito ed è nell’ordine di 2kmax ' 2β + 3. Poichè due righe spettrali distano
di B Hz, si ottiene il risultato (3.32).
    Benchè la formula di Carson sia stata derivata per segnali modulanti sinusoidali,
sperimentalmente essa si è rivelata valida anche per segnali non sinusoidali di banda
B. Per una spiegazione intuitiva di questo fatto rimandiamo a [3].
Vediamo alcune osservazioni:

     1. Notiamo che in base alla (3.32) utilizzare un elevato valore di β comporta una
        banda elevata del sistema. D’altra parte, come vedremo in seguito, un elevato β
        migliora le prestazioni del ricevitore.

     2. Definita la massima deviazione di frequenza del segnale modulato

                                  ∆F = max |∆fs (t)| = KF aM ,                         (3.40)
                                            t


       per un segnale FM la banda richiesta si può scrivere nel seguente modo

                                         Bs = 2(B + ∆F ) .                             (3.41)

     3. Per β ¿ 1, oppure in modo equivalente per ∆F ¿ 1, la (3.32) fornisce il valore
        di Bs ' 2B come avevamo visto per un segnale FM a banda stretta.
3.4 Modulatori                                                                                            55


3.4        Modulatori
Metodo indiretto

Iniziamo con lo schema di Figura 3.6 in cui viene riportata la realizzazione di un
modulatore FM a banda stretta, cioè con un basso indice di modulazione βF per il
quale vale la relazione (3.21). Analogamente, per un modulatore PM a banda stretta,

           Integratore          2πKF                                                          A
    a(t)                 d(t)                                               -                      s(t)

                                                                            +
                                                   sin (2 π f0t + ϕ 0)

                                                 −π
                                                 2


                                                                   cos(2 π f0t + ϕ 0)




                         Figura 3.6: Modulatore FM a banda stretta.

con βP ¿ 1, riportiamo in Figura 3.7 uno schema realizzativo.

                  KP                                                                    A
           a(t)                                                -                            s(t)

                                                               +
                                       sin (2 π f0t + ϕ 0)

                                   −π
                                   2


                                                      cos(2 π f0t + ϕ 0)




                         Figura 3.7: Modulatore PM a banda stretta.

     Ora per ottenere un modulatore FM a larga banda si può utilizzare lo schema di
Armstrong riportato in Figura 3.8 in cui viene generato un segnale FM a banda stretta
s0 (t) dato da
                   A0 [cos(2πfo0 t + ϕ00 ) − 2πKF d(t) sin(2πfo0 t + ϕ00 )] ,  (3.42)
che in base alla (3.21) può essere scritto come
                          s0 (t) = A0 cos(2πfo0 t + ϕ00 + 2πKF d(t)) .                               (3.43)
     Il limiter di Figura 3.8 normalizza l’inviluppo di (3.42) ad una costante. Vediamone
il funzionamento.
56                                                                                                  Modulazione angolare

                                                                     Narrowband FM


                  2πKF                                               A'    '
                                                                                                           Up frequency conversion   A'' s(t)
 a(t)      d(t)                          -                                s(t)   Moltiplicatore   s''(t)
                                                        Limiter                  di frequenza                           PBF
                                                                                       xN
                                         +
           sin (2 π f0' t + ϕ 0')
                                                                                                      cos(2 π f0''t + ϕ''0)
                                    −π
                                    2


                                         cos(2 π f0' t + ϕ'0)




 Figura 3.8: Metodo indiretto o di Armstrong per generare un segnale FM a larga banda.

    Dato un segnale x(t) = Mx (t) cos(ϕx (t)), di banda Bx e portante f0 , la caratteristica
di un limitatore (vedi Figura 3.9) è di normalizzare l’inviluppo di x(t) squadrando il
segnale di ingresso,                   ½
                                            1, x(t) > 0
                               y(t) =                                                (3.44)
                                          −1, x(t) < 0
e rimuovendo tramite un PBF le armoniche di y(t) oltre quelle desiderate attorno f0 ,
per cui idealmente
                                        f − f0        f + f0
                      HP BF (f ) = rect        + rect        .                (3.45)
                                          Bx            Bx
In uscita avremo
                                 z(t) = cos(ϕx (t)) .                         (3.46)
    Ritornando allo schema di Figura 3.8, tramite un moltiplicatore di frequenza la
frequenza istantanea di s0 (t) viene moltiplicata per N , formando un segnale s00 (t) con
frequenza istantanea

                              fs00 (t) = (f00 + KF a(t))N = f00 N + KF N a(t) .                                                       (3.47)

In effetti mentre la banda del segnale modulante è sempre B, la massima deviazione
di frequenza e corrispondentemente l’indice di modulazione sono aumentati di un fat-
tore N . A partire dal segnale s00 (t), utilizzando un opportuno stadio di conversione
di frequenza, denominato up-frequency conversion, si può “spostare” s00 (t) attorno la
frequenza desiderata f0 = f00 N + f000 .

                        x(t)                                      y(t)                                         z(t)
                                               1
                                                                                       h
                                                   -1                                    PBF




                               Figura 3.9: Schema di un limitatore (limiter).

    Un metodo per elevare l’indice di modulazione è tramite lo schema di Figura 3.10
in cui s0 (t) del tipo (3.43) viene trasformato tramite un dispositivo non lineare con
3.4 Modulatori                                                                            57


        s'(t)                                                                    s(t)
                            N                    PBF             Up frequency
                      ( )                       (Nf 0' )          conversion




        Figura 3.10: Metodo per elevare l’indice di modulazione di un segnale FM.


legge esponenziale di ordine N cui risultato è la creazione di repliche del segnale s0 (t)
attorno alle frequenze nf00 , n = 1, .., N . Di tutte queste repliche il filtro selettivo se-
leziona la replica desiderata attorno f00 N alla quale corrisponde un segnale con indice
di modulazione pari a quello di s0 (t) moltiplicato per N .

Metodo diretto

Un metodo diretto per generare un segnale FM è tramite un VCO, come illustrato
in Figura 3.11, all’interno di una configurazione PLL che insegue una frequenza di
riferimento f0 /N generata da un oscillatore. Il divisore di frequenza è necessario per
abbassare l’indice di modulazione, diciamo a circa 0.2, del segnale all’uscita del VCO e
cosı̀ avere disponibile un segnale FM a banda stretta del tipo (3.21) con una riga alla
frequenza f0 /N sempre presente. La configurazione PLL serve per creare un’uscita s(t)
con una portante f0 molto stabile, grazie al meccanismo di feedback. Esistono inoltre


                                                                     a(t)


                cos(2 π f 0 t+ ϕ 0)
                         N
                                                       LPF



                                  Divisore di
                                  frequenza
                                      :N




                                                       VCO


                                                s(t)


      Figura 3.11: Metodo diretto per generare un segnale FM utilizzando un PLL.


schemi più semplici che utilizzano il solo principio del VCO controllato dal segnale di
informazione [2, 3].
58                                                                 Modulazione angolare


3.5      Demodulatori
Discriminatore

Lo schema è riportato in Figura 3.12 e fa uso di un filtro derivatore con specifiche ideali
del tipo
                                    Hd (f ) = jKd f .                                (3.48)
In effetti è sufficiente che siano verificate le condizioni
                        
                         |Hd (f )| = Kd f
                                                  per |f − f0 | < Bs /2                   (3.49)
                                         π
                            arg Hd (f ) = 2
e Hd (f ) = Hd∗ (−f ) per |f + f0 | < Bs /2. Allora, entro la banda passante di s(t) avremo

                       d
        sd (t) = K d      s(t)
                       dt                                                 Z t
               = −K d 2πA (f0 + KF a(t)) sin(2πf0 t + ϕ0 + 2πKF                 a(τ ) dτ ) (3.50)
                                                                           −∞




                       Filtro
                     derivatore
                       hd (t)
            s(t)                         sd (t)                                 ao(t)
                         K d                            Envelope
                          d                             detector
                            dt

             Figura 3.12: Demodulatore di frequenza del tipo discriminatore.

    in cui K d = Kd
                 2π
                    è una costante non essenziale.
Notiamo che il filtro derivatore ha tramutato un segnale FM in AM. Ora in (3.50) il
termine sinusoidale è un segnale FM con banda passante da f0 − Bs /2 a f0 + Bs /2
mentre il termine 2π(f0 + KF a(t)) ha una banda B. Sotto l’ipotesi che B < f0 − Bs /2,
estraendo l’inviluppo della (3.50) avremo, a parte fattori non essenziali


                                 a0 (t) = 2π|f0 + KF a(t)|
                                        = 2π(f0 + KF a(t))                                (3.51)
    essendo f0 À KF am = βB. Utilizzando un filtro notch per eliminare la DC
dalla (3.51) riotteniamo il segnale desiderato. La cascata del filtro derivatore e del
demodulatore di inviluppo prende il nome di discriminatore.
    Tra le varie strutture per realizzare un derivatore ricordiamo quella che fa uso
dell’approssimazione
                                                   d
                            s(t) − s(t − ∆T ) = ∆T s(t) ,                       (3.52)
                                                   dt
3.6 Prestazioni                                                                         59


se ∆T è sufficientemente piccolo o meglio ∆T ¿ 1/Bs . Questa relazione porta al
demodulatore phase shift illustrato in Figura 3.13.

        s(t)                                +                                   ao(t)
                                                               Envelope
                                                               detector
                                            _


                            Ritardo
                              ∆t


                Figura 3.13: Demodulatore di frequenza del tipo phase shift.

Phase locked loop

Lo schema è riportato in Figura 3.14. Notiamo che il blocco phase-difference (PD) è


                                 Phase difference
               s(t)                                                     ao(t)
                                                LPF




                                                VCO



                      Figura 3.14: Demodulatore di frequenza tramite PLL.

stato realizzato tramite un prodotto a cui segue un filtro passa basso. Si può verificare
che il VCO nell’inseguire la fase di s(t) produce un errore all’uscita del PD proporzionale
alla deviazione di frequenza istantanea di s(t), ∆fs (t). Di conseguenza l’uscita del
blocco PD è proprio il segnale desiderato.
    In tutti questi schemi, se il segnale di ingresso, a causa della distorsione introdotta
dal canale non ideale, non ha un inviluppo costante, la derivata del segnale produce un
termine di distorsione proporzionale alla derivata dell’inviluppo. E’ allora importante
precedere il derivatore da un limiter, del tipo illustrato in Figura 3.9.


3.6      Prestazioni
FM

Lo schema complessivo del ricevitore è riportato in Figura 3.15.
60                                                                                 Modulazione angolare


     In presenza del rumore introdotto dal canale, il segnale al ricevitore r(t) viene
filtrato da un filtro del tipo banda passante di banda Bs attorno la portante f0 . Il
segnale assume la forma
                     rRc (t) = ζA cos(2πf0 t + ϕ0 + 2πKF d(t)) + ωRc (t)                           (3.53)
dove C è dovuta all’attenuazione del canale mentre ωRc (t) è il filtraggio di ω(t), rumore
bianco con spettro N0 /2.

               PBF
     r(t)                 r (t)                                                                    ao(t)
                          Rc                                        d                   Envelope
               h                      Limiter
                Rc                                                                      detector
                                                                    dt
            Banda B s



              Figura 3.15: Schema complessivo semplificato di un ricevitore FM.

   Utilizzando la usuale scomposizione di ωRc (t) nelle componenti in fase e quadratura
attorno f0 ,
               ωRc (t) = ωRc,I (t) cos(2πf0 t + ϕ0 ) − ωRc,Q (t) sin(2πf0 t + ϕ0 ) ,               (3.54)
possiamo scrivere
                           ©              £                                      ¤ª
               rRc (t) = Re ej(2πf0 t+ϕ0 ) CAej2πKF d(t) + ωRc,I (t) + jωRc,Q (t)                  (3.55)
E’ proprio la fase del segnale
                          (bb)
                        rRc (t) = CAej2πKF d(t) + ωRc,I (t) + jωRc,Q (t)                           (3.56)
che porta il segnale di informazione. La variazione rispetto a 2πKF d(t) è dovuta al
rumore (vedi Figura 3.16).
                   (bb)
   L’ampiezza di rRc (t) è irrilevante poichè viene normalizzata dal limitatore. Indichi-
amo con ϑ(t) l’errore di fase introdotto dal rumore:
                                       (bb)
                                     rRc (t)          ωRc,I (t) + jωRc,Q (t)
                     M ejϑ(t) =        j2πK  d(t)
                                                  =1+                                              (3.57)
                                   CAe     F             CAej2πKF d(t)
    Ebbene, la derivata di ϑ(t) è il segnale che va a sommarsi a 2πKF a(t) all’uscita
della cascata derivatore-rivelatore di inviluppo. Qui omettiamo la derivazione e ripor-
tiamo solamente i punti salienti nel caso particolare il rapporto segnale-rumore Γ sia
sufficientemente elevato.
     i) L’errore di fase ϑ(t) dovuto al rumore all’uscita dl filtro di ricezione ha uno spettro
        bianco all’interno della banda (−B, B) del segnale desiderato:
                                                  N0
                                     Pϑ (f ) =                  ,       |f | < B                   (3.58)
                                                 C 2 A2

  ii) All’uscita del filtro derivatore, ϑ̇(t) avrà uno spettro di forma parabolica:
                                                        N0
                                  Pϑ̇ (f ) = (2πf )2                ,      |f | < B                (3.59)
                                                       C 2 A2
3.6 Prestazioni                                                                                      61


           Im




                                                          r (bb)
                                                           Rc                     w
                                                                                      Rc,Q

                                                         (t)
                                                                       wRc,I


                                           2 π KF d(t)

             0                                                                               Re


                                                             (bb)
                       Figura 3.16: Composizione del fasore rRc   (t).


 iii) La potenza di ϑ̇(t) è data da
                                         Z B
                                                                      N0 2 3
                            Mϑ̇ (f ) =         Pϑ̇ (f ) df = (2π)2            B                   (3.60)
                                          −B                         C 2 A2 3

Richiamando la potenza del termine desiderato (3.51), rimosso della DC, data da

                                     Mao = (2πKF )2 Ma ,                                          (3.61)

il rapporto segnale-rumore all’uscita del ricevitore ha la seguente espressione
                                                    (CA)        2
                                 (2πKF )2 Ma          2
                                                         3 KF2 Ma
                           Λo =                   =                                               (3.62)
                                (2π)2 CN 0 2
                                       2 A2 3 B
                                                3    N0 B B 2

Moltiplicando e dividendo la precedente espressione per kf2 e richiamando la definizione
di βF (3.17) e quella di Γ (2.93) dove
                                                   A2
                                           Ms =       ,                                           (3.63)
                                                   2
risulta
                                         Λo = 3kf2 βF2 Γ .                                        (3.64)
    Dalla espressione (3.64) notiamo che se kf βF > √13 , cioè per valori elevati dell’indice
di modulazione, il ricevitore MF è il più efficiente di quello AM. L’inconveniente è che un
βF elevato comporta anche una elevata banda richiesta, come si osserva dalla formula
di Carson (3.32).
    Il termine 3kf2 βF2 prende anche il nome di guadagno del ricevitore GRic . Ad esempio
nella radiodiffusione del suono in MF si utilizza una banda B = 15 kHz e βF = 5.
Corrispondentemente Bs = 2B(1 + βF ) = 180 kHz e assumendo un fattore di forma di
a(t) pari a kf2 = 21 , valore tipico per un segnale voce, risulta un guadagno del ricevitore
pari a
                                     (GRic )dB = 15.7 dB .                              (3.65)
62                                                                          Modulazione angolare


    Concludiamo questa sezione sulle prestazioni di un ricevitore FM ricordando che
le precedenti considerazioni e il risultato (3.64) valgono nell’ipotesi di basso rumore
rispetto al segnale desiderato e ciò comporta di aver un rapporto Γ superiore ad una
certa soglia data da
                                   Γth = 20(1 + βF ) .                            (3.66)
   In altre parole solo operando sopra soglia, ossia per Γ ≥ Γth , allora vale la (3.64).
Se Γ < Γth si può constatare un decadimento delle prestazioni secondo la legge
                                                        1
                                 Λo = 3kf2 βF2                    ;                        (3.67)
                                                 1 + 2(1+β)
                                                        Γ

il quale è riportato in Figura 3.17

                                                            β =5
                                                             F


              Λ o (dB)                                           β =3
                                                                  F



                                                                      β =1
                                                                        F

                                                                        Λo = Γ




                                                            Γth = 20(1+ βF )




                      0      5     10     15       20        25                  Γ (dB)


Figura 3.17: Andamento di Λo in funzione di Γ per diversi valori di β in un ricevitore FM.

    Dal momento che β determina sia le prestazioni Λo che la banda richiesta Bs ,
bisognerà determinare quale delle due condizioni è più restrittiva. Vediamo il seguente
esempio.

Esempio

   Si desidera progettare un sistema FM in modo tale che la potenza trasmessa Ms sia
minima. I requisiti e parametri del sistema siano i seguenti
3.6 Prestazioni                                                                       63



          Λo = 40 dB , Bs = 120 kHz
                                              N0
          B = 10 kHz , kf2 = 12 ,             2
                                                 = 0.5 10−8 (V 2 /Hz) ,   C=1.



Ora il vincolo sulla banda impone che

                                 2B(1 + βF ) ≤ 120 kHz ,                          (3.68)

per cui deve essere
                                           β≤5 .                                  (3.69)
Il vincolo su Λo , supponendo di lavorare sopra soglia, impone che

                                 3 kf2 βF2 20(1 + βF ) ≥ 104 ,                    (3.70)

per cui deve essere
                                         βF ≥ 6.6 .                               (3.71)
Di conseguenza il sistema è limitato i banda e scegliamo

                                          βF = 5 .                                (3.72)

Lavorando sopra soglia segue che deve essere

                                   Λo = 3 kf2 βF2 Γ = 104                         (3.73)

da cui segue
                                      (Γ)dB = 24 dB .                             (3.74)
Dall’espressione Γ = NM0sB si ricava infine

                                   (Ms )dBm = 14.3 dBm .                          (3.75)

Se non ci fosse stato il vincolo in banda allora per βF = 6.6 e (Γ)dB = 24 dB sarebbe
risultato
                                  (Ms )dBm = 11.8 dBm ,                         (3.76)
con un risparmio di 2.5 dB nella potenza trasmessa, però con una occupazione di banda
di 153 kHz.

PM

Secondo lo schema di Figura 3.3, per ottenere un demodulatore di fase è sufficiente
integrare l’uscita di un ricevitore FM.
    Dal punto di vista analitico si tratta di estrarre la fase del segnale all’uscita del
limiter. Procedendo come nel caso MF, si ottiene un rapporto segnale-rumore all’uscita
del ricevitore pari a
                                     Λo = kf2 βP2 Γ ,                              (3.77)
dove βP è definito in (3.17).
64                                                                              Modulazione angolare


3.7              Preenfasi e deenfasi nella FM
Nella FM abbiamo osservato come la densità spettrale del rumore all’uscita del ricevi-
tore abbia un andamento del tipo f 2 , cioè sia più concentrata verso le alte frequenze.
L’idea è allora di filtrare il segnale ricostruito a0 (t) con un ulteriore filtro hde (t) che
attenui maggiormente le alte frequenze. Per non distorcere il segnale di informazione
ricostruito bisognerà però filtrare il segnale di informazione a(t) con un filtro hpe il cui
andamento in frequenza è il reciproco di quello hde . In altre parole deve essere
                                                      1
                                       Hpe (f ) '            ,     |f | ≤ B ,                                (3.78)
                                                    Hde (f )

secondo lo schema di Figura 3.18.

     a(t)                                                                                                    ao(t)
                  hpe           Trasmettitore          Canale            Ricevitore                 hde
                                    FM                                      FM




     pe(f)                                                                       de(f)




             0    fa,1   fa,2      f                                                     0   fa,1         fa,2       f



                                Figura 3.18: FM con preenfasi e deenfasi.

   Naturalmente bisognerà scalare il segnale all’uscita del filtro hpe in modo che ri-
manga invariata la potenza del segnale modulante. Diversamente potrebbe aumentare
βF e di conseguenza la banda del segnale modulato.
   Nelle radio FM tipicamente
                                                                1
                                                Hde (f ) =                                                   (3.79)
                                                             1 + j ffc

con fc = 2100 Hz e B = 15 kHz. A parità di potenza trasmessa, il rapporto Λo
migliora di 6, 12 dB.
Capitolo 4

Confronto tra i vari metodi di
modulazione ed esempi di sistemi

Il criterio di confronto si basa sulla banda occupata Bs , prestazioni (guadagno) del
ricevitore e complessità realizzativa.

Banda Bs

    La modulazione più efficiente in banda occupata è la SSB-SC con Bs = B. Essa è
utilizzata nelle applicazioni con restrizioni in banda in cui a(t) non ha DC, tipo nelle
trasmissioni voce alle microonde e nelle trasmissioni satellitari. Per trasmissioni di
segnale video si utilizza la VSB. Di certo non si utilizza la FM nei sistemi in cui la
banda è scarsa.

Efficienza in potenza (o guadagno GRic )

    La FM si utilizza nelle applicazioni in cui la potenza trasmessa è critica, ad esempio
nelle trasmissioni radio ad alta fedeltà. Di certo le DSB-TC e SSB-TC sono le meno
efficienti.

Complessità realizzativa

    AM con demodulatore non coerente e FM sono i sistemi con ricevitore più semplice
da realizzare. Di fatto questi sistemi sono molto usati nelle applicazioni broadcasting
tipo radio AM, video, radio FM ad alta fedeltà ed FM stereo.
    La SSB-SC richiede un demodulatore sincronizzato che è alquanto complesso, per
cui non viene utilizzata nelle applicazioni broadcasting. Tantomeno viene utilizzata la
DSB-SC che richiede il doppio della banda.


4.1      Esempi di sistemi di trasmissione analogici
Prima di passare in rassegna alcuni sistemi di trasmissione, riportiamo in dettaglio
la tipica configurazione del f ront − end di un ricevitore radio che va sotto il nome
di supereterodina [1, Cap. 18]. Recentemente, per le radio digitali sono emerse ar-
chitetture alternative con “conversione diretta”, le quali hanno il vantaggio di essere
integrabili in un singolo chip [1].

                                            65
66          Confronto tra i vari metodi di modulazione ed esempi di sistemi


4.1.1     Ricevitore supereterodina

L’obiettivo del f ront − end di un ricevitore radio è di estrarre il segnale modulato
desiderato, corrotto dal rumore, dalla miriade di segnali presenti nell’aria. La strut-
tura è riportata in Fiugura 4.1. Il principio è di traslare in giù lo spettro del segnale
desiderato corrotto dal rumore, diciamo dalle radio frequenze (RF) alle frequenze inter-
medie (IF). A questo punto il segnale può essere rivelato tramite un demodulatore del
tipo esaminato nei capitoli precedenti. Il filtro RF, del tipo passabanda, ha il compito
di amplificare il segnale prima di entrare nel mixer, il quale, tra l’altro introduce esso
stesso del rumore.
    Il compito del filtro RF è anche quello di attenuare molti dei segnali che si trovano
spettralmente vicino al segnale desiderato, secondo specifiche che vedremo tra poco.
Ad ogni modo la reiezione dei canali adiacenti è demandata al filtro alle frequenze
intermedie posto dopo il mixer.
    Sia f0 la frequenza della portante del segnale desiderato e Bs la sua banda. Se-
lezioniamo inoltre una volta per tutte la frequenza portante fIF del filtro IF. scegliamo
allora come frequenza dell’oscillatore locale


                                     fLO = f0 + fIF .                                  (4.1)


In tal caso sarà fLO > f0 . Il sintonizzatore seleziona come frequenza centrale del filtro
RF proprio f0 e come frequenza dell’oscillatore locale fLO , data dalla (4.1).
Notiamo che a differenza di fIF che è fissa, f0 e di conseguenza fLO sono variabili e
dipendono dalla “stazione radio” su cui desideriamo sintonizzarci.
   All’uscita del mixer avremo due repliche, o immagini, del segnale filtrato rRF (t),
una attorno la frequenza f0 + fLO = 2f0 + fIF e l’altra attorno f0 − fLO = −fIF . Per
simmetria avremo anche immagini complesso coniugate in ampiezza attorno −(f0 +fLO )
e −(f0 − fLO ) = fIF .
    Successivamente il filtro IF farà passare solo le imagini attorno ±fIF ed eliminerà
quelle attorno ±(2f0 + fIF ). Naturalmente la banda passante del filtro RF deve essere
specificata altrimenti il segnale desiderato all’uscita del filtro IF sarà effetto da inter-
ferenza. Notiamo infatti che se in rRF (t) è presente un segnale con portante f0 + 2fIF ,
dopo il mixer esso creerà una immagine attorno fIF che andrà ad interferire il segnale
desiderato. Come illustrato in Figura 4.2, se l’amplificatore RF ha una banda BRF
compresa tra Bs e 2fIF − Bs , attorno f0 , non vengono create immagini dei segnali
interferenti entro la banda desiderata attorno fIF . Tipicamente si seleziona per il filtro
RF una frequenza di taglio (in corrispondenza dell’inizio della banda attenuata) circa
pari a f0 ± fIF . Se ∆f è la spaziature tra le portanti dei canali vicino a quello desider-
atoè facile vedere che la banda di transizione del filtro IF può estendersi da fIF ± B2s
ad fIF ± (∆f − B2s ).
    Ci sono schemi in cui fLO < f0 , per fLO = f0 − fIF . All’uscita del mixer avremo
un’immagine desiderata attorno f0 − fLO = fIF e una attorno f0 + fLO = 2f0 − fIF che
viene attenuata dal successivo filto IF. In questo caso il segnale desiderato non risulta
“invertito in frequenza”. Anche in questo caso la banda del filtro RF può estendersi da
Bs fino ad un valore massimo 2fIF − Bs , altrimenti ci possono essere sovrapposizioni
in banda IF con altre stazioni trasmittenti.
                    PBF centrato                                           PBF centrato
                      attorno f0                                             attorno fIF
                     di banda BRF                                           di banda Bs
     r(t)         Filtro amplificatore   r (t)    Mixer                                                            ao (t)
                                          RF                           Filtro amplificatore
                          RF                                                    IF                  Demodulatore
Segnale radio
a largo spettro          ( f0 )                                                ( fIF )


                                  cos(2 π fL0 t+ ϕL0)


                                                          fL0 = fIF + f0
                                                                                                                            4.1 Esempi di sistemi di trasmissione analogici




                             Sintonizzatore

                            (comandato dalla
                            manopola   della
                            radio)




                           Figura 4.1: Ricevitore radio con f ront − end del tipo supereterodina.
                                                                                                                            67
68                            Confronto tra i vari metodi di modulazione ed esempi di sistemi
   Ingresso filtro RF




                                                                          Bs         Bs



                                                       ...                                   ...         ...                       ...
                                                                                                                                   f
             0
                                                                          f0                       fL0              fL0+fIF = f0 +2f IF

                                                                               ∆f

                                                                                       fIF                 f
                                                                                                               IF
   Maschera filtro RF




                        1




             0                                                                                                                      f
                            f0 - 2f IF+ Bs /2                f0 - Bs /2   f0   f0 + Bs /2                       f0 +2f - B /2
                                                                                                                      IF    s
 Maschera filtro IF




                        1



                                         fIF - Bs /2 + ∆ f
        0                                                                                                                           f
        fIF - Bs /2         fIF   fIF + Bs /2
 Uscita filtro IF




        0                                                                                                                          f
                            fIF




Figura 4.2:                        Illustrazione dei segnali nel dominio dela frequenza in un ricevitore
supereterodina.
4.1 Esempi di sistemi di trasmissione analogici                                                                       69


4.1.2        Radio FM
Il sistema radio FM viene utilizzato per trasmettere voce e musica con una banda di
15 kHz. Il sistema utilizza la tecnica FDM e occupa lo spettro 88 ÷ 108 M Hz con
portanti separate di 200 kHz. La modulazione è FM con βF = 5 (∆F = 75 kHz) e
viene utilizzata la preeenfasi. Il ricevitore, con f ront − end di tipo supereterodina è
riportato in Figura 4.3 dove fIF = 10.7 M Hz

                                                       Bs = 180 kHz

            Filtro amplificatore         Mixer
                                                           PBF                        Limitatore
                    RF                                                                                  ampl. audio
                                                                                          +
                                                                                                            +
                                                                                    demodulatore
                   ( f0 )                                  (f IF)                        FM
                                                                                                         deenfasi

                                                       fIF = 10.7 MHz
                       cos(2 π fL0 t+ ϕL0)




                     Sintonizzatore




                                          Figura 4.3: Ricevitore radio FM.




                   l (f) +   r(f)
                                                                        l (f) -   r(f)




        0                           15       19   23                         38                    53   f (kHz)



                  Figura 4.4: Spettro dei segnali all’ingresso del modulatore FM.


4.1.3        Radio FM stereo
A partire dai due segnali stereo sl (t) e sr (t), vengono formati i segnali somma sl (t)+sr (t)
e differenza sl (t) − sr (t), i quali vengono moltiplati in frequenza (FDM) utilizzando la
tecnica DSB-SC per il segnale differenza (vedi Figura 4.4). In tal modo il sistema è
70               Confronto tra i vari metodi di modulazione ed esempi di sistemi


compatibile con il sistema tradizionale, non stereo, prelevando solo le componeti fino
a 15 kHz. Come illustrato in Figura 4.5, il segnale composto dalla somma, segnale
DSB-SC e la portante (utilizzata in ricezione per demodulare il segnale DSB) vengono
sommati e modulati FM utilizzando una banda di 200 kHz (β ' 0.9).



     sl (t)      +
                              Preenfasi
                 +

                                                                                                   Bs = 200kHz
     sr (t)      +                                    Modul.                                                     s(t)
                                                     DSB-SC                                          Modul.
                 _            Preenfasi
                                                       (2f 0)                                         FM

                                                                Moltiplicatore
                                                                di frequenza

                                                                    x2




                                                                           f 0 = 19 kHz




                                                                                                              sl (t)
                                              LPF
                                          0 : 15 kHz                                      Deenf.

                                                         Moltiplicatore
                                                         di frequenza
        Stadio       Demod.                 NBF              x2                   Indicat.
        RF IF          FM                 a 19 kHz                               di stereo

                                                                                                              sr (t)
                                         BPF                          Demod.
                                      23 : 53kHz                                          Deenf.
                                                                       DSB




                     Figura 4.5: Trasmettitore e ricevitore per radio FM stereo.

In ricezione abbiamo le operazioni inverse.




4.1.4         Segnale televisivo
Un canale TV occupa una banda di 6 M Hz mentre il segnale video commerciale ha una
banda di 4.2 M Hz. In effetti per motivi realizzativi lo spettro del segnale modulato è
di tipo VSB-TC dopo il filtro IF in ricezione, mentre in trasmissione occupa una banda
maggiore, secondo l’illustrazione di Figura 4.6. Il segnale trasmesso, con tecnica FDM,
include in parte il segnale video con banda di 4.2 M Hz e in parte l’audio, modulato
4.1 Esempi di sistemi di trasmissione analogici                                                71


FM attorno 4.5 M Hz. Per uno schema realizzativo del trasmettitore e ricevitore,
rimandiamo a [4].



                                 Filtro IF in ricezione (tipo VSB)



                                  Segnale video                                Segnale audio




      -1.25 -0.75    0                                               4   4.5       f (MHz)

                (portante f 0)

                                       6



                    Figura 4.6: Occupazione i banda del segnale TV.
            Parte II

Esercizi sui filtri numerici e FFT




                73
Capitolo 5

Filtri numerici

In questa sezione, considereremo soprattutto alcuni esercizi relativi al filtraggio dei
segnali. L’attenzione verrà posta al filtraggio dei segnali a tempo discreto, e si supporrà
dunque di avere a che fare con segnali definiti su Z(T ).
   La relazione ingresso-uscita di un filtro definito su Z(T ) con risposta impulsiva
h(t), t ∈ Z(T ), risulta come noto data dall’operazione di convoluzione
                         +∞
                         X                                 +∞
                                                           X
            y(nT ) = T          h(kT )x(nT − kT ) = T            x(kT )h(nT − kT ).     (5.1)
                         k=−∞                             k=−∞

    Cominceremo con l’introdurre alcuni concetti fondamentali per la realizzazione e
la comprensione dei filtri a tempo discreto. Il lettore potrà rivelarne l’analogia con
concetti relativi ad altre discipline, in cui si considerano sistemi a tempo continuo.


5.1      Stabilità BIBO di un filtro numerico
Un filtro numerico si dice stabile in senso BIBO (Bounded Input-Bounded Output) se
l’uscita ad un ingresso limitato è anch’essa limitata. Si ricorda che il segnale x(nT ) è
limitato se esiste un numero finito M tale che
                              |x(t)| ≤ M,    per ogni t ∈ Z(T ).                        (5.2)
Vengono ora analizzate le condizioni per cui la traformazione lineare (5.1) risulta stabile
in senso BIBO. Come è logico attendersi, le condizioni riguardano la risposta impulsiva
h(nT ). Si ha infatti
                                       +∞
                                       X
                         |y(nT )| ≤          T |h(kT )||x(nT − kT )|
                                      k=−∞
                                         +∞
                                         X
                                    ≤M            T |h(kT )|,
                                           k=−∞

dove si è sfruttato il fatto che, per un ingresso limitato, vale la (5.2). Se dunque la
somma dei moduli della risposta impulsiva del filtro è finita, cosı̀ risulta l’uscita y(nT ).
La relazione precedente stabilisce una condizione sufficiente per la stabilità BIBO. Tale
condizione è anche necessaria: se infatti fosse
                                    +∞
                                    X
                                        T |h(kT )| = +∞                                  (5.3)
                                    k=−∞


                                              75
76                                                                       Filtri numerici


e h(kT ) non fosse limitata, basterebbe prendere l’ingresso x(nT ) = δZ(T ) (nT ) per
ottenere un’uscita y(nT ) = h(nT ) non limitata. Se infine valesse la (5.3) e h(kT ) fosse
limitata, basterebbe prendere l’ingresso x(nT −kT ) = h∗ (kT )/|h(kT )|, per |h(kT )| 6= 0
e 0 altrove, per avere y(nT ) = +∞ all’istante nT . Possiamo dunque concludere con il
seguente Teorema.

Teorema 1 Un filtro sui tempi discreti caratterizzato dalla risposta impulsiva h(t), t ∈
Z(T ) è stabile in senso BIBO se e solo se
                                  +∞
                                  X
                                         T |h(kT )| = +∞.
                                 k=−∞

   Dunque, un filtro risulta stabile in senso BIBO se la sua risposta impulsiva decade
in maniera sufficientemente rapida, per nT che tende a più o meno infinito, in modo
che valga la
                                 X+∞
                                       T |h(kT )| < +∞
                                  k=−∞

    Si introduce la seguente nomenclatura: un filtro a tempo discreto si dice di tipo FIR
(Finite Impulse Response) se la sua risposta impulsiva è di durata finita. Viceversa,
esso si dice di tipo IIR (Infinite Impulse Response) se la sua risposta impulsiva ha
durata non limitata.


5.2      Risposta in frequenza razionale
Una classe molto importante di filtri a tempo discreto è la classe dei filtri causali
a risposta in frequenza razionale, tali cioè che la trasformata di Fourier H(f ), f ∈
R/Z(T ), della risposta impulsiva h(t), t ∈ Z(T ), assume la forma
                                          P
                                      T rk=0 bk e−j2πf kT
                             H(f ) = Pq             −j2πf kT
                                                             ,                    (5.4)
                                           k=0 ak e

dove si può porre, senza perdita di generalità, a0 = 1. Nel caso infatti fosse a0 6= 1,
basterebbe dividere numeratore e denominatore per a0 . La risposta in frequenza H(f )
risulta, come è noto e come si vede immediatamente dalla (5.4), una funzione periodica
in f di periodo Fs = 1/T .
    Il termine razionale risulta più comprensibile se, anziché considerare la trasformata
di Fourier (5.4), ci riferiamo alla trasformata zeta della risposta impulsiva, detta anche
funzione di trasferimento del filtro,
                                            +∞
                                            X
                                       ∆
                               Hz (z) = T          h(nT )z −n ,
                                            n=−∞

la quale risulta un rapporto fra polinomi in z −1 . Infatti, ricordando che la trasformata
di Fourier si ottiene dalla trasformata zeta ponendo z = exp(j2πf T ), nell’ipotesi di
esistenza di entrambe, dalla (5.4) si ottiene
                                            P
                                          T rk=0 bk z −k
                                 Hz (z) = Pq           −k
                                                          .                           (5.5)
                                              k=0 ak z
5.2 Risposta in frequenza razionale                                                            77


    Vedremo come la classe dei filtri a risposta in frequenza razionale possa essere
realizzata mediante algoritmi numerici estremamente semplici.
    Consideriamo dapprima alcuni semplici esempi.
Esempio 1. La sequenza esponenziale.
     Consideriamo il filtro a tempo discreto con risposta impulsiva causale h(nT ) = pn 10 (nT ).
Il filtro è stabile in senso BIBO se risulta |p| < 1. In tali ipotesi, la risposta in frequenza è
una funzione razionale e risulta
                                          T
                           H(f ) =                 ,       f ∈ R/Z(1/T ).
                                     1 − pe−j2πf T
La trasformata zeta vale
                                                    T
                                        H(z) =                                               (5.6)
                                                 1 − pz −1
e presenta un polo in z = p all’interno del cerchio unitario del piano complesso e uno zero
nell’origine. La regione di convergenza della trasformata zeta è la regione |z| > |p|.
   Consideriamo invece un filtro con risposta in frequenza
                                          T
                           H(f ) =                 ,       f ∈ R/Z(1/T ),
                                     1 − pe−j2πf T

dove però sia |p| > 1. In questo caso, l’antitrasformata risulta, come è immediato verificare,
un segnale anti-causale ed uguale a

                                   h(nT ) = −pn 10 (−nT − T ).

Si tratta anche in questo caso di un filtro stabile in senso BIBO. La trasformata zeta vale
                                                    T
                                        H(z) =
                                                 1 − pz −1

ma questa volta la regione di convergenza risulta |z| < |p|.
    Infine, un filtro con risposta impulsiva causale h(nT ) = pn 10 (nT ), con |p| ≥ 1, non è
ovviamente stabile in senso BIBO. La sua trasformata zeta assume ancora la forma (5.6)
e converge per |z| > |p|, mentre la sua trasformata di Fourier non esiste (almeno in senso
ordinario).
    Un facile esercizio, risolvibile applicando più volte la regola di derivazione della trasfor-
mata di Fourier, permetterebbe di stabilire che la sequenza causale

                                   (n + k − 1)! n
                        h(nT ) =               p 10 (nT ),        nT ∈ Z(T ),                (5.7)
                                    n!(k − 1)!

stabile in senso BIBO per |p| < 1, ha trasformata di Fourier

                                            T
                           H(f ) =                     ,     f ∈ R/Z(T )                     (5.8)
                                     (1 − pe−j2πf T )k

e trasformata zeta, convergente per |z| > |p|,

                                                     T
                                     Hz (z) =                 .                              (5.9)
                                                (1 − pz −1 )k

    In conclusione, le (5.7)-(5.9), valide per k ≥ 1, forniscono il legame segnale-trasformata
relativo a sequenze causali e stabili con andamento esponenziale nel dominio del tempo e forma
razionale nel dominio della trasformata. In particolare, dato che ci limitiamo a considerare
78                                                                                 Filtri numerici


sequenze causali, la trasformata zeta (5.9) ha un polo, di molteplicità k, all’interno del cerchio
unitario e uno zero di molteplicità k nell’origine.
                                                                                                     2
    Consideriamo ora il caso della generica trasformata zeta razionale (5.5). Il calcolo
della antitrasformata è banale se q = 0. In tale caso, infatti, Hz (z) si riduce ad un
polinomio in z −1 e i coefficienti della risposta impulsiva risultano uguali a h(nT ) = bn
per n = 0, ..., r, e 0 altrove. La risposta impulsiva è dunque, in questo caso, di tipo
FIR.
    Nel caso q 6= 0, il modo di procedere è quello di sviluppare la (5.5) in frazioni
parziali: possiamo scrivere

                                        b0 + b1 z −1 + ... + br z −r
                         Hz (z) = T
                                        1 + a1 z −1 + ... + am z −q
                                                                                                (5.10)
                                         b0 + b1 z −1 + ... + br z −r
                                  =T                                         ,
                                     (1 − p1 z −1 )m1 · · · (1 − ps z −1 )ms

dove pi è il polo i-esimo della trasformata zeta, e mi la rispettiva molteplicità, con
m1 + ... + ms = q. Supponendo r < q nella espressione della trasformata zeta1 , la
(5.10) può essere scritta nella forma
                                m1
                                X                         ms
                                                          X
                                      A1j                         Asj
                     Hz (z) =               −1  j
                                                  + ... +               −1 )j
                                                                              ,                 (5.11)
                              j=1
                                  (1 − p1 z    )          j=1
                                                              (1 − ps z

dove, come è noto,

                      1         1      dmi −j £                 −1 mi
                                                                      ¤
          Aij =                   m −j  −1 m −j
                                                H z (z)(1 − pi z )      z=pi
                                                                             .                  (5.12)
                  (mi − j)! (−pi ) i d(z ) i

Si noti che la derivata viene fatta rispetto alla variabile w = z −1 . Si noti inoltre che nel
caso di un polo pi con molteplicità unitaria, il coefficiente Ai1 si calcola semplicemente
dalla (5.12) valutando la funzione Hz (z)(1 − pi z −1 ) per z = pi .
    Possiamo calcolare l’antitrasformata di Hz (z) usando i risultati dell’esempio prece-
dente. Se ne conclude che, se tutti i poli pi sono in modulo minori di 1, l’antitrasformata
della Hz (z) corrisponde alla combinazione lineare di sequenze con andamento esponen-
ziale della forma (5.7). Nel caso fosse r ≥ q, alla combinazione di esponenziali si
aggiungerebbe nella risposta impulsiva un contributo di durata finita, corrispondente
all’antitrasformata di un polinomio in z −1 .
Esempio 2.
   Si consideri un filtro causale con funzione di trasferimento
                                              1.5 + 0.5z −1 + 0.2z −2
                                 Hz (z) = T                           .                          (5.13)
                                               1 − 0.7z −1 + 0.1z −2
Si ricava facilmente che i poli di Hz (z) valgono z = 0.5 e z = 0.2 e sono quindi interni al
cerchio di raggio unitario. Se ne deduce che Hz (z) è la funzione di trasferimento di un filtro
     1
    Se cosı̀ non fosse, basterebbe prendere il resto della divisione del numeratore per il denominatore,
scomponendo Hz (z) nella somma di un polinomio in z −1 e di una funzione razionale della forma
voluta.
5.3 Equazioni alle differenze                                                                   79


causale e stabile. Applicando la scomposizione in frazioni parziali, dopo avere calcolato il
resto della divisione fra numeratore e denominatore, si trova
                                    ·                                ¸
                                                 5.5          6
                          Hz (z) = T 2 +                −              .
                                             1 − 0.5z −1 1 − 0.2z −1

La risposta impulsiva del filtro risulta pertanto di tipo IIR

                  h(nT ) = 2T δZ(T ) (nT ) + 5.5 · 0.5n 10 (nT ) − 6 · 0.2n 10 (nT ).

                                                                                                 2



5.3       Equazioni alle differenze
Si consideri un filtro con una risposta in frequenza razionale, come nell’equazione (5.4).
La relazione ingresso-uscita del filtro, espressa nel dominio della frequenza, risulta

                             Y (f ) = H(f )X(f ),        f ∈ R/Z(T ),                        (5.14)

dove Y (f ) e X(f ) sono la trasformata di Fourier dell’uscita e dell’ingresso, rispettiva-
mente. Moltiplicando entrambi i membri della (5.14) per il denominatore di H(f ) e
ricordando la regola di traslazione per la trasformata di Fourier, si ottiene nel dominio
del tempo la seguente relazione ricorsiva fra y(nT ) e x(nT )
                                q                            r
                                X                            X
                   y(nT ) = −          ak y((n − k)T ) + T         bk x((n − k)T ).          (5.15)
                                 k=1                         k=0


L’equazione lineare alle differenze finite (5.15), corrispondente ad una funzione di
trasferimento razionale, può facilmente essere realizzata mediante un algoritmo nu-
merico, come esemplificato nello schema di Fig. 5.1.
    La sua struttura suggerisce anche la forma normalizzata
                                  q                         r
                                  X                         X
                    y(nT ) = −          ak y((n − k)T ) +         b0k x((n − k)T ),
                                  k=1                       k=0


in cui vengono definiti i coefficienti b0k = T bk .
Esempio 3. La funzione di trasferimento (5.13) corrisponde alla seguente equazione alle
differenze

y(nT ) = 0.7y((n − 1)T ) − 0.1y((n − 2)T ) + 1.5T x(nT ) + 0.5T x((n − 1)T ) + 0.2T x((n − 2)T ).
                                                                                             (5.16)
Come si vede, l’uscita al tempo nT dipende dai valori precedenti dell’ingresso e dell’uscita. Se
però l’ingresso x(nT ) è nullo per nT < n0 T , anche l’uscita y(nT ) risulta nulla per nT < n0 T ,
dato che il filtro è causale e risulta h(nT ) = 0 per nT < 0. In tali ipotesi, il sistema (5.16)
evolve a partire da condizioni iniziali nulle a partire dall’istante nT0 .
    È possibile scrivere il seguente programma MATLAB per il calcolo dell’uscita da n0 T = 0
a nT = 100T corrispondente all’ingresso x(nT ) = sin(2πf0 nT )10 (nT ), con T = 1, f0 = 0.1T .
80                                                                       Filtri numerici

                   x(nT)                                      x(nT-rT)
                              T          T               T


                           Tb0     Tb1                Tbr-1      Tbr



                                             +

                                                                       y(nT)
                                             +


                                             +


                           -a q    -a q-1             -a 1


                              T          T               T
              y(nT-qT)

        Figura 5.1: Schema per la realizzazione dell’equazione a differenze finite.


% condizioni iniziali -caricamento dello ‘‘stato’’ del filtro

xs=[0,0];
ys=[0,0];
r1=length(xs);
q1=length(ys);

% istante iniziale
n0=0;

n=n0;
T=1;

while (n>=n0 & n<=100),

% nuovo ingresso

 xnT=sin(2*pi*0.1*n);

% calcolo dell’uscita: l’indice n+1 e‘ relativo al campione y(nT)

 y(n+1)=[0.7 -0.1]*ys’ + [1.5 0.5 0.2]*[xnT xs]’;

% aggiornamento dello stato

 ys=[y(n+1),       ys(1:q1-1)];
 xs=[xnT,          xs(1:r1-1)];
5.3 Equazioni alle differenze                                                               81



  n=n+1;
end;

                                                                                             2
    Nell’esempio precedente abbiamo visto come possiamo utilizzare la (5.15) per il
calcolo dell’uscita di un filtro causale con funzione di trasferimento razionale quando
l’ingresso è nullo prima di un certo istante. Come possiamo calcolare l’uscita nel
caso in cui l’ingresso sia diverso da zero, in generale, da meno infinito a più infinito?
Ovviamente, saremo interessati dal punto di vista operativo a conoscere l’uscita a
partire da un certo istante t di osservazione. Per poter utilizzare la (5.15) dovremmo
però conoscere le condizioni iniziali, specificate anche dai valori precedenti dell’uscita,
che purtroppo in generale non conosciamo dato che stiamo cercando di calcolarla.
    La soluzione del problema si ottiene in maniera semplice se il segnale di ingresso
x(t), t ∈ Z(T ), ha una durata convenzionale praticamente limitata. In questo caso,
infatti, è sufficiente pensare che il segnale sia nullo al di fuori di un certo intervallo ed
usare la (5.15) per calcolare l’uscita del filtro con la precisione voluta.

                      h(kT )




                                        n1 T                           kT

                      x(kT )



                                                                       kT

                      xT (kT )



                                               n0 T                    kT

                      h(n0 T + n1 T − kT )



                                                                       kT

Figura 5.2: Nel calcolo della convoluzione, all’istante n0 T +n1 T le uscite corrispondenti
a x(t) e xT (t) coincidono (praticamente).

   Nel caso invece il segnale abbia un andamento persistente, come ad esempio avviene
per i segnali sinusoidali, il segnale a gradino, o anche, in generale, per le realizzazioni dei
82                                                                           Filtri numerici


processi aleatori, è utile fare la seguente osservazione. Come abbiamo visto, la risposta
impulsiva h(nT ) di un filtro causale stabile con risposta in frequenza razionale ha un
andamento dato dalla somma di una sequenza di durata finita e di un certo numero di
sequenze esponenziali. Nei limiti di una precisione prefissata, tale risposta impulsiva
può considerarsi in ogni caso trascurabile a partire da un certo istante t = n1 T che
dipende dalla velocità di decadimento degli esponenziali, e quindi dal modulo dei poli
della funzione di trasferimento. Più i poli sono piccoli in modulo, più velocemente si
esaurisce la risposta impulsiva. Di conseguenza, se approssimiamo l’ingresso x(nT )
con una sua versione troncata xT (nT ) = x(nT )10 (nT − n0 T ), le uscite y(nT ) = x ∗
h(nT ) e yT (nT ) = xT ∗ h(nT ) sono praticamente uguali per t ≥ n0 T + n1 T (vedi
Fig. 5.2). Il calcolo di yT (nT ) può dunque essere effettuato utilizzando l’equazione alle
differenze (5.15) a partire da condizioni iniziali nulle: dopo un numero di campioni di
uscita pari a n1 T , ovvero dopo l’esaurimento del transitorio del filtro, i campioni di
yT (nT ) coincidono praticamente con quelli che si sarebbero ottenuti filtrando l’ingresso
originario. Si dice in questo caso che, dopo l’esaurimento del transitorio, l’uscita del
filtro è in regime permanente. Si noti l’analogia con la nomenclatura ed i concetti usati,
anche in altre discipline, per i segnali a tempo continuo.


5.4      L’uso di MATLAB per il progetto dei filtri
Abbiamo visto nella sezione precedente come sia possibile realizzare tramite un algorit-
mo numerico un filtro a tempo discreto con risposta in frequenza razionale. Esistono in
realtà dei criteri di organizzazione dei calcoli che rendono la realizzazione del filtro più
robusta, ad esempio qualora sia necessario utilizzare processori che utilizzano un’arit-
metica a precisione finita. Il programma MATLAB fornisce con il Signal Processing
Toolbox un insieme di procedure per il filtraggio a tempo discreto. In particolare, la
funzione filter(b,a,x), supponendo uguale ad 1 il primo elemento a(1) del vettore
a, filtra i dati contenuti nel vettore x di ingresso realizzando l’equazione alle differenze
y(n) = b(1)*x(n) + b(2)*x(n-1) + ... + b(nb+1)*x(n-nb)
                         - a(2)*y(n-1) - ... - a(na+1)*y(n-na).
Si noti che i coefficienti del vettore b(i) devono essere posti uguali a T bi−1 , secondo
quanto richiesto nella (5.15)2 .
    La funzione [H,f]=freqz(b,a,N,Fs) calcola N campioni complessi equispaziati
fra 0 e Fs /2, con Fs = 1/T , della trasformata di Fourier corrispondente alla funzione
di trasferimento razionale
                                 b(1) + b(2)z −1 + ... + b(nb + 1)z −nb
                      Hz (z) =                                          .
                                  1 + a(2)z −1 + ... + a(na + 1)z −na
In particolare, gli N valori della risposta in frequenza vengono posti nel vettore H,
mentre i rispettivi valori della frequenza, in Hz, vengono posti nel vettore f. Si noti
che la trasformata di Fourier H(f ) = Hz (ej2πf T ) ha simmetria hermitiana, e quindi ci
si può limitare a specificarla tra 0 e Fs /2.
    Per l’analisi di una funzione di trasferimento, sono utili anche le procedure residue
e roots che calcolano, rispettivamente, la scomposizione in frazioni parziali di un
rapporto di polinomi e le radici di un polinomio.
     2
    Gli algoritmi di MATLAB assumono che T =1. Ci si può facilmente ricondurre al caso generale
supponendo di riferirci ai coefficienti normalizzati T bk .
5.4 L’uso di MATLAB per il progetto dei filtri                                             83


    Un argomento di fondamentale importanza, cui qui accenneremo soltanto parzial-
mente, riguarda il progetto di filtri numerici. Il problema che qui ci si pone è il seguente:
assegnata una determinata risposta in frequenza del filtro, come è possibile determinare
i coefficienti bi e ai di una risposta in frequenza razionale che approssimi l’andamento
voluto? Esistono a questo proposito molte tecniche di progetto, relative sia a filtri FIR
(q = 0 nella (5.5)), che a filtri IIR.
    Tipicamente, i filtri che si desidera realizzare hanno un andamento della risposta in
frequenza che approssima uno degli andamenti ideali di Fig. 5.3, relativi a filtri passa-
basso, passa-alto, passa-banda e elimina-banda, rispettivamente. Nella Fig. 5.3, le
frequenze sono normalizzate rispetto alla frequenza di campionamento Fs . Trattandosi
di filtri reali, è sufficiente rappresentare l’andamento della risposta in frequenza fra
f = 0 e f = Fs /2. Come vedremo, i vari metodi di progetto si limitano molto spesso
a specificare solamente il modulo della risposta in frequenza desiderata.

          H(f )    a)                          H(f )     b)




                                     0.5 f                                 0.5 f
          H(f )    c)                          H(f )     d)




                                     0.5 f                                 0.5 f

Figura 5.3: Andamento dei filtri ideali a) passa-basso, b) passa-alto, c) passa-banda e
d) elimina-banda

    Trattandosi di un problema di approssimazione, occorrerà specificare nel progetto
le tolleranze ammesse nella realizzazione del filtro. A questo proposito, si consideri la
Fig. 5.4. In essa, viene rappresentato il modulo della risposta in frequenza (l’asse delle
ascisse è parametrizzato rispetto a f /Fs ) di un tipico filtro numerico che approssima
un filtro passa-basso ideale. I parametri da considerare sono:

   1. la banda passante, specificata dalla frequenza Wp . Si richiede che il filtro abbia
      modulo della risposta in frequenza circa uguale ad 1 per 0 ≤ f ≤ Wp . Per un
      filtro passabanda, andrà in genere specificato un intervallo di frequenze entro il
      quale si desidera che il filtro abbia modulo della trasformata di Fourier unitario;

   2. la banda oscura, specificata in questo caso dalla frequenza Ws . Si richiede che il
      filtro abbia modulo della risposta in frequenza circa uguale a 0 per Wp ≤ f ≤
      Fs /2. L’intervallo [Wp , Ws ] specifica la cosiddetta banda di transizione del filtro;

   3. il ripple in banda passante, quantificato tramite il valore Rp (spesso espresso in
      dB) che permette di determinare l’errore rispetto all’andamento desiderato;
84                                                                                            Filtri numerici

                     1.2



                        1
                   Rp
                     0.8



                     0.6



                     0.4



                     0.2


                                                                                              Rs
                        0
                         0   0.10   0.2   0.30   0.4   0.50   0.6   0.70   0.8   0.90   1.0
                                                 Wp           Ws
                Figura 5.4: Parametri di progetto di un filtro passa-basso.

     4. il ripple in banda attenuata, specificato tramite il valore massimo Rs del modulo
        della risposta in frequenza del filtro in banda attenuata.
5.4 L’uso di MATLAB per il progetto dei filtri                                                 85


Progetto di filtri IIR in MATLAB. Il programma MATLAB fornisce varie proce-
dure per il progetto di filtri IIR (q > 0 nella (5.5)). Considereremo in particolare il
caso dei filtri ellittici, i quali forniscono una approssimazione uniforme della risposta
in frequenza sia in banda passante che in banda oscura. Si può dimostrare che i filtri
ellittici sono ottimi, nel senso che, fissati i valori Wp , Rp e Rs , la banda di transizione
Ws − Wp è la minima possibile per un dato grado q del denominatore del filtro (q viene
detto l’ordine del filtro).
     Il progetto dei filtri ellittici passa-basso in MATLAB viene effettuato utilizzando
le due procedure ellipord e ellip del Signal Processing Toolbox. La sintassi di
ellipord è la seguente:
[N, Wn] = ellipord(Wp, Ws, RpdB, RsdB).
In ingresso alla funzione vanno specificate le frequenze Wp e Ws (vedi Fig. 5.4), nor-
malizzate rispetto a Fs /2. Inoltre, occorre specificare i valori di Rp e Rs , in dB. L’uscita
della funzione fornisce il valore N dell’ordine q del filtro che soddisfa le specifiche, e il
valore della frequenza naturale Wn da usare per l’effettivo progetto del filtro, effettuato
con la procedura
[b,a] = ellip(N, RpdB, RsdB, Wn).
Nei vettori b ed a, si trovano i coefficienti del numeratore e denominatore della risposta
in frequenza razionale (5.5) che soddisfa le specifiche. Si noti che i valori nel vettore
b includono la moltiplicazione per il quanto temporale T . Il metodo di progetto con
filtri ellittici non permette di specificare la caratteristica di fase del filtro.
Esempio 4. Supponiamo che la frequenza di campionamento del sistema numerico sia Fs = 8
kHz, e si voglia progettare un filtro passa-basso con banda passante da 0 a 1.6 kHz e banda
oscura da 2.4 kHz a 4 kHz=Fs /2. Si supponga di imporre Rp = 0.95 e Rs = 0.05. Il progetto
e la visualizzazione della risposta in frequenza del filtro, mostrata nelle figure 5.5 e 5.6, viene
effettuata con il seguente programma MATLAB.
% Parametri di progetto

Fs=8000;
RpdB=-20*log10(0.95);
RsdB=-20*log10(0.05);
Wp=1600/Fs*2;
Ws=2400/Fs*2;

% Progetto del filtro

[N,Wn]=ellipord(Wp, Ws, RpdB, RsdB);
[b,a]=ellip(N, RpdB, RsdB, Wn);

% Visualizzazione del filtro

[H,f]=freqz(b,a,512,Fs);
plot(f,abs(H));
plot(f,angle(H));

Si noti dalla Fig. 5.5 che il filtro soddisfa effettivamente le specifiche. Nella Fig. 5.6, si
noti la discontinuità di π attorno alla frequenza 2.5 kHz, dovuta al cambiamento di segno di
86                                                                                   Filtri numerici


H(f ) (corrispondente al punto angoloso nell’andamento del modulo). La fase è rappresentata
modulo 2π. L’ordine del filtro è risultato q = 3, e quindi i vettori b e a hanno dimensione 4.
Il filtro può essere utilizzato per l’elaborazione dell’ingresso posto nel vettore x mediante il
comando filter(b,a,x).                                                                       2

                         1

                        0.9

                        0.8

                        0.7

                        0.6

                        0.5

                        0.4

                        0.3

                        0.2

                        0.1

                         0
                          0   500   1000   1500   2000   2500   3000   3500   4000



      Figura 5.5: Modulo della risposta in frequenza del filtro ellittico (f in Hz).


                         4


                         3


                         2


                         1


                         0


                        −1


                        −2


                        −3


                        −4
                          0   500   1000   1500   2000   2500   3000   3500   4000



  Figura 5.6: Fase (radianti) della risposta in frequenza del filtro ellittico (f in Hz)

   Le funzioni ellipord e ellip possono essere utilizzate per il progetto di filtri
passa-alto, passa-banda e elimina-banda. Si considerino in particolare i seguenti esempi
esplicativi.
Esempio 5. Progetto di un filtro passa-alto (Fs = 8 kHz) con banda oscura [0,1.5] kHz e
banda passante [2.5,4] kHz, Rp = 0.99 e Rs = 0.01.

% Parametri di progetto

Fs=8000;
RpdB=-20*log10(0.99);
RsdB=-20*log10(0.01);
Wp=2500/Fs*2;
Ws=1500/Fs*2;
5.4 L’uso di MATLAB per il progetto dei filtri                                               87



% Progetto del filtro

[N,Wn]=ellipord(Wp, Ws, RpdB, RsdB);
[b,a]=ellip(N, RpdB, RsdB, Wn, ’high’);


Si noti che Wp > Ws e l’uso del parametro ’high’ nella chiamata a ellip. L’ordine del filtro
è risultato q = 4.                                                                       2

Esempio 6. Progetto di un filtro passa-banda (Fs = 8 kHz) con banda oscura negli intervalli
[0,1] kHz e [3,4] kHz e banda passante [1.5,2.5] kHz, Rp = 0.95 e Rs = 0.01.

% Parametri di progetto

Fs=8000;
RpdB=-20*log10(0.95);
RsdB=-20*log10(0.01);
Wp=[1500/Fs*2, 2500/Fs*2];
Ws=[1000/Fs*2, 3000/Fs*2];

% Progetto del filtro

[N,Wn]=ellipord(Wp, Ws, RpdB, RsdB);
[b,a]=ellip(N, RpdB, RsdB, Wn);


Si noti che Wp e Ws sono dei vettori, con componenti le frequenze che delimitano la banda
passante e le bande oscure. L’ordine del filtro risulta pari a due volte il valore N ritornato da
ellipord. In questo caso, è risultato N=4 e q = 8.                                            2

Esempio 7. Progetto di un filtro stop-banda (Fs = 8 kHz) con banda oscura [1.5,2.5] kHz e
banda passante negli intervalli [0,1] kHz e [3,4] kHz, Rs = 0.95 e Rp = 0.01.

% Parametri di progetto

Fs=8000;
RpdB=-20*log10(0.95);
RsdB=-20*log10(0.01);
Ws=[1000/Fs*2, 3000/Fs*2];
Wp=[1500/Fs*2, 2500/Fs*2];

% Progetto del filtro

[N,Wn]=ellipord(Wp, Ws, RpdB, RsdB);
[b,a]=ellip(N, RpdB, RsdB, Wn, ’stop’);


Si noti che Wp e Ws sono dei vettori, con componenti le frequenze che delimitano le bande
passanti e la banda oscura. Si noti inoltre l’uso del parametro ’stop’ in ingresso alla pro-
cedura ellip. L’ordine del filtro risulta anche in questo caso pari a due volte il valore N
ritornato da ellipord. È risultato in questo esempio N=4 e q = 8.                        2
88                                                                                Filtri numerici


     Altre procedure per il progetto di filtri IIR disponibili in MATLAB sono butter,
cheby1, cheby2, besself, invfreqz. In particolare, invfreqz permette il progetto di
filtri di cui si specifica sia il modulo che la fase.
Progetto di filtri FIR in MATLAB. I filtri FIR hanno alcuni svantaggi rispetto
ai filtri IIR ma anche alcuni importanti vantaggi. In generale, l’ordine di un filtro FIR
(ovvero il parametro r nella (5.5)) risulta in generale molto più grande dell’ordine di un
filtro IIR che soddisfa le stesse specifiche. D’altro canto, la durata del transitorio di un
filtro FIR è finita e pari alla durata della risposta impulsiva del filtro. Inoltre, esistono
metodi di progetto efficienti che garantiscono che il filtro FIR abbia esattamente fase
lineare. Come è noto, questo garantisce che una sinusoide in ingresso al filtro subisce
in uscita un ritardo indipendente dalla frequenza. Se dunque la risposta in frequenza
del filtro ha l’espressione
                                    H(f ) = e−j2πf t0 H0 (f ),
dove H0 (f ) vale 1 nella banda passante, e 0 altrove3 e il segnale di ingresso ha un’esten-
sione spettrale contenuta nella banda passante, l’uscita ha trasformata di Fourier

                              Y (f ) = H(f )X(f ) = e−j2πf t0 X(f ).

Nel dominio del tempo, risulta y(t) = x(t − t0 ) e l’uscita è una versione non distorta
(secondo Heaviside) del segnale di ingresso.
    Un filtro FIR causale di durata N T a fase lineare (a tratti) soddisfa la condizione

                     h(nT ) = h((N − 1 − n)T ),          n = 0, ..., (N − 1)T.

La risposta impulsiva è dunque simmetrica, come evidenziato nelle Fig. 5.7a e 5.7b nel
caso di N pari e N dispari, rispettivamente. In questo caso, la risposta in frequenza
del filtro
                                       N
                                       X −1
                             H(f ) = T      h(nT )e−j2πf nT
                                               n=0

risulta, come è immediato verificare
                                                                                
                             µ           ¶    N −3
                                               X              µ     µ           ¶¶
                                               2
           T e−j2πf T N2−1 h N T − T + 2
          
                                                   h(nT ) cos 2πf T n −
                                                                          N −1     , N dispari,
          
                                   2                                       2
          
                                              n=0
H(f ) =                      N −2                                  
          
                                            µ       µ           ¶¶
          
                             X2
          
                      N −1                                 N −1
          
           T e−j2πf T 2 2        h(nT ) cos 2πf T n −              , N pari.
                                                             2
                              n=0


La risposta in frequenza è dunque uguale al prodotto di una funzione reale per un
fattore a fase lineare. Eventuali discontinuità di π nella fase possono presentarsi in
corrispondenza di cambi di segno della funzione reale (da cui la dizione fase lineare a
tratti). Per N dispari, è possibile progettare i coefficienti h(nT ) in modo che la funzione
reale sia circa uguale ad 1 in un certo intervallo di frequenze e 0 altrove, cosicchè un
ingresso con estensione spettrale contenuta nella banda passante si ritrova ritardato in
uscita di (N − 1)/2 campioni e praticamente non distorto.
     3
    Dovendo H(f ) essere periodica di periodo 1/T , questo può avvenire solamente se t0 è un multiplo
di T .
5.4 L’uso di MATLAB per il progetto dei filtri                                            89


    Se N è pari, (N −1)/2 non è un numero intero e l’uscita non può essere in nessun caso
una semplice versione ritardata dell’ingresso a tempo discreto. Tuttavia, se l’ingresso
è ottenuto per campionamento su Z(T ) di una forma d’onda continua xa (t), t ∈ R,
nell’ipotesi in cui l’estensione spettrale del segnale campionato sia contenuta nella
banda passante del filtro, l’uscita risulta pari a y(nT ) = xa (nT − T (N − 1)/2). Essa
si ottiene dunque per campionamento della versione del segnale a tempo continuo
ritardato di t0 = T (N − 1)/2.

Nota. Se N è pari risulta in ogni caso H(Fs /2) = 0, Fs = 1/T . Infatti, H(Fs /2)
risulta uguale all’area del segnale

                                          Fs
                             h(nT )e−j2π 2 nT = (−1)n h(nT )

che risulta nulla, data la simmetria di h(nT ) (vedi Fig. 5.7a).
    Non è dunque conveniente cercare di progettare un filtro FIR passa-alto a fase
lineare con un numero pari di campioni.




      h(nT )    a)                        h(nT )     b)




                                         nT                                   nT


      h(nT )    c)                        h(nT )     d)




                                         nT                                   nT



Figura 5.7: Andamenti della risposta impulsiva di filtri FIR simmetrici e antisimmetrici.


    Un’altra classe di filtri FIR la cui risposta in frequenza presenta un fattore a fase
lineare è quella dei filtri antisimmetrici, la cui risposta impulsiva verifica la condizione

                               h(nT ) = −h((N − 1 − n)T ).

Gli andamenti tipici sono mostrati nelle Fig. 5.7c e 5.7d per N pari e N dispari
rispettivamente.
90                                                                         Filtri numerici


  La risposta in frequenza risulta
                             N −3                             
                              X              µ     µ         ¶¶
         
                       N −1
                                 2
                                                         N −1
         
          −jT e−j2πf T 2 2        h(nT ) sin 2πf T n −         , N dispari,
         
                                                          2
         
                              n=0
 H(f ) =                      N −2                             
         
                                             µ     µ         ¶¶
         
                              X 2
         
                       N −1                             N −1
         
          −jT e−j2πf T 2 2        h(nT ) sin 2πf T n −         , N pari.
                                                          2
                               n=0

    La risposta in frequenza risulta dunque il prodotto di un fattore a fase lineare e di
una funzione puramente immaginaria. In particolare, il fattore −j contribuisce ad una
fase costante di −π/2.
     Nota. Data l’antisimmetria, l’area della risposta impulsiva è nulla e risulta dunque
H(0) = 0. Non è dunque conveniente progettare un filtro passa-basso utilizzando filtri
FIR antisimmetrici.
     Per N dispari, risulta anche H(Fs /2) = 0, per cui il progetto di filtri passa-alto non
è consigliabile in questo caso.
     Il progetto di filtri FIR simmetrici in MATLAB si effettua utilizzando la procedura
                                    b = remez(r, f, M, w).
Il filtro fornito dall’algoritmo di Remez, particolarizzato da Parks e McClellan al proget-
to di filtri FIR, è ottimo nel senso che minimizza il massimo errore di approssimazione
nelle varie bande a parità di specifiche. La risposta in frequenza presenta una oscil-
lazione uniforme nelle varie bande (ed è dunque, come si dice, di tipo equiripple). I
parametri di ingresso alla procedura sono
     1. l’ordine r del filtro, la cui risposta impulsiva risulta pertanto di lunghezza N =
        r + 1 campioni;
     2. un vettore di frequenze f, normalizzate rispetto a F2 /2, Fs = 1/T , che specifica le
        frequenze che delimitano le bande attenuate e oscure della risposta in frequenza;
     3. un vettore M che specifica le ampiezze desiderate alle frequenze specificate nel
        vettore f;
     4. un vettore di pesi w che specifica il rapporto fra le ampiezze degli errori di ap-
        prossimazione nelle varie bande. Se il filtro non è soddisfacente in termini di
        errore assoluto, occorre aumentare l’ordine del filtro.
    Il vettore b di r+1 elementi contiene i coefficienti del filtro, che includono la molti-
plicazione per il quanto temporale T . Il filtro può essere utilizzato per l’elaborazione
dell’ingresso posto nel vettore x mediante il comando filter(b,1,x).
Esempio 8. Supponiamo che la frequenza di campionamento del sistema numerico sia Fs = 8
kHz, e si voglia progettare un filtro FIR simmetrico passa-basso di ordine r = 18 con banda
passante da 0 a 1.6 kHz e banda oscura da 2.4 kHz a 4 kHz=Fs /2. Detto δp il massimo
errore nel modulo della risposta in frequenza in banda passante e δs il massimo errore in
banda oscura, si desidera che δp /δs = 2, ovvero si tollera un errore doppio in banda passante
rispetto alla banda oscura.
    Il progetto e la visualizzazione del filtro possono essere ottenuti con i seguenti comandi
MATLAB.
5.4 L’uso di MATLAB per il progetto dei filtri                                           91


% Specifiche di progetto.

Fs=8000;
f=[0, 1600, 2400 4000]*2/Fs;
M=[1, 1,    0,   0];
w=[1, 2];
r=18;

% Progetto del filtro

b=remez(r,f,M,w);

% Visualizzazione del filtro

[H,f]=freqz(b,1,512,Fs);
figure;
plot(f,abs(H));
figure;
plot(f,angle(H));

Il modulo e la fase della risposta in frequenza del filtro ottenuto sono mostrati nelle Fig.
5.8 e 5.9. Si noti che la fase è rappresentata modulo 2π e che si hanno discontinuità di π
in banda attenuata, corrispondenti a cambi di segno della risposta in frequenza. Una stima
approssimata della lunghezza del filtro FIR con banda di transizione ν = Ws − Wp (espressa
in termini di frequenze normalizzate rispetto a Fs ) e con massimi errori δp e δs in banda
passante e banda oscura, può essere ottenuta dalla relazione empirica [4],[5]
                                     −10 log10 (δp δs ) − 15
                                 N'                          + 1.
                                             14ν
Si può altrimenti usare la procedura MATLAB remezord.

                        1.2



                         1



                        0.8



                        0.6



                        0.4



                        0.2



                         0
                          0    500   1000   1500   2000   2500   3000   3500   4000



 Figura 5.8: Modulo della risposta in frequenza del filtro FIR simmetrico (f in Hz).

                                                                                          2
Esempio 9. Progetto di un filtro passa-alto con r + 1 = 19 coefficienti (Fs = 8 kHz) con
banda oscura [0,1.5] kHz e banda passante [2.5,4] kHz, con un errore massimo in banda
passante uguale a quello in banda oscura.
92                                                                                   Filtri numerici

                         4


                         3


                         2


                         1


                         0


                        −1


                        −2


                        −3


                        −4
                          0   500   1000   1500   2000   2500   3000   3500   4000



Figura 5.9: Fase (radianti) della risposta in frequenza del filtro FIR simmetrico (f in
Hz).

% Specifiche di progetto.

Fs=8000;
f=[0, 1500, 2500, 4000]*2/Fs;
M=[0, 0,    1,   1];
w=[1, 1];
r=18;

% Progetto del filtro

b=remez(r,f,M,w);

                                                                                                  2

Esempio 10. Progetto di un filtro multi banda con r + 1 = 52 (Fs = 8 kHz) con bande
passanti [0,1] kHz, [2,3] kHz e bande oscure [1.2,1.8] kHz, [3.2,4] kHz. Nella banda [0,1] kHz si
tollera un errore pari a 1/2 di quello nelle bande [2,3] kHz e [3.2,4] kHz. Nella banda [1.2,1.8]
kHz si tollera un errore pari a 1/3 di quello nelle bande [2,3] kHz e [3.2,4] kHz.

% Specifiche di progetto.

Fs=8000;
f=[0, 1000, 1200, 1800, 2000, 3000, 3200, 4000]*2/Fs;
M=[1, 1,    0,    0,    1,    1,    0,    0];
w=[2,       3,          1,          1];
r=51;

% Progetto del filtro

b=remez(r,f,M,w);

                                                                                                  2
   Il progetto di filtri antisimmetrici in MATLAB si effettua ancora con la procedura
remez, usando il parametro ’Hilbert’. Si considerino i seguenti esempi.
5.4 L’uso di MATLAB per il progetto dei filtri                                               93


Esempio 11. Progetto di un filtro passa-alto anti-simmetrico con r + 1 = 18 coefficienti
(Fs = 8 kHz) con banda oscura [0,1.5] kHz e banda passante [2.5,4] kHz, con un errore
massimo in banda passante uguale a quello in banda oscura. È opportuno scegliere una
lunghezza pari del filtro, trattandosi di un filtro passa-alto antisimmetrico.
% Specifiche di progetto.

Fs=8000;
f=[0, 1500, 2500, 4000]*2/Fs;
M=[0, 0,    1,   1];
w=[1, 1];
r=17;

% Progetto del filtro

b=remez(r,f,M,w,’Hilbert’);


                                                                                              2
Esempio 12. L’uso della parola ’Hilbert’ deriva dal fatto che la fase costante −π/2 dovuta
alla presenza del fattore −j nella risposta in frequenza rende i filtri antisimmetrici adatti al
progetto di filtri di Hilbert discreti, con risposta in frequenza di modulo unitario a tutte le
frequenze e fase −π/2 per 0 < f < Fs /2. Per il progetto di un filtro di Hilbert di ordine 30
si possono utilizzare i seguenti comandi
Fs=8000;
r=30;

b=remez(r,[.1 0.9],[1 1],’Hilbert’)
Il filtro che si ottiene, a parte l’introduzione di un ritardo di 15 campioni, realizza ap-
prossimativamente la risposta in frequenza desiderata, come si può vedere con i seguenti
comandi
N=r+1;
[H,f]=freqz(b,1,512,Fs);
figure;
plot(f,abs(H));

% Disegna la fase, compensando il fattore corrispondente al ritardo
% dell’uscita.

figure;
plot(f,angle(H.*exp(j*2*pi*f/Fs*(N-1)/2)));
                                                                                              2

                                           Esercizi
   1. Progettare un filtro passa-basso IIR ellittico che soddisfa le seguenti specifiche
      (Fs =2 Hz): Rp = 0.98, Rs = 0.05, Wp = 0.6 Hz, Ws = 0.8 Hz. Si scriva una
      procedura per il calcolo dell’uscita e la si testi con gli ingressi x(t) = δZ(T ) (t), t ∈
      Z(T ) e x(t) = cos(2π0.4t)10 (t), t ∈ Z(T ). Si confrontino i propri risultati con
      quelli ottenuti usando la procedura filter.
94                                                                             Filtri numerici


     2. Progettare un filtro passa-basso FIR a fase lineare che soddisfa le seguenti speci-
        fiche (Fs =2 Hz): Rp = 0.98, Rs = 0.05, Wp = 0.6 Hz, Ws = 0.8 Hz. Si provi-
        no vari ordini del filtro finché le specifiche non sono soddisfatte esattamente.
        Si scriva una procedura per il calcolo dell’uscita e la si testi con gli ingressi
        x(t) = δZ(T ) (t), t ∈ Z(T ) e x(t) = cos(2π0.4t)10 (t), t ∈ Z(T ). Si confrontino i
        propri risultati con quelli ottenuti usando la procedura filter.

     3. Progettare un filtro passa-basso IIR ellittico che soddisfa le seguenti specifiche
        (Fs = 1/T = 8 kHz): Rp = 0.95, Rs = 0.02, Wp = 1.84 kHz, Ws = 2.48 kHz.
        Dopo avere calcolato i poli della funzione di trasferimento con la procedura roots,
        si stimi la durata convenzionale della risposta impulsiva all’1%. Si consideri
        l’ingresso x(nT ) = 2 sin(2πf0 nT ) + cos(2πf1 nT ), con f0 = 1 kHz e f1 = 3.2 kHz
        e si valuti la risposta a regime permanente del filtro. Si confronti l’uscita con il
        segnale x1 (nT ) = 2 sin(2πf0 nT ).

     4. Importanza della fase lineare. Progettare un filtro passa-basso IIR ellittico che
        soddisfa le seguenti specifiche (Fs = 1/T = 8 kHz): Rp = 0.95, Rs = 0.02,
        Wp = 2.4 kHz, Ws = 2.8 kHz. Si consideri l’ingresso x(nT ) = 2 sin(2πf0 nT ) +
        cos(2πf1 nT ), con f0 = 2.35 kHz e f1 = 1.5 kHz e si valuti la risposta a regime
        permanente del filtro. Si progetti un filtro FIR simmetrico che soddisfa alle stesse
        specifiche. Dopo avere confrontato l’ordine dei due filtri, si consideri l’uscita in
        regime permanente all’ingresso x(nT ). Si confrontino fra loro le uscite ottenute
        dai due filtri e l’ingresso x(nT ).

     5. Notch filter. Si consideri un filtro con funzione di trasferimento
                           1 − 2 cos(2πf0 T )z −1 + z −2            1 + 2ρ cos(2πf0 T ) + ρ2
            Hz (z) = C                                     ,   C=                            .
                         1 − 2ρ cos(2πf0 T )z −1 + ρ2 z −2             2 + 2 cos(2πf0 T )
        Si valutino in forma chiusa i poli e gli zeri della funzione di trasferimento. e si
        disegni il modulo e la fase della risposta in frequenza al variare di 0 < ρ < 1 e
        0 < f0 < Fs /2 con Fs = 1/T . In particolare, si valuti la frequenza in cui H(f )
        si annulla, e si considerino valori di ρ prossimi a 1. Sia Fs = 8 kHz. Si progetti
        un filtro che elimini un eventuale tono sinusoidale a 50 Hz sovrapposto al segnale
        utile. Tale disturbo potrebbe essere generato da interferenze con la tensione di
        rete.

     6. Nel file

         frase_8192.mat

        sono contenuti i campioni di segnale vocale relativi alla frase “E soprattutto,
        forse, ciò che gli occhi da soli non avrebbero potuto vedere.” La frequenza di
        campionamento è Fs = 8192 Hz. Il file può essere caricato con il comando load
        ed i campioni vengono posti nel vettore orig.
        Il segnale vocale è costituito da una successione di suoni elementari detti fonemi:
        ad esempio alla parola “fonemi” corrisponde la successione dei suoni elementari
        /f/ /o/ /n/ /e/ /m/ /i/. Inoltre le vocali (e in generale anche le consonanti
        vocalizzate, tipo “l”, “m”) hanno tipicamente un andamento quasi periodico.
        Questo contrasta con l’andamento irregolare e rumoroso delle fricative, tipo la
5.4 L’uso di MATLAB per il progetto dei filtri                                          95


     “s” o la “f”. Infine, le plosive, tipo la “p” o la “b”, sono precedute da una pausa
     prima dell’emissione del suono. Nella frase che stiamo esaminando, si possono
     osservare le caratteristiche dei vari segmenti del segnale con il comando plot. Se
     l’elaboratore è fornito di scheda audio, è possibile da MATLAB ascoltare la frase
     o una sua parte con il comando sound.
     Nel file
      frase_r330.mat
     è contenuta una versione della frase corrotta “in fase di registrazione” aggiungen-
     do al segnale un fastidioso tono a 330 Hz. Progettare un filtro notch che elimini
     tale disturbo.
  7. Con riferimento all’esercizio precedente, nel file
      frase_r.mat
     è contenuta una versione della frase corrotta in fase di registrazione con un tono
     di frequenza non nota. Usando una tecnica di stima spettrale (ad esempio, il
     periodogramma), si stimi la frequenza della sinusoide sovrapposta al segnale e la
     si elimini con un filtro notch. Nota: il filtro notch è molto selettivo, ed è quindi
     importante determinare accuratamente la frequenza della sinusoide per poterla
     cancellare efficacemente.
  8. Per ragioni tecniche, si vuole convertire la frequenza di campionamento del seg-
     nale vocale dell’esercizio 6 da 8192 Hz alla frequenza doppia 16384 Hz. Si real-
     izzi il convertitore di frequenza mediante interpolazione seguita da oppourtuno
     filtraggio.
  9. Il segnale telefonico viene usualmente campionato a Fs = 8 kHz, ma la sua esten-
     sione spettrale può essere limitata senza perdita di intelligibilità a [-3.33, 3.33]
     kHz. Si progetti uno schema di interpolazione/campionamento per passare dalla
     frequenza Fs = =8 kHz alla frequenza Fs0 = 6.66 kHz. Occorre dunque interpolare
     il segnale di un fattore 5 e sottocampionare di un fattore 6 (usando un prefiltro).
     Il file
      frase_8000.mat
     contiene la frase dell’esercizio 6 acquisita con Fs =8 KHz.
                                      Bibliografia
 [1] A. Oppenheim, R. Schafer, “Digital Signal Processing”.
 [2] A. Peled, B. Liu, “Digital Signal Processing”.
 [3] G.C. Temes, S.K. Mitra, “Modern Filter Theory and Design”.
 [4] R. Crochiere, L. Rabiner, “Multirate Digital Signal Processing”.
 [5] L. Rabiner et al., “Some Comparisons between FIR and IIR Digital Filters”, Bell
     Systems Technical Journal, vol. 53, Feb. 1974.
 [6] M. Bellanger, “Digital Processing of Signals”.
96   Filtri numerici
Capitolo 6

Esercizi sulla FFT

In questa sezione vengono proposti alcuni semplici esercizi riguardanti l’uso della FFT
per il calcolo della trasformata di Fourier di segnali a tempo discreto e a tempo continuo.
    Si ricorda che se x(t), t ∈ Z(T )/Z(N T ) è un segnale a tempo discreto di periodo
N T , la sua trasformata di Fourier ha l’espressione
                                   N
                                   X −1
                                                        nk           1
                      X(kF ) = T          x(nT )e−j2π N ,     F =      .              (6.1)
                                   n=0
                                                                    NT

La trasformata di Fourier X(kF ) risulta essere definita su Z(F )/Z(N F ) ed è quindi
completamente specificata dagli N valori assunti sulla cella elementare f ∈ {0, ..., (N −
1)F }. Il segnale x(nT ) viene recuperato da X(kF ) mediante la formula di inversione
                                            N
                                            X −1
                                                              nk
                              x(nT ) = F           X(nT )ej2π N .                     (6.2)
                                            n=0

    L’algoritmo di FFT permette di calcolare, a partire dai valori {x(0), ...., x((N −
1)T )}, la sommatoria (6.1) in modo efficiente. In particolare, se N è una potenza di
2, la (6.1) viene calcolata in O(N log2 N ) operazioni, il che consente una riduzione
drastica rispetto al calcolo diretto che richiede O(N 2 ) operazioni.
    La procedura MATLAB X=fft(x,N) calcola mediante un algoritmo di FFT la
sommatoria
                                         N
                                         X −1
                                                            nk
                             X(k + 1) =       x(n + 1)e−j2π N
                                           n=0
a partire da un vettore di ingresso x. Il risultato viene posto nel vettore di uscita X, di
dimensione N , che non è vincolato a essere una potenza di 2. Se il vettore di ingresso
ha dimensione minore di N , esso viene esteso aggiungendo in coda valori nulli. Si noti
che l’algoritmo di MATLAB suppone T =1, e che occorre in generale premoltiplicare
l’ingresso per T , ponendo x(n + 1) = T x(nT ).
    Per l’antitrasformata, si può usare la procedura MATLAB x=ifft(X), che calcola
in modo efficiente la sommatoria
                                             N −1
                                       1 X                nk
                            x(k + 1) =       X(n + 1)ej2π N
                                       N n=0

a partire dal vettore X di dimensione N . Nel caso T 6= 1, occorre porre X(n + 1) =
X(nT )/T .

                                              97
98                                                                              Esercizi sulla FFT


    L’algoritmo di FFT può dunque essere utilizzato per il calcolo della trasformata di
Fourier di segnali a tempo discreto e periodici. Vedremo di seguito la possibilità di
utilizzarla per il calcolo della trasformata di segnali a tempo discreto non periodici e
di segnali continui.

    Segnali a tempo discreto. Se x(nT ), t ∈ Z(T ) è un segnale a tempo discreto, in
generale non periodico, con estensione contenuta in {0, ..., (N −1)T }, possiamo usare la
FFT per calcolare i campioni della sua trasformata di Fourier. Infatti, dalla definizione
di trasformata, si ottiene
                   +∞
                   X                              N
                                                  X −1
       X(f ) = T          x(kT )e−j2πf nT = T            x(nT )e−j2πf nT ,     f ∈ R/Z(1/T ).
                   n=−∞                           n=0

Se calcoliamo la relazione precedente per f = kF , dove F = 1/N T , otteniamo proprio
                                                N
                                                X −1
                                                                   nk
                               X(kF ) = T              x(nT )e−j2π N ,
                                                n=0

che ha la stessa struttura della (6.1). Dunque, N campioni in un periodo di X(f ),
X(kF ), k = 0, ..., (N − 1)F , possono essere calcolati usando la FFT. Si noti che pos-
siamo infittire i campioni in cui viene calcolata la trasformata X(f ) semplicemente
aumentando la dimensione da N a M > N : in tale caso, i campioni aggiuntivi
x(N T ), ..., x((M − 1)T ) da usare per il calcolo usando la (6.1) sono evidentemente
uguali a zero.
    Se il segnale x(nT ) ha durata finita D ≤ N T , ma la sua estensione non è contenuta
nella cella elementare {0, ..., (N − 1)T }, occorre osservare che ai fini del calcolo dei
campioni X(kF ), k = 0, ..., (N − 1)F , possiamo considerare la versione periodicizzata
del segnale di ingresso
                                  xp (nT ) = perN T x(nT ).
Infatti, se x(nT ) ha estensione contenuta in {n0 T, (n0 + 1)T, ..., (n0 + N − 1)T }, si ha
                            n0X
                              +N −1                              N
                                                                 X −1
                                                                                     nk
                                                −j2πnT kF
              X(kF ) = T              x(nT )e               =T          xp (nT )e−j2π N .
                              n=n0                               n=0

Nel calcolo dei campioni della trasformata tramite la (6.1) occorre dunque considerare
i valori nella cella {0, ..., (N − 1)T } del segnale periodicizzato.
    Infine, se il segnale x(nT ) ha durata praticamente limitata, è possibile considerarlo
nullo entro una precisione prefissata al di fuori di un certo intervallo I0 . Questo equivale
in effetti a moltiplicare il segnale di ingresso per una finestra che vale 1 per t ∈ I0 e
0 altrove. I valori calcolati dei campioni della trasformata saranno pertanto relativi
alla convoluzione tra la trasformata di Fourier del segnale di ingresso con quella della
finestra.

    Stima della trasformata per segnali a tempo continuo. Supponiamo di
avere un segnale a tempo continuo x(t), t ∈ R e di volere calcolare una stima della
sua trasformata di Fuorier X(f ), f ∈ R. Per potere utilizzare a tale scopo un algo-
ritmo numerico, e in particolare la FFT, occorre dapprima campionare il segnale di
ingresso, ponendo xc (t) = x(t), t ∈ Z(T ). La scelta di T deve essere fatta in modo
                                                                                              99


da limitare l’aliasing, e in generale deve essere Fc = 1/T > B, dove B è la larghezza
di banda del segnale. Una volta campionato, il segnale ha una trasformata di Fourier
periodica Xc (f ) = repFc X(f ), f ∈ R/Z(Fc ) i cui campioni in un periodo possono essere
stimati mediante un algoritmo di FFT, secondo quanto esposto relativamente ai seg-
nali a tempo discreto. Se non si conosce a priori la larghezza di banda B del segnale,
occorrerà procedere per tentativi, valutando se le stime che si ottengono variano entro
la precisione desiderata al variare di T .
     Se il segnale x(t) è reale, la sua trasformata di Fourier ha simmetria hermitiana ed
estensione spettrale simmetrica [−B/2, B/2]. L’algoritmo di FFT fornisce i campioni
della trasformata periodica Xc (f ) = repFc X(f ) relativamente al periodo [0, Fc ], mentre
il confronto con X(f ) è più significativo se si considera la cella elementare [−Fc /2, Fc /2].
Posto F = Fc /N , una volta calcolati i valori Xc (0), ..., Xc ((N − 1)F ) con un algoritmo
di FFT, converrà dunque riferirsi al vettore
  · µ         ¶     µµ           ¶ ¶                                        µµ        ¶ ¶¸
          N              N                                                     N
    Xc      F , Xc           + 1 F , ..., Xc ((N − 1) F ) , Xc (0), ..., Xc       −1 F         ,
          2               2                                                     2
per N pari, e a
· µ           ¶    µµ         ¶ ¶                                         µµ      ¶ ¶¸
     N +1             N +1                                                   N −1
 Xc         F , Xc         + 1 F , ..., Xc ((N − 1) F ) , Xc (0), ..., Xc          F   ,
        2               2                                                      2
per N dispari, che contengono la sequenza dei campioni relativi al periodo [−Fc /2, Fc /2].
Tale operazione di ordinamento degli elementi del vettore di uscita può ottenersi con
la funzione MATLAB fftshift.

                                            Esercizi

   1. Si consideri il segnale x(t), t ∈ Z(T ), T = 2, con x(0) = 1, x(±T ) = 2, x(±2T ) =
      3 e x(nT ) = 0 altrove. Si calcoli in forma chiusa la trasformata di Fourier
      X(f ), f ∈ R/Z(1/T ). Si calcolino inoltre N campioni della trasformata in un
      periodo usando un algoritmo di FFT, per N = 8, 16, 256, e si verifichi in un
      grafico la coincidenza fra i campioni calcolati e l’espressione teorica.
      Si valuti inoltre approssimativamente il numero di operazioni richieste per il cal-
      colo degli N campioni della trasformata usando la FFT ed il calcolo diretto. Si
      tenga presente che il segnale di ingresso ha solamente 5 campioni diversi da zero.
      Nota: X(f ) è in generale una funzione complessa, ed occorre considerarne di
      volta in volta la parte reale e immaginaria, oppure il modulo e la fase.
   2. Si calcoli la DFT dei seguenti segnali, definiti su Z(T ), e si disegni il grafico del
      modulo, cercando di spiegarne le caratteristiche. Sia F = 1/T = 8 kHz.

        a. Trasformata su N = 512 punti. Segnale di ingresso
                                         x(nT ) = 1, 0 ≤ n ≤ 63
                                         0,          altrove.

        b. Trasformata su N = 256 punti. Segnale di ingresso
                                   µ      ¶          µ        ¶
                                     2πn               2πn
                  x(nT ) = 0.5 sin       9 + 0.7 sin       100 , 0 ≤ n ≤ 255.
                                     256               256
100                                                                    Esercizi sulla FFT


        c. Trasformata su N = 256 punti. Segnale di ingresso
                                 µ         ¶           µ         ¶
                                   2πn 100               2πn 200
                x(nT ) = 0.5 sin             + 0.7 sin             , 0 ≤ n ≤ 255.
                                   256 3                 256 3

  3. Una sinusoide di frequenza 50 Hz viene campionata con 500 campioni al secondo
     e analizzata usando una FFT su 64 campioni.

        a. Quale campione della trasformata sarà maggiore in modulo?
        b. Quale campione della trasformata avrà un’ampiezza immediatamente infe-
           riore a quella del campione di modulo maggiore, e qual’è l’ampiezza relativa
           dei due campioni (esprimere il risulatato in dB)?

      Si verifichino i risultati con MATLAB.

  4. Siano dati i seguenti segnali, definiti su Z(T ) per T = 1.
                       ¡        ¢
       a. x(nT ) = sin 2πn
                         256
                             172 ,
        b. x(nT ) = sin(n).

      Si analizzino i due segnali mediante FFT su 256 punti. Si preveda quale sarà
      il coefficiente della trasformata più grande in modulo nei due casi, e l’ampiezza
      relativa di tali campioni della trasformata. Si verifichi il risultato con MATLAB.

  5. Questo esercizio mostra come occorra fare attenzione nell’uso della FFT per il
     calcolo della trasformata di Fourier di segnali sinusoidali. Si consideri il segnale
     x(t) = cos 2πf0 t, t ∈ Z(T ), T = 1 f0 = 0.25 e si costruisca il vettore MATLAB

                              x(n + 1) = x(nT ),   n = 0, ..., N − 1

      per N = 32 e N = 64. Si calcoli poi la FFT di x nei due casi su N punti e la
      si disegni usando la funzione stem. Si discuta il risultato ottenuto. Si ripeta lo
      stesso esperimento per f0 = 0.254 e si discuta il risultato ottenuto. Si risolva
      inoltre l’esercizio per via analitica e si confronti con la soluzione trovata per via
      numerica.
      Nota: per f0 = 0.25 e i due valori di N considerati, x(t) è periodico di periodo
      N T . Per f0 = 0.254, x(t) non è periodico di periodo N T .

  6. Si scriva una procedura analoga alla procedura MATLAB freqz, usando la FFT.

  7. Dati i segnali x(nT ) con estensione 0, ..., (N −1)T e h(nT ) con estensione 0, ..., (M −
     1)T , si scriva una procedura MATLAB che calcola la convoluzione y(nT ) =
     h ∗ x(nT ) mediante l’uso della FFT. Si confronti il risultato con quello forni-
     to dalla funzione MATLAB y=T*conv(h,x), in cui si pone x(n + 1) = x(nT ),
     nT = 0, ..., (N − 1)T , e h(n + 1) = h(nT ), nT = 0, ..., (M − 1)T . Si scriva
     un programma che calcola la convoluzione di due segnali generici con estensioni
     −5T, ..., 4T e 3T, ..., 5T .
      Soluzione proposta per la prima parte:
                                                                                      101


    function y=convv(T,x,h);

    N=length(x); M=length(h);

    L=N+M-1;

    X=T*fft(x,L); H=T*fft(h,L);

    Y=X.*H;

    y=ifft(Y)/T;

    % Se x e h sono reali, y e‘ reale. Si pu\‘o eliminare
    % l’eventuale parte immaginaria, non identicamente nulla a causa
    % degli errori di calcolo.

    if (isreal(x) & isreal(h)) y=real(y);

    end;

 8. Metodo Overlap-Add. Con riferimento all’esercizio precedente, se il segnale x(t), t ∈
    Z(T ) ha una durata N T molto più grande di quella M T di h(t), non è efficiente
    calcolare direttamente la convoluzione usando la FFT, che deve essere valuta-
    ta per entrambi i segnali su almeno M + N − 1 punti. È conveniente allora
    suddividere il segnale di ingresso in blocchi non sovrapposti lunghi L,
                                 ½
                                    x(nT ), n = iL, ..., iL + L − 1,
                      xi (nT ) =
                                    0,       altrove

    ponendo                                    X
                                    x(nT ) =        xi (nT ).
                                                i

    Il risultato della convoluzione viene ottenuto sommando le uscite xi ∗ h(nT ),
    ciascuna delle quali può essere calcolata usando la FFT. Si noti che le uscite
    xi ∗ h(nT ) risultano sovrapposte di M − 1 campioni.
    Si scriva un programma MATLAB che calcola la convoluzione di due segnali con
    il metodo Overlap-Add, ponendo M = 4 e N = 64, e si confronti il risultato con
    il metodo diretto e quello dell’esercizio 7.

 9. Dati due segnali x1 (t) e x2 (t), t ∈ Z(T ) a durata limitata LT , è possibile
    considerarne le ripetizioni periodiche x1,p (t) = repLT x1 (t), t ∈ Z(T )/Z(LT ) e
    x2,p (t) = repLT x2 (t), t ∈ Z(T )/Z(LT ), senza perdita di informazione. Dimostrare
    e verificare su un esempio sviluppato con MATLAB che la convoluzione ciclica
    yp (nT ) = x1,p ∗ x2,p (nT ) è uguale alla ripetizione periodica della convoluzione
    y(nT ) = x1 ∗ x2 (nT ), ovvero yp (nT ) = repLT y(nT ).

10. Metodo Overlap-Save. Si considerino, come nell’Esercizio 8, due segnali x(t), t ∈
    Z(T ) e h(t) con estensione [0, ..., (N − 1)T ] e [0, ..., (M − 1)T ], rispettivamente,
    e N À M . Nel metodo Overlap-Save per il calcolo della convoluzione, il segnale
102                                                                       Esercizi sulla FFT


      x(nT ) viene suddiviso in blocchi xk (nT ) lunghi L campioni. Il metodo consiste
      nel calcolare una convoluzione ciclica (vedi Esercizio 9) tra h(nT ) e xk (nT ),
      identificando quella parte della convoluzione ciclica che corrisponde alla normale
      convoluzione. In particolare, supponendo L ≥ M , nella convoluzione ciclica
      di h(nT ) e xk (nT ) calcolata su L punti, risulta che i primi M − 1 non sono
      corretti, mentre i rimanenti punti sono gli stessi che otterremmo dalla normale
      convoluzione (perchè? Vedi l’Esercizio 9). Conviene dunque sezionare x(nT ) in
      segmenti di lunghezza L in modo che ogni segmento si sovrapponga al precedente
      per M − 1 punti.
      Dopo avere definito i segmenti xk (nT ) nel modo seguente

                      xk (nT ) = x((n + k(L − M + 1))T ), 0 ≤ n ≤ L − 1,

      si calcola pertanto la convoluzione ciclica yk (nT ) = h ∗ xk (nT ) su L punti e se ne
      scartano i primi M − 1. I rimanenti punti di ogni sottosequenza yk (nT ) vengono
      giustapposti gli uni di seguito agli altri, fino ad ottenere l’uscita filtrata finale.
      Si scriva un programma MATLAB che calcola la convoluzione di due segnali con
      il metodo Overlap-Save, ponendo M = 4 e N = 64, e si confronti il risultato con
      il metodo diretto e quello dell’Esercizio 7.

 11. Si stimi la trasformata di Fourier del segnale a tempo continuo

                                       x(t) = e−|6t| , t ∈ R.

 12. Si stimi la trasformata di Fourier del segnale a tempo continuo

                                     x(t) = e−|6(t−1)| ,   t ∈ R.

 13. Si stimi la trasformata di Fourier del segnale a tempo continuo

                                x(t) = e−|6t| cos(2π0.5t),     t ∈ R.

 14. Si stimi la trasformata di Fourier del segnale a tempo continuo

               sin(π(1 − r)t/T ) + 4r(t/T ) cos(π(1 + r)t/T )       t
      x(t) =                                                  rect    ,     r = 0.125,   t ∈ R.
                            π[1 − (4rt/T )2 ]t/T                   8T
Bibliografia

[1] N. Benvenuto and G. Cherubini, “Algorithms for communications systems and
    their application”, London: John Wiley & Sons, 2002.

[2] L.W. Couch II, “Digital and analog communication systems ”, Upper Saddle River,
    NJ: Prentice-Hall, 1997.

[3] M.S. Roden, “Analog and digital communication systems ”, Upper Saddle River,
    NJ: Prentice-Hall, 1996.

[4] J.G. Proakis and M. Salehi, “Communication systems engineering”, Englehood
    Cliffs, NJ: Prentice-Hall, 1994.




                                       103
