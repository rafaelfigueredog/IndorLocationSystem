# -*- coding: utf-8 -*-
from bluepy.btle import Scanner, DefaultDelegate
from datetime import datetime
import numpy as np
import time
import math

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
    print ' Contador: ', count 
    n = 3.00
    expoenteDist = -rssi-59/(10*n)
    distancia = math.pow(10, expoenteDist)
    distancias.append(distancia)
    print '\n Distancia:', distancia , 'm' 

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
    
nomeDoArquivo = raw_input("\nArquivo: ") # sem extensão
nomeDoArquivo = "dados/experimento6/" + nomeDoArquivo + ".txt"
arquivo = open(nomeDoArquivo, 'w')

rssiList = []
distancias = []

timeout, start_time = time.time() + 600, datetime.now()  

count = 0
while True:
    if (count >= 100):
        break
    
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(1)

    for dev in devices:
        if (dev.addr == "c8:fd:19:37:2b:0a"):
            count += 1
            imprime(dev.rssi)
            rssiList.append(dev.rssi)

end_time = datetime.now()
arquivo.write(str(rssiList))
arquivo.write('\n')
arquivo.write(str(distancias))
arquivo.write('\n')
arquivo.write('Experiment time: {} '.format(end_time - start_time))
arquivo.close()
print('\n Experiment time: {} '.format(end_time - start_time))