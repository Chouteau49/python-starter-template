import logging
import logging.config
import sys
import os


class Logs:
    """
    Classe pour configurer et gérer les logs.
    """

    def __init__(self, logging_ini_path: str):
        """
        Initialise la configuration des logs avec le chemin du fichier INI.
        """
        self._setup_logging(logging_ini_path)

    def _setup_logging(self, logging_ini_path: str):
        """
        Configure les logs à partir du fichier INI.
        """
        if not os.path.exists(logging_ini_path):
            raise FileNotFoundError(f"Le fichier de configuration des logs '{
                                    logging_ini_path}' n'existe pas.")

        # Créer le dossier logs s'il n'existe pas
        if not os.path.exists('logs'):
            os.makedirs('logs')

        logging.config.fileConfig(
            logging_ini_path, disable_existing_loggers=False)
        # Configurer le hook d'exception
        sys.excepthook = self.__log_exception

    def __log_exception(self, exc_type, exc_value, exc_traceback):
        """
        Log les exceptions non gérées.
        """
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        logging.critical("Exception non gérée", exc_info=(
            exc_type, exc_value, exc_traceback))
