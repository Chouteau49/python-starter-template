import smtplib
from email.mime.text import MIMEText
from configparser import ConfigParser


class EmailNotifier:
    """
    Classe pour envoyer des notifications par email.
    """

    def __init__(self, config_path: str):
        """
        Initialise le notifier avec le chemin du fichier de configuration.
        """
        self.config = ConfigParser()
        self.config.read(config_path)

    def send_email(self, subject: str, body: str):
        """
        Envoie un email avec le sujet et le corps spécifiés.
        """
        smtp_server = self.config.get('SMTP', 'smtp_server')
        from_email = self.config.get('SMTP', 'from_email')
        to_email = self.config.get('SMTP', 'to_email')

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        with smtplib.SMTP(smtp_server) as server:
            server.sendmail(from_email, [to_email], msg.as_string())
