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

    @staticmethod
    def deprecation_rows():
        """deprecation rows
        delete rows whose updated time < now - delta
        :return: None
        """
        db_handler = DBHandler()
        delta = datetime.timedelta(seconds=DELTA)
        record = db_handler.deprecation((datetime.datetime.now() - delta,))
        logger.info("delete {} row".format(record))

