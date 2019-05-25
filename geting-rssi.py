from bluepy.btle import Scanner, DefaultDelegate
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            """ print "Discovered device", dev.addr """
        elif isNewData:
            print "Received new data from", dev.addr

dist = []
for i in range(10):
    
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)

    if (len(devices) == 0):
        dist.append("NR")
        continue

    for dev in devices:
        print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        dist.append(dev.rssi)
        """ for (adtype, desc, value) in dev.getScanData():
            print "  %s = %s" % (desc, value) """

print(dist)