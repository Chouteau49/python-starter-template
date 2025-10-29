from app.core.settings import Settings


def test_settings_defaults():
    """Test des valeurs par défaut de Settings."""
    s = Settings()
    assert s.log_level == "INFO"
    assert s.log_file_path == "logs/app.log"
    assert s.log_timezone == "Europe/Paris"


def test_settings_env(monkeypatch):
    """Test override via variables d'environnement."""
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    s = Settings()
    assert s.log_level == "DEBUG"
