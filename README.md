# python-starter-template

Un template structuré et prêt à l'emploi pour démarrer rapidement vos projets Python. Conçu pour être modulaire, évolutif et adapté aux meilleures pratiques de développement logiciel.

## Version

Current version: 0.1.0

## Caractéristiques principales

- Une architecture prête à l'emploi
- Prise en charge de Docker
- Gestion des logs
- Configuration avec des fichiers .ini
- CLI avec argparse
- Un point de départ clair pour les développeurs

## Prérequis

- Python 3.8+
- Docker

## Installation

### Cloner le projet

```bash
git clone https://github.com/Chouteau49/python-starter-template.git
cd python-starter-template
```

### Créer un environnement virtuel

#### Sous Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Sous Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Configurer les fichiers

Exécutez le script `init_env.sh` pour créer le dossier `config` et copier les fichiers de configuration :

```bash
./scripts/init_env.sh
```

Copiez le fichier `config/config.example.ini` en `config/config.ini` et remplissez les informations nécessaires.

## Utilisation

### Exécution de l'application

#### En local

```bash
python src/main.py
```

#### Avec Docker Compose

```bash
docker-compose up --build
```

### Commandes disponibles

L'application utilise `argparse` pour gérer les arguments de la ligne de commande. Vous pouvez spécifier les chemins des fichiers de configuration et de logs :

```bash
python src/main.py --config config/config.ini --logging config/logging.ini
```

## Utilisation de Docker

Pour construire l'image Docker, utilisez la commande suivante :
```bash
docker build -t nom_image ./docker
```

Pour lancer les services avec docker-compose, utilisez la commande suivante :
```bash
docker-compose -f ./docker/docker-compose.yml up
```

## Structure des dossiers

```
python-starter-template/
├── config/                 # Fichiers de configuration
│   ├── config.ini          # Fichier de configuration principal
│   └── logging.ini         # Configuration des logs
├── config_samples/        # Exemples de fichiers de configuration
│   ├── config.ini.sample   # Exemple de fichier de configuration
│   └── logging.ini.sample  # Exemple de fichier de configuration des logs
├── docker/                 # Fichiers Docker
│   ├── .dockerignore       # Fichiers et dossiers à ignorer par Docker
│   ├── Dockerfile          # Instructions pour construire l'image Docker
│   └── docker-compose.yml  # Configuration de Docker Compose
├── logs/                   # Dossier pour les fichiers de logs
├── scripts/                # Scripts utilitaires
│   └── init_env.sh         # Script pour initialiser l'environnement
├── src/                    # Code source de l'application
│   ├── app/                # Application principale
│   │   └── application.py  # Point d'entrée de l'application
│   ├── services/           # Services de l'application
│   │   ├── args.py         # Gestion des arguments de la ligne de commande
│   │   ├── email_notifier.py # Service de notification par email
│   │   └── logs.py         # Gestion des logs
├── .gitignore              # Fichiers et dossiers à ignorer par Git
├── requirements.txt        # Liste des dépendances Python
└── README.md               # Documentation du projet
```

## Contributions

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalite`)
3. Commitez vos modifications (`git commit -am 'Ajoute une nouvelle fonctionnalité'`)
4. Pushez votre branche (`git push origin feature/ma-fonctionnalite`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Astuces

- Pour personnaliser le projet, modifiez les fichiers de configuration dans le dossier `config`.
- Ajoutez de nouveaux services en créant des modules dans le dossier `src/services`.
- Utilisez les logs pour déboguer et surveiller l'application.

## Exemple de commande d'exécution avec Docker Compose

```bash
docker-compose up --build
```

Pour l'instant, il suffit de créer et remplir le fichier `config/config.ini` à partir de l'exemple fourni (`config/config.example.ini`). Lors de l'exécution, un email sera envoyé pour tester la configuration.
