#!/usr/bin/python

import time
import sys
from serial import Serial
tty = Serial("/dev/ttyUSB0", 57600)
start = "\xa0\xa2"
end = "\xb0\xb3"
# Do cold start
payload= "\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0C\xB4"

pack = lambda x: chr(x>>8)+chr(x&0xff)
checksum = sum(map(ord, list(payload))) & 0x7fff
length = len(payload)

message = start + pack(length) + payload + pack(checksum) + end
print (pack(checksum))
print repr(message)
print repr (pack(checksum))
tty.write(message)
tty.close()
print "Done cold restart. Waiting 60 seconds"
time.sleep(6)

sys.exit()
