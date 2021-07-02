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
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo: tk.PhotoImage
    conectores: tk.PhotoImage = []
    direccionBase = "./src/conectores_menores/"

    def __init__(self):
        self.opcion = 0
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.conectores = var.Conectores_menores

    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        self.crear_botones()

    def crear_botones(self):
        self.crearImagenBoton('superior_posterior.png')
        self.crearImagenBoton("aislado_boton.png")
        self.crearImagenBoton("redondo_boton.png")
        self.crearImagenBoton("superior_anterior.png")

        self.crear_Borrador_()
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def left_but_down(self, evento):
        self. permitido = False
        if(self.opcion != 0):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()

            #OPCIONES
            if(self.opcion == 1):
                Retenedor = Image.open(self.direccionBase+"48.png")

            elif(self.opcion == 2):
                Retenedor = Image.open(self.direccionBase+"superior_anterior.png")

            elif(self.opcion == 3):
                Retenedor = Image.open(self.direccionBase+"superior_posterior.png")

            #posicionamiento
            if (tupla[0] == 48 and self.existe_diente(48)):
                if(self.opcion == 1):
                    if (var.revisarDatos("482") and not tupla[1][0]):
                        self.conf_imagen(Retenedor, 150, 161, ancho = 140)

            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(self.opcion == 1):
                    if(var.revisarDatos("471") and tupla[1][0]):
                        self.conf_imagen(Retenedor, 149, 160, vertical= True, ancho = 140)

                    if(var.revisarDatos("472") and not tupla[1][0]):
                        self.conf_imagen(Retenedor, 150, 280, ancho = 155)

            elif (tupla[0] == 46 and self.existe_diente(46)):
                if(self.opcion == 1):
                    if(var.revisarDatos("461") and tupla[1][0]):
                        self.conf_imagen(Retenedor, 155, 280, vertical= True)

                    if(var.revisarDatos("462") and not tupla[1][0]):
                        Retenedor = Image.open(self.direccionBase+"36_inf.png")
                        self.conf_imagen(Retenedor, 150, 372)

            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(self.opcion == 1):
                    Retenedor = Image.open(self.direccionBase+"35.png")
                    if(var.revisarDatos("451") and tupla[1][0]):
                        self.conf_imagen(Retenedor, 183, 392)

                    if(var.revisarDatos("452") and not tupla[1][0]):
                        self.conf_imagen(Retenedor, 210, 410,  vertical= True, rotacion=45, expand = True)

            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(self.opcion ==  1):
                    Retenedor = Image.open(self.direccionBase+"44.png")
                    if (tupla[1][0] and var.revisarDatos("441")):
                        self.conf_imagen(Retenedor, 236, 465,ancho = 110)
                    if(not tupla[1][0] and var.revisarDatos("442")):
                        self.conf_imagen(Retenedor, 278, 490,vertical= True,rotacion= 60, expand= True,ancho = 110) 
                if(self.opcion == 2):
                    Retenedor = Image.open(self.direccionBase + "aislado.png")
                    if(tupla[1][0]):
                        self.conf_imagen(Retenedor,220,458)
                    else:
                        self.conf_imagen(Retenedor,250,510,rotacion = 10, expand = True)
                if(self.opcion == 3):
                    Retenedor = Image.open(self.direccionBase + "redondo.png")
                    if (tupla[1][0] and var.revisarDatos("441")):
                        self.conf_imagen(Retenedor, 236, 460)
                    elif(not tupla[1][0] and var.revisarDatos("442")):
                        self.conf_imagen(Retenedor, 236, 470, vertical= True,rotacion = 60, expand = True,ancho = 90)

            elif (tupla[0] == 38 and self.existe_diente(38)):
                if(self.opcion == 1):
                    if (var.revisarDatos("382") and not tupla[1][0]):
                        self.conf_imagen(Retenedor, 654, 161, flip = True)

            elif (tupla[0] == 37 and self.existe_diente(37)):
                if(self.opcion == 1):
                    if(var.revisarDatos("371") and tupla[1][0]):
                        self.conf_imagen(Retenedor, 654, 164, vertical= True,flip=True)

                    if(var.revisarDatos("372") and not tupla[1][0]):
                        self.conf_imagen(Retenedor, 640, 266,flip = True, ancho = 170)

            elif (tupla[0] == 36 and self.existe_diente(36)):
                if(self.opcion == 1):
                    if(var.revisarDatos("361") and tupla[1][0]):
                        self.conf_imagen(Retenedor, 655, 281, vertical= True,flip = True)

                    if(var.revisarDatos("362") and not tupla[1][0]):
                        Retenedor = Image.open(self.direccionBase+"36_inf.png")
                        self.conf_imagen(Retenedor, 628, 345,flip = True, rotacion = -10)

            elif (tupla[0] == 35 and self.existe_diente(35)):
                if(self.opcion == 1):
                    Retenedor = Image.open(self.direccionBase+"35.png")
                    if(var.revisarDatos("351") and tupla[1][0]):
                        self.conf_imagen(Retenedor, 620, 372,flip = True)

                    if(var.revisarDatos("352") and not tupla[1][0]):
                        self.conf_imagen(Retenedor, 598, 385,  vertical= True, rotacion=-45, expand = True,flip = True)

            elif (tupla[0] == 34 and self.existe_diente(34)):
                if(self.opcion ==  1):
                    Retenedor = Image.open(self.direccionBase+"44.png")
                    if (tupla[1][0] and var.revisarDatos("341")):
                        self.conf_imagen(Retenedor, 236, 465,ancho = 110)
                    if(not tupla[1][0] and var.revisarDatos("342")):
                        self.conf_imagen(Retenedor, 278, 490,vertical= True,rotacion= 60, expand= True,ancho = 110) 
                if(self.opcion == 2):
                    Retenedor = Image.open(self.direccionBase + "aislado.png")
                    if(tupla[1][0]):
                        self.conf_imagen(Retenedor,220,458)
                    else:
                        self.conf_imagen(Retenedor,250,510,rotacion = 10, expand = True)
                if(self.opcion == 3):
                    Retenedor = Image.open(self.direccionBase + "redondo.png")
                    if (tupla[1][0] and var.revisarDatos("341")):
                        self.conf_imagen(Retenedor, 236, 460)
                    elif(not tupla[1][0] and var.revisarDatos("342")):
                        self.conf_imagen(Retenedor, 236, 470, vertical= True,rotacion = 60, expand = True,ancho = 90)

            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(self.opcion == 1):
                    Retenedor = Image.open(
                        self.direccionBase + "largo_incisal.png")
                    if (not tupla[1][1] and var.revisarDatos("431")):
                        self.conf_imagen(Retenedor, 279, 510, rotacion=00)
                    elif(tupla[1][1] and var.revisarDatos("432")):
                        self.conf_imagen(Retenedor, 325, 540, rotacion=10)

            elif (tupla[0] == 42 and self.existe_diente(42)):
                if(self.opcion == 1):
                    Retenedor = Image.open(
                        self.direccionBase + "largo_incisal.png")
                    if (not tupla[1][1] and var.revisarDatos("421")):
                        self.conf_imagen(Retenedor, 326, 542, rotacion=15)
                    elif(tupla[1][1] and var.revisarDatos("422")):
                        self.conf_imagen(Retenedor, 340, 530, rotacion=38,expand=True)

            elif (tupla[0] == 41 and self.existe_diente(41)):
                if(self.opcion == 1):
                    Retenedor = Image.open(
                        self.direccionBase + "largo_incisal.png")
                    if (not tupla[1][1] and var.revisarDatos("411")):
                        self.conf_imagen(Retenedor, 350, 535, rotacion=38,expand=True)
                    elif(tupla[1][1] and var.revisarDatos("412")):
                        self.conf_imagen(Retenedor, 400, 535, rotacion=48,expand=True)

            elif (tupla[0] == 33 and self.existe_diente(33)):
                if(self.opcion == 1):
                    Retenedor = Image.open(
                        self.direccionBase + "largo_incisal.png")
                    if (tupla[1][0] and var.revisarDatos("331")):
                        self.conf_imagen(Retenedor, 279, 510, rotacion=00)
                    elif(not tupla[1][0] and var.revisarDatos("332")):
                        self.conf_imagen(Retenedor, 325, 540, rotacion=10)

            elif (tupla[0] == 32 and self.existe_diente(32)):
                if(self.opcion == 1):
                    Retenedor = Image.open(
                        self.direccionBase + "largo_incisal.png")
                    if (tupla[1][0] and var.revisarDatos("321")):
                        self.conf_imagen(Retenedor, 279, 510, rotacion=00)
                    elif(not tupla[1][0] and var.revisarDatos("322")):
                        self.conf_imagen(Retenedor, 325, 540, rotacion=10)

            elif (tupla[0] == 31 and self.existe_diente(31)):
                if(self.opcion == 1):
                    Retenedor = Image.open(
                        self.direccionBase + "largo_incisal.png")
                    if (tupla[1][0] and var.revisarDatos("311")):
                        self.conf_imagen(Retenedor, 279, 510, rotacion=00)
                    elif(not tupla[1][0] and var.revisarDatos("312")):
                        self.conf_imagen(Retenedor, 325, 540, rotacion=10)

            if(self.permitido):
                var.agregarConec_Menor(self.tkimage)
                ultimo_elemento = len(self.conectores)-1
                im = self.canvas.create_image(
                    self.x, self.y, image=self.conectores[ultimo_elemento], anchor="nw", tag="conector")
                var.grabar(3, self.x, self.y, self.opcion)
                var.Subir.append(im)
    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("conector")
