---
fonte: "esame digitale 25_02_2025.pdf"
metodo: "ocr"
da_rivedere: true
---

Prova Scritta di Circuiti e Sistemi Elettronici
(DIGITALE)
25 febbraio 2025

- Si consideri una tecnologia CMOS di cui sono noti i seguenti parametri:

nMOS | pMOS
8! [wA/V?} 180 100
Coz (fF /um?) | 11.5 | 11.5

Ceso [fF /um] 0.5 0.5
Vro [V] 0.3 0.3

 

 

 

 

 

 

Inoltre, Larry = 300 nm, il ritardo Papeteanticn della tecnologia & too = 9 ps e il parasitic effort

dell’invertitore di riferimento @ pyiy = 0.95.
Se non diversamente specificato, si assuma che i gate siano progettati per avere uguali tempi

di salita e di discesa di caso peggiore e che sia 1 = Lyyy per tutti i transistori.

1. (8 Punti) Si consideri il gate logico CMOS G, che implementa la funzione Fg,(A,B,C,D) =
A(BC + D). Calcolare il logical effort (g¢1) ed il parasitic effort (pg) di tale gate.

Si consideri quindi il circuito di seguito riportato, che fa uso del gate Gj, e si risponda ad i quesiti proposti
sapendo che C; = 280 fF e che il dimensionamento dei transistori che compongono il pull-down del gate
NAND a 4 ingressi @ S, vanpa = 2. I transistori di pull-down dei tre gate connessi a valle del nodo X

hanno lo stesso dimensionamento, di seguito indicato con S,. .

 

 

 

 

 

 

 

 

 

 

 


---

Soluzione della prova Seritta di Clreuiti e Sistemi Blettroniel
(DIGITAL)
25 febbraio 2025

1. Limplementagione in logica CMOS del gate G, @ riportata nella figura sottostante.
L'analisi dei tempi di salita @ di discesa ci permette quindi di stabilire che,

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Vv
nel caso peggiore, la salita avviene attraverso la serie di due pMOS, mentre la
a4 bc discesn attraverso la serie di 3 nMOS, Segue che Speq = Sp/2 © Sag = Sy/3.
| Imponendo t, = ty si ottiene
D ,
ng, = * = 26h = a
einai Sn 36, 3
A Il logical effort ed il parasitic effort di G, possono essere calcolati imponendo
se Vuguaglianza della resistenze equivalenti del gate G, ¢ dell’invertitore di riferi-
b mento (da cui S, = 3S,,;~v) ed utilizzando le espressioni
c—4 Ge 4 Coa
= ae Gaye Cine

Sapendo che Cg, = Sp(1+aG,)Cm1, Cp, = Sn(1+2aG,)Cp, Crvv = Sn inv (l+e)Can e che Cp /Crn =
Pin, Si ottiene gq, = 2.36, pg, = 3.46.
Si ricorda che Cy = L3y;y Cor + 2LminCaso = 1.36 fF.

 
 
 

2. Oltre al gate G, nel circuito sono presenti solo gate NAND § NOR pe yaa e 9)

gnoRn = BY, pNANDn = PNORn = N° Pinv- Segue che g
pror2 = 1.9, gvAND2 = 1.36, pyvanD2=19.
Il path logical effort per il percorso IN + OUT vale G = gnanp,4* 9NOR2* 9G, = 8.02.

Il path branching effort @ equivalente al branching effort del gate NORg.

7 _ Coss—path+Co, _ (1+ §) + (1 +26) + (1+ fe) _
B= bwona = He” = oe = 3.955.

 
   
 

Infine, sapendo che Sp,wanp.s = 2, si pud caleolare Cry = Sn,wanpa(l + §)Cm = 3.87 fF. Si pud qu

calcolare il path effort come —

P= GBH =GBOOX ~ 2294.

    
   

3. eee So stage ali ti Pes eee Ic


---

 
    
    
 
    

 

procedere a ritroso sapendo che, per ogni stadio, deve valere la cor

Cour _ 771 (F

 

Cinv3 =

 

Cinv2 = os = 21.23 fF

Cinvi = Cinv2 _ 5 95 gp

 

C,
Cnor2 = ae = 6.79 fF
