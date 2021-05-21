import tkinter as tk
from PIL import Image
from tkinter import ttk
from interfaz import interfaz
from variables import VarGlo
from tkinter import Frame, Button, Label
from PIL import ImageTk as itk
import ctypes

resolucion = ctypes.windll.user32 
width = resolucion.GetSystemMetrics(0)
height = resolucion.GetSystemMetrics(1)

class interfaz_fase_2(interfaz):

    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    frame: Frame
    direccionBase = "./src/apoyos/"

    def __init__(self):
        global graficador
        global var
        global opcion
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.actual = "ninguno"
        opcion = 0
        self.Apoyos = var.Apoyos

    def iniciar_interfaz(self):
        self.Apoyos = var.Apoyos
        self.cambiar_interfaz()
        self.crear_botones()

    def crear_botones(self):
        
        self.im1 = Image.open(self.direccionBase+'apoyo_oclusal_superior.png')
        self.im1 = self.im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.im1 = itk.PhotoImage(self.im1)

        self.im3 = Image.open(self.direccionBase+'apoyo_incisal.png')
        self.im3 = self.im3.resize((var.size, var.size), Image.ANTIALIAS)
        self.im3 = itk.PhotoImage(self.im3)

        self.boton1 = ttk.Button(
            self.frame, image = self.im1, command=self.Escoger_apoyo_oclusal_superior)
        self.boton1.grid(column=0, row=1, padx=5)

        self.boton3 = ttk.Button(
            self.frame, image = self.im3, text="2", command=self.Escoger_apoyo_incisal)
        self.boton3.grid(column=0, row=2, padx=5)
        self.canvas.bind("<Configure>", self.show_width)
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)
        
            

    def borrar_linea(self):
        self.canvas.delete("diente1")
        var.borrarRetenedores()

    def show_width(self,event):
        self.w = event.width
        self.h = event.height

    def Escoger_apoyo_oclusal_superior(self):
        self.actual = "oclusal_superior"

    def Escoger_apoyo_incisal(self):
        self.actual = "incisal"

    def left_but_down(self, evento):
        opcion = 0
        self.permitido = False
        if(self.actual != "ninguno" and self.actual != None):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            if(self.actual == "oclusal_superior"):
                apoyoa = Image.open("./src/apoyos/apoyo_oclusal_superior.png")
                opcion = 1

            elif(self.actual == "incisal"):
                apoyoa = Image.open("./src/apoyos/apoyo_incisal.png")
                opcion = 2
                
            self.tkimage = itk.PhotoImage(apoyoa)
            if (tupla[0] == 48 and self.existe_diente(48)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,160,63,rotacion = 180)
                        
                    else:
                        self.conf_imagen(apoyoa,160,152)
                    
            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,160,177,rotacion = 180)
                    
                    else:
                        self.conf_imagen(apoyoa,160,269)

            elif (tupla[0] == 46 and self.existe_diente(46)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,163,302,rotacion = 180)
                        
                    else:
                        self.conf_imagen(apoyoa,175,388,rotacion = 40)

            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(opcion == 1):

                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,200,424,ancho = 35, alto = 25,rotacion = 172)

                    else:
                        self.conf_imagen(apoyoa,219,471,ancho = 35, alto = 25,rotacion = 55)

            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,240,508,ancho = 30, alto = 20,rotacion = 190)

                    else:
                        self.conf_imagen(apoyoa,270,550,ancho = 30, alto = 20,rotacion = 70)

            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa,207,502,ancho = 40, alto = 25,rotacion = 220)
                        
                    else:
                        self.conf_imagen(apoyoa,207,502,ancho = 40, alto = 25,rotacion = 40, flip = True)

            elif (tupla[0] == 42 and self.existe_diente(42)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa,263,545,ancho = 40, alto = 25,rotacion = 270)

                    else:
                        self.conf_imagen(apoyoa,305,555,ancho = 40, alto = 25,rotacion = 290, flip = True)

            elif (tupla[0] == 41 and self.existe_diente(41)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa,320,555,ancho = 40, alto = 25,rotacion = 270)
                        
                    else:
                        self.conf_imagen(apoyoa,368,560,ancho = 40, alto = 25,rotacion = 90, flip = True)

            if (tupla[0] == 38 and self.existe_diente(38)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,739,60,rotacion = 180)
                        
                    else:
                        self.conf_imagen(apoyoa,739,150)

            if (tupla[0] == 37 and self.existe_diente(37)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,739,175, rotacion = 180)
                        
                    else:
                        self.conf_imagen(apoyoa,739,255)
                        
            if (tupla[0] == 36 and self.existe_diente(36)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,740,292, rotacion = 180)
                    else:
                        self.conf_imagen(apoyoa,720,372, rotacion = 320)

            if (tupla[0] == 35 and self.existe_diente(35)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,700,400, ancho = 35, alto = 25,rotacion = 181)
                    else:
                        self.conf_imagen(apoyoa,680,450, ancho = 35, alto = 25,rotacion = 310)
                        
            if (tupla[0] == 34 and self.existe_diente(34)):
                if(opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa,663,482, ancho = 30, alto = 20,rotacion = 180)
                    else:
                        self.conf_imagen(apoyoa,640,530, ancho = 30, alto = 20,rotacion = 280)
                        

            if (tupla[0] == 33 and self.existe_diente(33)):
                if(opcion == 2):
                    if (not tupla[1][1]  or not tupla[1][0] ):
                        self.conf_imagen(apoyoa,500,525, ancho = 40, alto = 25,rotacion = 320)
                    else:
                        self.conf_imagen(apoyoa,540,490, ancho = 40, alto = 25,rotacion = 130, flip = True)

            if (tupla[0] == 32 and self.existe_diente(32)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa,440,550, ancho = 40, alto = 25,rotacion = 275)
                    else:
                        self.conf_imagen(apoyoa,486,540, ancho = 40, alto = 25,rotacion = 93, flip = True)

            if (tupla[0] == 31 and self.existe_diente(31)):
                if(opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa,380,558, ancho = 40, alto = 25,rotacion = 270)
                    else:
                        self.conf_imagen(apoyoa,426,555, ancho = 40, alto = 25,rotacion = 90, flip = True)
            
            var.agregarApoyo(self.tkimage)
            ultimo_elemento = len(self.Apoyos)-1
            if(self.permitido):
                self.canvas.create_image(
                    self.x, self.y, image=var.Apoyos[ultimo_elemento], anchor="nw", tag="apoyo"+"_"+str(ultimo_elemento))
                var.grabar(2, self.x, self.y, opcion)

    def limpiar(self):
        self.canvas.delete("apoyo")
        var.borrarApoyos()
        self.actual = "ninguno"

    def left_but_up(self, evento):
        pass


    
