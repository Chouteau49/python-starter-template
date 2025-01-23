import logging
from configparser import ConfigParser
from services.logs import Logs
from services.args import Args
from services.email_notifier import EmailNotifier


class Application:
    """
    Classe principale de l'application.
    """
    __banner__ = "Template de base pour projet python"
    __version__ = "1.0.0"

    def __init__(self):
        """
        Initialise l'application avec les arguments, les logs et la configuration.
        """
        self._args = Args().parse()
        self._logs = Logs(self._args.logging)
        self._conf = ConfigParser()
        self._conf.read(self._args.config)
        self._email_notifier = EmailNotifier(self._args.config)

    def run(self) -> bool:
        """
        Exécute l'application.
        """
        logging.info(self.__banner__)
        logging.info(f"Version: {self.__version__}")
        logging.info("Démarrage de l'application")
        self.send_error_email(Exception("Test d'envoi d'email d'erreur"))
        logging.info("Fin de l'exécution de l'application")
        return True

    def send_error_email(self, error: Exception):
        """
        Envoie un email en cas d'erreur.
        """
        try:
            self._email_notifier.send_email(
                "Erreur dans l'application",
                f"Une erreur est survenue lors de l'exécution de l'application: \n\n{
                    error}"
            )
            logging.info("Email d'erreur envoyé avec succès.")
        except Exception as e:
            logging.error(f"Erreur lors de l'envoi de l'email d'erreur: {e}")
