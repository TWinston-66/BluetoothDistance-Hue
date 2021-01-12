# BluetoothDistance-Hue

## Turn Hue Lights On/Off based on distance from host device

Determines RSSI then changes lights to match distance parameters 

## Installation
git clone https://github.com/TWinston-66/BluetoothDistance-Hue

python3 -m pip install -r requirements.txt

## Usage 
Change the `b` variable to match the IP or you Hue Bridge 

Change the `BT_ID` variable to match the Bluetooth ID of your target device 

Change the RSSI value in the `if` and `elif` statements to match distance criteria -- This will have to be tweaked 

Uncomment/Comment the `print(statusOUT)` statement if you want the RSSI value to be outputted 

sudo python3 Light_Track.py 

##Debug 

If you get an output similar to `connection refused` this either means the device cannot be found or has already been paired/connected 
