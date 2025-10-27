# -*- coding: utf-8 -*-
"""
Test simple pour `app._version`.
"""

from app import _version


def test_version_variables_present():
    assert hasattr(_version, '__version__')
    assert hasattr(_version, 'version')
    assert isinstance(_version.version, str)
    assert len(_version.version) > 0
    # Cover additional generated symbols
    assert hasattr(_version, '__version_tuple__')
    assert hasattr(_version, 'version_tuple')
    assert hasattr(_version, '__commit_id__')
    assert hasattr(_version, 'commit_id')
    # Basic sanity on types/values
    assert isinstance(_version.version_tuple, tuple)
    assert isinstance(_version.commit_id, str)
