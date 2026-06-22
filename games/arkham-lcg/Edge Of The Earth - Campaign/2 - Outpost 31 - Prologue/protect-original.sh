#!/usr/bin/env bash
# Guard the pristine Outpost 31 original. Modes: baseline | verify | lock | unlock (default: verify)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ORIG="$HERE/Outpost 31 - Original"
[ -d "$ORIG" ] || { echo "ERROR: original folder not found"; exit 1; }
MODE="${1:-verify}"
baseline(){ ( cd "$ORIG" && find . -type f -not -path "./_card-data-original/*" -not -name ".original-checksums.sha256" -print0 | sort -z | xargs -0 sha256sum > ".original-checksums.sha256" ); echo "baseline written ($(grep -c . "$ORIG/.original-checksums.sha256") files)"; }
verify(){ [ -f "$ORIG/.original-checksums.sha256" ] || { echo "no manifest; run: $0 baseline"; exit 1; }; ( cd "$ORIG" && sha256sum -c ".original-checksums.sha256" --quiet ) && echo "PASS - originals untouched" || { echo "FAIL - see above"; return 1; }; }
lock(){ find "$ORIG" -type f -not -path "*/_card-data-original/*" -exec chmod a-w {} +; echo "locked"; }
unlock(){ find "$ORIG" -type f -exec chmod u+w {} +; echo "unlocked"; }
case "$MODE" in baseline)baseline;;verify)verify;;lock)lock;;unlock)unlock;;*)echo "usage: $0 [baseline|verify|lock|unlock]";exit 1;;esac
