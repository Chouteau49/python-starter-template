"""
Tests unitaires pour `app.db.connection`.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from unittest.mock import MagicMock, patch

import pytest
from app.db.connection import DatabaseConnection


def test_get_session_raises_when_not_connected():
    db = DatabaseConnection("sqlite:///./test.db")
    with pytest.raises(RuntimeError):
        db.get_session()


@patch("app.db.connection.create_engine")
@patch("app.db.connection.sessionmaker")
def test_connect_and_get_session_success(mock_sessionmaker, mock_create_engine):
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine

    # sessionmaker returns a callable (SessionLocal)
    mock_SessionLocal = MagicMock()
    mock_sessionmaker.return_value = mock_SessionLocal

    db = DatabaseConnection("sqlite:///./test.db")
    db.connect()

    assert db.engine is mock_engine
    assert db.SessionLocal is mock_SessionLocal

    # Ensure get_session returns the result of calling SessionLocal
    mock_SessionLocal.return_value = "session-instance"
    session = db.get_session()
    assert session == "session-instance"


@patch("app.db.connection.create_engine")
def test_connect_failure_raises(mock_create_engine):
    mock_create_engine.side_effect = Exception("no db")

    db = DatabaseConnection("sqlite:///./bad.db")
    with pytest.raises(Exception):
        db.connect()


def test_disconnect_calls_dispose():
    db = DatabaseConnection("sqlite:///./test.db")
    mock_engine = MagicMock()
    db.engine = mock_engine
    db.disconnect()
    mock_engine.dispose.assert_called_once()
