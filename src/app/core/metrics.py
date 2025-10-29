"""
Exposition des métriques Prometheus pour le monitoring.
"""

from fastapi import APIRouter, Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    CollectorRegistry,
    Counter,
    Histogram,
    generate_latest,
)

# Utilisation d'un registre personnalisé pour éviter les conflits
METRICS_REGISTRY = CollectorRegistry()

# Compteurs de base
REQUEST_COUNT = Counter(
    "app_request_count",
    "Nombre total de requêtes HTTP",
    ["method", "endpoint"],
    registry=METRICS_REGISTRY,
)
ERROR_COUNT = Counter(
    "app_error_count",
    "Nombre total d'erreurs applicatives",
    ["type"],
    registry=METRICS_REGISTRY,
)
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Latence des requêtes HTTP en secondes",
    ["endpoint"],
    registry=METRICS_REGISTRY,
)

router = APIRouter()


@router.get("/metrics")
def metrics() -> Response:
    """
    Endpoint Prometheus pour les métriques.
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
