# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

from gevent import wsgi

def router(env, start_response):
	start_response("200 OK", [("Content-Type", "text/html")])
	return ["Welcome to Paasman."]

wsgi.WSGIServer(("", 8000), router).serve_forever()