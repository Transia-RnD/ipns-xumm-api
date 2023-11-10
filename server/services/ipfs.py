#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Optional, Any, Tuple

import ipfshttpclient

from server.middleware import AppMiddleware

class AppIPFSService(object):

    client: Any = None
    middleware: AppMiddleware = None

    def __init__(
        cls,
        middleware: AppMiddleware,
    ):
        cls.middleware = middleware
        cls.client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

    def ipfs_file(cls, path: str):
        try:
            res = cls.client.add(path)
            return res['Hash']
        except Exception as e:
            raise e

    def add_str(cls, string: str):
        try:
            res = cls.client.add_str(string)
            return res['Hash']
        except Exception as e:
            raise e

    def add_bytes(cls, byte: bytes):
        try:
            res = cls.client.add_bytes(byte)
            return res['Hash']
        except Exception as e:
            raise e

    def ipfs_json(cls, dict: Dict[str, Any]):
        try:
            res = cls.client.add_json(dict)
            return res['Hash']
        except Exception as e:
            raise e

    def ipfs_pin(cls, cid: str):
        try:
            ipns_res = cls.client.pin.add(cid)
            return ipns_res['Name']
        except Exception as e:
            raise e

    def ipns_publish(cls, cid: str):
        try:
            ipns_res = cls.client.name.publish(f"/ipfs/{cid}")
            return ipns_res['Name']
        except Exception as e:
            raise e

    def ipns_resolve(cls, name: str):
        try:
            resolved = cls.client.name.resolve(name)
            return resolved['Path']
        except Exception as e:
            raise e