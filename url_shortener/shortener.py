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

