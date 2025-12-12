
# Plan d’implémentation

## Structure du Monorepo

- /backend : contient le code pour le backend de l'application FastAPI.
- /web : contient le code pour la partie web de l'application Next.js.
- /mobile : contient le code pour la partie mobile de l'application avec Expo.

## Plan d’implémentation en tickets

1. Création de la structure de base de l'application : `/backend`, `/web`, `/mobile`.
2. Mise en place de l'authentification utilisateur côté backend (POST /api/v1/register).
3. Mise en place de la récupération des factures côté backend (GET /api/v1/bills).
4. Mise en place de la création de factures côté backend (POST /api/v1/bills).
5. Mise en place de la modification des factures côté backend (PUT /api/v1/bills/{id}).
6. Mise en place de la suppression des factures côté backend (DELETE /api/v1/bills/{id}).
7. Création de la page d'accueil côté web et mobile.
8. Création du tableau de bord utilisateur côté web et mobile.
9. Création de la page de création et modification de factures côté web et mobile.

## Conventions code

- Utiliser le PEP8 pour le code Python.
- Utiliser Airbnb style guide pour le Javascript/React code.
- Utiliser des commentaires pertinents pour expliquer le fonctionnement du code.

## Commandes de Run/Test

Pour démarrer le backend :
```bash
cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Pour démarrer le frontend web :
```bash
cd web
npm install
npm run dev
```

Pour démarrer l'application mobile :
```bash
cd mobile
npm install
npm start
```

Pour lancer les tests unitaires :
Backend :
```bash
cd backend
pytest
```

Web :
```bash
cd web
npm run test
```

Mobile :
```bash
cd mobile
npm run test
```