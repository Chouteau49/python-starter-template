"""
API FastAPI principale du projet, incluant les métriques Prometheus.
"""

from fastapi import FastAPI

from app.core.metrics import router as metrics_router

app = FastAPI(title="Python Starter Template API")

# Inclusion du router Prometheus
app.include_router(metrics_router)


# Exemple de route racine
@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Bienvenue sur l'API Python Starter Template !"}


# Pour lancer :
# uvicorn app.api:app --reload
