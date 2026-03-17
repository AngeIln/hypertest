# Architecture Technique

## Stack retenue
- Frontend: Next.js + TypeScript (+ Monaco prévu en intégration).
- Backend: FastAPI + SQLAlchemy.
- DB: PostgreSQL.
- Cache/queue: Redis.
- Runtime sandbox: service dédié (stub MVP).
- Infra: Docker Compose (dev), Kubernetes cible prod.

## Composants
- `frontend`: UI dashboard/éditeur/historique.
- `backend`: API auth, IA, exécution, sessions, tests.
- `workers` (prévu): file asynchrone pour tests/IA longue durée.
- `observability` (prévu): Sentry + Prometheus/Grafana.

## Sécurité
- JWT access token.
- Rate-limiting à ajouter via Redis.
- Sandbox isolée avec limites CPU/Mémoire/temps (vrai runtime à brancher).
