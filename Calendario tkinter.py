from tkinter import *
from tkinter import ttk
import datetime
from datetime import date, datetime 
import calendar

    
class Calendar(ttk.Frame):
    __fecha = None
    __año = None
    __meses = ("", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre","Octubre","Noviembre","Diciembre")
    
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, width=532, height=422)
        self.Botones()
        self.Fechar()
        self.Diassemana()
    def Validarmes(self, nuevafecha, valor):
        nuevomes = nuevafecha.month
        nuevoaño = nuevafecha.year
        if valor == 1:
            nuevomes += 1
            if nuevomes == 13:
                nuevomes = 1
                nuevoaño += 1
        if valor == 12:
            nuevoaño += 1
        if valor == -1:
            nuevomes -= 1
            if nuevomes == 0:
                nuevomes = 12
        if valor == -12:
            nuevoaño -= 1
            if nuevoaño == 0:
                nuevoaño = 9999
        return date(nuevoaño, nuevomes, 1)
                    
                    
    def Botones(self):
        # he cambiado algunos parametros para que todo cuadre mejor
        self.__cabecera = ttk.Frame(self, width=532, height=40).place(x=0,y=0)
        self.__anhomenos = ttk.Button(self.__cabecera,width=5, text="<<", command=lambda: self.NuevaFecha(-12))
        self.__anhomenos.place(x=15, y=5)
        self.__mesmenos = ttk.Button(self.__cabecera,width=5, text="<", command=lambda: self.NuevaFecha(-1))
        self.__mesmenos.place(x=70, y=5)
        self.__MesyAño__ = ttk.Label(self.__cabecera, text="", font=('Arial', 20, 'bold'))
        self.__MesyAño__.place(x=140, y=0)
        self.__mesmas = ttk.Button(self.__cabecera,width=5, text=">", command=lambda: self.NuevaFecha(1))
        self.__mesmas.place(x=400, y=5)
        self.__anhomas = ttk.Button(self.__cabecera, width=5, text=">>", command=lambda: self.NuevaFecha(12))
        self.__anhomas.place(x=457.5, y=5)
        self.__label = ttk.Label(self.__cabecera, text=" ",font=("Arial", 20, "bold")).place(x=130, y=0)
        
    def Diassemana(self):
        # he cambiado algunos parametros para que todo cuadre mejor
        self.diasSe = ttk.Frame(self, width = 532, height= 20).place(x=0, y=38)
        self.__lunes = ttk.Label(self.diasSe, text="lunes",width=76, font=("Arial", 11))
        self.__lunes.place(x=15, y=38)
        self.__martes = ttk.Label(self.diasSe, text="martes",width=76, font=("Arial", 11))
        self.__martes.place(x=76, y=38)
        self.__miercoles = ttk.Label(self.diasSe, text="miercoles",width=76, font=("Arial", 11))
        self.__miercoles.place(x=152, y=38)
        self.__jueves = ttk.Label(self.diasSe, text="jueves",width=76, font=("Arial", 11))
        self.__jueves.place(x=238, y=38)
        self.__viernes = ttk.Label(self.diasSe, text="viernes",width=76, font=("Arial", 11))
        self.__viernes.place(x=304, y=38)
        self.__sabado = ttk.Label(self.diasSe, text="sabado",width=76, font=("Arial", 11))
        self.__sabado.place(x=380, y=38)
        self.__domingo = ttk.Label(self.diasSe, text="domingo",width=76 ,font=("Arial", 11))
        self.__domingo.place(x=456, y=38)
    def Fechar(self, mes=None, año=None):
        #Establecemos una fecha nueva si no hay ninguna
        if año == None:
            self.__fecha = date.today()
        #Solo se activara cuando pulsemos los botones
        else:
            self.__fecha = date(año, mes, 1)
        self.__MesyAño__.config(text=(self.__meses[self.__fecha.month], self.__fecha.year))
    
    def NuevaFecha(self, valor):
        nuevafecha = self.Validarmes(self.__fecha, valor)
        self.Fechar(nuevafecha.month, nuevafecha.year)
        
    def Cuadrosdias(self):
        for m in range[5]:
            for n in range[6]:
                pass
                
        
        
"""class Dates(ttk.Frame):
    __mes= None
    __dias= None
    __gris = False
    __rojo = False
    def __init__(self, parent, **args):
        self.width = 76
        self.heigth = 61"""
        
        
class Mainapp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        self.configure(bg = "#DED7B9")
        self.calendar = Calendar(self)
        self.calendar.place(x=0,y=0)

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Mainapp()
    app.start()