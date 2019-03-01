# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# invenio-oarepo-ui is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_oarepo_ui import OARepoUI


def test_version():
    """Test version import."""
    from invenio_oarepo_ui import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = OARepoUI(app)
    assert 'invenio-oarepo-ui' in app.extensions

    app = Flask('testapp')
    ext = OARepoUI()
    assert 'invenio-oarepo-ui' not in app.extensions
    ext.init_app(app)
    assert 'invenio-oarepo-ui' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to invenio-oarepo-ui' in str(res.data)
