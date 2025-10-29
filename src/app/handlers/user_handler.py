"""
Gestionnaires de requêtes (routes, contrôleurs).
"""

import logging

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.settings import Settings
from app.models.user import CreateUserRequest, User
from app.services.user_service import IUserService, UserService

logger = logging.getLogger(__name__)
router = APIRouter()


def get_user_service() -> IUserService:
    # À adapter selon l'injection réelle (DI container, etc.)
    from app.repo.user_repository import InMemoryUserRepository

    return UserService(InMemoryUserRepository(), Settings())


@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    request: CreateUserRequest, user_service: IUserService = Depends(get_user_service)
) -> User:
    """
    Crée un nouvel utilisateur.
    """
    if not request.name.strip() or not request.email.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Données invalides"
        )
    try:
        return user_service.create_user(request.name, request.email)
    except Exception as e:
        logger.error(f"Erreur lors de la création d'utilisateur : {e}")
        raise HTTPException(status_code=400, detail="Erreur de création") from e


@router.get("/users/{user_id}", response_model=User)
async def get_user(
    user_id: int, user_service: IUserService = Depends(get_user_service)
) -> User:
    """
    Récupère un utilisateur par son ID.
    """
    try:
        user = user_service.get_user_by_id(user_id)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération d'utilisateur : {e}")
        raise HTTPException(status_code=400, detail="Erreur de récupération") from e
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé"
        )
    return user


@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(
    user_id: int, user_service: IUserService = Depends(get_user_service)
) -> dict:
    """
    Supprime un utilisateur par son ID.
    """
    if not user_service.delete_user(user_id):
        logger.warning(
            f"Tentative de suppression d'un utilisateur inexistant : ID {user_id}"
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé"
        )
    logger.info(f"Utilisateur supprimé avec succès : ID {user_id}")
    return {"detail": "Utilisateur supprimé"}
