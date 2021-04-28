
from variables import VarGlo, SingletonMeta
from tkinter.font import Font
import tkinter as tk
from interfaz_fase_1 import inter_1
from interfaz_fase_3 import interfaz_fase_3
from interfaz_fase_2 import interfaz_fase_2
from interfaz_fase_4 import interfaz_fase_4
from interfaz_fase_5 import interfaz_fase_5
from interfaz_fase_6 import interfaz_fase_6
import ctypes

resolucion = ctypes.windll.user32 
width = resolucion.GetSystemMetrics(0)
height = resolucion.GetSystemMetrics(1)

class orquestador (metaclass=SingletonMeta):
    def __init__(self):
        self.arreglo = []
        global var
        var = VarGlo()
        global pos_inicial
        pos_inicial = int(width/9)
        altura=int(height/8)
        boton1 = botonFase(pos_inicial, altura, "FASE I\nDIENTES", 0)
        self.arreglo.append(boton1)
        boton2 = botonFase(pos_inicial+int(width/7.8)*1, altura, "FASE II\nAPOYOS", 1)
        self.arreglo.append(boton2)
        boton3 = botonFase(pos_inicial+int(width/7.8)*2, altura, "FASE III\nRETENEDORES", 2)
        self.arreglo.append(boton3)
        boton4 = botonFase(pos_inicial+int(width/7.8)*3, altura, "FASE IV\nCONECTOR MENOR", 3)
        self.arreglo.append(boton4)
        boton5 = botonFase(pos_inicial+int(width/7.8)*4, altura, "FASE V\nCONECTOR MAYOR", 4)
        self.arreglo.append(boton5)
        boton6 = botonFase(pos_inicial+int(width/7.8)*5, altura, "FASE VI\nBASES (REJILLAS)", 5)
        self.arreglo.append(boton6)

    def cambiar(self):

        for n in self.arreglo:
            if (self.arreglo.index(n) < var.fase_actual):
                n.cambiar_estado(0)
            if (self.arreglo.index(n) == var.fase_actual):
                n.cambiar_estado(1)
            if(self.arreglo.index(n) == var.fase_actual+1):
                n.cambiar_estado(2)
            if (self.arreglo.index(n) > var.fase_actual+1):
                n.cambiar_estado(3)


class botonFase ():

    boton: tk.Button
    fase: int
    estado: int

    def __init__(self, x, y, nombre, fase):
        self.interfaz1 = inter_1()
        self.interfaz2 = interfaz_fase_2()
        self.interfaz3 = interfaz_fase_3()
        self.interfaz4 = interfaz_fase_4()
        self.interfaz5 = interfaz_fase_5()
        self.interfaz6 = interfaz_fase_6()

        self.fase = fase
        global orq
        btn_font = Font(family="Roboto Mono", size=10)
        var = VarGlo()
        self.x = x
        self.y = y
        self.nombre = nombre
        self.boton = tk.Button(var.ventana, text=self.nombre, font=btn_font, bd=0, width=int(width/64),
                               overrelief="flat", cursor="hand1", command=self.seleccionar)

        self.boton.place(x=self.x, y=self.y)
        self.boton.bind("<Enter>", self.on_enter_fase)
        self.boton.bind("<Leave>", self.on_leave_fase)

    def on_enter_fase(self, e):
        if (self.boton['state'] == tk.NORMAL and self.estado != 0):
            self.boton["background"] = "#4dffc3"

    def on_leave_fase(self, e):
        if (self.boton['state'] == tk.NORMAL and self.estado != 0 and self.fase != var.fase_actual):
            self.boton["background"] = "#ffffff"

    def apagar(self):
        if (self.boton['state'] == tk.NORMAL):
            self.boton['state'] = tk.DISABLED

    def encender(self):
        if (self.boton['state'] == tk.DISABLED):
            self.boton['state'] = tk.NORMAL

    def seleccionar(self):
        orq = orquestador()
        var.fase_actual = self.fase
        orq.cambiar()
        if(self.fase == 0):
            self.interfaz1.iniciar_interfaz()
            var.Iniciar_Dentadura()
            self.interfaz2.limpiar()
            self.interfaz3.limpiar()
            self.interfaz4.limpiar()
            self.interfaz5.limpiar()
            self.interfaz6.limpiar()
        elif(self.fase == 1):
            self.interfaz2.iniciar_interfaz()
            self.interfaz3.limpiar()
            self.interfaz4.limpiar()
            self.interfaz5.limpiar()
            self.interfaz6.limpiar()

        elif(self.fase == 2):
            self.interfaz3.iniciar_interfaz()
            self.interfaz4.limpiar()
            self.interfaz5.limpiar()
            self.interfaz6.limpiar()

        elif(self.fase == 3):
            self.interfaz4.iniciar_interfaz()
            self.interfaz5.limpiar()
            self.interfaz6.limpiar()

        elif(self.fase == 4):
            self.interfaz5.iniciar_interfaz()
            self.interfaz6.limpiar()

        elif(self.fase == 5):
            self.interfaz6.iniciar_interfaz()

    def cambiar_estado(self, n):
        if(n == 0):
            self.encender()
            self.estado = 0
            self.boton["background"] = "#0c5deb"

        elif(n == 1):
            self.encender()
            self.boton["background"] = "#4dffc3"
            self.estado = 1

        elif(n == 2):
            self.encender()
            self.boton["background"] = "#ffffff"
            self.estado = 2

        elif(n == 3):
            self.apagar()
            self.boton["background"] = "#9ba1ab"
            self.estado = 2
