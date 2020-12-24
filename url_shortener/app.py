#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" app main file """
import datetime
import logging
import os
import urllib

from flask import Flask, jsonify, redirect, request

from url_shortener import DBHandler, UrlShortener


app = Flask(__name__)
shortener = UrlShortener()
logger = logging.getLogger(__name__)

def main():
    """ main function """
    logging.basicConfig(level=logging.INFO)
    app.run(port=os.getenv("APP_PORT"), debug=True)


if __name__ == "__main__":
    main()
