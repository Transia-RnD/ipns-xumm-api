#!/usr/bin/env python
# coding: utf-8

import connexion
import os

from server import encoder
from server import error
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

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

# Main Flask App Run
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('API_PORT', 9000)), debug=True)