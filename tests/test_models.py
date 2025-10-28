"""
Tests pour les modèles.
"""

import pytest
from pydantic import ValidationError

from app.models.user import User


class TestUserModel:
    """
    Tests pour le modèle User.
    """

    def test_user_creation_valid(self):
        """Test de création d'utilisateur valide."""
        user = User(name="John Doe", email="john@example.com")
        assert user.name == "John Doe"
        assert user.email == "john@example.com"
        assert user.is_active is True
        assert user.id is None

    def test_user_creation_invalid_email(self):
        """Test de création avec email invalide."""
        with pytest.raises(ValidationError):
            User(name="John Doe", email="invalid-email")

    def test_user_creation_missing_name(self):
        """Test de création sans nom."""
        with pytest.raises(ValidationError):
            User(email="john@example.com")
