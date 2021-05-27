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
            self.frame, image=self.im1, command=lambda:[self.retenedor(), self.Escoger_retenedor_circular()])
        self.boton2.grid(column=0, row=1, padx=5)
        self.boton3 = ttk.Button(
            self.frame, image=self.im2, command=lambda:[self.retenedor_i(), self.Escoger_retenedor_vertical_sup_iz()])
        self.boton3.grid(column=0, row=2, padx=5)
        self.boton7 = ttk.Button(
            self.frame, image=self.im6, command=lambda:[self.retenedor_t(), self.Escoger_retenedor_barra_t()])
        self.boton7.grid(column=0, row=5, padx=5)

        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def retenedor(self):
        self.ancho=int(width/4)
        self.largo=int(3*height/4)
        self.img = Image.open('./src/imagenes/retenedor.png')
        self.img = self.img.resize((self.ancho, int(7*self.largo/32)), Image.ANTIALIAS)
        self.img = itk.PhotoImage(self.img) 
        self.label = ttk.Label(self.frame, image = self.img).place(x=-2,y=int(5*self.largo/8))
        self.tamaño=Font(family="Bahnschrift", size = int(width/100))
        self.opcion=Font(family="Roboto Mono", size = int(width/196))
        self.titulo = ttk.Label(self.frame, font=self.tamaño, width=self.ancho, text="Retenedor circunferencial").place(x=13*self.ancho/64,y=55*self.largo/64)
        self.descripcion = ttk.Label(self.frame, font=self.opcion, wraplength= int(15*self.ancho/16), width=self.ancho, justify="center",
        text="Abraza la circunferencia del diente molar o premolar. Tiene dos brazos curvos: uno del mismo grosor desde su inicio hasta su fin, y otro que se va adelgazando progresivamente hasta terminar en punta. Color ROJO. Se usa indistintamente en dientes posteriores molares y premolares, superiores e inferiores.").place(x=self.ancho/32,y=58*self.largo/64) 

    def retenedor_i(self):
        self.ancho=int(width/4)
        self.largo=int(3*height/4)
        self.img = Image.open('./src/imagenes/retenedor_i.png')
        self.img = self.img.resize((self.ancho, int(7*self.largo/32)), Image.ANTIALIAS)
        self.img = itk.PhotoImage(self.img) 
        self.label = ttk.Label(self.frame, image = self.img).place(x=-2,y=int(5*self.largo/8))
        self.tamaño=Font(family="Bahnschrift", size = int(width/100))
        self.opcion=Font(family="Roboto Mono", size = int(width/196))
        self.titulo = ttk.Label(self.frame, font=self.tamaño, text="Retenedor de barra en I", width=self.ancho).place(x=13*self.ancho/64,y=55*self.largo/64)
        self.descripcion = ttk.Label(self.frame, font=self.opcion, wraplength= int(15*self.ancho/16), width=self.ancho, justify="center",
        text="Tiene un solo brazo, bastante largo que viene a tomar contacto con el diente en un solo punto (llamado en “I”), o dos puntos (llamado en “T” o en “Y”). Color ROJO. Los retenedores en “I” se usan en dientes superiores por ser menos notorios al sonreír, generalmente en caninos o 1° premolares superiores.").place(x=self.ancho/32,y=58*self.largo/64) 

    def retenedor_t(self):
        self.ancho=int(width/4)
        self.largo=int(3*height/4)
        self.img = Image.open('./src/imagenes/retenedor_t.png')
        self.img = self.img.resize((self.ancho, int(7*self.largo/32)), Image.ANTIALIAS)
        self.img = itk.PhotoImage(self.img) 
        self.label = ttk.Label(self.frame, image = self.img).place(x=-2,y=int(5*self.largo/8))
        self.tamaño=Font(family="Bahnschrift", size = int(width/100))
        self.opcion=Font(family="Roboto Mono", size = int(width/196))
        self.titulo = ttk.Label(self.frame, font=self.tamaño, text="Retenedor de barra en T", width=self.ancho).place(x=13*self.ancho/64,y=55*self.largo/64)
        self.descripcion = ttk.Label(self.frame, font=self.opcion, wraplength= int(15*self.ancho/16), width=self.ancho, justify="center",
        text="Tiene un solo brazo, bastante largo que viene a tomar contacto con el diente en un solo punto (llamado en “I”), o dos puntos (llamado en “T” o en “Y”). Color ROJO. Los retenedores en “T” se usan más en dientes inferiores.").place(x=self.ancho/32,y=58*self.largo/64) 
    
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
        w = int(width/1920)
        h = int(height/1080)
        self.permitido = False
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
                    self.conf_imagen(Retenedor,85,50,ancho = 180, alto = 140,extra = RetenedorD, separado = 5)
                    
            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,85,165,ancho = 160, alto = 140,extra = RetenedorD, separado = 20)

            elif (tupla[0] == 46 and self.existe_diente(46)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,103,300,ancho = 150, alto = 130,extra = RetenedorD, separado = 12,rotacion = 15)

            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,105,440,ancho = 140, alto = 95,extra = RetenedorD, separado = 20,rotacion = 30)

            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(opcion == 1):
                    self.permitido = True
                    Retenedor = Retenedor.resize((120*w, 80*h), Image.ANTIALIAS)
                    self.tkimage = itk.PhotoImage(Retenedor.rotate(30))
                    self.x = 142
                    self.y = 435

                if(opcion == 2):
                    self.conf_imagen(Retenedor,155,475)
                   
                if(opcion == 3):
                    self.conf_imagen(Retenedor,155,475)

            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(opcion == 2):
                    self.conf_imagen(Retenedor,215,560, rotacion = 25)
                
                if(opcion == 3):
                    self.conf_imagen(Retenedor,215,560, rotacion = 25)

            if (tupla[0] == 38 and self.existe_diente(38)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,685,47,ancho = 175, alto = 140, extra = RetenedorD, flip = True, separado = 5)
                    
            if (tupla[0] == 37 and self.existe_diente(37)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,692,165, ancho = 155,alto = 125, extra = RetenedorD, flip = True, separado =15)

            if (tupla[0] == 36 and self.existe_diente(36)):
                if(opcion == 1):
                    self.conf_imagen(Retenedor,687,285, ancho =165, alto =130, extra = RetenedorD, flip = True, separado =8, rotacion = 340)
                    
            if (tupla[0] == 35 and self.existe_diente(35)):
                if(opcion == 1):
                    self.permitido = True
                    Retenedor = Retenedor.resize((140*w, 95*h), Image.ANTIALIAS)
                    Retenedor = Retenedor.rotate(30)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 540
                    self.y = 342

            if (tupla[0] == 34 and self.existe_diente(34)):
                if(opcion == 1):
                    self.permitido = True
                    Retenedor = Retenedor.resize((120*w, 80*h), Image.ANTIALIAS)
                    Retenedor = Retenedor.rotate(30)
                    Retenedor = Retenedor.transpose(Image.FLIP_LEFT_RIGHT)
                    self.tkimage = itk.PhotoImage(Retenedor)
                    self.x = 525
                    self.y = 420

                if(opcion == 2):
                    self.conf_imagen(Retenedor, 689,455, flip = True)
                
                if(opcion == 3):
                    self.conf_imagen(Retenedor, 689,455, flip = True)

            if (tupla[0] == 33 and self.existe_diente(33)):
                if(opcion == 2):
                    self.conf_imagen(Retenedor, 645,535, rotacion = 335, flip = True)
                
                if(opcion == 3):
                    self.conf_imagen(Retenedor, 645,535, rotacion = 335, flip = True)

            var.agregarRetenedor(self.tkimage)
            ultimo_elemento = len(self.Retenedores)-1
            if(self.permitido):
                self.canvas.create_image(self.x, self.y, image=self.Retenedores[ultimo_elemento], anchor="nw", tag="retenedor")
                var.grabar(3,self.x,self.y,opcion)
                
    def left_but_up(self, evento):
        return

    def limpiar(self):
        self.canvas.delete("retenedor")
