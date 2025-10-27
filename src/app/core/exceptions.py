"""
Exceptions personnalisées pour l'application.
"""

import logging

logger = logging.getLogger(__name__)


class AppException(Exception):
    """
    Exception de base pour l'application.
    """

    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.status_code = status_code
        logger.error(f"Exception levée : {message}")


class UserNotFoundException(AppException):
    """
    Exception pour utilisateur non trouvé.
    """

    def __init__(self, user_id: int):
        super().__init__(f"Utilisateur avec ID {user_id} non trouvé", 404)


class ValidationException(AppException):
    """
    Exception pour erreurs de validation.
    """

    def __init__(self, message: str):
        super().__init__(f"Erreur de validation : {message}", 400)


class DatabaseException(AppException):
    """
    Exception pour erreurs de base de données.
    """

    def __init__(self, message: str):
        super().__init__(f"Erreur base de données : {message}", 500)
