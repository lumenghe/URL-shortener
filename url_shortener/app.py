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

