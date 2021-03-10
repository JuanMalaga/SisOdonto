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
        diente17 = tk.PhotoImage(file="./src_S/TercerMolar_I_S.png")
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