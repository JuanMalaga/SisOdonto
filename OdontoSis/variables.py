import clases
import tkinter as tk

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class VarGlo(metaclass=SingletonMeta):

    Dientes = []
    Apoyos : clases.componente_odontologico = []
    Retenedores : clases.componente_odontologico = []
    Conectores_menores : clases.componente_odontologico = []
    Conectores_mayores : clases.componente_odontologico = []
    Bases : clases.componente_odontologico = []
    canvas : tk.Canvas
    frame : tk.Frame
    frame2 : tk.Frame
    ventana : tk.Tk
    
    #actual
    actual = ""
    fase_actual = 0

    def Iniciar_Dentadura(self):
        self.Dientes = [1, 4, 5, 2, 3, 10, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
        self.Dientes.sort()

    def Iniciar_Dentadura_Sup(self):
        self.Dientes = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
        self.Dientes.sort()

    def agregar_Interfaz(self,ventana, canvas,frame, frame2):
        self.ventana = ventana
        self.canvas = canvas
        self.frame = frame
        self.frame2 = frame2
        
    def agregarDiente(self,elemento):
        self.Dientes.append(elemento)
        self.Dientes.sort()

    def eliminarDiente(self,elemento):
        if(self.Dientes.count(elemento) > 0):
            self.Dientes.remove(elemento)    

    def agregarRetenedor(self, elemento):
        aux = clases.componente_odontologico(x,y)
        self.Retenedores.append(aux)   

    def agregarApoyo(self, x,y):
        aux = clases.componente_odontologico(x,y)
        self.Apoyos.append(aux)
    
    def agregarConec_Menor(self, x,y):
        aux = clases.componente_odontologico(x,y)
        self.Conectores_menores.append(aux)

    def agregarConec_Mayor(__instance, x,y):
        aux = clases.componente_odontologico(x,y)
        self.Conectores_mayores.append(aux)

    def agregarBase(self, x,y):
        aux = clases.componente_odontologico(x,y)
        self.Bases.append(aux)
    