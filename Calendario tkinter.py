from tkinter import *
from tkinter import ttk
import datetime
import calendar



"""class Month():
    dates:
    moth: actual.month
    year: actual.year
    def setdates():
    
class date():
    date:
    actual.date
    active:"True or False"
    weekend:
    setdate(date):
    setactive(True/False):
    
class Calendar(ttk.Frame):
    header: 
    daysName:
    strmonth:
    activeYear:
    activemonth:
    def __init__():
    def backYear:
    def backMonth:
    def forYear:
    def forMonth:"""
b = tuple(calendar.month_name)
a = tuple(calendar.day_abbr)
print(a)
print(b)
mesactual=(b[1])

class Mainapp(Tk):
    __strmes = None
    __mes = None
    __mesmas = None
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        self.configure(bg = "#DED7B9")
        self.Header()
        self.diassemana()
    def Header(self):
        self.label = ttk.Label(self, text=(mesactual))
        self.label.pack()
        self.bt1 = ttk.Button(self, text=" << ").place(x=24.5, y=5)
        self.bt1 = ttk.Button(self, text=" < ").place(x=83.5, y=5)
        self.bt1 = ttk.Button(self, text=" > ").place(x=398.5, y=5)
        self.bt1 = ttk.Button(self, text=" >> ").place(x=457.5, y=5)
    def diassemana(self, **args):
        """cont=0
        sitio=0
        while len(a) > cont:
            Label(self, text=a[cont]).place(x=sitio, y=38)
            sitio +=76
            cont +=1"""
        
        self.lunes = ttk.Label(self, text="lunes").place(x=0, y=38)
        self.martes = ttk.Label(self, text="martes").place(x=76, y=38)
        self.miercoles = ttk.Label(self, text="miercoles").place(x=152, y=38)
        self.jueves = ttk.Label(self, text="jueves").place(x=228, y=38)
        self.viernes = ttk.Label(self, text="viernes").place(x=304, y=38)
        self.sabado = ttk.Label(self, text="sabado").place(x=380, y=38)
        self.domingo = ttk.Label(self, text="domingo").place(x=456, y=38)

    def start(self):
            self.mainloop()



if __name__ == "__main__":
    app = Mainapp()
    app.start()