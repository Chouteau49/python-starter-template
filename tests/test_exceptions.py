"""
Tests pour les exceptions personnalisées.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from app.core.exceptions import (
    AppException,
    DatabaseException,
    UserNotFoundException,
    ValidationException,
)


class TestExceptions:
    """Tests pour les exceptions de l'application."""

    def test_app_exception_creation(self):
        """Test de création d'une exception d'application."""
        exception = AppException("Erreur test", 400)
        assert str(exception) == "Erreur test"
        assert exception.status_code == 400

    def test_user_not_found_exception_creation(self):
        """Test de création d'une exception utilisateur non trouvé."""
        exception = UserNotFoundException(123)
        assert str(exception) == "Utilisateur avec ID 123 non trouvé"
        assert exception.status_code == 404

    def test_validation_exception_creation(self):
        """Test de création d'une exception de validation."""
        exception = ValidationException("Email invalide")
        assert str(exception) == "Erreur de validation : Email invalide"
        assert exception.status_code == 400

    def test_database_exception_creation(self):
        """Test de création d'une exception de base de données."""
        exception = DatabaseException("Connexion échouée")
        assert str(exception) == "Erreur base de données : Connexion échouée"
        assert exception.status_code == 500
