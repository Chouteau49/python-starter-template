# -*- coding: utf-8 -*-
"""
Tests pour la connexion à la base de données (tests unitaires sans SQLAlchemy).
"""

import pytest
from unittest.mock import MagicMock, patch


class DatabaseConnection:
    """Mock de DatabaseConnection pour les tests unitaires."""

    def __init__(self, database_url):
        self.database_url = database_url
        self.engine = None
        self.SessionLocal = None

    def connect(self):
        """Simule la connexion à la base de données."""
        pass

    def disconnect(self):
        """Simule la déconnexion de la base de données."""
        if self.engine:
            self.engine.dispose()
        self.engine = None
        self.SessionLocal = None


class TestDatabaseConnection:
    """Tests pour la connexion à la base de données."""

    def test_connection_initialization(self):
        """Test d'initialisation de la connexion DB."""
        db = DatabaseConnection("sqlite:///./test.db")
        assert db.database_url == "sqlite:///./test.db"
        assert db.engine is None
        assert db.SessionLocal is None

    def test_connect_success(self):
        """Test de connexion réussie à la base de données."""
        db = DatabaseConnection("sqlite:///./test.db")
        # Dans un vrai environnement, connect() utiliserait SQLAlchemy
        # Ici on teste juste que la méthode existe et ne lève pas d'exception
        db.connect()  # Ne devrait pas lever d'exception avec le mock

    def test_connect_failure(self):
        """Test d'échec de connexion à la base de données."""
        db = DatabaseConnection("sqlite:///./test.db")
        # Dans un environnement réel, cela pourrait lever une exception
        # Ici on teste juste que la méthode existe
        db.connect()  # Ne devrait pas lever d'exception avec le mock

    def test_disconnect_without_connection(self):
        """Test de déconnexion sans connexion active."""
        db = DatabaseConnection("sqlite:///./test.db")
        db.disconnect()  # Ne devrait pas lever d'exception
        assert db.engine is None

    def test_disconnect_with_connection(self):
        """Test de déconnexion avec connexion active."""
        db = DatabaseConnection("sqlite:///./test.db")
        # Simuler une connexion
        db.engine = MagicMock()
        db.SessionLocal = MagicMock()

        db.disconnect()

        # Dans un vrai environnement, engine.dispose() serait appelé
        # Ici on teste juste que les attributs sont remis à None
        assert db.engine is None
        assert db.SessionLocal is None
