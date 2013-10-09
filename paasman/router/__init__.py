# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

# inspiration from https://github.com/rtyler/proxylet/blob/master/proxylet.py

from gevent import wsgi

def router(env, start_response):
    if env.get("REQUEST_METHOD", None) == "GET":
        return proxy(env, start_response)
    # otherwise, just return 501
    start_response("501 Not Implemented", [("Content-Type", "text/html")])
    return ["Proxy only allows GET"]

def proxy(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return ["Welcome to Paasman::proxy"]

def get_appname(hostname):
    """Parse the application name for the incoming.
    """
    try:
        return hostname.split(".")[0]
    except:
        return None

#wsgi.WSGIServer(("", 8000), router).serve_forever()