# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

from flask import Flask, request, jsonify
from paasman.director.manager import DirectorManager

app = Flask(__name__)

# TODO: move the filepath to director.cfg
import os
manager = DirectorManager("_deployments/")

def api_error(message, status=400):
    return jsonify(
        {"error": dict(
            message=message
        )}
    ), status

@app.route("/apps/", methods=["GET"])
def list_apps():
    return ""

@app.route("/apps/", methods=["POST"])
def deploy_app():
    file = request.files["file"]
    appname = request.form.get("app", None)
    if not appname or not file:
        return api_error("name and file is required", 400)
    if file:
        #TODO: use manager.store_application()
        file.save(os.path.join("_deployments", file.filename))
        return file.filename
    return "No file?"

@app.route("/apps/<int:id>/", methods=["GET"])
def app_state(id):
    return ""

@app.route("/apps/<int:id>/", methods=["PUT"])
def edit_app(id):
    return ""

@app.route("/apps/<int:id>/", methods=["DELETE"])
def delete_app(id):
    return ""
