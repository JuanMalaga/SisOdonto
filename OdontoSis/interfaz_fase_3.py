import tkinter as tk
from PIL import Image
from tkinter import ttk
from interfaz import interfaz
from variables import VarGlo
from tkinter import Frame, Button, Label
from variables import VarGlo
from PIL import ImageTk as itk

class interfaz_fase_3(interfaz):

    x = 0
    y = 0
    fondo : tk.PhotoImage
    Retenedores : tk.PhotoImage = []
    ventana: tk.Tk
    canvas: tk.Canvas
    frame: Frame
    direccionBase = "./src/retenedores/"

    def __init__ (self):
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.actual = "ninguno"
        self.Retenedores = var.Retenedores

    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        self.crear_botones()
        self.actual = "ninguno"
        
    def limpiar(self):
        graficador.limpiar()
        
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

    def Escoger_retenedor_barra_t(self):
        self.actual = "retenedor_barra_T"


    def left_but_down(self, evento):
        opcion = 0
        permitido = False
        print(evento.x)
        print(evento.y)
        print(self.actual)
        if(self.actual != "ninguno"):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            if(self.actual == "retenedor_circular"):
                Retenedor = Image.open("./src/retenedores/retenedores_izquierdo.png")
                RetenedorD = Image.open("./src/retenedores/retenedores_derecho.png")
                opcion = 1
            elif(self.actual == "retenedor_Vert_sup_iz"):
                Retenedor = Image.open("./src/retenedores/Retenedor_Vertica_sup_iz.png")
                opcion = 2
            elif(self.actual == "retenedor_barra_T"):
                Retenedor = Image.open("./src/retenedores/retenedor_barra_T.png")
                opcion = 3

            self.tkimage = itk.PhotoImage(Retenedor)
            
            if(opcion == 1):
                print("entro")

            if (tupla[0] == 48 and self.existe_diente(48)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((160, 120), Image.ANTIALIAS)
                    RetenedorD = RetenedorD.resize((150, 125), Image.ANTIALIAS)
                    self.tkimage = itk.PhotoImage(self.get_concat_h_cut_center(Retenedor,RetenedorD))
                    self.x = 65
                    self.y = 37
                    
            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((160, 120), Image.ANTIALIAS)
                    RetenedorD = RetenedorD.resize((160, 120), Image.ANTIALIAS)
                    self.tkimage = itk.PhotoImage(self.get_concat_h_cut_center(Retenedor,RetenedorD))
                    self.x = 60
                    self.y = 135   

            elif (tupla[0] == 46 and self.existe_diente(46)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((165, 130), Image.ANTIALIAS)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 65
                    self.y = 245

            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((140, 95), Image.ANTIALIAS)
                    self.tkimage = itk.PhotoImage(Retenedor.rotate(30))
                    self.x = 105
                    self.y = 355

            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((120, 80), Image.ANTIALIAS)
                    self.tkimage = itk.PhotoImage(Retenedor.rotate(30))
                    self.x = 142
                    self.y = 435

                if(opcion == 2):
                    permitido = True
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 110
                    self.y = 410
                
                if(opcion == 3):
                    permitido = True
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 110
                    self.y = 410
                    

            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(opcion == 2):
                    permitido = True
                    Retenedor = Retenedor.rotate(25, Image.NEAREST)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 155
                    self.y = 475
                
                if(opcion == 3):
                    permitido = True
                    Retenedor = Retenedor.rotate(25, Image.NEAREST)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 155
                    self.y = 475

            if (tupla[0] == 38 and self.existe_diente(38)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((160, 120), Image.ANTIALIAS)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    
                    self.x = 575
                    self.y = 32

            if (tupla[0] == 37 and self.existe_diente(37)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((160, 120), Image.ANTIALIAS)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 578
                    self.y = 132

            if (tupla[0] == 36 and self.existe_diente(36)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((165, 130), Image.ANTIALIAS)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 563
                    self.y = 235 

            if (tupla[0] == 35 and self.existe_diente(35)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((140, 95), Image.ANTIALIAS)
                    Retenedor = Retenedor.rotate(30)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 540
                    self.y = 342

            if (tupla[0] == 34 and self.existe_diente(34)):
                if(opcion == 1):
                    permitido = True
                    Retenedor = Retenedor.resize((120, 80), Image.ANTIALIAS)
                    Retenedor = Retenedor.rotate(30)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 525
                    self.y = 420

                if(opcion == 2):
                    permitido = True
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 575
                    self.y = 395
                
                if(opcion == 3):
                    permitido = True
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 575
                    self.y = 395

            if (tupla[0] == 33 and self.existe_diente(33)):
                if(opcion == 2):
                    permitido = True
                    Retenedor = Retenedor.rotate(25, Image.NEAREST)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 530
                    self.y = 460
                
                if(opcion == 3):
                    permitido = True
                    Retenedor = Retenedor.rotate(25, Image.NEAREST)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 530
                    self.y = 460

            var.agregarRetenedor(self.tkimage)
            ultimo_elemento = len(self.Retenedores)-1
            if(permitido):
                self.canvas.create_image(self.x, self.y, image=self.Retenedores[ultimo_elemento], anchor="nw", tag="retenedor")
                var.grabar(3,self.x,self.y,opcion)
                
    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("retenedor")
