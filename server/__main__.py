#!/usr/bin/env python
# coding: utf-8

import os
import connexion

from server import encoder
from server import error
from flask_cors import CORS

# common
APP_ENV = 'config.TestConfig'

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        'latest.yaml',
        arguments={'title': 'IPNS Xumm Api'},
        pythonic_params=True
    )
    app.add_error_handler(
        error.BadRequestError, 
        error.bad_request_handler
    )
    app.add_error_handler(
        error.NotAuthorizedError, 
        error.not_auth_handler
    )
    app.add_error_handler(
        error.NotFoundError, 
        error.not_found_handler
    )
    app.add_error_handler(
        error.InternalServerError, 
        error.internal_handler
    )
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 9000)),
        debug=False if APP_ENV == 'config.ProductionConfig' else True
    )


if __name__ == '__main__':
    main()
