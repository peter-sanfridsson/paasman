# -*- coding: utf-8 -*-

import gevent
from gevent.queue import Queue

tasks = Queue()

def worker():
    while 1:
        task = tasks.get()
        print "working: %s" % task
        gevent.sleep(0)