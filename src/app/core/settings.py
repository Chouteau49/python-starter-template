"""
Configuration globale de l'application.
"""


import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Chargement automatique du .env à l'initialisation
    load_dotenv(dotenv_path=os.getenv("DOTENV_PATH", ".env"), override=True)
    """
    Paramètres de configuration via variables d'environnement.
    """

    log_level: str = "INFO"
    log_file_path: str = "logs/app.log"
    log_timezone: str = "Europe/Paris"

    smtp_server: str | None = None
    smtp_from_email: str | None = None
    smtp_to_email: str | None = None
