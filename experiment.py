# -*- coding: utf-8 -*-
from bluepy.btle import Scanner, DefaultDelegate
from datetime import datetime
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        """ if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr """


"""   
def imprime(rssi):
    print '\x1b[2J\x1b[1;1H'
    print '\n RSSI:',rssi,'dbm' """

RSSI = []
sizeRSSI = 0
start_time = datetime.now()  
while sizeRSSI < 600:
    
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10)

    for dev in devices:
        if (dev.addr == "7c:01:0a:77:3c:b9"):
            #imprime(dev.rssi)
            RSSI.append(dev.rssi)
            sizeRSSI += 1
        #print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        #for (adtype, desc, value) in dev.getScanData():
        #    print "  %s = %s" % (desc, value)

end_time = datetime.now()
print '\n Experiment time: {} \n'.format(end_time - start_time)
print ' RSSI:', RSSI 
print "\n Dados Coletados: ", sizeRSSI
