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

# TODO: we should start the etcd process so we can follow leader, or?
etcd_client = etcd.Etcd("172.17.42.1", follow_leader=False)
# we mount the coreos /var/ to /coreos_run/
docker_client = docker.Client("unix://coreos_run/docker.sock")

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
    #while True:
    #    print "hello"
    #    gevent.sleep(0)

def docker_worker():
    """Manage a queue and perform actions via the hosts docker remote api"""