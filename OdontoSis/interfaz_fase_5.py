import tkinter as tk
from PIL import Image
from tkinter import ttk
from interfaz import interfaz
from variables import VarGlo
from tkinter import Frame, Button, Label
from PIL import ImageTk as itk

class interfaz_fase_5(interfaz):

    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo : tk.PhotoImage
    conectores : tk.PhotoImage = []


    def __init__ (self):
        global graficador 
        global var
        var = VarGlo()
        graficador = Graficador_conectores_mayores()

    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        graficador.crear_botones()
        
    def limpiar(self):
        graficador.limpiar()
        
class Graficador_conectores_mayores:
    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    conectores: tk.PhotoImage = []
    frame: Frame
    direccionBase = "./src/conectores_mayores/inferiores/"

    def __init__(self):
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.actual = "ninguno"
        self.conectores = var.Conectores_mayores
    def cambio_fase(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.crear_botones()

    def crear_botones(self):
        self.im1 = Image.open(self.direccionBase+'barra_lingual_simple.png')
        self.im1 = self.im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.im1 = itk.PhotoImage(self.im1)

        self.im2 = Image.open(self.direccionBase +
                              "doble_barra_lingual.png")
        self.im2 = self.im2.resize((var.size, var.size), Image.ANTIALIAS)
        self.im2 = itk.PhotoImage(self.im2)

        self.im3 = Image.open(self.direccionBase +
                              "placa_lingual.png")
        self.im3 = self.im3.resize((var.size, var.size), Image.ANTIALIAS)
        self.im3 = itk.PhotoImage(self.im3)

        self.boton2 = ttk.Button(
            self.frame, image=self.im1, command=self.Escoger_retenedor_circular)
        self.boton2.grid(column=0, row=1, padx=5)
        self.boton3 = ttk.Button(
            self.frame, image=self.im2, command=self.Escoger_retenedor_vertical_sup_iz)
        self.boton3.grid(column=0, row=2, padx=5)
        self.boton4 = ttk.Button(
            self.frame, image=self.im3, command=self.Escoger_retenedor_vertical_sup_der)
        self.boton4.grid(column=0, row=3, padx=5)

        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def Escoger_retenedor_circular(self):
        self.actual = "barra_lingual_simple"

    def Escoger_retenedor_vertical_sup_iz(self):
        self.actual = "doble_barra_lingual"

    def Escoger_retenedor_vertical_sup_der(self):
        self.actual = "placa_lingual"

    def left_but_down(self, evento):
        if(self.actual != ""):
            self.x = evento.x
            self.y = evento.y
            conector_mayor = tk.PhotoImage()
            opcion = 0
            if(self.actual == "barra_lingual_simple"):
                conector_mayor = tk.PhotoImage(
                    file=self.direccionBase+"barra_lingual_simple.png")
                self.x = 170
                self.y = 134
                opcion = 1

            elif(self.actual == "doble_barra_lingual"):
                conector_mayor = tk.PhotoImage(
                    file=self.direccionBase+"doble_barra_lingual.png")
                self.x = 184
                self.y = 172
                opcion = 2

            elif(self.actual == "placa_lingual"):
                conector_mayor = tk.PhotoImage(
                    file=self.direccionBase+"placa_lingual.png")
                self.x = 248
                self.y = 406
                opcion = 3

            var.agregarConec_Mayor(conector_mayor)
            var.grabar(5,self.x,self.y,opcion)

            self.canvas.create_image(self.x, self.y, image=self.conectores[len(
                self.conectores)-1], anchor="nw", tag="conector_mayor")

    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("conector_mayor")
