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


@app.route("/", methods=["GET"])
def welcome():
    """welcome GET function"""
    return jsonify({"message": "Welcome"}), 201


@app.route("/shorten_url", methods=["POST"])
def post_shorten_url():
    """shorten url POST function"""
    if not request.json:
        return jsonify({"message": "not json format"}), 400

    if "url" not in request.json:
        return jsonify({"message": "url not found"}), 400

    url = request.json["url"]
    if url[:4] != "http":
        url = "http://" + url

    parsed_url = urllib.parse.urlparse(url)
    if not parsed_url.scheme:
        return jsonify({"message": "not valid url"}), 400

    db_handler = DBHandler()
    # check if shorter url is in database
    recode = db_handler.fetch_shortened((url,))
    now = datetime.datetime.now()
    if recode:
        # if shorter url is in database, update updated time
        db_handler.update(
            (
                now,
                url,
            )
        )
        return jsonify({"shortened": recode[0]}), 201
    # if not in url table, insert it
    shortened = shortener.shortener_factory(url)
    db_handler.insert((shortened, url, now, now))

    return jsonify({"shortened": shortened}), 201


@app.route("/shorten_url", methods=["GET"])
def shorten_url_get():
    """shorten url GET function"""
    return jsonify({"message": "must be POST"}), 400


@app.route("/remove/<shortened>", methods=["GET"])
def remove_shortened(shortened):
    """remove shortened GET function"""
    db_handler = DBHandler()
    recode = db_handler.fetch_original_url((shortened,))
    if recode:
        _ = db_handler.delete_shortener((shortened,))
        return (
            jsonify({"remove": shortened}),
            201,
        )

    return jsonify({"message": "shortened not found"}), 201

@app.route("/original_url", methods=["POST"])
def post_original_url():
    """original url POST function"""
    shortened = request.json["shortened"]

    db_handler = DBHandler()
    recode = db_handler.fetch_original_url((shortened,))
    if recode:
        # if shorter url is in database, update updated time
        db_handler.update(
            (
                datetime.datetime.now(),
                recode[1],
            )
        )
        return jsonify({"url": recode[1]}), 201
    return jsonify({"message": "unknow shortened"}), 400

def main():
    """ main function """
    logging.basicConfig(level=logging.INFO)
    app.run(port=os.getenv("APP_PORT"), debug=True)


if __name__ == "__main__":
    main()
