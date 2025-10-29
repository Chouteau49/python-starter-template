import pytest
from app.handlers.user_handler import get_user_service, router
from app.models.user import User
from app.services.user_service import IUserService
from fastapi import FastAPI, status
from fastapi.testclient import TestClient


class DummyUserService(IUserService):
    def __init__(self):
        self.users = {1: User(id=1, name="Default User", email="default@example.com")}

    def create_user(self, name: str, email: str) -> User:
        if not name or not email:
            raise ValueError("Invalid data")
        user_id = max(self.users.keys(), default=0) + 1
        user = User(id=user_id, name=name, email=email)
        self.users[user_id] = user
        return user

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def get_all_users(self) -> list[User]:
        return list(self.users.values())

    def delete_user(self, user_id: int) -> bool:
        return self.users.pop(user_id, None) is not None


@pytest.fixture
def app():
    app = FastAPI()
    app.dependency_overrides[get_user_service] = lambda: DummyUserService()
    app.include_router(router)
    return app


@pytest.fixture
def client(app):
    return TestClient(app)


def test_create_user_success(client):
    response = client.post(
        "/users", json={"name": "Alice", "email": "alice@example.com"}
    )
    assert (
        response.status_code == status.HTTP_201_CREATED
    )  # Correction du statut attendu
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


@pytest.mark.parametrize(
    "name,email",
    [
        ("", "test@example.com"),
        ("Bob", ""),
        ("", ""),
    ],
)
def test_create_user_invalid(client, name, email):
    response = client.post("/users", json={"name": name, "email": email})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_get_user_success(client):
    response = client.get("/users/1")  # Utilise l'utilisateur par défaut
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Default User"


def test_create_user_invalid_data(client):
    """
    Teste le cas où les données fournies pour créer un utilisateur sont invalides.
    """
    response = client.post("/users", json={"name": " ", "email": " "})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_get_user_not_found(client):
    """
    Teste le cas où l'utilisateur demandé n'existe pas.
    Couvre les lignes 33-34.
    """
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Utilisateur non trouvé"


def test_get_user_error(client):
    """
    Teste le cas où une erreur se produit lors de la récupération d'un utilisateur.
    Couvre les lignes 37-39.
    """
    response = client.get("/users/invalid")
    assert response.status_code in (400, 422)  # Erreur de validation ou récupération


@pytest.mark.parametrize("user_id", [-1, 0, "abc"])
def test_get_user_invalid_id(client, user_id):
    response = client.get(f"/users/{user_id}")
    assert response.status_code in (
        status.HTTP_404_NOT_FOUND,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


@pytest.mark.parametrize("user_id,expected_status", [(1, 200), (999, 404)])
def test_get_user(user_id, expected_status, client):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == expected_status


def test_create_user(client):
    payload = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.post("/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == payload["name"]


def test_create_user_error(client):
    """
    Teste le cas où la création d'un utilisateur échoue.
    Couvre les lignes 20-22.
    """
    response = client.post("/users", json={"name": " ", "email": " "})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_delete_user(client):
    """
    Teste la suppression d'un utilisateur existant et inexistant.
    Couvre les lignes 54-56.
    """
    # Cas où l'utilisateur existe
    user_id = 1  # Utilise l'utilisateur par défaut
    payload = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.post("/users", json=payload)
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK


def test_delete_user_not_found(client):
    """
    Teste le cas où l'utilisateur à supprimer n'existe pas.
    Couvre les lignes 51-53.
    """
    response = client.delete("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Utilisateur non trouvé"


def test_delete_user_error(client):
    """
    Teste le cas où une erreur se produit lors de la suppression d'un utilisateur.
    Couvre les lignes 67-68.
    """
    response = client.delete("/users/invalid")
    assert response.status_code in (400, 422)  # Erreur de validation ou suppression
