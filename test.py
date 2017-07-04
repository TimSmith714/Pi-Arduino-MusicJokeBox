from time import sleep
from UUGear import *
import sys
import pygame
import datetime
import os

print 'starting init'
pygame.init()
UUGearDevice.setShowLogs(0)
fname = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M') + "-log.txt"
open(fname, 'a')

try: 
    device = UUGearDevice('UUGear-Arduino-8483-2314')

    if device.isValid():
        device.setPinModeAsOutput(13)
        pygame.mixer.music.load('track01.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.pause()
        for i in range(30):
            print str(i)
            if float(device.analogRead(3)) > float(device.analogRead(4)):
                print "On"
                if pygame.mixer.music.get_busy == False:
                    pygame.mixer.music.unpause()
            else:
                print "Off"
                if pygame.mixer.music.get_busy == True:
                    pygame.mixer.music.pause()

            print "Device 1: %0.2f" % (float(device.analogRead(3)) * 3.3 / 1024), "V"
            print "Device 2: %0.2f" % (float(device.analogRead(4)) * 3.3 / 1024), "V"
            f = open(fname, 'ab')
            f.write(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M.%S') + "\n")
            f.close()
	    sleep(0.5)
            if float(device.analogRead(4)) * 3.3 / 1024 < 0.1:
                print("Stopping script")
                pygame.mixer.music.stop()
                device.detach()
                device.stopDaemon()
                pygame.quit()
                print("Script Stopped")
                exit()


	pygame.mixer.music.stop()
        device.detach()
        device.stopDaemon()
        pygame.quit()
        print("Script Finished")
    else:
	print 'UUGear device is not currently installed'
except:
    print "Unexpected error:", sys.exc_info()[0]
    device.detach()
    device.stopDaemon()
    print("Script Finished")

