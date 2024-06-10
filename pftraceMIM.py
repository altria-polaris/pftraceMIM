import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class pftraceMIM(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH)

        self.button = ttk.Button(self, text="Hello World")
        self.button.pack(side="top")

if __name__ == "__main__":

    app = ttk.Window("Trace Processor Multi-Instance Manager", "darkly", resizable=(False, False), size=(768,640))
    pftraceMIM(app)
    app.mainloop()