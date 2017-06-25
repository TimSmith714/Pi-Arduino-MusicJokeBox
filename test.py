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
            if float(device.analogRead(3)) > float(device.analogRead(4)):
                print "On"
            else:
                print "Off"

            print "Device 1: %0.2f" % (float(device.analogRead(3)) * 3.3 / 1024), "V"
            print "Device 2: %0.2f" % (float(device.analogRead(4)) * 3.3 / 1024), "V"
	    sleep(0.5)

	device.detach()
	device.stopDaemon()
        print 'script finished'
    else:
	print 'UUGear device is not currently installed'
except:
    print "Unexpected error:", sys.exc_info()[0]
    device.detach()
    device.stopDaemon()

