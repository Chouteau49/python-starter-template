# Plan d'Upgrade du Projet Python Starter Template

Ce document liste les améliorations architecturales, de code et de configuration nécessaires pour moderniser le projet vers Python 3.13+ avec les bonnes pratiques 2025. Les tâches sont ordonnées par priorité et dépendances.

## Phase 1 : Configuration et Outils Modernes

1. **Remplacer requirements.txt par pyproject.toml** ✅
   - Créer `pyproject.toml` avec [tool.poetry] ou [build-system] pour gérer les dépendances, versionnement (setuptools-scm), et configurations Ruff/Pytest.
   - Migrer les dépendances de requirements.txt vers pyproject.toml.
   - Supprimer requirements.txt.

2. **Supprimer bumpversion.cfg et intégrer versionnement moderne** ✅
   - Configurer setuptools-scm dans pyproject.toml pour le versionnement automatique basé sur Git tags.
   - Mettre à jour les fichiers qui utilisent bumpversion (application.py, README.md, docker-compose.yml) pour utiliser setuptools-scm.

3. **Mettre à jour la configuration** ✅
   - Remplacer config.ini par des variables d'environnement (via python-dotenv).
   - Créer un fichier .env.example avec les variables nécessaires (LOG_LEVEL, LOG_FILE_PATH, etc.).
   - Supprimer config/ et config_samples/.

4. **Ajouter hooks pre-commit** ✅
   - Créer `.pre-commit-config.yaml` pour exécuter Ruff (lint/format), mypy, etc., avant chaque commit.

## Phase 2 : Architecture et Code

1. **Refactoriser l'architecture en couches modulaires** ✅
   - Réorganiser src/app/ en couches : core/, models/, services/, handlers/, db/, repo/.
   - Implémenter POO avec typage statique (PEP 484/585).
   - Appliquer patterns SOLID et injection de dépendances.
   - Créer des exemples de code pour chaque couche (service, modèle, handler).

2. **Améliorer le système de logs** ✅
   - Intégrer logging avec couleurs (rich ou colorama).
   - Ajouter rotation et archivage des logs.
   - Configurer via variables d'env (LOG_LEVEL, LOG_FILE_PATH, LOG_TIMEZONE=Europe/Paris).
   - Écrire des logs dans toutes les méthodes (debug, info, warning, etc.).

3. **Ajouter gestion d'erreurs et exceptions** ✅
   - Créer des exceptions personnalisées.
   - Logger les erreurs sans masquer les détails.

## Phase 3 : Tests et Qualité

1. **Implémenter TDD avec Pytest** ✅
   - Ajouter tests unitaires, d'intégration et E2E.
   - Configurer pytest-cov pour couverture 85% minimum.
   - Générer rapports HTML.

2. **Configurer Ruff pour linting et formatage** ✅
   - Intégrer Ruff dans pyproject.toml.
   - Configurer hooks pre-commit pour Ruff.

## Phase 4 : Déploiement et CI/CD

1. **Mettre à jour Docker** ✅
   - Dockerfile : Passer à Python 3.13-slim, multi-étapes, optimisé.
   - docker-compose.yml : Ajouter health checks, restarts, variables d'env.
   - Utiliser stacks Portainer pour orchestration.

2. **Ajouter workflows GitHub Actions** ✅
   - Créer `.github/workflows/ci-cd.yml` pour tests, linting, build Docker, déploiement.

## Phase 5 : Documentation et Finalisation

1. **Générer docs avec MkDocs** ✅
   - Créer docs/ avec guide utilisateur, configuration, architecture, releases, API.
   - Intégrer diagrammes Mermaid/PlantUML.
   - Déployer sur GitHub Pages.

2. **Mettre à jour README.md** ✅
   - Ajouter guide d'installation détaillé, utilisation, architecture, exemples.
   - Inclure badges, sections pour CI/CD, etc.

3. **Ajouter exemples de code** ✅
   - Dans src/, créer des fichiers d'exemple pour illustrer les bonnes pratiques (ex. : UserService, UserModel, AuthHandler).

4. **Nettoyer et finaliser** ✅
   - Supprimer scripts/init_env.sh et init_env.ps1 (remplacer par instructions dans README).
   - Vérifier compatibilité Python 3.13+.
   - Tester l'ensemble du pipeline CI/CD.

5. **Automatiser CHANGELOG** ✅
   - Intégrer Towncrier pour génération automatique du CHANGELOG à partir de fragments.
   - Configurer dans pyproject.toml et workflow CI/CD.

## Priorités et Dépendances

- Les phases 1 et 2 peuvent être parallèles.
- Phase 3 dépend de la refactorisation architecturale.
- Phase 4 dépend des configurations modernes.
- Phase 5 dépend de tout le reste.

Chaque tâche sera validée avec tests et linting avant de passer à la suivante.
