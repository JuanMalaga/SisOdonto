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
        self.botonsubir = ttk.Button(self.frame, bg= "yellow", border = "0", side="top", width=500).pack()

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
                base = Image.open("./src/bases/base_doble.png")
                opcion = 1

            elif(self.actual == "base_triple"):
                base = Image.open("./src/bases/base_triple.png")
                opcion = 2
            
            self.tkimage = itk.PhotoImage(base) 
               
            #CUATRO

            if (self.no_existe_diente(47) and self.no_existe_diente(46) and self.no_existe_diente(45) and self.no_existe_diente(44) and self.existe_diente(43)):
                if(tupla[0] == 47 or tupla[0] == 46 or tupla[0] == 45 or tupla[0] == 44):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/base_doble3.png")
                            self.conf_imagen(base,180,168,ancho = 155, alto = 420,rotacion = 8, flip=True)

            #TOTAL

            if (self.no_existe_diente(47) and self.no_existe_diente(46) and self.no_existe_diente(45) and self.no_existe_diente(44) and 
                self.no_existe_diente(43) and self.no_existe_diente(42) and self.no_existe_diente(41)):
                if(tupla[0] == 47 or tupla[0] == 46 or tupla[0] == 45 or tupla[0] == 44 or tupla[0] == 43 or tupla[0] == 42 or tupla[0] == 41):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/base_semicompleto.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(31) and self.no_existe_diente(32) and self.no_existe_diente(33) and self.no_existe_diente(34) and self.no_existe_diente(35) and 
                self.no_existe_diente(36) and self.no_existe_diente(37)):
                if(tupla[0] == 31 or tupla[0] == 32 or tupla[0] == 33 or tupla[0] == 34 or tupla[0] == 35 or tupla[0] == 36 or tupla[0] == 37):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/base_semicompleto_d.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(47) and self.no_existe_diente(46) and self.no_existe_diente(45) and self.no_existe_diente(44) and 
                self.no_existe_diente(43) and self.no_existe_diente(42) and self.no_existe_diente(41) and self.no_existe_diente(31) and 
                self.no_existe_diente(32) and self.no_existe_diente(33) and self.no_existe_diente(34) and self.no_existe_diente(35) and 
                self.no_existe_diente(36) and self.no_existe_diente(37)):
                if(tupla[0] == 47 or tupla[0] == 46 or tupla[0] == 45 or tupla[0] == 44 or tupla[0] == 43 or tupla[0] == 42 or tupla[0] == 41 
                or tupla[0] == 31 or tupla[0] == 32 or tupla[0] == 33 or tupla[0] == 34 or tupla[0] == 35 or tupla[0] == 36 or tupla[0] == 37):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/base_completo.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            #TRIPLE

            if (self.no_existe_diente(47) and self.no_existe_diente(46) and self.no_existe_diente(45) and self.existe_diente(44)):
                if(tupla[0] == 47 or tupla[0] == 46 or tupla[0] == 45):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_474645.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)  

            if (self.no_existe_diente(46) and self.no_existe_diente(45) and self.no_existe_diente(44) and self.existe_diente(47) and self.existe_diente(43)):
                if(tupla[0] == 46 or tupla[0] == 45 or tupla[0] == 44):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_464544.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)  

            if (self.no_existe_diente(45) and self.no_existe_diente(44) and self.no_existe_diente(43) and self.existe_diente(46) and self.existe_diente(42)):
                if(tupla[0] == 45 or tupla[0] == 44 or tupla[0] == 43):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_454443.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)  

            if (self.no_existe_diente(44) and self.no_existe_diente(43) and self.no_existe_diente(42) and self.existe_diente(45) and self.existe_diente(41)):
                if(tupla[0] == 44 or tupla[0] == 43 or tupla[0] == 42):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_444342.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(43) and self.no_existe_diente(42) and self.no_existe_diente(41) and self.existe_diente(44) and self.existe_diente(31)):
                if(tupla[0] == 43 or tupla[0] == 42 or tupla[0] == 41):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_434241.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(42) and self.no_existe_diente(41) and self.no_existe_diente(31) and self.existe_diente(43) and self.existe_diente(32)):
                if(tupla[0] == 42 or tupla[0] == 41 or tupla[0] == 31):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_424131.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(41) and self.no_existe_diente(31) and self.no_existe_diente(32) and self.existe_diente(42) and self.existe_diente(33)):
                if(tupla[0] == 41 or tupla[0] == 31 or tupla[0] == 32):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_413132.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(31) and self.no_existe_diente(32) and self.no_existe_diente(33) and self.existe_diente(41) and self.existe_diente(34)):
                if(tupla[0] == 31 or tupla[0] == 32 or tupla[0] == 33):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_313233.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(32) and self.no_existe_diente(33) and self.no_existe_diente(34) and self.existe_diente(31) and self.existe_diente(35)):
                if(tupla[0] == 32 or tupla[0] == 33 or tupla[0] == 34):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_323334.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(33) and self.no_existe_diente(34) and self.no_existe_diente(35) and self.existe_diente(32) and self.existe_diente(36)):
                if(tupla[0] == 33 or tupla[0] == 34 or tupla[0] == 35):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_333435.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)
            
            if (self.no_existe_diente(34) and self.no_existe_diente(35) and self.no_existe_diente(36) and self.existe_diente(33) and self.existe_diente(37)):
                if(tupla[0] == 34 or tupla[0] == 35 or tupla[0] == 36):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_343536.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(35) and self.no_existe_diente(36) and self.no_existe_diente(37) and self.existe_diente(34)):
                if(tupla[0] == 35 or tupla[0] == 36 or tupla[0] == 37):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/tres/base_triple_353637.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            #DOBLES

            if (self.no_existe_diente(47) and self.no_existe_diente(46) and self.existe_diente(45)):
                if(tupla[0] == 47 or tupla[0] == 46): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_4746.png")
                            self.conf_imagen(base,-8,162,ancho=510, alto=260, rotacion=1)

            if (self.no_existe_diente(46) and self.no_existe_diente(45) and self.existe_diente(47) and self.existe_diente(44)):
                if(tupla[0] == 46 or tupla[0] == 45): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_4645.png")
                            self.conf_imagen(base,5,290,ancho = 512, alto = 220, rotacion=-1)

            if (self.no_existe_diente(45) and self.no_existe_diente(44) and self.existe_diente(46) and self.existe_diente(43)):
                if(tupla[0] == 45 or tupla[0] == 44): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_4544.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(44) and self.no_existe_diente(43) and self.existe_diente(45) and self.existe_diente(42)):
                if(tupla[0] == 44 or tupla[0] == 43): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_4443.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(43) and self.no_existe_diente(42) and self.existe_diente(44) and self.existe_diente(41)):
                if(tupla[0] == 43 or tupla[0] == 42): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_4342.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)
            
            if (self.no_existe_diente(42) and self.no_existe_diente(41) and self.existe_diente(43) and self.existe_diente(31)):
                if(tupla[0] == 42 or tupla[0] == 41): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_4241.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)
            
            if (self.no_existe_diente(41) and self.no_existe_diente(31) and self.existe_diente(42) and self.existe_diente(32)):
                if(tupla[0] == 41 or tupla[0] == 31): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_4131.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(32) and self.no_existe_diente(31) and self.existe_diente(33) and self.existe_diente(41)):
                if(tupla[0] == 32 or tupla[0] == 31): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_3231.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(33) and self.no_existe_diente(32) and self.existe_diente(34) and self.existe_diente(31)):
                if(tupla[0] == 33 or tupla[0] == 32): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_3332.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(34) and self.no_existe_diente(33) and self.existe_diente(35) and self.existe_diente(32)):
                if(tupla[0] == 34 or tupla[0] == 33): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_3433.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(35) and self.no_existe_diente(34) and self.existe_diente(36) and self.existe_diente(33)):
                if(tupla[0] == 35 or tupla[0] == 34): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_3534.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(36) and self.no_existe_diente(35) and self.existe_diente(37) and self.existe_diente(34)):
                if(tupla[0] == 36 or tupla[0] == 35): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_3635.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(37) and self.no_existe_diente(36) and self.existe_diente(35)):
                if(tupla[0] == 37 or tupla[0] == 36): 
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/dos/base_doble_3736.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            #INDIVIDUAL
        
            if (self.no_existe_diente(47) and self.existe_diente(46)):
                if(tupla[0] == 47):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_47.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(46) and self.existe_diente(45) and self.existe_diente(47)):
                if(tupla[0] == 46):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_46.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)
                   
            if (self.no_existe_diente(45) and self.existe_diente(44) and self.existe_diente(46)):
                if(tupla[0] == 45):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_45.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(44) and self.existe_diente(43) and self.existe_diente(45)):
                if(tupla[0] == 44):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_44.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(43) and self.existe_diente(42) and self.existe_diente(44)):
                if(tupla[0] == 43):
                    if(opcion == 1):
                        if (not tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_43.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(42) and self.existe_diente(41) and self.existe_diente(43)):
                if(tupla[0] == 42):
                    if(opcion == 1):
                        if (not tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_42.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(41) and self.existe_diente(31) and self.existe_diente(42)):
                if(tupla[0] == 41):
                    if(opcion == 1):
                        if (not tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_41.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(37) and self.existe_diente(36)):
                if(tupla[0] == 37):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_37.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815) 
                              
            if (self.no_existe_diente(36) and self.existe_diente(35) and self.existe_diente(37)):
                if(tupla[0] == 36):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/base_doble1.png")
                            self.conf_imagen(base,620,275,ancho=150, alto=270,rotacion = -8)    
          
            if (self.no_existe_diente(35) and self.existe_diente(34) and self.existe_diente(36)):
                if(tupla[0] == 35):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_35.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)
                        
            if (self.no_existe_diente(34) and self.existe_diente(33) and self.existe_diente(35)):
                if(tupla[0] == 34):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_34.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)           

            if (self.no_existe_diente(33) and self.existe_diente(32) and self.existe_diente(34)):
                if(tupla[0] == 33):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_33.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(32) and self.existe_diente(31) and self.existe_diente(33)):
                if(tupla[0] == 32):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_32.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815)

            if (self.no_existe_diente(31) and self.existe_diente(32) and self.existe_diente(41)):
                if(tupla[0] == 31):
                    if(opcion == 1):
                        if (tupla[1][0]):
                            base = Image.open("./src/bases/uno/base_31.png")
                            self.conf_imagen(base,0,1,ancho=962, alto=815) 

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