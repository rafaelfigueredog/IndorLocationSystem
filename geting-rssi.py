from bluepy.btle import Scanner, DefaultDelegate
import time


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        """ if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr """




RSSI = []
timeout = time.time() + 300  
while True:
    if time.time() >= timeout:
        break
    
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(1.0)

    for dev in devices:
        if (dev.addr == "fb:c6:58:b7:fd:e1"):
            print '\x1b[2J\x1b[1;1H'
            print 'RSSI:', dev.rssi, 'dbm' 
            RSSI.append(dev.rssi)
        #print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        #for (adtype, desc, value) in dev.getScanData():
        #    print "  %s = %s" % (desc, value)

print(RSSI)
print(len(RSSI))
