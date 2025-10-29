from app.models.user import User


def test_user_model_repr():
    """
    Teste la méthode __repr__ de la classe User.
    Couvre la ligne 40.
    """
    user = User(id=1, name="Alice", email="alice@example.com")
    assert repr(user) == "User(id=1, name='Alice', email='alice@example.com')"
