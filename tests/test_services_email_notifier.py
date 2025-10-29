from app.services.email_notifier import EmailNotifier


def test_email_notifier_send_failure():
    """
    Teste le cas où l'envoi d'un email échoue.
    Couvre la ligne 43.
    """
    notifier = EmailNotifier(config_path="config/email_config.json")
    result = notifier.send_email(to="invalid-email", subject="Test", body="Message")
    assert result is False


def test_email_notifier_send_success():
    """
    Teste le cas où l'envoi d'un email réussit.
    Couvre la ligne 52.
    """
    notifier = EmailNotifier(config_path="config/email_config.json")
    result = notifier.send_email(to="valid@example.com", subject="Test", body="Message")
    assert result is True
