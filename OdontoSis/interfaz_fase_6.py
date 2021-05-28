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
        self.Retenedores = var.Retenedores

    def iniciar_interfaz(self):
        self.Retenedores = var.Retenedores
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
            self.frame, image=self.im1, command=lambda:[self.base(), self.Escoger_retenedor_circular()])
        self.boton2.grid(column=0, row=1, padx=5)

        self.boton3 = ttk.Button(
            self.frame, image=self.im2, command=lambda:[self.base(), self.Escoger_retenedor_vertical_sup_iz()])
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
    
    def Escoger_retenedor_circular(self):
        self.actual = "base_doble"

    def Escoger_retenedor_vertical_sup_iz(self):
        self.actual = "base_triple"

    def left_but_down(self, evento):
        opcion = 0
        a = 80
        b = 92
        self.permitido = False
        if(self.actual != "ninguno" and self.actual != None):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            if(self.actual == "base_doble"):
                retenedor = Image.open("./src/bases/base_doble.png")
                opcion = 1

            elif(self.actual == "base_triple"):
                retenedor = Image.open("./src/bases/base_triple.png")
                opcion = 2
            
            self.tkimage = itk.PhotoImage(retenedor)

            if (tupla[0] == 48 and self.existe_diente(48)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,160,63,rotacion = 180)
                        
                    else:
                        self.conf_imagen(retenedor,160,152)

            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,160,177,rotacion = 180)
                    
                    else:
                        self.conf_imagen(retenedor,160,269)

            elif (tupla[0] == 46 and self.existe_diente(46)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,163,302,rotacion = 180)
                        
                    else:
                        self.conf_imagen(retenedor,175,388,rotacion = 40)

            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(opcion == 1):

                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,200,424,ancho = 35, alto = 25,rotacion = 172)

                    else:
                        self.conf_imagen(retenedor,219,471,ancho = 35, alto = 25,rotacion = 55)

            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,240,508,ancho = 30, alto = 20,rotacion = 190)

                    else:
                        self.conf_imagen(retenedor,270,550,ancho = 30, alto = 20,rotacion = 70)

            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(retenedor,265,581,ancho = 40, alto = 25,rotacion = 220)
                        
                    else:
                        self.conf_imagen(retenedor,313,625,ancho = 40, alto = 25,rotacion = 40, flip = True)

            elif (tupla[0] == 42 and self.existe_diente(42)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(retenedor,320,630,ancho = 40, alto = 25,rotacion = 270)

                    else:
                        self.conf_imagen(retenedor,375,645,ancho = 40, alto = 25,rotacion = 70, flip = True)

            elif (tupla[0] == 41 and self.existe_diente(41)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(retenedor,387,647,ancho = 40, alto = 25,rotacion = 270)
                        
                    else:
                        self.conf_imagen(retenedor,445,650,ancho = 40, alto = 25,rotacion = 90, flip = True)

            if (tupla[0] == 38 and self.existe_diente(38)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,739,60,rotacion = 180)
                        
                    else:
                        self.conf_imagen(retenedor,739,150)

            if (tupla[0] == 37 and self.existe_diente(37)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,739,175, rotacion = 180)
                        
                    else:
                        self.conf_imagen(retenedor,739,255)
                        
            if (tupla[0] == 36 and self.existe_diente(36)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,740,292, rotacion = 180)
                    else:
                        self.conf_imagen(retenedor,720,372, rotacion = 320)

            if (tupla[0] == 35 and self.existe_diente(35)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,700,400, ancho = 35, alto = 25,rotacion = 181)
                    else:
                        self.conf_imagen(retenedor,680,450, ancho = 35, alto = 25,rotacion = 310)
                        
            if (tupla[0] == 34 and self.existe_diente(34)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(retenedor,663,482, ancho = 30, alto = 20,rotacion = 180)
                    else:
                        self.conf_imagen(retenedor,640,530, ancho = 30, alto = 20,rotacion = 280)
                        

            if (tupla[0] == 33 and self.existe_diente(33)):
                if(opcion == 2):
                    if (not tupla[1][1]  or not tupla[1][0] ):
                        self.conf_imagen(retenedor,520+a,518+b, ancho = 40, alto = 25,rotacion = 320)
                    else:
                        self.conf_imagen(retenedor,570+a,472+b, ancho = 40, alto = 25,rotacion = 130, flip = True)

            if (tupla[0] == 32 and self.existe_diente(32)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(retenedor,450+a,550+b, ancho = 40, alto = 25,rotacion = 280)
                    else:
                        self.conf_imagen(retenedor,510+a,535+b, ancho = 40, alto = 25,rotacion = 93, flip = True)

            if (tupla[0] == 31 and self.existe_diente(31)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(retenedor,375+a,558+b, ancho = 40, alto = 25,rotacion = 270)
                    else:
                        self.conf_imagen(retenedor,435+a,555+b, ancho = 40, alto = 25,rotacion = 90, flip = True)

            var.agregarRetenedor(self.tkimage)
            ultimo_elemento = len(self.Retenedores)-1
            if(self.permitido):
                self.canvas.create_image(
                    self.x, self.y, image=var.Retenedores[ultimo_elemento], anchor="nw", tag="base"+"_"+str(ultimo_elemento))
                var.grabar(2, self.x, self.y, opcion)

    def limpiar(self):
        self.canvas.delete("base")   
        var.borrarRetenedores()
        self.actual = "ninguno" 
    
    def left_but_up(self, evento):
        return  