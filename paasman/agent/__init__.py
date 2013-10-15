# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

import gevent
import etcd
import docker
import zmq.green as zmq

# TODO: we should start the etcd process so we can follow leader, or?
etcd_client = etcd.Etcd("172.17.42.1", follow_leader=False)
# we mount the coreos /var/ to /coreos_run/
docker_client = docker.Client("unix://coreos_run/docker.sock")

zmq_ctx = zmq.Context()
subscriber = zmq.socket(zmq.SUB)
subscriber.connect("tcp://172.17.42.1:5555") # TODO: 172.17.42.1 on a single node, change when clustering

teller = zmq.socket(zmq.REQ)
teller.connect("tcp://172.17.42.1:5111") # 172.17.42.1 on a single node, change when clustering

try:
    # Try to fetch the directors publish address (in pub/sub)
    director_address = ec.get("director_publish_addr").value
except:
    director_address = None

def director_address():
    """Listening on changes on the director address to the master server (ZeroMQ)"""
    while True:
        addr = etcd.watch("director_publish_addr")
        director_address = addr.value

def event_listener():
    print docker_client.info()
    while True:
        print "send to master"
        teller.send("node is calling")
        response = teller.recv() # blocking, wait on response from server
        # we may use timeout on recv and put the request to an internal queue and
        #   when the master response, we send the queued commands
        print response

        gevent.sleep(5) # wait 5 seconds since we doesn't want to send a flood of messages

def docker_worker():
    """Manage a queue and perform actions via the hosts docker remote api"""
