"""
Tests pour la configuration de l'application.
"""


from app.core.settings import Settings


class TestSettings:
    """Tests pour les paramètres de configuration."""

    def test_settings_creation(self):
        """Test de création des settings par défaut."""
        settings = Settings()
        assert settings.log_level == "INFO"
        assert settings.log_file_path == "logs/app.log"
        assert settings.log_timezone == "Europe/Paris"
        assert settings.smtp_server is None
        assert settings.smtp_from_email is None
        assert settings.smtp_to_email is None

    def test_settings_with_env_vars(self, monkeypatch):
        """Test des settings avec variables d'environnement."""
        monkeypatch.setenv("LOG_LEVEL", "DEBUG")
        monkeypatch.setenv("LOG_FILE_PATH", "custom.log")
        monkeypatch.setenv("SMTP_SERVER", "smtp.example.com")

        settings = Settings()
        assert settings.log_level == "DEBUG"
        assert settings.log_file_path == "custom.log"
        assert settings.smtp_server == "smtp.example.com"

    def test_email_settings_defaults(self):
        """Test des paramètres email par défaut (None)."""
        settings = Settings()
        assert settings.smtp_server is None
        assert settings.smtp_from_email is None
        assert settings.smtp_to_email is None
