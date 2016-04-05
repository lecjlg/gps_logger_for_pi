#!/usr/bin/python
from serial import Serial
import time
import sys
print ("Sychronise Protocol and Baud Rate x10 - ascii")

protobaud = '$PSRF100,0,57600,8,1,0*37'"\r\n"

count = 9
while (count < 10):

    tty = Serial("/dev/ttyUSB0", 4800)
    tty.write(protobaud+"\n\r")
    print ("sending command")
    print (protobaud+"\n")
    tty.close()
    time.sleep(.300)
    count = count + 1


