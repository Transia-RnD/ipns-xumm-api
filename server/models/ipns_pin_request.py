# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server import util


class IPNSPinRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, key: str=None, json: Dict[str, object]=None):  # noqa: E501
        """IPNSPinRequest - a model defined in Swagger

        :param key: The key of this IPNSPinRequest.  # noqa: E501
        :type key: str
        :param json: The json of this IPNSPinRequest.  # noqa: E501
        :type json: Dict[str, object]
        """
        self.swagger_types = {
            'key': str,
            'json': Dict[str, object]
        }

        self.attribute_map = {
            'key': 'key',
            'json': 'json'
        }
        self._key = key
        self._json = json

    @classmethod
    def from_dict(cls, dikt) -> 'IPNSPinRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IPNSPinRequest of this IPNSPinRequest.  # noqa: E501
        :rtype: IPNSPinRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self) -> str:
        """Gets the key of this IPNSPinRequest.


        :return: The key of this IPNSPinRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this IPNSPinRequest.


        :param key: The key of this IPNSPinRequest.
        :type key: str
        """

        self._key = key

    @property
    def json(self) -> Dict[str, object]:
        """Gets the json of this IPNSPinRequest.


        :return: The json of this IPNSPinRequest.
        :rtype: Dict[str, object]
        """
        return self._json

    @json.setter
    def json(self, json: Dict[str, object]):
        """Sets the json of this IPNSPinRequest.


        :param json: The json of this IPNSPinRequest.
        :type json: Dict[str, object]
        """
        if json is None:
            raise ValueError("Invalid value for `json`, must not be `None`")  # noqa: E501

        self._json = json
