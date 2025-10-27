# -*- coding: utf-8 -*-
"""
Tests unitaires pour `app.db.connection`.
"""

import sys
import types
import pytest
from unittest.mock import patch, MagicMock

# Insérer un module sqlalchemy factice si l'environnement ne l'a pas installé
if 'sqlalchemy' not in sys.modules:
    sqlalchemy = types.ModuleType('sqlalchemy')
    sqlalchemy.Engine = object
    def _fake_create_engine(url):
        return MagicMock()
    sqlalchemy.create_engine = _fake_create_engine
    orm = types.ModuleType('sqlalchemy.orm')
    # Provide Session and sessionmaker symbols expected by the module
    class Session:  # dummy type for annotation compatibility
        pass
    def _fake_sessionmaker(**kwargs):
        return MagicMock()
    orm.Session = Session
    orm.sessionmaker = _fake_sessionmaker
    sys.modules['sqlalchemy'] = sqlalchemy
    sys.modules['sqlalchemy.orm'] = orm

from app.db.connection import DatabaseConnection


def test_get_session_raises_when_not_connected():
    db = DatabaseConnection("sqlite:///./test.db")
    with pytest.raises(RuntimeError):
        db.get_session()


@patch('app.db.connection.create_engine')
@patch('app.db.connection.sessionmaker')
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
    mock_SessionLocal.return_value = 'session-instance'
    session = db.get_session()
    assert session == 'session-instance'


@patch('app.db.connection.create_engine')
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
