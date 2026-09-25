---
fonte: "soluzione_190615.pdf"
metodo: "testo-pdf"
da_rivedere: false
---

Soluzione della prova scritta di Fondamenti di Elettronica

                       del 11 settembre 2015, parte digitale

1) Il pull-up implementa la funzione 𝑃𝑈 = 𝐴̅ 𝐵̅ + 𝐶̅ (𝐴̅ + 𝐵̅) mentre per il pull-down 𝑃𝐷 =
   𝐴𝐵 + 𝐶 (𝐴 + 𝐵). Si può verificare in maniera semplice che ̅̅̅̅
                                                               𝑃𝐷 = 𝑃𝑈 = 𝐹
2) I tempi di discesa /salita sono dati da:
                                                2𝐶𝐿
                                   𝑡𝑓,𝑟 =    ′
                                                         𝐹 (𝑉𝑇 /𝑉𝐷𝐷 )
                                            𝛽𝑛,𝑝 𝑆𝑒𝑞 𝑉𝐷𝐷

    con F= 2.09, dove usiamo 𝛽𝑝′ o 𝛽𝑛′ a seconda che si tratti di carica o scarica. Per i diversi casi
otteniamo:
                   A     B     C     Seq               tf [ps]          tr [ps]
                   0     0     0     (½+2/3) 2                              330
                   0     0     1     ½ 2                                    774
                   0     1     0     ½ 2                                    774
                   0     1     1     ½                     774
                   1     0     0     ½ 2                                  774
                   1     0     1     ½                     774
                   1     1     0     ½                     774
                   1     1     1     (½+2/3)               330


3) Dalla tabella della verità si vede che PF=0.5, quindi:
            2
   𝑃𝐷 = 𝐶𝐿 𝑉𝐷𝐷 𝑓𝐶𝐾 𝑃𝐹 (1 − 𝑃𝐹 ) = 20.25𝜇𝑊
4) Essendoci l’invertitore, la rete di pass-transistor deve implementare la funzione 𝐹̅ = 𝑃𝐷 che
abbiamo nel pull-down del gate CMOS. Una possibilità è la seguente:
