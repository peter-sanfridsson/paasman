# -*- coding: utf-8 -*-

import gevent
from paasman.agent import event_listener

if __name__ == "__main__":
    el = gevent.spawn(event_listener)
    gevent.joinall([el])
