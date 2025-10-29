import smtplib
from abc import ABC, abstractmethod
from configparser import ConfigParser
from email.mime.text import MIMEText


class Notifier(ABC):
    """
    Interface pour les notificateurs.
    """

    @abstractmethod
    def send_notification(self, subject: str, body: str) -> None:
        pass


class EmailNotifier(Notifier):
    """
    Notificateur par email.
    """

    def __init__(self, config_path: str) -> None:
        self._config: ConfigParser = ConfigParser()
        self._config.read(config_path)

    def _build_message(
        self, subject: str, body: str, from_email: str, to_email: str
    ) -> MIMEText:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email
        return msg

    def send_notification(self, subject: str, body: str) -> None:
        smtp_server: str = self._config.get("SMTP", "smtp_server")
        from_email: str = self._config.get("SMTP", "from_email")
        to_email: str = self._config.get("SMTP", "to_email")

        msg: MIMEText = self._build_message(subject, body, from_email, to_email)

        with smtplib.SMTP(smtp_server) as server:
            server.sendmail(from_email, [to_email], msg.as_string())

    def send_email(self, to: str, subject: str, body: str) -> bool:
        """
        Simule l'envoi d'un email. Retourne False si l'email est invalide.
        """
        if "@" not in to:  # Vérification basique de l'email
            return False
        # Logique simulée pour l'envoi d'email
        return True
