# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server import util


class IPNSPublishResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None):  # noqa: E501
        """IPNSPublishResponse - a model defined in Swagger

        :param name: The name of this IPNSPublishResponse.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'IPNSPublishResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IPNSPublishResponse of this IPNSPublishResponse.  # noqa: E501
        :rtype: IPNSPublishResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this IPNSPublishResponse.


        :return: The name of this IPNSPublishResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this IPNSPublishResponse.


        :param name: The name of this IPNSPublishResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name
