"""
Système de logs moderne avec couleurs et rotation.
"""

import datetime
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from zoneinfo import ZoneInfo

from rich.logging import RichHandler

from app.core.settings import settings


class Logger:
    """
    Configuration centralisée des logs.
    """

    def __init__(self):
        self.logger = logging.getLogger()
        self._configured = False

    def configure(self, level: str | None = None, file_path: str | None = None) -> None:
        """
        Configure le système de logs.
        """
        if self._configured:
            return

        level = level or settings.log_level
        file_path = file_path or settings.log_file_path

        # Niveau de log
        numeric_level = getattr(logging, level.upper(), logging.INFO)
        self.logger.setLevel(numeric_level)

        # Formatter avec timezone
        timezone = ZoneInfo(settings.log_timezone)
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
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        self._configured = True
        self.logger.info("Système de logs configuré")


# Instance globale
logger = Logger()


def get_logger(name: str) -> logging.Logger:
    """
    Retourne un logger configuré pour un module.
    """
    if not logger._configured:
        logger.configure()
    return logging.getLogger(name)
