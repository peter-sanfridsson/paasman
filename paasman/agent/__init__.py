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

#etcd_client = etcd.Etcd("172.17.42.1")
docker_client = docker.Client("/run/docker.sock")

def event_listener():
    print docker_client.info()
    #while True:
    #    print "hello"
    #    gevent.sleep(0)