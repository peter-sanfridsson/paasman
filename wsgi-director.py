# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""
import gevent
from gevent import wsgi
from paasman.director import app

from paasman.director import dispatcher

if __name__ == "__main__":
    gevent.spawn(dispatcher.worker)
    gevent.spawn(dispatcher.manager)
    print "started dispatcher worker"

    wsgi.WSGIServer(("", 8001), app).serve_forever()
