"""
Application principale du template Python moderne.
"""

from app.repo.user_repository import InMemoryUserRepository
from app.services.logs import get_logger
from app.services.user_service import UserService

from ._version import version as __version__


class Application:
    """
    Classe principale de l'application avec architecture moderne.
    """

    __banner__ = "Python Starter Template - Architecture Moderne"

    def __init__(self):
        """
        Initialise l'application avec les services modernes.
        """
        # Configuration des logs
        self.logger = get_logger(__name__)

        # Injection de dépendances
        user_repo = InMemoryUserRepository()
        self.user_service = UserService(user_repo)

        self.logger.info("Application initialisée avec succès")

    def run(self) -> bool:
        """
        Exécute l'application et démontre les fonctionnalités.
        """
        try:
            self.logger.info(self.__banner__)
            self.logger.info(f"Version: {__version__}")
            self.logger.info("Démarrage de l'application moderne")

            # Démonstration des nouvelles fonctionnalités
            self._demonstrate_features()

            self.logger.info("Fin de l'exécution de l'application")
            return True

        except Exception as e:
            self.logger.critical(f"Erreur critique dans l'application : {e}")
            return False

    def _demonstrate_features(self) -> None:
        """
        Démontre les fonctionnalités du template moderne.
        """
        self.logger.info("=== Démonstration des fonctionnalités ===")

        # Création d'un utilisateur
        user = self.user_service.create_user("Demo User", "demo@example.com")
        self.logger.info(f"Utilisateur créé : {user.name} ({user.email})")

        # Récupération d'un utilisateur
        retrieved = self.user_service.get_user_by_id(user.id)
        if retrieved:
            self.logger.info(f"Utilisateur récupéré : {retrieved.name}")

        # Liste des utilisateurs
        all_users = self.user_service.get_all_users()
        self.logger.info(f"Nombre total d'utilisateurs : {len(all_users)}")

        self.logger.info("=== Fin de la démonstration ===")
