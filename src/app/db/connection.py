# -*- coding: utf-8 -*-
"""
Accès aux données (connexions DB).
"""

import logging

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

logger = logging.getLogger(__name__)


class DatabaseConnection:
    """
    Gestion de la connexion à la base de données.
    """

    def __init__(self, database_url: str = "sqlite:///./test.db"):
        self.database_url = database_url
        self.engine: Engine | None = None
        self.SessionLocal = None

    def connect(self) -> None:
        """
        Établit la connexion à la DB.
        """
        try:
            self.engine = create_engine(self.database_url)
            self.SessionLocal = sessionmaker(
                autocommit=False, autoflush=False, bind=self.engine
            )
            logger.info("Connexion à la base de données établie")
        except Exception as e:
            logger.error(f"Erreur de connexion à la DB : {e}")
            raise

    def get_session(self) -> Session:
        """
        Retourne une session DB.
        """
        if not self.SessionLocal:
            raise RuntimeError("Connexion DB non établie")
        return self.SessionLocal()

    def disconnect(self) -> None:
        """
        Ferme la connexion.
        """
        if self.engine:
            self.engine.dispose()
            logger.info("Connexion DB fermée")
