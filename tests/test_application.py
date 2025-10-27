"""
Tests pour l'application principale.
"""

from unittest.mock import MagicMock, patch

from app.application import Application


class TestApplication:
    """Tests pour l'application principale."""

    @patch("app.application.get_logger")
    @patch("app.application.UserService")
    @patch("app.application.InMemoryUserRepository")
    def test_application_initialization(self, mock_repo, mock_service, mock_logger):
        """Test d'initialisation de l'application."""
        mock_logger.return_value = MagicMock()

        app = Application()

        # Vérifier que le logger est configuré
        mock_logger.assert_called_once()

        # Vérifier que le repository est créé
        mock_repo.assert_called_once()

        # Vérifier que le service est créé avec le repository
        mock_service.assert_called_once_with(mock_repo.return_value)

        assert app.user_service == mock_service.return_value

    @patch("app.application.get_logger")
    @patch("app.application.UserService")
    @patch("app.application.InMemoryUserRepository")
    def test_run_demo(self, mock_repo, mock_service, mock_logger):
        """Test de l'exécution de la démonstration."""
        # Configuration des mocks
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance

        mock_user_service = MagicMock()
        mock_service.return_value = mock_user_service

        # Mock des méthodes du service
        mock_user_service.create_user.return_value = MagicMock(
            id=1, name="Demo User", email="demo@example.com"
        )
        mock_user_service.get_user_by_id.return_value = MagicMock(
            id=1, name="Demo User", email="demo@example.com"
        )
        mock_user_service.get_all_users.return_value = [
            MagicMock(id=1, name="Demo User", email="demo@example.com")
        ]

        app = Application()
        app.run()

        # Vérifier que les logs sont appelés
        assert mock_logger_instance.info.call_count >= 6  # Plusieurs appels de log

        # Vérifier que les méthodes du service sont appelées
        mock_user_service.create_user.assert_called_once_with(
            "Demo User", "demo@example.com"
        )
        mock_user_service.get_user_by_id.assert_called_once_with(1)
        mock_user_service.get_all_users.assert_called_once()
