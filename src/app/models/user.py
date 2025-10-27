"""
Modèles de données de l'application.
"""

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """
    Modèle pour un utilisateur.
    """

    id: int | None = None
    name: str
    email: EmailStr
    is_active: bool = True

    class Config:
        from_attributes = True
