# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# invenio-oarepo-ui is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""OARepo UI module for invenio"""

from __future__ import absolute_import, print_function

from flask_babelex import gettext as _

from . import config


class OARepoUI(object):
    """invenio-oarepo-ui extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['invenio-oarepo-ui'] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith('INVENIO_OAREPO_UI_'):
                app.config.setdefault(k, getattr(config, k))
