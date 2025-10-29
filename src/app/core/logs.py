"""
Système de logs moderne avec couleurs et rotation.
"""

import datetime
import gzip
import logging
import shutil
from logging.handlers import RotatingFileHandler
from pathlib import Path
from zoneinfo import ZoneInfo

from rich.logging import RichHandler

from app.core.settings import Settings


class GzipRotatingFileHandler(RotatingFileHandler):
    def emit(self, record):
        super().emit(record)
        self._compress_old_logs()

    def _compress_old_logs(self):
        for i in range(self.backupCount, 0, -1):
            log_file = f"{self.baseFilename}.{i}"
            gz_file = f"{log_file}.gz"
            if Path(log_file).exists() and not Path(gz_file).exists():
                with open(log_file, "rb") as f_in, gzip.open(gz_file, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
                Path(log_file).unlink()


"""
Système de logs moderne avec couleurs et rotation.
"""


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

        # Handler fichier avec rotation + compression gzip des archives
        if file_path:
            log_dir = Path(file_path).parent
            log_dir.mkdir(parents=True, exist_ok=True)
            file_handler = GzipRotatingFileHandler(
                file_path,
                maxBytes=10 * 1024 * 1024,
                backupCount=5,
                encoding="utf-8",
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def _wrap_emit(self, emit_func, handler, compress_func):
        def wrapper(record):
            emit_func(record)
            compress_func(handler)

        return wrapper

        self._configured = True
        self.logger.info("Système de logs configuré")


class LoggerService:
    """
    Service de gestion des logs avec rotation et configuration avancée.
    """

    def __init__(self, log_file: str = "logs/app.log", log_level: str = "INFO"):
        self.logger = logging.getLogger("LoggerService")
        self.logger.setLevel(log_level)

        # Création du dossier des logs si nécessaire
        log_path = Path(log_file).parent
        log_path.mkdir(parents=True, exist_ok=True)

        # Gestionnaire de rotation des fichiers de log
        handler = RotatingFileHandler(log_file, maxBytes=10**6, backupCount=5)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)


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
