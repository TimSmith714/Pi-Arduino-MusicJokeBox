from time import sleep
from UUGear import *

print 'starting'

UUGearDevice.setShowLogs(0)

try: 
    device = UUGearDevice('UUGear-Arduino-8483-2314')

    if device.isValid():
        for i in range(10):
            print str(i)
            print "Device 1: %0.2f" % (float(device.analogRead(0)) * 3.3 / 1024), "V"
            print "Device 2: %0.2f" % (float(device.analogRead(1)) * 3.3 / 1024), "V"
	    sleep(0.5)

	device.detach()
	device.stopDaemon()
    else:
	print 'UUGear device is not currently installed'
except(e):
    print 'Error:' + str(e)

