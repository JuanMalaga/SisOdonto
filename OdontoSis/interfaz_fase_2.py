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
        print(self.canvas.widget.winfo_width())
        self.w = event.width
        self.h = event.height
        print ('width  = {}, height = {}'.format(self.w, self.h))

    def Escoger_apoyo_oclusal_superior(self):
        self.actual = "oclusal_superior"

    def Escoger_apoyo_incisal(self):
        self.actual = "incisal"

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
                        print("inferior")
                        self.x = 127
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
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(40))
                        self.x = 140
                        self.y = 345

            elif (tupla[0] == 45 and self.existe_diente(45)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(172))
                        self.x = 160
                        self.y = 368
                    else:
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(55))
                        self.x = 175
                        self.y = 415

            elif (tupla[0] == 44 and self.existe_diente(44)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        apoyoa = apoyoa.resize((30, 20), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 190
                        self.y = 445
                    else:
                        apoyoa = apoyoa.resize((30, 20), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(70))
                        self.x = 215
                        self.y = 480

            elif (tupla[0] == 43 and self.existe_diente(43)):
                if(opcion == 2):
                    permitido = True
                    if (not tupla[1][1]):
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(220))
                        self.x = 207
                        self.y = 502
                    else:
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        apoyoa = apoyoa.transpose(Image.FLIP_LEFT_RIGHT)
                        apoyoa = apoyoa.rotate(40)
                        self.tkimage = itk.PhotoImage(apoyoa)
                        self.x = 250
                        self.y = 540   

            elif (tupla[0] == 42 and self.existe_diente(42)):
                if(opcion == 2):
                    permitido = True
                    if (not tupla[1][1]):
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(270))
                        self.x = 263
                        self.y = 545

                    else:
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        apoyoa = apoyoa.rotate(290)
                        apoyoa = apoyoa.transpose(Image.FLIP_LEFT_RIGHT)
                        self.tkimage = itk.PhotoImage(apoyoa)
                        self.x = 305
                        self.y = 555

            elif (tupla[0] == 41 and self.existe_diente(41)):
                if(opcion == 2):
                    permitido = True
                    if (not tupla[1][1]):
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(270))
                        self.x = 320
                        self.y = 555
                    else:
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        apoyoa = apoyoa.transpose(Image.FLIP_LEFT_RIGHT)
                        apoyoa = apoyoa.rotate(90)
                        self.tkimage = itk.PhotoImage(apoyoa)
                        self.x = 368
                        self.y = 560

            if (tupla[0] == 38 and self.existe_diente(38)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("arriba")
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(180))
                        self.x = 624
                        self.y = 44
                    else:
                        print("abajo")
                        self.x = 629
                        self.y = 120

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
                        self.x = 629
                        self.y = 251
                    else:
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(320))
                        print("no")
                        self.x = 612
                        self.y = 335

            if (tupla[0] == 35 and self.existe_diente(35)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(181))
                        self.x = 600
                        self.y = 355
                    else:
                        print("no")
                        apoyoa = apoyoa.resize((35, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(310))
                        self.x = 580
                        self.y = 408
            if (tupla[0] == 34 and self.existe_diente(34)):
                if(opcion == 1):
                    permitido = True
                    if (tupla[1][0]):
                        print("esta rotando")
                        apoyoa = apoyoa.resize((30, 20), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(147))
                        self.x = 572
                        self.y = 430
                    else:
                        print("no")
                        apoyoa = apoyoa.resize((30, 20), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(280))
                        self.x = 545
                        self.y = 465

            if (tupla[0] == 33 and self.existe_diente(33)):
                if(opcion == 2):
                    permitido = True
                    if (not tupla[1][1]  or not tupla[1][0] ):
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(320))
                        self.x = 500
                        self.y = 525

                    else:
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        apoyoa = apoyoa.transpose(Image.FLIP_LEFT_RIGHT)
                        apoyoa = apoyoa.rotate(130)
                        self.tkimage = itk.PhotoImage(apoyoa)
                        self.x = 540
                        self.y = 490

            if (tupla[0] == 32 and self.existe_diente(32)):
                if(opcion == 2):
                    permitido = True
                    if (not tupla[1][1]):
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(275))
                        self.x = 440
                        self.y = 550

                    else:
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        apoyoa = apoyoa.transpose(Image.FLIP_LEFT_RIGHT)
                        apoyoa = apoyoa.rotate(93)
                        self.tkimage = itk.PhotoImage(apoyoa)
                        self.x = 486
                        self.y = 540

            if (tupla[0] == 31 and self.existe_diente(31)):
                if(opcion == 2):
                    permitido = True
                    if (not tupla[1][1]):
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        self.tkimage = itk.PhotoImage(apoyoa.rotate(270))
                        self.x = 380
                        self.y = 558
                    else:
                        apoyoa = apoyoa.resize((40, 25), Image.ANTIALIAS)
                        apoyoa = apoyoa.transpose(Image.FLIP_LEFT_RIGHT)
                        apoyoa = apoyoa.rotate(90)
                        self.tkimage = itk.PhotoImage(apoyoa)
                        self.x = 426
                        self.y = 555

            var.agregarApoyo(self.tkimage)
            ultimo_elemento = len(self.Apoyos)-1
            if(permitido):
                self.canvas.create_image(
                    self.x, self.y, image=var.Apoyos[ultimo_elemento], anchor="nw", tag="apoyo"+"_"+str(ultimo_elemento))
                var.grabar(2, self.x, self.y, opcion)

    def limpiar(self):
        self.canvas.delete("apoyo")
        var.borrarApoyos()
        self.actual = "ninguno"

    def left_but_up(self, evento):
        pass