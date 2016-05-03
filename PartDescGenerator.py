import os
import os.path
import string
import random

class PartDescGenerator:
    def __init__(self,serial,alias,spec,manufacturer):
        self.serial       = serial
        self.alias        = alias
        self.spec         = spec
        self.manufacturer = manufacturer
        
    def generateDesc(self):
        if(self.alias != ""):
            return "The '" + self.alias + "' " + self.spec + ", from " + self.manufacturer
        else:
            return "The " + self.serial + " " + self.spec + ", from " + self.manufacturer