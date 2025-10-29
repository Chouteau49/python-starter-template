"""
Gestionnaires de requêtes (routes, contrôleurs).
"""

import logging

from fastapi import APIRouter, Depends, HTTPException

from app.core.settings import Settings
from app.models.user import User
from app.services.user_service import IUserService, UserService

logger = logging.getLogger(__name__)
router = APIRouter()


def get_user_service() -> IUserService:
    # À adapter selon l'injection réelle (DI container, etc.)
    from app.repo.user_repository import InMemoryUserRepository

    return UserService(InMemoryUserRepository(), Settings())


@router.post("/users", response_model=User)
async def create_user(
    name: str, email: str, user_service: IUserService = Depends(get_user_service)
) -> User:
    try:
        return user_service.create_user(name, email)
    except Exception as e:
        logger.error(f"Erreur lors de la création d'utilisateur : {e}")
        raise HTTPException(status_code=400, detail="Erreur de création") from e


@router.get("/users/{user_id}", response_model=User)
async def get_user(
    user_id: int, user_service: IUserService = Depends(get_user_service)
) -> User:
    try:
        user = user_service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
        return user
    except Exception as e:
        logger.error(f"Erreur lors de la récupération d'utilisateur : {e}")
        raise HTTPException(status_code=400, detail="Erreur de récupération") from e
