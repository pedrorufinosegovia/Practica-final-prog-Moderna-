from tkinter import *
from tkinter import ttk
import datetime
from datetime import date, datetime 
import calendar
ahora = datetime.now()
meses = tuple(calendar.month_name)
diassemana = tuple(calendar.day_abbr)
intmesactual=ahora.month
añoactual=ahora.year
strmesactual = meses[ahora.month]

"""class Month():
    mesactual =
    moth: actual.month
    year: actual.year
    def setdates():
    
class date():
    date:
    actual.date
    active:"True or False"
    weekend:
    setdate(date):
    setactive(True/False):"""
    
class Calendar(ttk.Frame):
    __strmes = None
    __mes = None
    __mesmas = None
    meses = tuple(calendar.month_name)
    intmesactual=ahora.month
    añoactual=ahora.year
    strmesactual = meses[ahora.month]
    ahora = datetime.now()
    def __init__(self, parent, **args):
        ttk.Framne.__init__(self, parent, width=532, heigth=422)
        self.Botones()
        self.Diassemana()
        
    def Botones(self):
        self.cabecera = ttk.Frame(self, width=532, heigth=40).place(x=0,y=0)
        self.anhomenos = ttk.Button(self.cabecera, text=" << ")
        self.anhomenos.place(x=24.5, y=5)
        self.mesmenos = ttk.Button(self.cabecera, text=" < ")
        self.mesmenos.place(x=83.5, y=5)
        self.mesmas = ttk.Button(self.cabecera, text=" > ")
        self.mesmas.place(x=398.5, y=5)
        self.anhomas = ttk.Button(self.cabecera, text=" >> ")
        self.anhomas.place(x=457.5, y=5)
        self.label = ttk.Label(self.cabecera, text=(self.strmesactual, self.añoactual))
        self.label.pack()
        
    def Diassemnana(self):
        self.dias = ttk.Frame(self, width = 532, heigth= 20).place(x=0, y=38)
        self.lunes = ttk.Label(self, text="lunes", font=("Arial", 11)).place(x=0, y=38)
        self.martes = ttk.Label(self, text="martes", font=("Arial", 11)).place(x=76, y=38)
        self.miercoles = ttk.Label(self, text="miercoles", font=("Arial", 11)).place(x=152, y=38)
        self.jueves = ttk.Label(self, text="jueves", font=("Arial", 11)).place(x=228, y=38)
        self.viernes = ttk.Label(self, text="viernes", font=("Arial", 11)).place(x=304, y=38)
        self.sabado = ttk.Label(self, text="sabado", font=("Arial", 11)).place(x=380, y=38)
        self.domingo = ttk.Label(self, text="domingo", font=("Arial", 11)).place(x=456, y=38)

class Mainapp(Tk):
    """__strmes = None
    __mes = None
    __mesmas = None
    meses = tuple(calendar.month_name)
    intmesactual=ahora.month
    añoactual=ahora.year
    strmesactual = meses[ahora.month]
    ahora = datetime.now()"""
    calendar = Calendar()
    calendar.__init__()
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        self.configure(bg = "#DED7B9")
        self.calendar = Calendar(self)
        self.calendar.__init__()

    def start(self):
        self.mainloop()



if __name__ == "__main__":
    app = Mainapp()
    app.start()