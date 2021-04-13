import tkinter as tk
from PIL import Image
from tkinter import ttk
from interfaz import interfaz
from variables import VarGlo
from tkinter import Frame, Button, Label
from PIL import ImageTk as itk


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

        self.im2 = Image.open(self.direccionBase+'apoyo_oclusal_inferior.png')
        self.im2 = self.im2.resize((var.size, var.size), Image.ANTIALIAS)
        self.im2 = itk.PhotoImage(self.im2)

        self.im3 = Image.open(self.direccionBase+'apoyo_incisal.png')
        self.im3 = self.im3.resize((var.size, var.size), Image.ANTIALIAS)
        self.im3 = itk.PhotoImage(self.im3)

        self.im4 = Image.open(self.direccionBase+'apoyo_circular.png')
        self.im4 = self.im4.resize((var.size, var.size), Image.ANTIALIAS)
        self.im4 = itk.PhotoImage(self.im4)

        self.boton1 = ttk.Button(
            self.frame, image=self.im1, command=self.Escoger_apoyo_oclusal_superior)
        self.boton1.grid(column=0, row=1, padx=5)

        self.boton3 = ttk.Button(
            self.frame, image=self.im3, text="2", command=self.Escoger_apoyo_incisal)
        self.boton3.grid(column=0, row=2, padx=5)

        self.boton4 = ttk.Button(
            self.frame, image=self.im4, text="1", command=self.Escoger_apoyo_circular)
        self.boton4.grid(column=1, row=2, padx=5)

        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def borrar_linea(self):
        self.canvas.delete("diente1")
        var.borrarRetenedores()

    def Escoger_apoyo_oclusal_superior(self):
        self.actual = "oclusal_superior"

    def Escoger_apoyo_oclusal_inferior(self):
        self.actual = "oclusal_inferior"

    def Escoger_apoyo_incisal(self):
        self.actual = "incisal"

    def Escoger_apoyo_circular(self):
        self.actual = "circular"

    def left_but_down(self, evento):
        opcion = 0
        permitido = False
        print(evento.x)
        print(evento.y)
        print(self.actual)
        if(self.actual != "ninguno" and self.actual != None):
            self.x = evento.x
            self.y = evento.y
            tupla = self.obtener_diente()
            if(self.actual == "oclusal_superior"):
                print("carga")
                apoyoa = Image.open("./src/apoyos/apoyo_oclusal_superior.png")
                opcion = 1

            elif(self.actual == "incisal"):
                apoyoa = Image.open("./src/apoyos/apoyo_incisal.png")
                opcion = 2

            elif(self.actual == "circular"):
                apoyoa = Image.open("./src/apoyos/apoyo_circular.png")
                opcion = 3
            
            self.tkimage = itk.PhotoImage(apoyoa)
            
            if (tupla[0] == 48 and self.existe_diente(48)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 130
                        self.y = 50
                    else:
                        print("no")
                        self.x = 131
                        self.y = 125

            elif (tupla[0] == 47 and self.existe_diente(47)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 127
                        self.y = 150
                    else:
                        print("no")
                        self.x = 125
                        self.y = 226

            elif (tupla[0] == 46 and self.existe_diente(46)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 125
                        self.y = 260
                    else:
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(25))
                        self.x = 140
                        self.y = 341

            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(195))
                        self.x = 145
                        self.y = 370
                    else:
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(10))
                        self.x = 159
                        self.y = 419

            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(200))
                        self.x = 175
                        self.y = 445
                    else:
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(15))
                        self.x = 195
                        self.y = 487 

            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(opcion == 2):
                    permitido = True
                    if (tupla[1][0]):
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(250))
                        self.x = 210
                        self.y = 500
                    else:
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(270))
                        self.x = 260
                        self.y = 530    

            elif (tupla[0] == 42 and self.existe_diente(42)):
                if(opcion == 2):
                    permitido = True
                    if (tupla[1][0]):
                        apoyoa = apoyoa.resize((40, 30), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(270))
                        self.x = 300
                        self.y = 535 
                    else:
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(15))
                        self.x = 195
                        self.y = 487

            elif (tupla[0] == 41 and self.existe_diente(41)):
                if(opcion == 2):
                    permitido = True
                    if (tupla[1][0]):
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(200))
                        self.x = 175
                        self.y = 445
                    else:
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(15))
                        self.x = 195
                        self.y = 487

            if (tupla[0] == 38 and self.existe_diente(38)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 624
                        self.y = 44
                    else:
                        print("no")
                        self.x = 629
                        self.y = 124

            if (tupla[0] == 37 and self.existe_diente(37)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 628
                        self.y = 144
                    else:
                        print("no")
                        self.x = 629
                        self.y = 222
            if (tupla[0] == 36 and self.existe_diente(36)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 624
                        self.y = 251
                    else:
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(340))
                        print("no")
                        self.x = 610
                        self.y = 335

            if (tupla[0] == 35 and self.existe_diente(35)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(170))
                        self.x = 605
                        self.y = 355
                    else:
                        print("no")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(340))
                        self.x = 584
                        self.y = 410
            if (tupla[0] == 34 and self.existe_diente(34)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(170))
                        self.x = 570
                        self.y = 430
                    else:
                        print("no")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(340))
                        self.x = 554
                        self.y = 467

            if (tupla[0] == 33 and self.existe_diente(33)):
                if(opcion == 2):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 130
                        self.y = 50
                    else:
                        print("no")
                        self.x = 131
                        self.y = 125

            if (tupla[0] == 32 and self.existe_diente(32)):
                if(opcion == 2):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 130
                        self.y = 50
                    else:
                        print("no")
                        self.x = 131
                        self.y = 125

            if (tupla[0] == 31 and self.existe_diente(31)):
                if(opcion == 2):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 130
                        self.y = 50
                    else:
                        print("no")
                        self.x = 131
                        self.y = 125

            var.agregarApoyo(self.tkimage)
            ultimo_elemento = len(self.Apoyos)-1
            if(permitido):
                self.canvas.create_image(
                    self.x, self.y, image=var.Apoyos[ultimo_elemento], anchor="nw", tag="apoyo"+"_"+str(ultimo_elemento))
                var.grabar(2, self.x, self.y, opcion)

    def limpiar(self):
        self.canvas.delete("apoyo")
        var.borrarApoyos()

    def left_but_up(self, evento):
        pass