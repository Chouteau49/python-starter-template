"""
Tests pour UserService.
"""
import pytest
from app.models.user import User
from app.services.user_service import UserService
from app.repo.user_repository import InMemoryUserRepository


class TestUserService:
    """
    Tests unitaires pour UserService.
    """

    @pytest.fixture
    def user_repo(self):
        return InMemoryUserRepository()

    @pytest.fixture
    def user_service(self, user_repo):
        return UserService(user_repo)

    def test_create_user(self, user_service):
        """Test de création d'utilisateur."""
        user = user_service.create_user("John Doe", "john@example.com")
        assert user.name == "John Doe"
        assert user.email == "john@example.com"
        assert user.is_active is True
        assert user.id is not None

    def test_get_user_by_id(self, user_service):
        """Test de récupération d'utilisateur par ID."""
        created = user_service.create_user("Jane Doe", "jane@example.com")
        retrieved = user_service.get_user_by_id(created.id)
        assert retrieved == created

    def test_get_user_by_id_not_found(self, user_service):
        """Test de récupération d'utilisateur inexistant."""
        retrieved = user_service.get_user_by_id(999)
        assert retrieved is None

    def test_get_all_users(self, user_service):
        """Test de récupération de tous les utilisateurs."""
        user1 = user_service.create_user("User1", "user1@example.com")
        user2 = user_service.create_user("User2", "user2@example.com")
        all_users = user_service.get_all_users()
        assert len(all_users) == 2
        assert user1 in all_users
        assert user2 in all_users