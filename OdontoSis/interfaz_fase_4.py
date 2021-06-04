import tkinter as tk
from PIL import Image
from tkinter import ttk
from interfaz import interfaz
from variables import VarGlo
from tkinter import Frame, Button, Label
from PIL import ImageTk as itk

class interfaz_fase_4(interfaz):

    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo : tk.PhotoImage
    conectores : tk.PhotoImage = []
    direccionBase = "./src/conectores_menores/"

    def __init__ (self):
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.actual = "ninguno"
        self.conectores = var.Conectores_menores

    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        self.crear_botones()
        
    def limpiar(self):
        self.limpiar()
    

    def cambio_fase(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.crear_botones()

    def crear_botones(self):
        self.im1 = Image.open(self.direccionBase+'inferior_posterior.png')
        self.im1 = self.im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.im1 = itk.PhotoImage(self.im1)

        self.im2 = Image.open(self.direccionBase +
                              "superior_anterior.png")
        self.im2 = self.im2.resize((var.size, var.size), Image.ANTIALIAS)
        self.im2 = itk.PhotoImage(self.im2)

        self.im3 = Image.open(self.direccionBase +
                              "superior_posterior.png")
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
        self.actual = "inferior_posterior"

    def Escoger_retenedor_vertical_sup_iz(self):
        self.actual = "superior_anterior"

    def Escoger_retenedor_vertical_sup_der(self):
        self.actual = "superior_posterior"

    def left_but_down(self, evento):
        if(self.actual != ""):
            self. permitido = False
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            opcion = 0
            if(self.actual == "inferior_posterior"):
                Retenedor = Image.open(self.direccionBase+"48.png")
                opcion = 1

            elif(self.actual == "superior_anterior"):
                Retenedor = tk.PhotoImage(
                    file=self.direccionBase+"superior_anterior.png")
                opcion = 2

            elif(self.actual == "superior_posterior"):
                Retenedor = tk.PhotoImage(
                    file=self.direccionBase+"superior_posterior.png")
                opcion = 3

            if (tupla[0] == 48 and self.existe_diente(48)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,150,161)

            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)

            elif (tupla[0] == 46 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 45 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 44 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 43 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 42 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 41 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 38 and self.existe_diente(48)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)

            elif (tupla[0] == 37 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)

            elif (tupla[0] == 36 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 35 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 34 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 33 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 32 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
            elif (tupla[0] == 31 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,140,161)
                    
            var.agregarConec_Menor(self.tkimage)
            ultimo_elemento = len(self.conectores)-1
            if(self.permitido):
                self.canvas.create_image(self.x, self.y, image=self.conectores[ultimo_elemento], anchor="nw", tag="conector")
                var.grabar(3,self.x,self.y,opcion)    

    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("conector")
