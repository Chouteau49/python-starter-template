"""
Services métier de l'application.
"""

import logging
from abc import ABC, abstractmethod

from app.core.settings import Settings
from app.models.user import User
from app.repo.user_repository import UserRepository

logger = logging.getLogger(__name__)


class IUserService(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def get_all_users(self) -> list[User]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass


class UserService(IUserService):
    """
    Service pour la gestion des utilisateurs.
    """

    def __init__(self, user_repo: UserRepository, settings: Settings) -> None:
        self.user_repo = user_repo
        self.settings = settings

    def create_user(self, name: str, email: str) -> User:
        logger.info(f"Création d'un utilisateur : {name} ({email})")
        user = User(name=name, email=email)
        return self.user_repo.save(user)

    def get_user_by_id(self, user_id: int) -> User | None:
        logger.debug(f"Récupération de l'utilisateur ID {user_id}")
        return self.user_repo.find_by_id(user_id)

    def get_all_users(self) -> list[User]:
        logger.debug("Récupération de tous les utilisateurs")
        return self.user_repo.find_all()

    def delete_user(self, user_id: int) -> bool:
        """
        Supprime un utilisateur par son ID.
        Retourne True si l'utilisateur a été supprimé, False sinon.
        """
        try:
            return self.user_repo.delete(user_id)
        except Exception as e:
            logger.error(
                f"Erreur lors de la suppression de l'utilisateur {user_id} : {e}"
            )
            return False
