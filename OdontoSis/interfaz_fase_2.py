import tkinter as tk
from PIL import Image
from tkinter import ttk
from interfaz import interfaz 
from variables import VarGlo
from tkinter import Frame, Button, Label
from PIL import ImageTk as itk


class interfaz_fase_2(interfaz):

    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    frame : Frame
    direccionBase = "./src/apoyos/"

    def __init__ (self):
        global graficador 
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.actual = "ninguno"
        self.Apoyos = var.Apoyos
           
    
    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        self.crear_botones()
        
    def crear_botones(self):
        self.im1 = Image.open(self.direccionBase+'apoyo_oclusal_superior.png')
        self.im1 = self.im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.im1 = itk.PhotoImage(self.im1)

        self.im2 = Image.open(self.direccionBase+'apoyo_oclusal_inferior.png')
        self.im2 = self.im2.resize((var.size, var.size), Image.ANTIALIAS)
        self.im2 = itk.PhotoImage(self.im2)

        self.im3 = Image.open(self.direccionBase+'apoyo_incisal.png')
        self.im3 = self.im3.resize((var.size, var.size), Image.ANTIALIAS)
        self.im3 = itk.PhotoImage(self.im3)

        self.im4 = Image.open(self.direccionBase+'apoyo_circular.png')
        self.im4 = self.im4.resize((var.size, var.size), Image.ANTIALIAS)
        self.im4 = itk.PhotoImage(self.im4)

        self.boton1 = ttk.Button(
            self.frame, image = self.im1, command=self.Escoger_apoyo_oclusal_superior)
        self.boton1.grid(column=0, row=1, padx=5)

        self.boton2 = ttk.Button(
            self.frame, image = self.im2, text="1", command=self.Escoger_apoyo_oclusal_inferior)
        self.boton2.grid(column=1, row=1, padx=5)

        self.boton3 = ttk.Button(
            self.frame, image = self.im3, text="2", command=self.Escoger_apoyo_incisal)
        self.boton3.grid(column=0, row=2, padx=5)

        self.boton4 = ttk.Button(
            self.frame, image = self.im4, text="1", command=self.Escoger_apoyo_circular)
        self.boton4.grid(column=1, row=2, padx=5)

        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)
        
            

    def borrar_linea(self):
        self.canvas.delete("diente1")

    def Escoger_apoyo_oclusal_superior(self):
        self.actual="oclusal_superior"

    def Escoger_apoyo_oclusal_inferior(self):
        self.actual="oclusal_inferior"

    def Escoger_apoyo_incisal(self):
        self.actual="incisal"

    def Escoger_apoyo_circular(self):
        self.actual="circular"    
    
    def left_but_down(self, evento):

        if(self.actual!=""):    
            self.x = evento.x-10
            self.y = evento.y-20
            apoyoa = tk.PhotoImage()
            opcion = 0
            if(self.actual == "oclusal_superior"):
                apoyoa = tk.PhotoImage(file="./src/apoyos/apoyo_oclusal_superior.png")
                opcion = 1
            elif(self.actual == "oclusal_inferior"):
                apoyoa = tk.PhotoImage(file="./src/apoyos/apoyo_oclusal_inferior.png")
                opcion = 2
            elif(self.actual == "incisal"):
                apoyoa = tk.PhotoImage(file="./src/apoyos/apoyo_incisal.png")
                opcion = 3
            elif(self.actual == "circular"):
                apoyoa = tk.PhotoImage(file="./src/apoyos/apoyo_circular.png")
                opcion = 4
            
            var.agregarApoyo(apoyoa)
            var.grabar(2,self.x,self.y,opcion)
            self.canvas.create_image(self.x, self.y, image=self.Apoyos[len(self.Apoyos)-1], anchor="nw", tag="apoyo")

    
    def left_but_up(self, evento):
        self.obtener_diente()