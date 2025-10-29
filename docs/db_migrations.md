# Migrations de base de données (Alembic/SQLAlchemy)

Ce projet utilise SQLAlchemy pour l'accès aux données et Alembic pour la gestion des migrations.

## Pourquoi Alembic ?
Alembic permet de versionner le schéma de la base de données, d'appliquer des migrations incrémentales et de garantir la cohérence entre les environnements (dev, test, prod).

## Installation

```bash
poetry add alembic --dev
```

## Initialisation

```bash
alembic init migrations
```

Cela crée un dossier `migrations/` avec la configuration par défaut.

## Configuration

Dans `alembic.ini`, configurez la chaîne de connexion :

```
sqlalchemy.url = sqlite:///./app.db
# ou pour PostgreSQL
# sqlalchemy.url = postgresql://user:password@localhost/dbname
```

## Générer une migration

```bash
alembic revision --autogenerate -m "Initial migration"
```

## Appliquer les migrations

```bash
alembic upgrade head
```

## Intégration CI/CD
Ajoutez la commande Alembic dans vos workflows pour garantir que la base est à jour à chaque déploiement.

## Documentation
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

---

> **Bonnes pratiques** :
> - Versionnez le dossier `migrations/`.
> - Testez les migrations sur une base de test avant production.
> - Documentez chaque changement de schéma.
