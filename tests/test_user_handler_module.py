# -*- coding: utf-8 -*-
"""
Tests unitaires pour `app.handlers.user_handler`.
"""

import sys
import types
import asyncio
import pytest
from unittest.mock import MagicMock

# Fournir un module `fastapi` factice si non installé pour les tests unitaires
if 'fastapi' not in sys.modules:
    fastapi = types.ModuleType('fastapi')
    class HTTPException(Exception):
        def __init__(self, status_code: int, detail: str = ""):
            super().__init__(detail)
            self.status_code = status_code
            self.detail = detail
    class APIRouter:
        def __init__(self):
            pass
        def post(self, *args, **kwargs):
            def _decorator(fn):
                return fn
            return _decorator
        def get(self, *args, **kwargs):
            def _decorator(fn):
                return fn
            return _decorator
    fastapi.HTTPException = HTTPException
    fastapi.APIRouter = APIRouter
    sys.modules['fastapi'] = fastapi

from app.handlers.user_handler import UserHandler


def test_create_user_success():
    service = MagicMock()
    service.create_user.return_value = MagicMock(id=1, name="A", email="a@x.com")

    handler = UserHandler(service)
    result = asyncio.run(handler.create_user("A", "a@x.com"))

    assert result == service.create_user.return_value
    service.create_user.assert_called_once_with("A", "a@x.com")


def test_create_user_failure_raises_http_exception():
    service = MagicMock()
    service.create_user.side_effect = Exception("boom")

    handler = UserHandler(service)
    with pytest.raises(Exception):
        asyncio.run(handler.create_user("A", "a@x.com"))


def test_get_user_found():
    service = MagicMock()
    service.get_user_by_id.return_value = MagicMock(id=1, name="A", email="a@x.com")

    handler = UserHandler(service)
    result = asyncio.run(handler.get_user(1))

    assert result == service.get_user_by_id.return_value


def test_get_user_not_found_raises_http_exception():
    service = MagicMock()
    service.get_user_by_id.return_value = None

    handler = UserHandler(service)
    with pytest.raises(Exception):
        asyncio.run(handler.get_user(999))
