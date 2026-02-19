#!/usr/bin/env bash
set -euo pipefail

cd /home/roberdeth/projects/github/30-days-of-code

# Si no hay cambios, no hace nada
if [[ -z "$(git status --porcelain)" ]]; then
  exit 0
fi

git add -A
git commit -m "auto: backup $(date '+%Y-%m-%d %H:%M:%S')"

# Asegura rama main (por si el repo queda en detached o similar)
git push origin main
