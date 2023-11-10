#!/usr/bin/env python
# coding: utf-8

import logging
import connexion
from typing import Dict, Any

# server
from server.models.ipns_pin_request import IPNSPinRequest  # noqa: E501
from server.models.ipns_pin_response import IPNSPinResponse  # noqa: E501
from server.models.ipns_publish_request import IPNSPublishRequest  # noqa: E501
from server.models.ipns_publish_response import IPNSPublishResponse  # noqa: E501
from server.models.ipns_resolve_request import IPNSResolveRequest  # noqa: E501
from server.models.ipns_resolve_response import IPNSResolveResponse  # noqa: E501
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
from server.services.ipfs import AppIPFSService

# Create Logger
logger = logging.getLogger("app")


def ipns_pin_json(body, token_info: Dict[str, Any]):  # noqa: E501
    """Pin an IPNS Json

     # noqa: E501

    :param body: Json to pin
    :type body: dict | bytes

    :rtype: IPNSPinResponse
    """
    try:
        if connexion.request.is_json:
            body = IPNSPinRequest.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

        client = AppIPFSService(token_info['middleware'])
        key_name: str = client.create_key(client.middleware.claims['user_id'])
        cid = client.ipfs_json(body.json)
        ipns_name = client.ipns_publish(cid, key_name)
        return IPNSPinResponse(ipns_name)

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


def ipns_publish(body, token_info: Dict[str, Any]):  # noqa: E501
    """Publish an IPNS CID

     # noqa: E501

    :param body: CID to publish
    :type body: dict | bytes

    :rtype: IPNSPublishResponse
    """
    try:
        if connexion.request.is_json:
            body = IPNSPublishRequest.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

        client = AppIPFSService(token_info['middleware'])
        ipns_name = client.ipns_publish(body.cid)
        return IPNSPublishResponse(ipns_name)

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


def ipns_resolve(body, token_info: Dict[str, Any]):  # noqa: E501
    """Resolve an IPNS Name

     # noqa: E501

    :param body: Name to resolve
    :type body: dict | bytes

    :rtype: IPNSResolveResponse
    """
    try:
        if connexion.request.is_json:
            body = IPNSResolveRequest.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

        client = AppIPFSService(token_info['middleware'])
        ipns_cid = client.ipns_resolve(body.name)
        return IPNSResolveResponse(ipns_cid)

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
