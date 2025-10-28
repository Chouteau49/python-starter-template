"""
Tests pour UserService.
"""

from unittest.mock import MagicMock, patch

import pytest
from app.repo.user_repository import InMemoryUserRepository
from app.services.user_service import UserService


class TestUserService:
    """
    Tests unitaires pour UserService.
    """

    @pytest.fixture
    def user_repo(self):
        return InMemoryUserRepository()

    @pytest.fixture
    def user_service(self, user_repo):
        settings = MagicMock()
        service = UserService(user_repo, settings)
        return service

    @patch("app.services.user_service.logger")
    def test_create_user(self, mock_logger, user_service):
        """Test de création d'utilisateur."""
        user = user_service.create_user("John Doe", "john@example.com")
        assert user.name == "John Doe"  # nosec
        assert user.email == "john@example.com"  # nosec
        assert user.is_active is True  # nosec
        assert user.id is not None  # nosec
        mock_logger.info.assert_called()

    @patch("app.services.user_service.logger")
    def test_get_user_by_id(self, mock_logger, user_service):
        """Test de récupération d'utilisateur par ID."""
        created = user_service.create_user("Jane Doe", "jane@example.com")
        retrieved = user_service.get_user_by_id(created.id)
        assert retrieved == created  # nosec

    @patch("app.services.user_service.logger")
    def test_get_user_by_id_not_found(self, mock_logger, user_service):
        """Test de récupération d'utilisateur inexistant."""
        retrieved = user_service.get_user_by_id(999)
        assert retrieved is None  # nosec

    @patch("app.services.user_service.logger")
    def test_get_all_users(self, mock_logger, user_service):
        """Test de récupération de tous les utilisateurs."""
        user1 = user_service.create_user("User1", "user1@example.com")
        user2 = user_service.create_user("User2", "user2@example.com")
        all_users = user_service.get_all_users()
        assert len(all_users) == 2  # nosec
        assert user1 in all_users  # nosec
        assert user2 in all_users  # nosec
