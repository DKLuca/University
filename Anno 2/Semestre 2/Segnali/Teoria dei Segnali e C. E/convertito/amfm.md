---
fonte: "amfm.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

La portante viene recuperata con un filtro passa-banda (seguito da un
PLL). Si assume che s(t) abbia contenuto spettrale trascurabile attorno
alla frequenza 0



     Modulazione di
     Ampiezza(AM)	

  Modulazione di
Argomento (PM, FM)	

         Modulazione di Ampiezza	

DSB e SSB sono sistemi di modulazione di ampiezza, in cui l’ampiezza
della portante viene modulata dal segnale di informazione (nel sistema
SSB, il segnale modulato viene filtrato con un filtro opportuno)	

	

DSB, e soprattutto SSB, permettono un uso efficiente dello spettro (banda
B o 2B, dove B è la banda del segnale di informazione)	

	

Più alta è la frequenza della portante, più ampia è, con gli stessi dispositivi,
la larghezza di banda disponibile per la trasmissione, che sarà suddivisa in
vari canali mediante tecniche di Frequency Division Multiplexing	

	

Frequency Division Multiplexing
           (FDM)	

         Modulazione di Ampiezza	

Frequenze radio relativamente basse (onde lunghe: 144 Khz – 351 KHz,
onde medie: 530 KHz – 1,7 MHz, onde corte: 1,7 MHz – 30 MHz),
richiedono un’alta efficienza spettrale (e antenne di dimensioni adeguate)	

	

Inoltre, queste possono propagarsi a grande distanza, a causa di modi di
propagazione come l’onda di terra (onde lunghe e medie) e la
propagazione ionosferica (onde corte) – fenomeni di rifrazione dell’onda
elettromagnetica nello strato terra-aria o di riflessione nella ionosfera
permettono all’onda di seguire la curvatura terrestre e di propagarsi a
grande distanza -	

	

DSB e SSB sono le modulazioni più usate per le trasmissioni sulle onde
corte, eccetto che il braodcasting, in cui si utilizza la modulazione AM di
inviluppo 	

La portante viene recuperata con un filtro passa-banda (seguito da un
PLL). Si assume che s(t) abbia contenuto spettrale trascurabile attorno
alla frequenza 0
                      Recupero della portante


• Sistemi SC (Suppressed Carrier: es. DSB-SC) Si utilizza una non-linearità
  che introduce una riga spettrale, che viene poi selezionata da un filtro
  passa-banda (seguito da un PLL)
            vR (t) = s(t) cos(2 f0t), vR2 (t) = s2(t) cos2(2 f0t)
          s2(t) = Ms + s (t), vR2 (t) = Ms cos(2 2f0t) + rumore.
  La portante viene poi recuperata con un filtro passa-banda (seguito da un
  PLL).


                                          Costa’s loop per recupero	

                                          portanti in quadratura	

                              Ergodicità

• Legge dei grandi numeri: xi v.a. indipendenti ed equidistribuite:
                          x1 + x2 + · · · + xN
                                               ⇥ E[x]
                                   N
• Ergodicità di un processo aleatorio stazionario. Per T ⇥ +⇤
                         1 T
                              T x(t) dt ⇥ E[x(t)] = mx
                        2T
                        1 T 2                  2
                             T x (t) dt ⇥ E[x (t)] = Mx
                       2T
                         1 T
                                x(t)x(t + ) dt ⇥ rx( )
                        2T T
• Definito xT (t) = x(t)rect(t/T )
                            1
                              E[|XT (f )|2] ⇥ Rx(f )
                            T
  Il metodo di stima spettrale Periodogramma si basa sulla relazione prece-
  dente
Modulazione AM di inviluppo	

Modulazione AM di inviluppo	

Amplitude Modulation	

Segnali nella AM	

Ricevitore	

Ricevitore	

Ricevitore	

Ricevitore	

Ricevitore	

Ricevitore	

Prestazioni (piccolo rumore)	

Modulazione di Argomento	

Modulazione di Argomento	

Modulazione di Argomento	

Segnale sinusoidale (PM)	

Segnale sinusoidale	

Segnale sinusoidale	





            Criterio: 90% Energia totale	

Segnale sinusoidale (FM)	

          Formula di Carson	

Modulazione di fase:	





Modulazione di frequenza:	

            Demodulatore FM	

Derivatore:	





     Segnale AM	
          “portante”	

Prestazioni	




quadrato fattore di forma	

   Esempio: FM commerciale	





Ulteriore guadagno di 6-10 dB con enfasi-deenfasi	

(amplificazione alte frequenze in tx - attenuazione in rx)
