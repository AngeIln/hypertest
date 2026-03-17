# AI Code Studio – MVP Monorepo

Plateforme web pour générer, corriger, expliquer et exécuter du code avec IA.

## Vision

Ce dépôt implémente une base **MVP** alignée avec le cahier des charges:

- Génération/explication de snippets (Python, JavaScript, Java, C#, SQL).
- Éditeur web + exécution sandboxée (Python/JS) avec limites.
- Historique de sessions et versioning simple.
- Authentification utilisateur (JWT + OAuth prêt à intégrer).
- Déclenchement de tests unitaires depuis l'interface (endpoint backend + worker stub).

## Architecture

- `frontend/`: Next.js (App Router), TypeScript, Tailwind-ready.
- `backend/`: FastAPI + SQLAlchemy + JWT.
- `infra/`: `docker-compose.yml` (PostgreSQL, Redis, backend, frontend).
- `docs/`: produit, roadmap et architecture technique.

## Lancer en local

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
docker compose -f infra/docker-compose.yml up --build
```

- Frontend: <http://localhost:3000>
- Backend API docs: <http://localhost:8000/docs>

## Endpoints principaux

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/ai/generate`
- `POST /api/v1/ai/explain`
- `POST /api/v1/execution/run`
- `GET /api/v1/sessions`
- `POST /api/v1/tests/run`

## Remarques

Cette version pose une base de production-friendly, mais garde certaines briques en mode stub:
- appels LLM (service mocké) ;
- sandbox runtime (limites simulées + interface extensible) ;
- collaboration temps réel (prévue v2).
