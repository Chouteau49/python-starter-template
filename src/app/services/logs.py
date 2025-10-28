"""
Système de logs moderne avec couleurs et rotation.
"""


import datetime
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from zoneinfo import ZoneInfo

from app.core.settings import Settings
from rich.logging import RichHandler


class Logger:
    """
    Configuration centralisée des logs.
    """

    def __init__(self, settings: Settings):
        self.logger = logging.getLogger()
        self._configured = False
        self._settings = settings

    def configure(self, level: str | None = None, file_path: str | None = None) -> None:
        """
        Configure le système de logs.
        """
        if self._configured:
            return

        level = level or self._settings.log_level
        file_path = file_path or self._settings.log_file_path

        # Niveau de log
        numeric_level = getattr(logging, level.upper(), logging.INFO)
        self.logger.setLevel(numeric_level)

        # Formatter avec timezone
        timezone = ZoneInfo(self._settings.log_timezone)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        formatter.converter = lambda *args: datetime.datetime.now(timezone).timetuple()

        # Handler console avec Rich
        console_handler = RichHandler(rich_tracebacks=True)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Handler fichier avec rotation
        if file_path:
            log_dir = Path(file_path).parent
            log_dir.mkdir(exist_ok=True)
            file_handler = RotatingFileHandler(
                file_path,
                maxBytes=10 * 1024 * 1024,
                backupCount=5,  # 10MB, 5 backups
                encoding="utf-8",  # Encodage UTF-8 pour supporter les caractères accentués
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        self._configured = True
        self.logger.info("Système de logs configuré")


def get_logger(name: str) -> logging.Logger:
    """
    Retourne un logger configuré pour un module.
    """
    # Pour l'injection, on attend une instance Settings
    raise RuntimeError(
        "Utilisez get_logger_injected(name, settings) pour l'injection de dépendances."
    )


def get_logger_injected(name: str, settings: Settings) -> logging.Logger:
    """
    Retourne un logger configuré pour un module, avec injection de Settings.
    """
    # Singleton par settings
    if not hasattr(get_logger_injected, "_logger_instance"):
        get_logger_injected._logger_instance = Logger(settings)  # type: ignore
    logger_instance = get_logger_injected._logger_instance  # type: ignore
    if not logger_instance._configured:
        logger_instance.configure()
    return logging.getLogger(name)
