# -*- coding: utf_8 -*-
import urllib2
import json
import time
import datetime

APIKEY='syfr5BYgL1goHp0zkA7VwfRWmDY='

def http_put():
    CurTime = datetime.datetime.now()
    url='http://api.heclouds.com/devices/527178171/datapoints'
    values={"datastreams":[{"id":"level","datapoints":[{"at":CurTime.isoformat(),"value":12}]},{"id":"distance","datapoints":[{"at":CurTime.isoformat(),"value":45}]},{"id":"temperature","datapoints":[{"at":CurTime.isoformat(),"value":76}]},{"id":"height","datapoints":[{"at":CurTime.isoformat(),"value":90}]}]}
    jdata = json.dumps(values)
    request = urllib2.Request(url,jdata)
    request.add_header('api-key',APIKEY)
    request.get_method = lambda:'POST'
    try:
        request = urllib2.urlopen(request)
    except ValueError or urllib2:
        time.sleep(20)
    return request.read()

def main():
    time.sleep(10)
    resp = http_put()
    print "OneNET_Ans:\n %s" % resp
    time.sleep(10)

if __name__ == '__main__':
    while True:
         main()
