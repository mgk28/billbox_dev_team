#!/bin/bash
# Script de démarrage du backend BillBox

cd "$(dirname "$0")"
source ../.venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

