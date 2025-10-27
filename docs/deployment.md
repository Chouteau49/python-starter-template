# Déploiement

## Vue d'ensemble

Ce guide explique comment déployer l'application Python Starter Template en production. L'application supporte plusieurs méthodes de déploiement : Docker, serveur traditionnel, et cloud.

## Prérequis de production

### Variables d'environnement

Créez un fichier `.env` avec les valeurs de production :

```bash
# Configuration de production
APP_NAME=Mon Application
LOG_LEVEL=WARNING
LOG_TIMEZONE=Europe/Paris

# Base de données de production
DATABASE_URL=postgresql://user:password@db-host:5432/prod_db

# Sécurité
SECRET_KEY=votre-cle-secrete-très-longue-et-complexe

# Email de production
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=contact@mondomaine.com
SMTP_PASSWORD=votre-mot-de-passe-app
SMTP_FROM_EMAIL=contact@mondomaine.com
SMTP_TO_EMAIL=admin@mondomaine.com
```

### Base de données

L'application supporte plusieurs SGBD :

- **SQLite** : Pour les tests et développement
- **PostgreSQL** : Recommandé pour la production
- **MySQL** : Supporté mais moins testé

#### Configuration PostgreSQL

```sql
-- Créer la base de données
CREATE DATABASE prod_db;

-- Créer l'utilisateur
CREATE USER app_user WITH PASSWORD 'secure_password';

-- Donner les permissions
GRANT ALL PRIVILEGES ON DATABASE prod_db TO app_user;
```

## Déploiement avec Docker

### Construction de l'image

```bash
# Construction de l'image
docker build -t python-starter-template:latest .

# Vérification
docker images python-starter-template
```

### Exécution en conteneur

```bash
# Exécution simple
docker run -d \
  --name python-app \
  -p 8000:8000 \
  --env-file .env \
  python-starter-template:latest

# Avec volume pour les logs
docker run -d \
  --name python-app \
  -p 8000:8000 \
  -v /opt/app/logs:/app/logs \
  --env-file .env \
  python-starter-template:latest
```

### Docker Compose

Utilisez le `docker-compose.yml` fourni :

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: prod_db
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  postgres_data:
```

```bash
# Démarrage
docker-compose up -d

# Suivi des logs
docker-compose logs -f app

# Arrêt
docker-compose down
```

## Déploiement traditionnel

### Avec Gunicorn

```bash
# Installation
pip install gunicorn

# Configuration de production
pip install --upgrade pip
pip install -e .

# Lancement avec Gunicorn
gunicorn \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --access-logfile logs/access.log \
  --error-logfile logs/error.log \
  app.handlers.user_handler:app
```

### Avec uvicorn

```bash
# Installation
pip install uvicorn[standard]

# Lancement
uvicorn \
  --host 0.0.0.0 \
  --port 8000 \
  --workers 4 \
  --access-log \
  app.handlers.user_handler:app
```

### Systemd (Linux)

Créez un service systemd `/etc/systemd/system/python-app.service` :

```ini
[Unit]
Description=Python Starter Template
After=network.target

[Service]
User=appuser
Group=appuser
WorkingDirectory=/opt/python-app
Environment=PATH=/opt/python-app/venv/bin
ExecStart=/opt/python-app/venv/bin/gunicorn --bind 0.0.0.0:8000 --workers 4 --worker-class uvicorn.workers.UvicornWorker app.handlers.user_handler:app
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Recharger systemd
sudo systemctl daemon-reload

# Démarrer le service
sudo systemctl start python-app

# Activer au démarrage
sudo systemctl enable python-app

# Suivre les logs
sudo journalctl -u python-app -f
```

## Déploiement cloud

### Heroku

1. **Préparation :**
   ```bash
   # Créer requirements.txt pour Heroku
   pip freeze > requirements.txt

   # Créer Procfile
   echo "web: gunicorn --bind 0.0.0.0:\$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker app.handlers.user_handler:app" > Procfile
   ```

2. **Déploiement :**
   ```bash
   # Créer l'application Heroku
   heroku create votre-app-name

   # Configurer les variables d'environnement
   heroku config:set APP_NAME="Mon App"
   heroku config:set DATABASE_URL="postgresql://..."

   # Déployer
   git push heroku main
   ```

### Railway

1. **Connexion :**
   ```bash
   # Installer Railway CLI
   npm install -g @railway/cli

   # Se connecter
   railway login
   ```

2. **Déploiement :**
   ```bash
   # Créer un projet
   railway init

   # Déployer
   railway up
   ```

### Vercel (pour API seulement)

```bash
# Installer Vercel CLI
npm install -g vercel

# Déployer
vercel --prod
```

## Configuration du reverse proxy

### Nginx

Configuration exemple pour Nginx :

```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Logs
    access_log /var/log/nginx/app_access.log;
    error_log /var/log/nginx/app_error.log;

    # Sécurité
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
}
```

### Apache

Configuration exemple pour Apache :

```apache
<VirtualHost *:80>
    ServerName votre-domaine.com

    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/

    ErrorLog ${APACHE_LOG_DIR}/app_error.log
    CustomLog ${APACHE_LOG_DIR}/app_access.log combined
</VirtualHost>
```

## Monitoring et logging

### Logs

Les logs sont automatiquement configurés avec rotation :

```bash
# Structure des logs
logs/
├── app.log          # Logs principaux
├── app.log.1        # Archive 1
├── app.log.2        # Archive 2
└── access.log       # Logs d'accès (avec Gunicorn)
```

### Métriques

Pour le monitoring, considérez :

- **Prometheus** : Collecte de métriques
- **Grafana** : Visualisation des métriques
- **Sentry** : Gestion des erreurs
- **DataDog** : Monitoring complet

### Health checks

L'application fournit un endpoint de health check :

```bash
# Vérifier la santé
curl http://localhost:8000/health

# Avec Docker
docker ps
docker stats
```

## Sécurité

### Bonnes pratiques

1. **Variables d'environnement** : Ne jamais commiter les secrets
2. **HTTPS** : Toujours utiliser HTTPS en production
3. **Firewall** : Limiter l'accès aux ports nécessaires
4. **Mises à jour** : Maintenir les dépendances à jour
5. **Sauvegardes** : Sauvegarder régulièrement la base de données

### Configuration de sécurité

```bash
# Générer une clé secrète
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Utiliser HTTPS
# Configuration Nginx avec Let's Encrypt
certbot --nginx -d votre-domaine.com
```

## Performance

### Optimisations

1. **Workers Gunicorn** : `workers = 2 * CPU + 1`
2. **Cache** : Utiliser Redis pour le cache
3. **CDN** : Servir les assets statiques via CDN
4. **Database** : Optimiser les requêtes et utiliser des indexes

### Scaling

- **Horizontal** : Plusieurs instances derrière un load balancer
- **Vertical** : Augmenter les ressources de la machine
- **Database** : Read replicas pour les lectures

## Troubleshooting

### Problèmes courants

1. **Port déjà utilisé :**
   ```bash
   # Trouver le processus
   lsof -i :8000

   # Tuer le processus
   kill -9 <PID>
   ```

2. **Mémoire pleine :**
   ```bash
   # Vérifier l'usage mémoire
   docker stats

   # Redémarrer le conteneur
   docker-compose restart app
   ```

3. **Base de données indisponible :**
   ```bash
   # Vérifier la connexion
   docker-compose logs db

   # Redémarrer la DB
   docker-compose restart db
   ```

### Logs de debug

```bash
# Logs détaillés
LOG_LEVEL=DEBUG python src/main.py

# Logs Docker
docker-compose logs -f --tail=100 app

# Logs système
sudo journalctl -u python-app -f
``` 
 