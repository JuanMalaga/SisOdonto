import tkinter as tk
from PIL import Image
from tkinter import ttk
from variables import interfaz
from variables import VarGlo
from tkinter import Frame, Button, Label
from variables import VarGlo
from PIL import ImageTk as itk

class interfaz_fase_3(interfaz):

    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo : tk.PhotoImage
    Retenedores : tk.PhotoImage = []


    def __init__ (self):
        global graficador 
        global var
        var = VarGlo()
        
        graficador = Graficador_retenedores()



    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        graficador.crear_botones()
        
    def limpiar(self):
        graficador.limpiar()
        
class Graficador_retenedores:
    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    Retenedores: tk.PhotoImage = []
    frame: Frame
    direccionBase = "./src/retenedores/"
    
    def __init__(self):
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.actual = "ninguno"
        self.Retenedores = var.Retenedores

    def cambio_fase(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.crear_botones()

    def crear_botones(self):
        self.im1 = Image.open(self.direccionBase+'retenedores.png')
        self.im1 = self.im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.im1 = itk.PhotoImage(self.im1)

        self.im2 = Image.open(self.direccionBase +
                              "Retenedor_Vertica_sup_iz.png")
        self.im2 = self.im2.resize((var.size, var.size), Image.ANTIALIAS)
        self.im2 = itk.PhotoImage(self.im2)

        self.im3 = Image.open(self.direccionBase +
                              "Retenedor_Vertica_sup_der.png")
        self.im3 = self.im3.resize((var.size, var.size), Image.ANTIALIAS)
        self.im3 = itk.PhotoImage(self.im3)

        self.im4 = Image.open(self.direccionBase +
                              "Retenedor_Vertical_inf_izq.png")
        self.im4 = self.im4.resize((var.size, var.size), Image.ANTIALIAS)
        self.im4 = itk.PhotoImage(self.im4)

        self.im5 = Image.open(self.direccionBase +
                              "Retenedor_Vertica_inf_der.png")
        self.im5 = self.im5.resize((var.size, var.size), Image.ANTIALIAS)
        self.im5 = itk.PhotoImage(self.im5)

        self.im6 = Image.open(self.direccionBase +
                              "retenedor_barra_T.png")
        self.im6 = self.im6.resize((var.size, var.size), Image.ANTIALIAS)
        self.im6 = itk.PhotoImage(self.im6)

        self.boton2 = ttk.Button(
            self.frame, image=self.im1, command=self.Escoger_retenedor_circular)
        self.boton2.grid(column=0, row=1, padx=5)
        self.boton3 = ttk.Button(
            self.frame, image=self.im2, command=self.Escoger_retenedor_vertical_sup_iz)
        self.boton3.grid(column=0, row=2, padx=5)
        self.boton4 = ttk.Button(
            self.frame, image=self.im3, command=self.Escoger_retenedor_vertical_sup_der)
        self.boton4.grid(column=0, row=3, padx=5)
        self.boton5 = ttk.Button(
            self.frame, image=self.im4, command=self.Escoger_retenedor_vertical_inf_iz)
        self.boton5.grid(column=0, row=4, padx=5)
        self.boton6 = ttk.Button(
            self.frame, image=self.im5, command=self.Escoger_retenedor_vertical_inf_der)
        self.boton6.grid(column=0, row=5, padx=5)
        self.boton7 = ttk.Button(
            self.frame, image=self.im6, command=self.Escoger_retenedor_barra_t)
        self.boton7.grid(column=0, row=5, padx=5)
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def borrar_linea(self):
        self.canvas.delete("diente1")

    def Escoger_retenedor_circular(self):
        self.actual = "retenedor_circular"

    def Escoger_retenedor_vertical_sup_iz(self):
        self.actual = "retenedor_Vert_sup_iz"

    def Escoger_retenedor_vertical_sup_der(self):
        self.actual = "retenedor_Vert_sup_der"

    def Escoger_retenedor_vertical_inf_iz(self):
        self.actual = "retenedor_Vert_inf_iz"

    def Escoger_retenedor_vertical_inf_der(self):
        self.actual = "retenedor_Vert_inf_der"

    def Escoger_retenedor_barra_t(self):
        self.actual = "retenedor_barra_T"


    def left_but_down(self, evento):
        if(self.actual != ""):
            self.x = evento.x-40
            self.y = evento.y-35
            Retenedor = tk.PhotoImage()
            opcion = 0
            
            if(self.actual == "retenedor_circular"):
                Retenedor = tk.PhotoImage(
                    file="./src/retenedores/retenedores.png")
                opcion = 1
            elif(self.actual == "retenedor_Vert_sup_iz"):
                Retenedor = tk.PhotoImage(
                    file="./src/retenedores/Retenedor_Vertica_sup_iz.png")
                opcion = 2
            elif(self.actual == "retenedor_Vert_sup_der"):
                Retenedor = tk.PhotoImage(
                    file="./src/retenedores/Retenedor_Vertica_sup_der.png")
                opcion = 3
            elif(self.actual == "retenedor_Vert_inf_iz"):
                Retenedor = tk.PhotoImage(
                    file="./src/retenedores/Retenedor_Vertical_inf_izq.png")
                opcion = 4
            elif(self.actual == "retenedor_Vert_inf_der"):
                Retenedor = tk.PhotoImage(
                    file="./src/retenedores/Retenedor_Vertica_inf_der.png")
                opcion = 5
            elif(self.actual == "retenedor_barra_T"):
                Retenedor = tk.PhotoImage(
                    file="./src/retenedores/retenedor_barra_T.png")
                opcion = 6

            var.grabar(3,self.x,self.y,opcion)
            var.agregarRetenedor(Retenedor)
            self.canvas.create_image(self.x, self.y, image=self.Retenedores[len(
                self.Retenedores)-1], anchor="nw", tag="retenedor")

    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("retenedor")
