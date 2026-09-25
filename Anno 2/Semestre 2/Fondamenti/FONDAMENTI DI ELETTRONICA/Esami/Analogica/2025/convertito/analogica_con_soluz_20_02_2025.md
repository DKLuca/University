---
fonte: "analogica_con_soluz_20_02_2025.pdf"
metodo: "ocr"
da_rivedere: true
---

| Fe di Blettroni
Prom ered Eos on

Nome: ieee ccekaWe id ens dedeoeds 1s. CQQMOtOe: weveseduued dese wade eeeuee .. Matrieola: ee eeebekeeee
Paunti Aseegnati: Fulawedlestesd 406s beFHAGek cD cUReedihs thee] MY ebteds ove

1. Gon riferimento al circuit di Fig. 1, trovare il punto di lavoro del circuito, caleolando tutte le
Yonsioni ¢ correnti. (7 punti)

2. Disegnare il circuito equivalente ai piccoli segnali ¢ calcolare i parametri differenziali dei componenti,
tenendo conto anche degli effetti capacitivi del BIT. (5 punti)

3. a kidads Gal chreuito 1 coudenmetore C;, deternlaate la metrics ammettense dal timeneote ele-
cuito (quindi dal nodo Vp in avanti). (10 punti)

4. Sfruttando la matrice calcolata sopra, trovare l'espressione della funzione di trasferimento Ay(s) =
V,/V; (tenendo stavolta conto del condensatore C;). (8 punti)

Ry = 6 EN, Ro = 10 kN, Ry = 4.2 kN, Voc = 15 V, Vay = 25 mV, Is = 10-" A, Bp = By = 20,
C= 10 pF, Co = 2 pF, @; = 1 V, tr = 100 ps.

Vcc

 


---

Soluzione del compito di Fondamenti di Elettonica
20 febbraio 2025

1. Il BIT é acceso e in regione normale (Ve > Vg). Indicando con J; la corrente sulla generica
resistenza R; con i = 1,2,3, possiamo quindi scrivere i] seguente set di equazioni statiche:

 

 

 

Veo = Ril +Vee+ Reals (1)
I.
Veo = Rih+ Roh =Rih + Ro(h —Is)=Rh+t Re (1 =35) (2)
Br+l Br+1 (2)
I = Ico= Is ex >. 3)
pr ° Begin \ Va :

Sostituendo Eq.(2) nella (1) e ponendo Eq.(3) in forma logaritmica otteniamo il seguente sistema

non lineare:

 

 

 

=) ( R3Ry Ry )

Vi = o{(1+— R 4

cc Vee ( Te + Iz | Rg + Ro tao] (4)
wy Iz Br

RL G — (5)

il quale pué essere risolto con il metodo iterativo, ottenendo Vag = 0.6492 V e J3 = 1.993 mA. Le
altre correnti risultano valere Jp = J3/(Br +1) = 94.9 uA, Ic = Brlp = 1.898 mA, 1; = 997 pA e
Ty = 902 A. Si ottiene quindi che la tensione di base vale Vg = RoJ2 = 9.02 V.

2. I parametri differenziali del BJT valgono: rre = Vin/Ip = 263 2 € gm = I¢/Vin = 75.92 mS. Le
capacita legate alle due giunzioni sono pari a Cgp = TF9m = 7.59 pF e Cac = Cyo/\/1— Vac/P; =
0.76 pF. Il circuito equivalente ai piccoli segnali risulta essere quello indicato in Fig.1, dove Rp =
R,||R2 = 3.75 kQ:

 

 

 

 

 

 

a j; Cbe ib
i I
a vb t Lo vo vb — vo
= .
157 ee “io ss “io
Cbe gmvybe emvbe
=f 2
Fig. 1 Fig. 2

3. Con riferimento al circuito qui sopra, togliamo come indicato il condensatore C; e calcoliamo la
matrice ammettenza del circuito tra i nodi vp e vp. Vista la presenza dei condensatori, la matrice
va calcolata nel dominio delle frequenze. Inoltre sfruttiamo le proprieta delle matrici ammettenza,
per semplificare i] calcolo dei componenti della matrice. In particolare, visto che Rp e Cgc sono in
parallelo alla porta di ingresso, Ry é in parallelo alla porta di tscita, mentre Cpr collega ingresso
e uscita, togliamo tutti questi.componenti per poi inserirli direttamente nella matrice finale. Il
circuito che rimane é quello di Fig. 2, per il quale calcoliamo Ja matrice |Y’|. Le componenti di tale

matrice valgono:

 

 

r Ig 1

i = —_ = ;

GY Vole, ee ”
Ip i SS.

Yj,(s) = =|. =-— .

i2(8) = Holga 10 te (7)
Ree) ‘ Re,
‘s 6 i . 3 x ot 4 rt ; ie

 


---

 

=, Bs Io « mel; | . a
Yoo) = 72] = on 8
cs Elie io ite a
Yo0(s) . Vo ae Im Neen (9)

 

A questo punto é facile aggiungere il contributo di Rp, Cac, Cae e Ra, per cui la matrice totale

‘ oe +s(Cec+ Cae) are —sCar
IY(s)|=| : (10)
Henge = CHB Ao +9m+ Re + SCBE

4, Indicando con Z; l'impedenza di ingresso vista al nodo Vg, il guadagno di tensione pudé essere
calcolato scomponendolo come: ;

| =o “2V0 Ve
Ay(s) = yi (11)
e sfruttando le espressioni che permettono di calcolare le funzioni di rete dalle componenti della

Vo —Yo1 = +9m+sCBE

 

Va Bint Yas ~ i +9m+ we t+8CBe
7 / ;
1 Wil ocees iP (+ + Im + sCpe) ‘ (-2+ - sCoe)
Y= == -—— =—+——+8(Cact Cae) + ;
Ben a ete * Rp eee GPP) + 9m+ Be + 8CaB

 

    

Splash eae (2)

 

' | RRS ae Pee
a. ; 1 SH Mea pence inks } etn mee Xin 2.8 4
© | ies 46(Cac+ Can +O) = 2 = 2
i i. 7a (LtanteCne) eeceans f& cae + s(Cac + Car + 2) img SCBE
