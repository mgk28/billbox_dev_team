# BillBox Backend

Backend FastAPI pour BillBox.

## Installation

1. Assurez-vous d'avoir un environnement virtuel activé :
```bash
# À la racine du projet
source .venv/bin/activate
```

2. Installez les dépendances :
```bash
cd backend
pip install -r requirements.txt
```

## Lancement

### Méthode 1 : Avec le script
```bash
./start.sh
```

### Méthode 2 : Manuellement
```bash
# Depuis le dossier backend
source ../.venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Méthode 3 : Avec uvicorn directement
```bash
cd backend
uvicorn app.main:app --reload
```

Le serveur sera accessible sur : http://localhost:8000

## Documentation API

Une fois le serveur lancé, accédez à :
- Documentation interactive : http://localhost:8000/docs
- Documentation alternative : http://localhost:8000/redoc

## Endpoints

- `GET /` - Page d'accueil
- `GET /invoices/` - Liste toutes les factures
- `POST /invoices/` - Crée une nouvelle facture
- `GET /invoices/{invoice_id}` - Récupère une facture par ID

## Base de données

La base de données SQLite est créée automatiquement dans `billbox.db` à la racine du projet au premier lancement.

