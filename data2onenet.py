# -*- coding: utf_8 -*-

import time
from socket import*


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    error = client.connect(('192.168.1.6', 1811))
    print error
    while True:
         time.sleep(1)