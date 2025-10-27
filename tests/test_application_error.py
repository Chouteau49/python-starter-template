"""
Test du chemin d'erreur pour `Application.run`.
"""

from unittest.mock import MagicMock, patch

from app.application import Application


@patch("app.application.get_logger")
@patch("app.application.InMemoryUserRepository")
@patch("app.application.UserService")
def test_run_handles_exceptions(mock_user_service, mock_repo, mock_get_logger):
    mock_logger = MagicMock()
    mock_get_logger.return_value = mock_logger

    mock_repo.return_value = MagicMock()
    mock_user_service.return_value = MagicMock()

    app = Application()

    # Forcer une exception pendant la démonstration
    def raise_exc():
        raise Exception("boom")

    app._demonstrate_features = raise_exc

    result = app.run()
    assert result is False
    mock_logger.critical.assert_called_once()
