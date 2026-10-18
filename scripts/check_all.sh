#!/bin/sh
# Usual local checks (decision 0061 adds check_export). Run from the repo root.
set -e
python3 scripts/check_scores.py | tail -1
python3 scripts/check_export.py
echo "no-JS: script tags in public/ (only application/ld+json allowed):"
if grep -rhoE '<script[^>]*>' public | grep -v 'type="application/ld+json"'; then echo "FAIL: non-JSON-LD script found"; exit 1; fi
echo "no-JS: ok"
