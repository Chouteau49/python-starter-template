---
mode: 'agent'
model: Claude Sonnet 4
tools: ['codebase', 'search']
description: 'Générer des tests unitaires et d’intégration pour un module Python.'
---
Votre tâche : générer des tests pytest pour les fonctions et classes du module ciblé.
Demandez le nom du module et les cas d’usage critiques si non précisé.
Inclure des tests pour les cas limites, exceptions, et entrées variées.

<!-- Inspired by: https://github.com/github/awesome-copilot/blob/main/prompts/write-tests.prompt.md -->
