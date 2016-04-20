import Tkinter

class PartName(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.grid() #Create Grid Layout Manager
        
        label = Tkinter.Label(self,anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=0,columnspan=2,sticky="ew")
        
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=1,sticky="ew")
        self.entry.bind("<Return>",self.onPressEnter)
        
        button = Tkinter.Button(self,text=u"Comboborate",command=self.onButtonClick)
        button.grid(column=1,row=1)
    
        #Allow Column To Resize
        self.grid_columnconfigure(0,weight=1)
        #Allow H Resize, Disallow V Resize
        self.resizable(True,False)
        
    def onButtonClick(self):
        print "ButtonClick"
        
    def onPressEnter(self,event):
        print "PressEnter"
        
if __name__ == "__main__":
    app = PartName(None)
    app.title("Part Name")
    app.mainloop()