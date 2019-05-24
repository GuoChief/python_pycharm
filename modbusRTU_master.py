# -*- coding: utf_8 -*-
import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = "COM4"
def modbus_getdata():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=19200, bytesize=8, parity='E', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        registersdata=master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4)
        print registersdata
    except modbus_tk.modbus.ModbusError as exc:
        print ("ERR")

##if __name__ == "__main__":
while True:
       modbus_getdata()
       time.sleep(10)