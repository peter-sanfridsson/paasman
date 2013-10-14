# -*- coding: utf-8 -*-

from fabrick.api import *

env.user = "core"
# or let hosts be defined as cli arguments?
env.hosts = "10.10.10." # change to openstack ip on remote deployment

project_path = "/home/core/"
