import tkinter as tk
from PIL import Image
from tkinter import ttk
import variables


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
        diente1 = tk.PhotoImage(file="./src/TercerMolar_I_I.png")
        self.dientes.append(diente1)
        diente2 = tk.PhotoImage(file="./src/SegundoMolar_I_I.png")
        self.dientes.append(diente2)
        diente3 = tk.PhotoImage(file="./src/PrimerMolar_I_I.png")
        self.dientes.append(diente3)
        diente4 = tk.PhotoImage(file="./src/SegundoPreMolar_I_I.png")
        self.dientes.append(diente4)
        diente5 = tk.PhotoImage(file="./src/PrimerPreMolar_I_I.png")
        self.dientes.append(diente5)
        diente6 = tk.PhotoImage(file="./src/Canino_I_I.png")
        self.dientes.append(diente6)
        diente7 = tk.PhotoImage(file="./src/IncisivoLateral_I_I.png")
        self.dientes.append(diente7)
        diente8 = tk.PhotoImage(file="./src/IncisivoCentral_I_I.png")
        self.dientes.append(diente8)
        diente9 = tk.PhotoImage(file="./src/IncisivoCentral_D_I.png")
        self.dientes.append(diente9)
        diente10 = tk.PhotoImage(file="./src/IncisivoLateral_D_I.png")
        self.dientes.append(diente10)
        diente11 = tk.PhotoImage(file="./src/Canino_D_I.png")
        self.dientes.append(diente11)
        diente12 = tk.PhotoImage(file="./src/PrimerPreMolar_D_I.png")
        self.dientes.append(diente12)
        diente13 = tk.PhotoImage(file="./src/SegundoPreMolar_D_I.png")
        self.dientes.append(diente13)
        diente14 = tk.PhotoImage(file="./src/PrimerMolar_D_I.png")
        self.dientes.append(diente14)
        diente15 = tk.PhotoImage(file="./src/SegundoMolar_D_I.png")
        self.dientes.append(diente15)
        diente16 = tk.PhotoImage(file="./src/TercerMolar_D_I.png")
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
        global var
        var = variables.VarGlo()
        self.Dientes = var.Dientes
        self.pos_x_ini = 78
        self.pos_y_ini = 43
        self.ventana = var.ventana
        self.canvas = var.canvas
        global fondo
        #declarar todas las imagenes
        fondo = tk.PhotoImage(file="./src_s/Base_S.png")
        diente1 = tk.PhotoImage(file="./src_s/TercerMolar_I_S.png")
        self.dientes.append(diente1)
        diente2 = tk.PhotoImage(file="./src_s/SegundoMolar_I_S.png")
        self.dientes.append(diente2)
        diente3 = tk.PhotoImage(file="./src_s/PrimerMolar_I_S.png")
        self.dientes.append(diente3)
        diente4 = tk.PhotoImage(file="./src_s/SegundoPreMolar_I_S.png")
        self.dientes.append(diente4)
        diente5 = tk.PhotoImage(file="./src_s/PrimerPreMolar_I_S.png")
        self.dientes.append(diente5)
        diente6 = tk.PhotoImage(file="./src_s/Canino_I_S.png")
        self.dientes.append(diente6)
        diente7 = tk.PhotoImage(file="./src_s/IncisivoLateral_I_S.png")
        self.dientes.append(diente7)
        diente8 = tk.PhotoImage(file="./src_s/IncisivoCentral_I_S.png")
        self.dientes.append(diente8)
        diente9 = tk.PhotoImage(file="./src_s/IncisivoCentral_D_S.png")
        self.dientes.append(diente9)
        diente10 = tk.PhotoImage(file="./src_s/IncisivoLateral_D_S.png")
        self.dientes.append(diente10)
        diente11 = tk.PhotoImage(file="./src_s/Canino_D_S.png")
        self.dientes.append(diente11)
        diente12 = tk.PhotoImage(file="./src_s/PrimerPreMolar_D_S.png")
        self.dientes.append(diente12)
        diente13 = tk.PhotoImage(file="./src_s/SegundoPreMolar_D_S.png")
        self.dientes.append(diente13)
        diente14 = tk.PhotoImage(file="./src_s/PrimerMolar_D_S.png")
        self.dientes.append(diente14)
        diente15 = tk.PhotoImage(file="./src_s/SegundoMolar_D_S.png")
        self.dientes.append(diente15)
        diente16 = tk.PhotoImage(file="./src_s/TercerMolar_D_S.png")
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
