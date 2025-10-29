<!-- Based on: https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/python.instructions.md -->
---
description: "Python coding conventions and guidelines"
applyTo: "**/*.py"
---
# Conventions et bonnes pratiques Python

## Principes généraux
- Prioriser la lisibilité et la clarté du code.
- Utiliser des noms de fonctions et variables descriptifs, avec annotations de type (PEP 484/585).
- Documenter chaque fonction et classe avec des docstrings conformes à PEP 257.
- Découper les fonctions complexes en sous-fonctions simples et testables.
- Respecter le style PEP 8 : indentation 4 espaces, lignes ≤79 caractères, espaces et sauts de ligne appropriés.
- Utiliser le module `typing` pour les annotations (List, Dict, etc.).
- Gérer les cas limites et exceptions avec des classes personnalisées et des messages explicites.
- Expliquer les choix d’architecture et d’algorithme dans les commentaires.
- Mentionner l’usage des dépendances externes dans les commentaires.

## Architecture
- Organiser le code en couches : core, models, services, handlers, db, repo.
- Appliquer les principes SOLID et l’injection de dépendances.
- Utiliser la POO pour structurer la logique métier et les données.

## Tests
- Écrire des tests unitaires et d’intégration pour chaque module critique.
- Documenter les cas de test et les comportements attendus.
- Couvrir les cas limites (entrées vides, types invalides, grands volumes).

## Documentation
- Rédiger des docstrings pour toutes les fonctions/classes publiques.
- Utiliser MkDocs pour la documentation utilisateur et technique.

## Sécurité et performance
- Valider toutes les entrées utilisateur.
- Utiliser des secrets via dotenv ou vault.
- Optimiser les I/O avec async/await.
- Profiler le code pour identifier les goulots d’étranglement.

## Revue de code
- Relire chaque PR pour la clarté, la sécurité, la performance et la couverture de tests.
- Exiger des tests et une documentation pour toute nouvelle fonctionnalité.
