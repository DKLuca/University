#!/usr/bin/env python3
"""
Conversione a cascata: scandisce la repo e per ogni PDF/immagine trovato
in una cartella "Materia" crea un file .md dentro una sottocartella
"convertito/" accanto all'originale. Non tocca mai i file originali né
gli .md già scritti a mano altrove nella stessa cartella.

Uso:
  python3 converti_tutto.py --root /percorso/repo [--only "sottostringa"] [--force] [--dpi 200] [--workers 2] [--timeout 90] [--file-timeout 240] [--max-pages 40] [--max 999999]
"""
import argparse
import os
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

SKIP_DIRS = {".git", "node_modules", "sito-quartz", "convertito", "__pycache__"}
EXTS_PDF = {".pdf"}
EXTS_IMG = {".jpg", ".jpeg", ".png"}
TESS_LANG = "ita+eng"

def log(msg):
    print(msg, flush=True)

def sh(cmd, timeout=None):
    return subprocess.run(cmd, capture_output=True, timeout=timeout)

def pdftotext_layout(pdf_path, timeout):
    try:
        r = sh(["pdftotext", "-layout", pdf_path, "-"], timeout=timeout)
    except subprocess.TimeoutExpired:
        return ""
    if r.returncode != 0:
        return ""
    return r.stdout.decode("utf-8", errors="replace")

def pdf_page_count(pdf_path, timeout=15):
    try:
        r = sh(["pdfinfo", pdf_path], timeout=timeout)
    except subprocess.TimeoutExpired:
        return None
    if r.returncode != 0:
        return None
    for line in r.stdout.decode("utf-8", errors="replace").splitlines():
        if line.lower().startswith("pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return None
    return None

def ocr_image(img_path, timeout):
    try:
        r = sh(["tesseract", img_path, "stdout", "-l", TESS_LANG], timeout=timeout)
    except subprocess.TimeoutExpired:
        return "", "timeout OCR immagine"
    if r.returncode != 0:
        return "", r.stderr.decode("utf-8", errors="replace")
    return r.stdout.decode("utf-8", errors="replace"), ""

def ocr_pdf(pdf_path, dpi, timeout, file_deadline):
    with tempfile.TemporaryDirectory() as tmp:
        prefix = os.path.join(tmp, "page")
        try:
            r = sh(["pdftoppm", "-png", "-r", str(dpi), pdf_path, prefix], timeout=timeout)
        except subprocess.TimeoutExpired:
            return "", "timeout rasterizzazione"
        if r.returncode != 0:
            return "", r.stderr.decode("utf-8", errors="replace")
        pages = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
        if not pages:
            return "", "nessuna pagina rasterizzata"
        parts = []
        for i, p in enumerate(pages, 1):
            if time.monotonic() > file_deadline:
                parts.append(f"\n\n<!-- OCR interrotto: superato il tempo massimo per file dopo {i-1}/{len(pages)} pagine -->\n\n")
                return ("\n\n---\n\n".join(parts)), "parziale-timeout"
            text, err = ocr_image(os.path.join(tmp, p), timeout=timeout)
            if err:
                parts.append(f"\n\n<!-- errore OCR pagina {i}: {err.strip()} -->\n\n")
            else:
                parts.append(text)
        return ("\n\n---\n\n".join(parts)), ""

def is_probably_digital(text, min_chars=200):
    return len(text.strip()) >= min_chars

def convert_file(path, dpi, timeout, max_ocr_mb, max_pages, file_timeout):
    ext = os.path.splitext(path)[1].lower()
    if ext in EXTS_PDF:
        size_mb = os.path.getsize(path) / (1024 * 1024)
        is_large = size_mb > max_ocr_mb
        probe_timeout = 15 if is_large else timeout
        text = pdftotext_layout(path, timeout=probe_timeout)
        if is_probably_digital(text):
            return text, "testo-pdf", None
        if is_large:
            return None, "saltato-grande", f"{size_mb:.0f} MB senza abbastanza testo estraibile in {probe_timeout}s: probabile libro/raccolta scansionata, OCR automatico saltato"
        pages = pdf_page_count(path)
        if pages is not None and pages > max_pages:
            return None, "saltato-molte-pagine", f"{pages} pagine (limite {max_pages}): probabile scansione lunga, OCR automatico saltato"
        file_deadline = time.monotonic() + file_timeout
        ocr_text, err = ocr_pdf(path, dpi=dpi, timeout=timeout, file_deadline=file_deadline)
        if err == "parziale-timeout":
            return ocr_text, "ocr-parziale", None
        if err:
            return None, "errore", err
        return ocr_text, "ocr", None
    elif ext in EXTS_IMG:
        text, err = ocr_image(path, timeout=timeout)
        if err:
            return None, "errore", err
        return text, "ocr", None
    return None, None, None

def write_markdown(out_path, source_name, method, text):
    da_rivedere = "true" if method in ("ocr", "ocr-parziale") else "false"
    frontmatter = (
        "---\n"
        f'fonte: "{source_name}"\n'
        f'metodo: "{method}"\n'
        f"da_rivedere: {da_rivedere}\n"
        "---\n\n"
    )
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write((text or "").strip() + "\n")

def find_todo(root, only, force):
    todo = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if only and only not in dirpath:
            continue
        for fname in sorted(filenames):
            ext = os.path.splitext(fname)[1].lower()
            if ext not in EXTS_PDF and ext not in EXTS_IMG:
                continue
            src = os.path.join(dirpath, fname)
            stem = os.path.splitext(fname)[0]
            out_dir = os.path.join(dirpath, "convertito")
            out_path = os.path.join(out_dir, stem + ".md")
            if not force and os.path.exists(out_path):
                continue
            todo.append((src, fname, out_path))
    return todo

def write_skip_stub(out_path, source_name, method, reason):
    frontmatter = (
        "---\n"
        f'fonte: "{source_name}"\n'
        f'metodo: "{method}"\n'
        "da_rivedere: true\n"
        "---\n\n"
        f"_Conversione automatica saltata: {reason}._\n\n"
        "_Se serve, apri il file originale e trascrivi/convertilo a mano._\n"
    )
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)

def process_one(item, root, dpi, timeout, max_ocr_mb, max_pages, file_timeout):
    src, fname, out_path = item
    rel = os.path.relpath(src, root)
    log(f"[avviato ] {rel}")
    t0 = time.monotonic()
    text, method, err = convert_file(src, dpi, timeout, max_ocr_mb, max_pages, file_timeout)
    dt = time.monotonic() - t0
    if method in ("saltato-grande", "saltato-molte-pagine"):
        write_skip_stub(out_path, fname, method, err)
        return (method, rel, err, dt)
    if err or text is None:
        return ("errore", rel, err, dt)
    write_markdown(out_path, fname, method, text)
    return (method, rel, None, dt)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--only", default=None)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--file-timeout", type=int, default=240)
    ap.add_argument("--max-pages", type=int, default=40)
    ap.add_argument("--max", type=int, default=10**9)
    ap.add_argument("--max-ocr-mb", type=float, default=15.0)
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    todo = find_todo(root, args.only, args.force)
    log(f"Da processare in questa chiamata: {min(len(todo), args.max)} (rimanenti totali: {len(todo)})")
    batch = todo[: args.max]

    stats = {}
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process_one, it, root, args.dpi, args.timeout, args.max_ocr_mb, args.max_pages, args.file_timeout): it for it in batch}
        for fut in as_completed(futs):
            method, rel, err, dt = fut.result()
            stats[method] = stats.get(method, 0) + 1
            if method in ("saltato-grande", "saltato-molte-pagine"):
                log(f"[{method}] {rel}: {err} ({dt:.0f}s)")
            elif err:
                log(f"[ERRORE] {rel}: {err} ({dt:.0f}s)")
            else:
                log(f"[{method:13s}] {rel} ({dt:.0f}s)")

    log("\n--- Riepilogo di questa chiamata ---")
    for k, v in stats.items():
        log(f"{k}: {v}")
    restanti = len(find_todo(root, args.only, False))
    log(f"Ancora da fare (esclusi errori già marcati): {restanti}")

if __name__ == "__main__":
    main()
