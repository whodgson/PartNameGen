import os
import os.path
import string
import random

class PartNameGenerator:
    def __init__(self,manufacturerName,typeName):
        self.manufacturerName = manufacturerName
        self.typeName = typeName
        
    def generateName(self):
        partNameSerial = self.generateSerial(self.manufacturerName,self.typeName,3)
        partNameAlias = self.getAlias(self.typeName)
        partNameSpec = self.getSpec(self.typeName)
        #Return Generated Part Name
        if(partNameAlias != ""):
            return partNameSerial + " " + partNameAlias + " " + partNameSpec
        else:
            return partNameSerial + " " + partNameSpec
    
    def generateAlphanumeric(self,size):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return "".join(random.choice(chars) for _ in range(size))
    
    def generateSerial(self,manufacturerName,typeName,size):
        return manufacturerName[0] + typeName[0] + "-" \
        + self.generateAlphanumeric(size)
        
    def getAlias(self,typeName):
        if os.path.isfile("res/" + typeName + "Alias.txt"):
            with open("res/" + typeName + "Alias.txt") as file:
                lines = file.read().splitlines()
            return "'" + random.choice(lines) + "'"
        else:
            return ""
        
    def getSpec(self,typeName):
        if os.path.isfile("res/" + typeName + "Spec.txt"):
            with open("res/" + typeName + "Spec.txt") as file:
                lines = file.read().splitlines()
            return random.choice(lines)
        else:
            return "Part"