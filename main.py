from PartNameGenerator import PartNameGenerator
from PartDescGenerator import PartDescGenerator

import os
import os.path
import string

import Tkinter
import tkMessageBox
from Tkinter import *

class PartNamer(Tkinter.Tk):
    def __init__(self,parent):
        #Call Super's Constructor
        Tkinter.Tk.__init__(self,parent)
        #Store Reference To Parent
        self.parent = parent
        #Initialize GUI
        self.initializeWindow()
        
    def initializeWindow(self):
        #Create Grid Layout Manager
        self.grid() 
        #Create Title Label
        self.titleLabel = Tkinter.Label(self,anchor="c",text="PART NAME GEN",fg="white",bg="blue")
        self.titleLabel.grid(column=0,row=0,columnspan=2,sticky="ew")
        #Create Manufacturer Label
        self.manufacturerLabel = Tkinter.Label(self,anchor="c",text="Manufacturer",fg="blue",bg="white")
        self.manufacturerLabel.grid(column=0,row=1,columnspan=1,sticky="ew")
        #Create Type Option Label
        self.typeLabel = Tkinter.Label(self,anchor="c",text="Part Type",fg="blue",bg="white")
        self.typeLabel.grid(column=1,row=1,columnspan=1,sticky="ew")
        #Create Manufacturer Entry
        self.manufacturerVar = Tkinter.StringVar()
        self.manufacturerEntry = Tkinter.Entry(self, textvariable=self.manufacturerVar)
        self.manufacturerEntry.grid(column=0,row=2,sticky="ew")
        self.manufacturerEntry.bind("<Return>",self.onPressEnter)
        #Create Type Option Menu
        self.typeList = self.getPartTypes()
        self.typeVar  = Tkinter.StringVar()
        self.typeVar.set("Engine")
        self.typeMenu = Tkinter.OptionMenu(self,self.typeVar,*self.typeList)
        self.typeMenu.config(width=20)
        self.typeMenu.grid(column=1,row=2,stick="ew")
        #Create Generate Button
        self.generateButton = Tkinter.Button(self,text=u"Generate",command=self.onGenerateButtonClick)
        self.generateButton.grid(column=0,row=3,columnspan=2,sticky="ew")
        #Create Output Frame
        self.outputFrame = Frame(self)
        self.outputFrame.grid(column=0,row=4,columnspan=2,rowspan=1,stick="w")
        #Create Output Field
        self.outputText = Text(self.outputFrame, height=15)
        self.outputText.pack(side="left",fill="both",expand=True)
        #Create Output Scrollbar
        self.outputScroll = Scrollbar(self.outputFrame)
        self.outputText.config(yscrollcommand=self.outputScroll.set)
        self.outputScroll.config(command=self.outputText.yview)
        self.outputScroll.pack(side="right",fill="y")
        #Create Clear Button
        self.clearButton = Tkinter.Button(self,text=u"Clear",command=self.onClearButtonClick)
        self.clearButton.grid(column=0,row=5,columnspan=2,sticky="ew")
        
        #Allow Column To Resize
        self.grid_columnconfigure(0,weight=1)
        #Disallow H Resize, Disallow V Resize
        self.resizable(False,False)
        
    def onGenerateButtonClick(self):
        print "ButtonClick", self.typeVar.get()
        if not self.manufacturerVar.get() == "":
            #Clear the output frame
            self.outputText.delete(1.0,END)
            #Create a new name generator
            nameGenerator = PartNameGenerator(self.manufacturerVar.get(),self.typeVar.get())
            #Get dictionary containing full name and name components
            nameDict = nameGenerator.generateName()
            name   = nameDict['name']
            serial = nameDict['serial']
            alias  = nameDict['alias']
            spec   = nameDict['spec']
            #Output full name to output frame
            self.outputText.insert(END,name + "\n")
            #Create a new description generator
            descGenerator = PartDescGenerator(serial,alias,spec,self.manufacturerVar.get())
            #Output full description to output frame
            self.outputText.insert(END,descGenerator.generateDesc())
        else:
            self.showError("Manufacturer Cannot Be Blank")
        
    def onClearButtonClick(self):
        self.outputText.delete(1.0,END)
        
    def onPressEnter(self,event):
        print "PressEnter"
        
    def showError(self, message):
        tkMessageBox.showinfo("Error",message)
        
    def getPartTypes(self):
        if os.path.isfile("res/Types.txt"):
            with open("res/Types.txt") as file:
                types = file.read().splitlines()
            return types
        else:
            return ["Engine"]
        
        
if __name__ == "__main__":
    app = PartNamer(None)
    app.title("Part Name Generator")
    app.mainloop()