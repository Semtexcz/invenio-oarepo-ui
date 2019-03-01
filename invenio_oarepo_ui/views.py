# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# invenio-oarepo-ui is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""OARepo UI module for invenio"""

from __future__ import absolute_import, print_function

from flask import Blueprint, current_app, jsonify, request, session
from flask_login import current_user

blueprint = Blueprint(
    'invenio_oarepo_ui',
    __name__,
    url_prefix='/oarepo/1.0'
)


@blueprint.route("/collections")
def collections():
    # get all record rest endpoints and present them as collections
    collections = current_app.config.get('INVENIO_OAREPO_UI_COLLECTIONS', {})
    collections = [
        {
            'code': k,
            **v
        } for k, v in collections.items()
    ]

    return jsonify(collections)


@blueprint.route('/auth/status')
def login_status():
    if current_user.is_anonymous:
        resp = {
            'logged_in': False,
            'user': None,
            'user_info': None
        }
    else:
        resp = {
            'logged_in': True,
            'user': {
                'id': current_user.id,
                'email': current_user.email,
                'roles': [
                    {
                        'id': x.name,
                        'label': x.description
                    } for x in current_user.roles
                ]
            },
            'user_info': session.get('user_info', None).to_dict()
        }

    return jsonify(resp)
