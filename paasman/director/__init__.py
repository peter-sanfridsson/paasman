# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

from flask import Flask, request, jsonify
from paasman.director.manager import DirectorManager
from paasman.director import dispatcher

from werkzeug import secure_filename
from flask import send_from_directory
import requests
import etcd
import json



app = Flask(__name__)

# TODO: move the filepath to director.cfg
import os

UPLOAD_FOLDER = 'app/apps'
##UPLOAD_FOLDER ='_deployments/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def api_error(message, status=400):
    return jsonify(
        {"error": dict(
            message=message
        )}
    ), status

@app.route("/apps/", methods=["GET"])
def list_apps():
    dispatcher.tasks.put_nowait("hello!")

    ####    list all deployed apps
    ##with etcd
    #ls="{"
    #for key in e.list("apps"):
    #    if not app.key=="apps/ignore":
    #        ls+=key.key.lstrip('apps/')
    #        ls+=","
    #ls=ls.rstrip(",")
    #ls+="}"    
    #return ls,200

    return "added to queue"

@app.route("/apps/", methods=["POST"])
def deploy_app():
    file = request.files["file"]
    
    ##??
    ##appname = request.form.get("app", None)
    name = request.form.get('name',None)
    port = request.for.get('port',None)

    
    if not name or not file or not port:
        return api_error("name and file and port is required", 400)
    if file:
        #TODO: use manager.store_application()
        filename = secure_filename(file.filename)
        try:
            os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'],name)
        except:
            pass        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],name,filename))

        ##etcd stuff if we want it
        #e.set("app/"+name+"/file",filename)
        #e.set("app/"+name+"/in_port",port
        #instances#the director will crash if this in the wrong order
        #e.set("apps/"+name,1)
        return "{'host':"+name+".130.240.233.89.xip.io'}",200
    return "No file?"

@app.route("/apps/<appname>/", methods=["GET"])
def app_state(appname):
    return ""
    #return "{instances:\""+e.get("apps/"+appname).value+"\"}"
@app.route("/apps/<appname>/", methods=["PUT"])
def edit_app(appname):
    return ""
    #nummer= request.get_json()["instances"]
    #e.set("app/"+name,nummer)
    #return "",200

@app.route("/apps/<appname>/", methods=["DELETE"])
def delete_app(appname):
    return ""              
    #e.set("app/"+name+,0)
    #return "",200   

@app.route('/files/<appname>')
def uploaded_file(appname):
    try:
        filename=e.get("app/"+appname+"/file").value
        return send_from_directory(app.config['UPLOAD_FOLDER'],appname,
                               filename)
    except:
        return "something gone wrong",500
