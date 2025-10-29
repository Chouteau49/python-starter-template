---
mode: 'agent'
model: Claude Sonnet 4
tools: ['codebase', 'search']
description: 'Générer un nouveau module ou composant Python selon l’architecture du projet.'
---
Votre objectif est de générer un module Python conforme à l’architecture multi-couches : core, models, services, handlers, db, repo.
Demandez le nom du module, le type (service, modèle, handler, etc.) et les dépendances si non précisé.
Respectez les conventions PEP 8, typage statique, docstrings, et tests associés.

<!-- Inspired by: https://github.com/github/awesome-copilot/blob/main/prompts/setup-component.prompt.md -->
