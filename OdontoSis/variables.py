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

    def agregar_Interfaz(self,ventana, canvas):
        self.Dientes = [1, 4, 5, 2, 3, 10, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
        self.Dientes.sort()
        self.ventana = ventana
        self.canvas = canvas
        
    def agregarDiente(self,elemento):
        __instance.Dientes.append(elemento)
        __instance.Dientes.sort()

    def eliminarDiente(self,elemento):
        if(var.Dientes.count(n) > 0):
            __instance.Dientes.remove(elemento)    

    def agregarRetenedor(self, elemento):
        aux = clases.componente_odontologico(x,y)
        __instance.Retenedores.append(aux)   

    def agregarApoyo(self, x,y):
        aux = clases.componente_odontologico(x,y)
        __instance.Apoyos.append(aux)
    
    def agregarConec_Menor(self, x,y):
        aux = clases.componente_odontologico(x,y)
        __instance.Conectores_menores.append(aux)

    def agregarConec_Mayor(__instance, x,y):
        aux = clases.componente_odontologico(x,y)
        __instance.Conectores_mayores.append(aux)

    def agregarBase(self, x,y):
        aux = clases.componente_odontologico(x,y)
        __instance.Bases.append(aux)
    