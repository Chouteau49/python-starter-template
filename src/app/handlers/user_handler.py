# -*- coding: utf-8 -*-
"""
Gestionnaires de requêtes (routes, contrôleurs).
"""

import logging

from fastapi import APIRouter, HTTPException

from app.models.user import User
from app.services.user_service import UserService

logger = logging.getLogger(__name__)

router = APIRouter()


class UserHandler:
    """
    Handler pour les endpoints utilisateurs.
    """

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    @router.post("/users", response_model=User)
    async def create_user(self, name: str, email: str) -> User:
        """
        Crée un utilisateur via API.
        """
        try:
            return self.user_service.create_user(name, email)
        except Exception as e:
            logger.error(f"Erreur lors de la création d'utilisateur : {e}")
            raise HTTPException(status_code=400, detail="Erreur de création") from e

    @router.get("/users/{user_id}", response_model=User)
    async def get_user(self, user_id: int) -> User:
        """
        Récupère un utilisateur par ID.
        """
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
        return user

    @router.get("/users", response_model=list[User])
    async def get_users(self) -> list[User]:
        """
        Récupère tous les utilisateurs.
        """
        return self.user_service.get_all_users()
