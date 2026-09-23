#!/usr/bin/env bash
# Copia gli appunti (Anno 1/2/3) dalla repo dentro sito-quartz/content/,
# escludendo i PDF originali (Quartz lavora solo su .md + immagini/allegati).
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="$(dirname "$SCRIPT_DIR")"      # .../sito-quartz
REPO_ROOT="$(dirname "$SITE_DIR")"       # root della repo

CONTENT_DIR="$SITE_DIR/content"
mkdir -p "$CONTENT_DIR"

echo "REPO_ROOT=$REPO_ROOT"
echo "CONTENT_DIR=$CONTENT_DIR"
echo "--- contenuto di REPO_ROOT ---"
ls -la "$REPO_ROOT"

for anno in "Anno 1" "Anno 2" "Anno 3"; do
  if [ -d "$REPO_ROOT/$anno" ]; then
    echo "Trovato: $REPO_ROOT/$anno -> copio in $CONTENT_DIR/"
    rsync -a --delete \
      --exclude='*.pdf' --exclude='*.PDF' \
      --exclude='*.mkv' --exclude='*.lnk' \
      "$REPO_ROOT/$anno" "$CONTENT_DIR/"
    rc=$?
    n=$(find "$CONTENT_DIR/$anno" -type f 2>/dev/null | wc -l)
    echo "  rsync exit=$rc, file presenti ora in content/$anno: $n"
  else
    echo "NON TROVATO: $REPO_ROOT/$anno"
  fi
done

echo "--- contenuto finale di $CONTENT_DIR ---"
find "$CONTENT_DIR" -maxdepth 2 | sort

echo "Sync completato in: $CONTENT_DIR"
