# -*- coding: utf-8 -*-
""" deprecation system which will automatically remove useless URL """
import datetime
import logging
import time

from url_shortener import DBHandler

logger = logging.getLogger(__name__)

DELTA = 60

class DeprecationHandler:
    """ deprecation handler class """
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
