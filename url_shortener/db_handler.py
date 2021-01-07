# -*- coding: utf-8 -*
"""Database Handler class"""
import logging
import os

import psycopg2

from url_shortener import sql

logger = logging.getLogger(__name__)


class DBHandler:
    """class of Database Handler"""

    def __init__(self):
        logging.basicConfig(level=logging.INFO)"ok")
