from bluetooth.ble import BeaconService
import triangulate
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
    
    strength_history.append(strengths)
    recent = strength_history[-10:]
    best_strengths = []
    for i in range(len(strengths)):
        best_strengths.append(max([el[i] for el in recent]))
    print ("recents = " + str(recent) + " best: "+ str(best_strengths)) 

    loc = triangulate.triangulate(locs, best_strengths)
    if loc:
        print (loc)


print("Done.")
