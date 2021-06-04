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
    ventana: tk.Tk
    canvas: tk.Canvas
    frame: Frame
    direccionBase = "./src/bases/"

    def __init__ (self):
        global graficador 
        global var
        global opcion
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.actual = "ninguno"
        opcion = 0
        self.Bases = var.Bases

    def iniciar_interfaz(self):
        self.Bases = var.Bases
        self.cambiar_interfaz()
        self.crear_botones()

    def crear_botones(self):

        self.im1 = Image.open(self.direccionBase + 'base_doble.png')
        self.im1 = self.im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.im1 = itk.PhotoImage(self.im1)

        self.im2 = Image.open(self.direccionBase + 'base_triple.png')
        self.im2 = self.im2.resize((var.size, var.size), Image.ANTIALIAS)
        self.im2 = itk.PhotoImage(self.im2)

        self.boton2 = ttk.Button(
            self.frame, image=self.im1, command=lambda:[self.base(), self.Escoger_base_circular()])
        self.boton2.grid(column=0, row=1, padx=5)

        self.boton3 = ttk.Button(
            self.frame, image=self.im2, command=lambda:[self.base(), self.Escoger_base_vertical_sup_iz()])
        self.boton3.grid(column=0, row=2, padx=5)
        self.canvas.bind("<Configure>", self.show_width)
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

    def borrar_linea(self):
        self.canvas.delete("diente1")
    
    def show_width(self,event):
        self.w = event.width
        self.h = event.height
    
    def Escoger_base_circular(self):
        self.actual = "base_doble"

    def Escoger_base_vertical_sup_iz(self):
        self.actual = "base_triple"

    def left_but_down(self, evento):
        opcion = 0
        self.permitido = False
        if(self.actual != "ninguno" and self.actual != None):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            if(self.actual == "base_doble"):
                base = Image.open("./src/bases/base_doble1.png")
                opcion = 1

            elif(self.actual == "base_triple"):
                base = Image.open("./src/bases/base_triple.png")
                opcion = 2
            
            self.tkimage = itk.PhotoImage(base)
            
            #IZQUIERDA

            #MULTIPLE

            if (tupla[0] == 47 and self.no_existe_diente(47) and self.no_existe_diente(46) and self.no_existe_diente(45)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble3.png")
                        self.conf_imagen(base,160,155,ancho = 150, alto = 350,rotacion = 0, flip=True)

            if (tupla[0] == 47 and self.no_existe_diente(47) and self.no_existe_diente(46)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble2.png")
                        self.conf_imagen(base,170,168,ancho = 160, alto = 395,rotacion = 3, flip=True)

            #INDIVIDUAL
        
            elif (tupla[0] == 47 and self.no_existe_diente(47)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1.png")
                        self.conf_imagen(base,160,175, ancho=150, alto=270, rotacion = 0, flip=True)

            elif (tupla[0] == 46 and self.no_existe_diente(46)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1.png")
                        self.conf_imagen(base,180,290,ancho=150, alto=270,rotacion = 5, flip=True)
                   
            elif (tupla[0] == 45 and self.no_existe_diente(45)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1.png")
                        self.conf_imagen(base,215,400,ancho=130, alto=200,rotacion = 20, flip=True)

            elif (tupla[0] == 44 and self.no_existe_diente(44)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1_ro.png")
                        self.conf_imagen(base,238,463,ancho=120, alto=162,rotacion = 5, flip=True)

            elif (tupla[0] == 43 and self.no_existe_diente(43)):
                if(opcion == 1):
                    if (not tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1_ro.png")
                        self.conf_imagen(base,295,525,ancho=90, alto=135,rotacion = 26, flip=True)

            #DERECHA

            #MULTIPLE

            if (tupla[0] == 37 and self.no_existe_diente(37) and self.no_existe_diente(36) and self.no_existe_diente(35)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble3.png")
                        self.conf_imagen(base,632,174,ancho = 150, alto = 310,rotacion = 0)

            #INDIVIDUAL

            elif (tupla[0] == 37 and self.no_existe_diente(37)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1.png")
                        self.conf_imagen(base,632,175,ancho=150,alto=260,rotacion = 0) 
                              
            elif (tupla[0] == 36 and self.no_existe_diente(36)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1.png")
                        self.conf_imagen(base,620,275,ancho=150, alto=270,rotacion = -8)
          
            elif (tupla[0] == 35 and self.no_existe_diente(35)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1_ro.png")
                        self.conf_imagen(base,655,378,ancho=100, alto=150,rotacion = 8)
                        
            elif (tupla[0] == 34 and self.no_existe_diente(34)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1_ro.png")
                        self.conf_imagen(base,620,450,ancho=100, alto=162,rotacion = -5)           

            elif (tupla[0] == 33 and self.no_existe_diente(33)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        base = Image.open("./src/bases/base_doble1_ro.png")
                        self.conf_imagen(base,575,525, ancho=90, alto=130,rotacion = -28)

            var.agregarBase(self.tkimage)
            ultimo_elemento = len(self.Bases)-1
            if(self.permitido):
                self.canvas.create_image(
                    self.x, self.y, image=var.Bases[ultimo_elemento], anchor="nw", tag="base"+"_"+str(ultimo_elemento))
                var.grabar(2, self.x, self.y, opcion)

    def limpiar(self):
        self.canvas.delete("base")   
        var.borrarBase()
        self.actual = "ninguno" 
    
    def left_but_up(self, evento):
        return  