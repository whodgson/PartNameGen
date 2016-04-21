import Tkinter

class PartName(Tkinter.Tk):
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
        self.manufacturerEntry = Tkinter.Entry(self)
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
        
        #Allow Column To Resize
        self.grid_columnconfigure(0,weight=1)
        #Disallow H Resize, Disallow V Resize
        self.resizable(False,False)
        
    def onButtonClick(self):
        print "ButtonClick", self.typeVar.get()
        
    def onPressEnter(self,event):
        print "PressEnter"
        
if __name__ == "__main__":
    app = PartName(None)
    app.title("Part Name Generator")
    app.mainloop()