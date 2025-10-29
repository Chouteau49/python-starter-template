from app.core.metrics import (
    ERROR_COUNT,
    METRICS_REGISTRY,
    REQUEST_COUNT,
    REQUEST_LATENCY,
)
from prometheus_client import generate_latest


def get_metric_value(metric, labels):
    for sample in metric.collect()[0].samples:
        if all(sample.labels[k] == v for k, v in labels.items()):
            return sample.value
    return None


def test_metrics_counters():
    REQUEST_COUNT.labels(method="GET", endpoint="/test").inc()
    ERROR_COUNT.labels(type="test").inc()
    REQUEST_LATENCY.labels(endpoint="/test").observe(0.123)
    # Vérification via l’API publique
    assert get_metric_value(REQUEST_COUNT, {"method": "GET", "endpoint": "/test"}) >= 1
    assert get_metric_value(ERROR_COUNT, {"type": "test"}) >= 1
    assert get_metric_value(REQUEST_LATENCY, {"endpoint": "/test"}) is not None


def test_metrics_registration():
    """Vérifie que les métriques sont correctement enregistrées dans le registre personnalisé."""
    metrics_output = generate_latest(METRICS_REGISTRY).decode("utf-8")
    assert "app_request_count" in metrics_output
    assert "app_error_count" in metrics_output
    assert "app_request_latency_seconds" in metrics_output
