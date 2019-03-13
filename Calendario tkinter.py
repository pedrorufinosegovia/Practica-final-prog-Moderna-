from tkinter import *
from tkinter import ttk
import datetime
from datetime import date, datetime 
import calendar

class Calendario(ttk.Frame):
    __meses = ("", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre","Octubre","Noviembre","Diciembre")
    __dias = []
    __calen = calendar.Calendar()
    def __init__(self, parent):
        #Creamos las funciones y las iniciamos
        ttk.Frame.__init__(self, parent, width=532, height=422)
        self.Botones()
        self.Fechar()
        self.Diassemana()
        self.Crearcuadrodias()
        self.DarValorDias()
        #creamos los dias
        for m in range(6):
            for n in range(7):
                d = self.__dias[n + m * 7]
                d.place(x=n*76, y=m*61+55)
                
                
    def Validarmes(self, nuevafecha, valor):
        #cambiamos la fecha vieja por la nueva
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
                nuevoaño -=1
        if valor == -12:
            nuevoaño -= 1
            if nuevoaño == 0:
                nuevoaño = 9999
        return date(nuevoaño, nuevomes, 1)
        DarValorDias
                    
                    
    def Botones(self):
        # Creamos los botones para aumnetar o disminuir los meses
        # he cambiado algunos parametros para que todo cuadre mejor
        self.__cabecera = ttk.Frame(self, width=532, height=40).place(x=0,y=0)
        self.__Añomenos = ttk.Button(self.__cabecera,width=5, text="<<", command=lambda: self.NuevaFecha(-12))
        self.__Añomenos.place(x=15, y=5)
        self.__Mesmenos = ttk.Button(self.__cabecera,width=5, text="<", command=lambda: self.NuevaFecha(-1))
        self.__Mesmenos.place(x=70, y=5)
        self.__Mesmas = ttk.Button(self.__cabecera,width=5, text=">", command=lambda: self.NuevaFecha(1))
        self.__Mesmas.place(x=400, y=5)
        self.__Añomas = ttk.Button(self.__cabecera, width=5, text=">>", command=lambda: self.NuevaFecha(12))
        self.__Añomas.place(x=457.5, y=5)
        self.__MesyAño__ = ttk.Label(self.__cabecera, text="", font=('Arial', 20, 'bold'))
        self.__MesyAño__.place(x=140, y=0)
    def Diassemana(self):
        # Creamos los dias de la semana
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
        self.__viernes.place(x=314, y=38)
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
        self.DarValorDias()
        
    def NuevaFecha(self, valor):
        #Se activa al pulsar el boton
        nuevafecha = self.Validarmes(self.__fecha, valor)
        #Con la fecha conseguida la sustituimos por la anterior
        self.Fechar(nuevafecha.month, nuevafecha.year)
        
    def Crearcuadrodias(self):
        for m in range(42):
            cuadro = Dates(self)
            if (m+1) % 7 == 0 or (m+2) % 7 == 0:
                cuadro.weekend(True)
            self.__dias.append(cuadro)
    
    def DarValorDias(self):
        if len(self.__dias) > 0:
            estanmes = self.__calen.itermonthdates(self.__fecha.year, self.__fecha.month)
            for dia, año in enumerate(estanmes):
                self.__dias[dia].Ponervalor(año)
                self.__dias[dia].Noesdeestemes(año.month == self.__fecha.month)
                maximo = año

            if dia < 41:
                masmes = self.Validarmes(self.__fecha, 1)
                noestanmes = self.__calen.itermonthdates(masmes.year, masmes.month)
                for item in noestanmes:
                    if item > maximo:
                        dia += 1
                        self.__dias[dia].Ponervalor(item)
                        self.__dias[dia].Noesdeestemes(item.month == self.__fecha.month)
                        if dia >= 41:
                            break
            
            
class Dates(ttk.Frame):
    __finde = False
    __pertenecemes = True
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=76, height=61, borderwidth=0.8, relief='ridge' )
        self.__numero = ttk.Label(self, text="", anchor=E ,font=("Arial", 28),width = 2)
        self.__numero.place(x=20, y=10)
        
    def weekend(self, valor=None):
        if valor:
            self.__finde = True
            if self.__pertenecemes:
                self.__numero.config(foreground="#FF6157")
        else:
            self.__finde = False
            self.Noesdeestemes(self.__pertenecemes)        
    
    def Noesdeestemes(self, value=None):
        if value:
            self.__pertenecemes = True
            if self.__finde:
                self.__numero.config(foreground="#FF6157")
            else:
                self.__numero.config(foreground="#000000")
        else:
            self.__pertenecemes = False
            self.__numero.config(foreground = "#C2C2C2")
            
        
    def Ponervalor(self, valor=None):
        #ponemos el dia en su sitio
        self.__fecha2 = valor
        self.__numero.config(text=(self.__fecha2.day))
        self.Noesdeestemes(self.__pertenecemes)
        self.weekend(self.__finde)
      
class Mainapp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        self.configure(bg = "#DED7B9")
        self.calendar = Calendario(self)
        self.calendar.place(x=0,y=0)

    def start(self):
        self.mainloop()
        
        
if __name__ == "__main__":
    app = Mainapp()
    app.start()