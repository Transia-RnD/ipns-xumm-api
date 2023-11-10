import logging
# import os
# from typing import Dict, Any
import jwt

logger = logging.getLogger('app')


def verify_xumm_token(token):
    """
    Decode a JWT token without verifying its signature.

    WARNING: This method should NOT be used in production or with sensitive data,
    as it does not verify the authenticity of the token.

    :param token: The JWT token to decode.
    :return: The decoded token payload.
    """
    try:
        # Decode the token without verification
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        return decoded_token
    except jwt.exceptions.DecodeError as e:
        # Handle the error (e.g., log it, raise an exception, return None, etc.)
        print(f"Decode error: {e}")
        return None

def get_token(headers):
    return headers.get('Authorization').split(' ').pop()


def get_ip_address(request):
    ip_address = None
    try:
        ip_address = request.headers.get(
            'X-Forwarded-For',
            request.remote_addr
        )
    except Exception as e:
        logger.error(e)
        ip_address = request.remote_addr
    
    return ip_address
