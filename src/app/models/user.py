"""
Modèles de données de l'application.
"""

from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    """
    Modèle pour un utilisateur.
    """

    id: int | None = None
    name: str
    email: EmailStr
    is_active: bool = True

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )
