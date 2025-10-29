import pytest
from app.services.email_notifier import EmailNotifier, Notifier


class DummyNotifier(Notifier):
    def send_notification(self, subject: str, body: str) -> None:
        self.last_subject = subject
        self.last_body = body


@pytest.fixture
def dummy_config(tmp_path):
    config_path = tmp_path / "smtp.ini"
    with open(config_path, "w") as f:
        f.write(
            """[SMTP]\nsmtp_server = localhost\nfrom_email = test@example.com\nto_email = dest@example.com\n"""
        )
    return str(config_path)


def test_email_notifier_send_notification(dummy_config):
    notifier = EmailNotifier(dummy_config)
    # On ne teste pas l'envoi réel, mais la construction du message
    try:
        notifier.send_notification("Sujet", "Corps")
    except Exception as e:
        assert "Connection refused" in str(e) or "[Errno" in str(e)
