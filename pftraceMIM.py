import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2.TkinterDnD import _require
from webbrowser import open_new_tab

class ControllerFrame():
    def __init__(self):
        self.port = -1
        self.enabled = False

    def StartDeamon(self, pid = -1):
        return
    
    def StopDeamon(self):
        self.enabled = False
        return

class pftraceMIM(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH)
        
        # init tkinterdnd2
        _require(self) 

        self.button = ttk.Button(self, text="Hello World")
        self.button.pack(side="top")
        self.drop_target_register('DND_Files')
        self.dnd_bind('<<DropEnter>>', self.DragEnter)
        self.dnd_bind('<<DropLeave>>', self.DragLeave)
        self.dnd_bind('<<Drop>>', self.Drop)

    def DragEnter(self, event):
        event.widget.focus_force()
        print('Entering %s' % event.widget)

    def DragLeave(self, event):
        print('Leaving %s' % event.widget)

    def Drop(self, event):
        print('Dropped %s' % event.widget)
        #open_new_tab('https://github.com/altria-polaris/pftraceMIM')

if __name__ == "__main__":

    app = ttk.Window("Trace Processor Multi-Instance Manager", "darkly", resizable=(False, False), size=(768,640))
    pftraceMIM(app)
    app.mainloop()