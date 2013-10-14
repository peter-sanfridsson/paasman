# -*- coding: utf-8 -*-
"""
    authors
    =======
    mikhln-9
    sanpet-8
"""

# inspiration from https://github.com/rtyler/proxylet/blob/master/proxylet.py
# and https://gist.github.com/ncode/1074646

from gevent import wsgi
import sys
import urllib2
import etcd
import traceback
from cgi import escape
from random import choice

def router(env, start_response):
    if env.get("REQUEST_METHOD", None) == "GET":
        return proxy(env, start_response)
    # otherwise, just return 501
    start_response("501 Not Implemented", [("Content-Type", "text/html")])
    return ["Proxy only allows GET"]

def proxy(env, start_response):
    http_host = env['HTTP_HOST']
    path=get_appname(http_host)
    try:
        try:
            response = urllib2.urlopen(path)
        except urllib2.HTTPError:
            response = sys.exc_info()[1]
        print ('%s: %s %s' % (path, response.code, response.msg))
        headers = [(k, v) for (k, v) in response.headers.items()]
    except Exception:
        ex = sys.exc_info()[1]
        sys.stderr.write('error while reading %s:\n' % path)
        traceback.print_exc()
        tb = traceback.format_exc()
        start_response('502 Bad Gateway', [('Content-Type', 'text/html')])
        error_str = escape(str(ex) or ex.__class__.__name__ or 'Error')
        return ['<h1>%s</h1><h2>%s</h2><pre>%s</pre>' % (error_str, escape(path), escape(tb))]
    else:
        start_response('%s %s' % (response.code, response.msg), headers)
        data = response.read()
        return [data]

def get_appname(hostname):
    """Parse the application name for the incoming.
    """
    e=etcd.Etcd(host="172.17.42.1")
    try:
        appname=hostname.split(".")[0]
        listofinstances=[]
        ls = e.get("apps/"+appname+"/running")
            for key in ls:
                listofinstances.append(key.value())
            port=choice(listofinstances)
            return "172.17.42.1:"+port
    except:
        return ""
    
wsgi.WSGIServer(("", 80), router).serve_forever()
