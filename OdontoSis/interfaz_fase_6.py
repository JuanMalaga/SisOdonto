import tkinter as tk
from PIL import Image
from tkinter import ttk
from tkinter.font import Font
from interfaz import interfaz
from variables import VarGlo
from tkinter import Frame, Button, Label
from PIL import ImageTk as itk
import ctypes

resolucion = ctypes.windll.user32 
width = resolucion.GetSystemMetrics(0)
height = resolucion.GetSystemMetrics(1)

class interfaz_fase_6(interfaz):

    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo : tk.PhotoImage
    bases : tk.PhotoImage = []


    def __init__ (self):
        global graficador 
        global var
        var = VarGlo()
        graficador = Graficador_bases()

    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        graficador.crear_botones()
        
    def limpiar(self):
        graficador.limpiar()

class Graficador_bases:
    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    conectores: tk.PhotoImage = []
    frame: Frame
    direccionBase = "./src/bases/"

    def __init__(self):
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.actual = "ninguno"
        self.conectores = var.Bases
    def cambio_fase(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.crear_botones()

    def crear_botones(self):
        self.im1 = Image.open(self.direccionBase+'base_doble.png')
        self.im1 = self.im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.im1 = itk.PhotoImage(self.im1)

        self.im2 = Image.open(self.direccionBase +
                              "base_triple.png")
        self.im2 = self.im2.resize((var.size, var.size), Image.ANTIALIAS)
        self.im2 = itk.PhotoImage(self.im2)

        self.boton2 = ttk.Button(
            self.frame, image=self.im1, command=lambda:[self.base(), self.Escoger_retenedor_circular()])
        self.boton2.grid(column=0, row=1, padx=5)
        self.boton3 = ttk.Button(
            self.frame, image=self.im2, command=lambda:[self.base(), self.Escoger_retenedor_vertical_sup_iz()])
        self.boton3.grid(column=0, row=2, padx=5)

        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def base(self):
        self.ancho=int(width/4)
        self.largo=int(3*height/4)
        self.img = Image.open('./src/imagenes/bases.png')
        self.img = self.img.resize((self.ancho, int(7*self.largo/32)), Image.ANTIALIAS)
        self.img = itk.PhotoImage(self.img) 
        self.label = ttk.Label(self.frame, image = self.img).place(x=-2,y=int(5*self.largo/8))
        self.tamaño=Font(family="Bahnschrift", size = int(width/100))
        self.opcion=Font(family="Roboto Mono", size = int(width/196))
        self.titulo = ttk.Label(self.frame, font=self.tamaño, width=self.ancho, text="Rejillas para bases acrílicas").place(x=5*self.ancho/32,y=55*self.largo/64)
        self.descripcion = ttk.Label(self.frame, font=self.opcion, wraplength= int(61*self.ancho/64), width=self.ancho, justify="center",
        text="Son rejillas que se colocan en los espacios donde faltan los dientes naturales, y en donde se colocarán los dientes artificiales. Color AZUL.").place(x=self.ancho/32,y=58*self.largo/64) 

    def Escoger_retenedor_circular(self):
        self.actual = "base_doble"

    def Escoger_retenedor_vertical_sup_iz(self):
        self.actual = "base_triple"



    def left_but_down(self, evento):
        if(self.actual != ""):
            self.x = evento.x
            self.y = evento.y
            Retenedor = tk.PhotoImage()
            if(self.actual == "base_doble"):
                Retenedor = tk.PhotoImage(
                    file=self.direccionBase+"base_doble.png")

            elif(self.actual == "base_triple"):
                Retenedor = tk.PhotoImage(
                    file=self.direccionBase+"base_triple.png")

            
            self.conectores.append(Retenedor)
            self.canvas.create_image(evento.x-40, evento.y-35, image=self.conectores[len(
                self.conectores)-1], anchor="nw", tag="base")

    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("base")        