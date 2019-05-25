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


def imprime(rssi):
    print '\x1b[2J\x1b[1;1H'
    print '\n RSSI:',rssi,'dbm'
    print '\n Distancia:', (10 **((-59 - rssi)/(10*2))) , 'm' 
    
nomeDoArquivo = raw_input("\nArquivo: ") # sem extensão
nomeDoArquivo += ".txt"
arquivo = open(nomeDoArquivo, 'w')

RSSI = []

timeout, start_time = time.time() + 300, datetime.now()  
while True:
    if time.time() >= timeout:
        break
    
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(0.5)

    for dev in devices:
        if (dev.addr == "fb:c6:58:b7:fd:e1"):
            imprime(dev.rssi)
            RSSI.append(dev.rssi)
        #print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        #for (adtype, desc, value) in dev.getScanData():
        #    print "  %s = %s" % (desc, value)
arquivo.write(str(RSSI))
arquivo.close()
end_time = datetime.now()
print('\nExperiment time: {} \n'.format(end_time - start_time))