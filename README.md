# Python Starter Template

[![CI](https://github.com/Chouteau49/python-starter-template/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Chouteau49/python-starter-template/actions)
[![Coverage](https://codecov.io/gh/Chouteau49/python-starter-template/branch/main/graph/badge.svg)](https://codecov.io/gh/Chouteau49/python-starter-template)
[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Un template structuré et prêt à l'emploi pour démarrer rapidement vos projets Python. Conçu pour être modulaire, évolutif et adapté aux meilleures pratiques de développement logiciel moderne (Python 3.13+, POO, SOLID, TDD, etc.).

## Fonctionnalités principales

- **Architecture modulaire** : Couches claires (core, models, services, handlers, db, repo)
- **Typage statique** : Utilisation de Pydantic et annotations PEP 484/585
- **Système de logs avancé** : Couleurs, rotation, archivage, timezone Paris
- **Tests complets** : Unitaire, intégration, E2E avec couverture 85%+
- **Linting et formatage** : Ruff pour qualité et cohérence
- **Déploiement moderne** : Docker multi-étapes, stacks Portainer
- **CI/CD** : GitHub Actions pour automatisation complète
- **Documentation** : MkDocs avec diagrammes et guides détaillés

## Démarrage rapide

### Prérequis

- Python 3.13+
- Docker (optionnel pour développement local)

### Installation

```bash
# Cloner le repo
git clone https://github.com/Chouteau49/python-starter-template.git
cd python-starter-template

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -e .[dev]

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos valeurs

# Installer les hooks pre-commit
pre-commit install
```

### Utilisation

```bash
# Lancer les tests
pytest

# Lancer l'application
python src/main.py

# Avec Docker
docker-compose up --build
```

## Structure du projet

```
├── src/
│   └── app/
│       ├── core/          # Configuration globale, exceptions
│       ├── models/        # Modèles de données (Pydantic)
│       ├── services/      # Logique métier
│       ├── handlers/      # Gestion des requêtes (FastAPI)
│       ├── db/            # Accès base de données
│       └── repo/          # Interfaces repositories
├── tests/                 # Tests unitaires et intégration
├── docs/                  # Documentation MkDocs
├── docker/                # Dockerfiles et compose
├── .github/               # Workflows CI/CD et instructions Copilot
├── pyproject.toml         # Configuration moderne (dépendances, outils)
├── .pre-commit-config.yaml # Hooks de qualité
└── .env.example           # Variables d'environnement
```

## Philosophie

Ce template suit les principes modernes de développement Python :

- **POO et SOLID** : Programmation orientée objet avec principes SOLID
- **TDD** : Tests d'abord, couverture élevée
- **Qualité** : Linting automatique, formatage, hooks pre-commit
- **Performance** : Async/await, optimisation profiling
- **Sécurité** : Validation des entrées, gestion des secrets
- **Maintenabilité** : Architecture claire, documentation complète

## Docs

📖 [Documentation complète](https://chouteau49.github.io/python-starter-template/)

- [Guide d'installation](https://chouteau49.github.io/python-starter-template/installation/)
- [Configuration](https://chouteau49.github.io/python-starter-template/configuration/)
- [Architecture](https://chouteau49.github.io/python-starter-template/architecture/)
- [API](https://chouteau49.github.io/python-starter-template/api/)

## Développement

### Tests

```bash
# Tests avec couverture
pytest --cov=src --cov-report=html

# Tests spécifiques
pytest tests/test_user_service.py
```

Documentation des tests
-----------------------

La documentation relative aux modules factices et à l'exécution des tests se trouve dans `docs/TESTS_FAKE_MODULES.md`.

### Linting et formatage

```bash
# Vérifier le code
ruff check .

# Formater le code
ruff format .
```

### CHANGELOG

Le CHANGELOG est généré automatiquement avec Towncrier.

```bash
# Créer un fragment de changement
echo "Ajout de la fonctionnalité X" > newsfragments/123.feature

# Générer le CHANGELOG
towncrier build --version 0.2.0 --yes

# Pour une release
towncrier build --version $(python -c "import setuptools_scm; print(setuptools_scm.get_version())") --yes
```

## Déploiement

### Avec Docker

```bash
# Construire l'image
docker-compose build

# Lancer l'application
docker-compose up
```

### Avec Portainer

Utilisez les stacks Portainer pour orchestration en production.

## Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## License

Distribué sous licence MIT. Voir `LICENSE` pour plus d'informations.

## Support

- [Issues](https://github.com/Chouteau49/python-starter-template/issues)
- [Discussions](https://github.com/Chouteau49/python-starter-template/discussions)
- [Documentation](https://chouteau49.github.io/python-starter-template/)
