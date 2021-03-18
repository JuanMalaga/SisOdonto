import tkinter as tk
from PIL import Image
from tkinter import ttk
from tkinter import Frame, Button, Label
from variables import VarGlo
from PIL import ImageTk as itk


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
            self.frame, image=self.im1, command=self.Escoger_retenedor_circular)
        self.boton2.grid(column=0, row=1, padx=5)
        self.boton3 = ttk.Button(
            self.frame, image=self.im2, command=self.Escoger_retenedor_vertical_sup_iz)
        self.boton3.grid(column=0, row=2, padx=5)
        

        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

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