from PartNameGenerator import PartNameGenerator

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
        self.typeList = ["Engine","LF Tank","LFO Tank"]
        self.typeVar  = Tkinter.StringVar()
        self.typeVar.set("Engine")
        self.typeMenu = Tkinter.OptionMenu(self,self.typeVar,*self.typeList)
        self.typeMenu.config(width=20)
        self.typeMenu.grid(column=1,row=2,stick="ew")
        #Create Generate Button
        self.generateButton = Tkinter.Button(self,text=u"Generate",command=self.onButtonClick)
        self.generateButton.grid(column=0,row=3,columnspan=2,sticky="ew")
        #Create Output Frame
        self.outputFrame = Frame(self)
        self.outputFrame.grid(column=0,row=4,columnspan=2,rowspan=1,stick="w")
        #Create Output Field
        self.outputText = Text(self.outputFrame, height=15)
        self.outputText.pack(side="left",fill="both",expand=True)
        # Create Output Scrollbar
        self.outputScroll = Scrollbar(self.outputFrame)
        self.outputText.config(yscrollcommand=self.outputScroll.set)
        self.outputScroll.config(command=self.outputText.yview)
        self.outputScroll.pack(side="right",fill="y")
        
        #Allow Column To Resize
        self.grid_columnconfigure(0,weight=1)
        #Disallow H Resize, Disallow V Resize
        self.resizable(False,False)
        
    def onButtonClick(self):
        print "ButtonClick", self.typeVar.get()
        if not self.manufacturerVar.get() == "":
            nameGenerator = PartNameGenerator(self.manufacturerVar.get(),self.typeVar.get())
            self.outputText.delete(1.0,END)
            self.outputText.insert(END,nameGenerator.generateName() + "\n")    
        else:
            self.showError("Manufacturer Cannot Be Blank")
        
    def onPressEnter(self,event):
        print "PressEnter"
        
    def showError(self, message):
        tkMessageBox.showinfo("Error",message)
        
if __name__ == "__main__":
    app = PartNamer(None)
    app.title("Part Name Generator")
    app.mainloop()