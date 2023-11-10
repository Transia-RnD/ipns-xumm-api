#!/usr/bin/env python
# coding: utf-8

import logging
import connexion
from typing import Dict, Any

# server
from server.models.ipns_publish_request import IPNSPublishRequest  # noqa: E501
from server.models.message_response import MessageResponse  # noqa: E501
from server.error import (
    BadRequestError,
    NotAuthorizedError,
    NotFoundError,
    InternalServerError,
    bad_request_handler,
    not_auth_handler,
    not_found_handler,
    internal_handler,
)
from server.middleware import AppMiddleware

# Create Logger
logger = logging.getLogger("app")


def ipns_publish(body, token_info: Dict[str, Any]):  # noqa: E501
    """Publish an IPNS CID

     # noqa: E501

    :param body: CID to publish
    :type body: dict | bytes

    :rtype: MessageResponse
    """
    try:
        if connexion.request.is_json:
            body = IPNSPublishRequest.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

        # We assume at this moment the object exists.
        # print(token_info)
        print(token_info['claims'])
        # print(body)
        # print(token_info)
        return MessageResponse(200, 'success', 'IPNS Publish Successful')

    except BadRequestError as e:
        # Handle bad request error
        logger.error(f'BadRequestError: {str(e)}')
        return bad_request_handler(e)
    except NotAuthorizedError as e:
        # Handle not authorized error
        logger.error(f'NotAuthorizedError: {str(e)}')
        return not_auth_handler(e)
    except NotFoundError as e:
        # Handle not found error
        logger.error(f'NotFoundError: {str(e)}')
        return not_found_handler(e)
    except InternalServerError as e:
        # Handle internal server error
        logger.error(f'InternalServerError: {str(e)}')
        return internal_handler(e)
    except Exception as e:
        # Handle other exceptions
        logger.error(f'Exception: {str(e)}')
        return internal_handler(e)
