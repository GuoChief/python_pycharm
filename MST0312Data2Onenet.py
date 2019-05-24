# -*- coding: utf_8 -*-
import time
import datetime
import urllib2
import json
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

APIKEY='syfr5BYgL1goHp0zkA7VwfRWmDY='
PORT = "COM4"

def http_put(netsend_data):
    CurTime = datetime.datetime.now()
    url='http://api.heclouds.com/devices/527178171/datapoints'
    values={"datastreams":[{"id":"level","datapoints":[{"at":CurTime.isoformat(),"value":netsend_data[0]}]},{"id":"distance","datapoints":[{"at":CurTime.isoformat(),"value":netsend_data[1]}]},{"id":"temperature","datapoints":[{"at":CurTime.isoformat(),"value":netsend_data[2]}]},{"id":"height","datapoints":[{"at":CurTime.isoformat(),"value":netsend_data[3]}]}]}
    jdata = json.dumps(values)
    request = urllib2.Request(url,jdata)
    request.add_header('api-key',APIKEY)
    request.get_method = lambda:'POST'
    try:
        request = urllib2.urlopen(request)
    except ValueError or urllib2:
        time.sleep(20)
    return request.read()

def modbus_getdata():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=19200, bytesize=8, parity='E', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        registersdata=master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4)
    except modbus_tk.modbus.ModbusError as exc:
        print ("ERR")
    return registersdata

def main():
    read_data=modbus_getdata()
    resp = http_put(read_data)
    print "OneNET_Ans:\n %s" % resp
    time.sleep(10)

if __name__ == '__main__':
    while True:
         main()