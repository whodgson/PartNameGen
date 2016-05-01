import os
import os.path
import string
import random

class PartNameGenerator:
    def __init__(self,manufacturerName,typeName):
        self.manufacturerName = manufacturerName
        self.typeName = typeName
    def generateName(self):
        partNameSerial = ""
        partNameSerialLength = 3
        partNameAlias = ""
        partNameSpec = ""
        #Generate Random Serial
        partNameSerial = self.manufacturerName[0] + self.typeName[0] + "-" \
        + self.generateSerial(partNameSerialLength)
        #Get Random Alias if File Exists
        if os.path.isfile("res/" + self.typeName + "Alias.txt"):
            with open("res/" + self.typeName + "Alias.txt") as file:
                lines = file.read().splitlines()
            partNameAlias = random.choice(lines)
        #Get Rnadom Spec if File Exists
        if os.path.isfile("res/" + self.typeName + "Spec.txt"):
            with open("res/" + self.typeName + "Spec.txt") as file:
                lines = file.read().splitlines()
            partNameSpec = random.choice(lines)
        else:
            partNameSpec = "Part"
        #Return Generated Part Name
        return partNameSerial + " '" + partNameAlias + "' " + partNameSpec
    
    def generateSerial(self,size):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return "".join(random.choice(chars) for _ in range(size))
    