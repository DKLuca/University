---
fonte: "esame digitale 17_06_2025.pdf"
metodo: "ocr"
da_rivedere: true
---

[oqemeeNom (a

Matricola
Data 17 Giugno 2025

Prova Scritta di Complementi di Elettronica II

17 Giugno 2025
Sia Vpp=1.2V e si assumano i seguenti parametri tecnologici per i MOSFET:

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Si riportino negli spazi bianchi all’interno del testo l’espressione analitica ed il valore nu-
merico dei risultati.

BL1 BL2

 

 

 

 

   
  
  
 

ous 45- or fo. moma
zza delle interconnessioni e alla capacita
panecith prodotto da M1 oppure M3 sulle
izione, assumendo Lsp=2Luin-

della interconnessione che realizza la bitline
1e, sapendo che la lunghezza delle regioni

a occupa un’area pari @
od ce picnic


---

Soluzione della Prova Scritta di Complementi di Elettronica II
17 Giugno 2025

1) La capacita per unita di lunghezza della bitline data da:

for 2h Eor
C= 7. Y + inf(@Tee + AYA

Inotre, siccome M1 ed M3 hanno dimensionamento minimo ed la lunghezza delle regioni di diffusione
a e drain vale Lep=2Ly;N, la capacita C..4 prodotta da ogni cella connessa alle bitline
ta

 

= 0.254f F/jum

Coe ® 2L341~Cjo = 50.40F

Per calcolare il massimo numero di celle connesse alle bitline compatibili con una capacita di 0.5 pF,
partiamo notando che, siccome la cella di memoria é quadrata ed ha un'occupazione d’area pari a
0.49j:m2, allora il lato della cella deve essere 0.7:m. La capacita complessiva Co.7 che corrisponde
ad un tratto di bitline lungo 0.7m vale pertanto Co.7=0.7 -c+C.eu=0.228 f F, in quanto comprende
la Coey di una cella di memoria. Il massimo numero di celle che @ possibile connettere ad una bitline
del settore per avere una capacita minore di 0.5 pF vale quindi Ngz=0.5pf /Co.7~2192.

2) Supponendo che la polarizzazione della word line di scrittura WW L sia pari Vpp, allora la tensione

Vx corrispondente alla scrittura di un UNO logico pari a Vx,.=Vpp—Vro=0.85, , dove si @ usato
Vro per la soglia di M1 perché si ha y=0 nella tabella dei parametri dei transistori.
Durante la scrittura di uno ZERO logico avremo la WW L polarizzate a Vpp e la bitline polarizzata
a massa, mentre Vx rappresenta la tensione di drain del transistore M1 attraverso il quale si
scarica il nodo X. Il transitorio @ quasi uguale al transitorio di discesa di un invertitore CMOS, ad
eccezione del fatto che la Vpg iniziale di M1 @ Vpsr=Vx,=Vpp—Vro=0.85 V invece di Vpp=1.2
V. In particolare, siccome Vpsr=Vpp—Vro, durante il transitorio M1 lavora sempre in regione
triodo. Usando i noti risultati del transitorio di discesa dell'invertitore, il tempo di discesa pud
essere valutato come

a 2Cs5 1 = 2(Vpp — Vro) — er
w0™ T- Bf 2(Vpp — Vro) | Vosr 2(Vop — Vro) — Vos1

dove Cs=2Cy1=0.70f F (con Cun=(Lig1n~Coz + 2LMinCoso)~0.35 fF), Sn,ai=! @ il dimension-
amento di M1, Vps;=0.85 V e Vps é infine specificato nel testo come Vpsr=0.1Vpp=0.12V.

Sostituendo i valori numerici, otteniamo tyo~11-9ps.

3) Durante la fase di ritenzione ® il transistore M1 che, a causa della sua I,77, pud scaricare la
capacita Cs di immagazzinamento dell’informazione. Si supponga che sul nodo X sia memorizzata
la tensione Vx;=0.85 V corrispondente ad un UNO logico e che la BL1 sia a massa. In queste
condizioni M1 ha una Vpg iniziale pari Vy,,=0.85 V mentre ha Vgs=0. In tali condizioni la sua

corrente di sotto-soglia vale

V;
Togs = S Ieten exP (-—*-) = 15.9pA

 

La scarica della capacita Cs avviene con una corrente J,ss costante, almeno fino a quando Vps
rimane maggiore di tre o quattro volte Vin=26mV, quindi il tempo di degrado della tensione Vx si
trova dividendo semplicemente la variazione di carica per la corrente di perdita, Pertanto otteniamo

~ 94
Togs “

ts0%
