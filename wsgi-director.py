# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

from gevent import wsgi
from paasman.director import app

if __name__ == "__main__":
    wsgi.WSGIServer(("", 8001), app).serve_forever()
