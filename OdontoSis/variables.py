import tkinter as tk
import os


class componente_odontologico:

    def __init__(self, fase, x, y, unidad):
        self.pos_x = x
        self.pos_y = y
        self.unidad = unidad
        self.fase = fase


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class VarGlo(metaclass=SingletonMeta):

    Dientes = []
    Apoyos = []
    Retenedores = []
    Conectores_menores = []
    Conectores_mayores = []
    Bases = []
    cambios: componente_odontologico = []
    canvas: tk.Canvas
    frame: tk.Frame
    frame2: tk.Frame
    ventana: tk.Tk
    size = 30

    # actual
    actual = ""
    fase_actual = 0

    def Guardar_archivo(self):
        file = open("datos/archivo.txt", "w", encoding="utf-8")
        for i in self.cambios:
            file.write("(")
            file.write(str(i.fase))
            file.write(",")
            file.write(str(i.pos_x))
            file.write(",")
            file.write(str(i.pos_y))
            file.write(",")
            file.write(str(i.unidad))
            file.write(") \n")
        file.close()

    def Iniciar_Dentadura(self):
        self.Dientes = [48, 47, 46, 45, 44, 43, 42, 41, 31, 32, 33, 34, 35, 36, 37, 38]
        
    def Iniciar_Dentadura_Sup(self):
        self.Dientes = [17, 18, 19, 20, 21, 22,
                        23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
        self.Dientes.sort()

    def agregar_Interfaz(self, ventana, canvas, frame, frame2):
        self.ventana = ventana
        self.canvas = canvas
        self.frame = frame
        self.frame2 = frame2

    def agregarDiente(self, elemento):
        self.Dientes.append(elemento)
        self.Dientes.sort()
        self.grabar(1,0,0,elemento)

    def eliminarDiente(self, elemento):
        if(self.Dientes.count(elemento) > 0):
            self.Dientes.remove(elemento)
            self.grabar(1,0,0,-1*elemento)

    #Funciones de retenedores
    def agregarRetenedor(self, elemento):
        self.Retenedores.append(elemento)
        
    def elininarRetenedor(self, elemento):
        self.Retenedores.remove(elemento)

    def borrarRetenedores(self):
        self.Retenedores.clear()

    #Funciones de apoyos
    def agregarApoyo(self, elemento):
        self.Apoyos.append(elemento)

    def elininarApoyo(self, elemento):
        self.Apoyos.remove(elemento)

    def borrarApoyos(self):
        self.Apoyos.clear()

    #Funciones de conector_mayor
    def agregarConec_Menor(self,elemento):
        self.Conectores_menores.append(elemento)

    def agregarConec_Mayor(self,elemento):
        
        self.Conectores_mayores.append(elemento)

    def agregarBase(self,elemento):
        
        self.Bases.append(elemento)

    def grabar(self, fase, X, Y, unidad):
        aux = componente_odontologico(fase, X, Y, unidad)
        self.cambios.append(aux)
        



    

    
