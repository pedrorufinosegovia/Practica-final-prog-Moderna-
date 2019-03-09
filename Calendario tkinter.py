from tkinter import *
from tkinter import ttk
import datetime
from datetime import date, datetime 
import calendar

    
class Calendar(ttk.Frame):
    mes = None
    año = None
    meses = ("", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre","Octubre","Noviembre","Diciembre")
    
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, width=532, height=422)
        self.Validarmes()
        self.Botones()
        self.Diassemana()
        self.dates = Dates(self)
        self.dates.__init__(self)
        
    def Validarmes(self, valor=None):
        ahora= datetime.now()
        if valor == None:
            self.año= ahora.year
            self.mes = 1
            return
        else:
            if valor == 1:
                self.mes += 1
            if valor == 12:
                self.año += 1
            if valor == -1:
                self.mes = -1
                if self.mes == 0:
                    self.mes = 12
            if valor == -12:
                self.año -= 1
                if self.año == 1899:
                    self.año = 2099
        
    def Botones(self):
        # he cambiado algunos parametros para que todo cuadre mejor
        self.cabecera = ttk.Frame(self, width=532, height=40).place(x=0,y=0)
        self.anhomenos = ttk.Button(self.cabecera,width=5, text="<<", command=lambda: self.Validarmes(-12))
        self.anhomenos.place(x=15, y=5)
        self.mesmenos = ttk.Button(self.cabecera,width=5, text="<", command=lambda: self.Validarmes(-1))
        self.mesmenos.place(x=70, y=5)
        self.mesmas = ttk.Button(self.cabecera,width=5, text=">", command=lambda: self.Validarmes(1))
        self.mesmas.place(x=400, y=5)
        self.anhomas = ttk.Button(self.cabecera, width=5, text=">>", command=lambda: self.Validarmes(12))
        self.anhomas.place(x=457.5, y=5)
        self.label = ttk.Label(self.cabecera, text=(self.meses[self.mes], self.año),font=("Arial", 20, "bold")).place(x=130, y=0)
        
    def Diassemana(self):
        # he cambiado algunos parametros para que todo cuadre mejor
        self.diasSe = ttk.Frame(self, width = 532, height= 20).place(x=0, y=38)
        self.lunes = ttk.Label(self.diasSe, text="lunes",width=76, font=("Arial", 11))
        self.lunes.place(x=0, y=38)
        self.martes = ttk.Label(self.diasSe, text="martes",width=76, font=("Arial", 11))
        self.martes.place(x=76, y=38)
        self.miercoles = ttk.Label(self.diasSe, text="miercoles",width=76, font=("Arial", 11))
        self.miercoles.place(x=152, y=38)
        self.jueves = ttk.Label(self.diasSe, text="jueves",width=76, font=("Arial", 11))
        self.jueves.place(x=238, y=38)
        self.viernes = ttk.Label(self.diasSe, text="viernes",width=76, font=("Arial", 11))
        self.viernes.place(x=304, y=38)
        self.sabado = ttk.Label(self.diasSe, text="sabado",width=76, font=("Arial", 11))
        self.sabado.place(x=380, y=38)
        self.domingo = ttk.Label(self.diasSe, text="domingo",width=76 ,font=("Arial", 11))
        self.domingo.place(x=456, y=38)

        
class Dates(ttk.Frame):
    mes= None
    dias= None
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, width=532, height =366)
    

class Mainapp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        self.configure(bg = "#DED7B9")
        self.calendar = Calendar(self)
        self.calendar.__init__(self)

    def start(self):
        self.mainloop()



if __name__ == "__main__":
    app = Mainapp()
    app.start()