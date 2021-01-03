# -*- coding: utf-8 -*-
"""shortener generator class"""
import base64
import logging
from hashlib import blake2b

logger = logging.getLogger(__name__)


class UrlShortener:
    """class of generating a 8 bytes hash shorter url."""

    DIGEST_SIZE = 8

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def shortener_factory(self, url):
        """factory which builds shortener
        :param url: original url
        :return: shorter url
        """
        hashed = blake2b(url.encode("utf-8"), digest_size=self.DIGEST_SIZE)
        base64_bytes = base64.b64encode(hashed.digest(), altchars=b"@~")
        base64_message = base64_bytes.decode("utf-8")
        return base64_message
