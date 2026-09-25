---
fonte: "FEA&D SPIEGAZIONI.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

MOS

Metallo (detto Gate) (M)
Ossido (O)
Substrato (semiconduttore in silicio detto Bulk) (S)

Il campo elettrico nell’ossido è costante

Il potenziale nel substrato decresce a ritmo esponenziale dopo l’interfaccia O-S

Anche le concentrazioni di cariche cambiano:

    -    Le cariche mobili (𝜌𝜌𝑖𝑖𝑖𝑖𝑖𝑖 = −qn) decrescono allontanandosi dall’interfaccia e dipendono positivamente
         dal potenziale
    -    Le cariche ﬁsse (𝜌𝜌𝑑𝑑 = 𝑞𝑞(𝑝𝑝 – 𝑁𝑁𝐴𝐴− )) crescono allontanandosi dall’interfaccia e dipendono negativamente
         dal potenziale. Queste cariche, in regione di svuotamento, sono in numero ﬁsso e sono pari al valore di
         drogaggio (𝑁𝑁𝐴𝐴 )


CALCOLO 𝑸𝑸𝑫𝑫 :

La considerazione in regione di svuotamento (𝑉𝑉𝐺𝐺 > 𝑉𝑉𝐹𝐹𝐹𝐹 ) è che le cariche ﬁsse siano in numero molto maggiore
rispetto a quelle mobili (𝑄𝑄𝐷𝐷 >> 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 ) e che quindi queste ultime possano essere omesse dal calcolo di 𝑄𝑄𝐷𝐷
(quantità di carica ﬁssa per unità d’area). Per questo calcolo si ipotizza anche che il valore di 𝜌𝜌𝑑𝑑 sia nullo dopo la
regione di svuotamento di dimensione 𝑊𝑊𝐷𝐷 :

                                                      𝑄𝑄𝐷𝐷 = −𝑞𝑞𝑁𝑁𝐴𝐴 𝑊𝑊𝐷𝐷

Concentrazione di carica costante  campo elettrico lineare (in questo caso decrescente)  potenziale
quadratico

Tramite l’equazione del potenziale in zona di svuotamento (𝜓𝜓(𝑧𝑧)), si determina l’equazione relativa al potenziale
all’interfaccia O-S ponendo 𝑧𝑧 = 𝑊𝑊𝐷𝐷 ed ottenendo:

                                                        ψ(WD ) = ψs

Si trova quindi l’equazione relativa alla dimensione della zona di svuotamento (𝑊𝑊𝐷𝐷 ).
Da qui si riprende l’equazione deﬁnita per 𝑄𝑄𝐷𝐷 e si sostituisce dentro quella di 𝑊𝑊𝐷𝐷 :

                                                   𝑄𝑄𝐷𝐷 = −�2𝑞𝑞𝑁𝑁𝐴𝐴 𝜓𝜓𝑠𝑠 𝜀𝜀𝑆𝑆𝑆𝑆


CALCOLO 𝝍𝝍𝒔𝒔 :

Se 𝑉𝑉𝐺𝐺 >> 𝑉𝑉𝐹𝐹𝐹𝐹 allora si ha che la concentrazione di 𝜌𝜌𝑖𝑖𝑖𝑖𝑖𝑖 è molto alta e NON VALE più la considerazione fatta in
precedenza 𝑄𝑄𝐷𝐷 >> 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 .
Si ha quindi 𝑄𝑄𝐷𝐷 ≈ 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 e si dice che il substrato è in inversione.
Il passaggio da svuotamento (𝑄𝑄𝐷𝐷 >> 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 ) ad inversione (𝑄𝑄𝐷𝐷 ≈ 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 ) si ha quando:

                                                     𝑛𝑛(𝜓𝜓𝑠𝑠 ) = 𝑛𝑛𝑠𝑠 = 𝑁𝑁𝐴𝐴

Da questa si ottiene il valore di 𝜓𝜓𝑠𝑠 tramite l’equazione della distribuzione di 𝑛𝑛(𝜓𝜓):

                                                                 𝑛𝑛𝑖𝑖2 𝑉𝑉𝜓𝜓𝑠𝑠
                                                        𝑛𝑛𝑠𝑠 =        𝑒𝑒 𝑡𝑡ℎ
                                                                 𝑁𝑁𝐴𝐴

                                                                           𝑁𝑁𝐴𝐴
                                                    𝜓𝜓𝑠𝑠 = 2𝑉𝑉𝑡𝑡ℎ ln �          �
                                                                           𝑛𝑛𝑖𝑖
CALCOLO 𝑽𝑽𝑻𝑻 :

La carica totale del substrato è pari a

                                                     𝑄𝑄𝑆𝑆 = −𝐶𝐶𝑂𝑂𝑂𝑂 (𝑉𝑉𝐺𝐺 − 𝑉𝑉𝐹𝐹𝐹𝐹 − 𝜓𝜓𝑠𝑠 )

                                                                           𝜀𝜀𝑂𝑂𝑂𝑂
                                                                𝐶𝐶𝑂𝑂𝑂𝑂 =
                                                                           𝑇𝑇𝑂𝑂𝑂𝑂

Ricordando che 𝜓𝜓𝑠𝑠 dipende da 𝑉𝑉𝐺𝐺 poiché è proprio quest’ultima che fa variare la concentrazione di 𝑛𝑛 (e quindi di
𝜌𝜌𝑖𝑖𝑖𝑖𝑖𝑖 ) deﬁnendo in che zona si sta lavorando (∗).

Essendo che la decrescita di 𝜌𝜌𝑖𝑖𝑖𝑖𝑖𝑖 è esponenziale man mano che ci si allontana dall’interfaccia O-S, si può
ipotizzare 𝑄𝑄𝐷𝐷 >> 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 (come se si fosse in regione di svuotamento).
Di conseguenza si ha che la carica totale nel substrato (𝑄𝑄𝑆𝑆 ) è circa pari alla carica ﬁssa (𝑄𝑄𝐷𝐷 ).

Si deﬁnisce il fattore

                                                                     �2𝜀𝜀𝑆𝑆𝑆𝑆 𝑞𝑞𝑁𝑁𝐴𝐴
                                                              𝛾𝛾 =
                                                                       𝐶𝐶𝑂𝑂𝑂𝑂

Dall’equazione di 𝑄𝑄𝑆𝑆 si ottiene la tensione di soglia

                                                     𝑉𝑉𝑇𝑇 = 𝑉𝑉𝐺𝐺 = 𝑉𝑉𝐹𝐹𝐹𝐹 + 𝜓𝜓𝑠𝑠 + 𝛾𝛾�𝜓𝜓𝑠𝑠



MOSFET

E’ un MOS con due terminali ai lati (Source (S) e Drain (D)) drogati in maniera opposta rispetto al substrato.

Il substrato prima detto S, viene detto Bulk (B).

Sono dette W la profondità del MOSFET ed L la lunghezza di canale (la minima distanza tra i terminali di S e D).

In condizioni tipiche VB = 0 e VSB = 0 e se 𝑉𝑉𝐷𝐷𝐷𝐷 > 0 :

     -    Con 𝑉𝑉𝐺𝐺𝐺𝐺 ≤ 𝑉𝑉𝐹𝐹𝐹𝐹  𝐼𝐼𝐷𝐷𝐷𝐷 = 0 ∀ 𝑉𝑉𝐷𝐷𝐷𝐷  MOSFET OFF

     -    Con 𝑉𝑉𝐹𝐹𝐹𝐹 < 𝑉𝑉𝐺𝐺𝐺𝐺 < 𝑉𝑉𝑇𝑇  zona svuotata su interfaccia O-B da S a D  𝐼𝐼𝐷𝐷𝐷𝐷 = 0 ∀ 𝑉𝑉𝐷𝐷𝐷𝐷  MOSFET OFF

     -    Con 𝑉𝑉𝐺𝐺𝐺𝐺 > 𝑉𝑉𝑇𝑇  B invertito all’interfaccia e strato di 𝑒𝑒 − liberi tra S e D  𝐼𝐼𝐷𝐷𝐷𝐷 = 𝑓𝑓(𝑉𝑉𝐷𝐷𝐷𝐷 )  MOSFET ON


EFFETTO VALVOLA:

𝐼𝐼𝐷𝐷𝐷𝐷 dipende da 𝑉𝑉𝐺𝐺𝐺𝐺 per la proposizione (∗).

Quindi con 𝑉𝑉𝐷𝐷𝐷𝐷 = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 e 𝑉𝑉𝐺𝐺𝐺𝐺 ↑  𝐼𝐼𝐷𝐷𝐷𝐷 ↑


EFFETTO BODY:

Deﬁnita la tensione tra G e B che manda in inversione il canale come

                                                        𝑉𝑉𝑇𝑇0 = 𝑉𝑉𝐹𝐹𝐹𝐹 + 𝜓𝜓𝑠𝑠 + 𝛾𝛾�𝜓𝜓𝑠𝑠
                                                                 𝜓𝜓𝑠𝑠 = 2𝜓𝜓𝐹𝐹
𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝐹𝐹𝐹𝐹 − 𝜓𝜓𝑠𝑠 rappresenta la caduta di tensione nell’ossido considerando un dispositivo MOS, ma se si è in
presenza di un MOSFET si ha 𝑉𝑉𝐺𝐺𝐺𝐺 = 𝑉𝑉𝐺𝐺𝐺𝐺 + 𝑉𝑉𝑆𝑆𝑆𝑆 (∗∗).

Di conseguenza si ha che per il MOSFET la caduta di tensione nell’ossido è 𝑉𝑉𝐺𝐺𝐺𝐺 + 𝑉𝑉𝑆𝑆𝑆𝑆 − 𝑉𝑉𝐹𝐹𝐹𝐹 − 𝜓𝜓𝑠𝑠 .

Si considera quindi la tensione riferita al S e si ha che 𝜓𝜓𝑠𝑠′ = 𝜓𝜓𝑠𝑠 + 𝑉𝑉𝑆𝑆𝑆𝑆 .

Dalle equazioni precedenti si ottiene che 𝑄𝑄𝐷𝐷 = −𝛾𝛾𝐶𝐶𝑂𝑂𝑂𝑂 �𝜓𝜓𝑠𝑠  𝑄𝑄𝐷𝐷 = −𝛾𝛾𝐶𝐶𝑂𝑂𝑂𝑂 �𝜓𝜓𝑠𝑠′

Quindi se 𝑉𝑉𝑆𝑆𝑆𝑆 ↑  𝜓𝜓𝑠𝑠′ ↑  𝑄𝑄𝐷𝐷 ↑.

Dalla deﬁnizione precedente si ottiene anche che 𝑊𝑊𝐷𝐷 = �(2𝜀𝜀𝑆𝑆𝑆𝑆 𝜓𝜓𝑠𝑠′ )⁄(𝑞𝑞𝑁𝑁𝐴𝐴 )

La tensione di soglia riferita a B è

                                                              𝑉𝑉𝐺𝐺𝐺𝐺 𝑇𝑇 = 𝑉𝑉𝐹𝐹𝐹𝐹 + 𝜓𝜓𝑠𝑠′ + 𝛾𝛾�𝜓𝜓𝑠𝑠′

Per la (∗∗) si ha quindi che

                                             𝑉𝑉𝐺𝐺𝐺𝐺𝑇𝑇 − 𝑉𝑉𝑆𝑆𝑆𝑆 = 𝑉𝑉𝐺𝐺𝑆𝑆𝑇𝑇 = 𝑉𝑉𝑇𝑇0 + 𝛾𝛾��𝜓𝜓𝑠𝑠′ − �𝜓𝜓𝑠𝑠 �

Dove 𝛾𝛾 viene detto fattore di effetto body (0,3 ÷ 0,5 √𝑉𝑉)


CARICA LIBERA DI CANALE:

In inversione (𝑉𝑉𝐺𝐺𝐺𝐺 > 𝑉𝑉𝑇𝑇 ) si considera la condizione 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 ≈ 𝑄𝑄𝐷𝐷 (all’interfaccia O-B) ed essendo che 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 è
                                                       𝜓𝜓𝑠𝑠
                                             𝑛𝑛𝑖𝑖2
dipendente da 𝜌𝜌𝑖𝑖𝑖𝑖𝑖𝑖 = −𝑞𝑞𝑞𝑞, ed 𝑛𝑛𝑠𝑠 =            𝑒𝑒 𝑉𝑉𝑡𝑡ℎ si ha che se 𝜓𝜓𝑠𝑠 ↑  𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 ↑↑.
                                             𝑁𝑁𝐴𝐴


Si arriva al punto per il quale 𝜓𝜓𝑠𝑠 non può variare più di tanto

                                                                    𝑄𝑄𝑆𝑆     𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 + 𝑄𝑄𝐷𝐷    𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼
                                   𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝐹𝐹𝐹𝐹 − 𝜓𝜓𝑠𝑠 = −             =−                 =−          + 𝛾𝛾�𝜓𝜓𝑠𝑠
                                                                   𝐶𝐶𝑂𝑂𝑂𝑂          𝐶𝐶𝑂𝑂𝑂𝑂        𝐶𝐶𝑂𝑂𝑂𝑂

Valutando 𝑉𝑉𝑆𝑆𝑆𝑆 = 0 si ha 𝑉𝑉𝐺𝐺𝐺𝐺 = 𝑉𝑉𝐺𝐺𝐺𝐺 + 𝑉𝑉𝑆𝑆𝑆𝑆 = 𝑉𝑉𝐺𝐺𝐺𝐺 e quindi

                                                                                      𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼           𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼
                                           𝑉𝑉𝐺𝐺𝐺𝐺 = 𝑉𝑉𝐹𝐹𝐹𝐹 + 𝜓𝜓𝑠𝑠 + 𝛾𝛾�𝜓𝜓𝑠𝑠 −                  = 𝑉𝑉𝑇𝑇0 −
                                                                                       𝐶𝐶𝑂𝑂𝑂𝑂             𝐶𝐶𝑂𝑂𝑂𝑂

Attraverso la quale si ottiene che

                                                              𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 = −𝐶𝐶𝑂𝑂𝑂𝑂 �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇0 �

Oppure, se 𝑉𝑉𝑆𝑆𝑆𝑆 > 0, si ha

                                                              𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 = −𝐶𝐶𝑂𝑂𝑂𝑂 (𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )


MODELLO DELLA CORRENTE:

Se 𝑉𝑉𝐺𝐺𝐺𝐺 < 𝑉𝑉𝑇𝑇  𝐼𝐼𝐷𝐷𝐷𝐷 = 0 e MOSFET OFF

Se 𝑉𝑉𝐺𝐺𝐺𝐺 ≥ 𝑉𝑉𝑇𝑇  𝐼𝐼𝐷𝐷𝐷𝐷 > 0 e MOSFET ON

Se, oltre alla condizione di 𝑉𝑉𝐺𝐺𝐺𝐺 ≥ 𝑉𝑉𝑇𝑇 si aggiunge il fatto di avere 𝑉𝑉𝐷𝐷𝐷𝐷 > 0 si ha che 𝜓𝜓𝑠𝑠 non è costante lungo tutta
l’interfaccia O-B, ma cambia e dipende da 𝑥𝑥 ∈ [0, 𝐿𝐿].
Si ha quindi 𝜓𝜓𝑠𝑠 = 𝜓𝜓𝑠𝑠′′ (𝑥𝑥) = 𝜓𝜓𝑠𝑠′ + 𝑉𝑉(𝑥𝑥) con 𝑉𝑉(𝑥𝑥 = 0) = 0 e 𝑉𝑉(𝑥𝑥 = 𝐿𝐿) = 𝑉𝑉𝐷𝐷𝐷𝐷 .

Supponendo che la quantità di carica 𝜌𝜌𝐷𝐷 non dipenda da 𝑉𝑉(𝑥𝑥) e che sia quindi 𝑄𝑄𝐷𝐷 ≈ −𝛾𝛾𝐶𝐶𝑂𝑂𝑂𝑂 �𝜓𝜓𝑠𝑠′ .

Seguendo i passaggi svolti per calcolare 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 , utilizzando però la deﬁnizione di 𝜓𝜓𝑠𝑠′′ , si ottiene

                                                     𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 = −𝐶𝐶𝑂𝑂𝑂𝑂 �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉(𝑥𝑥)� (∗∗∗)

Ricordando che 𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 è la densità di carica per unità d’area, si può esprimere la densità di corrente per unità
d’area come

                                                                          𝐼𝐼𝐷𝐷𝐷𝐷
                                                               𝐽𝐽𝐷𝐷𝐷𝐷 =          = −𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 (𝑥𝑥)𝑣𝑣(𝑥𝑥)
                                                                           𝑊𝑊
                                    𝑑𝑑𝑑𝑑(𝑥𝑥)
Dove 𝑣𝑣(𝑥𝑥) = −𝜇𝜇𝑛𝑛 𝐸𝐸(𝑥𝑥) = 𝜇𝜇𝑛𝑛                è la velocità degli 𝑒𝑒 − (cariche libere di canale) ed 𝐼𝐼𝐷𝐷𝐷𝐷 è deﬁnita come corrente
                                      𝑑𝑑𝑑𝑑
per unità di lunghezza.

                                                                  𝑑𝑑𝑑𝑑(𝑥𝑥)                                         𝑑𝑑𝑑𝑑(𝑥𝑥)
                               𝐼𝐼𝐷𝐷𝐷𝐷 = −𝑊𝑊𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 (𝑥𝑥)𝜇𝜇𝑛𝑛               = 𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂 �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉(𝑥𝑥)�𝜇𝜇𝑛𝑛
                                                                     𝑑𝑑𝑑𝑑                                             𝑑𝑑𝑑𝑑

Si deﬁnisce la conducibilità intrinseca del MOSFET 𝛽𝛽𝑛𝑛′ = 𝜇𝜇𝑛𝑛 𝐶𝐶𝑂𝑂𝑂𝑂 (dipende solo da 𝑇𝑇𝑂𝑂𝑂𝑂 e non dalle dimensioni).

Per ottenere l’equazione della corrente

                    𝐿𝐿                         𝐿𝐿                                                              𝑉𝑉𝐷𝐷𝐷𝐷
                                                                              𝑑𝑑𝑑𝑑(𝑥𝑥)
                  � 𝐼𝐼𝐷𝐷𝐷𝐷 𝑑𝑑𝑑𝑑 = 𝑊𝑊𝛽𝛽𝑛𝑛′ � �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉(𝑥𝑥)�                     𝑑𝑑𝑑𝑑 = 𝑊𝑊𝛽𝛽𝑛𝑛′ � �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉(𝑥𝑥)� 𝑑𝑑𝑑𝑑
                   0                         0                                   𝑑𝑑𝑑𝑑                        0
                                                                                  ⇓
                                                                                                          2
                                                                                                      𝑉𝑉𝐷𝐷𝐷𝐷
                                                       𝐼𝐼𝐷𝐷𝐷𝐷 𝐿𝐿 = 𝑊𝑊𝛽𝛽𝑛𝑛′ �(𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )𝑉𝑉𝐷𝐷𝐷𝐷 −         �
                                                                                                        2
                                                                                  ⇓
                                                                                                      2
                                                                                                   𝑉𝑉𝐷𝐷𝐷𝐷
                                                           𝐼𝐼𝐷𝐷𝐷𝐷 = 𝛽𝛽𝑛𝑛 �(𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )𝑉𝑉𝐷𝐷𝐷𝐷 −        �
                                                                                                     2

                                                                                𝑊𝑊
Dove 𝛽𝛽𝑛𝑛 = 𝛽𝛽𝑛𝑛′ 𝑆𝑆 è la conducibilità del MOSFET ed 𝑆𝑆 =                           è il suo fattore di forma.
                                                                                𝐿𝐿


Si nota che il massimo di 𝐼𝐼𝐷𝐷𝐷𝐷 si ha per 𝑉𝑉𝐷𝐷𝐷𝐷 = 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 .
In tale condizione, la (∗∗∗) diventa

                           𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 (𝐿𝐿) = −𝐶𝐶𝑂𝑂𝑂𝑂 (𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉𝐷𝐷𝐷𝐷 ) = −𝐶𝐶𝑂𝑂𝑂𝑂 (𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − (𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )) = 0

Bisogna quindi effettuare delle considerazioni sul modello della corrente appena calcolato.
In particolare si ha:

                                                                                         2
                                                                                      𝑉𝑉𝐷𝐷𝐷𝐷
                                         𝐼𝐼𝐷𝐷𝐷𝐷 = 𝛽𝛽𝑛𝑛 �(𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )𝑉𝑉𝐷𝐷𝐷𝐷 −             �    𝑉𝑉𝐷𝐷𝐷𝐷 ≤ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇
                                                                                        2

Deﬁnita come regione di TRIODO.

Per 𝑉𝑉𝐷𝐷𝐷𝐷 ≥ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 il canale si strozza vicino al D e si dice che è in pinch-off. In questa condizione, le cariche
libere sono molto poche vicino al D, ma sono soggette ad un campo elettrico molto elevato che fa si che
riescano comunque a transitare verso S (velocità molto alte delle cariche libere).
Il risultato è che la corrente rimane pressoché invariata al valore

                                                               𝛽𝛽𝑛𝑛
                                                    𝐼𝐼𝐷𝐷𝐷𝐷 =        (𝑉𝑉 − 𝑉𝑉𝑇𝑇 )2          𝑉𝑉𝐷𝐷𝐷𝐷 ≥ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇
                                                                2 𝐺𝐺𝐺𝐺

Deﬁnita come regione di SATURAZIONE.
MODELLIZZAZIONE DI LUNGHEZZA DI CANALE:

Se 𝑉𝑉𝐷𝐷𝐷𝐷 ≥ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 e 𝑉𝑉𝐷𝐷𝐷𝐷 ↑, il punto di pinch-off si sposta sempre più verso il S facendo si che il canale si restringa
passando da 𝐿𝐿 ad 𝐿𝐿′ = 𝐿𝐿 − ∆𝐿𝐿.

Applicando il modella appena derivato (mantenendo l’ipotesi di variazione graduale della tensione di canale con
il potenziale 𝑉𝑉(𝑥𝑥)), si ottiene che

                                                     2
                              ⎧𝛽𝛽 �(𝑉𝑉 − 𝑉𝑉 )𝑉𝑉 − 𝑉𝑉𝐷𝐷𝐷𝐷 � (1 + 𝜆𝜆𝑉𝑉 )                     𝑉𝑉𝐷𝐷𝐷𝐷 ≤ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇             𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇
                              ⎪ 𝑛𝑛    𝐺𝐺𝐺𝐺 𝑇𝑇 𝐷𝐷𝐷𝐷
                                                    2               𝐷𝐷𝐷𝐷
                   𝐼𝐼𝐷𝐷𝐷𝐷 =
                              ⎨ 𝛽𝛽𝑛𝑛
                              ⎪ (𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )2 (1 + 𝜆𝜆𝑉𝑉𝐷𝐷𝐷𝐷 )                          𝑉𝑉𝐷𝐷𝐷𝐷 ≥ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇   𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆
                              ⎩ 2
                                                                                                     1
Dove si è introdotto il fattore di modulazione di lunghezza di canale 𝜆𝜆 � �.
                                                                                                     𝑉𝑉



P-MOSFET:

Per quanto riguarda il p-MOSFET (substrato n-Si), valgono tutti i ragionamenti fatti per l’n-MOSFET, con l’unica
differenza che le tensioni sono opposte:

                                                         𝑉𝑉𝐺𝐺𝐺𝐺 > 𝑉𝑉𝐹𝐹𝐹𝐹        ⇒ 𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎
                                                        � 𝑉𝑉𝑇𝑇 < 𝑉𝑉𝐺𝐺𝐺𝐺 < 𝑉𝑉𝐹𝐹𝐹𝐹 ⇒ 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠
                                                          𝑉𝑉𝐺𝐺𝐺𝐺 < 𝑉𝑉𝑇𝑇            ⇒ 𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖

ricordando anche che il la concentrazione di atomi di drogaggio è indicata come 𝑁𝑁𝐷𝐷 .

Densità di carica ﬁssa: 𝜌𝜌𝑑𝑑 = 𝑞𝑞𝑁𝑁𝐷𝐷

Quantità di carica per unità d’area: 𝑄𝑄𝐷𝐷 = 𝜌𝜌𝑑𝑑 𝑊𝑊𝐷𝐷

                                      �2𝜀𝜀𝑆𝑆𝑆𝑆 𝑞𝑞𝑁𝑁𝐷𝐷
Fattore di effetto body: 𝛾𝛾 =
                                          𝐶𝐶𝑂𝑂𝑂𝑂


Carica totale nel substrato: 𝑄𝑄𝑆𝑆 ≈ 𝑄𝑄𝐷𝐷 = �2𝜀𝜀𝑆𝑆𝑆𝑆 𝑞𝑞𝑁𝑁𝐷𝐷 𝜓𝜓𝑠𝑠 = 𝛾𝛾𝐶𝐶𝑂𝑂𝑂𝑂 �𝜓𝜓𝑠𝑠

Potenziale all’interfaccia: 𝜓𝜓𝑠𝑠 = −2𝜓𝜓𝐹𝐹 < 0

Tensione di soglia: 𝑉𝑉𝑇𝑇0 = 𝑉𝑉𝐹𝐹𝐹𝐹 + 𝜓𝜓𝑠𝑠 + 𝛾𝛾�|𝜓𝜓𝑠𝑠 | < 0

Effetto body: 𝜓𝜓𝑠𝑠′ = 𝜓𝜓𝑠𝑠 + 𝑉𝑉𝑆𝑆𝑆𝑆 con 𝑉𝑉𝑆𝑆𝑆𝑆 < 0  𝑉𝑉𝑇𝑇 = 𝑉𝑉𝑇𝑇0 − 𝛾𝛾��|𝜓𝜓𝑠𝑠′ | − �|𝜓𝜓𝑠𝑠 |�  𝑉𝑉𝑇𝑇 ↓ se 𝜓𝜓𝑠𝑠 ↑

                              𝑊𝑊
Fattore di forma: 𝑆𝑆 =
                              𝐿𝐿


Conducibilità intrinseca p-MOSFET: 𝛽𝛽𝑝𝑝′ = 𝜇𝜇𝑝𝑝 𝐶𝐶𝑂𝑂𝑂𝑂

Conducibilità del p-MOSFET: 𝛽𝛽𝑝𝑝 = 𝛽𝛽𝑝𝑝′ 𝑆𝑆

Funzionamento:

     -    𝑉𝑉𝐺𝐺𝐺𝐺 > 𝑉𝑉𝑇𝑇  p-MOSFET OFF

     -    𝑉𝑉𝐺𝐺𝐺𝐺 < 𝑉𝑉𝑇𝑇  p-MOSFET ON

                                                                                         2 ⁄ ](1
               o     𝑉𝑉𝐷𝐷𝐷𝐷 > 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇  𝐼𝐼𝑆𝑆𝑆𝑆 = 𝛽𝛽𝑝𝑝 [(𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝐷𝐷𝐷𝐷 2   − 𝜆𝜆𝑉𝑉𝐷𝐷𝐷𝐷 )  TRIODO
                                                                                 2
               o     𝑉𝑉𝐷𝐷𝐷𝐷 ≤ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇  𝐼𝐼𝑆𝑆𝑆𝑆 = 𝛽𝛽𝑝𝑝 ⁄2 (𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 ) (1 − 𝜆𝜆𝑉𝑉𝐷𝐷𝐷𝐷 )  SATURAZIONE
EFFETTI REATTIVI DEL MOSFET:

Per i seguenti calcoli si considera un n-MOSFET.
Ci sono 2 tipi di effetti reattivi nei MOSFET, che sono dovuti a delle capacità differenziali che dipendono dal
relativo punto di lavoro:

    1) Effetti reattivi intrinseci dovuti al fatto che c’è un condensatore MOS ed alla carica indotta nel substrato
       tramite il gate:

             a. MOSFET ON  𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 (𝑥𝑥) = −𝐶𝐶𝑂𝑂𝑂𝑂 �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉(𝑥𝑥)� quantità di carica di canale per unità d’area
                           𝑄𝑄𝐷𝐷 è praticamente costante e non introduce effetti reattivi
                                                                                         𝑥𝑥
                       i. Regione TRIODO  si considera 𝑉𝑉(𝑥𝑥) = 𝑉𝑉𝐷𝐷𝐷𝐷 e resistività canale costante lungo il
                                                                       𝐿𝐿
                          canale.

                          La carica di canale è:

                                             𝐿𝐿                         𝐿𝐿
                                                                                                      𝑥𝑥                                  𝑉𝑉𝐷𝐷𝐷𝐷
                           |𝑄𝑄𝐶𝐶𝐶𝐶 | = 𝑊𝑊 � |𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 | 𝑑𝑑𝑑𝑑 = 𝑊𝑊 � 𝐶𝐶𝑂𝑂𝑂𝑂 �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉𝐷𝐷𝐷𝐷 � 𝑑𝑑𝑑𝑑 = 𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂 𝐿𝐿 �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 −         �
                                            0                          0                              𝐿𝐿                                    2
                                                                                        ⇓
                                                                                 𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝐺𝐺𝐺𝐺                   𝑉𝑉𝐺𝐺𝐺𝐺 𝑉𝑉𝐺𝐺𝐺𝐺
                                        |𝑄𝑄𝐶𝐶𝐶𝐶 | = 𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂 𝐿𝐿 �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 −                 � = 𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂 𝐿𝐿 �       +       − 𝑉𝑉𝑇𝑇 �
                                                                                        2                            2      2

                                               Le capacità differenziali tra G − D e G − S in triodo sono:

                                                                               𝜕𝜕|𝑄𝑄𝐶𝐶𝐶𝐶 | 1
                                                                    𝐶𝐶𝐺𝐺𝑆𝑆𝐶𝐶 =            = 𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂
                                                                                 𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺  2
                                                                               𝜕𝜕|𝑄𝑄𝐶𝐶𝐶𝐶 | 1
                                                                    𝐶𝐶𝐺𝐺𝐷𝐷𝐶𝐶 =            = 𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂
                                                                                 𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺  2

                                                                                                       𝑥𝑥 2
                      ii. Regione SATURAZIONE  si considera 𝑉𝑉(𝑥𝑥) = 𝑉𝑉𝐷𝐷𝐷𝐷 � � e 𝑉𝑉𝐷𝐷𝐷𝐷 = 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 .
                                                                                                       𝐿𝐿


                          La carica di canale è:

                                             𝐿𝐿                      𝐿𝐿
                                                                                                     𝑥𝑥 2       2
                            |𝑄𝑄𝐶𝐶𝐶𝐶 | = 𝑊𝑊 � |𝑄𝑄𝐼𝐼𝐼𝐼𝐼𝐼 | 𝑑𝑑𝑑𝑑 = 𝑊𝑊 � 𝐶𝐶𝑂𝑂𝑂𝑂 �𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉𝐷𝐷𝐷𝐷 � � � 𝑑𝑑𝑑𝑑 = 𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂 𝐿𝐿(𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )
                                            0                       0                                𝐿𝐿         3

                          Le capacità differenziali tra G-D e G-S in saturazione sono:

                                                                               𝜕𝜕|𝑄𝑄𝐶𝐶𝐶𝐶 | 2
                                                                    𝐶𝐶𝐺𝐺𝑆𝑆𝐶𝐶 =             = 𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂
                                                                                 𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺   3
                                                                               𝜕𝜕|𝑄𝑄𝐶𝐶𝐶𝐶 |
                                                                    𝐶𝐶𝐺𝐺𝐷𝐷𝐶𝐶 =             =0
                                                                                 𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺

             b. MOSFET OFF  𝑄𝑄𝐷𝐷 (𝑥𝑥) = −𝛾𝛾𝛾𝛾𝑂𝑂𝑂𝑂 �𝜓𝜓𝑠𝑠 quantità di carica ﬁssa per unità d’area
                            le giunzioni S-B e D-B isolano S e D da B
                            𝜓𝜓𝑠𝑠 è la caduta di tensione totale nel substrato che dipende solo da 𝑉𝑉𝐺𝐺𝐺𝐺

                 Le capacità differenziali sono:

                                                                              𝜕𝜕|𝑄𝑄𝐷𝐷 |
                                                              𝐶𝐶𝐺𝐺𝐺𝐺 = 𝑊𝑊𝑊𝑊             ≈ 𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂
                                                                               𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺
                                                                         𝜕𝜕|𝑄𝑄𝐷𝐷 |
                                                              𝐶𝐶𝐺𝐺𝑆𝑆𝐷𝐷 =            =0
                                                                          𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺
                                                                         𝜕𝜕|𝑄𝑄𝐷𝐷 |
                                                              𝐶𝐶𝐺𝐺𝐷𝐷𝐷𝐷 =            =0
                                                                          𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺
        Tabella riassuntiva:

                     REGIONE                                      𝐶𝐶𝐺𝐺𝐺𝐺                                       𝐶𝐶𝐺𝐺𝐺𝐺                               𝐶𝐶𝐺𝐺𝐺𝐺
                        OFF                                        0                                             0                               𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂
                                                             1                                             1
                      TRIODO                                   𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂                                    𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂                              0
                                                             2                                             2
                                                             2
                 SATURAZIONE                                   𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂                                        0                                   0
                                                             3


    2) Effetti reattivi parassiti dovuti alla non idealità della struttura ed agli effetti di bordo:

              a. Capacità di overlap dovute al fatto che l’ossido (di lunghezza 𝐿𝐿𝑑𝑑 ) si sovrappone ai terminali S e D
                 (lunghi entrambi 𝐿𝐿𝑠𝑠 ) di una quantità 𝑥𝑥𝑑𝑑 uguale da entrambe le parti.
                 Questa sovrapposizione crea delle capacità tra G ed i terminali S e D.

                    La capacità appena citata è da sommarsi a quella di fringing, dovuta all’effetto di bordo del
                    campo elettrico che crea, tramite l’aria, le capacità tra il terminale G e quelli di S e D.

                    La capacità totale parassita dovuta da non idealità e da effetti di bordo è quindi:

                                                                                                              𝐹𝐹
                                      𝐶𝐶𝐺𝐺𝑆𝑆0 = 𝐶𝐶𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜 + 𝐶𝐶𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 = 𝑥𝑥𝑑𝑑 𝐶𝐶𝑂𝑂𝑂𝑂 + 𝐶𝐶𝑓𝑓𝑓𝑓 � �
                                                                                                              𝑚𝑚

                                      Le capacità parassite tra i terminali (indipendenti dalle tensioni) sono:

                                      𝐶𝐶𝐺𝐺𝑆𝑆𝑃𝑃 = 𝐶𝐶𝐺𝐺𝐷𝐷𝑃𝑃 = 𝑊𝑊𝐶𝐶𝐺𝐺𝑆𝑆0

              b. Capacità di giunzione dovuta al fatto che le giunzioni S-B e D-B sono in polarizzazione inversa:

                                                                                                  1             𝐹𝐹
                                                                             𝐶𝐶𝐽𝐽 = 𝐶𝐶𝐽𝐽0                     � 2�
                                                                                                               𝑚𝑚
                                                                                                |𝑉𝑉 |
                                                                                            �1 + 𝜙𝜙𝑆𝑆𝑆𝑆
                                                                                                     𝐽𝐽



                    Dove 𝜙𝜙𝐽𝐽 è il potenziale di built-in e 𝐶𝐶𝐽𝐽0 è la capacità di giunzione all’equilibrio.

                    Le capacità tra i terminali dovute alle giunzioni in inversa sono:

                                                                                  𝐶𝐶𝑆𝑆𝑆𝑆 = 𝐶𝐶𝐷𝐷𝐷𝐷 = 𝑊𝑊𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽


In generale le capacità del MOSFET sono le seguenti:

                                                                                  (𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑 𝑑𝑑𝑑𝑑𝑑𝑑 𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 𝑑𝑑𝑑𝑑 𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙)
                                ⎧𝐶𝐶𝐺𝐺𝐺𝐺 = 𝐶𝐶𝐺𝐺𝑆𝑆𝐶𝐶 + 𝐶𝐶𝐺𝐺𝑆𝑆𝑃𝑃
                                ⎪ 𝐶𝐶𝐺𝐺𝐺𝐺 = 𝐶𝐶𝐺𝐺𝐷𝐷 + 𝐶𝐶𝐺𝐺𝐷𝐷                       (𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑 𝑑𝑑𝑑𝑑𝑑𝑑 𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 𝑑𝑑𝑑𝑑 𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙)
                                                  𝐶𝐶         𝑃𝑃

                                ⎨𝐶𝐶𝐺𝐺𝐺𝐺                                           (𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑 𝑑𝑑𝑑𝑑𝑑𝑑 𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 𝑑𝑑𝑑𝑑 𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙)
                                ⎪                                          (𝑁𝑁𝑁𝑁𝑁𝑁 𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑 𝑑𝑑𝑑𝑑𝑑𝑑 𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 𝑑𝑑𝑑𝑑 𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙)
                                ⎩ 𝐶𝐶𝑆𝑆𝑆𝑆 = 𝐶𝐶𝐷𝐷𝐷𝐷 = 𝑊𝑊𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽

Molta importanza hanno le capacità viste dal gate nei vari punti di lavoro:

                                                                                                       𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂 + 2𝑊𝑊𝐶𝐶𝐺𝐺𝑆𝑆0           𝑂𝑂𝑂𝑂𝑂𝑂 𝑒𝑒 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇
     𝐶𝐶𝐺𝐺 = 𝐶𝐶𝐺𝐺𝐺𝐺 + 𝐶𝐶𝐺𝐺𝐺𝐺 + 𝐶𝐶𝐺𝐺𝐺𝐺 = 𝐶𝐶𝐺𝐺𝑆𝑆𝐶𝐶 + 𝐶𝐶𝐺𝐺𝑆𝑆𝑃𝑃 + 𝐶𝐶𝐺𝐺𝐷𝐷𝐶𝐶 + 𝐶𝐶𝐺𝐺𝐷𝐷𝑃𝑃 + 𝐶𝐶𝐺𝐺𝐺𝐺 = �2
                                                                                                           𝑊𝑊𝑊𝑊𝐶𝐶𝑂𝑂𝑂𝑂 + 2𝑊𝑊𝐶𝐶𝐺𝐺𝑆𝑆0       𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆
                                                                                                       3
AMPLIFICATORE A SOURCE COMUNE:

Questo ampliﬁcatore prevede che ci sia una tensione di ingresso (𝑉𝑉𝐼𝐼𝐼𝐼 ) tra G ed S e che quest’ultimo sia
riferimento di tensione per G e D (la cui tensione è anche quella di uscita 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ).
La tensione di alimentazione è 𝑉𝑉𝐷𝐷𝐷𝐷 ed è collegata ad una resistenza 𝑅𝑅𝐷𝐷 collegata a sua volta a D.

Studiando i vari punti di lavoro:

    -    MOSFET OFF  𝐼𝐼𝐷𝐷𝐷𝐷 = 0  𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐺𝐺𝐺𝐺 < 𝑉𝑉𝑇𝑇  𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 = 𝑉𝑉𝐷𝐷𝐷𝐷

    -    MOSFET SATURAZIONE  𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐺𝐺𝐺𝐺 > 𝑉𝑉𝑇𝑇 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 > 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 = 𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇
                                                                 ⇓
                                                                              𝛽𝛽𝑛𝑛
                               𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑅𝑅𝐷𝐷 𝐼𝐼𝐷𝐷𝐷𝐷 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑅𝑅𝐷𝐷 (𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇 )2
                                                                               2

    -    MOSFET TRIODO  𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐺𝐺𝐺𝐺 > 𝑉𝑉𝑇𝑇 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 < 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 = 𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇
                                                                    ⇓
                                                                                                                          2
                                                                                                                       𝑉𝑉𝐷𝐷𝐷𝐷
                                      𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑅𝑅𝐷𝐷 𝐼𝐼𝐷𝐷𝐷𝐷 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑅𝑅𝐷𝐷 𝛽𝛽𝑛𝑛 �(𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )𝑉𝑉𝐷𝐷𝐷𝐷 −          �
                                                                                                                         2
                                                                                                      2
                                                                                                   𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑅𝑅𝐷𝐷 𝛽𝛽𝑛𝑛 �(𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇 )𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 −            �
                                                                                                      2
                                                                  ⇓
                                        legge quadratica che ha solo una soluzione possibile

L’applicazione digitale consiste nella porta NOT che prevede l’utilizzo di tale schema in regione OFF o TRIODO.


CONNESSIONE A DIODO:

La connessione a diodo prevede che 𝑉𝑉𝐺𝐺𝐺𝐺 = 𝑉𝑉𝐷𝐷𝐷𝐷 rendendo possibile il funzionamento nella sola regione di
saturazione (𝑉𝑉𝐷𝐷𝐷𝐷 ≥ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 ).
Per il resto lo schema è uguale a quello appena descritto.

Il MOSFET è ON se 𝑉𝑉𝐺𝐺𝐺𝐺 = 𝑉𝑉𝐷𝐷𝐷𝐷 > 𝑉𝑉𝑇𝑇 e si ha:

                                                                                         𝛽𝛽𝑛𝑛
                                        𝑉𝑉𝐷𝐷𝐷𝐷 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑅𝑅𝐷𝐷 𝐼𝐼𝐷𝐷𝐷𝐷 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑅𝑅𝐷𝐷         (𝑉𝑉 − 𝑉𝑉𝑇𝑇 )2
                                                                                          2 𝐷𝐷𝐷𝐷


SPECCHIO DI CORRENTE:

Lo specchio di corrente con n-MOSFET prevede che il transistor di sinistra sia connesso a diodo come nella
conﬁgurazione appena descritta, mentre quello di destra ha il terminale D (nodo di 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ) connesso ad una rete
esterna dove scorre la 𝐼𝐼𝑂𝑂𝑂𝑂𝑂𝑂 .

I due terminali di gate sono connessi insieme in maniera tale da avere 𝑉𝑉𝐺𝐺𝑆𝑆1 = 𝑉𝑉𝐺𝐺𝑆𝑆2 = 𝑉𝑉𝐺𝐺𝐺𝐺 .

Nel MOSFET di sinistra (ON se in SATURAZIONE, altrimenti OFF) scorre la 𝐼𝐼𝑟𝑟𝑟𝑟𝑟𝑟 , corrente che sarà specchiata sul
lato destro.

Con l’ipotesi che i due transistor siano identici si impone che, per funzionare, lo specchio di corrente necessiti
che il MOSFET di sinistra sia anch’esso in regione di saturazione:

                                             𝛽𝛽𝑛𝑛
                                𝐼𝐼𝑂𝑂𝑂𝑂𝑂𝑂 =        (𝑉𝑉 − 𝑉𝑉𝑇𝑇 )2 = 𝐼𝐼𝐷𝐷𝑆𝑆1 = 𝐼𝐼𝑟𝑟𝑟𝑟𝑟𝑟 ,        𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 > 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇
                                              2 𝐺𝐺𝐺𝐺
INVERTER CMOS

L’inverte CMOS prevede l’utilizzo combinato di un p-MOSFET (𝑀𝑀𝑝𝑝 ) (collegato tramite S all’alimentazione 𝑉𝑉𝐷𝐷𝐷𝐷 ) e di
un n-MOSFET (𝑀𝑀𝑛𝑛 ) (collegato a massa tramite S).
Il terminale D è dunque in comune ad entrambi i transistor e deﬁnisce la tensione 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 .
Il gate è altresì in comune ed è collegato alla tensione di ingresso 𝑉𝑉𝐼𝐼𝐼𝐼 .

Ricordando che 𝑉𝑉𝑇𝑇𝑛𝑛 > 0 e 𝑉𝑉𝑇𝑇𝑝𝑝 < 0, come ultima caratteristica si ha che 𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 = 𝐼𝐼𝑆𝑆𝐷𝐷𝑝𝑝 .

Si presentano queste varie condizioni di funzionamento:

     -     𝑀𝑀𝑛𝑛 𝑂𝑂𝑂𝑂𝑂𝑂  𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 = 𝐼𝐼𝑆𝑆𝑆𝑆𝑝𝑝 = 0  𝑉𝑉𝑆𝑆𝐷𝐷𝑝𝑝 = 0  𝑀𝑀𝑝𝑝 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇  𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷
     -     𝑀𝑀𝑝𝑝 𝑂𝑂𝑂𝑂𝑂𝑂  𝐼𝐼𝐷𝐷𝐷𝐷𝑛𝑛 = 𝐼𝐼𝑆𝑆𝑆𝑆𝑝𝑝 = 0  𝑉𝑉𝐷𝐷𝐷𝐷𝑛𝑛 = 0  𝑀𝑀𝑛𝑛 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇  𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 0

                                                             𝛽𝛽𝑛𝑛                           2       𝛽𝛽𝑝𝑝                    2
     -     𝑀𝑀𝑛𝑛 , 𝑀𝑀𝑝𝑝 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆  𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 =        �𝑉𝑉𝐺𝐺𝑆𝑆𝑛𝑛 − 𝑉𝑉𝑇𝑇𝑛𝑛 � = �𝑉𝑉𝐺𝐺𝑆𝑆𝑝𝑝 − 𝑉𝑉𝑇𝑇𝑝𝑝 � = 𝐼𝐼𝐷𝐷𝑆𝑆𝑝𝑝
                                                                2                        2
                                                                                       ⇓
                                                             𝛽𝛽𝑛𝑛                       2         𝛽𝛽𝑝𝑝                              2
                                                                �𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇𝑛𝑛 � = �𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑝𝑝 �
                                                              2                       2
                                                                                    ⇓
                                                                                        𝛽𝛽𝑝𝑝
                                                                          𝑉𝑉𝑇𝑇𝑛𝑛 + �         �𝑉𝑉 + 𝑉𝑉𝑇𝑇𝑝𝑝 �
                                                                                        𝛽𝛽𝑛𝑛 𝐷𝐷𝐷𝐷
                                                             𝑉𝑉𝐼𝐼𝐼𝐼 =                                              = 𝑉𝑉𝐿𝐿𝐿𝐿
                                                                                           𝛽𝛽𝑝𝑝
                                                                                       1+�
                                                                                           𝛽𝛽𝑛𝑛

           In questa condizione (entrambi i transistor saturi), quindi, 𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐿𝐿𝐿𝐿 ∀ 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 . 𝑉𝑉𝐿𝐿𝐿𝐿 è detta tensione di
           soglia logica.

                                                                                                                                                             2
                                                                               𝛽𝛽𝑛𝑛                        2                                              𝑉𝑉𝐷𝐷𝑆𝑆 𝑝𝑝
     -     𝑀𝑀𝑛𝑛 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆, 𝑀𝑀𝑝𝑝 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇  𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 =                �𝑉𝑉𝐺𝐺𝑆𝑆𝑛𝑛 − 𝑉𝑉𝑇𝑇𝑛𝑛 � = 𝛽𝛽𝑝𝑝 ��𝑉𝑉𝐺𝐺𝑆𝑆𝑝𝑝 − 𝑉𝑉𝑇𝑇𝑝𝑝 � 𝑉𝑉𝐷𝐷𝐷𝐷𝑝𝑝 −                    � = 𝐼𝐼𝑆𝑆𝑆𝑆𝑝𝑝
                                                                                2                                                                               2

                                                                                                ⇓
                                                                 𝛽𝛽𝑛𝑛                       2                                                                           (𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 −𝑉𝑉𝐷𝐷𝐷𝐷 )2
                                                                        �𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇𝑛𝑛 � = 𝛽𝛽𝑝𝑝 ��𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑝𝑝 � (𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 − 𝑉𝑉𝐷𝐷𝐷𝐷 ) −                                          �
                                                                    2                                                                                                            2


           Relazione quadratica tra 𝑉𝑉𝐼𝐼𝐼𝐼 e 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 .

                                                                                                                           2                                        2
                                                                                                                        𝑉𝑉𝐷𝐷𝑆𝑆           𝛽𝛽𝑝𝑝
     -     𝑀𝑀𝑛𝑛 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇, 𝑀𝑀𝑝𝑝 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆  𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 = 𝛽𝛽𝑛𝑛 ��𝑉𝑉𝐺𝐺𝑆𝑆𝑛𝑛 − 𝑉𝑉𝑇𝑇𝑛𝑛 �𝑉𝑉𝐷𝐷𝐷𝐷𝑛𝑛 −                    𝑛𝑛
                                                                                                                                    �=      �𝑉𝑉𝐺𝐺𝑆𝑆𝑝𝑝 − 𝑉𝑉𝑇𝑇𝑝𝑝 � = 𝐼𝐼𝑆𝑆𝑆𝑆𝑝𝑝
                                                                                                                              2           2
                                                                                                ⇓
                                                                                                           𝑉𝑉 2        𝛽𝛽𝑝𝑝                                 2
                                                                 𝛽𝛽𝑛𝑛 ��𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇𝑛𝑛 �𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 − 𝑂𝑂𝑂𝑂𝑂𝑂� =                 �𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑝𝑝 �
                                                                                                               2        2


           Relazione quadratica tra 𝑉𝑉𝐼𝐼𝐼𝐼 e 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 .


Tabella riassuntiva della caratteristica statica:

                                                                                                         𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅 𝑀𝑀𝑛𝑛
                                                       𝑂𝑂𝑂𝑂𝑂𝑂                                   𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆               𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇
                                                                                                                            𝑉𝑉𝐼𝐼𝐼𝐼 > 𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝
                               𝑂𝑂𝑂𝑂𝑂𝑂                                                                                     �                          ⑤
                                                                                                                                  𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 0
                                                                                    𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐿𝐿𝐿𝐿                    𝑉𝑉𝐿𝐿𝐿𝐿 < 𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝
 𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅 𝑀𝑀𝑝𝑝   𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆                       �𝑉𝑉 − 𝑉𝑉 < 𝑉𝑉                 < 𝑉𝑉     − 𝑉𝑉     ③ �              2
                                                                                                                                                         ④
                                                                       𝐼𝐼𝐼𝐼    𝑇𝑇𝑛𝑛        𝑂𝑂𝑂𝑂𝑂𝑂     𝐼𝐼𝐼𝐼     𝑇𝑇𝑝𝑝               𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ∝ 𝑉𝑉𝐼𝐼𝐼𝐼
                                                  𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝑇𝑇𝑛𝑛            𝑉𝑉𝑇𝑇 < 𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝐿𝐿𝐿𝐿
                            𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇      �                   ①         � 𝑛𝑛 2                       ②
                                                𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷                 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ∝ 𝑉𝑉𝐼𝐼𝐼𝐼
Si deﬁniscono anche i vali livelli di tensione logici:

     -    Relativi all’output (tensioni dette nominali)

                 o     𝑉𝑉𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 = 𝑓𝑓(𝑉𝑉𝑂𝑂𝑂𝑂 )
                 o     𝑉𝑉𝑂𝑂𝑂𝑂 = 0 𝑉𝑉 = 𝑓𝑓(𝑉𝑉𝑂𝑂𝑂𝑂 ) = 𝑓𝑓 −1 (𝑉𝑉𝑂𝑂𝑂𝑂 )

     -    Relativi all’input

                                                      ∂VOUT
                 o     𝑉𝑉𝐼𝐼𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 = 𝑉𝑉𝐼𝐼𝐼𝐼 ∈ ② |                  = −1
                                                       𝜕𝜕𝑉𝑉𝐼𝐼𝐼𝐼
                                                      ∂VOUT
                 o     𝑉𝑉𝐼𝐼𝐻𝐻𝑀𝑀𝑀𝑀𝑀𝑀 = 𝑉𝑉𝐼𝐼𝐼𝐼 ∈ ④ |                  = −1
                                                       𝜕𝜕𝑉𝑉𝐼𝐼𝐼𝐼


Considerando l’effetto di modulazione di lunghezza di canale (𝜆𝜆 ≠ 0) si ha che il guadagno di tensione 𝐴𝐴𝑉𝑉 , per
𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐿𝐿𝐿𝐿 , è più basso rispetto al caso ideale, dove 𝐴𝐴𝑉𝑉 → ∞.


DIMENSIONAMENTO MOSFET:

                                                                                       𝑉𝑉𝐷𝐷𝐷𝐷
Tipicamente si vuole che sia 𝑉𝑉𝑇𝑇𝑛𝑛 = �𝑉𝑉𝑇𝑇𝑝𝑝 � = 𝑉𝑉𝑇𝑇 e 𝑉𝑉𝐿𝐿𝐿𝐿 =                                 𝛽𝛽𝑛𝑛 = 𝛽𝛽𝑝𝑝 .
                                                                                         2

                                                               ′
                                                             𝛽𝛽𝑛𝑛
Questa condizione implica che sia 𝑆𝑆𝑝𝑝 =                       ′ 𝑆𝑆𝑛𝑛 .
                                                             𝛽𝛽𝑝𝑝

                                                                                                                                                      ′
                                                                                                                                                    𝛽𝛽𝑛𝑛
Se si considera la lunghezza di canale minima come comune (𝐿𝐿𝑛𝑛 = 𝐿𝐿𝑝𝑝 = 𝐿𝐿𝑚𝑚𝑚𝑚𝑚𝑚 )  𝑊𝑊𝑝𝑝 =                                                          ′    𝑊𝑊𝑛𝑛 .
                                                                                                                                                    𝛽𝛽𝑝𝑝


Essendo che 𝛽𝛽𝑝𝑝 = 𝜇𝜇𝑝𝑝 𝐶𝐶𝑂𝑂𝑂𝑂 e 𝛽𝛽𝑛𝑛 = 𝜇𝜇𝑛𝑛 𝐶𝐶𝑂𝑂𝑂𝑂 e che 𝜇𝜇𝑛𝑛 = 2𝜇𝜇𝑝𝑝  𝑊𝑊𝑛𝑛 = 2𝑊𝑊𝑝𝑝  p-MOSFET largo il doppio di n-MOSFET.


TEMPI DI COMMUTAZIONE:

Ipotizzando transizioni istantanee dell’ingresso, trascurando l’effetto di modulazione di lunghezza di canale e
considerando una sola capacità come carico sull’uscita dell’inverter (𝐶𝐶𝐿𝐿 ), si vogliono studiare i transitori di
discesa e di salita di 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 :

     -    TRANSITORIO DI DISCESA

          Si considera come ingresso un fronte di salita  𝑉𝑉𝐼𝐼𝐼𝐼 (𝑡𝑡 = 0− ) = 0 𝑉𝑉 e 𝑉𝑉𝐼𝐼𝐼𝐼 (𝑡𝑡 = 0+ ) = 𝑉𝑉𝐷𝐷𝐷𝐷 .

          Per 𝑡𝑡 = 0−  𝑀𝑀𝑛𝑛 𝑂𝑂𝑂𝑂𝑂𝑂  𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷  𝐶𝐶𝐿𝐿 si carica ﬁno a 𝑉𝑉𝐶𝐶𝐿𝐿 = 𝑉𝑉𝐷𝐷𝐷𝐷

          Per 𝑡𝑡 = 0+  𝑀𝑀𝑛𝑛 𝑂𝑂𝑂𝑂 e 𝑀𝑀𝑝𝑝 𝑂𝑂𝑂𝑂𝑂𝑂  𝐶𝐶𝐿𝐿 si scarica attraverso 𝑀𝑀𝑛𝑛 tramite la corrente 𝐼𝐼𝑛𝑛
                                                 𝑉𝑉𝐷𝐷𝑆𝑆𝑛𝑛 = 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 > 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇𝑛𝑛 = 𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇𝑛𝑛  𝑀𝑀𝑛𝑛 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆
                                                                                        𝑑𝑑𝑉𝑉               𝛽𝛽                         2   𝛽𝛽                        2
                                                               𝐼𝐼𝑛𝑛 = −𝐶𝐶𝐿𝐿 𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑛𝑛 �𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇𝑛𝑛 � = 𝑛𝑛 �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 � (∗ 4)
                                                                             𝑑𝑑𝑑𝑑     2                       2
                                                               ﬁnché 𝑀𝑀𝑛𝑛 è saturo, 𝐶𝐶𝐿𝐿 si scarica a corrente costante

          Si deﬁnisce il 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 come il tempo impiegato dal n-MOSFET per uscire dalla regione di saturazione.
          Integrando entrambi i membri della (∗ 4):

            𝑡𝑡    𝛽𝛽                      2                  𝑡𝑡      𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂                  𝛽𝛽𝑛𝑛                        2   𝑡𝑡                    𝑉𝑉           (𝑡𝑡=𝑡𝑡   )
          ∫0 𝑆𝑆𝑆𝑆𝑆𝑆 2𝑛𝑛 �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 � 𝑑𝑑𝑑𝑑 = −𝐶𝐶𝐿𝐿 ∫0 𝑆𝑆𝑆𝑆𝑆𝑆         𝑑𝑑𝑑𝑑
                                                                                   𝑑𝑑𝑑𝑑 
                                                                                                  2
                                                                                                        �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 � ∫0 𝑆𝑆𝑆𝑆𝑆𝑆 𝑑𝑑𝑑𝑑 = −𝐶𝐶𝐿𝐿 ∫𝑉𝑉 𝑂𝑂𝑂𝑂𝑂𝑂(𝑡𝑡=0)𝑆𝑆𝑆𝑆𝑆𝑆 𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                                                                                                                           𝑂𝑂𝑂𝑂𝑂𝑂
                                                                                                      ⇓
                                   𝛽𝛽𝑛𝑛                  2                  𝑉𝑉 −𝑉𝑉                  𝛽𝛽                    2
                                      �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 � 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 = −𝐶𝐶𝐿𝐿 ∫𝑉𝑉 𝐷𝐷𝐷𝐷 𝑇𝑇𝑛𝑛 𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂  𝑛𝑛 �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 � 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 = 𝐶𝐶𝐿𝐿 𝑉𝑉𝑇𝑇𝑛𝑛
                                    2                                        𝐷𝐷𝐷𝐷                    2
                                                                                                      ⇓
                                                                                                       2𝐶𝐶𝐿𝐿 𝑉𝑉𝑇𝑇𝑛𝑛
                                                                                 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 =                              2
                                                                                               𝛽𝛽𝑛𝑛 �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 �
        Per 𝑡𝑡 > 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 si ha che 𝑀𝑀𝑛𝑛 è in regione triodo e che la 𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 = 𝐼𝐼𝑛𝑛 non è più costante:

                                   𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂                                            𝑉𝑉 2          𝛽𝛽𝑛𝑛                            𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                   𝐼𝐼𝑛𝑛 = −𝐶𝐶𝐿𝐿                 = 𝛽𝛽𝑛𝑛 ��𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 �𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 − 𝑂𝑂𝑂𝑂𝑂𝑂�                  𝑑𝑑𝑑𝑑 = −                                  2
                                      𝑑𝑑𝑑𝑑                                                     2       2𝐶𝐶𝐿𝐿              2�𝑉𝑉𝐷𝐷𝐷𝐷 −𝑉𝑉𝑇𝑇𝑛𝑛 �𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 −𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂


        Deﬁnendo 𝑉𝑉𝛼𝛼 = 2�𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 �, 𝑡𝑡𝑇𝑇𝑇𝑇 = 𝑡𝑡𝑓𝑓 − 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 come il tempo nel quale 𝑀𝑀𝑛𝑛 è in triodo e 𝑡𝑡𝑓𝑓 come il tempo
        per il quale il transitorio di scarica è concluso (𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 �𝑡𝑡 = 𝑡𝑡𝑓𝑓 � = 𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 tensione massima di uscita
        considerabile come uno 0 logico), si ha:

                                               𝛽𝛽𝑛𝑛                       𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂                 𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 1                    1
                                                      𝑑𝑑𝑑𝑑 = −                        2     =−                  �          +                   �
                                               2𝐶𝐶𝐿𝐿              𝑉𝑉𝛼𝛼 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂              𝑉𝑉𝛼𝛼       𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 𝑉𝑉𝛼𝛼 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                                                           ⇓
                 𝑡𝑡𝑓𝑓                     𝑡𝑡𝑓𝑓
                        𝛽𝛽𝑛𝑛                         𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 1                    1                           1 𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀          1            1
              �                𝑑𝑑𝑑𝑑 = � −                      �           +                   � 𝑑𝑑𝑑𝑑 = − �                         �          +                � 𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
               𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 2𝐶𝐶𝐿𝐿           𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆        𝑉𝑉
                                                         𝛼𝛼      𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂      𝑉𝑉𝛼𝛼 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂                  𝑉𝑉𝛼𝛼 𝑉𝑉𝐷𝐷𝐷𝐷 −𝑉𝑉𝑇𝑇𝑛𝑛   𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂   𝑉𝑉
                                                                                                                                                  𝛼𝛼 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                                                           ⇓
                                                                       𝛽𝛽𝑛𝑛             1         𝑉𝑉𝛼𝛼 − 𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀
                                                                             𝑡𝑡𝑇𝑇𝑇𝑇 = ln �                              �
                                                                      2𝐶𝐶𝐿𝐿            𝑉𝑉𝛼𝛼            𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀
                                                                                           ⇓
                                                   𝐶𝐶𝐿𝐿                 2�𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 � − 𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀
                              𝑡𝑡𝑇𝑇𝑇𝑇 =                           ln �                                           �
                                       𝛽𝛽𝑛𝑛 �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 �                       𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀

                             Di conseguenza:

                                                                    2𝐶𝐶𝐿𝐿                 𝑉𝑉𝑇𝑇𝑛𝑛    1     2�𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 � − 𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀
                             𝑡𝑡𝑓𝑓 = 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 + 𝑡𝑡𝑇𝑇𝑇𝑇 =                            �               + ln �                                    ��
                                                            𝛽𝛽𝑛𝑛 �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 � 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 2               𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀

        Con decrescita lineare di 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 per 𝑡𝑡 < 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 e poi logaritmica per 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 < 𝑡𝑡 < 𝑡𝑡𝑓𝑓 .

    -   TRANSITORIO DI SALITA

        Si considera come ingresso un fronte di discesa  𝑉𝑉𝐼𝐼𝐼𝐼 (𝑡𝑡 = 0− ) = 𝑉𝑉𝐷𝐷𝐷𝐷 e 𝑉𝑉𝐼𝐼𝐼𝐼 (𝑡𝑡 = 0+ ) = 0 𝑉𝑉.

        I ragionamenti ed i calcoli svolti per il transitorio di discesa sono analoghi (𝑀𝑀𝑛𝑛 𝑂𝑂𝑂𝑂𝑂𝑂 e 𝑀𝑀𝑝𝑝 𝑂𝑂𝑂𝑂) e quindi,
        deﬁnendo 𝑉𝑉𝑂𝑂𝐻𝐻𝑀𝑀𝑀𝑀𝑀𝑀 come la tensione per la quale si considera concluso il transitorio di carica di 𝐶𝐶𝐿𝐿
        (nonché la tensione minima di uscita considerabile come un 1 logico), si ha:


                                                           2𝐶𝐶𝐿𝐿                      𝑉𝑉𝑇𝑇𝑝𝑝      1     2 �𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝 � − �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑂𝑂𝐻𝐻𝑀𝑀𝑀𝑀𝑀𝑀 �
                  𝑡𝑡𝑟𝑟 = 𝑡𝑡𝑆𝑆𝑆𝑆𝑆𝑆 + 𝑡𝑡𝑇𝑇𝑇𝑇 =                                 �−                  + ln �                                                 ��
                                                   𝛽𝛽𝑝𝑝 �𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝 �        𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝 2                 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑂𝑂𝐻𝐻𝑀𝑀𝑀𝑀𝑀𝑀


Essendo che 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 non potrà mai arrivare a valori di tensione pari a quelli di alimentazione o massa, i tempi di
transizione vengono considerati conclusi quando la tensione raggiunge il 90% dell’escursione massima:

                                                                         𝑉𝑉𝑂𝑂𝐻𝐻𝑀𝑀𝑀𝑀𝑀𝑀 = 0,9 𝑉𝑉𝐷𝐷𝐷𝐷
                                                                       �
                                                                        𝑉𝑉𝑂𝑂𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 = 0,1 𝑉𝑉𝐷𝐷𝐷𝐷

Per sempliﬁcare la formula dei tempi di commutazione, si deﬁnisce la funzione:

                                                                     1      𝑟𝑟   1
                                                       𝐹𝐹(𝑟𝑟) =          �      + ln(19 − 20𝑟𝑟)�
                                                                   1 − 𝑟𝑟 1 − 𝑟𝑟 2

                                                               2𝐶𝐶𝐿𝐿         𝑉𝑉𝑇𝑇
                                                     ⎧𝑡𝑡𝑓𝑓 =             𝐹𝐹 � 𝑛𝑛 � 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑑𝑑𝑑𝑑 𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑
                                                     ⎪       𝛽𝛽   𝑉𝑉
                                                               𝑛𝑛 𝐷𝐷𝐷𝐷       𝑉𝑉𝐷𝐷𝐷𝐷

                                                                             �𝑉𝑉    �
                                                     ⎨𝑡𝑡 = 2𝐶𝐶𝐿𝐿 𝐹𝐹 � 𝑇𝑇𝑝𝑝 � 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑑𝑑𝑑𝑑 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠
                                                     ⎪  𝑟𝑟
                                                             𝛽𝛽𝑝𝑝 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷
                                                     ⎩
I tempi di commutazione visti ﬁno ad adesso sono relativi alla sola uscita.

Per studiare il comportamento dell’uscita a fronte di un determinato ingresso si usano i tempi di propagazione:

     -    𝑡𝑡𝑝𝑝𝑝𝑝 è il tempo di propagazione in salita
     -    𝑡𝑡𝑝𝑝𝑝𝑝 è il tempo di propagazione in discesa

Questi due tempi sono gli intervalli che intercorrono da quando 𝑉𝑉𝐼𝐼𝐼𝐼 è al 50% del suo range ﬁno a quando 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 è
al 50% del suo range.

Considerando 𝑉𝑉𝑇𝑇𝑛𝑛 = �𝑉𝑉𝑇𝑇𝑝𝑝 � = 𝑉𝑉𝑇𝑇 , 𝑡𝑡𝑝𝑝𝑝𝑝 = 𝑡𝑡𝑝𝑝𝑝𝑝 e 𝑡𝑡𝑓𝑓 = 𝑡𝑡𝑟𝑟 si ottiene il tempo di propagazione:

                                                          𝑡𝑡𝑓𝑓 + 𝑡𝑡𝑟𝑟    𝐶𝐶𝐿𝐿 1      1    𝑉𝑉𝑇𝑇
                                                𝑡𝑡𝑝𝑝 =                =       � + � 𝐹𝐹 �        �
                                                               2        𝑉𝑉𝐷𝐷𝐷𝐷 𝛽𝛽𝑛𝑛 𝛽𝛽𝑝𝑝 𝑉𝑉𝐷𝐷𝐷𝐷

                                                                         1
Notando che se 𝑟𝑟 = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐  𝐹𝐹(𝑟𝑟) = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐  𝑡𝑡𝑝𝑝 ∝                        per far sì che 𝑡𝑡𝑝𝑝 ↓  𝑉𝑉𝑇𝑇 ↓ , 𝛽𝛽𝑛𝑛 ↑ , 𝛽𝛽𝑝𝑝 ↑.
                                                                       𝑉𝑉𝐷𝐷𝐷𝐷




CONSUMO DI POTENZA:

Se viene considerata la potenza statica (caratterizzata da ingressi costanti e privi di commutazioni)  𝑃𝑃 = 0.

Questo dal punto di vista teorico, ma da quello pratico intervengono le non idealità del MOSFET che portano:

     -    Correnti di sottosoglia (correnti che si presentano anche per 𝑉𝑉𝐺𝐺 < 𝑉𝑉𝑇𝑇 )  𝐼𝐼𝑂𝑂𝑂𝑂𝑂𝑂 > 0
     -    Correnti inverse di giunzione  𝐼𝐼𝑆𝑆 > 0
     -    Correnti di leakage (dovute all’ossido molto sottile)  correnti di perdita nel gate  𝐼𝐼𝐺𝐺 ≠ 0


Per quanto riguarda la potenza dinamica (caratterizzata da ingressi che commutano)  𝑃𝑃 ≠ 0

                            ∞                            ∞                                             𝑉𝑉𝑂𝑂𝑂𝑂
                                                                      𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                    𝐸𝐸 = � 𝑉𝑉𝐷𝐷𝐷𝐷 𝐼𝐼𝐷𝐷𝐷𝐷 (𝑡𝑡) 𝑑𝑑𝑑𝑑 = � 𝑉𝑉𝐷𝐷𝐷𝐷 𝐶𝐶𝐿𝐿               𝑑𝑑𝑑𝑑 = 𝑉𝑉𝐷𝐷𝐷𝐷 𝐶𝐶𝐿𝐿 � 𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 𝐶𝐶𝐿𝐿 𝑉𝑉𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠
                           0                          0                  𝑑𝑑𝑑𝑑                        𝑉𝑉𝑂𝑂𝑂𝑂


Deﬁnendo 𝒻𝒻0→1 come la frequenza media di commutazioni 0 → 1 e 𝑉𝑉𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 = 𝑉𝑉𝐷𝐷𝐷𝐷 , si ha:

                                                                                       2
                                                          𝑃𝑃𝑑𝑑𝑑𝑑𝑑𝑑 = 𝐸𝐸𝒻𝒻0→1 = 𝐶𝐶𝐿𝐿 𝑉𝑉𝐷𝐷𝐷𝐷 𝒻𝒻0→1

Che è una potenza dinamica media.


INGRESSI GRADUALI:

Nel concreto gli ingressi non sono mai istantanei, e questo produce una corrente di cortocircuito 𝐼𝐼𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 che si
presenta durante 𝑡𝑡𝑟𝑟 e 𝑡𝑡𝑓𝑓 poiché in questi intervalli si ha 𝑉𝑉𝑇𝑇𝑛𝑛 < 𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝 e quindi 𝑀𝑀𝑛𝑛 𝑂𝑂𝑂𝑂 ed 𝑀𝑀𝑝𝑝 𝑂𝑂𝑂𝑂.

La non istantaneità di un ingresso è molto rilevante quando si ha un inverter pilotato da uno a monte (che quindi
genera un’uscita graduale).

Dallo schema dell’inverter con carico 𝐶𝐶𝐿𝐿 , quando 𝑉𝑉𝑇𝑇𝑛𝑛 < 𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝 , si ha:

                                                                                          𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                             𝐼𝐼𝑆𝑆𝐷𝐷𝑝𝑝 − 𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 = 𝐶𝐶𝐿𝐿
                                                                                             𝑑𝑑𝑑𝑑

Il caso peggiore si ha quando 𝐶𝐶𝐿𝐿 è molto piccola poiché fa sì che 𝐼𝐼𝐶𝐶𝐿𝐿 ≈ 0  𝐼𝐼𝑆𝑆𝐷𝐷𝑝𝑝 ≈ 𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 ≈ 𝐼𝐼𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 .
Si deﬁnisce 𝐼𝐼𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 come il valore massimo raggiunto da 𝐼𝐼𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 .
Per calcolare la potenza di cortocircuito si considerano:

                                                        𝑉𝑉𝑇𝑇𝑛𝑛 < 𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝐿𝐿𝐿𝐿                                   𝑡𝑡1 < 𝑡𝑡 < 𝑡𝑡2
                                                       � 𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐿𝐿𝐿𝐿                                                 𝑡𝑡 = 𝑡𝑡2
                                                         𝑉𝑉𝐿𝐿𝐿𝐿 < 𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝                         𝑡𝑡2 < 𝑡𝑡 < 𝑡𝑡3

Con le solite ipotesi di 𝑉𝑉𝑇𝑇𝑛𝑛 = �𝑉𝑉𝑇𝑇𝑝𝑝 � = 𝑉𝑉𝑇𝑇 , 𝛽𝛽𝑛𝑛 = 𝛽𝛽𝑝𝑝 , 𝜆𝜆 = 0, si ha:

                                 𝑡𝑡3                                     𝑡𝑡2                                  𝑡𝑡3                                   𝑡𝑡2
                𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = � 𝑉𝑉𝐷𝐷𝐷𝐷 𝐼𝐼𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 (𝑡𝑡) 𝑑𝑑𝑑𝑑 = � 𝑉𝑉𝐷𝐷𝐷𝐷 𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 (𝑡𝑡) 𝑑𝑑𝑑𝑑 + � 𝑉𝑉𝐷𝐷𝐷𝐷 𝐼𝐼𝑆𝑆𝐷𝐷𝑝𝑝 (𝑡𝑡) 𝑑𝑑𝑑𝑑 = 2𝑉𝑉𝐷𝐷𝐷𝐷 � 𝐼𝐼𝐷𝐷𝑆𝑆𝑛𝑛 (𝑡𝑡) 𝑑𝑑𝑑𝑑
                                𝑡𝑡1                                     𝑡𝑡1                                  𝑡𝑡2                                   𝑡𝑡1


Essendo che per 𝑡𝑡1 < 𝑡𝑡 < 𝑡𝑡2  𝑀𝑀𝑛𝑛 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆:

                                                                  𝑡𝑡2                                           𝑡𝑡2
                                                                   𝛽𝛽𝑛𝑛
                                       𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = 2𝑉𝑉𝐷𝐷𝐷𝐷 �         (𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇 )2 𝑑𝑑𝑑𝑑 = 𝑉𝑉𝐷𝐷𝐷𝐷 𝛽𝛽𝑛𝑛 � (𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇 )2 𝑑𝑑𝑑𝑑
                                                               𝑡𝑡1 2                                          𝑡𝑡1


Dato che 𝑉𝑉𝐼𝐼𝐼𝐼 è la 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 dell’inverter a monte, essa cresce linearmente da 0 a 𝑉𝑉𝐷𝐷𝐷𝐷 nell’intervallo da 0 a 𝑡𝑡𝑟𝑟 :

                                                                         𝑡𝑡              𝑉𝑉𝑇𝑇                                   𝑉𝑉𝐿𝐿𝐿𝐿 𝑡𝑡𝑟𝑟
                                                𝑉𝑉𝐼𝐼𝐼𝐼 (𝑡𝑡) = 𝑉𝑉𝐷𝐷𝐷𝐷         ⇒ 𝑡𝑡1 = 𝑡𝑡𝑟𝑟 𝑛𝑛                       𝑡𝑡2 = 𝑡𝑡𝑟𝑟         =
                                                                        𝑡𝑡𝑟𝑟             𝑉𝑉𝐷𝐷𝐷𝐷                                 𝑉𝑉𝐷𝐷𝐷𝐷 2

                                                                                               ⇓
                                                                              𝑡𝑡𝑟𝑟
                                                                                                                                               3
                                                                               2                                     𝛽𝛽𝑛𝑛 𝑡𝑡𝑟𝑟 𝑉𝑉𝐷𝐷𝐷𝐷
                                            𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = 𝑉𝑉𝐷𝐷𝐷𝐷 𝛽𝛽𝑛𝑛 � 𝑉𝑉 (𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇 )2 𝑑𝑑𝑑𝑑 =                          �       − 𝑉𝑉𝑡𝑡 �
                                                                          𝑡𝑡𝑟𝑟
                                                                                     𝑇𝑇𝑛𝑛                               3        2
                                                                                 𝑉𝑉𝐷𝐷𝐷𝐷


                                                                                         ⇓
                                                                                                               3
                                                                                     𝛽𝛽𝑛𝑛 𝑡𝑡𝑟𝑟 𝑉𝑉𝐷𝐷𝐷𝐷
                                                                    𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑇𝑇𝑟𝑟 =          �       − 𝑉𝑉𝑡𝑡 �
                                                                                        3        2
                                                                                                                      3
                                                                                            𝛽𝛽𝑛𝑛 𝑡𝑡𝑓𝑓 𝑉𝑉𝐷𝐷𝐷𝐷
                                                                   𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑇𝑇𝑓𝑓 =                  �       − 𝑉𝑉𝑡𝑡 �
                                                                                              3         2

Dato che 𝐼𝐼𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = 𝐼𝐼𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 @ 𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐿𝐿𝐿𝐿 :

                                                                                                                    2
                                                                        𝛽𝛽𝑛𝑛                    𝛽𝛽𝑛𝑛 𝑉𝑉𝐷𝐷𝐷𝐷
                                                        𝐼𝐼𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 =         (𝑉𝑉𝐿𝐿𝐿𝐿 − 𝑉𝑉𝑇𝑇 )2 = �          − 𝑉𝑉𝑇𝑇 �
                                                                         2                       2 2

Da cui:

                                                                               2                  𝑉𝑉𝐷𝐷𝐷𝐷
                                                               𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑇𝑇𝑟𝑟 = 𝑡𝑡𝑟𝑟 𝐼𝐼𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 �        − 𝑉𝑉𝑇𝑇 �
                                                                               3                    2

                                                                               2                  𝑉𝑉𝐷𝐷𝐷𝐷
                                                               𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑇𝑇𝑓𝑓 = 𝑡𝑡𝑓𝑓 𝐼𝐼𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 �        − 𝑉𝑉𝑇𝑇 �
                                                                               3                    2

Per un ingresso che esegue un ciclo completo (𝑉𝑉𝐼𝐼𝐼𝐼 da 0 a 𝑉𝑉𝐷𝐷𝐷𝐷 e da 𝑉𝑉𝐷𝐷𝐷𝐷 a 0) con frequenza di commutazione 𝒻𝒻:

                                                                                            2                           𝑉𝑉𝐷𝐷𝐷𝐷
                                      𝑃𝑃𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = �𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑇𝑇𝑟𝑟 + 𝐸𝐸𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑇𝑇𝑓𝑓 � 𝒻𝒻 = �𝑡𝑡𝑟𝑟 + 𝑡𝑡𝑓𝑓 �𝐼𝐼𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 �        − 𝑉𝑉𝑇𝑇 � 𝒻𝒻
                                                                                            3                             2

Se si ha il tempo di commutazione 𝑡𝑡𝑐𝑐 = 𝑡𝑡𝑟𝑟 = 𝑡𝑡𝑓𝑓 :

                                                                             4                  𝑉𝑉𝐷𝐷𝐷𝐷
                                                               𝑃𝑃𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = 𝑡𝑡𝑐𝑐 𝐼𝐼𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 �        − 𝑉𝑉𝑇𝑇 � 𝒻𝒻
                                                                             3                    2

Il caso migliore si ha quando 𝐶𝐶𝐿𝐿 è grande, a discapito, però, del rallentamento di variazione di 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 .
Nel caso di cascata di inverter si ha 𝑡𝑡𝑝𝑝1                                    = 𝑡𝑡𝑐𝑐2        𝑃𝑃𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑇𝑇2 ↑.
                                                                     𝑂𝑂𝑂𝑂𝑂𝑂           𝐼𝐼𝐼𝐼


Nella progettazione degli inverter si cerca di avere 𝑡𝑡𝑐𝑐 ≈ 𝑡𝑡𝑝𝑝  𝑃𝑃𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = 10% 𝑃𝑃𝑑𝑑𝑑𝑑𝑑𝑑 .

Con ingressi non istantanei si modiﬁcano anche le ipotesi fatte per il calcolo di 𝑡𝑡𝑟𝑟 e 𝑡𝑡𝑓𝑓 che possono essere
stimati (data la complessità del calcolo in condizioni di ingresso graduale):

                                                                                         𝑡𝑡𝑝𝑝 = 𝑡𝑡𝑝𝑝𝑟𝑟0 + 𝜂𝜂𝑡𝑡𝑟𝑟𝐼𝐼𝐼𝐼

Dove 𝑡𝑡𝑝𝑝𝑟𝑟0 è il tempo di propagazione con ingresso istantaneo ed 𝜂𝜂 è un parametro empirico (≈ 0,25).


CAPACITA’ INVERTER CMOS:

Essendo che 𝑡𝑡𝑐𝑐 e 𝑡𝑡𝑝𝑝 sono dipendenti dagli effetti reattivi dei MOSFET, si devono valutare le capacità in ingresso
ed in uscita dell’inverter.

Così come dai calcoli effettuati per il relativo calcolo, si considera 𝐶𝐶𝐺𝐺𝑆𝑆0 = 𝐶𝐶𝐺𝐺𝐷𝐷0 e si ottiene:

                                                                               𝐶𝐶𝐺𝐺𝑛𝑛 ≈ 𝑊𝑊𝑛𝑛 𝐿𝐿𝑛𝑛 𝐶𝐶𝑂𝑂𝑂𝑂 + 2𝑊𝑊𝑛𝑛 𝐶𝐶𝐺𝐺𝑆𝑆0

                                                                               𝐶𝐶𝐺𝐺𝑝𝑝 ≈ 𝑊𝑊𝑝𝑝 𝐿𝐿𝑝𝑝 𝐶𝐶𝑂𝑂𝑂𝑂 + 2𝑊𝑊𝑝𝑝 𝐶𝐶𝐺𝐺𝑆𝑆0

Si pone 𝐿𝐿𝑛𝑛 = 𝐿𝐿𝑝𝑝 = 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 e si ottiene la capacità di ingresso dell’inverter CMOS:

                                                     𝐶𝐶𝐼𝐼𝐼𝐼𝐼𝐼 = 𝐶𝐶𝐺𝐺𝑛𝑛 + 𝐶𝐶𝐺𝐺𝑝𝑝 = �𝑊𝑊𝑛𝑛 + 𝑊𝑊𝑝𝑝 �𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 2�𝑊𝑊𝑛𝑛 + 𝑊𝑊𝑝𝑝 �𝐶𝐶𝐺𝐺𝑆𝑆0

                𝑆𝑆𝑝𝑝       𝑊𝑊𝑝𝑝
Posto 𝛼𝛼 ≔             =          :
                𝑆𝑆𝑛𝑛       𝑊𝑊𝑛𝑛


                                                                 𝐶𝐶𝐼𝐼𝐼𝐼𝐼𝐼 = 𝑆𝑆𝑛𝑛 (1 + 𝛼𝛼)�𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 2𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝐺𝐺𝑆𝑆0 �

Quindi:

                                                                              𝐶𝐶𝑀𝑀1 = 𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 2𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝐺𝐺𝑆𝑆0

                                                                                   𝐶𝐶𝐼𝐼𝐼𝐼𝐼𝐼 = 𝑆𝑆𝑛𝑛 (1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1

Dove 𝐶𝐶𝑀𝑀1 è la capacità del MOSFET ad area minima che dipende solo da parametri tecnologici.

L’area minima è:

                                                                               𝐴𝐴𝑀𝑀𝑀𝑀𝑀𝑀 = 𝑊𝑊𝑀𝑀𝑀𝑀𝑀𝑀 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 = 𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀

                                           𝐴𝐴𝐼𝐼𝐼𝐼𝐼𝐼 = 𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 + 𝛼𝛼𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 = (1 + 𝛼𝛼)𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 = 𝑆𝑆𝑛𝑛 (1 + 𝛼𝛼)𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀

              𝑊𝑊𝑛𝑛                     𝑊𝑊𝑝𝑝
Con 𝑆𝑆𝑛𝑛 =              e 𝑆𝑆𝑝𝑝 =                 .
             𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀                 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀




Per la capacità di uscita, sono da considerare tutti i contributi capacitivi sul nodo di uscita.
Per il calcolo si considera un inverter che fa da carico ad un inverter a monte:

                                                                         𝐶𝐶𝐼𝐼𝐼𝐼𝑉𝑉2 = 𝑆𝑆𝑛𝑛2 (1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1 = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐

Non vengono per ora valutate altre capacità se non quelle relative a G (𝐺𝐺𝑝𝑝2 e 𝐺𝐺𝑛𝑛2 ).

Si considera un ulteriore effetto capacitivo 𝐶𝐶𝑊𝑊 dovuto all’interconnessione tra i due inverter.
                                                                                               𝐶𝐶𝐽𝐽0
Si pone 𝑉𝑉𝑆𝑆𝑆𝑆 = 0  𝐶𝐶𝑆𝑆𝑆𝑆 = 0, 𝑉𝑉𝐷𝐷𝐷𝐷 = 𝑓𝑓(𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ), 𝐶𝐶𝐷𝐷𝐷𝐷 = 𝑊𝑊𝐿𝐿𝑠𝑠                                .
                                                                                              �𝑉𝑉     �
                                                                                           �1+ 𝜙𝜙𝐷𝐷𝐷𝐷
                                                                                                  𝐽𝐽



Essendo che il calcolo sarebbe troppo complesso, si considera 𝐶𝐶𝐷𝐷𝐷𝐷 = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 e 𝐶𝐶𝐷𝐷𝐵𝐵𝑒𝑒𝑒𝑒 come la capacità equivalente
al valore medio di 𝐶𝐶𝐷𝐷𝐷𝐷 durante i transitori di carica o scarica.

N.B.: tutti gli elementi relativi al secondo inverter sono identiﬁcati dal pedice “2”.

Si considera l’esempio della carica scambiata nel transitorio di scarica:

                                                               ∞                               𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇
                                                                          𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂                    𝑓𝑓 𝑊𝑊𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽
                                                                                                                      0
                                               ∆𝑄𝑄𝐽𝐽 = � 𝐶𝐶𝐷𝐷𝐷𝐷                      𝑑𝑑𝑑𝑑 = �                             𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                             𝑜𝑜              𝑑𝑑𝑑𝑑            𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇
                                                                                                     𝑖𝑖          𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                                                                          �1 + 𝜙𝜙
                                                                                                                       𝐽𝐽



                                                                                          ⇓

                                                                                                                                                                  𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇
                                                                                                                                                                          𝑓𝑓
                                                             𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇
                          ∆𝑄𝑄𝐽𝐽               1                       𝑓𝑓 𝑊𝑊𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽                      𝑊𝑊𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0                   𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                                                    0
            𝐶𝐶𝐷𝐷𝐵𝐵𝑒𝑒𝑒𝑒 =          =                       �                             𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 =                         �2𝜙𝜙𝐽𝐽 �1 +          �
                         ∆𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑓𝑓 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑖𝑖 𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇                                  𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑓𝑓 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑖𝑖               𝜙𝜙𝐽𝐽
                                                                   𝑖𝑖          𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                                        �1 + 𝜙𝜙                                                                    𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇
                                                                                                                                                           𝑖𝑖
                                                                                     𝐽𝐽



                                                                                          ⇓

                                                                    2𝜙𝜙𝐽𝐽 𝑊𝑊𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0          𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑓𝑓        𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑖𝑖
                                                𝐶𝐶𝐷𝐷𝐵𝐵𝑒𝑒𝑒𝑒 =                              ��1 +            − �1 +            �
                                                                  𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑓𝑓 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑖𝑖          𝜙𝜙𝐽𝐽             𝜙𝜙𝐽𝐽


Essendo 𝑉𝑉𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 e 𝑉𝑉𝑂𝑂𝑂𝑂 = 0 𝑉𝑉 (𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑓𝑓 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑇𝑇𝑖𝑖 = 𝑉𝑉𝑂𝑂𝑂𝑂 − 𝑉𝑉𝑂𝑂𝑂𝑂 = −𝑉𝑉𝐷𝐷𝐷𝐷 ) si ha:


                                                                                 2𝜙𝜙𝐽𝐽        𝑉𝑉𝐷𝐷𝐷𝐷
                                                                      𝐾𝐾𝑒𝑒𝑒𝑒 =          ��1 +        − 1�
                                                                                 𝑉𝑉𝐷𝐷𝐷𝐷        𝜙𝜙𝐽𝐽


                                                                            𝐶𝐶𝐷𝐷𝐵𝐵𝑒𝑒𝑒𝑒 = 𝐾𝐾𝑒𝑒𝑒𝑒 𝑊𝑊𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0

Deﬁnita solo da parametri tecnologici e dalla tensione di alimentazione ed identica sia per 𝑀𝑀𝑛𝑛 che per 𝑀𝑀𝑝𝑝 .
Si possono quindi sostituire tutte le 𝐶𝐶𝐷𝐷𝐷𝐷 con 𝐶𝐶𝐷𝐷𝐵𝐵𝑒𝑒𝑒𝑒 = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 ed il contributo sul nodo di uscita risulterà costante.

Oltre alle 𝐶𝐶𝐷𝐷𝐷𝐷 , il contributo sul nodo di uscita è dato anche da 𝐶𝐶𝐺𝐺𝐷𝐷𝑛𝑛 e 𝐶𝐶𝐺𝐺𝐷𝐷𝑝𝑝 che vedono una tensione ai loro capi
pari a 𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 .
Si calcola il relativo contributo sul nodo di uscita:

                                      ∞                                                              ∞
                                                                     𝑑𝑑(𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 − 𝑉𝑉𝐼𝐼𝐼𝐼 )                                        𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼
                     ∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂 = � 𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 )                              𝑑𝑑𝑑𝑑 = � 𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ) �           −         � 𝑑𝑑𝑑𝑑
                                    0                                         𝑑𝑑𝑑𝑑                  0                                𝑑𝑑𝑑𝑑       𝑑𝑑𝑑𝑑

Dato che dipende dall’evoluzione temporale combinata di 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 e di 𝑉𝑉𝐼𝐼𝐼𝐼 , si considerano questi ultimi come
disgiunti  𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 varia solamente dopo che 𝑉𝑉𝐼𝐼𝐼𝐼 si è stabilizzato (in un tempo 𝑡𝑡𝑅𝑅𝐼𝐼𝐼𝐼 ):

                 ∞                                                             𝑡𝑡𝑅𝑅𝐼𝐼𝐼𝐼                                               𝑡𝑡𝑅𝑅𝐼𝐼𝐼𝐼
                                              𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼                                                   𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼                                               𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂 = � 𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ) �             −         � 𝑑𝑑𝑑𝑑 = − �          𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 )          𝑑𝑑𝑑𝑑 + �          𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 )            𝑑𝑑𝑑𝑑
               0                                𝑑𝑑𝑑𝑑       𝑑𝑑𝑑𝑑            ���������������������
                                                                              0                                       𝑑𝑑𝑑𝑑          ���������������������
                                                                                                                                     0                                        𝑑𝑑𝑑𝑑
                                                                                                         ′
                                                                                                   𝐴𝐴≡∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂                                                 ′′
                                                                                                                                                          𝐵𝐵≡∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂


                                                      𝐴𝐴) 0 < 𝑡𝑡 < 𝑡𝑡𝑅𝑅𝐼𝐼𝐼𝐼 ⟹ 𝑉𝑉𝐼𝐼𝐼𝐼 𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣, 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷
                                                      𝐵𝐵) 𝑡𝑡𝑅𝑅𝐼𝐼𝐼𝐼 < 𝑡𝑡 < ∞ ⟹ 𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐷𝐷𝐷𝐷 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣
Questi due macro-casi vengono scomposti nelle zone ①
                                                   � , ②③④
                                                       �����, ⑤
                                                              �.
                                                                                                   ❶               ❷              ❸


     -     𝐴𝐴❶  𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝑇𝑇𝑛𝑛  𝑀𝑀𝑛𝑛 𝑂𝑂𝑂𝑂𝑂𝑂, 𝑀𝑀𝑝𝑝 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 con 𝑉𝑉𝐷𝐷𝑆𝑆𝑝𝑝 = 0

                                                                         1                                                                          1
                     𝐶𝐶𝐺𝐺𝐷𝐷𝑛𝑛 = 𝑊𝑊𝑛𝑛 𝐶𝐶𝐺𝐺𝑆𝑆0 e 𝐶𝐶𝐺𝐺𝐷𝐷𝑝𝑝 = 𝑊𝑊𝑝𝑝 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 𝑊𝑊𝑝𝑝 𝐶𝐶𝐺𝐺𝑆𝑆0  𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴1 = 𝑊𝑊𝑝𝑝 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + �𝑊𝑊𝑛𝑛 + 𝑊𝑊𝑝𝑝 �𝐶𝐶𝐺𝐺𝑆𝑆0
                                                                         2                                                                          2


     -     𝐴𝐴❷  𝑉𝑉𝑇𝑇𝑛𝑛 < 𝑉𝑉𝐼𝐼𝐼𝐼 < 𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝  𝑀𝑀𝑛𝑛 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 con 𝑉𝑉𝐷𝐷𝑆𝑆𝑛𝑛 = 𝑉𝑉𝐷𝐷𝐷𝐷 , 𝑀𝑀𝑝𝑝 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇

                                                                         1                                                                          1
                     𝐶𝐶𝐺𝐺𝐷𝐷𝑛𝑛 = 𝑊𝑊𝑛𝑛 𝐶𝐶𝐺𝐺𝑆𝑆0 e 𝐶𝐶𝐺𝐺𝐷𝐷𝑝𝑝 = 𝑊𝑊𝑝𝑝 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 𝑊𝑊𝑝𝑝 𝐶𝐶𝐺𝐺𝑆𝑆0  𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴2 = 𝑊𝑊𝑝𝑝 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + �𝑊𝑊𝑛𝑛 + 𝑊𝑊𝑝𝑝 �𝐶𝐶𝐺𝐺𝑆𝑆0
                                                                         2                                                                          2


     -     𝐴𝐴❸  𝑉𝑉𝐼𝐼𝐼𝐼 > 𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝  𝑀𝑀𝑛𝑛 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 con 𝑉𝑉𝐷𝐷𝑆𝑆𝑛𝑛 = 𝑉𝑉𝐷𝐷𝐷𝐷 , 𝑀𝑀𝑝𝑝 𝑂𝑂𝑂𝑂𝑂𝑂

                     𝐶𝐶𝐺𝐺𝐷𝐷𝑛𝑛 = 𝑊𝑊𝑛𝑛 𝐶𝐶𝐺𝐺𝑆𝑆0 e 𝐶𝐶𝐺𝐺𝐷𝐷𝑝𝑝 = 𝑊𝑊𝑝𝑝 𝐶𝐶𝐺𝐺𝑆𝑆0  𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴3 = �𝑊𝑊𝑛𝑛 + 𝑊𝑊𝑝𝑝 �𝐶𝐶𝐺𝐺𝑆𝑆0

                                                                                  ⇓       �𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴1 = 𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴2 �

                                      𝑡𝑡𝑅𝑅𝐼𝐼𝐼𝐼                                                            𝑉𝑉𝐷𝐷𝐷𝐷
                       ′
                                                                                      𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼
                    ∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂 = −�               𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 )                   𝑑𝑑𝑑𝑑 = − � 𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ) 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼
                                     0                                                  𝑑𝑑𝑑𝑑             0
                                                                𝑉𝑉𝑇𝑇𝑛𝑛                                 𝑉𝑉𝐷𝐷𝐷𝐷 +𝑉𝑉𝑇𝑇𝑝𝑝                                    𝑉𝑉𝐷𝐷𝐷𝐷
                                             = −�                        𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴1 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼 − �                            𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴2 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼 − �                        𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴3 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼
                                                              0                                       𝑉𝑉𝑇𝑇𝑛𝑛                                            𝑉𝑉𝐷𝐷𝐷𝐷 +𝑉𝑉𝑇𝑇𝑝𝑝
                                                               𝑉𝑉𝐷𝐷𝐷𝐷 +𝑉𝑉𝑇𝑇𝑝𝑝                                      𝑉𝑉𝐷𝐷𝐷𝐷
                                             = −�                                 𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴1 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼 − �                          𝐶𝐶𝐺𝐺𝐷𝐷𝐴𝐴3 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼
                                                              0                                                𝑉𝑉𝐷𝐷𝐷𝐷 +𝑉𝑉𝑇𝑇𝑝𝑝
                                                1
                                             = − 𝑊𝑊𝑝𝑝 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 �𝑉𝑉𝐷𝐷𝐷𝐷 + 𝑉𝑉𝑇𝑇𝑝𝑝 � − �𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 𝑉𝑉𝐷𝐷𝐷𝐷
                                                2


Si ricorda che 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝑆𝑆𝑛𝑛 e che per il caso 𝐵𝐵 si ha 𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐷𝐷𝐷𝐷 ( 𝑀𝑀𝑝𝑝 𝑂𝑂𝑂𝑂𝑂𝑂 sempre):

(quindi per esempio  𝑉𝑉𝐷𝐷𝑆𝑆𝑛𝑛 = 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 > 𝑉𝑉𝐺𝐺𝑆𝑆𝑛𝑛 − 𝑉𝑉𝑇𝑇𝑛𝑛 = 𝑉𝑉𝐼𝐼𝐼𝐼 − 𝑉𝑉𝑇𝑇𝑛𝑛 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 )

     -     𝐵𝐵❶  𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 > 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛  𝑀𝑀𝑛𝑛 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 con 𝑉𝑉𝐺𝐺𝑆𝑆𝑛𝑛 = 𝑉𝑉𝐷𝐷𝐷𝐷

                     Caso equivalente ad 𝐴𝐴❸  𝐶𝐶𝐺𝐺𝐷𝐷𝐵𝐵1 = �𝑊𝑊𝑛𝑛 + 𝑊𝑊𝑝𝑝 �𝐶𝐶𝐺𝐺𝑆𝑆0

     -     𝐵𝐵❷ e 𝐵𝐵❸  𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 < 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛  𝑀𝑀𝑛𝑛 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 con 𝑉𝑉𝐷𝐷𝑆𝑆𝑛𝑛 = 𝑉𝑉𝐷𝐷𝐷𝐷

                                                                                                                       1
                     Caso equivalente ad 𝐴𝐴❶ ed 𝐴𝐴❷  𝐶𝐶𝐺𝐺𝐷𝐷𝐵𝐵23 = 𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + �𝑊𝑊𝑛𝑛 + 𝑊𝑊𝑝𝑝 �𝐶𝐶𝐺𝐺𝑆𝑆0
                                                                                                                       2


                                                                                                               ⇓

                                                    ∞                                                               0
                                 ′′
                                                                                               𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                              ∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂 =�                   𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 )                  𝑑𝑑𝑑𝑑 = � 𝐶𝐶𝐺𝐺𝐺𝐺 (𝑉𝑉𝐼𝐼𝐼𝐼 , 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 ) 𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂
                                                  𝑡𝑡𝑅𝑅𝐼𝐼𝐼𝐼                                        𝑑𝑑𝑑𝑑            𝑉𝑉𝐷𝐷𝐷𝐷
                                                                              𝑉𝑉𝐷𝐷𝐷𝐷 −𝑉𝑉𝑇𝑇𝑛𝑛                                  0
                                                                  =�                           𝐶𝐶𝐺𝐺𝐷𝐷𝐵𝐵1 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼 + �                         𝐶𝐶𝐺𝐺𝐷𝐷𝐵𝐵23 𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼
                                                                             𝑉𝑉𝐷𝐷𝐷𝐷                                          𝑉𝑉𝐷𝐷𝐷𝐷 −𝑉𝑉𝑇𝑇𝑛𝑛
                                                                                                   1
                                                                  = −�𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 �
                                                                                                   2

Quindi, ipotizzando 𝑉𝑉𝑇𝑇𝑛𝑛 = �𝑉𝑉𝑇𝑇𝑝𝑝 � = 𝑉𝑉𝑇𝑇 :

                                  ′           ′′
                                                                                       1
                   ∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂 = ∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂 + ∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂 = −2�𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 𝑉𝑉𝐷𝐷𝐷𝐷 − �𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 (𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇 )
                                                                                       2
                                                                                          1
                                  ∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂     ∆𝑄𝑄𝑂𝑂𝑂𝑂𝑂𝑂 2�𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 𝑉𝑉𝐷𝐷𝐷𝐷 + 2 �𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 (𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇 )
                     𝐶𝐶𝐺𝐺𝐷𝐷𝑒𝑒𝑒𝑒 =           =−           =
                                  ∆𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂      𝑉𝑉𝐷𝐷𝐷𝐷                                      𝑉𝑉𝐷𝐷𝐷𝐷
                                                                       1                                𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇
                                             = 2�𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 + �𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 �               �
                                                                       2                                    𝑉𝑉𝐷𝐷𝐷𝐷

                  𝑉𝑉𝐷𝐷𝐷𝐷 −𝑉𝑉𝑇𝑇
Dove 𝑅𝑅𝐷𝐷𝐷𝐷 ≔                    e quindi:
                     𝑉𝑉𝐷𝐷𝐷𝐷


                                                                                     1
                                                𝐶𝐶𝐺𝐺𝐷𝐷𝑒𝑒𝑒𝑒 = 2�𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 + �𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 𝑅𝑅𝐷𝐷𝐷𝐷
                                                                                     2


IMPORTANTE:             il termine 2�𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 è indicativo del fatto che le capacità parassite costanti vengono
                        raddoppiate nella capacità di carico equivalente.
                        Questo effetto prende il nome di EFFETTO MILLER ed agisce sui componenti connessi
                        direttamente tra IN ed OUT secondo la seguente formula:

                                                                                    𝐶𝐶𝑒𝑒𝑒𝑒 = (1 − 𝐴𝐴𝑉𝑉 )𝐶𝐶

                         Dove 𝐶𝐶 è la capacità connessa direttamente tra IN ed OUT.
                         Una capacità connessa tra IN ed OUT viene quindi ampliﬁcata in base al guadagno del
                         dispositivo e viene quindi vista come “ingrandita” al nodo di uscita.

                         Questo fa sì che la risposta in frequenza peggiori, così come la velocità di variazione di 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 .

                         Per l’inverter si ha 𝐴𝐴𝑉𝑉𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 = −1  𝐶𝐶𝑒𝑒𝑒𝑒 = 2𝐶𝐶  capacità parassita 𝐶𝐶𝐺𝐺𝐷𝐷𝑛𝑛 + 𝐶𝐶𝐺𝐺𝐷𝐷𝑝𝑝 raddoppiata.


La capacità totale sul nodo di uscita (𝐶𝐶𝐿𝐿 ) quindi risulta essere:

         𝐶𝐶𝐿𝐿 = ��
                𝐶𝐶𝐺𝐺𝐷𝐷� ���
                      𝑒𝑒𝑒𝑒
                           + 𝐶𝐶�𝐷𝐷𝐵𝐵
                                 �� 𝑒𝑒𝑒𝑒
                                         + 𝐶𝐶
                                           ��  + 𝐶𝐶𝐼𝐼𝐼𝐼𝑉𝑉
                                             𝑊𝑊���  ��2
                  𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿𝐿       𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶
                                                                 1
                                       = 2�𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 + �𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 𝑅𝑅𝐷𝐷𝐷𝐷 + 𝐾𝐾
                                                                                                         ��    𝑊𝑊𝐿𝐿𝑠𝑠��
                                                                                                           𝑒𝑒𝑒𝑒���   𝐶𝐶𝐽𝐽0 + 𝐶𝐶𝑊𝑊 + 𝑆𝑆𝑛𝑛2 (1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1
                                                                                                                                    ���������
                                         �����������������������������
                                                                 2
                                                                       𝐶𝐶𝐺𝐺𝐷𝐷𝑒𝑒𝑒𝑒                                 𝐶𝐶𝐷𝐷𝐵𝐵𝑒𝑒𝑒𝑒                    𝐶𝐶𝐼𝐼𝐼𝐼𝑉𝑉2



Espandendo il calcolo di 𝐶𝐶𝐼𝐼𝐼𝐼𝑉𝑉2 :

                                                      𝑊𝑊𝑛𝑛2       𝑊𝑊𝑝𝑝
         𝐶𝐶𝐼𝐼𝐼𝐼𝑉𝑉2 = 𝑆𝑆𝑛𝑛2 (1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1 =                    �1 + 2 � �𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 2𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝐺𝐺𝑆𝑆0 � = �𝑊𝑊𝑛𝑛2 + 𝑊𝑊𝑝𝑝2 ��𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 2𝐶𝐶𝐺𝐺𝑆𝑆0 �
                                                     𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀     𝑊𝑊𝑛𝑛2

                                                                              ⇓
                               1
𝐶𝐶𝐿𝐿 = 2�𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐶𝐶𝐺𝐺𝑆𝑆0 + �𝑊𝑊𝑝𝑝 + 𝑊𝑊𝑛𝑛 �𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 𝑅𝑅𝐷𝐷𝐷𝐷 + 𝐾𝐾𝑒𝑒𝑒𝑒 𝑊𝑊𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0 + 𝐶𝐶𝑊𝑊 + 2�𝑊𝑊𝑛𝑛2 + 𝑊𝑊𝑝𝑝2 �𝐶𝐶𝐺𝐺𝑆𝑆0 + �𝑊𝑊𝑛𝑛2 + 𝑊𝑊𝑝𝑝2 �𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂
                               2

Il ritardo minimo garantito dalla tecnologia CMOS si ha con:

     -     𝑊𝑊𝑝𝑝 = 𝑊𝑊𝑝𝑝2 e 𝑊𝑊𝑛𝑛 = 𝑊𝑊𝑛𝑛2
     -     𝐿𝐿𝑛𝑛 = 𝐿𝐿𝑝𝑝 = 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀
     -     𝑉𝑉𝑇𝑇𝑛𝑛 = �𝑉𝑉𝑇𝑇𝑝𝑝 � = 𝑉𝑉𝑇𝑇

Da cui si ottiene ﬁnalmente il valore di 𝐶𝐶𝐿𝐿 :

           1                                                                             1
𝐶𝐶𝐿𝐿 = �1 + 𝑅𝑅𝐷𝐷𝐷𝐷 � 𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 4𝑊𝑊𝑛𝑛 𝐶𝐶𝐺𝐺𝑆𝑆0 + 𝐾𝐾𝑒𝑒𝑒𝑒 𝑊𝑊𝑛𝑛 𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0 + �1 + 𝑅𝑅𝐷𝐷𝐷𝐷 � 𝑊𝑊𝑝𝑝 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 4𝑊𝑊𝑝𝑝 𝐶𝐶𝐺𝐺𝑆𝑆0 + 𝐾𝐾𝑒𝑒𝑒𝑒 𝑊𝑊𝑝𝑝 𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0 + 𝐶𝐶𝑊𝑊
       ���������������������������������
           2                                                                             2
                                              𝐶𝐶𝑛𝑛
                                                                                        ⇓
                                                                  1
                                                       𝐶𝐶𝑛𝑛 = �1 + 𝑅𝑅𝐷𝐷𝐷𝐷 � 𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 + 4𝑊𝑊𝑛𝑛 𝐶𝐶𝐺𝐺𝑆𝑆0 + 𝐾𝐾𝑒𝑒𝑒𝑒 𝑊𝑊𝑛𝑛 𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0
                                                                  2

                                                                                      𝐶𝐶𝐿𝐿 = 𝐶𝐶𝑛𝑛 (1 + 𝛼𝛼) + 𝐶𝐶𝑊𝑊


Supponendo una transizione istantanea di 𝑉𝑉𝐼𝐼𝐼𝐼 , dall’equazione calcolata per il tempo di propagazione si ottiene:

                                                                                   𝑡𝑡𝑟𝑟 + 𝑡𝑡𝑓𝑓    𝐶𝐶𝐿𝐿 1      1    𝑉𝑉𝑇𝑇
                                                                          𝑡𝑡𝑝𝑝 =               =       � + � 𝐹𝐹 �        �
                                                                                        2        𝑉𝑉𝐷𝐷𝐷𝐷 𝛽𝛽𝑛𝑛 𝛽𝛽𝑝𝑝 𝑉𝑉𝐷𝐷𝐷𝐷

                                                                                                       ⇓

                                                                                  𝐶𝐶𝑛𝑛 (1 + 𝛼𝛼) + 𝐶𝐶𝑊𝑊 1     1    𝑉𝑉𝑇𝑇
                                                                         𝑡𝑡𝑝𝑝 =                       � + � 𝐹𝐹 �        �
                                                                                          𝑉𝑉𝐷𝐷𝐷𝐷       𝛽𝛽𝑛𝑛 𝛽𝛽𝑝𝑝 𝑉𝑉𝐷𝐷𝐷𝐷

Quindi se 𝐶𝐶𝐿𝐿 ↑  𝑡𝑡𝑝𝑝 ↑ e se 𝑉𝑉𝐷𝐷𝐷𝐷 ↑  𝑡𝑡𝑝𝑝 ↓.

Si nota inoltre che 𝐶𝐶𝑛𝑛 e 𝛽𝛽𝑛𝑛 dipendono da 𝑆𝑆𝑛𝑛 .

                                ′        𝛽𝛽𝑝𝑝              ′
                                                    𝑆𝑆𝑝𝑝 𝛽𝛽𝑝𝑝
                              𝛽𝛽𝑛𝑛                                  𝛼𝛼                𝛼𝛼                   𝐶𝐶 (1+𝛼𝛼)+𝐶𝐶𝑊𝑊             𝜀𝜀               𝑉𝑉
Deﬁnendo 𝜀𝜀 ≔                   ′              =          ′    =         𝛽𝛽𝑝𝑝 = 𝛽𝛽𝑛𝑛  𝑡𝑡𝑝𝑝 = 𝑛𝑛                           �1 + 𝛼𝛼� 𝐹𝐹 �𝑉𝑉 𝑇𝑇 �
                              𝛽𝛽𝑝𝑝       𝛽𝛽𝑛𝑛       𝑆𝑆𝑛𝑛 𝛽𝛽𝑛𝑛       𝜀𝜀                𝜀𝜀                      𝛽𝛽𝑛𝑛 𝑉𝑉𝐷𝐷𝐷𝐷                              𝐷𝐷𝐷𝐷


Dalla quale, se 𝛼𝛼 ↑  𝛽𝛽𝑝𝑝 ↑ ma anche 𝐶𝐶𝐿𝐿 ↑.

Per avere un 𝑡𝑡𝑝𝑝𝑜𝑜𝑜𝑜𝑜𝑜 (tempo di propagazione ottimale) rispetto ad 𝛼𝛼𝑜𝑜𝑜𝑜𝑜𝑜 si deve porre:


                       𝜕𝜕𝑡𝑡𝑝𝑝      𝜕𝜕𝑡𝑡𝑝𝑝               𝜀𝜀                                         𝜀𝜀                         𝐶𝐶𝑊𝑊
                              =0 ⇒        ∝ 𝐶𝐶𝑛𝑛 �1 +          � − �𝐶𝐶𝑛𝑛 �1 + 𝛼𝛼𝑜𝑜𝑜𝑜𝑜𝑜 � + 𝐶𝐶𝑊𝑊 � 2 = 0 ⇒ 𝛼𝛼𝑜𝑜𝑜𝑜𝑜𝑜 = �𝜀𝜀 �1 +      �
                       𝜕𝜕𝜕𝜕        𝜕𝜕𝜕𝜕               𝛼𝛼𝑜𝑜𝑜𝑜𝑜𝑜                                   𝛼𝛼𝑜𝑜𝑜𝑜𝑜𝑜                     𝐶𝐶𝑛𝑛

                                                                                                                                           2
                                                                                                                            𝐶𝐶 �1+√𝜀𝜀�                 𝑉𝑉𝑇𝑇
Se l’interconnessione è breve  𝐶𝐶𝑊𝑊 ≪ 𝐶𝐶𝑛𝑛  𝛼𝛼𝑜𝑜𝑜𝑜𝑜𝑜 ≈ √𝜀𝜀  𝑡𝑡𝑝𝑝𝑜𝑜𝑜𝑜𝑜𝑜 ≈ 𝑛𝑛                                                                 𝐹𝐹 �            �
                                                                                                                             𝛽𝛽𝑛𝑛 𝑉𝑉𝐷𝐷𝐷𝐷              𝑉𝑉𝐷𝐷𝐷𝐷


E quindi 𝑡𝑡𝑝𝑝𝑜𝑜𝑜𝑜𝑜𝑜 NON dipende dal dimensionamento poiché 𝑊𝑊𝑛𝑛 è contenuto sia in 𝛽𝛽𝑛𝑛 che in 𝐶𝐶𝑛𝑛 e si sempliﬁca.

Inoltre si ha che se 𝑊𝑊𝑛𝑛 ↑  𝐼𝐼𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐/𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 ↑ ma anche 𝐶𝐶 ↑  gli effetti si compensano.

Producendo i MOSFET ad area minima, si occupa meno spazio e 𝑡𝑡𝑝𝑝𝑜𝑜𝑜𝑜𝑜𝑜 ∝ 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 .

Espandendo l’equazione di 𝐶𝐶𝑛𝑛 e quella di 𝛽𝛽𝑛𝑛 e sempliﬁcando un po’, si ottiene:

                                                                              2
                                                𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 �1 + √𝜀𝜀�       𝑉𝑉𝑇𝑇         1                      𝐶𝐶𝐺𝐺𝑆𝑆0               𝐶𝐶𝐽𝐽
                                         𝑡𝑡𝑝𝑝 =                    𝐹𝐹 �        � ��1 + 𝑅𝑅𝐷𝐷𝐷𝐷 � 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 + 4         + 𝐾𝐾𝑒𝑒𝑒𝑒 𝐿𝐿𝑠𝑠 0 �
                                                       𝜇𝜇𝑛𝑛 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷        2                      𝐶𝐶𝑂𝑂𝑂𝑂               𝐶𝐶𝑂𝑂𝑂𝑂

     𝐶𝐶𝐺𝐺𝑆𝑆0       𝐶𝐶𝐽𝐽0
Se             ,           ≪ 1  𝑡𝑡𝑝𝑝𝑜𝑜𝑜𝑜𝑜𝑜 ∝ 𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀  le tecnologie CMOS scalate sono più veloci.
     𝐶𝐶𝑂𝑂𝑂𝑂 𝐶𝐶𝑂𝑂𝑂𝑂




OSCILLATORE AD ANELLO:

E’ una catena di 𝑁𝑁 (dispari) inverter tutti uguali connessi ad anello che creano quindi un circuito instabile che
oscilla generando una forma d’onda periodica (onda quadra).
Ogni inverter ha un suo 𝑡𝑡𝑝𝑝 e se 𝑁𝑁 ≥ 5 si ha:
                                                       𝑇𝑇𝑜𝑜𝑜𝑜𝑜𝑜 ≈ 2𝑁𝑁𝑡𝑡𝑝𝑝

                                                                                              1
Ciò rende possibile misurare 𝑡𝑡𝑝𝑝 a partire da 𝒻𝒻𝑜𝑜𝑜𝑜𝑜𝑜 =                                              (fornendo quindi un circuito di test per tecnologie CMOS).
                                                                                            𝑇𝑇𝑜𝑜𝑜𝑜𝑜𝑜
QUADRIPOLO

Un quadripolo è un componente che ha 4 terminali  4 tensioni e 4 correnti in rappresentazione indeﬁnita.

Se è lineare  sistema di equazioni lineare in dominio tempo
Se è anomalo  linearizzazione  sistema di equazioni lineare in dominio tempo
Se ci sono effetti reattivi  Trasformata Di Laplace (TDL)  sistema di equazioni lineare in dominio frequenza

Se si ha la rappresentazione deﬁnita bastano 3 tensioni e 3 correnti poiché un morsetto è di riferimento.


DOPPIO BIPOLO

Componente avente 2 porte  2 correnti e 2 tensioni indipendenti

Ci sono sempre 4 morsetti, ma il 1° ed il 3° sono posti a sinistra del componente (formando la porta 1), mentre il
2° ed il 4° alla destra (formando la porta 2).

Sulla porta 1 si hanno:

    -    Al morsetto 1 la tensione 𝑉𝑉1𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 e la corrente entrante 𝐼𝐼1
    -    Al morsetto 3 la tensione 𝑉𝑉3𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 e la corrente uscente 𝐼𝐼3

Sulla porta 2 si hanno:

    -    Al morsetto 2 la tensione 𝑉𝑉2𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 e la corrente entrante 𝐼𝐼2
    -    Al morsetto 4 la tensione 𝑉𝑉4𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 e la corrente uscente 𝐼𝐼4

Vige il seguente sistema di equazioni:

                                                              𝐼𝐼1 = −𝐼𝐼3
                                                  ⎧           𝐼𝐼2 = −𝐼𝐼4
                                                  ⎨𝑉𝑉1 = 𝑉𝑉1𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 − 𝑉𝑉3𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚
                                                  ⎩𝑉𝑉2 = 𝑉𝑉2𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 − 𝑉𝑉4𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚

Si ottengono quindi 4 variabili (𝐼𝐼1 , 𝐼𝐼2 , 𝑉𝑉1 , 𝑉𝑉2 ) che descrivono il comportamento del componente tramite il sistema

                                                          𝑉𝑉 = 𝑧𝑧11 𝐼𝐼1 + 𝑧𝑧12 𝐼𝐼2
                                                         � 1
                                                          𝑉𝑉2 = 𝑧𝑧21 𝐼𝐼1 + 𝑧𝑧22 𝐼𝐼2

Si può studiare il comportamento di un doppio bipolo tramite diversi tipi di matrici, decidendo a priori quali
debbano essere le variabili dipendenti e quali quelle indipendenti:

    -    Matrice impedenza:

                                                        𝑉𝑉 = 𝑓𝑓(𝐼𝐼1 , 𝐼𝐼2 ) = 𝑧𝑧11 𝐼𝐼1 + 𝑧𝑧12 𝐼𝐼2
                                                       � 1
                                                        𝑉𝑉2 = 𝑓𝑓(𝐼𝐼1 , 𝐼𝐼2 ) = 𝑧𝑧21 𝐼𝐼1 + 𝑧𝑧22 𝐼𝐼2

                                  𝑧𝑧11      𝑧𝑧12
         Dove la matrice è 𝑍𝑍̿ = �𝑧𝑧        𝑧𝑧22 � e tutti gli elementi sono espressi in Ω.
                                       21


    -    Matrice ammettenza:

                                                       𝐼𝐼 = 𝑓𝑓(𝑉𝑉1 , 𝑉𝑉2 ) = 𝑦𝑦11 𝑉𝑉1 + 𝑦𝑦12 𝑉𝑉2
                                                      �1
                                                       𝐼𝐼2 = 𝑓𝑓(𝑉𝑉1 , 𝑉𝑉2 ) = 𝑦𝑦21 𝑉𝑉1 + 𝑦𝑦22 𝑉𝑉2

                                  𝑦𝑦11       𝑦𝑦12
         Dove la matrice è 𝑌𝑌� = �𝑦𝑦         𝑦𝑦22 � e tutti gli elementi sono espressi in 𝑆𝑆 (Siemens).
                                       21
    -    Matrici ibride:

              o    Matrice ibrida h:

                                                     𝑉𝑉 = 𝑓𝑓(𝐼𝐼1 , 𝑉𝑉2 ) = ℎ11 𝐼𝐼1 + ℎ12 𝑉𝑉2
                                                    � 1
                                                     𝐼𝐼2 = 𝑓𝑓(𝐼𝐼1 , 𝑉𝑉2 ) = ℎ21 𝐼𝐼1 + ℎ22 𝑉𝑉2

                                           ℎ [Ω] ℎ12 [. ]
                   Dove la matrice è ℎ� = � 11              �.
                                           ℎ21 [. ] ℎ22 [𝑆𝑆]

              o    Matrice ibrida h:

                                                     𝐼𝐼 = 𝑓𝑓(𝑉𝑉1 , 𝐼𝐼2 ) = 𝑔𝑔11 𝑉𝑉1 + 𝑔𝑔12 𝐼𝐼2
                                                    � 1
                                                     𝑉𝑉2 = 𝑓𝑓(𝑉𝑉1 , 𝐼𝐼2 ) = 𝑔𝑔21 𝑉𝑉1 + 𝑔𝑔22 𝐼𝐼2

                                            𝑔𝑔 [S] 𝑔𝑔12 [. ]
                   Dove la matrice è 𝑔𝑔̿ = � 11                �.
                                            𝑔𝑔21 [. ] 𝑔𝑔22 [Ω]

    -    Matrici a catena:

         Si suppone di avere due blocchi (𝐴𝐴, 𝐵𝐵) identiﬁcati con le matrici generiche ����     ����
                                                                                       𝑚𝑚 𝐴𝐴 ed 𝑚𝑚 𝐵𝐵 .


         Ponendo i due blocchi uno in cascata all’altro si ottiene che 𝑉𝑉2𝐴𝐴 = 𝑉𝑉1𝐵𝐵 e 𝐼𝐼2𝐴𝐴 = −𝐼𝐼1𝐵𝐵 .

                                                                                                � = ����
         Sostituendo le varie formule si ottiene la matrice rappresentativa dell’intera cascata 𝑚𝑚  𝑚𝑚 𝐴𝐴 ����
                                                                                                          𝑚𝑚𝐵𝐵 .

         Le matrici a catena sono dunque utili per rappresentare blocchi in cascata, come dice il nome.

Si possono effettuare passaggi da una matrice ad un’altra partendo dalle equazioni della matrice data e
ricavando (tramite inversioni di formule e sostituzioni) la matrice che si desidera (in base alle variabili
indipendenti che si vogliono avere).


TRIPOLO

I tripoli sono doppi bipoli dove un terminale è destinato all’ingresso, uno all’uscita ed uno come riferimento
comune (un BJT è un tripolo).

Sul terminale comune scorre la somma delle correnti dei terminali di ingresso ed uscita ed è ﬁttiziamente
sdoppiato per ottenere uno pseudo doppio bipolo.

Le matrici descrittive di un tripolo sono quelle dei doppi bipoli, ma adattate:

                                                     𝑚𝑚11      𝑚𝑚12      𝑚𝑚𝑖𝑖      𝑚𝑚𝑟𝑟
                                                𝑚𝑚
                                                � = �𝑚𝑚
                                                         21    𝑚𝑚22 � = �𝑚𝑚𝑓𝑓      𝑚𝑚𝑜𝑜 �

Dove i pedici 𝑟𝑟 ed 𝑓𝑓 degli elementi della matrice signiﬁcano, relativamente, 𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟 e 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓.


Supponendo di avere un tripolo descritto dalla matrice

    -    Ammettenza e di aver collegato ad esso tre componenti esterni 𝑌𝑌1 , 𝑌𝑌2 , 𝑌𝑌3 posti rispettivamente:

              o    𝑌𝑌1 in parallelo alla porta 1 del tripolo
              o    𝑌𝑌2 in parallelo alla porta 2 del tripolo
              o    𝑌𝑌3 tra i morsetti di ingresso e di uscita del tripolo
        Si hanno quindi:

            o    in ingresso, prima di 𝑌𝑌1 , una corrente entrante 𝐼𝐼1′ = 𝐼𝐼1 + 𝑌𝑌1 𝑉𝑉1 + 𝑌𝑌3 (𝑉𝑉1 − 𝑉𝑉2 )
            o    in uscita, dopo di 𝑌𝑌2 , una corrente entrante 𝐼𝐼2′ = 𝐼𝐼2 + 𝑌𝑌2 𝑉𝑉2 − 𝑌𝑌3 (𝑉𝑉1 − 𝑉𝑉2 )

        Sostituendo 𝐼𝐼1 ed 𝐼𝐼2 con le equazioni derivate tramite la matrice descrivente il tripolo, si ottiene la
        matrice ammettenza dell’intero blocco:

                                                   𝑦𝑦𝑖𝑖′   𝑦𝑦𝑟𝑟′      𝑦𝑦𝑖𝑖 + 𝑌𝑌1 + 𝑌𝑌3        𝑦𝑦𝑟𝑟 − 𝑌𝑌3
                                           𝑌𝑌�′ = � ′            � = � 𝑦𝑦 − 𝑌𝑌           𝑦𝑦𝑜𝑜 + 𝑌𝑌2 + 𝑌𝑌3 �
                                                   𝑦𝑦𝑓𝑓    𝑦𝑦𝑜𝑜′            𝑓𝑓    3


        Questo vale solo per la matrice ammettenza!

        Per calcolare immediatamente le componenti:

            o    𝑌𝑌1 in parallelo alla porta 1 viene sommato al termine 𝑦𝑦𝑖𝑖

            o    𝑌𝑌2 in parallelo alla porta 2 viene sommato al termine 𝑦𝑦𝑜𝑜

            o    𝑌𝑌3 tra ingresso e uscita viene sommato agli elementi della diagonale principale (𝑦𝑦𝑖𝑖 ed 𝑦𝑦𝑜𝑜 ) e
                 sottratto in quelli della diagonale secondaria (𝑦𝑦𝑟𝑟 ed 𝑦𝑦𝑓𝑓 )

    -   Impedenza e di aver collegato ad esso tre componenti esterni 𝑍𝑍1 , 𝑍𝑍2 , 𝑍𝑍3 posti rispettivamente:

            o    𝑍𝑍1 in serie al morsetto di ingresso del tripolo (relativo alla porta 1)
            o    𝑍𝑍2 in serie al morsetto di uscita del tripolo (relativo alla porta 2)
            o    𝑍𝑍3 in serie al morsetto di riferimento del tripolo

        Si hanno quindi:

            o    in ingresso, prima di 𝑍𝑍1 , una tensione 𝑉𝑉1′ = 𝑉𝑉1 + 𝑍𝑍1 𝐼𝐼1 + 𝑍𝑍3 (𝐼𝐼1 + 𝐼𝐼2 )
            o    in uscita, dopo di 𝑍𝑍2 , una tensione 𝑉𝑉2′ = 𝑉𝑉2 + 𝑍𝑍2 𝐼𝐼2 + 𝑍𝑍3 (𝐼𝐼1 + 𝐼𝐼2 )

        Sostituendo 𝑉𝑉1 e 𝑉𝑉2 con le equazioni derivate tramite la matrice descrivente il tripolo, si ottiene la
        matrice impedenza dell’intero blocco:

                                                  𝑧𝑧𝑖𝑖′    𝑧𝑧𝑟𝑟′      𝑧𝑧𝑖𝑖 + 𝑍𝑍1 + 𝑍𝑍3        𝑧𝑧𝑟𝑟 + 𝑍𝑍3
                                          𝑍𝑍�′ = � ′             � = � 𝑧𝑧 + 𝑍𝑍           𝑧𝑧𝑜𝑜 + 𝑍𝑍2 + 𝑍𝑍3 �
                                                  𝑧𝑧𝑓𝑓     𝑧𝑧𝑜𝑜′            𝑓𝑓    3


        Questo vale solo per la matrice impedenza!

        Per calcolare immediatamente le componenti:

            o    𝑍𝑍1 in serie alla porta 1 viene sommato al termine 𝑧𝑧𝑖𝑖

            o    𝑍𝑍2 in serie alla porta 2 viene sommato al termine 𝑧𝑧𝑜𝑜

            o    𝑍𝑍3 in serie al terminale di riferimento viene sommato a tutti gli elementi della matrice


LINEARIZZAZIONE DEI TRANSISTOR

Per l’analisi dinamica di BJT e MOSFET si deve passare al dominio dei piccoli segnali in frequenza (TDL) poiché
aventi comportamenti non lineari e con effetti reattivi.

Il BJT è un tripolo  considerato un doppio bipolo sdoppiando ﬁttiziamente un terminale.
Il MOSFET è un quadripolo, ma il Bulk è polarizzato a tensione ﬁssa  diventa un tripolo  doppio bipolo
-   Linearizzazione del diodo:

                                                                       𝑉𝑉𝐷𝐷
    La corrente nel diodo è 𝐼𝐼𝐷𝐷 = 𝐼𝐼𝑆𝑆 �𝑒𝑒 𝑉𝑉𝑡𝑡ℎ − 1�.
    Al piccolo segnale si studia la derivata nel punto di lavoro (𝑄𝑄) sfruttando lo sviluppo di Taylor limitato al
    1° ordine.

    Quindi si ha:

                          𝜕𝜕𝐼𝐼𝐷𝐷
             o   𝑖𝑖𝐷𝐷 =            � 𝑣𝑣𝐷𝐷
                          𝜕𝜕𝑉𝑉𝐷𝐷 𝑄𝑄


                           𝜕𝜕𝐼𝐼𝐷𝐷             𝐼𝐼𝐷𝐷0 +𝐼𝐼𝑆𝑆        1
             o   𝑔𝑔𝐷𝐷 =             � =                     =
                           𝜕𝜕𝑉𝑉𝐷𝐷 𝑄𝑄             𝑉𝑉𝑡𝑡ℎ          𝑟𝑟𝐷𝐷


                          𝜕𝜕𝑄𝑄𝐷𝐷                   𝜕𝜕𝐼𝐼𝐷𝐷
             o   𝐶𝐶𝐷𝐷 =             � = 𝜏𝜏 𝑇𝑇               � = 𝜏𝜏 𝑇𝑇 𝑔𝑔𝐷𝐷  in inversa si ha 𝐶𝐶𝐷𝐷 ≈ 0
                          𝜕𝜕𝑉𝑉𝐷𝐷 𝑄𝑄                𝜕𝜕𝑉𝑉𝐷𝐷 𝑄𝑄


                                       1
             o   𝐶𝐶𝐽𝐽 = 𝐶𝐶𝐽𝐽0                     in diretta si ha 𝐶𝐶𝐽𝐽 ≈ 0
                                       𝑉𝑉𝐷𝐷
                                   �1− 𝜙𝜙 0
                                            𝐽𝐽



-   Linearizzazione del modello Ebers-Moll del BJT:

    Al grande segnale si ha che il BJT npn è descritto dai parametri 𝐼𝐼𝑆𝑆 , 𝛽𝛽𝐹𝐹 (10 ÷ 300), 𝛽𝛽𝑅𝑅 (1 ÷ 3) e dal
    sistema di equazioni:

                                                                  ⎧ 𝐼𝐼𝐸𝐸 = (1 + 𝛽𝛽𝐹𝐹 )𝐼𝐼𝐵𝐵𝐵𝐵 − 𝛽𝛽𝑅𝑅 𝐼𝐼𝐵𝐵𝐵𝐵 = 𝐼𝐼𝑡𝑡 + 𝐼𝐼𝐵𝐵𝐵𝐵
                                                                  ⎪ 𝐼𝐼𝐶𝐶 = 𝛽𝛽𝐹𝐹 𝐼𝐼𝐵𝐵𝐵𝐵 − (1 + 𝛽𝛽𝑅𝑅 )𝐼𝐼𝐵𝐵𝐵𝐵 = 𝐼𝐼𝑡𝑡 − 𝐼𝐼𝐵𝐵𝐵𝐵
                                                                                                              𝑉𝑉
                                                                                                            𝐵𝐵𝐵𝐵         𝑉𝑉
                                                                  ⎨𝐼𝐼 = 𝛽𝛽 𝐼𝐼 − 𝛽𝛽 𝐼𝐼 = 𝐼𝐼 �𝑒𝑒 𝑉𝑉𝐵𝐵𝐵𝐵
                                                                                                 𝑡𝑡ℎ − 𝑒𝑒 𝑉𝑉𝑡𝑡ℎ �
                                                                  ⎪ 𝑡𝑡    𝐹𝐹 𝐵𝐵𝐵𝐵 𝑅𝑅 𝐵𝐵𝐵𝐵 𝑆𝑆
                                                                  ⎩

    Il punto di lavoro è 𝑄𝑄 ≡ �𝑉𝑉𝐵𝐵𝐸𝐸0 , 𝑉𝑉𝐶𝐶𝐵𝐵0 , 𝐼𝐼𝐵𝐵0 , 𝐼𝐼𝐶𝐶0 � e quindi si calcolano i vari parametri differenziali:

             o   Giunzione BE:

                                                                                                           𝑉𝑉𝑡𝑡ℎ
                                                                                         𝑟𝑟𝐵𝐵𝐵𝐵 =
                                                                                                    𝐼𝐼𝐵𝐵𝐸𝐸0 + 𝐼𝐼𝐵𝐵𝐸𝐸𝑆𝑆

                                                                                           𝐶𝐶𝐵𝐵𝐵𝐵 = 𝐶𝐶𝐷𝐷 + 𝐶𝐶𝐽𝐽

             o   Giunzione BC:

                                                                                                           𝑉𝑉𝑡𝑡ℎ
                                                                                         𝑟𝑟𝐵𝐵𝐵𝐵 =
                                                                                                    𝐼𝐼𝐵𝐵𝐶𝐶0 + 𝐼𝐼𝐵𝐵𝐶𝐶𝑆𝑆

                                                                                           𝐶𝐶𝐵𝐵𝐵𝐵 = 𝐶𝐶𝐷𝐷 + 𝐶𝐶𝐽𝐽

    Facendo riferimento alla conﬁgurazione ad E comune (𝐵𝐵 ≡ 𝐼𝐼𝐼𝐼, 𝐶𝐶 ≡ 𝑂𝑂𝑂𝑂𝑂𝑂, 𝐸𝐸 ≡ 𝑅𝑅𝑅𝑅𝑅𝑅, 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐶𝐶𝐶𝐶 ):

                                                                                                            𝑉𝑉𝐶𝐶𝐶𝐶
                                    𝐼𝐼𝑡𝑡 = 𝛽𝛽𝐹𝐹 𝐼𝐼𝐵𝐵𝐵𝐵 (𝑉𝑉𝐵𝐵𝐵𝐵 ) − 𝛽𝛽𝑅𝑅 𝐼𝐼𝐵𝐵𝐵𝐵 (𝑉𝑉𝐵𝐵𝐵𝐵 ) = 𝛽𝛽𝐹𝐹0 �1 +              � 𝐼𝐼 (𝑉𝑉 ) − 𝛽𝛽𝑅𝑅 𝐼𝐼𝐵𝐵𝐵𝐵 (𝑉𝑉𝐵𝐵𝐵𝐵 )
                                                                                                             𝑉𝑉𝐴𝐴 𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵

                                                                                               ⇓

              𝜕𝜕𝐼𝐼𝑡𝑡           𝜕𝜕𝐼𝐼𝑡𝑡           𝜕𝜕𝐼𝐼𝑡𝑡           𝜕𝜕𝐼𝐼𝑡𝑡                       𝜕𝜕𝐼𝐼𝑡𝑡      𝜕𝜕𝐼𝐼𝑡𝑡           𝜕𝜕𝐼𝐼𝑡𝑡
    𝑖𝑖𝑡𝑡 =           � 𝑣𝑣 +           � 𝑣𝑣 =           � 𝑣𝑣 +           � (𝑣𝑣 + 𝑣𝑣𝐸𝐸𝐸𝐸 ) = �         � +         � � 𝑣𝑣 +         � 𝑣𝑣
             𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄 𝐵𝐵𝐵𝐵 𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄 𝐵𝐵𝐵𝐵 𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄 𝐵𝐵𝐵𝐵 𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄 𝐵𝐵𝐵𝐵             𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄 𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄 𝐵𝐵𝐵𝐵 𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄 𝐸𝐸𝐸𝐸
                                                                                          ⇓

                                      𝜕𝜕𝐼𝐼𝑡𝑡          𝜕𝜕𝐼𝐼𝐵𝐵𝐵𝐵          𝜕𝜕𝐼𝐼𝐵𝐵𝐵𝐵          𝜕𝜕𝐼𝐼𝐵𝐵𝐵𝐵     𝛽𝛽𝐹𝐹
                                             � = 𝛽𝛽𝐹𝐹          � − 𝛽𝛽𝑅𝑅          � = 𝛽𝛽𝐹𝐹          � =
                                     𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄      𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄       𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄       𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄 𝑟𝑟𝐵𝐵𝐵𝐵

                                      𝜕𝜕𝐼𝐼𝑡𝑡          𝜕𝜕𝐼𝐼𝐵𝐵𝐵𝐵          𝜕𝜕𝐼𝐼𝐵𝐵𝐵𝐵           𝐼𝐼𝐵𝐵𝐸𝐸  𝛽𝛽𝑅𝑅
                                             � = 𝛽𝛽𝐹𝐹          � − 𝛽𝛽𝑅𝑅          � = −𝛽𝛽𝐹𝐹0 0 −
                                     𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄      𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄       𝜕𝜕𝑉𝑉𝐵𝐵𝐵𝐵 𝑄𝑄          𝑉𝑉𝐴𝐴 𝑟𝑟𝐵𝐵𝐵𝐵

                                                                                          ⇓

                                                       𝛽𝛽𝐹𝐹         𝐼𝐼𝐵𝐵𝐸𝐸  𝛽𝛽𝑅𝑅                   𝐼𝐼𝐵𝐵𝐸𝐸  𝛽𝛽𝑅𝑅
                                           𝑖𝑖𝑡𝑡 = �          − 𝛽𝛽𝐹𝐹0 0 −          � 𝑣𝑣𝐵𝐵𝐵𝐵 + �𝛽𝛽𝐹𝐹0 0 +         � 𝑣𝑣
                                                      𝑟𝑟𝐵𝐵𝐵𝐵          𝑉𝑉𝐴𝐴 𝑟𝑟𝐵𝐵𝐵𝐵                    𝑉𝑉𝐴𝐴 𝑟𝑟𝐵𝐵𝐵𝐵 𝐶𝐶𝐶𝐶

                                                                                          ⇓

                                                                     𝛽𝛽𝐹𝐹             𝐼𝐼𝐵𝐵𝐸𝐸        𝛽𝛽𝑅𝑅
                                                            ⎧𝑔𝑔𝑚𝑚 ≔        + 𝛽𝛽𝐹𝐹0 0 −
                                                            ⎪       𝑟𝑟𝐵𝐵𝐵𝐵              𝑉𝑉𝐴𝐴       𝑟𝑟𝐵𝐵𝐵𝐵
                                                                                𝐼𝐼𝐵𝐵𝐸𝐸0 𝛽𝛽𝑅𝑅
                                                            ⎨ 𝑔𝑔𝐶𝐶𝐶𝐶 ≔ 𝛽𝛽𝐹𝐹0              +
                                                            ⎪                     𝑉𝑉𝐴𝐴       𝑟𝑟𝐵𝐵𝐵𝐵
                                                            ⎩ 𝑖𝑖𝑡𝑡 = 𝑔𝑔𝑚𝑚 𝑣𝑣𝐵𝐵𝐵𝐵 + 𝑔𝑔𝐶𝐶𝐶𝐶 𝑣𝑣𝐶𝐶𝐶𝐶

Si sono ottenuti i parametri differenziali dipendenti dal punto di lavoro 𝑄𝑄: 𝑟𝑟𝐵𝐵𝐵𝐵 , 𝐶𝐶𝐵𝐵𝐵𝐵 , 𝑟𝑟𝐵𝐵𝐵𝐵 , 𝐶𝐶𝐵𝐵𝐵𝐵 , 𝑔𝑔𝑚𝑚 , 𝑔𝑔𝐶𝐶𝐶𝐶 .

Fanno parte del Circuito Equivalente ai Piccoli Segnali (CEPS) del BJT detto di Giacoletto-Johnson.

In regione normale (attiva):

     o    la giunzione BC è in inversa  𝑟𝑟𝐵𝐵𝐵𝐵 → ∞ e 𝐶𝐶𝐵𝐵𝐵𝐵 → 0
                                                                       𝑉𝑉
     o    la giunzione BE è in diretta  𝐼𝐼𝐵𝐵𝐸𝐸0 ≫ 𝐼𝐼𝐵𝐵𝐸𝐸𝑆𝑆 ⇒ 𝑟𝑟𝐵𝐵𝐵𝐵 ≈ 𝑡𝑡ℎ
                                                                                                              𝐼𝐼𝐵𝐵𝐸𝐸0
                                                                                                       𝛽𝛽𝐹𝐹               𝐼𝐼𝐵𝐵𝐸𝐸0            𝐼𝐼𝐵𝐵𝐸𝐸0             𝐼𝐼𝐵𝐵𝐸𝐸0       𝛽𝛽𝐹𝐹
                                                                𝑉𝑉𝐴𝐴 ≫ 𝑉𝑉𝑡𝑡ℎ ⇒ 𝑔𝑔𝑚𝑚 ≈                          − 𝛽𝛽𝐹𝐹0             = 𝛽𝛽𝐹𝐹             − 𝛽𝛽𝐹𝐹0             ≈
                                                                                                       𝑟𝑟𝐵𝐵𝐵𝐵              𝑉𝑉𝐴𝐴              𝑉𝑉𝑡𝑡ℎ                𝑉𝑉𝐴𝐴         𝑟𝑟𝐵𝐵𝐵𝐵
                                                                                                                      ⇓
                                                                                                         𝑔𝑔𝑚𝑚 𝑟𝑟𝐵𝐵𝐵𝐵 = 𝛽𝛽0 ≈ 𝛽𝛽𝐹𝐹

Dove 𝛽𝛽0 è il guadagno di corrente al piccolo segnale.

In regime quasi-stazionario ed in regione normale il tutto si riduce a 3 soli parametri differenziali
(𝑔𝑔𝑚𝑚 , 𝑟𝑟𝐵𝐵𝐵𝐵 , 𝑟𝑟𝐶𝐶𝐶𝐶 ):

     o    𝒻𝒻 dei segnali bassa  effetti reattivi trascurabili

                        𝐼𝐼𝐵𝐵𝐸𝐸0                                                        𝐼𝐼𝐶𝐶0
     o    𝑔𝑔𝑚𝑚 = 𝛽𝛽𝐹𝐹              e 𝐼𝐼𝐶𝐶 = 𝐼𝐼𝑡𝑡 = 𝛽𝛽𝐹𝐹 𝐼𝐼𝐵𝐵𝐵𝐵  𝑔𝑔𝑚𝑚 =
                        𝑉𝑉𝑡𝑡ℎ                                                          𝑉𝑉𝑡𝑡ℎ


                           𝐼𝐼𝐵𝐵𝐸𝐸0       𝛽𝛽𝑅𝑅               𝐼𝐼𝐵𝐵𝐸𝐸0       𝐼𝐼𝐶𝐶0                𝐼𝐼𝐶𝐶0
     o    𝑔𝑔𝐶𝐶𝐶𝐶 = 𝛽𝛽𝐹𝐹0             +            ≈ 𝛽𝛽𝐹𝐹0             ≈            𝑔𝑔𝐶𝐶𝐶𝐶 ≈
                            𝑉𝑉𝐴𝐴         𝑟𝑟𝐵𝐵𝐵𝐵              𝑉𝑉𝐴𝐴         𝑉𝑉𝐴𝐴                 𝑉𝑉𝐴𝐴


     o    𝑔𝑔𝑚𝑚 𝑟𝑟𝐵𝐵𝐵𝐵 = 𝛽𝛽0 e 𝑔𝑔𝑚𝑚 𝑣𝑣𝐵𝐵𝐵𝐵 = 𝑔𝑔𝑚𝑚 𝑟𝑟𝐵𝐵𝐵𝐵 𝑖𝑖𝐵𝐵𝐵𝐵  𝑔𝑔𝑚𝑚 𝑣𝑣𝐵𝐵𝐵𝐵 = 𝛽𝛽0 𝑖𝑖𝐵𝐵𝐵𝐵

     o    se si trascura l’effetto Early  𝑉𝑉𝐴𝐴 → ∞  𝑟𝑟𝐶𝐶𝐶𝐶 → ∞  solo 2 parametri (𝑔𝑔𝑚𝑚 , 𝑟𝑟𝐵𝐵𝐵𝐵 )


Per il BJT pnp il CEPS è identico (il generatore di corrente dipendente è comunque pilotato da 𝑣𝑣𝐵𝐵𝐵𝐵 ).

                                                                                          ⇓

                                         Al piccolo segnale il BJT npn ed il BJT pnp sono identici!
-   Linearizzazione del MOSFET:

    Si prende in considerazione un n-MOSFET il cui comportamento è descritto dalle equazioni:

                                                               𝑉𝑉 2
                       ⎧𝐼𝐼𝐷𝐷𝐷𝐷 = 𝛽𝛽𝑛𝑛 �(𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 )𝑉𝑉𝐷𝐷𝐷𝐷 − 𝐷𝐷𝐷𝐷 � (1 + 𝜆𝜆𝑉𝑉𝐷𝐷𝐷𝐷 ),     𝑉𝑉𝐷𝐷𝐷𝐷 ≤ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇
                       ⎪                                        2
                                 𝛽𝛽𝑛𝑛                 2
                       ⎨ 𝐼𝐼𝐷𝐷𝐷𝐷 = (𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇 ) (1 + 𝜆𝜆𝑉𝑉𝐷𝐷𝐷𝐷 ),         𝑉𝑉𝐷𝐷𝐷𝐷 ≥ 𝑉𝑉𝐺𝐺𝐺𝐺 − 𝑉𝑉𝑇𝑇          𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆
                       ⎪          2
                       ⎩            𝑉𝑉𝑇𝑇 = 𝑉𝑉𝑇𝑇0 + 𝛾𝛾��2𝜓𝜓𝐹𝐹 + 𝑉𝑉𝑆𝑆𝑆𝑆 − �2𝜓𝜓𝐹𝐹 �,             𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸𝐸 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵

    La linearizzazione si esegue quindi rispetto ai potenziali 𝑉𝑉𝐺𝐺 , 𝑉𝑉𝐷𝐷 , 𝑉𝑉𝑆𝑆 :

                                   𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷         𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷         𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷
                        𝑖𝑖𝐷𝐷𝐷𝐷 =            � 𝑣𝑣 +           � 𝑣𝑣 +           � 𝑣𝑣 = 𝑔𝑔𝑚𝑚 𝑣𝑣𝐺𝐺𝐺𝐺 + 𝑔𝑔𝐷𝐷𝐷𝐷 𝑣𝑣𝐷𝐷𝐷𝐷 + 𝑔𝑔𝑚𝑚𝐵𝐵 𝑣𝑣𝑆𝑆𝑆𝑆
                                   𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺 𝑄𝑄 𝐺𝐺𝐺𝐺 𝜕𝜕𝑉𝑉𝐷𝐷𝐷𝐷 𝑄𝑄 𝐷𝐷𝐷𝐷 𝜕𝜕𝑉𝑉𝑆𝑆𝑆𝑆 𝑄𝑄 𝑆𝑆𝑆𝑆

                                                                                      ⇓

                             𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷     𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷 𝜕𝜕𝑉𝑉𝑇𝑇       𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷 𝜕𝜕𝑉𝑉𝑇𝑇                     𝛾𝛾
                  𝑔𝑔𝑚𝑚𝐵𝐵 =            � =         �        � =−         �           � = −𝑔𝑔𝑚𝑚                   = −𝑔𝑔𝑚𝑚 𝛼𝛼
                             𝜕𝜕𝑉𝑉𝑆𝑆𝑆𝑆 𝑄𝑄 𝜕𝜕𝑉𝑉𝑇𝑇 𝑄𝑄 𝜕𝜕𝑉𝑉𝑆𝑆𝑆𝑆 𝑄𝑄  𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺 𝑄𝑄 𝜕𝜕𝑉𝑉𝑆𝑆𝑆𝑆 𝑄𝑄       2�2𝜓𝜓𝐹𝐹 + 𝑉𝑉𝑆𝑆𝐵𝐵0

                                                                                      ⇓

                                                                           𝑔𝑔𝑚𝑚𝐵𝐵 = −𝑔𝑔𝑚𝑚 𝛼𝛼
                                                                                     𝛾𝛾
                                                                        𝛼𝛼 =
                                                                              2�2𝜓𝜓𝐹𝐹 + 𝑉𝑉𝑆𝑆𝐵𝐵0

    Per gli altri parametri differenziali si ha:

         o    In TRIODO:

                                    𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷
                        𝑔𝑔𝑚𝑚 =                � = 𝛽𝛽𝑛𝑛 �1 + 𝜆𝜆𝑉𝑉𝐷𝐷𝑆𝑆0 �𝑉𝑉𝐷𝐷𝑆𝑆0
                                    𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺 𝑄𝑄
                                     𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷                                                              𝜆𝜆𝐼𝐼𝐷𝐷𝑆𝑆0
                        𝑔𝑔𝐷𝐷𝐷𝐷 =               � = 𝛽𝛽𝑛𝑛 �𝑉𝑉𝐺𝐺𝑆𝑆0 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉𝐷𝐷𝑆𝑆0 ��1 + 𝜆𝜆𝑉𝑉𝐷𝐷𝑆𝑆0 � +
                                     𝜕𝜕𝑉𝑉𝐷𝐷𝐷𝐷 𝑄𝑄                                                         1+𝜆𝜆𝑉𝑉𝐷𝐷𝑆𝑆0


         o    In SATURAZIONE:

                                    𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷
                        𝑔𝑔𝑚𝑚 =                � = 𝛽𝛽𝑛𝑛 (𝑉𝑉𝐺𝐺𝑆𝑆0 − 𝑉𝑉𝑇𝑇 )�1 + 𝜆𝜆𝑉𝑉𝐷𝐷𝑆𝑆0 �
                                    𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺 𝑄𝑄
                                     𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷          𝛽𝛽𝑛𝑛                   2           𝜆𝜆𝐼𝐼𝐷𝐷𝑆𝑆0
                        𝑔𝑔𝐷𝐷𝐷𝐷 =               � =           𝜆𝜆�𝑉𝑉𝐺𝐺𝑆𝑆0 − 𝑉𝑉𝑇𝑇 � =
                                     𝜕𝜕𝑉𝑉𝐷𝐷𝐷𝐷 𝑄𝑄        2                             1+𝜆𝜆𝑉𝑉𝐷𝐷𝑆𝑆0


    Se si pone 𝑣𝑣𝑆𝑆𝑆𝑆 = 0 non si ha il generatore di corrente pilotato 𝑔𝑔𝑚𝑚𝐵𝐵 𝑣𝑣𝑆𝑆𝑆𝑆 .
    Se inoltre non si considera l’ELMC (𝜆𝜆 = 0) si ha:

         o    In TRIODO:

                                    𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷
                        𝑔𝑔𝑚𝑚 =                � = 𝛽𝛽𝑛𝑛 𝑉𝑉𝐷𝐷𝑆𝑆0
                                    𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺 𝑄𝑄
                                     𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷
                        𝑔𝑔𝐷𝐷𝐷𝐷 =               � = 𝛽𝛽𝑛𝑛 �𝑉𝑉𝐺𝐺𝑆𝑆0 − 𝑉𝑉𝑇𝑇 − 𝑉𝑉𝐷𝐷𝑆𝑆0 �
                                     𝜕𝜕𝑉𝑉𝐷𝐷𝐷𝐷 𝑄𝑄


         o    In SATURAZIONE:

                                    𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷
                        𝑔𝑔𝑚𝑚 =                � = 𝛽𝛽𝑛𝑛 �𝑉𝑉𝐺𝐺𝑆𝑆0 − 𝑉𝑉𝑇𝑇 � = �2𝛽𝛽𝑛𝑛 𝐼𝐼𝐷𝐷𝑆𝑆0
                                    𝜕𝜕𝑉𝑉𝐺𝐺𝐺𝐺 𝑄𝑄
                                     𝜕𝜕𝐼𝐼𝐷𝐷𝐷𝐷
                        𝑔𝑔𝐷𝐷𝐷𝐷 =               � = 0  MOLTO BENE!
                                     𝜕𝜕𝑉𝑉𝐷𝐷𝐷𝐷 𝑄𝑄
          Per quanto riguarda gli effetti reattivi del MOSFET si ha:

                o          𝐶𝐶𝐺𝐺𝐺𝐺 e 𝐶𝐶𝐺𝐺𝐺𝐺 sono comprese nella 𝐶𝐶𝐺𝐺 e 𝐶𝐶𝐺𝐺𝐺𝐺 = 0 se MOSFET ON
                o          Con 𝑉𝑉𝑆𝑆𝑆𝑆 = 0  𝐶𝐶𝑆𝑆𝑆𝑆 è cortocircuitata
                o          𝐶𝐶𝐺𝐺𝐺𝐺 e 𝐶𝐶𝐷𝐷𝐷𝐷

          Per il p-MOSFET il CEPS è identico (generatori di corrente dipendente comunque pilotato da 𝑣𝑣𝐺𝐺𝐺𝐺 e 𝑣𝑣𝑆𝑆𝑆𝑆 ).

                                                                                    ⇓

                                             Al piccolo segnale n-MOSFET e p-MOSFET sono identici!
                                             Le equazioni sono le stesse, ma col valore assoluto per le tensioni!


CONFRONTO BJT-MOSFET

Per entrambi i transistor si ha che il CEPS si interfaccia all’uscita con un generatore di corrente pilotato da 𝑔𝑔𝑚𝑚 ,
che ha il compito di regolare il trasferimento di segnale dalla porta IN alla porta OUT (è l’elemento 𝑦𝑦21 ≡ 𝑦𝑦𝑓𝑓 di 𝑌𝑌�).

                                                                                  𝐼𝐼𝐶𝐶0
Per il BJT in attiva e regime quasi-stazionario si ha 𝑔𝑔𝑚𝑚𝐵𝐵𝐵𝐵𝐵𝐵 =                         𝑔𝑔𝑚𝑚𝐵𝐵𝐵𝐵𝐵𝐵 ∝ 𝐼𝐼𝐶𝐶0 , mentre per il MOSFET in
                                                                                  𝑉𝑉𝑡𝑡ℎ
saturazione si ha 𝑔𝑔𝑚𝑚𝑀𝑀𝑀𝑀𝑀𝑀 = �2𝛽𝛽𝑛𝑛 𝐼𝐼𝐷𝐷𝐷𝐷 0  𝑔𝑔𝑚𝑚𝑀𝑀𝑀𝑀𝑀𝑀 ∝ �𝐼𝐼𝐷𝐷𝑆𝑆0 .

Queste proporzionalità indicano che 𝑔𝑔𝑚𝑚𝐵𝐵𝐵𝐵𝐵𝐵 > 𝑔𝑔𝑚𝑚𝑀𝑀𝑀𝑀𝑀𝑀 a parità di corrente  BJT migliore del MOSFET per
                                                                                   applicazioni analogiche, ma c’è
                                                                                   consumo di corrente a causa di 𝐼𝐼𝐵𝐵

Per avere una 𝑔𝑔𝑚𝑚𝑀𝑀𝑀𝑀𝑀𝑀 maggiore, e compensare lo svantaggio, si deve usare il MOSFET in sottosoglia (𝑉𝑉𝐺𝐺𝐺𝐺
leggermente inferiore a 𝑉𝑉𝑇𝑇 ), dove il MOSFET è OFF, ma c’è comunque della carica di canale che consente di
avere una corrente.
                                                                                                                               𝐼𝐼𝐷𝐷𝑆𝑆0
Diventa un modello complesso che però fa sì che 𝐼𝐼𝐷𝐷𝐷𝐷 ∝ 𝑒𝑒 𝑉𝑉𝐺𝐺𝐺𝐺 ottenendo quindi 𝑔𝑔𝑚𝑚𝑀𝑀𝑀𝑀𝑀𝑀 =                                         .
                                                                                                                               𝑉𝑉𝑡𝑡ℎ




FUNZIONI DI RETE DEL BJT

Il CEPS del BJT è un circuito a 𝜋𝜋 ed in regione attiva (𝑟𝑟𝐶𝐶𝐶𝐶 = ∞) si può sintetizzare con la matrice ammettenza:

                                                                     1
                                                                  ⎡       + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵 + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵       −𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵 ⎤
                                                  𝑦𝑦𝑖𝑖   𝑦𝑦𝑟𝑟      𝑟𝑟
                                           𝑌𝑌� = �𝑦𝑦              ⎢  𝐵𝐵𝐵𝐵                                           ⎥
                                                    𝑓𝑓   𝑦𝑦𝑜𝑜 � = ⎢                                 1
                                                                          𝑔𝑔𝑚𝑚 − 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵                + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵 ⎥
                                                                  ⎣                               𝑟𝑟𝐶𝐶𝐶𝐶            ⎦

Per capire meglio come si è ottenuta questa matrice, si considera il generatore di corrente comandato in
tensione 𝑔𝑔𝑚𝑚 𝑣𝑣𝐵𝐵𝐵𝐵 come tripolo e si assegnano:

                    1
     -    𝑌𝑌1 ≡            + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵
                  𝑟𝑟𝐵𝐵𝐵𝐵
                    1
     -    𝑌𝑌2 ≡
                  𝑟𝑟𝐶𝐶𝐶𝐶
     -    𝑌𝑌3 ≡ 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵

Da qui si costruisce la matrice come nel caso descritto nel paragrafo TRIPOLO.

Si considera l’impedenza di ingresso del BJT per studiarne poi il comportamento in frequenza nel caso di utilizzo
come ampliﬁcatore di tensione.
                                                                                   1
Ipotizzando un funzionamento a vuoto del BJT (ampliﬁcatore di tensione)  𝑌𝑌𝐶𝐶 = = 0 si ha che:
                                                                                                                        𝑍𝑍𝐶𝐶
                                                                     𝑦𝑦𝑟𝑟 𝑦𝑦𝑓𝑓          𝑦𝑦𝑟𝑟 𝑦𝑦𝑓𝑓 𝑦𝑦𝑖𝑖 𝑦𝑦𝑜𝑜 − 𝑦𝑦𝑟𝑟 𝑦𝑦𝑓𝑓 𝐷𝐷𝑌𝑌
                                              𝑌𝑌𝐼𝐼𝐼𝐼 = 𝑦𝑦𝑖𝑖 −                  = 𝑦𝑦𝑖𝑖 −          =                     =
                                                                  𝑌𝑌𝐶𝐶 + 𝑦𝑦𝑜𝑜             𝑦𝑦𝑜𝑜              𝑦𝑦𝑜𝑜         𝑦𝑦𝑜𝑜
                                                                                      ⇓

                                                                                                1      𝑦𝑦𝑜𝑜
                                                                                   𝑍𝑍𝐼𝐼𝐼𝐼 =          =
                                                                                               𝑌𝑌𝐼𝐼𝐼𝐼 𝐷𝐷𝑌𝑌

Che dipende da 𝑠𝑠 sia al numeratore che al denominatore, ma se 𝑦𝑦𝑟𝑟 è piccolo (è unilatero)  𝐷𝐷𝑌𝑌 = 𝑦𝑦𝑖𝑖 𝑦𝑦𝑜𝑜 e

                                                        1                  1                             𝑟𝑟𝐵𝐵𝐵𝐵
                                            𝑍𝑍𝐼𝐼𝐼𝐼 ≈        =                              =
                                                       𝑦𝑦𝑖𝑖     1                            1 + 𝑠𝑠𝑟𝑟𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵 + 𝐶𝐶𝐵𝐵𝐵𝐵 )
                                                                                                         (𝐶𝐶
                                                                     + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵 + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵
                                                              𝑟𝑟𝐵𝐵𝐵𝐵
                                                                                  1
Da cui si ricava un polo a pulsazione 𝑝𝑝 = −                                                     per 𝒻𝒻 ↑ ⇒ 𝑍𝑍𝐼𝐼𝐼𝐼 ↓.
                                                                    𝑟𝑟𝐵𝐵𝐵𝐵 (𝐶𝐶𝐵𝐵𝐵𝐵 +𝐶𝐶𝐵𝐵𝐵𝐵 )
Maggiore assorbimento di corrente ad alte frequenze (non bene per ampliﬁcatori di tensione).


Si considera l’impedenza di uscita del BJT per studiarne poi il comportamento in frequenza nel caso di utilizzo
come ampliﬁcatore di corrente.
Ipotizzando un generatore ideale di corrente in ingresso al BJT (ampliﬁcatore di tensione)  𝑌𝑌𝐺𝐺 = 0 si ha che:

                                                                                        𝑦𝑦𝑟𝑟 𝑦𝑦𝑓𝑓          𝑦𝑦𝑟𝑟 𝑦𝑦𝑓𝑓 𝐷𝐷𝑌𝑌
                                                          𝑌𝑌𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑦𝑦𝑜𝑜 −                       = 𝑦𝑦𝑜𝑜 −          =
                                                                                      𝑦𝑦𝑖𝑖 + 𝑌𝑌𝐺𝐺            𝑦𝑦𝑖𝑖     𝑦𝑦𝑖𝑖

                                                                                               ⇓

                                                                                                 1            𝑦𝑦𝑖𝑖
                                                                                 𝑍𝑍𝑂𝑂𝑂𝑂𝑂𝑂 =               =
                                                                                               𝑌𝑌𝑂𝑂𝑂𝑂𝑂𝑂       𝐷𝐷𝑌𝑌

Che dipende da 𝑠𝑠 sia al numeratore che al denominatore, ma se 𝑦𝑦𝑟𝑟 è piccolo (è unilatero)  𝐷𝐷𝑌𝑌 = 𝑦𝑦𝑖𝑖 𝑦𝑦𝑜𝑜 e

                                                                         1             1                𝑟𝑟𝐶𝐶𝐶𝐶
                                                          𝑍𝑍𝑂𝑂𝑂𝑂𝑂𝑂 ≈         =                   =
                                                                        𝑦𝑦𝑜𝑜     1                 1 + 𝑠𝑠𝑟𝑟 𝐶𝐶𝐶𝐶 𝐶𝐶𝐵𝐵𝐵𝐵
                                                                                      + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵
                                                                               𝑟𝑟𝐶𝐶𝐶𝐶

                                                                             1
Da cui si ricava un polo a pulsazione 𝑝𝑝 = −                                           per 𝒻𝒻 ↑ ⇒ 𝑍𝑍𝑂𝑂𝑂𝑂𝑂𝑂 ↓.
                                                                    𝑟𝑟𝐵𝐵𝐵𝐵 𝐶𝐶𝐵𝐵𝐵𝐵
Maggiore erogazione di corrente ad alte frequenze (ottimo per ampliﬁcatori di corrente).

Il BJT è quindi un buon ampliﬁcatore di corrente in regione attiva poiché 𝐼𝐼𝐶𝐶 = 𝛽𝛽𝐹𝐹 𝐼𝐼𝐵𝐵 .

Considerando 𝑌𝑌𝐶𝐶 = ∞  𝑍𝑍𝐶𝐶 = 0 si ottiene il guadagno di corrente di cortocircuito:

                                                                                                                                                 𝑟𝑟 𝐶𝐶
                  𝑦𝑦𝑓𝑓          𝑔𝑔𝑚𝑚 − 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵           𝑔𝑔𝑚𝑚 𝑟𝑟𝐵𝐵𝐵𝐵 − 𝑠𝑠𝑟𝑟𝐵𝐵𝐵𝐵 𝐶𝐶𝐵𝐵𝐵𝐵          𝛽𝛽0 − 𝑠𝑠𝑟𝑟𝐵𝐵𝐵𝐵 𝐶𝐶𝐵𝐵𝐵𝐵                  1 − 𝑠𝑠 𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵
                                                                                                                                                    𝛽𝛽0
       𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 =      =                              =                                    =                                  = 𝛽𝛽0
                  𝑦𝑦𝑖𝑖     1                            1 +  𝑠𝑠𝑟𝑟     (𝐶𝐶    +    𝐶𝐶     )   1 +  𝑠𝑠𝑟𝑟    (𝐶𝐶    +   𝐶𝐶     )       1 + 𝑠𝑠𝑟𝑟𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵 + 𝐶𝐶𝐵𝐵𝐵𝐵 )
                                                                                                                                                (𝐶𝐶
                                + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵 + 𝑠𝑠𝐶𝐶𝐵𝐵𝐵𝐵             𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵         𝐵𝐵𝐵𝐵              𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵        𝐵𝐵𝐵𝐵
                         𝑟𝑟𝐵𝐵𝐵𝐵

                                                                 𝛽𝛽0                                                            1
L’espressione presenta uno zero in 𝑧𝑧 =                                      ed un polo in 𝑝𝑝 = −                                               .
                                                             𝑟𝑟𝐵𝐵𝐵𝐵 𝐶𝐶𝐵𝐵𝐵𝐵                                           𝑟𝑟𝐵𝐵𝐵𝐵 (𝐶𝐶𝐵𝐵𝐵𝐵 +𝐶𝐶𝐵𝐵𝐵𝐵 )

                              |𝑧𝑧|               𝐶𝐶
Da cui si ricava che |𝑝𝑝| = 𝛽𝛽0 �1 + 𝐵𝐵𝐵𝐵� ≫ 1  |𝑧𝑧| ≫ |𝑝𝑝|.
                                                 𝐶𝐶𝐵𝐵𝐵𝐵


Il modello di Ebers-Moll però non è realistico ad alte 𝒻𝒻 e la stima di 𝑧𝑧 non è affidabile.

Per il calcolo della pulsazione di taglio 𝜔𝜔𝐵𝐵 (dove il valore di guadagno è �𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶                                                              � − 3 𝑑𝑑𝑑𝑑, nonché quando
                                                                                                                                         𝑀𝑀𝑀𝑀𝑀𝑀
                1
�𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 � =       ) si deve calcolare il modulo del guadagno di corrente di cortocircuito ponendo 𝑠𝑠 = 𝑗𝑗𝑗𝑗:
                √2
                                                                                       𝑟𝑟 𝐶𝐶
                                                                           1 − 𝑗𝑗𝑗𝑗 𝐵𝐵𝐵𝐵 𝐵𝐵𝐵𝐵
                                                                                           𝛽𝛽0
                                             �𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 (𝑗𝑗𝑗𝑗)� = 𝛽𝛽0 �                                   �
                                                                       1 + 𝑗𝑗𝑗𝑗𝑟𝑟𝐵𝐵𝐵𝐵 (𝐶𝐶𝐵𝐵𝐵𝐵 + 𝐶𝐶𝐵𝐵𝐵𝐵 )


Essendo che |𝑧𝑧| ≫ |𝑝𝑝|  si presenta prima il polo, che provoca un’attenuazione del guadagno.

La pulsazione del polo deﬁnisce anche la banda passante, e per questo viene anche detta

                                                                                           1
                                                          𝜔𝜔𝐵𝐵 = |𝑝𝑝| =
                                                                              𝑟𝑟𝐵𝐵𝐵𝐵 (𝐶𝐶𝐵𝐵𝐵𝐵 + 𝐶𝐶𝐵𝐵𝐵𝐵 )

Nella banda passante si ha �𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 � = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 e si possono trascurare gli effetti reattivi giungendo ad un
                                                                                                 𝜔𝜔
comportamento quasi-stazionario  funzioni di rete indipendenti da 𝒻𝒻 ﬁno a 𝒻𝒻𝐵𝐵 = 𝐵𝐵.
                                                                                                                               2𝜋𝜋


Si deﬁnisce anche la pulsazione di cut-off 𝜔𝜔 𝑇𝑇 , ossia quella per la quale si ha �𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 � = 1.

Per il relativo calcolo si trascura l’effetto dello zero e si ottiene:

                                                          𝛽𝛽0                                    𝛽𝛽0
                                𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 (𝑗𝑗𝑗𝑗) ≈           𝜔𝜔 ⇒ �𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 (𝑗𝑗𝜔𝜔 𝑇𝑇 )� = 1 =
                                                    1 + 𝑗𝑗                                          𝜔𝜔 2
                                                           𝜔𝜔𝐵𝐵                              �1 + � 𝑇𝑇 �
                                                                                                    𝜔𝜔               𝐵𝐵
                                                                                ⇓

                                                                                          𝑔𝑔𝑚𝑚
                                                           𝜔𝜔 𝑇𝑇 ≈ 𝛽𝛽0 𝜔𝜔𝐵𝐵 =
                                                                                    𝐶𝐶𝐵𝐵𝐵𝐵 + 𝐶𝐶𝐵𝐵𝐵𝐵

Detto prodotto banda-guadagno.


FUNZIONI DI RETE DEL MOSFET

La matrice ammettenza che si ottiene dal CEPS del MOSFET è:

                                                𝑦𝑦𝑖𝑖       𝑦𝑦𝑟𝑟      𝑠𝑠(𝐶𝐶𝐺𝐺𝐺𝐺 + 𝐶𝐶𝐺𝐺𝐺𝐺 )     −𝑠𝑠𝐶𝐶𝐺𝐺𝐺𝐺
                                         𝑌𝑌� = �𝑦𝑦         𝑦𝑦𝑜𝑜 � = � 𝑔𝑔𝑚𝑚 − 𝑠𝑠𝐶𝐶𝐺𝐺𝐺𝐺                       �
                                                     𝑓𝑓                                   𝑔𝑔𝐷𝐷𝐷𝐷 + 𝑠𝑠𝐶𝐶𝐺𝐺𝐺𝐺

Il guadagno di corrente di cortocircuito è:

                                                                                               𝐶𝐶
                                                   𝑦𝑦𝑓𝑓   𝑔𝑔𝑚𝑚 − 𝑠𝑠𝐶𝐶𝐺𝐺𝐺𝐺              1 − 𝑠𝑠 𝐺𝐺𝐺𝐺
                                                                                               𝑔𝑔𝑚𝑚
                                        𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 =      =                    = 𝑔𝑔𝑚𝑚
                                                   𝑦𝑦𝑖𝑖 𝑠𝑠(𝐶𝐶𝐺𝐺𝐺𝐺 + 𝐶𝐶𝐺𝐺𝐺𝐺 )        𝑠𝑠(𝐶𝐶𝐺𝐺𝐺𝐺 + 𝐶𝐶𝐺𝐺𝐺𝐺 )

Quindi un polo nell’origine ed uno zero ad alte 𝒻𝒻 il quale, se si trascura l’effetto, porta ad avere:

                                                                                     𝑔𝑔𝑚𝑚
                                                                𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 ≈
                                                                             𝑠𝑠(𝐶𝐶𝐺𝐺𝐺𝐺 + 𝐶𝐶𝐺𝐺𝐺𝐺 )

Il modulo per 𝑠𝑠 = 𝑗𝑗𝑗𝑗 risulta essere:

                                                                                        𝑔𝑔𝑚𝑚
                                                          �𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 (𝑗𝑗𝑗𝑗)� ≈
                                                                                 𝜔𝜔(𝐶𝐶𝐺𝐺𝐺𝐺 + 𝐶𝐶𝐺𝐺𝐺𝐺 )
                                                                                                              𝑔𝑔𝑚𝑚
La pulsazione di cut-off (o di taglio) si ha per �𝐴𝐴𝐼𝐼𝐶𝐶𝐶𝐶 (𝑗𝑗𝑗𝑗)� = 1 e quindi 𝜔𝜔 𝑇𝑇 =                                    .
                                                                                                          𝐶𝐶𝐺𝐺𝐺𝐺 +𝐶𝐶𝐺𝐺𝐺𝐺


Si nota che 𝜔𝜔 𝑇𝑇𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀 ≪ 𝜔𝜔 𝑇𝑇𝐵𝐵𝐵𝐵𝐵𝐵  BJT sono molto più veloci dei MOSFET.
Questo si somma al fatto che 𝜔𝜔 𝑇𝑇𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀 dipende dal punto di lavoro e quindi da �𝐼𝐼𝐷𝐷𝑆𝑆0 , mentre 𝜔𝜔 𝑇𝑇𝐵𝐵𝐵𝐵𝐵𝐵 no (dipende
dalla larghezza della base e quindi dal reciproco di 𝜏𝜏𝐹𝐹  𝜏𝜏𝐹𝐹 ↓ ⇒ 𝜔𝜔 𝑇𝑇 ↑ ⇒ maggiore velocità).
GUADAGNO DI TENSIONE DELL’INVERTER CMOS

                                                                                    𝑑𝑑𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂                                               𝑣𝑣
Il guadagno di tensione è deﬁnito come 𝐴𝐴𝑉𝑉 =                                                    e linearizzando si ha 𝐴𝐴𝑉𝑉 = 𝑂𝑂𝑂𝑂𝑂𝑂.
                                                                                     𝑑𝑑𝑉𝑉𝐼𝐼𝐼𝐼                                                 𝑣𝑣𝐼𝐼𝐼𝐼


Per l’inverter CMOS, dal CEPS si ottiene che:

                                                                                                      𝑔𝑔𝑚𝑚𝑛𝑛 + 𝑔𝑔𝑚𝑚𝑝𝑝
                                                                                         𝐴𝐴𝑉𝑉 = −
                                                                                                      𝑔𝑔𝐷𝐷𝑆𝑆𝑛𝑛 + 𝑔𝑔𝐷𝐷𝑆𝑆𝑝𝑝

Se poi ci si pone nella condizione di 𝑉𝑉𝐼𝐼𝐼𝐼 = 𝑉𝑉𝐿𝐿𝐿𝐿 = 𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 (entrambi i MOSFET in saturazione) si ottiene che:

                                                                                    𝑔𝑔𝑚𝑚𝑛𝑛 + 𝑔𝑔𝑚𝑚𝑝𝑝                          2(2 + 𝜆𝜆𝑉𝑉𝐷𝐷𝐷𝐷 )
                                                            𝐴𝐴𝑉𝑉 |𝑉𝑉𝐿𝐿𝐿𝐿 = −                              �            =−
                                                                                   𝑔𝑔𝐷𝐷𝑆𝑆𝑛𝑛 + 𝑔𝑔𝐷𝐷𝑆𝑆𝑝𝑝                      𝜆𝜆(𝑉𝑉𝐷𝐷𝐷𝐷 − 2𝑉𝑉𝑇𝑇 )
                                                                                                              𝑉𝑉𝐿𝐿𝐿𝐿


Con 𝑉𝑉𝑇𝑇𝑛𝑛 = 𝑉𝑉𝑇𝑇𝑝𝑝 , 𝜆𝜆𝑛𝑛 = 𝜆𝜆𝑝𝑝 = 𝜆𝜆, 𝛽𝛽𝑛𝑛 = 𝛽𝛽𝑝𝑝 = 𝛽𝛽.

Se 𝜆𝜆 = 0  𝐴𝐴𝑉𝑉 |𝑉𝑉𝐿𝐿𝐿𝐿 = ∞.


AMPLIFICATORI ELEMENTARI

Per lo studio al piccolo segnale degli ampliﬁcatori elementari si seguono i seguenti step:

     1) Calcolo del punto di lavoro 𝑄𝑄 dell’ampliﬁcatore

     2) Linearizzazione del circuito e del CEPS

     3) Calcolo dei parametri differenziali del CEPS

     4) Estrazione della matrice descrittiva del CEPS

     5) Calcolo delle funzioni di rete (se ci sono effetti reattivi in 𝒻𝒻 tramite la TDL, sennò nel dominio del tempo):

                               𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 (𝑠𝑠)           𝑣𝑣       (𝑡𝑡)
                 a. 𝐴𝐴𝑉𝑉 =                     = 𝑂𝑂𝑂𝑂𝑂𝑂(𝑡𝑡)  guadagno di tensione
                                 𝑉𝑉𝐼𝐼𝐼𝐼 (𝑠𝑠)           𝑣𝑣𝐼𝐼𝐼𝐼
                              𝐼𝐼𝑂𝑂𝑂𝑂𝑂𝑂 (𝑠𝑠)        𝑖𝑖𝑂𝑂𝑂𝑂𝑂𝑂 (𝑡𝑡)
                 b. 𝐴𝐴𝐼𝐼 =                     =                    guadagno di corrente
                               𝐼𝐼𝐼𝐼𝐼𝐼 (𝑠𝑠)          𝑖𝑖𝐼𝐼𝐼𝐼 (𝑡𝑡)
                                𝑉𝑉𝐼𝐼𝐼𝐼 (𝑠𝑠)        𝑣𝑣𝐼𝐼𝐼𝐼 (𝑡𝑡)
                 c. 𝑍𝑍𝐼𝐼𝐼𝐼 =                   =                   impedenza di ingresso
                                𝐼𝐼𝐼𝐼𝐼𝐼 (𝑠𝑠)       𝑖𝑖𝐼𝐼𝐼𝐼 (𝑡𝑡)
                                    𝑉𝑉𝑂𝑂𝑂𝑂𝑂𝑂 (𝑠𝑠)                      𝑣𝑣         (𝑡𝑡)
                 d. 𝑍𝑍𝑂𝑂𝑂𝑂𝑂𝑂 =                     �               = 𝑂𝑂𝑂𝑂𝑂𝑂(𝑡𝑡) �                     impedenza di uscita (calcolare col segnale di IN spento)
                                    𝐼𝐼𝑂𝑂𝑂𝑂𝑂𝑂 (𝑠𝑠) 𝒮𝒮                   𝑖𝑖𝑂𝑂𝑂𝑂𝑂𝑂
                                                        𝐼𝐼𝐼𝐼 =0                          𝒮𝒮𝐼𝐼𝐼𝐼 =0


Gli ampliﬁcatori elementari con BJT sono i seguenti:

(GLI EFFETTI REATTIVI SONO SEMPRE STATI TRASCURATI  dominio 𝑡𝑡; BJT npn sempre ipotizzato in zona attiva)

     -     BJT connesso a diodo

     -     Specchio di corrente a BJT npn (no effetto Early)

     -     BJT ad emettitore comune  essendo che 𝑍𝑍_𝐼𝐼𝐼𝐼 e 𝑍𝑍𝑂𝑂𝑂𝑂𝑂𝑂 non sono ideali si usa come buffer

     -     BJT a collettore comune  non è invertente, 𝐴𝐴𝑉𝑉 ≈ 1 e 𝑍𝑍_𝐼𝐼𝐼𝐼 e 𝑍𝑍𝑂𝑂𝑂𝑂𝑂𝑂 sono vicine a quelle ideali  buffer
           (particolare utilità se inserito prima e dopo un BJT E.C. ottenendo catena di ampliﬁcazione)

     -     BJT a base comune  molto simile al E.C., ma non invertente, funziona meglio ad altissime 𝒻𝒻 perché ha
                               maggiore banda passante
    -    BJT a Darlington  migliora i parametri differenziali e quindi le funzioni di rete

    -    BJT a doppio carico (D.C.)  unisce BJT E.C. e BJT C.C. e crea un ampliﬁcatore retro azionato
                                      migliora 𝑍𝑍𝐼𝐼𝐼𝐼
                                      cala 𝐴𝐴𝑉𝑉 che però può essere indipendente dal BJT
                                      la retroazione tramite 𝑅𝑅𝐸𝐸 conferisce maggiore stabilità al punto di lavoro 𝑄𝑄

    -    Carico attivo  si usa per svincolare le funzioni di rete dal punto di lavoro del sistema;
                         E’ estremamente utile perché prendendo in considerazione un BJT ad E.C., un carico
                         troppo oneroso farebbe calare 𝐴𝐴𝑉𝑉 ;
                         Un esempio è un generatore di corrente che si realizza tramite uno specchio di corrente
                         a BJT pnp che vede al collettore del BJT dal lato del carico un BJT npn;

L’impatto di un carico a valle di un ampliﬁcatore fa si che il punto di lavoro venga modiﬁcato e così anche le
funzioni di rete.

Essendo che è impossibile ricalcolare 𝑄𝑄 per ogni possibile carico, si introducono dei condensatori di
disaccoppiamento che lo rendono molto più stabile.
Questi condensatori hanno solitamente valori di capacità molto alti in modo da rendere la loro impedenza
trascurabile (rispetto al carico) già a bassissime frequenze.
Ciò fa sì che, in banda passante, la capacità di disaccoppiamento sia un cortocircuito, mentre quelle del BJT
siano un circuito aperto.

L’unico caso per il quale gli effetti reattivi e le capacità di disaccoppiamento sono rilevanti è per il calcolo delle
frequenze di taglio (che risultano essere 2, una ad alta pulsazione 𝜔𝜔𝐻𝐻 ed una a bassa pulsazione 𝜔𝜔𝐿𝐿 ) che
determinano la panda passante dell’ampliﬁcatore (che è quindi un passa banda poiché la capacità limita il
guadagno a basse frequenze).

Oltre alle capacità di disaccoppiamento si introducono anche le capacità di by-pass che sono utili ad alte 𝒻𝒻
poiché cortocircuitano le resistenze poste in parallelo ad esse.


Gli ampliﬁcatori elementari con MOSFET sono i seguenti:

(GLI EFFETTI REATTIVI SONO SEMPRE STATI TRASCURATI  dominio 𝑡𝑡; 𝑉𝑉𝑆𝑆𝑆𝑆 = 0)

    -    MOSFET a Source comune  in saturazione prestazioni simili al BJT ad E.C., ma 𝑍𝑍𝐼𝐼𝐼𝐼 ↑ e 𝑔𝑔𝑚𝑚 ↓

    -    MOSFET a Drain comune  in saturazione prestazioni simili al BJT ad C.C., ma 𝑍𝑍𝐼𝐼𝐼𝐼 = ∞ (BENE) e 𝑔𝑔𝑚𝑚 ↓

    -    MOSFET a Gate comune  in saturazione prestazioni simili al BJT ad B.C., ma non invertente, 𝑍𝑍𝐼𝐼𝐼𝐼 bassa
INVERTER CMOS:

E’ la porta logica più semplice che si possa realizzare ed è composta da un n-MOSFET e da un p-MOSFET.

Se

     -     p-MOSFET conduce (n-MOSFET OFF)  1 logico
     -     n-MOSFET conduce (p-MOSFET OFF)  0 logico


PORTE LOGICHE A CMOS

Lo schema di connessione può essere generalizzato ad ogni funzione logica 𝐹𝐹(𝐼𝐼1 , 𝐼𝐼2 , … , 𝐼𝐼𝑛𝑛 ) come segue:

     1) rete di pull-up (PU)  connette l’uscita a tensione di alimentazione ed è responsabile di generare 𝐹𝐹 = 1

     2) rete di pull-down (PD)  connette l’uscita a tensione di massa ed è responsabile di generare 𝐹𝐹 = 0


PU e PD devono essere complementari e quindi si usano p-MOSFET per realizzare la rete di PU, mentre gli n-
MOSFET per realizzare quella di PD.

Queste porte logiche sono dette statiche poiché il comportamento statico del circuito ne determina il
funzionamento.

Quindi nelle porte a CMOS:

     -     PU realizzato con p-MOSFET

     -     PD realizzato con n-MOSFET

     -     gli ingressi pilotano solo i Gate dei MOSFET

     -     MOSFET visti come interruttori:

                o     n-MOSFET ON se pilotato da un 1 logico e 𝑉𝑉𝐷𝐷𝐷𝐷 = 0 𝑉𝑉
                o     n-MOSFET OFF se pilotato da uno 0 logico

                o     p-MOSFET ON se pilotato da un 0 logico
                o     p-MOSFET OFF se pilotato da uno 1 logico e 𝑉𝑉𝑆𝑆𝑆𝑆 = 0 𝑉𝑉

     -     la serie di MOSFET implementa un prodotto booleano

     -     il parallelo di MOSFET implementa una somma booleana

     -     il PU deve generare 𝐹𝐹 = 1 ed è quindi:

                                                           𝑃𝑃𝑃𝑃(𝐼𝐼�1 , 𝐼𝐼�2 , … , 𝐼𝐼�𝑛𝑛 ) = 𝐹𝐹(𝐼𝐼1 , 𝐼𝐼2 , … , 𝐼𝐼𝑛𝑛 )

     -     il PD deve generare 𝐹𝐹 = 0 ed è quindi:

                                                           𝑃𝑃𝑃𝑃(𝐼𝐼1 , 𝐼𝐼2 , … , 𝐼𝐼𝑛𝑛 ) = ������������������
                                                                                         𝐹𝐹(𝐼𝐼1 , 𝐼𝐼2 , … , 𝐼𝐼𝑛𝑛 )

                                            ��������������������
Dalle funzioni di PU e di PD si ottiene che 𝑃𝑃𝑃𝑃(𝐼𝐼                            � �              �
                                                   1 , 𝐼𝐼2 , … , 𝐼𝐼𝑛𝑛 ) = 𝑃𝑃𝑃𝑃(𝐼𝐼1 , 𝐼𝐼2 , … , 𝐼𝐼𝑛𝑛 ).


PU e PD sono quindi duali tra loro: nell’implementazione questo si traduce col fatto che un parallelo diventa una
serie e viceversa, ma questo non porta sempre alla rete minima o ad una rete dove PU e PD sono duali tra loro.
La sintesi è l’implementazione di funzioni logiche con un circuito digitale.

L’analisi di una porta logica è l’estrazione della relativa funzione logica.


Proprietà generali porte CMOS:

𝑃𝑃𝑃𝑃 = 𝑂𝑂𝑂𝑂 ⇒ 𝑃𝑃𝑃𝑃 = 𝑂𝑂𝑂𝑂𝑂𝑂
                            �  𝑉𝑉𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 e 𝑉𝑉𝑂𝑂𝑂𝑂 = 0 𝑉𝑉 in condizioni statiche e consumo di potenza nullo
𝑃𝑃𝑃𝑃 = 𝑂𝑂𝑂𝑂 ⇒ 𝑃𝑃𝑃𝑃 = 𝑂𝑂𝑂𝑂𝑂𝑂

Una funzione 𝐹𝐹 con 𝑁𝑁 ingressi richiede almeno 2𝑁𝑁 transistor.


Essendo che le commutazioni in transitorio dipendono dalle capacità in gioco e dalle conducibilità di PU e di PD,
la complessità dello studio di queste reti sarebbe eccessivamente complesso.

Per sempliﬁcarlo, si trasformano PU e PD in due transistor equivalenti che vengono quindi a formare un inverter
equivalente per il quale valgono tutte le equazioni calcolate per l’inverter normale (tempo di propagazione,
consumo di potenza, …).

Il dimensionamento del transistor equivalente (dimensionamento equivalente) dipende dai dimensionamenti e
dalla topologia di PU e PD originali.

Ovviamente il transistor equivalente deve rispettare tutte le relazioni che valgono per il MOSFET normale.

    -    Parallelo di MOSFET:

         Ingressi: 𝐴𝐴, 𝐵𝐵
         Tensioni: alimentazione 𝑉𝑉𝐷𝐷 = 𝑉𝑉𝐷𝐷1 = 𝑉𝑉𝐷𝐷2 , massa 𝑉𝑉𝑆𝑆 = 𝑉𝑉𝑆𝑆1 = 𝑉𝑉𝑆𝑆2
         Corrente totale della porta: 𝐼𝐼 = 𝐼𝐼𝐷𝐷𝑆𝑆1 + 𝐼𝐼𝐷𝐷𝑆𝑆2

         Con n-MOSFET con dimensionamenti 𝑆𝑆1 ed 𝑆𝑆2 :

              o    Caso 1: 𝐴𝐴 = 0, 𝐵𝐵 = 1  𝑇𝑇1 𝑂𝑂𝑂𝑂𝑂𝑂, 𝑇𝑇2 𝑂𝑂𝑂𝑂  caso banale con un solo transistor
              o    Caso 2: 𝐴𝐴 = 1, 𝐵𝐵 = 0  𝑇𝑇1 𝑂𝑂𝑂𝑂, 𝑇𝑇2 𝑂𝑂𝑂𝑂𝑂𝑂  caso banale con un solo transistor
              o    Caso 3: 𝐴𝐴 = 1, 𝐵𝐵 = 1  𝑇𝑇1 𝑂𝑂𝑂𝑂, 𝑇𝑇2 𝑂𝑂𝑂𝑂  2 transistor in parallelo con stesse 𝑉𝑉𝐺𝐺 , 𝑉𝑉𝐷𝐷 , 𝑉𝑉𝑆𝑆

         Espandendo le equazioni delle correnti 𝐼𝐼𝐷𝐷𝑆𝑆1 ed 𝐼𝐼𝐷𝐷𝑆𝑆2 si ottiene che il dimensionamento equivalente nel
         caso 3 (quello di maggior interesse) è:

                                                                𝑆𝑆𝑒𝑒𝑒𝑒 = 𝑆𝑆1 + 𝑆𝑆2

    -    Serie di MOSFET:

         Ingressi: 𝐴𝐴, 𝐵𝐵
         Tensioni: alimentazione 𝑉𝑉𝐷𝐷 = 𝑉𝑉𝐷𝐷2 , massa 𝑉𝑉𝑆𝑆 = 𝑉𝑉𝑆𝑆1 , 𝑉𝑉𝑥𝑥 = 𝑉𝑉𝑆𝑆2 = 𝑉𝑉𝐷𝐷1
         Corrente totale della porta: 𝐼𝐼 = 𝐼𝐼𝐷𝐷𝑆𝑆1 = 𝐼𝐼𝐷𝐷𝑆𝑆2

         Con n-MOSFET con dimensionamenti 𝑆𝑆1 ed 𝑆𝑆2 (𝑇𝑇1 collegato a massa, 𝑇𝑇2 ad alimentazione):

              o    Caso 1: 𝐴𝐴 = 0, 𝐵𝐵 = 1  𝑇𝑇2 𝑂𝑂𝑂𝑂𝑂𝑂, 𝑇𝑇1 𝑂𝑂𝑂𝑂  caso banale con la serie spenta
              o    Caso 2: 𝐴𝐴 = 1, 𝐵𝐵 = 0  𝑇𝑇2 𝑂𝑂𝑂𝑂, 𝑇𝑇1 𝑂𝑂𝑂𝑂𝑂𝑂  caso banale con la serie spenta
              o    Caso 3: 𝐴𝐴 = 1, 𝐵𝐵 = 1  𝑇𝑇2 𝑂𝑂𝑂𝑂, 𝑇𝑇2 𝑂𝑂𝑂𝑂  2 transistor in serie con stesse 𝑉𝑉𝐺𝐺 = 𝑉𝑉𝐺𝐺1 = 𝑉𝑉𝐺𝐺2 , 𝑉𝑉𝐵𝐵

         Espandendo le equazioni delle correnti 𝐼𝐼𝐷𝐷𝑆𝑆1 ed 𝐼𝐼𝐷𝐷𝑆𝑆2 ed ipotizzando 𝜆𝜆 = 0, 𝛾𝛾 = 0 (𝑉𝑉𝑇𝑇𝑛𝑛 = �𝑉𝑉𝑇𝑇𝑝𝑝 � ), si ottiene
         che il dimensionamento equivalente nel caso 3 (quello di maggior interesse) è:
                                                                                           𝑆𝑆1 𝑆𝑆2
                                                                              𝑆𝑆𝑒𝑒𝑒𝑒 =
                                                                                         𝑆𝑆1 + 𝑆𝑆2

         𝑇𝑇1 è sempre in regione triodo se 𝑇𝑇2 𝑂𝑂𝑂𝑂 ed il dimensionamento equivalente non cambia sia per 𝑇𝑇2 in
         saturazione, sia per 𝑇𝑇2 in triodo.


Prestazioni dinamiche porte CMOS:

In una porta generica, anche se coi transistor equivalenti per PU e per PD, la carica e la scarica del nodo di uscita
seguono percorsi differenti.

Tra tutti deve essere garantito quello di caso peggiore, sia per il transitorio di carica della capacità di carico 𝐶𝐶𝐿𝐿 ,
sia per quello di scarica:

    -    PORTA NOR:

             o    SCARICA 𝐶𝐶𝐿𝐿 :

                  Il caso peggiore è quando 𝐶𝐶𝐿𝐿 si scarica su un solo n-MOSFET (nella rete di PD).

                  Il tempo di discesa è identico a quello dell’inverter:

                                                                                                2𝐶𝐶𝐿𝐿                𝑉𝑉𝑇𝑇
                                                                        𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁 =                           𝐹𝐹 �        �
                                                                                       𝛽𝛽𝑛𝑛′ 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷

                  Dove 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 è il dimensionamento dell’n-MOSFET.

             o    CARICA 𝐶𝐶𝐿𝐿 :

                  Il caso peggiore è quando 𝐶𝐶𝐿𝐿 si carica tramite i due p-MOSFET in serie (nella rete di PU).
                  Considerando identici i due p-MOSFET aventi entrambi dimensionamento 𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁 :

                                                                                           𝑆𝑆1 𝑆𝑆2  𝑆𝑆𝑝𝑝
                                                                              𝑆𝑆𝑒𝑒𝑒𝑒 =             = 𝑁𝑁𝑁𝑁𝑁𝑁
                                                                                         𝑆𝑆1 + 𝑆𝑆2      2

                  Si deﬁnisce il dimensionamento relativo tra n-MOSFET e p-MOSFET nella porta NOR come:

                                                                                                    𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁
                                                                                    𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁 ≔
                                                                                                    𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁

                  Si ottiene:

                                                    2𝐶𝐶𝐿𝐿              𝑉𝑉𝑇𝑇            4𝐶𝐶𝐿𝐿                𝑉𝑉𝑇𝑇                4𝐶𝐶𝐿𝐿                     𝑉𝑉𝑇𝑇
                               𝑡𝑡𝑟𝑟𝑁𝑁𝑁𝑁𝑁𝑁 =     ′
                                                                 𝐹𝐹 �        �= ′                     𝐹𝐹 �        �= ′                              𝐹𝐹 �        �
                                              𝛽𝛽𝑝𝑝 𝑆𝑆𝑒𝑒𝑒𝑒 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷   𝛽𝛽𝑝𝑝 𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷   𝛽𝛽𝑝𝑝 𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷


                  Volendo 𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑡𝑡𝑟𝑟𝑁𝑁𝑁𝑁𝑁𝑁 si ha:

                                                                               1         2
                                                                                ′
                                                                                  = ′
                                                                              𝛽𝛽𝑛𝑛 𝛽𝛽𝑝𝑝 𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁

                                                                                         ⇓

                                                                                             𝛽𝛽𝑛𝑛′
                                                                          𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁 = 2             = 2𝜀𝜀
                                                                                             𝛽𝛽𝑝𝑝′
           Volendo 𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑡𝑡𝑟𝑟𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑡𝑡𝐼𝐼𝐼𝐼𝐼𝐼 (in modo che la NOR abbia lo stesso ritardo dell’inverter):

                                                                    𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑆𝑆𝐼𝐼𝐼𝐼𝐼𝐼
                                                                 �𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁 = 2𝜀𝜀𝑆𝑆𝐼𝐼𝐼𝐼𝐼𝐼
                                                                      𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁 = 2𝜀𝜀

           Il calcolo di 𝐶𝐶𝐼𝐼𝐼𝐼 deve tenere conto che ogni ingresso vede un n-MOSFET ed un p-MOSFET:

                                                           𝐶𝐶𝐼𝐼𝐼𝐼 = 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 (1 + 2𝜀𝜀)𝐶𝐶𝑀𝑀1

           Per l’occupazione per unità d’area si ha:

                   𝐴𝐴 = 2𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 + 2𝑊𝑊𝑝𝑝 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 = 2𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀 �𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 + 𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁 � = 2𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 (1 + 2𝜀𝜀)

                                                                              ⇓

                                                                       𝐴𝐴
                                                     𝐴𝐴●𝑁𝑁𝑁𝑁𝑁𝑁 =               = 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 (2 + 4𝜀𝜀)
                                                                     𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀


           Per una generica NOR ad 𝑁𝑁 ingressi si ha:

                                                                    𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑁𝑁𝑁𝑁
                                                          𝐶𝐶
                                                        � 𝐼𝐼𝐼𝐼 =   𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 (1 + 𝑁𝑁𝑁𝑁)𝐶𝐶𝑀𝑀1
                                                         𝐴𝐴●𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁 (𝑁𝑁 + 𝑁𝑁 2 𝜀𝜀)


-   PORTA NAND:

       o   CARICA 𝐶𝐶𝐿𝐿 :

           Il caso peggiore è quando 𝐶𝐶𝐿𝐿 si carica tramite un solo p-MOSFET (nella rete di PU).
           Si deﬁnisce il dimensionamento relativo tra n-MOSFET e p-MOSFET nella porta NAND come:

                                                                                         𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁
                                                                        𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 ≔
                                                                                         𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁

           Il tempo di salita è identico a quello dell’inverter:

                                                            2𝐶𝐶𝐿𝐿                 𝑉𝑉𝑇𝑇                  2𝐶𝐶𝐿𝐿                       𝑉𝑉𝑇𝑇
                                  𝑡𝑡𝑟𝑟𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 =     ′
                                                                            𝐹𝐹 �        �= ′                                  𝐹𝐹 �        �
                                                   𝛽𝛽𝑝𝑝 𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷   𝛽𝛽𝑝𝑝 𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷

           Dove 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 , 𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 sono i dimensionamenti di n-MOSFET e p-MOSFET.

       o   SCARICA 𝐶𝐶𝐿𝐿 :

           Il caso peggiore è quando 𝐶𝐶𝐿𝐿 si scarica tramite i due n-MOSFET in serie (nella rete di PD).

           Considerando identici i due n-MOSFET in serie aventi entrambi dimensionamento 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 :

                                                                                𝑆𝑆1 𝑆𝑆2  𝑆𝑆𝑛𝑛
                                                                   𝑆𝑆𝑒𝑒𝑒𝑒 =             = 𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁
                                                                              𝑆𝑆1 + 𝑆𝑆2       2

           Si ottiene:

                                                                  2𝐶𝐶𝐿𝐿              𝑉𝑉𝑇𝑇             4𝐶𝐶𝐿𝐿                 𝑉𝑉𝑇𝑇
                                         𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 =                        𝐹𝐹 �        �= ′                       𝐹𝐹 �        �
                                                           𝛽𝛽𝑛𝑛′ 𝑆𝑆𝑒𝑒𝑒𝑒 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷   𝛽𝛽𝑛𝑛 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷
                 Volendo 𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑡𝑡𝑟𝑟𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 si ha:

                                                                        2           1
                                                                            =
                                                                       𝛽𝛽𝑛𝑛′ 𝛽𝛽𝑝𝑝′ 𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁

                                                                                ⇓

                                                                                  𝛽𝛽𝑛𝑛′    𝜀𝜀
                                                                   𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 =        ′
                                                                                         =
                                                                                  2𝛽𝛽𝑝𝑝 2

                 Volendo 𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑡𝑡𝑟𝑟𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑡𝑡𝐼𝐼𝐼𝐼𝐼𝐼 (in modo che la NAND abbia lo stesso ritardo dell’inverter):

                                                                     𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 = 2𝑆𝑆𝐼𝐼𝐼𝐼𝐼𝐼
                                                                     𝑆𝑆           = 𝜀𝜀𝑆𝑆𝐼𝐼𝐼𝐼𝐼𝐼
                                                                    � 𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁
                                                                                       𝜀𝜀
                                                                         𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 =
                                                                                       2

                 Il calcolo di 𝐶𝐶𝐼𝐼𝐼𝐼 deve tenere conto che ogni ingresso vede un n-MOSFET ed un p-MOSFET:

                                                                                        𝜀𝜀
                                                              𝐶𝐶𝐼𝐼𝐼𝐼 = 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 �1 + � 𝐶𝐶𝑀𝑀1
                                                                                        2

                 Per l’occupazione per unità d’area si ha:

                                                                                                                                       𝜀𝜀
                        𝐴𝐴 = 2𝑊𝑊𝑛𝑛 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 + 2𝑊𝑊𝑝𝑝 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 = 2𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀 �𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 + 𝑆𝑆𝑝𝑝𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 � = 2𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 �1 + �
                                                                                                                                       2

                                                                                ⇓

                                                                          𝐴𝐴
                                                        𝐴𝐴●𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 =             = 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 (2 + 𝜀𝜀)
                                                                        𝐿𝐿2𝑀𝑀𝑀𝑀𝑀𝑀


                 Per una generica NAND ad 𝑁𝑁 ingressi si ha:

                                                                                       𝜀𝜀
                                                            ⎧           𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 =
                                                            ⎪                         𝑁𝑁
                                                                                          𝜀𝜀
                                                            ⎨𝐶𝐶𝐼𝐼𝐼𝐼 = 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 �1 + 𝑁𝑁� 𝐶𝐶𝑀𝑀1
                                                            ⎪
                                                            ⎩ 𝐴𝐴●𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 = 𝑆𝑆𝑛𝑛𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 (𝑁𝑁 + 𝜀𝜀)


La porta NAND i p-MOSFET e gli n-MOSFET sono più simili in termini di area. Questo rende più simili anche le reti
di PU e di PD poiché la scarsa conducibilità dei p-MOSFET è compensata dal fatto che gli n-MOSFET sono in
serie e, quindi, conducono di meno.

A parità di prestazioni dinamiche (imposte uguali a quelle dell’inverter), è preferibile una NAND perché occupa
meno area.

Tutti questi ragionamenti sono stati fatti NON considerando l’EMLC, l’effetto Body ed il self-loading (quest’ultimo
rende validi questi risultati solo se la capacità a valle della porta che si considera è più grande rispetto a quelle
dei MOSFET).


Effetto del self-loading nelle porte CMOS:

Quando non si riesce a far scaricare totalmente 𝐶𝐶𝐿𝐿 in tempo si veriﬁca l’effetto del self-loading.

Per tenerne conto bisogna valutare tutti i contributi capacitivi sul nodo di uscita della porta logica.
Essendo che la porta NAND è la più appetibile per l’occupazione di area a parità di prestazioni dinamiche, si
considera una porta NAND ad 𝑚𝑚 ingressi che pilota 𝑘𝑘 porte logiche a valle:

                                                                                  𝐹𝐹𝐹𝐹𝑁𝑁𝐼𝐼𝐼𝐼 = 𝑚𝑚
                                                                                 𝐹𝐹𝐹𝐹𝑁𝑁𝑂𝑂𝑂𝑂𝑂𝑂 = 𝑘𝑘

                                                                                    𝐶𝐶𝑊𝑊 = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐
                                                      𝐶𝐶𝐼𝐼𝑁𝑁𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢 𝑝𝑝𝑝𝑝𝑝𝑝 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑙𝑙𝑙𝑙 𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 𝑎𝑎 𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣

Si ipotizza una transizione 0 → 1 istantanea di tutti gli ingressi della NAND e quindi l’uscita commuta 1 → 0:

    -      Tutti i MOSFET direttamente collegati all’uscita vedono prima della commutazione dell’ingresso

                                                                            𝑉𝑉𝐺𝐺𝐷𝐷𝑝𝑝𝑝𝑝𝑝𝑝 = 0 − 𝑉𝑉𝐷𝐷𝐷𝐷 = −𝑉𝑉𝐷𝐷𝐷𝐷

            E, subito dopo la commutazione dell’ingresso e dell’uscita, vedono

                                                                             𝑉𝑉𝐺𝐺𝐷𝐷𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 0 = 𝑉𝑉𝐷𝐷𝐷𝐷

           Quindi il salto di tensione da prima a dopo le commutazioni è 𝑉𝑉𝐺𝐺𝐷𝐷𝑇𝑇𝑇𝑇𝑇𝑇 = 𝑉𝑉𝐺𝐺𝐷𝐷𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 − 𝑉𝑉𝐺𝐺𝐷𝐷𝑝𝑝𝑝𝑝𝑝𝑝 = 2𝑉𝑉𝐷𝐷𝐷𝐷

    -      Le capacità 𝐶𝐶𝐺𝐺𝐺𝐺 di questi MOSFET vedono un salto di tensione di 2𝑉𝑉𝐷𝐷𝐷𝐷 che è paragonabile al caricare
           una capacità doppia 2𝐶𝐶𝐺𝐺𝐺𝐺 a 𝑉𝑉𝐷𝐷𝐷𝐷

La capacità sul nodo di uscita ha come contributi:

    -      Le 𝑘𝑘 𝐶𝐶𝐼𝐼𝑁𝑁𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 delle porte logiche a valle
    -      Dalla capacità di interconnessione 𝐶𝐶𝑊𝑊
    -      Da un n-MOSFET (vedere struttura NAND per capire perché)
    -      Dagli 𝑚𝑚 p-MOSFET (vedere struttura NAND per capire perché)

Quindi:

                                                       1                                                                 1
    𝐶𝐶𝐿𝐿 = 𝑘𝑘𝐶𝐶𝐼𝐼𝑁𝑁𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 + 𝐶𝐶𝑊𝑊 + 𝑊𝑊𝑛𝑛 �2𝐶𝐶𝐺𝐺𝑆𝑆0 + 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 𝑅𝑅𝐷𝐷𝐷𝐷 + 𝐾𝐾𝑒𝑒𝑒𝑒 𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0 � + 𝑚𝑚𝑊𝑊𝑝𝑝 �2𝐶𝐶𝐺𝐺𝑆𝑆0 + 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 𝑅𝑅𝐷𝐷𝐷𝐷 + 𝐾𝐾𝑒𝑒𝑒𝑒 𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0 �
                                                       2                                                                 2

                                                            𝑉𝑉𝑇𝑇                       𝑊𝑊𝑛𝑛                         𝑊𝑊𝑝𝑝
                                         𝑅𝑅𝐷𝐷𝐷𝐷 = 1 −             ,         𝑆𝑆𝑛𝑛 =             ,         𝑆𝑆𝑝𝑝 =             = 𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 𝑆𝑆𝑛𝑛
                                                           𝑉𝑉𝐷𝐷𝐷𝐷                     𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀                     𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀

                                                                                           ⇓

                                                      𝐶𝐶𝐿𝐿 = 𝑘𝑘𝐶𝐶𝐼𝐼𝑁𝑁𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 + 𝐶𝐶𝑊𝑊 + 𝑆𝑆𝑛𝑛 (1 + 𝑚𝑚𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 )𝐶𝐶𝑝𝑝1

                                                                              1
                                                  𝐶𝐶𝑝𝑝1 = 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 �2𝐶𝐶𝐺𝐺𝑆𝑆0 + 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 𝐶𝐶𝑂𝑂𝑂𝑂 𝑅𝑅𝐷𝐷𝐷𝐷 + 𝐾𝐾𝑒𝑒𝑒𝑒 𝐿𝐿𝑠𝑠 𝐶𝐶𝐽𝐽0 �
                                                                              2

Dove 𝐶𝐶𝑝𝑝1 è la capacità sul nodo di OUT dovuta ad un transistore ad area minima (𝑊𝑊 = 𝐿𝐿 = 𝐿𝐿𝑀𝑀𝑀𝑀𝑀𝑀 ).

Trovata la capacità di carico dalla NAND, si passa alla valutazione di 𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 considerando gli 𝑚𝑚 n-MOSFET messi
in serie (rete di PD).
                             1        1    𝑆𝑆𝑛𝑛
Questa serie ha 𝑆𝑆𝑒𝑒𝑒𝑒 = 1 1      1 = 𝑚𝑚 =      :
                                      + +⋯+                       𝑚𝑚
                                  ��
                                  𝑆𝑆𝑛𝑛 ��
                                        𝑆𝑆���
                                          𝑛𝑛 ����
                                               𝑆𝑆𝑛𝑛     𝑆𝑆𝑛𝑛
                                         𝑚𝑚


                                                                                                𝑉𝑉
                            2𝐶𝐶𝐿𝐿              𝑉𝑉𝑇𝑇      2𝑚𝑚𝐶𝐶𝐿𝐿              𝑉𝑉𝑇𝑇     2𝐹𝐹 � 𝑇𝑇 � 𝑚𝑚
                                                                                               𝑉𝑉𝐷𝐷𝐷𝐷
        𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 = ′                 𝐹𝐹 �        �= ′               𝐹𝐹 �        �=                    �𝑘𝑘𝐶𝐶𝐼𝐼𝑁𝑁𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 + 𝐶𝐶𝑊𝑊 + 𝑆𝑆𝑛𝑛 (1 + 𝑚𝑚𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 )𝐶𝐶𝑝𝑝1 �
                      𝛽𝛽𝑛𝑛 𝑆𝑆𝑒𝑒𝑒𝑒 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷   𝛽𝛽𝑛𝑛 𝑆𝑆𝑛𝑛 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷     𝛽𝛽𝑛𝑛′ 𝑉𝑉𝐷𝐷𝐷𝐷 𝑆𝑆𝑛𝑛
                                                                              ⇓

                                                         𝑉𝑉𝑇𝑇
                                               2𝐹𝐹 �
                                                        𝑉𝑉𝐷𝐷𝐷𝐷 � 𝑚𝑚
                                  𝑡𝑡𝑓𝑓𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 =                � �𝑘𝑘𝐶𝐶𝐼𝐼𝑁𝑁𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 + 𝐶𝐶𝑊𝑊 � + 𝑚𝑚(1 + 𝑚𝑚𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 )𝐶𝐶𝑝𝑝1 �
                                                 𝛽𝛽𝑛𝑛′ 𝑉𝑉𝐷𝐷𝐷𝐷 𝑆𝑆𝑛𝑛

Dove:
         𝑚𝑚
    -           �𝑘𝑘𝐶𝐶𝐼𝐼𝑁𝑁𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 + 𝐶𝐶𝑊𝑊 �  effetto del carico che dipende quindi dal 𝐹𝐹𝐹𝐹𝑁𝑁𝑂𝑂𝑂𝑂𝑂𝑂 (𝑘𝑘)
         𝑆𝑆𝑛𝑛


    -    𝑚𝑚(1 + 𝑚𝑚𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 )𝐶𝐶𝑝𝑝1  effetto del self-loading dovuto al 𝐹𝐹𝐹𝐹𝑁𝑁𝐼𝐼𝐼𝐼 e non dal dimensionamento 𝑆𝑆𝑛𝑛

                                                                     𝜀𝜀
Ricordando che per la porta NAND vale 𝛼𝛼𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁 =                         il self-loading dipende linearmente dal 𝐹𝐹𝐹𝐹𝑁𝑁𝐼𝐼𝐼𝐼
                                                                    𝑚𝑚


Sono stati trascurati gli effetti reattivi degli 𝑚𝑚 − 1 n-MOSFET della rete di PD che rendono maggiore il ritardo e
che crescono di numero in base ad 𝑚𝑚 e di valore in base ad 𝑆𝑆𝑛𝑛 .


Riduzione del ritardo delle porte CMOS:

Si è visto che se il 𝐹𝐹𝐹𝐹𝑁𝑁𝐼𝐼𝐼𝐼 è alto, è alto anche il ritardo ed il self-loading (che dipende dal quadrato del 𝐹𝐹𝐹𝐹𝑁𝑁𝐼𝐼𝐼𝐼 )
domina.

Per ridurre il ritardo ci sono 4 metodi:

    1) Dimensionamento progressivo:

         Si pensi ad una rete di PD composta da una serie di n-MOSFET da 𝑇𝑇1 (collegato a massa) a 𝑇𝑇𝑞𝑞 (collegato
         al nodo di OUT).

         Ognuno di essi vede una capacità sul suo nodo di uscita che deve caricare e scaricare (da 𝐶𝐶1 a 𝐶𝐶𝑞𝑞 = 𝐶𝐶𝐿𝐿 ).

         Il problema è che su 𝑇𝑇1 scorre la corrente di scarica di tutte le capacità di carico e rappresenta quindi il
         collo di bottiglia della rete.

         Il problema si risolve usando un dimensionamento maggiore in modo che possa transitare più corrente:

                                                                          𝑆𝑆1 > 𝑆𝑆2 > ⋯ > 𝑆𝑆𝑞𝑞

    2) Ordinamento dei segnali di ingresso:

         Spesse volte si può individuare il percorso critico che stabilisce il tempo di ritardo di caso peggiore e che
         è relativo all’ingresso che è più lento a commutare.

         Questo segnale verrà connesso al MOSFET più vicino all’uscita e mai a quello che rappresenta il collo di
         bottiglia.

         Facendo riferimento alla rete del Dimensionamento progressivo ed ipotizzando che il segnale lento sia
         quello in ingresso a 𝑇𝑇𝑞𝑞 , si ha che la scarica di tutte le capacità può cominciare prima rispetto alla sola 𝐶𝐶𝐿𝐿
         (unica capacità che deve per forza scaricarsi attraverso 𝑇𝑇𝑞𝑞 ).

    3) Strutturazione su più livelli di logica:

         L’obiettivo di questo metodo è AVERE SEMPRE 𝐹𝐹𝐹𝐹𝑁𝑁𝐼𝐼𝐼𝐼 ≤ 4.

         Se la porta logica presa in considerazione ha tanti ingressi, la si divide in più porte che si connettono ad
         altri livelli in modo da ottenere la stessa funzione logica, ma attraverso più “strati”.
    4) Separazione tra grandi 𝑭𝑭𝑭𝑭𝑵𝑵𝑰𝑰𝑰𝑰 e grandi 𝑪𝑪𝑳𝑳 :

         Se si è in presenza di una 𝐶𝐶𝐿𝐿 elevata, è possibile che si voglia ridurre il ritardo dovuto al carico
         aumentando le dimensioni della porta logica a monte aumentando tanto il ritardo dovuto al self-loading
         e quindi al 𝐹𝐹𝐹𝐹𝑁𝑁𝐼𝐼𝐼𝐼 .

         In queste condizioni (𝐶𝐶𝐿𝐿 ≫ 𝐶𝐶𝐼𝐼𝐼𝐼 ) si tende quindi a separare la porta logica dal carico tramite l’ausilio di
         buffer.


Consumo di potenza delle porte CMOS:

La potenza statica è nulla, ma quella dinamica dipende dalle commutazioni.

Per l’inverter vale:

                                                                            2
                                                         𝑃𝑃𝑑𝑑𝑑𝑑𝑑𝑑 = 𝐶𝐶𝐿𝐿 𝑉𝑉𝐷𝐷𝐷𝐷 𝒻𝒻0→1

Dove 𝒻𝒻0→1 è la frequenza media delle transizioni 0 → 1 sul nodo di OUT.
Per l’inverter però si ha 𝒻𝒻𝐼𝐼𝐼𝐼 = 𝒻𝒻0→1 e quindi si ha:

                                                                             2
                                                          𝑃𝑃𝑑𝑑𝑑𝑑𝑑𝑑 = 𝐶𝐶𝐿𝐿 𝑉𝑉𝐷𝐷𝐷𝐷 𝒻𝒻𝐼𝐼𝐼𝐼

Per una porta logica generica la frequenza di lavoro del circuito è dettata dalla frequenza di clock 𝒻𝒻𝐶𝐶𝐶𝐶 e si ha:

                                                          𝒻𝒻0→1 = 𝒻𝒻𝐶𝐶𝐶𝐶 𝑃𝑃0→1

Dove 𝑃𝑃0→1 è detta switching activity (probabilità che ci sia una commutazione 0 → 1 sul nodo di OUT).

Per calcolarla:

                                        𝑃𝑃0→1 = 𝑃𝑃0 𝑃𝑃1 = (1 − 𝑃𝑃1 )𝑃𝑃1 = 𝑃𝑃0 (1 − 𝑃𝑃0 )

Dove 𝑃𝑃0 e 𝑃𝑃1 sono le probabilità di avere uno 0 o un 1 in OUT e dipendono dalla funzione logica implementata.

Nel caso in cui la probabilità di avere in ingresso un 1 o uno 0 non sia uguale, bisogna calcolare i valori di 𝑃𝑃0 e 𝑃𝑃1
in base alla funzione logica implementata assumendo gli ingressi come incorrelati (per esempio, si possono
avere le probabilità di avere un 1 all’ingresso 𝐴𝐴 ed all’ingresso 𝐵𝐵 deﬁnite come 𝑃𝑃𝐴𝐴 e 𝑃𝑃𝐵𝐵 e poi calcolare 𝑃𝑃0 e 𝑃𝑃1 ).


Per una generica porta logica con 𝑛𝑛 ingressi si hanno 2𝑛𝑛 possibili combinazioni di ingressi (supposti incorrelati!).
Detti 𝑁𝑁0 ed 𝑁𝑁1 il numero di 0 e di 1 in OUT nella tabella di verità.
Ipotizzando la probabilità di avere, per gli ingressi, una probabilità di uguale di essere 0 o 1, si ha:

                                                𝑁𝑁1                  𝑁𝑁0                𝑁𝑁1
                                        𝑃𝑃1 =       ,       𝑃𝑃0 =        = 1 − 𝑃𝑃1 = 1 − 𝑛𝑛
                                                2𝑛𝑛                  2𝑛𝑛                2

                                                                       ⇓

                                                                                 𝑁𝑁0 𝑁𝑁1
                                                        𝑃𝑃0→1 = 𝑃𝑃0 𝑃𝑃1 =
                                                                                  22𝑛𝑛


Pilotaggio di grandi capacità con porte CMOS:

Le capacità di carico collegate al nodo di OUT aumentano il tempo di ritardo ed inﬂuenzano le performance.

Preso in considerazione un inverter CMOS che pilota una capacità di carico 𝐶𝐶𝐿𝐿 (si trascura il self-loading), si ha:
                                                                         𝐶𝐶𝐼𝐼𝐼𝐼 = 𝑆𝑆𝑛𝑛 (1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1

                       𝑆𝑆𝑝𝑝                ′
                                         𝛽𝛽𝑛𝑛
Considerato 𝛼𝛼 =              = 𝜀𝜀 =       ′     𝛽𝛽𝑛𝑛 = 𝛽𝛽𝑝𝑝  𝑡𝑡𝑟𝑟 = 𝑡𝑡𝑓𝑓 :
                       𝑆𝑆𝑛𝑛              𝛽𝛽𝑝𝑝


                                             2𝐶𝐶𝐿𝐿             𝑉𝑉𝑇𝑇      𝐶𝐶𝐿𝐿 2𝐶𝐶𝐼𝐼𝐼𝐼                  𝑉𝑉𝑇𝑇      𝐶𝐶𝐿𝐿 2(1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1        𝑉𝑉𝑇𝑇
                              𝑡𝑡𝑝𝑝 =                     𝐹𝐹 �        �=                          𝐹𝐹 �        �=                       𝐹𝐹 �        �
                                       𝛽𝛽𝑛𝑛′ 𝑆𝑆𝑛𝑛 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷    𝐶𝐶𝐼𝐼𝐼𝐼 𝛽𝛽𝑛𝑛′ 𝑆𝑆𝑛𝑛 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷    𝐶𝐶𝐼𝐼𝐼𝐼   𝛽𝛽𝑛𝑛′ 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷

                                                                                       ⇓

                                                                                 𝑡𝑡𝑝𝑝 = 𝑋𝑋𝑡𝑡𝑝𝑝0

                                                                                            𝐶𝐶𝐿𝐿
                                                                                  𝑋𝑋 ≔
                                                                                           𝐶𝐶𝐼𝐼𝐼𝐼

                                                                             2(1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1        𝑉𝑉𝑇𝑇
                                                                   𝑡𝑡𝑝𝑝0 =                   𝐹𝐹 �        �
                                                                                𝛽𝛽𝑛𝑛′ 𝑉𝑉𝐷𝐷𝐷𝐷      𝑉𝑉𝐷𝐷𝐷𝐷

Dove:

     -    𝑡𝑡𝑝𝑝0 è il tempo di propagazione di un inverter caricato da un inverter identico

     -    𝑋𝑋 = 1000 ÷ 10000 se l’inverter è connesso ad una lunga catena di interconnessione o ad un pin di OUT
          del circuito integrato

Per far sì che 𝑋𝑋 cali deve essere inserito un buffer, ma il 𝑡𝑡𝑝𝑝 totale dipende dal dimensionamento di quest’ultimo.

Per capire quanto debba essere grande, si considerano quindi 2 inverter in cascata a formare un buffer:

     -    Il 1° inverter è ipotizzato ad area minima  𝐶𝐶𝐼𝐼𝐼𝐼 = 𝑆𝑆𝑛𝑛 (1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1 = (1 + 𝜀𝜀)𝐶𝐶𝑀𝑀1

     -    Il 2° inverter ha dimensionamento del n-MOSFET pari ad 𝑆𝑆 ed ha come capacità di ingresso 𝐶𝐶𝐼𝐼𝑁𝑁2

Quindi:

                                                  𝐶𝐶𝐼𝐼𝑁𝑁2 = 𝑆𝑆𝑛𝑛 (1 + 𝛼𝛼)𝐶𝐶𝑀𝑀1 = 𝑆𝑆(1 + 𝜀𝜀)𝐶𝐶𝑀𝑀1 = 𝑆𝑆𝐶𝐶𝐼𝐼𝐼𝐼 = 𝐶𝐶𝐿𝐿1

                                                                                       ⇓

                                                                                         𝐶𝐶𝐼𝐼𝑁𝑁2
                                                                                  𝑆𝑆 =
                                                                                          𝐶𝐶𝐼𝐼𝐼𝐼

Si approssima il ritardo come la somma dei ritardi dei singoli inverter:

                           𝐶𝐶𝐿𝐿1           𝐶𝐶𝐿𝐿           𝐶𝐶𝐼𝐼𝑁𝑁2          𝐶𝐶𝐿𝐿            𝐶𝐶𝐼𝐼𝑁𝑁   𝐶𝐶𝐿𝐿                    𝐶𝐶𝐿𝐿 𝐶𝐶𝐼𝐼𝐼𝐼                  𝑋𝑋
  𝑡𝑡𝑝𝑝 = 𝑡𝑡𝑝𝑝1 + 𝑡𝑡𝑝𝑝2 =          𝑡𝑡𝑝𝑝0 +         𝑡𝑡𝑝𝑝0 =         𝑡𝑡𝑝𝑝0 +         𝑡𝑡𝑝𝑝0 = � 2 +            � 𝑡𝑡𝑝𝑝0 = �𝑆𝑆 +                � 𝑡𝑡𝑝𝑝0 = �𝑆𝑆 + � 𝑡𝑡𝑝𝑝0
                           𝐶𝐶𝐼𝐼𝐼𝐼         𝐶𝐶𝐼𝐼𝑁𝑁2          𝐶𝐶𝐼𝐼𝐼𝐼         𝐶𝐶𝐼𝐼𝑁𝑁2           𝐶𝐶𝐼𝐼𝐼𝐼 𝐶𝐶𝐼𝐼𝑁𝑁2                 𝐶𝐶𝐼𝐼𝑁𝑁2 𝐶𝐶𝐼𝐼𝐼𝐼                𝑆𝑆

                                                                                       ⇓

                                                                                       𝑋𝑋
                                                                           𝑡𝑡𝑝𝑝 = �𝑆𝑆 + � 𝑡𝑡𝑝𝑝0
                                                                                       𝑆𝑆

Se 𝑆𝑆 cresce si ha un aumento di 𝑡𝑡𝑝𝑝 dovuto all’aumento di 𝐶𝐶𝐼𝐼𝑁𝑁2 , ma c’è anche una diminuzione di 𝑡𝑡𝑝𝑝 dovuta al fatto
che aumenta la corrente di carica e scarica su 𝐶𝐶𝐿𝐿 .

Per calcolare 𝑆𝑆𝑜𝑜𝑜𝑜𝑜𝑜 si pone:
                                                                            𝜕𝜕𝑡𝑡𝑝𝑝              𝑋𝑋
                                                                                   = 𝑡𝑡𝑝𝑝0 �1 − 2 � = 0
                                                                             𝜕𝜕𝜕𝜕              𝑆𝑆

                                                                                           ⇓

                                                                                    𝑆𝑆𝑜𝑜𝑜𝑜𝑜𝑜 = √𝑋𝑋

                                                                                           ⇓

                                                                                                       𝐶𝐶𝐿𝐿
                                                                    𝑡𝑡𝑝𝑝𝑜𝑜𝑜𝑜𝑜𝑜 = 2𝑡𝑡𝑝𝑝0 √𝑋𝑋 = 2𝑡𝑡𝑝𝑝0 �
                                                                                                      𝐶𝐶𝐼𝐼𝐼𝐼

Avendo inserito il buffer si è ottenuto che 𝑡𝑡𝑝𝑝 ∝ √𝑋𝑋 anziché 𝑡𝑡𝑝𝑝 ∝ 𝑋𝑋 (come nel caso senza buffer).
Si inserisce il buffer se 𝑋𝑋 > 4, ma se 𝑋𝑋 ≫ 4 si possono inserire più buffer.

Per capire quanti buffer inserire in base ad 𝑋𝑋 si comincia inserendo 𝑁𝑁 − 1 buffer tra il primo inverter e 𝐶𝐶𝐿𝐿 .
           𝐶𝐶𝐿𝐿𝑖𝑖        𝐶𝐶𝑖𝑖+1     𝑆𝑆
Si pone              =            = 𝑖𝑖+1 = 𝑈𝑈 = 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 e quindi:
          𝐶𝐶𝐼𝐼𝑁𝑁𝑖𝑖        𝐶𝐶𝑖𝑖           𝑆𝑆𝑖𝑖


                                                                  𝐶𝐶𝑖𝑖+1
                                                       𝑡𝑡𝑝𝑝𝑖𝑖 =          𝑡𝑡 = 𝑈𝑈𝑡𝑡𝑝𝑝0 ,              𝑖𝑖 = 1, 2, … , 𝑁𝑁 − 1
                                                                    𝐶𝐶𝑖𝑖 𝑝𝑝0

Tutti i 𝑡𝑡𝑝𝑝𝑖𝑖 sono uguali ed il tempo di ritardo dell’ultimo buffer è:

                                                                                  𝐶𝐶𝐿𝐿        𝐶𝐶𝐿𝐿
                                                                     𝑡𝑡𝑝𝑝𝑁𝑁 =          𝑡𝑡 =          𝑡𝑡
                                                                                  𝐶𝐶𝑁𝑁 𝑝𝑝0 𝑈𝑈𝑁𝑁−1 𝐶𝐶1 𝑝𝑝0

Dato che tutti i 𝑡𝑡𝑝𝑝𝑖𝑖 sono uguali, il caso ottimo si ha se 𝑡𝑡𝑝𝑝𝑖𝑖 = 𝑡𝑡𝑝𝑝𝑁𝑁 :

                                                               𝐶𝐶𝐿𝐿                                  𝐶𝐶𝐿𝐿                    𝐶𝐶𝐿𝐿
                                                𝑈𝑈𝑡𝑡𝑝𝑝0 =           𝑡𝑡           ⇒ 𝑈𝑈 =                          ⇒ 𝑈𝑈 𝑁𝑁 =        = 𝑋𝑋
                                                            𝑈𝑈 𝐶𝐶1 𝑝𝑝0
                                                              𝑁𝑁−1                                 𝑁𝑁−1
                                                                                                 𝑈𝑈 𝐶𝐶1                      𝐶𝐶1

Da cui segue che:

                                                                                               ln(𝑋𝑋)
                                                                                  𝑁𝑁𝑜𝑜𝑜𝑜𝑜𝑜 =
                                                                                               ln(𝑈𝑈)

                                                                                           ⇓

                                                                    𝑁𝑁𝑜𝑜𝑜𝑜𝑜𝑜
                                                                                                           ln(𝑋𝑋)
                                                            𝑡𝑡𝑝𝑝 = � 𝑡𝑡𝑝𝑝𝑖𝑖 = 𝑁𝑁𝑜𝑜𝑜𝑜𝑜𝑜 𝑈𝑈𝑡𝑡𝑝𝑝0 =                  𝑈𝑈𝑡𝑡
                                                                                                           ln(𝑈𝑈) 𝑝𝑝0
                                                                       𝑖𝑖


Per calcolare 𝑈𝑈𝑜𝑜𝑜𝑜𝑜𝑜 si pone:

                                                             𝜕𝜕𝑡𝑡𝑝𝑝           ln(𝑋𝑋)   ln(𝑋𝑋)
                                                                    = 𝑡𝑡𝑝𝑝0 �        −           𝑈𝑈� = 0
                                                             𝜕𝜕𝜕𝜕             ln(𝑈𝑈) 𝑈𝑈 ln2 (𝑈𝑈)

                                                                                           ⇓

                                                                                     𝑈𝑈𝑜𝑜𝑜𝑜𝑜𝑜 = 𝑒𝑒

                                                                                  𝑁𝑁𝑜𝑜𝑜𝑜𝑜𝑜 = ln(𝑋𝑋)

                                                                                                  𝐶𝐶𝐿𝐿
                                                                             𝑡𝑡𝑝𝑝𝑜𝑜𝑜𝑜𝑜𝑜 = ln �         � 𝑡𝑡 𝑒𝑒
                                                                                                 𝐶𝐶𝐼𝐼𝐼𝐼 𝑝𝑝0
Essendo 𝑈𝑈 ∈ ℕ  𝑈𝑈𝑜𝑜𝑜𝑜𝑜𝑜 = 3.
TECNOLOGIE CIRCUITALI ALTERNATIVE AL CMOS

    1) LOGICHE A RAPPORTO (RTL, TTL):

            o   1 transistor per ogni ingresso

            o   BJT o MOSFET

            o   presenza solo di PU o solo di PD

            o   consumo potenza statico non nullo

    2) LOGICHE STATICHE CMOS:

            o   basate su n-MOSFET e p-MOSFET

            o   PU e PD complementari

            o   consumo potenza statico nullo

            o   molti transistor (𝑁𝑁 ingressi  2𝑁𝑁 transistor)

            o   elevati 𝑡𝑡𝑝𝑝  comportamento dinamico limitato

    3) LOGICHE ALTERNATIVE ALLE PORTE LOGICHE CMOS:

            a. Logiche a PASS-TRANSISTOR (P.T.)

                        transistor visto come interruttore

                        segnale passa attraverso il MOSFET (non è collegato al Gate)

                        minore numero di MOSFET

            b. Logiche dinamiche CMOS

                        minore numero di MOSFET

                        consumo potenza statico nullo

                        nell’elaborazione del segnale si presentano 2 fasi distinte

                             •   fase di PRECARICA / PRESCARICA

                             •   fase di VALUTAZIONE DELL’INGRESSO


LOGICHE A PASS-TRANSISTOR (P.T.):

Alcuni ingressi pilotano i Gate e fungono come da enable, ma queste logiche si presentano come una rete di
interruttori con in aggiunta un buffer.

Si deve stare molto attenti a non creare competizioni sui nodi di OUT poiché verrà raggiunto dal segnale che
determinerà il valore di 𝐹𝐹.

Per realizzare una XOR, una NAND o una NOR bastano 4 MOSFET anziché gli 8 della logica CMOS.
Nel caso sia presente un solo P.T. (n-MOSFET), il nodo di uscita (nodo 𝑥𝑥) è caratterizzato dalla presenza di una 𝐶𝐶𝑥𝑥 :

     -     Se il valore dell’ingresso 𝐴𝐴 e della tensione sul nodo 𝑥𝑥 è la stessa, non succede nulla

     -     Se 𝐴𝐴 = 0 𝑉𝑉 e 𝑉𝑉𝑥𝑥 = 𝑉𝑉𝐷𝐷𝐷𝐷  transitorio di scarica attraverso il MOSFET

     -     Se 𝐴𝐴 = 𝑉𝑉𝐷𝐷𝐷𝐷 e 𝑉𝑉𝑥𝑥 = 0 𝑉𝑉  transitorio di carica attraverso il MOSFET, ma 𝐶𝐶𝑥𝑥 si carica ﬁno a 𝑉𝑉𝑥𝑥 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇
                                          Si dice che è stato trasmesso un 1 𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑

Questo caso fa capire due cose:

     1) Minore immunità ai disturbi
     2) Se si considera l’effetto body, si nota che a lungo andare 𝑉𝑉𝑇𝑇 cresce (perché cambia 𝑉𝑉𝑆𝑆 !!!), facendo
        diminuire ancora di più 𝑉𝑉𝑥𝑥 e si rischia si mandare un segnale troppo debole all’inverter dove il p-MOSFET
        si accende, facendo sì che ci sia un consumo statico di potenza!

Nel caso in cui l’unico P.T. sia un p-MOSFET, si ha il passaggio di uno 0 𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑.

La soluzione è quella di usare i pass-transistor complementari dove per ogni segnale ci sono un n-MOSFET ed
un p-MOSFET che possono quindi far passare, rispettivamente, uno 0 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 ed un 1 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓.


Tempi di commutazione nei P.T. complementari:

Bisogna usare un approccio approssimativo poiché il calcolo sarebbe troppo complicato.

Si prende di riferimento il P.T. complementare appena studiato e si nota che per entrambi i transitori di carica e
scarica si hanno sempre 3 fasi.
Quindi se 𝐴𝐴 = 𝐵𝐵 = 𝑉𝑉𝐷𝐷𝐷𝐷 (𝐴𝐴 è l’ingresso, 𝐵𝐵 è il segnale di controllo) si ha n-MOSFET e p-MOSFET:

     1) saturo – saturo
     2) saturo – triodo
     3) off – triodo

E’ di interesse la fare 2 dove �𝑉𝑉𝑇𝑇𝑝𝑝0 � < 𝑉𝑉𝑥𝑥 ≤ 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 (𝑉𝑉𝑥𝑥 ):

                                                                  2
                     𝑑𝑑𝑉𝑉𝑥𝑥                                         𝑉𝑉𝐷𝐷𝑆𝑆𝑝𝑝    𝛽𝛽𝑛𝑛                  2
              𝐶𝐶𝑥𝑥          = 𝛽𝛽𝑝𝑝 ��𝑉𝑉𝐺𝐺𝑆𝑆𝑝𝑝 − 𝑉𝑉𝑇𝑇𝑝𝑝 � 𝑉𝑉𝐷𝐷𝑆𝑆𝑝𝑝 −          � + �𝑉𝑉𝐺𝐺𝑆𝑆𝑛𝑛 − 𝑉𝑉𝑇𝑇𝑛𝑛 �
                      𝑑𝑑𝑑𝑑                                             2         2
                                                                                            (𝑉𝑉𝑥𝑥 − 𝑉𝑉𝐷𝐷𝐷𝐷 )2    𝛽𝛽𝑛𝑛                              2
                                          = 𝛽𝛽𝑝𝑝 ��−𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑝𝑝0 � (𝑉𝑉𝑥𝑥 − 𝑉𝑉𝐷𝐷𝐷𝐷 ) −                     � + �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑥𝑥 − 𝑉𝑉𝑇𝑇𝑛𝑛 (𝑉𝑉𝑥𝑥 )�
                                                                                                     2            2

Essendo un’equazione troppo complicata, si attua una soluzione alternativa.

Si sostituisce il P.T. con una RESISTENZA EQUIVALENTE indipendente dalle tensioni dei nodi 𝐴𝐴 ed 𝑥𝑥.

Quindi si ha 𝑉𝑉𝐴𝐴 = 𝑉𝑉𝐷𝐷𝐷𝐷 e sulla 𝑅𝑅𝑒𝑒𝑒𝑒 scorrono 𝐼𝐼𝑝𝑝 + 𝐼𝐼𝑛𝑛 :

                                                                                  𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑥𝑥
                                                                       𝑅𝑅𝑒𝑒𝑒𝑒 =
                                                                                   𝐼𝐼𝑝𝑝 + 𝐼𝐼𝑛𝑛

Essendo che non dipende troppo da 𝑉𝑉𝑥𝑥 si può considerare 𝑅𝑅𝑒𝑒𝑒𝑒 ≈ 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐.

Nel caso 𝑉𝑉𝑥𝑥 = 0, si pone 𝜆𝜆 = 0, si hanno entrambi i MOSFET saturi:

                                                              𝑉𝑉𝐷𝐷𝐷𝐷                            𝑉𝑉𝐷𝐷𝐷𝐷
                                     𝑅𝑅𝑒𝑒𝑒𝑒 (𝑉𝑉𝑥𝑥 = 0) =              =
                                                           𝐼𝐼𝑝𝑝 + 𝐼𝐼𝑛𝑛 𝛽𝛽𝑛𝑛                    2      𝛽𝛽𝑝𝑝              2
                                                                                    − 𝑉𝑉𝑇𝑇𝑛𝑛0 � + �𝑉𝑉𝐺𝐺𝑆𝑆𝑝𝑝 − 𝑉𝑉𝑇𝑇𝑝𝑝0 �
                                                                        2 �𝑉𝑉𝐺𝐺𝑆𝑆𝑛𝑛                    2
                                                                                              2𝑉𝑉𝐷𝐷𝐷𝐷
                                                       𝑅𝑅𝑒𝑒𝑒𝑒 =                               2                           2
                                                                  𝛽𝛽𝑛𝑛 �𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛0 � + 𝛽𝛽𝑝𝑝 �𝑉𝑉𝐷𝐷𝐷𝐷 − �𝑉𝑉𝑇𝑇𝑝𝑝0 ��

Quindi, essendoci un circuito RC, il transitorio di carica diventa:

                                                                                                           𝑡𝑡
                                                                                                       −
                                                                          𝑉𝑉𝑥𝑥 = 𝑉𝑉𝐷𝐷𝐷𝐷 �1 − 𝑒𝑒 𝑅𝑅𝑒𝑒𝑒𝑒𝐶𝐶𝑥𝑥 �


                                                                  𝑡𝑡𝑟𝑟𝑥𝑥 = ln(10) 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶𝑥𝑥 ≈ 2,3 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶𝑥𝑥

Per P.T. in serie, si usa sempre l’approccio approssimativo tramite sostituzione del P.T. con 𝑅𝑅𝑒𝑒𝑒𝑒 (solitamente
uguale per tutti).
Essendo che anche la capacità 𝐶𝐶 vista a valle di ogni P.T. è la medesima per tutti, si ottiene una rete di RC
distribuite per la quale si usa la formula di Elmore:

                                                       𝑛𝑛           𝑖𝑖                            𝑛𝑛
                                                                                                                𝑛𝑛(𝑛𝑛 − 1)
                                             𝜏𝜏𝑛𝑛 = � �𝐶𝐶𝑖𝑖 � 𝑅𝑅𝑗𝑗 � = 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶 � 𝑖𝑖 = 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶                          ∝ 𝑛𝑛2
                                                                                                                     2
                                                    𝑖𝑖=1           𝑗𝑗=1                       𝑖𝑖=1


                                                                              𝑡𝑡𝑝𝑝 = 𝑡𝑡𝑟𝑟𝑥𝑥 ≈ 2,3 𝜏𝜏𝑛𝑛


Dimensionamento dei P.T. complementari:

                                        1
Per un P.T. si ha che 𝑅𝑅𝑒𝑒𝑒𝑒 ∝               e 𝐶𝐶 ∝ 𝑊𝑊  𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶 ≈ 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐.
                                        𝑊𝑊

                             𝑛𝑛(𝑛𝑛−1)
Dato che 𝜏𝜏𝑛𝑛 = 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶                𝜏𝜏𝑛𝑛 è indipendente dal dimensionamento e si sceglie quindi quello minimo
                                2


                                                                             𝑆𝑆𝑛𝑛 = 1,             𝑆𝑆𝑝𝑝 = 𝜀𝜀

Da cui si ha 𝑡𝑡𝑓𝑓 = 𝑡𝑡𝑟𝑟 .

La dipendenza si presenta nel numero di P.T. e per evitare 𝑡𝑡𝑝𝑝 ≈ 2,3 𝜏𝜏𝑛𝑛 troppo elevati si spezzano le catene troppo
lunghe inserendo dei buffer.
                                                                                                                                   𝑛𝑛
Se si volesse spezzare una catena di 𝑛𝑛 transistor in serie e dividerli in 𝑚𝑚 blocchi ci sarebbero                                      blocchi da 𝑚𝑚
                                                                                                                                   𝑚𝑚
                                                  𝑛𝑛
transistor l’uno con l’aggiunta di − 1 buffer.
                                  𝑚𝑚
Si ha:

                                                                                              𝑚𝑚(𝑚𝑚 − 1)
                                                                           𝜏𝜏𝑚𝑚 = 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶
                                                                                                  2

                                                 𝑛𝑛    𝑛𝑛                                   𝑛𝑛(𝑚𝑚 − 1)    𝑛𝑛
                             𝑡𝑡𝑝𝑝 ≈ 2,3 𝜏𝜏𝑚𝑚        + � − 1� 𝑇𝑇𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 = 2,3 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶            + � − 1� 𝑇𝑇𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏
                                                 𝑚𝑚    𝑚𝑚                                        2        𝑚𝑚

                                                             𝜕𝜕𝑡𝑡𝑝𝑝                𝑛𝑛 𝑛𝑛
                                                                    = 2,3 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶 − 2 𝑇𝑇𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 = 0
                                                             𝜕𝜕𝜕𝜕                  2 𝑚𝑚

                                                                                               2𝑇𝑇𝑏𝑏𝑏𝑏𝑏𝑏
                                                                             𝑚𝑚𝑜𝑜𝑜𝑜𝑜𝑜 = �
                                                                                              2,3 𝑅𝑅𝑒𝑒𝑒𝑒 𝐶𝐶

Solitamente si ha 𝑚𝑚𝑜𝑜𝑜𝑜𝑜𝑜 = 3.
Svantaggi dei P.T. complementari:

L’utilizzo di P.T. complementari, anziché quelli normali, prevede un aumento importante del numero di transistor
(che comunque rimane sotto a quello delle logiche CMOS).

Oltre a questo si ha il problema del dover avere tutti i segnali anche negati ed il fatto che aumentano le capacità
e quindi la potenza dinamica.


Una soluzione può essere il TRANSISTOR DI RIPRISTINO, ossia un transistor p-MOSFET (per esempio) che ha il
Gate collegato all’uscita dell’inverter (il cui ingresso è connesso al nodo 𝑥𝑥).

Si ha quindi un solo n-MOSFET ed un solo p-MOSFET (ulteriormente all’inverter) per una NAND.

Si risolvono i problemi dei segnali negati e del numero di transistor presenti.

Il problema non si pone durante la carica di 𝐶𝐶𝑥𝑥 poiché il p-MOSFET connesso a 𝑉𝑉𝐷𝐷𝐷𝐷 fa sì che la capacità si carichi
anche quando n-MOSFET è spento (1 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓).
Si pone quando 𝐶𝐶𝑥𝑥 deve scaricarsi perché il p-MOSFET si oppone alla scarica, rallentandola e rendendo
necessario che n-MOSFET sia più conduttivo, aumentandone il dimensionamento e di conseguenza il valore di
𝐶𝐶𝑥𝑥 che aumenta a sua volta la potenza spesa.


LOGICHE DINAMICHE CMOS:

Come detto, si distinguono le fasi di precarica / prescarica e di valutazione dell’ingresso, ma per poterlo fare è
necessario un segnale di controllo che detti quando queste fasi iniziano e ﬁniscono: il segnale di CLOCK.

La funzione logica è deﬁnita solamente dal PD o dal PU ed è implementata nella stessa maniera con cui lo era
nella logiche statiche CMOS.

Se la funzione è implementata tramite un PD si parla di 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 , se con un PU di 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑝𝑝 .

Con 𝑁𝑁 ingressi ci sono in totale 𝑁𝑁 + 2 MOSFET.

Il segnale di clock determina:

     -    𝜙𝜙 = 0      fase di precarica per il 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛
                      fase di valutazione per il 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑝𝑝

     -    𝜙𝜙 = 1      fase di valutazione per il 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛
                      fase di prescarica per il 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑝𝑝

Un lato positivo è che non c’è mai un percorso conduttivo tra 𝑉𝑉𝐷𝐷𝐷𝐷 e massa  potenza statica nulla, nessuna 𝐼𝐼𝐶𝐶𝐶𝐶

Per il 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 , quando 𝜙𝜙 = 0, 𝐶𝐶𝐿𝐿 si carica ﬁno a valore di 𝑉𝑉𝐷𝐷𝐷𝐷 ( 𝐹𝐹 = 1) e poi, nella fase di valutazione con 𝜙𝜙 =
1, se il PD è attivo, si ha 𝐹𝐹 = 0, altrimenti 𝐹𝐹 rimane al valore di 𝑉𝑉𝐷𝐷𝐷𝐷 .

Questo processo viene ripetuto ogni ciclo di clock ed è estremamente importante che gli ingressi siano costanti
nella fase di valutazione!!!

Ulteriori caratteristiche:

     -    𝑉𝑉𝑂𝑂𝑂𝑂 = 𝑉𝑉𝐷𝐷𝐷𝐷 e 𝑉𝑉𝑂𝑂𝑂𝑂 = 0 𝑉𝑉

     -    minore immunità ai disturbi quando il nodo di OUT è isolato (quando 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 e 𝐹𝐹 = 1 il nodo non ha
          modo di rimanere ﬁsso al potenziale a cui è e quindi si scarica).
          I margini di rumore sono: 𝑁𝑁𝑀𝑀𝐻𝐻 = 𝑉𝑉𝐷𝐷𝐷𝐷 − 𝑉𝑉𝑇𝑇𝑛𝑛 𝑝𝑝𝑝𝑝𝑝𝑝 𝐹𝐹 = 1 e 𝑁𝑁𝑀𝑀𝐿𝐿 = 𝑉𝑉𝑇𝑇𝑛𝑛 𝑝𝑝𝑝𝑝𝑝𝑝 𝐹𝐹 = 0  𝑁𝑁𝑀𝑀𝐻𝐻 > 𝑁𝑁𝑀𝑀𝐿𝐿
Per il calcolo dei tempi di ritardo si fa la somma tra i tempi delle due fasi.

Nel caso di 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 si ha:

     -     tempo di precarica che è uguale a 𝑡𝑡𝑟𝑟 di un inverter
     -     tempo di valutazione che dipende dal valore di 𝐹𝐹
              o se 𝐹𝐹 = 1  𝑡𝑡𝑟𝑟 = 0 (𝐶𝐶𝐿𝐿 è già carico)
              o se 𝐹𝐹 = 0  𝑡𝑡𝑓𝑓 si calcola come nelle logiche statiche CMOS col dimensionamento equivalente

Il tempo di precarica / prescarica, per quanto piccolo possa essere, è comunque tempo che può essere usato
per eseguire altre operazioni.


La diminuzione del numero di MOSFET fa sì che 𝐶𝐶𝐼𝐼𝐼𝐼 ↓  meno self-loading  logiche dinamiche più veloci!!!

La potenza statica non c’è così come quella di cortocircuito, però rimane quella dinamica:

                                                               2
                                            𝑃𝑃𝑑𝑑𝑑𝑑𝑑𝑑 = 𝐶𝐶𝐿𝐿 𝑉𝑉𝐷𝐷𝐷𝐷 𝒻𝒻𝐶𝐶𝐶𝐶 𝑃𝑃0→1 ,   𝑃𝑃0→1 = 𝑃𝑃0 𝑃𝑃1

                                                                                                        2
Nel caso di 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 si ha che la precarica porta sempre 𝐹𝐹 = 1  𝑃𝑃1 = 1  𝑃𝑃𝑑𝑑𝑑𝑑𝑑𝑑 = 𝐶𝐶𝐿𝐿 𝑉𝑉𝐷𝐷𝐷𝐷 𝒻𝒻𝐶𝐶𝐶𝐶 𝑃𝑃0

                  𝑁𝑁
Essendo 𝑃𝑃0 = 𝑛𝑛0 con 𝑛𝑛 ingressi, si ha che la potenza dinamica delle logiche dinamiche è molto più alta rispetto a
               2
quella delle logiche statiche.


Logiche domino:

Un 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 può accettare in ingresso commutazioni lente 0 → 1 che inducono solo un 𝑡𝑡𝑝𝑝 maggiore.
Un 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 fornisce in uscita commutazioni 1 → 0 che NON possono essere ingresso di un 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 .

Un 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑝𝑝 può accettare in ingresso commutazioni lente 1 → 0 che inducono solo un 𝑡𝑡𝑝𝑝 maggiore.
Un 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑝𝑝 fornisce in uscita commutazioni 0 → 1 che NON possono essere ingresso di un 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑝𝑝 .

Per ovviare al problema si creano catene dette logiche domino che consistono nell’alternare un 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑛𝑛 ed un
𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝜙𝜙𝑝𝑝 in modo da non avere problemi con gli ingressi.

Questo porta con sé lo svantaggio di dover avere due segnali di clock (normale e negato) poiché la valutazione
deve avvenire nello stesso lasso temporale per tutti i blocchi.

Nel caso in cui non si voglia alternare, si può inserire un inverter tra blocchi dello stesso tipo, ma aumentando 𝑡𝑡𝑝𝑝 .
