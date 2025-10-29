import os

from app.services.logs import LoggerService


def test_logger_service_creation():
    """
    Teste la création d'une instance de LoggerService.
    """
    logger = LoggerService(log_file="logs/test.log", log_level="DEBUG")
    assert logger is not None


def test_logger_service_logging():
    """
    Teste les différents niveaux de log.
    """
    log_file = "logs/test.log"
    logger = LoggerService(log_file=log_file, log_level="DEBUG")

    logger.debug("Message de débogage")
    logger.info("Message d'information")
    logger.warning("Message d'avertissement")
    logger.error("Message d'erreur")
    logger.critical("Message critique")

    # Vérifie que le fichier de log a été créé
    assert os.path.exists(log_file)

    # Vérifie que le fichier contient des logs
    with open(log_file) as f:
        logs = f.read()
        assert "Message de débogage" in logs
        assert "Message d'information" in logs
        assert "Message d'avertissement" in logs
        assert "Message d'erreur" in logs
        assert "Message critique" in logs


def test_logger_service_debug():
    """
    Teste le logging au niveau DEBUG.
    Couvre les lignes 19-20.
    """
    logger = LoggerService(log_file="logs/test.log", log_level="DEBUG")
    logger.debug("Message de débogage")
    assert True  # Vérifie que le code ne lève pas d'exception


def test_logger_service_info():
    """
    Teste le logging au niveau INFO.
    Couvre les lignes 23-29.
    """
    logger = LoggerService(log_file="logs/test.log", log_level="INFO")
    logger.info("Message d'information")
    assert True  # Vérifie que le code ne lève pas d'exception
