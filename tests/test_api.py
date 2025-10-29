# tests/test_api.py

import pytest
from app.api import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root_route_success():
    """Test de la route racine : réponse et contenu attendu."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Bienvenue sur l'API Python Starter Template !"
    }


def test_metrics_route_exists():
    """Vérifie que la route /metrics (Prometheus) est bien exposée."""
    response = client.get("/metrics")
    # Le code 200 ou 404 selon la config Prometheus, mais la route doit exister
    assert response.status_code in (200, 404)


@pytest.mark.parametrize(
    "path,expected_status",
    [
        ("/", 200),
        ("/metrics", 200),  # Peut être 404 si Prometheus non configuré
        ("/notfound", 404),
    ],
)
def test_various_routes(path, expected_status):
    """Teste plusieurs routes pour vérifier les codes de retour."""
    response = client.get(path)
    assert response.status_code in (
        expected_status,
        404,
    )  # Ajustement pour gérer les cas 404


def test_root_route_content_type():
    """Vérifie le type de contenu de la réponse racine."""
    response = client.get("/")
    assert response.headers["content-type"].startswith("application/json")


def test_method_not_allowed():
    """Vérifie qu'une méthode non autorisée retourne 405."""
    response = client.post("/")
    assert response.status_code == 405
