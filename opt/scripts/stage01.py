#!/usr/bin/python
import time
import sys
from serial import Serial

# Set NMEA mode at 4800 baud
#---------------------------------------------------------------------------
print("Attempting to Switch GPS into NMEA mode")

tty = Serial("/dev/ttyUSB0", 4800)
pack = lambda x: chr(x>>8)+chr(x&0xff)
start = '\xa0\xa2'
end = '\xb0\xb3'

payload = '\x81\x02\x01\x01\x00\x01\x01\x01\x05\x01\x01\x01\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x12\xC0'
checksum = sum(map(ord, list(payload))) & 0x7fff
length = len(payload)

nmeamode = start + pack(length) + payload + pack(checksum) + end
print ("sending command")
print repr(nmeamode)
tty.write(nmeamode)
tty.close()

print ("try again")

tty = Serial("/dev/ttyUSB0", 4800)
tty.write(nmeamode)
tty.close()

print ("closing")
sys.exit()

#Sychronise Protocol and Baud Rate - ascii
#---------------------------------------------------------------------------

print ("Sychronise Protocol and Baud Rate x10 - ascii")

protobaud= '$PSRF100,0,57600,8,1,0*37'

count = 0
while (count < 10):
    tty.write(protobaud)
    print ("sending command")
    print (protobaud)
    time.sleep(.300)
    count = count + 1

print ("sleep for 5 seconds")
time.sleep(5)




#Synchronise Protocol and Baud Rate - binary
#---------------------------------------------------------------------------
print ("Sychronise Protocol and Baud Rate x10 - binary")


pack = lambda x: chr(x>>8)+chr(x&0xff)
start = '\xa0\xa2'
end = '\xb0\xb3'
payload = '\x86\x00\x00\xE1\x00\x08\x01\x00\x00'
checksum = sum(map(ord, list(payload))) & 0x7fff
length = len(payload)
protobaudhex = start + pack(length) + payload + pack(checksum) + end

count = 0
while (count < 10):
    tty.write(protobaudhex)
    print ("sending command")
    print repr(protobaudhex)
    time.sleep(.300)
    count = count + 1

print ("sleep for 5 seconds")
time.sleep(5)



# Do cold start
#---------------------------------------------------------------------------
print ("Attempt a cold reset")

payload = "\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0C\x94"
checksum = sum(map(ord, list(payload))) & 0x7fff
length = len(payload)
message = start + pack(length) + payload + pack(checksum) + end
print repr(message)
tty.write(message)



#print ("-----------------------------------------")
#print ("start")
#print repr(start)
#
#print ("end")
#print repr(end)
#
#print ("payload")
#print repr(payload)

#print ("pack length")
#print (pack)

#print ("checksum")
#print repr(pack(checksum))

