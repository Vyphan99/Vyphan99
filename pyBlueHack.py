#This script that avertises a bluetooth low energy beacon for 15 seconds 

import time #<--import time is the first party through Python

from bluetooth.ble import BeaconServices #<-- 3rd party module 

#Create an instance of the onject from the 3rd party class

service = BeaconServices() #<--Create a Beacon service

#start avertising with   |               UUIDs                 | Parameters 
service.start_advertising("11111111-2222-3333-4444-555555555555, 1, 1, 1, 200") #<-- TCP,UDP

time.sleep(15) #<--Stop the service at every 15 sec 

service.stop_advertising() #<-- Create a stop service to stop every 15 sec 

print("Done.")#<--Print function: print the "Done." message on the screen 