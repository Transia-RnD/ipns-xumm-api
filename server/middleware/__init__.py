#!/usr/bin/env python
# coding: utf-8

import logging
from typing import Dict, Any

from server.middleware.utils import verify_xumm_token
from server.error import InternalServerError

logger = logging.getLogger('app')

API_ENV: str = 'config.ProductionConfig'

class AppMiddleware(object):

    claims: Dict[str, Any] = None

    @classmethod
    def mock(
        cls,
        claims: Dict[str, Any],
    ) -> 'AppMiddleware':
        cls.claims = claims
        return cls

    def __init__(
        cls,
        token: str,
        request_json: Dict[str, Any],
    ) -> 'AppMiddleware':

        if API_ENV == 'config.TestConfig':
            cls.claims: Dict[str, Any] = {
                'user_id': '9VMygWuiDaeY5iom4Wh6cyofFVi1',
                'email': 'test@transia.co'
            }
            return None

        cls.claims: Dict[str, Any] = verify_xumm_token(token)
        # import json
        # print(json.dumps(cls.claims, indent=4, sort_keys=True))
        if cls.claims['firebase']['sign_in_provider'] != 'oidc.xumm':
            raise InternalServerError('invalid parameters')
