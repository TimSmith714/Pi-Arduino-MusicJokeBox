from time import sleep
from UUGear import *
import sys

print 'starting'

UUGearDevice.setShowLogs(0)

try: 
    device = UUGearDevice('UUGear-Arduino-8483-2314')

    if device.isValid():
        for i in range(10):
            print str(i)
            analog_one = float(device.analogRead(3)) * 3.3 / 1024
            analog_two = float(device.anaogRead(4)) * 3.3 / 1024
            if analog_one > analog_two:
                print "On"
            else:
                print "Off"

            print "Device 1: %0.2f" % (float(device.analogRead(3)) * 3.3 / 1024), "V"
            print "Device 2: %0.2f" % (float(device.analogRead(4)) * 3.3 / 1024), "V"
	    sleep(0.5)

	device.detach()
	device.stopDaemon()
    else:
	print 'UUGear device is not currently installed'
except:
    #print 'Error:' + str(e)
    print "Unexpected error:", sys.exc_info()[0]

