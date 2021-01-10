from phue import Bridge
import time
import subprocess

b = Bridge('10.0.0.2')
ON = False
connect = subprocess.check_output(["rfcomm", "connect", "0", "CC:2D:B7:B8:F6:DB", "10", ">/dev/null &"])

while True:
    status = subprocess.check_output(["hcitool", "rssi", "CC:2D:B7:B8:F6:DB"])
    statusOUT = str(status)
    statusOUT = statusOUT.replace('RSSI return value', '')
    statusOUT = statusOUT.replace("b'", '')
    statusOUT = statusOUT.replace("'", '')
    statusOUT = statusOUT.replace(':', '')
    statusOUT = statusOUT.replace('\\n', '')
    #print(statusOUT)
    #Arrived Turn Lights On 
    if int(statusOUT) > -5 and ON == False:
        ON = True
        #time.sleep(4)
        b.set_light(3, 'on', True)
        b.set_light(2, 'on', True)
        b.set_light(1, 'on', True)
        time.sleep(4)
    #Left Turn Lights Off
    elif int(statusOUT) < -4 and ON == True: 
        ON = False
        #time.sleep(3)
        b.set_light(3, 'on', False)
        b.set_light(2, 'on', False)
        b.set_light(1, 'on', False)
        time.sleep(4)

    time.sleep(0.3)