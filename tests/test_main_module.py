# -*- coding: utf-8 -*-
"""
Tests unitaires pour `app.main`.
"""

from unittest.mock import patch, MagicMock
import sys

import main as app_main


def test_main_calls_sys_exit_on_success():
    mock_app = MagicMock()
    mock_app.run.return_value = True

    with patch('main.Application', return_value=mock_app):
        with patch('sys.exit') as mock_exit:
            app_main.main()
            # sys.exit called with not success -> not True == False
            mock_exit.assert_called_once_with(False)


def test_main_calls_sys_exit_on_failure():
    mock_app = MagicMock()
    mock_app.run.return_value = False

    with patch('main.Application', return_value=mock_app):
        with patch('sys.exit') as mock_exit:
            app_main.main()
            mock_exit.assert_called_once_with(True)
