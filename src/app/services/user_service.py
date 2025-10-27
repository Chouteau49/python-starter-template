# -*- coding: utf-8 -*-
"""
Services métier de l'application.
"""

import logging

from app.models.user import User
from app.repo.user_repository import UserRepository

logger = logging.getLogger(__name__)


class UserService:
    """
    Service pour la gestion des utilisateurs.
    """

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, name: str, email: str) -> User:
        """
        Crée un nouvel utilisateur.
        """
        logger.info(f"Création d'un utilisateur : {name} ({email})")
        user = User(name=name, email=email)
        return self.user_repo.save(user)

    def get_user_by_id(self, user_id: int) -> User | None:
        """
        Récupère un utilisateur par ID.
        """
        logger.debug(f"Récupération de l'utilisateur ID {user_id}")
        return self.user_repo.find_by_id(user_id)

    def get_all_users(self) -> list[User]:
        """
        Récupère tous les utilisateurs.
        """
        logger.debug("Récupération de tous les utilisateurs")
        return self.user_repo.find_all()
