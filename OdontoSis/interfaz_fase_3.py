import tkinter as tk
from PIL import Image
from tkinter import ttk
from tkinter.font import Font
from interfaz import interfaz
from variables import VarGlo
from tkinter import Frame, Button, Label
from variables import VarGlo
from PIL import ImageTk as itk
import ctypes

resolucion = ctypes.windll.user32 
width = resolucion.GetSystemMetrics(0)
height = resolucion.GetSystemMetrics(1)

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
        self.opcion = 0
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.Retenedores = var.Retenedores

    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        self.crear_botones()
        
    def crear_botones(self):
        self.crearImagenBoton('retenedores.png','./src/imagenes/retenedor.png',"Retenedor circunferencial","")
        self.crearImagenBoton("Retenedor_Vertica_sup_iz.png",'./src/imagenes/retenedor_i.png',"Retenedor de barra en I","")
        self.crearImagenBoton("retenedor_barra_T.png",'./src/imagenes/retenedor_t.png',"Retenedor de barra en T","")
        self.crear_Borrador_()    
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def left_but_down(self, evento):
        self.permitido = False
        suma = 0
        const = 10
        if(self.opcion != 0):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            if(self.opcion == 1):
                Retenedor = Image.open("./src/retenedores/retenedores_izquierdo.png")
                RetenedorD = Image.open("./src/retenedores/retenedores_derecho.png")

            elif(self.opcion == 2):
                Retenedor = Image.open("./src/retenedores/Retenedor_Vertica_sup_iz.png")
               
            elif(self.opcion == 3):
                Retenedor = Image.open("./src/retenedores/retenedor_barra_T.png")
                

            self.tkimage = itk.PhotoImage(Retenedor)
            
            if(tupla[1][0]):
                RetenedorD = Image.open("./src/retenedores/retenedores_derecho_inv.png")

            if (tupla[0] == 48 and self.existe_diente(48)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        vert = True
                        suma = const
                    else:
                        vert = False
                    self.conf_imagen(Retenedor,85,50+suma,ancho = 180, alto = 140,extra = RetenedorD, separado = 15, vertical = vert)
            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        vert = True
                        suma = const
                    else:
                        vert = False
                    self.conf_imagen(Retenedor,85,165+suma,ancho = 160, alto = 140,extra = RetenedorD, separado = 15, vertical = vert)

            elif (tupla[0] == 46 and self.existe_diente(46)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        Retenedor = Image.open("./src/retenedores/37_inv.png")
                    else:
                        Retenedor = Image.open("./src/retenedores/37.png")
                    self.conf_imagen(Retenedor,112,295)

            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        Retenedor = Image.open("./src/retenedores/35_inv.png")
                    else:
                        Retenedor = Image.open("./src/retenedores/35.png")
                    
                    self.conf_imagen(Retenedor,159,418, alto = 110)

                if(self.opcion == 2):
                    self.conf_imagen(Retenedor,110,392,rotacion =350)
                   
                if(self.opcion == 3):
                    self.conf_imagen(Retenedor,110,392,rotacion =350)

            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        Retenedor = Image.open("./src/retenedores/34_inv.png")
                    else:
                        Retenedor = Image.open("./src/retenedores/34.png")
                    self.conf_imagen(Retenedor,210,500)

                if(self.opcion == 2):
                    self.conf_imagen(Retenedor,155,475)
                   
                if(self.opcion == 3):
                    self.conf_imagen(Retenedor,155,475)

            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(self.opcion == 2):
                    self.conf_imagen(Retenedor,215,560, rotacion = 25)
                
                if(self.opcion == 3):
                    self.conf_imagen(Retenedor,215,560, rotacion = 25)

            if (tupla[0] == 38 and self.existe_diente(38)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        vert = True
                        suma = const
                    else:
                        vert = False
                    self.conf_imagen(Retenedor,685,47+suma,ancho = 175, alto = 140, extra = RetenedorD, flip = True, separado = 5, vertical = vert)
                    
            if (tupla[0] == 37 and self.existe_diente(37)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        vert = True
                        suma = const
                    else:
                        vert = False
                    self.conf_imagen(Retenedor,692,165+suma, ancho = 155,alto = 125, extra = RetenedorD, flip = True, separado =15, vertical = vert)

            if (tupla[0] == 36 and self.existe_diente(36)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        Retenedor = Image.open("./src/retenedores/37_inv.png")
                    else:
                        Retenedor = Image.open("./src/retenedores/37.png")
                    self.conf_imagen(Retenedor,700,280, flip = True, rotacion = -10)
                    
            if (tupla[0] == 35 and self.existe_diente(35)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        Retenedor = Image.open("./src/retenedores/35_inv.png")
                    else:
                        Retenedor = Image.open("./src/retenedores/35.png")

                    self.conf_imagen(Retenedor,670,400, flip = True, alto = 100)
                if(self.opcion == 2):
                    self.conf_imagen(Retenedor, 735,368, flip = True,rotacion =10)
                
                if(self.opcion == 3):
                    self.conf_imagen(Retenedor, 735,368, flip = True,rotacion =10)
            if (tupla[0] == 34 and self.existe_diente(34)):
                if(self.opcion == 1):
                    if(tupla[1][0]):
                        Retenedor = Image.open("./src/retenedores/34_inv.png")
                    else:
                        Retenedor = Image.open("./src/retenedores/34.png")
                    self.conf_imagen(Retenedor,633,480,flip = True)

                if(self.opcion == 2):
                    self.conf_imagen(Retenedor, 689,455, flip = True)
                
                if(self.opcion == 3):
                    self.conf_imagen(Retenedor, 689,455, flip = True)

            if (tupla[0] == 33 and self.existe_diente(33)):
                if(self.opcion == 2):
                    self.conf_imagen(Retenedor, 645,535, rotacion = 335, flip = True)
                
                if(self.opcion == 3):
                    self.conf_imagen(Retenedor, 645,535, rotacion = 335, flip = True)

            var.agregarRetenedor(self.tkimage)
            ultimo_elemento = len(self.Retenedores)-1
            if(self.permitido):
                self.canvas.create_image(self.x, self.y, image=self.Retenedores[ultimo_elemento], anchor="nw", tag="retenedor")
                var.grabar(3,self.x,self.y,self.opcion)
                
    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("retenedor")
