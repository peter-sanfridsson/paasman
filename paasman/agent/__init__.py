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

etcd_client = etcd.Etcd("172.17.42.1")
docker_client = docker.Client("/run/docker.sock")

#director_address = 

def director_address():
    """Listening on changes on the director address to the ZeroMQ"""

def event_listener():
    print docker_client.info()
    #while True:
    #    print "hello"
    #    gevent.sleep(0)

def docker_worker():
    """Manage a queue and perform actions via the hosts docker remote api"""