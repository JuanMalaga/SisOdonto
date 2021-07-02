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


class interfaz_fase_2(interfaz):
    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    frame: Frame
    direccionBase = "./src/apoyos/"

    def __init__(self):
        self.opcion = 0
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.Apoyos = var.Apoyos

    def iniciar_interfaz(self):
        self.Apoyos = var.Apoyos
        self.cambiar_interfaz()
        self.crear_botones()

    def crear_botones(self):
        self.im1 = self.crearImagenBoton('apoyo_oclusal_superior.png', "./src/imagenes/oclusales.png", "Apoyos oclusales",
                                         "")
        self.im3 = self.crearImagenBoton('apoyo_incisal.png', './src/imagenes/incisal.png', "Apoyos incisales",
                                         "")
        self.crear_Borrador_()
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def left_but_down(self, evento):
        a = 80
        b = 92
        #self.cuadriculas()
        self.permitido = False
        if(self.opcion != 0):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            if(self.opcion == 1):
                apoyoa = Image.open("./src/apoyos/apoyo_oclusal_superior.png")
                self.tkimage = itk.PhotoImage(apoyoa)

            elif(self.opcion == 2):
                apoyoa = Image.open("./src/apoyos/apoyo_incisal.png")
                self.tkimage = itk.PhotoImage(apoyoa)
            
            if (tupla[0] == 48 and self.existe_diente(48)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 160, 63, rotacion=180)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 160, 152)
                        dato = "2"
            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 160, 177, rotacion=180)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 160, 269)
                        dato = "2"
            elif (tupla[0] == 46 and self.existe_diente(46)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 163, 302, rotacion=180)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 175, 388, rotacion=40)
                        dato = "2"
            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 198, 424,
                                         ancho=30, alto=20, rotacion=172)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 219, 480,
                                         ancho=30, alto=20, rotacion=65)
                        dato = "2"
            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 240, 508,
                                         ancho=30, alto=20, rotacion=190)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 270, 550,
                                         ancho=30, alto=20, rotacion=70)
                        dato = "2"
            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(self.opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa, 265, 581,
                                         ancho=40, alto=25, rotacion=250)
                        dato = "1"
                    else:
                        self.conf_imagen(
                            apoyoa, 313, 625, ancho=40, alto=25, rotacion=19, flip=True)
                        dato = "2"
            elif (tupla[0] == 42 and self.existe_diente(42)):
                if(self.opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa, 320, 630,
                                         ancho=40, alto=25, rotacion=270)
                        dato = "1"
                    else:
                        self.conf_imagen(
                            apoyoa, 375, 645, ancho=40, alto=25, rotacion=49, flip=True)
                        dato = "2"
            elif (tupla[0] == 41 and self.existe_diente(41)):
                if(self.opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa, 387, 647,
                                         ancho=40, alto=25, rotacion=290)
                        dato = "1"
                    else:
                        self.conf_imagen(
                            apoyoa, 445, 650, ancho=40, alto=25, rotacion=55, flip=True)
                        dato = "2"
            if (tupla[0] == 38 and self.existe_diente(38)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 739, 60, rotacion=180)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 739, 150)
                        dato = "2"
            if (tupla[0] == 37 and self.existe_diente(37)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 739, 175, rotacion=180)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 739, 255)
                        dato = "2"
            if (tupla[0] == 36 and self.existe_diente(36)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 748, 292, rotacion=180)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 720, 372, rotacion=320)
                        dato = "2"
            if (tupla[0] == 35 and self.existe_diente(35)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 710, 402,
                                         ancho=30, alto=20, rotacion=185)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 683, 458,
                                         ancho=30, alto=20, rotacion=302)
                        dato = "2"
            if (tupla[0] == 34 and self.existe_diente(34)):
                if(self.opcion == 1):
                    if (tupla[1][0]):
                        self.conf_imagen(apoyoa, 670, 482,
                                         ancho=30, alto=20, rotacion=180)
                        dato = "1"
                    else:
                        self.conf_imagen(apoyoa, 640, 530,
                                         ancho=30, alto=20, rotacion=280)
                        dato = "2"

            if (tupla[0] == 33 and self.existe_diente(33)):
                if(self.opcion == 2):
                    if (not tupla[1][1] or not tupla[1][0]):
                        self.conf_imagen(apoyoa, 520+a, 518+b,
                                         ancho=40, alto=25, rotacion=340)
                        dato = "1"
                    else:
                        self.conf_imagen(
                            apoyoa, 570+a, 472+b, ancho=40, alto=25, rotacion=105, flip=True)
                        dato = "2"
            if (tupla[0] == 32 and self.existe_diente(32)):
                if(self.opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa, 450+a, 550+b,
                                         ancho=40, alto=25, rotacion=305)
                        dato = "1"
                    else:
                        self.conf_imagen(
                            apoyoa, 510+a, 535+b, ancho=40, alto=25, rotacion=93, flip=True)
                        dato = "2"
            if (tupla[0] == 31 and self.existe_diente(31)):
                if(self.opcion == 2):
                    if (not tupla[1][1]):
                        self.conf_imagen(apoyoa, 375+a, 558+b,
                                         ancho=40, alto=25, rotacion=290)
                        dato = "1"
                    else:
                        self.conf_imagen(
                            apoyoa, 435+a, 555+b, ancho=40, alto=25, rotacion=70, flip=True)
                        dato = "2"

            if(self.permitido):
                ApoyoEnPantalla = str(tupla[0])+dato
                var.AgregarDato(ApoyoEnPantalla)
                var.agregarApoyo(self.tkimage)
                self.canvas.create_image(
                    self.x, self.y, image=var.Apoyos[-1], anchor="nw", tag="apoyo"+"_"+str(len(var.Apoyos)))
                var.grabar(2, self.x, self.y, self.opcion)

    def limpiar(self):

        self.canvas.delete("apoyo")
        
        for i in range(len(var.Apoyos)):
            self.canvas.delete("apoyo"+"_"+str(i+1))

        var.borrarApoyos()
        

    def left_but_up(self, evento):
        pass
