# Instructions pour les messages de commit

Génère tous les messages de commit en français.

## Format requis :

- Première ligne : résumé en une seule ligne (maximum 50 caractères)
- Deuxième ligne : vide
- Corps du message : description détaillée en français (maximum 50 caractères par ligne)

## Types de commit en français :

- feat: nouvelle fonctionnalité
- fix: correction de bug
- docs: documentation
- style: formatage, style
- refactor: refactorisation
- test: ajout/modification de tests
- chore: tâches de maintenance
- build: modifications du système de build
- perf: amélioration des performances
- ci: intégration continue
- revert: annulation d'un commit précédent

## Exemples :

- feat: ajouter l'authentification par email
- fix: corriger l'erreur de validation du formulaire
- docs: mettre à jour le guide d'installation

## Prompt associé

Pour une génération assistée et plus professionnelle, utilise le prompt défini dans `prompts/commit.prompt.md`, qui inclut des conventions Git modernes (2025) et des bonnes pratiques pour Python.
