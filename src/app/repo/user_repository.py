"""
Interfaces et implémentations pour les repositories.
"""

from abc import ABC, abstractmethod

from app.models.user import User


class UserRepository(ABC):
    """
    Interface pour le repository des utilisateurs.
    """

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def find_all(self) -> list[User]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass


class InMemoryUserRepository(UserRepository):
    """
    Implémentation en mémoire pour les tests/démo.
    """

    def __init__(self):
        self.users = {}
        self.next_id = 1

    def save(self, user: User) -> User:
        if user.id is None:
            user.id = self.next_id
            self.next_id += 1
        self.users[user.id] = user
        return user

    def find_by_id(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def find_all(self) -> list[User]:
        return list(self.users.values())

    def delete(self, user_id: int) -> bool:
        return self.users.pop(user_id, None) is not None
