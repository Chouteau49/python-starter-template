<!-- Inspired by: https://github.com/github/awesome-copilot/blob/main/collections/security.md -->
---
description: "Security best practices for Python projects"
applyTo: "**/*.py"
---
# Bonnes pratiques de sécurité

- Valider toutes les entrées utilisateur et API.
- Utiliser des secrets via python-dotenv ou un vault sécurisé.
- Ne jamais stocker de secrets en dur dans le code ou les configs.
- Scanner les dépendances avec safety pour éviter les vulnérabilités connues.
- Appliquer le principe du moindre privilège pour les accès DB et services.
- Logger les accès et erreurs critiques.
