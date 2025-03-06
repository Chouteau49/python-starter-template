# Utiliser une image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY src/ /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port (si nécessaire)
# EXPOSE 8000

# Définir la commande par défaut pour exécuter l'application
CMD ["python", "src/main.py"]
