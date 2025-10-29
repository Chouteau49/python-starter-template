import pytest
from app.core.settings import Settings


@pytest.fixture
def set_env(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("LOG_FILE_PATH", "logs/test_app.log")
    monkeypatch.setenv("LOG_TIMEZONE", "Europe/Paris")
    monkeypatch.setenv("SMTP_SERVER", "localhost")
    monkeypatch.setenv("SMTP_FROM_EMAIL", "test@example.com")
    monkeypatch.setenv("SMTP_TO_EMAIL", "dest@example.com")


def test_settings_env(set_env):
    settings = Settings()
    assert settings.log_level == "DEBUG"
    assert settings.log_file_path == "logs/test_app.log"
    assert settings.log_timezone == "Europe/Paris"
    assert settings.smtp_server == "localhost"
    assert settings.smtp_from_email == "test@example.com"
    assert settings.smtp_to_email == "dest@example.com"
