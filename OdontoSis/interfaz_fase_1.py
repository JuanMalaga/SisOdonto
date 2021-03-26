import variables
import tkinter as tk
from variables import interfaz
from PIL import Image
from tkinter import ttk


var = variables.VarGlo()

class inter_1(interfaz):

    # VARIABLES
    
    def __init__(self): 
        global frame 
        frame = var.frame
        self.diente1 = tk.IntVar(value=1)
        self.diente2 = tk.IntVar(value=1)
        self.diente3 = tk.IntVar(value=1)
        self.diente4 = tk.IntVar(value=1)
        self.diente5 = tk.IntVar(value=1)
        self.diente6 = tk.IntVar(value=1)
        self.diente7 = tk.IntVar(value=1)
        self.diente8 = tk.IntVar(value=1)
        self.diente9 = tk.IntVar(value=1)
        self.diente10 = tk.IntVar(value=1)
        self.diente11 = tk.IntVar(value=1)
        self.diente12 = tk.IntVar(value=1)
        self.diente13 = tk.IntVar(value=1)
        self.diente14 = tk.IntVar(value=1)
        self.diente15 = tk.IntVar(value=1)
        self.diente16 = tk.IntVar(value=1)
        
        
    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        self.etiquetas()
        self.tiposD()
        global graficador
        graficador  =  Graficador()
        var.Iniciar_Dentadura()
        graficador.actualizar()
        

    def iniciar_interfaz_sup(self):
        self.cambiar_interfaz()
        self.etiquetas()
        self.tiposD()
        graficador_sup = Graficador_Superior()
        var.Iniciar_Dentadura_Sup()
        graficador_sup.actualizar() 
        

    def etiquetas(self):
        tk.Label(frame, text="¿Qué dientes desea eliminar?",
         font="Bahnschrift 11", width=44, height=2).pack(anchor="w")
        tk.Checkbutton(frame, text="Tercer Molar Izquierdo (48)", variable=self.diente1,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente1, 1)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Molar Izquierdo (47)", variable=self.diente2,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente2, 2)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Molar Izquierdo (46)", variable=self.diente3,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente3, 3)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Premolar Izquierdo (45)", variable=self.diente4,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente4, 4)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Premolar Izquierdo (44)", variable=self.diente5,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente5, 5)).pack(anchor="w")
        tk.Checkbutton(frame, text="Canino (Cúspide) Izquierdo (43)", variable=self.diente6,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente6, 6)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Lateral Izquierdo (42)", variable=self.diente7,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente7, 7)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Central Izquierdo (41)", variable=self.diente8,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente8, 8)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Central Derecho (31)", variable=self.diente9,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente9, 9)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Lateral Derecho (32)", variable=self.diente10,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente10, 10)).pack(anchor="w")
        tk.Checkbutton(frame, text="Canino (Cúspide) Derecho (33)", variable=self.diente11,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente11, 11)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Premolar Derecho (34)", variable=self.diente12,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente12, 12)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Premolar Derecho (35)", variable=self.diente13,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente13, 13)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Molar Derecho (36)", variable=self.diente14,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente14, 14)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Molar Derecho (37)", variable=self.diente15,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente15, 15)).pack(anchor="w")
        tk.Checkbutton(frame, text="Tercer Molar Derecho (38)", variable=self.diente16,
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente16, 16)).pack(anchor="w")

    def tiposD(self):
        self.tipos = tk.PhotoImage(file="./src/tipos.png")
        imagen = tk.Label(var.frame2, image = self.tipos, width=353, height=240, background="white")
        imagen.pack()
        
    
    # OPCIONES DE BORRADO
    def Listener(self,variable, n):
        if variable.get():
            var.agregarDiente(n)
            
        else:
            var.eliminarDiente(n)
        graficador.actualizar()
        var.canvas = graficador.canvas     


class Graficador:

    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo: tk.PhotoImage
    dientes: tk.PhotoImage = []

    def __init__(self):
        global var
        var = variables.VarGlo()
        self.Dientes = var.Dientes
        self.pos_x_ini = 78
        self.pos_y_ini = 43
        self.ventana = var.ventana
        self.canvas = var.canvas
        global fondo
        #declarar todas las imagenes
        fondo = tk.PhotoImage(file="./src/Base_I_res.png")
        diente1 = tk.PhotoImage(file="./src/dientes/TercerMolar_I_I.png")
        self.dientes.append(diente1)
        diente2 = tk.PhotoImage(file="./src/dientes/SegundoMolar_I_I.png")
        self.dientes.append(diente2)
        diente3 = tk.PhotoImage(file="./src/dientes/PrimerMolar_I_I.png")
        self.dientes.append(diente3)
        diente4 = tk.PhotoImage(file="./src/dientes/SegundoPreMolar_I_I.png")
        self.dientes.append(diente4)
        diente5 = tk.PhotoImage(file="./src/dientes/PrimerPreMolar_I_I.png")
        self.dientes.append(diente5)
        diente6 = tk.PhotoImage(file="./src/dientes/Canino_I_I.png")
        self.dientes.append(diente6)
        diente7 = tk.PhotoImage(file="./src/dientes/IncisivoLateral_I_I.png")
        self.dientes.append(diente7)
        diente8 = tk.PhotoImage(file="./src/dientes/IncisivoCentral_I_I.png")
        self.dientes.append(diente8)
        diente9 = tk.PhotoImage(file="./src/dientes/IncisivoCentral_D_I.png")
        self.dientes.append(diente9)
        diente10 = tk.PhotoImage(file="./src/dientes/IncisivoLateral_D_I.png")
        self.dientes.append(diente10)
        diente11 = tk.PhotoImage(file="./src/dientes/Canino_D_I.png")
        self.dientes.append(diente11)
        diente12 = tk.PhotoImage(file="./src/dientes/PrimerPreMolar_D_I.png")
        self.dientes.append(diente12)
        diente13 = tk.PhotoImage(file="./src/dientes/SegundoPreMolar_D_I.png")
        self.dientes.append(diente13)
        diente14 = tk.PhotoImage(file="./src/dientes/PrimerMolar_D_I.png")
        self.dientes.append(diente14)
        diente15 = tk.PhotoImage(file="./src/dientes/SegundoMolar_D_I.png")
        self.dientes.append(diente15)
        diente16 = tk.PhotoImage(file="./src/dientes/TercerMolar_D_I.png")
        self.dientes.append(diente16)
        self.Iniciar_Dentadura()

    def actualizar(self):
        self.canvas.delete("all")
        self.Dientes = var.Dientes
        self.Iniciar_Dentadura()

    def Iniciar_Dentadura(self):

        self.canvas.create_image(0, 0, image=fondo, anchor="nw")
        
        for element in self.Dientes:

            if(element == 1):

                self.canvas.create_image(
                    self.pos_x_ini, self.pos_y_ini, image=self.dientes[0], anchor="nw")

            elif(element == 2):

                self.canvas.create_image(
                    self.pos_x_ini, self.pos_y_ini+100, image=self.dientes[1], anchor="nw")

            elif(element == 3):

                self.canvas.create_image(
                    self.pos_x_ini, self.pos_y_ini+200, image=self.dientes[2], anchor="nw")

            elif(element == 4):

                self.canvas.create_image(
                    self.pos_x_ini+25, self.pos_y_ini+300, image=self.dientes[3], anchor="nw")

            elif(element == 5):

                self.canvas.create_image(
                    self.pos_x_ini+72, self.pos_y_ini+377, image=self.dientes[4], anchor="nw")

            elif(element == 6):

                self.canvas.create_image(
                    self.pos_x_ini+127, self.pos_y_ini+437, image=self.dientes[5], anchor="nw")

            elif(element == 7):

                self.canvas.create_image(
                    self.pos_x_ini+192, self.pos_y_ini+454, image=self.dientes[6], anchor="nw")

            elif(element == 8):

                self.canvas.create_image(
                    self.pos_x_ini+237, self.pos_y_ini+454, image=self.dientes[7], anchor="nw")

            elif(element == 9):

                self.canvas.create_image(
                    self.pos_x_ini+287, self.pos_y_ini+462, image=self.dientes[8], anchor="nw")

            elif(element == 10):

                self.canvas.create_image(
                    self.pos_x_ini+357, self.pos_y_ini+437, image=self.dientes[9], anchor="nw")

            elif(element == 11):

                self.canvas.create_image(
                    self.pos_x_ini+402, self.pos_y_ini+427, image=self.dientes[10], anchor="nw")

            elif(element == 12):

                self.canvas.create_image(
                    self.pos_x_ini+462, self.pos_y_ini+377, image=self.dientes[11], anchor="nw")

            elif(element == 13):

                self.canvas.create_image(
                    self.pos_x_ini+473, self.pos_y_ini+299, image=self.dientes[12], anchor="nw")

            elif(element == 14):

                self.canvas.create_image(
                    self.pos_x_ini+498, self.pos_y_ini+200, image=self.dientes[13], anchor="nw")

            elif(element == 15):

                self.canvas.create_image(
                    self.pos_x_ini+508, self.pos_y_ini+92, image=self.dientes[14], anchor="nw")

            elif(element == 16):

                self.canvas.create_image(
                    self.pos_x_ini+504, self.pos_y_ini-5, image=self.dientes[15], anchor="nw")

class Graficador_Superior:

    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo: tk.PhotoImage
    dientes: tk.PhotoImage = []

    def __init__(self):
        global vars
        vars = variables.VarGlo()
        self.Dientes = vars.Dientes
        self.pos_x_ini = 45
        self.pos_y_ini = 530
        self.ventana = vars.ventana
        self.canvas = vars.canvas
        global fondo
        #declarar todas las imagenes
        fondo = tk.PhotoImage(file="./src_s/Base_S.png")
        diente17 = tk.PhotoImage(file="./src_s/TercerMolar_I_S.png")
        self.dientes.append(diente17)
        diente18 = tk.PhotoImage(file="./src_s/SegundoMolar_I_S.png")
        self.dientes.append(diente18)
        diente19 = tk.PhotoImage(file="./src_s/PrimerMolar_I_S.png")
        self.dientes.append(diente19)
        diente20 = tk.PhotoImage(file="./src_s/SegundoPreMolar_I_S.png")
        self.dientes.append(diente20)
        diente21 = tk.PhotoImage(file="./src_s/PrimerPreMolar_I_S.png")
        self.dientes.append(diente21)
        diente22 = tk.PhotoImage(file="./src_s/Canino_I_S.png")
        self.dientes.append(diente22)
        diente23 = tk.PhotoImage(file="./src_s/IncisivoLateral_I_S.png")
        self.dientes.append(diente23)
        diente24 = tk.PhotoImage(file="./src_s/IncisivoCentral_I_S.png")
        self.dientes.append(diente24)
        diente25 = tk.PhotoImage(file="./src_s/IncisivoCentral_D_S.png")
        self.dientes.append(diente25)
        diente26 = tk.PhotoImage(file="./src_s/IncisivoLateral_D_S.png")
        self.dientes.append(diente26)
        diente27 = tk.PhotoImage(file="./src_s/Canino_D_S.png")
        self.dientes.append(diente27)
        diente28 = tk.PhotoImage(file="./src_s/PrimerPreMolar_D_S.png")
        self.dientes.append(diente28)
        diente29 = tk.PhotoImage(file="./src_s/SegundoPreMolar_D_S.png")
        self.dientes.append(diente29)
        diente30 = tk.PhotoImage(file="./src_s/PrimerMolar_D_S.png")
        self.dientes.append(diente30)
        diente31 = tk.PhotoImage(file="./src_s/SegundoMolar_D_S.png")
        self.dientes.append(diente31)
        diente32 = tk.PhotoImage(file="./src_s/TercerMolar_D_S.png")
        self.dientes.append(diente32)
        self.Iniciar_Dentadura_Sup()

    def actualizar(self):
        self.canvas.delete("all")
        self.Dientes = vars.Dientes
        self.Iniciar_Dentadura_Sup()

    def Iniciar_Dentadura_Sup(self):

        self.canvas.create_image(0, 0, image=fondo, anchor="nw")
        
        for element in self.Dientes:

            if(element == 17):

                self.canvas.create_image(
                    self.pos_x_ini, self.pos_y_ini, image=self.dientes[0], anchor="nw")

            elif(element == 18):

                self.canvas.create_image(
                    self.pos_x_ini, self.pos_y_ini-100, image=self.dientes[1], anchor="nw")

            elif(element == 19):

                self.canvas.create_image(
                    self.pos_x_ini+15, self.pos_y_ini-188, image=self.dientes[2], anchor="nw")

            elif(element == 20):

                self.canvas.create_image(
                    self.pos_x_ini+40, self.pos_y_ini-275, image=self.dientes[3], anchor="nw")

            elif(element == 21):

                self.canvas.create_image(
                    self.pos_x_ini+65, self.pos_y_ini-340, image=self.dientes[4], anchor="nw")

            elif(element == 22):

                self.canvas.create_image(
                    self.pos_x_ini+115, self.pos_y_ini-402, image=self.dientes[5], anchor="nw")

            elif(element == 23):

                self.canvas.create_image(
                    self.pos_x_ini+166, self.pos_y_ini-455, image=self.dientes[6], anchor="nw")

            elif(element == 24):

                self.canvas.create_image(
                    self.pos_x_ini+250, self.pos_y_ini-494, image=self.dientes[7], anchor="nw")

            elif(element == 25):

                self.canvas.create_image(
                    self.pos_x_ini+355, self.pos_y_ini-480, image=self.dientes[8], anchor="nw")

            elif(element == 26):

                self.canvas.create_image(
                    self.pos_x_ini+440, self.pos_y_ini-465, image=self.dientes[9], anchor="nw")

            elif(element == 27):

                self.canvas.create_image(
                    self.pos_x_ini+495, self.pos_y_ini-425, image=self.dientes[10], anchor="nw")

            elif(element == 28):

                self.canvas.create_image(
                    self.pos_x_ini+520, self.pos_y_ini-346, image=self.dientes[11], anchor="nw")

            elif(element == 29):

                self.canvas.create_image(
                    self.pos_x_ini+545, self.pos_y_ini-280, image=self.dientes[12], anchor="nw")

            elif(element == 30):

                self.canvas.create_image(
                    self.pos_x_ini+552, self.pos_y_ini-200, image=self.dientes[13], anchor="nw")

            elif(element == 31):

                self.canvas.create_image(
                    self.pos_x_ini+548, self.pos_y_ini-102, image=self.dientes[14], anchor="nw")

            elif(element == 32):

                self.canvas.create_image(
                    self.pos_x_ini+542, self.pos_y_ini-5, image=self.dientes[15], anchor="nw")