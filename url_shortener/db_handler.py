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
        logging.basicConfig(level=logging.INFO)

    @staticmethod
    def _execute(sql_message, data, return_function=None):
        """connect and execute sql message
        :param sql_message: sql message
        :param data: sql message
        :param return_function: sql type, could be insert or fetchone
        :return: record depend on return function type
        """
        conn = None
        record = None
        try:
            # read database configuration
            params = {
                "database": os.getenv("POSTGRES_DB"),
                "user": os.getenv("POSTGRES_USER"),
                "host": os.getenv("POSTGRES_HOST"),
                "password": os.getenv("POSTGRES_PASSWORD"),
                "port": os.getenv("POSTGRES_PORT"),
            }
            # make connection
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # execute sql message
            cur.execute(sql_message, data)
            if return_function in [
                    "insert",
                    "update",
                    "delete",
                    "deprecation",
            ]:
                record = cur.rowcount
                logger.info("{} record changed".format(record))
            elif return_function == "fetchone":
                record = cur.fetchone()
                logger.info(record)
            # commit
            conn.commit()
        except Exception as error:
            logger.error(error)
        finally:
            if conn is not None:
                conn.close()

        return record

    def insert(self, data):
        """insert data
        :param data: in format (shortener, original_url, created)
        :return: number of records updated
        """
        return self._execute(sql.INSERT, data, return_function="insert")

    def fetch_shortened(self, data):
        """fetch shortened
        :param data: in format (original_url)
        :return: shorter url record
        """
        return self._execute(
            sql.GET_SHORTENER, data, return_function="fetchone"
        )

    def update(self, data):
        pass

    def fetch_original_url(self, data):
        pass

    def deprecation(self, data):
        pass

    def delete_shortener(self, data):
        pass
