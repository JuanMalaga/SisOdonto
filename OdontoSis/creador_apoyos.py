import tkinter as tk
from PIL import Image
from tkinter import ttk
from tkinter import Frame, Button, Label
from variables import VarGlo

class Graficador_apoyos:
    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    Apoyos: tk.PhotoImage = []
    frame : Frame

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
        self.boton2 = ttk.Button(
            self.frame, text="1", command=self.Escoger_apoyo_circular_superior)
        self.boton2.grid(column=0, row=1, padx=5)
        self.boton3 = ttk.Button(
            self.frame, text="2", command=self.Escoger_apoyo_circular_inferior)
        self.boton3.grid(column=0, row=2, padx=5)
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)
        
            

    def borrar_linea(self):
        self.canvas.delete("diente1")

    def Escoger_apoyo_circular_superior(self):
        self.actual="circular_superior"

    def Escoger_apoyo_circular_inferior(self):
        self.actual="circular_inferior"

    
    def left_but_down(self, evento):

        if(self.actual!=""):    
            self.x = evento.x
            self.y = evento.y
            apoyoa = tk.PhotoImage()
            if(self.actual == "circular_superior"):
                apoyoa = tk.PhotoImage(file="./src/apoyo_circular_superior.png")
                
            elif(self.actual == "circular_inferior"):
                apoyoa = tk.PhotoImage(file="./src/apoyo_circular_inferior.png")
                
            self.Apoyos.append(apoyoa) 
 
            self.canvas.create_image(evento.x-40, evento.y-35, image=self.Apoyos[len(self.Apoyos)-1], anchor="nw", tag="baston")


    def left_but_up(self, evento):
        return     