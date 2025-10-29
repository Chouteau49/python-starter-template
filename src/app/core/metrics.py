"""
Exposition des métriques Prometheus pour le monitoring.
"""

from fastapi import APIRouter, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

# Compteurs de base
REQUEST_COUNT = Counter(
    "app_request_count", "Nombre total de requêtes HTTP", ["method", "endpoint"]
)
ERROR_COUNT = Counter(
    "app_error_count", "Nombre total d'erreurs applicatives", ["type"]
)
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds", "Latence des requêtes HTTP en secondes", ["endpoint"]
)

router = APIRouter()


@router.get("/metrics")
def metrics() -> Response:
    """
    Endpoint Prometheus pour les métriques.
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
