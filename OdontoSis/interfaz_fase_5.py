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


class interfaz_fase_5(interfaz):
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo: tk.PhotoImage
    conectores: tk.PhotoImage = []
    direccionBase = "./src/conectores_mayores/inferiores/"
    frame: Frame

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
        
        if(self.opcion != 0):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            self.tkimage = None

            if(self.opcion == 1):
                conector_mayor = Image.open(
                    self.direccionBase+"conec_mayor.png")

                mitad = Image.open(self.direccionBase+"conec_mayor.png")
                mitad = mitad.transpose(Image.FLIP_LEFT_RIGHT)

                self.conf_imagen(conector_mayor, 249, 75,extra=mitad, Ampliar_separacion=True)

                
            elif(self.opcion == 2):
                conector_mayor = tk.PhotoImage(
                    file=self.direccionBase+"doble_barra_lingual.png")
                self.x = 184
                self.y = 172
    

            elif(self.opcion == 3):
                conector_mayor = tk.PhotoImage(
                    file=self.direccionBase+"placa_lingual.png")
                self.x = 248
                self.y = 406


            var.agregarConec_Mayor(self.tkimage)
            ultimo_elemento = len(self.conectores)-1
            if(self.permitido):
                self.canvas.create_image(
                    self.x, self.y, image=self.conectores[ultimo_elemento], anchor="nw", tag="conector_mayor")
                var.grabar(5, self.x, self.y, self.opcion)
            superponedor = Image.open(self.direccionBase+"base_limpia.png")
            
            
            self.cortar_imagenes(evento.y-73, evento.y-73)
            

    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("conector_mayor")
    
    def cortar_imagenes(self,x=-1,y=-1):
        self.borradores = []
        superponedor = Image.open(self.direccionBase+"base_limpia.png")

        if(x!=-1 and y!=-1):
            crop = (0,0,superponedor.width,x)
            crop2 = (0,0,superponedor.width,y)
            
        
        self.conf_imagen(superponedor,249,73,crop=crop)
        self.borradores.append(self.tkimage)
        self.canvas.create_image(self.x, self.y, image=self.borradores[-1], anchor="nw", tag="conector_mayor")

        mitad = Image.open(self.direccionBase+"base_limpia.png")
        self.conf_imagen(mitad, 249+superponedor.width,73,crop=crop2,flip=True)
        self.borradores.append(self.tkimage)
        self.canvas.create_image(self.x, self.y, image=self.borradores[-1], anchor="nw", tag="conector_mayor")
