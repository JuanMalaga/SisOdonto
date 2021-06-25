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

constante_x = width/1920
constante_y = height/1080

class interfaz_fase_5(interfaz):
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo: tk.PhotoImage
    conectores: tk.PhotoImage = []
    direccionBase = "./src/conectores_mayores/inferiores/"
    frame: Frame
    borradores = []
    def __init__(self):
        self.opcion = 0
        global var
        var = VarGlo()
        self.canvas = var.canvas
        self.frame = var.frame
        self.conectores = var.Conectores_mayores

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
        self.crearImagenBoton('barra_lingual_simple.png', './src/imagenes/barra_lingual_simple.png', "Barra lingual simple",
                              "Es muy delgada, se aloja en el piso de la boca, se aleja 3 mm del margen gingival. Su longitud depende de cada caso.")
        self.crearImagenBoton("doble_barra_lingual.png", './src/imagenes/doble_barra_lingual.png', " Doble barra lingual",
                              "La barra inferior es igual a la anterior. La barra superior va sobre los dientes anteriores inferiores. La barra inferior se aleja 3 mm del margen gingival.")
        self.crearImagenBoton("placa_lingual.png", './src/imagenes/placa.png', "Placa lingual",
                              "Cubre toda la encía, y llega hasta los cíngulos de los dientes anteriores, y hasta el ecuador de los dientes posteriores.")
        self.crear_Borrador_()

        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def left_but_down(self, evento):
        self.permitido = False
        tag = "conector_mayor"
        if(self.opcion != 0):
            superponedor = Image.open(self.direccionBase+"base_limpia.png")
            punto_de_corte = evento.y-73*constante_y
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            self.tkimage = None

            if(self.opcion == 1):
                conector_mayor = Image.open(
                    self.direccionBase+"conec_mayor.png")
                
            elif(self.opcion == 2):
                conector_mayor = Image.open(
                    self.direccionBase+"doble_barra_lingual_mitad.png")
                
            elif(self.opcion == 3):
                conector_mayor = Image.open(
                    self.direccionBase+"placa_lingual.png")
            
            if(self.opcion != 3):
                if(evento.x>470*constante_x):
                    self.canvas.delete("conector_mayor_derecho")
                    self.conf_imagen(conector_mayor, 249+conector_mayor.width, 75,flip=True)
                    tag = tag + "_derecho"
                else:
                    self.canvas.delete("conector_mayor_izquierdo")
                    self.conf_imagen(conector_mayor, 249, 75)
                    tag = tag + "_izquierdo"
            else:
                self.conf_imagen(conector_mayor,288,460)

            if(self.permitido):
                var.agregarConec_Mayor(self.tkimage)
                self.canvas.create_image(
                    self.x, self.y, image=self.conectores[-1], anchor="nw", tag=tag)
                
                var.grabar(5, self.x, self.y, self.opcion)
            print(evento.y)
            if(self.opcion != 3):
                if(evento.y<471*constante_y):
                    if(evento.x>470*constante_x):
                        self.cortar_imagenes(derecha = punto_de_corte)
                    else:
                        self.cortar_imagenes(izquierda = punto_de_corte)
                else:
                    if(evento.x>470):
                        self.cortar_imagenes(derecha = 398*constante_y)
                    else:
                        self.cortar_imagenes(izquierda = 398*constante_y)   

    def left_but_up(self, evento):
        for i in var.Subir:
            self.canvas.tag_raise(i)

    def limpiar(self):
        self.canvas.delete("conector_mayor")
        self.canvas.delete("conector_mayor_derecho")
        self.canvas.delete("conector_mayor_izquierdo")
    
    def cortar_imagenes(self,izquierda=-1,derecha=-1):
        superponedor = Image.open(self.direccionBase+"base_limpia.png")

        if(izquierda!=-1):
            crop = (0,0,superponedor.width,izquierda)
            self.conf_imagen(superponedor,249,73,crop=crop)
            self.borradores.append(self.tkimage)
            
        if(derecha!=-1):
            crop2 = (0,0,superponedor.width,derecha)
            mitad = Image.open(self.direccionBase+"base_limpia.png")
            self.conf_imagen(mitad, 249+superponedor.width,73,crop=crop2,flip=True)
            self.borradores.append(self.tkimage)
        
        self.canvas.create_image(self.x, self.y, image=self.borradores[-1], anchor="nw", tag="conector_mayor")

        
        

        