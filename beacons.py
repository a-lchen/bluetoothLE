from bluetooth.ble import BeaconService
import triangulate
import pygame
from time import sleep

class Beacon(object):
    
    def __init__(self, data, address):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
        
    def __str__(self):
        ret = "Beacon: address:{ADDR} uuid:{UUID} major:{MAJOR}"\
                " minor:{MINOR} txpower:{POWER} rssi:{RSSI}"\
                .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                        MINOR=self._minor, POWER=self._power, RSSI=self._rssi)
        return ret



pygame.init()
screen = pygame.display.set_mode((850,850))
pygame.draw.rect(screen, (255,255,255), (25,25,800,800), 0)
pygame.display.update

def visualize(x,y):
    pygame.draw.rect(screen, (255,255,255), (25,25,800,800), 0)
    pygame.draw.rect(screen, (0,0,0), (225, 225, 400, 400), 1)
    pygame.draw.rect(screen, (0,0,0), ((x*400)+225,(y*400)+225,10,10), 0)
    pygame.display.update
    pygame.display.flip()

service = BeaconService()
strength_history = []
while True:
    devices = service.scan(1)
    strengths = []
    locs = [(0,0), (1,0)]
    for address, data in list(devices.items()):
    	b = Beacon(data, address)
    	print(b)
	print triangulate.strength_to_length(b._rssi)
    	strengths.append(b._rssi)
    if (len(strengths) != 2):
        continue 
    strength_history.append(strengths)
    recent = strength_history[-10:]
    best_strengths = []
    for i in range(len(strengths)):
        best_strengths.append(max([el[i] for el in recent]))
    print ("recents = " + str(recent) + " best: "+ str(best_strengths)) 

    loc = triangulate.triangulate(locs, best_strengths)
    if loc:
        print (loc)
        visualize(loc[0],loc[1])


print("Done.")
