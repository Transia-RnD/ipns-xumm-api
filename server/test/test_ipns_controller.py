#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import

from flask import json

from server.models.ipns_publish_request import IPNSPublishRequest  # noqa: E501
from server.test import BaseTestCase


class TestIPNSontroller(BaseTestCase):
    """TestIPNSontroller integration test stubs"""

    def test_ipns_publish(cls):
        """Test case for ipns_publish

        Resend verification email
        """
        cls.client.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {cls.token}'  # noqa: E501
        body = IPNSPublishRequest(cid='CID')
        response = cls.client.open(
            '/v1/ipns/publish',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
        )
        cls.assert200(
            response,
            'Response body is : ' + response.data.decode('utf-8')
        )

if __name__ == '__main__':
    import unittest
    unittest.main()
