# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

from flask import Flask
from paasman.director.manager import DirectorManager

app = Flask(__name__)

# TODO: move the filepath to director.cfg
import os
manager = DirectorManager(os.path.abspath("../paasman/_deployments/"))

@app.route("/apps/", methods=("GET"))
def list_apps():
    return ""

@app.route("/apps/", methods=("POST"))
def deploy_app():
    return ""

@app.route("/apps/<int:id>/", methods=("GET"))
def app_state(id):
    return ""

@app.route("/apps/<int:id>/", methods=("PUT"))
def edit_app(id):
    return ""

@app.route("/apps/<int:id>/", methods=("DELETE"))
def delete_app(id):
    return ""
