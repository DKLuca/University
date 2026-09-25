# Conversione PDF/immagini -> Markdown

Script per convertire in automatico PDF e immagini (appunti scansionati, dispense, esami)
in file `.md`, senza toccare gli originali.

## Cosa fa

Per ogni PDF/JPG/PNG trovato in una cartella, crea un file `.md` corrispondente dentro
una sottocartella `convertito/` accanto all'originale (es. `Materia/convertito/nome.md`).
Non sovrascrive mai gli originali né gli `.md` scritti a mano altrove.

Ogni `.md` generato ha un frontmatter con:
- `fonte`: nome del file originale
- `metodo`: come e' stato ottenuto il testo (vedi sotto)
- `da_rivedere`: `true` se il testo va controllato a mano (quasi sempre per l'OCR)

Metodi possibili:
- `testo-pdf`: il PDF aveva già testo digitale estraibile (veloce, affidabile).
- `ocr`: PDF/immagine scansionata, testo riconosciuto via OCR (Tesseract, italiano+inglese).
  Da rivedere sempre: l'OCR su scrittura a mano in particolare può contenere molti errori.
- `ocr-parziale`: l'OCR ha superato il tempo massimo consentito per un singolo file ed è
  stato interrotto: contiene solo le prime pagine.
- `saltato-grande` / `saltato-molte-pagine`: file troppo grande o con troppe pagine per
  l'OCR automatico (probabile libro/raccolta scansionata) -> saltato di proposito,
  va convertito a mano se serve.
- `non-convertibile`: il file ha estensione `.pdf` ma non è davvero un PDF (es. un file
  di testo/dati rinominato per errore).

## Uso

```bash
python3 converti_tutto.py --root /percorso/repo [opzioni]
```

Opzioni principali:
- `--only "sottostringa"`: limita alle cartelle il cui percorso contiene questa stringa
- `--force`: riconverte anche i file che hanno già un `.md` in `convertito/`
- `--workers N`: quante conversioni in parallelo (default 2, adatta al numero di core)
- `--timeout N`: secondi massimi per singola operazione (rasterizzazione/OCR di una pagina)
- `--file-timeout N`: secondi massimi totali per un singolo file durante l'OCR pagina per
  pagina, oltre i quali si ottiene un `ocr-parziale` invece di bloccare tutto
- `--max-pages N`: sopra questo numero di pagine, salta l'OCR (default 40)
- `--max-ocr-mb N`: sopra questa dimensione (MB) senza testo estraibile, salta l'OCR (default 15)
- `--dpi N`: risoluzione di rasterizzazione per l'OCR (default 200; abbassarla aiuta con
  pagine molto grandi/lente)

Lo script è **ripetibile**: si può rilanciare più volte, salta automaticamente i file già
convertiti (a meno di `--force`), quindi va bene interromperlo e rilanciarlo.

## Cosa controllare a mano

Cerca nei file generati `da_rivedere: true` (quasi tutto ciò che è passato per OCR), e in
particolare tutti i file con metodo `saltato-grande`, `saltato-molte-pagine`,
`ocr-parziale` o `non-convertibile`: per questi la conversione automatica non è stata
fatta o è incompleta.
