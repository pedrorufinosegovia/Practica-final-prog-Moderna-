from tkinter import *
from tkinter import ttk
import datetime

"""class Calendar():"""
"""class Month():"""
"""class date():"""
class Mainapp(Tk):
    """calendario = Calendar()"""
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
    def start(self):
        self.root.mainloop()

        



if __name__ == "__main__":
    app = Mainapp()
    app.start()