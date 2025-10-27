"""
Configuration globale de l'application.
"""

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Paramètres de configuration via variables d'environnement.
    """

    log_level: str = "INFO"
    log_file_path: str = "logs/app.log"
    log_timezone: str = "Europe/Paris"

    smtp_server: str | None = None
    smtp_from_email: str | None = None
    smtp_to_email: str | None = None

    model_config = ConfigDict(
        env_prefix="",
    )


# Instance globale des settings
settings = Settings()
