# -*- coding: utf-8 -*-

import gevent
import zmq.green as zmq
from gevent.queue import Queue

tasks = Queue()

zmq_ctx = zmq.Context()

def worker():
    while 1:
        task = tasks.get()
        print "working: %s" % task
        gevent.sleep(0)

def manager():
    socket = zmq_ctx.socket(zmq.REP)
    socket.bind("tcp://*:5111")

    while True:
        r = socket.recv()
        tasks.put_nowait(r)
        socket.send("you said %s" % r)