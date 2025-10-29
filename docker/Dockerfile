# Étape de build
FROM python:3.13-slim as builder

WORKDIR /app

# Installer les dépendances de build
COPY pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .

# Étape finale
FROM python:3.13-slim

WORKDIR /app

# Copier les dépendances installées depuis l'étape de build
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copier le code source
COPY src/ /app/src/

# Créer répertoire pour les logs
RUN mkdir -p /app/logs

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV TZ=Europe/Paris

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Exposer le port (si FastAPI)
EXPOSE 8000

# Commande par défaut
CMD ["python", "src/main.py"]
