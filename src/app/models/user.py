"""
Modèles de données de l'application.
"""

from pydantic import BaseModel, ConfigDict, EmailStr, model_validator


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

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


class CreateUserRequest(BaseModel):
    """
    Modèle pour la création d'un utilisateur.
    """

    name: str
    email: EmailStr

    @model_validator(mode="after")
    def validate_fields(self):
        if not self.name.strip():
            raise ValueError("Le nom ne peut pas être vide")
        if not self.email.strip():
            raise ValueError("L'email ne peut pas être vide")
        return self
