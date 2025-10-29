from app.core.exceptions import (
    AppException,
    DatabaseException,
    UserNotFoundException,
    ValidationException,
)


def test_app_exception():
    """Test AppException générique."""
    e = AppException("Erreur générique", 501)
    assert str(e) == "Erreur générique"
    assert e.status_code == 501


def test_user_not_found_exception():
    """Test UserNotFoundException."""
    e = UserNotFoundException(123)
    assert "123" in str(e)
    assert e.status_code == 404


def test_validation_exception():
    """Test ValidationException."""
    e = ValidationException("champ manquant")
    assert "champ manquant" in str(e)
    assert e.status_code == 400


def test_database_exception():
    """Test DatabaseException."""
    e = DatabaseException("connexion perdue")
    assert "connexion perdue" in str(e)
    assert e.status_code == 500
