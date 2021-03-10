import tkinter as tk
from PIL import Image
from tkinter import ttk
from tkinter import Frame, Button, Label
from variables import VarGlo

class Graficador_retenedores:
    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    Retenedores: tk.PhotoImage = []
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
            self.frame, text="1", command=self.Escoger_retenedor_circular)
        self.boton2.grid(column=0, row=1, padx=5)
        self.boton3 = ttk.Button(
            self.frame, text="2", command=self.Escoger_retenedor_vertical_sup_iz)
        self.boton3.grid(column=0, row=2, padx=5)
        self.boton4 = ttk.Button(
            self.frame, text="3", command=self.Escoger_retenedor_vertical_sup_der)
        self.boton4.grid(column=0, row=3, padx=5)
        self.boton5 = ttk.Button(
            self.frame, text="4", command=self.Escoger_retenedor_vertical_inf_iz)
        self.boton5.grid(column=0, row=4, padx=5)
        self.boton6 = ttk.Button(
            self.frame, text="5", command=self.Escoger_retenedor_vertical_inf_der)
        self.boton6.grid(column=0, row=5, padx=5)
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def borrar_linea(self):
        self.canvas.delete("diente1")

    def Escoger_retenedor_circular(self):
        self.actual="retenedor_circular"

    def Escoger_retenedor_vertical_sup_iz(self):
        self.actual="retenedor_Vert_sup_iz"

    def Escoger_retenedor_vertical_sup_der(self):
        self.actual="retenedor_Vert_sup_der"

    def Escoger_retenedor_vertical_inf_iz(self):
        self.actual="retenedor_Vert_inf_iz"

    def Escoger_retenedor_vertical_inf_der(self):
        self.actual="retenedor_Vert_inf_der"            

    def left_but_down(self, evento):
        if(self.actual!=""):    
            self.x = evento.x
            self.y = evento.y
            Retenedor = tk.PhotoImage()
            if(self.actual == "retenedor_circular"):
                Retenedor = tk.PhotoImage(file="./src/retenedores.png")
                
            elif(self.actual == "retenedor_Vert_sup_iz"):
                Retenedor = tk.PhotoImage(file="./src/Retenedor_Vertica_sup_iz.png")
                
            elif(self.actual == "retenedor_Vert_sup_der"):
                Retenedor = tk.PhotoImage(file="./src/Retenedor_Vertica_sup_der.png")
                
            elif(self.actual == "retenedor_Vert_inf_iz"):
                Retenedor = tk.PhotoImage(file="./src/Retenedor_Vertical_inf_izq.png")

            elif(self.actual == "retenedor_Vert_inf_der"):
                Retenedor = tk.PhotoImage(file="./src/Retenedor_Vertica_inf_der.png")
                        
            self.Retenedores.append(Retenedor) 
            self.canvas.create_image(evento.x-40, evento.y-35, image=self.Retenedores[len(self.Retenedores)-1], anchor="nw", tag="retenedor")


    def left_but_up(self, evento):
        return     

    def limpiar(self):
        self.canvas.delete("retenedor")