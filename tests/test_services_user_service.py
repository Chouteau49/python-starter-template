from app.core.settings import Settings
from app.repo.user_repository import InMemoryUserRepository
from app.services.user_service import UserService


def test_user_service_delete_failure():
    """
    Teste le cas où la suppression d'un utilisateur échoue.
    """
    user_repo = InMemoryUserRepository()
    settings = Settings()
    service = UserService(user_repo=user_repo, settings=settings)
    result = service.delete_user(user_id=999)
    assert result is False
