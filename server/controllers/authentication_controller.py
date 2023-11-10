#!/usr/bin/env python
# coding: utf-8

import logging
import connexion
from flask import abort
from typing import Dict, Any  # noqa: E501

from server.middleware import AppMiddleware

from server.models.message_response import MessageResponse  # noqa: E501
from server import util, error

logger = logging.getLogger('app')


def bearer_auth(token) -> AppMiddleware:
    """bearer_auth."""
    try:
        request_json = connexion.request.get_json()
        middleware: AppMiddleware = AppMiddleware(token, request_json)
        return {
            'claims': middleware.claims,
            'middleware': middleware,
        }
    except ValueError as e:
        logger.error(e)
        abort(401, str(e))

