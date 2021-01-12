from phue import Bridge
import time
import subprocess

b = Bridge('127.0.0.1')
BT_ID = "00:11:22:33:FF:EE" 
ON = False

connect = subprocess.check_output(["rfcomm", "connect", "0", BT_ID, "10", ">/dev/null &"])

while True:
    status = subprocess.check_output(["hcitool", "rssi", BT_ID])
    statusOUT = str(status)
    statusOUT = statusOUT.replace('RSSI return value', '')
    statusOUT = statusOUT.replace("b'", '')
    statusOUT = statusOUT.replace("'", '')
    statusOUT = statusOUT.replace(':', '')
    statusOUT = statusOUT.replace('\\n', '')
    #print(statusOUT)
    
    if int(statusOUT) > -5 and ON == False:
        ON = True
        b.set_light(3, 'on', True)
        b.set_light(2, 'on', True)
        b.set_light(1, 'on', True)
        time.sleep(4)
    
    elif int(statusOUT) < -4 and ON == True: 
        ON = False
        b.set_light(3, 'on', False)
        b.set_light(2, 'on', False)
        b.set_light(1, 'on', False)
        time.sleep(4)

    time.sleep(0.3)
