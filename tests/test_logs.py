# -*- coding: utf-8 -*-
"""
Tests pour le système de logging.
"""

import pytest
import logging
from unittest.mock import patch, MagicMock
from pathlib import Path

from app.services.logs import Logger, get_logger, logger


class TestLogger:
    """Tests pour le système de logging."""

    @patch('app.services.logs.logging')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    @patch('app.services.logs.RotatingFileHandler')
    @patch('app.services.logs.Path')
    def test_configure_first_time(self, mock_path, mock_file_handler, mock_rich_handler, mock_settings, mock_logging):
        """Test de première configuration du logger."""
        # Configuration des mocks
        mock_settings.log_level = "INFO"
        mock_settings.log_file_path = "logs/app.log"
        mock_settings.log_timezone = "Europe/Paris"

        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()

        mock_rich_instance = MagicMock()
        mock_rich_handler.return_value = mock_rich_instance

        mock_file_instance = MagicMock()
        mock_file_handler.return_value = mock_file_instance

        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        # Test
        logger_instance = Logger()
        logger_instance.configure()

        # Vérifications
        assert logger_instance._configured is True
        mock_rich_handler.assert_called_once()
        mock_file_handler.assert_called_once_with(
            "logs/app.log",
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )
        mock_path_instance.parent.mkdir.assert_called_once_with(exist_ok=True)
        mock_logger.info.assert_called_with("Système de logs configuré")

    @patch('app.services.logs.logging')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    def test_configure_without_file_path(self, mock_rich_handler, mock_settings, mock_logging):
        """Test de configuration sans chemin de fichier."""
        mock_settings.log_level = "DEBUG"
        mock_settings.log_file_path = None
        mock_settings.log_timezone = "UTC"

        mock_rich_instance = MagicMock()
        mock_rich_handler.return_value = mock_rich_instance

        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        logger_instance = Logger()
        logger_instance.configure()

        assert logger_instance._configured is True
        mock_rich_handler.assert_called_once()
        mock_logger.info.assert_called_with("Système de logs configuré")

    @patch('app.services.logs.logging')
    @patch('app.services.logs.ZoneInfo')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    @patch('app.services.logs.RotatingFileHandler')
    @patch('app.services.logs.Path')
    def test_configure_custom_parameters(self, mock_path, mock_file_handler, mock_rich_handler, mock_settings, mock_zoneinfo, mock_logging):
        """Test de configuration avec paramètres personnalisés."""
        mock_settings.log_timezone = "Europe/Paris"

        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()

        mock_rich_instance = MagicMock()
        mock_rich_handler.return_value = mock_rich_instance

        mock_file_instance = MagicMock()
        mock_file_handler.return_value = mock_file_instance

        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        logger_instance = Logger()
        logger_instance.configure(level="DEBUG", file_path="custom.log")

        assert logger_instance._configured is True
        mock_file_handler.assert_called_once_with(
            "custom.log",
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )
        mock_logger.info.assert_called_with("Système de logs configuré")

    def test_configure_idempotent(self):
        """Test que la reconfiguration n'a pas d'effet."""
        logger_instance = Logger()
        logger_instance._configured = True

        # Cette configuration ne devrait rien faire
        logger_instance.configure()

        # Le logger devrait rester configuré
        assert logger_instance._configured is True

    @patch('app.services.logs.logger')
    def test_get_logger_configures_if_needed(self, mock_global_logger):
        """Test que get_logger configure le logger si nécessaire."""
        mock_global_logger._configured = False
        mock_global_logger.configure = MagicMock()

        result = get_logger("test.module")

        mock_global_logger.configure.assert_called_once()
        assert isinstance(result, logging.Logger)

    @patch('app.services.logs.logger')
    def test_get_logger_returns_logger_when_configured(self, mock_global_logger):
        """Test que get_logger retourne directement un logger si déjà configuré."""
        mock_global_logger._configured = True

        result = get_logger("test.module")

        assert isinstance(result, logging.Logger)
        mock_global_logger.configure.assert_not_called()

    @patch('app.services.logs.logging')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    @patch('app.services.logs.RotatingFileHandler')
    @patch('app.services.logs.Path')
    def test_different_log_levels(self, mock_path, mock_file_handler, mock_rich_handler, mock_settings, mock_logging):
        """Test de différents niveaux de log."""
        mock_settings.log_file_path = "logs/app.log"
        mock_settings.log_timezone = "Europe/Paris"

        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()

        mock_rich_instance = MagicMock()
        mock_rich_handler.return_value = mock_rich_instance

        mock_file_instance = MagicMock()
        mock_file_handler.return_value = mock_file_instance

        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        # Configurer les niveaux de log sur le mock
        mock_logging.DEBUG = 10
        mock_logging.INFO = 20
        mock_logging.WARNING = 30
        mock_logging.ERROR = 40
        mock_logging.CRITICAL = 50

        for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            mock_settings.log_level = level
            logger_instance = Logger()
            logger_instance.configure()

            assert logger_instance._configured is True
            expected_numeric = getattr(mock_logging, level)
            mock_logger.setLevel.assert_called_with(expected_numeric)
            mock_logger.info.assert_called_with("Système de logs configuré")

    @patch('app.services.logs.logging')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    @patch('app.services.logs.RotatingFileHandler')
    @patch('app.services.logs.Path')
    def test_directory_creation(self, mock_path, mock_file_handler, mock_rich_handler, mock_settings, mock_logging):
        """Test que le répertoire de logs est créé."""
        mock_settings.log_level = "INFO"
        mock_settings.log_file_path = "deep/nested/logs/app.log"
        mock_settings.log_timezone = "Europe/Paris"

        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()

        mock_rich_instance = MagicMock()
        mock_rich_handler.return_value = mock_rich_instance

        mock_file_instance = MagicMock()
        mock_file_handler.return_value = mock_file_instance

        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        logger_instance = Logger()
        logger_instance.configure()

        mock_path_instance.parent.mkdir.assert_called_once_with(exist_ok=True)
        mock_logger.info.assert_called_with("Système de logs configuré")

    @patch('app.services.logs.logging')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    @patch('app.services.logs.RotatingFileHandler')
    @patch('app.services.logs.Path')
    def test_formatter_configuration(self, mock_path, mock_file_handler, mock_rich_handler, mock_settings, mock_logging):
        """Test de la configuration du formatter."""
        mock_settings.log_level = "INFO"
        mock_settings.log_file_path = "logs/app.log"
        mock_settings.log_timezone = "America/New_York"

        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()

        mock_rich_instance = MagicMock()
        mock_rich_handler.return_value = mock_rich_instance

        mock_file_instance = MagicMock()
        mock_file_handler.return_value = mock_file_instance

        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        logger_instance = Logger()
        logger_instance.configure()

        mock_rich_instance.setFormatter.assert_called_once()
        mock_file_instance.setFormatter.assert_called_once()
        mock_logger.addHandler.assert_any_call(mock_rich_instance)
        mock_logger.addHandler.assert_any_call(mock_file_instance)
        mock_logger.info.assert_called_with("Système de logs configuré")

    @patch('app.services.logs.logging')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    @patch('app.services.logs.RotatingFileHandler')
    @patch('app.services.logs.Path')
    def test_logger_initialization(self, mock_path, mock_file_handler, mock_rich_handler, mock_settings, mock_logging):
        """Test de l'initialisation du logger."""
        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        logger_instance = Logger()

        assert logger_instance._configured is False
        assert logger_instance.logger == mock_logger

    @patch('app.services.logs.logging')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    @patch('app.services.logs.RotatingFileHandler')
    @patch('app.services.logs.Path')
    def test_info_log_after_configuration(self, mock_path, mock_file_handler, mock_rich_handler, mock_settings, mock_logging):
        """Test que le message d'info est loggé après configuration."""
        mock_settings.log_level = "INFO"
        mock_settings.log_file_path = "logs/app.log"
        mock_settings.log_timezone = "Europe/Paris"

        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()

        mock_rich_instance = MagicMock()
        mock_rich_handler.return_value = mock_rich_instance

        mock_file_instance = MagicMock()
        mock_file_handler.return_value = mock_file_instance

        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        logger_instance = Logger()
        logger_instance.configure()

        mock_logger.info.assert_called_with("Système de logs configuré")

    @patch('app.services.logs.logging')
    @patch('app.services.logs.ZoneInfo')
    @patch('app.services.logs.settings')
    @patch('app.services.logs.RichHandler')
    @patch('app.services.logs.RotatingFileHandler')
    @patch('app.services.logs.Path')
    def test_timezone_configuration(self, mock_path, mock_file_handler, mock_rich_handler, mock_settings, mock_zoneinfo, mock_logging):
        """Test de la configuration de timezone."""
        mock_settings.log_level = "INFO"
        mock_settings.log_file_path = "logs/app.log"
        mock_settings.log_timezone = "America/New_York"

        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()

        mock_rich_instance = MagicMock()
        mock_rich_handler.return_value = mock_rich_instance

        mock_file_instance = MagicMock()
        mock_file_handler.return_value = mock_file_instance

        mock_logger = MagicMock()
        mock_logging.getLogger.return_value = mock_logger

        logger_instance = Logger()
        logger_instance.configure()

        assert logger_instance._configured is True
        mock_logger.info.assert_called_with("Système de logs configuré")
