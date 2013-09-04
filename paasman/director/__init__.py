# -*- coding: utf-8 -*-
"""
    author: mikhln-9
"""

from flask import Flask

app = Flask(__name__)

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