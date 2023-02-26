#Jacob R. Butler
#RevUC 2023
#
#Handles reading and writing character values to RFID tags

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#reader = None

#Reads in Character from tag
def readCharacter():
    reader = SimpleMFRC522()
    
    try:
        
        id, characterStringIn = reader.read()
    finally:
        GPIO.cleanup()
        
        
    return characterStringIn


#Writes out character to tag
def writeCharacter(characterStringOut):
    reader = SimpleMFRC522()
    
    try:
        
        
        reader.write(characterStringOut)
    finally:
        GPIO.cleanup()
        
    
    return