import tkinter as tk
from PIL import Image
from tkinter import ttk
from tkinter import Frame, Button, Label
from variables import VarGlo
from PIL import ImageTk as itk

class Graficador_apoyos:
    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    Apoyos: tk.PhotoImage = []
    frame : Frame
    direccionBase = "./src/apoyos/"

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
            self.x = evento.x
            self.y = evento.y
            apoyoa = tk.PhotoImage()
            if(self.actual == "oclusal_superior"):
                apoyoa = tk.PhotoImage(file="./src/apoyos/apoyo_oclusal_superior.png")
                
            elif(self.actual == "oclusal_inferior"):
                apoyoa = tk.PhotoImage(file="./src/apoyos/apoyo_oclusal_inferior.png")

            elif(self.actual == "incisal"):
                apoyoa = tk.PhotoImage(file="./src/apoyos/apoyo_incisal.png")

            elif(self.actual == "circular"):
                apoyoa = tk.PhotoImage(file="./src/apoyos/apoyo_circular.png")

            self.Apoyos.append(apoyoa) 
 
            self.canvas.create_image(evento.x-10, evento.y-20, image=self.Apoyos[len(self.Apoyos)-1], anchor="nw", tag="baston")


    def left_but_up(self, evento):
        return     