#!/usr/bin/env bash
# Copia gli appunti (Anno 1/2/3) dalla repo dentro sito-quartz/content/,
# escludendo i PDF originali (Quartz lavora solo su .md + immagini/allegati).
# Va eseguito dalla ROOT della repo, oppure lo script lo fa da solo.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="$(dirname "$SCRIPT_DIR")"      # .../sito-quartz
REPO_ROOT="$(dirname "$SITE_DIR")"       # root della repo

CONTENT_DIR="$SITE_DIR/content"
mkdir -p "$CONTENT_DIR"

for anno in "Anno 1" "Anno 2" "Anno 3"; do
  if [ -d "$REPO_ROOT/$anno" ]; then
    rsync -a --delete \
      --exclude='*.pdf' --exclude='*.PDF' \
      --exclude='*.mkv' --exclude='*.lnk' \
      "$REPO_ROOT/$anno" "$CONTENT_DIR/"
  fi
done

echo "Sync completato in: $CONTENT_DIR"
