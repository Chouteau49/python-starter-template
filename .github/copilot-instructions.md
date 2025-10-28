# Instructions pour GitHub Copilot

Ces instructions guident le développement d'une application Python moderne (version 3.13 ou supérieure) en respectant les bonnes pratiques 2025. Priorise la qualité, la maintenabilité et la scalabilité.

## Environnement Virtuel

- **Utilisation du virtualenv `.venv`** :
  - Avant toute installation de dépendances, crée ou active l'environnement virtuel local avec la commande :
    `source .venv/bin/activate` (Linux/Mac) ou `.venv\Scripts\activate` (Windows).
  - Toutes les installations de paquets Python doivent être réalisées dans cet environnement virtuel, jamais directement sur le système Arch Linux ou Windows.
  - Vérifie que le dossier `.venv/` est bien présent à la racine du projet et que le fichier `pyproject.toml` référence cet environnement.
  - Ajoute `.venv/` au `.gitignore` pour éviter de versionner l'environnement.

## Architecture et Structure

- **Couches modulaires** : Organise le code en couches claires (services, models, core, handlers, db, repo, etc.).
  - `core/` : Logique métier centrale, configurations globales.
  - `models/` : Définitions des données (classes Pydantic ou dataclasses typées).
  - `services/` : Logique applicative (ex. : services métier, API clients).
  - `handlers/` : Gestion des requêtes (ex. : routes FastAPI, contrôleurs).
  - `db/` : Accès aux données (repositories, connexions DB).
  - `repo/` : Interfaces et implémentations pour les repositories.
- **POO et Typage** : Utilise exclusivement la programmation orientée objet avec typage statique (annotations PEP 484/585). Méthodes privées avec `_` ou `__`, publiques sans préfixe.
- **Patterns SOLID** : Applique les principes SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion). Utilise l'injection de dépendances.
- **Gestion des Exceptions** : Capture et gère les erreurs avec des exceptions personnalisées. Log les erreurs et lève des exceptions appropriées sans masquer les détails.

## Logs et Monitoring

- **Système de Logs Moderne** :
  - Utilise `logging` avec configuration avancée (niveaux : DEBUG, INFO, WARNING, ERROR, CRITICAL).
  - Logs en console avec couleurs (via `colorama` ou `rich`).
  - Logs dans un fichier `app.log` avec rotation (via `RotatingFileHandler`) et archivage (compression gzip).
  - Écriture des logs dans toutes les méthodes : `logger.debug()`, `logger.info()`, etc., avec messages descriptifs en français.
- **Configuration via Variables d'Environnement** :
  - `LOG_LEVEL` : Niveau de log (default: INFO).
  - `LOG_FILE_PATH` : Chemin du fichier de logs (default: logs/app.log).
  - `LOG_TIMEZONE` : Heure de Paris (utilise `pytz` ou `zoneinfo` pour UTC+1/+2).
- **Monitoring** : Intègre des métriques basiques (ex. : via `prometheus_client`) pour les performances et erreurs.

## Tests et Qualité

- **TDD (Test-Driven Development)** : Écris les tests avant le code. Utilise `pytest` avec fixtures et parametrization.
- **Couverture de Code** : Vise minimum 85% de couverture (via `pytest-cov`). Génère des rapports HTML.
- **Tests d'Intégration et End-to-End** : Utilise `pytest` avec des fixtures pour les tests d'intégration, et des outils comme Selenium ou Playwright pour les tests E2E.
- **Linting et Formatage** : Utilise Ruff pour linter et formater tout le code. Configure des hooks pre-commit (via `pre-commit`) pour vérifier avant chaque commit.
- **Contrôle de Code** : Vérifie tous les fichiers Python avec Ruff. Corrige automatiquement les erreurs de style et de type.

## Déploiement

- **Docker sans Swarm** : Crée des images multi-étapes optimisées. Utilise des stacks Portainer pour orchestration simple.
  - Dockerfile : Base sur `python:3.13-slim`, copie des dépendances, expose les ports nécessaires.
  - docker-compose.yml : Définit les services, volumes, réseaux.
- **Bonnes Pratiques Déploiement** :
  - Variables d'environnement pour la configuration (pas de secrets en dur).
  - Health checks et restarts automatiques.
  - Logs centralisés via Docker (ou ELK stack si avancé).

## Documentation

- **Génération de Docs** : Utilise MkDocs dans le dossier `docs/` pour construire la documentation.
  - Sections : Guide utilisateur, Configuration, Architecture, Releases, API (si applicable).
  - Intègre des diagrammes (via Mermaid ou PlantUML) pour l'architecture.
  - Déploie automatiquement sur GitHub Pages via Actions.

## Autres Bonnes Pratiques 2025

- **Dépendances** : Gère avec Poetry pour les environnements virtuels et lockfiles.
- **Sécurité** : Valide les entrées, utilise des secrets via `python-dotenv` et services comme Azure Key Vault ou HashiCorp Vault, évite les vulnérabilités connues (scans avec `safety`).
- **Performance** : Utilise async/await pour les I/O (FastAPI, aiohttp). Optimise avec profiling (`cProfile`).
- **Migrations DB** : Utilise Alembic pour SQLAlchemy si base de données.
- **CI/CD** : Configure GitHub Actions pour tests, linting, build Docker, déploiement.
- **Versionnement** : Utilise Semantic Versioning avec `pyproject.toml` (via setuptools-scm ou similaire).
