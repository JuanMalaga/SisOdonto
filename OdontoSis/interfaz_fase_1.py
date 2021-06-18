import variables
import tkinter as tk
from interfaz import interfaz
from PIL import Image
from PIL import ImageTk as itk
from tkinter import ttk
from tkinter.font import Font
import ctypes

resolucion = ctypes.windll.user32 
var = variables.VarGlo()
width = resolucion.GetSystemMetrics(0)
height = resolucion.GetSystemMetrics(1)

class inter_1(interfaz):

    # VARIABLES
    
    def __init__(self): 
        self.iniciar_dentadura()
        
    def iniciar_dentadura(self):
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
        self.actual = "ninguno"
        self.iniciar_dentadura()
        self.cambiar_interfaz()

        self.etiquetas()
        #self.tiposD()
        global graficador
        graficador  =  Graficador()
        var.Iniciar_Dentadura()
        graficador.actualizar()

    def iniciar_interfaz_sup(self):
        self.cambiar_interfaz()
        self.etiquetas()
        #self.tiposD()
        graficador_sup = Graficador_Superior()
        var.Iniciar_Dentadura_Sup()
        graficador_sup.actualizar() 
        
    def etiquetas(self):
        tamaño=Font(family="Bahnschrift", size = int(width/100))
        opcion=Font(family="Roboto Mono", size = int(width/160))
        anchura=int(width/4)
        etiqueta=int(3*height/4)
        tk.Label(frame, text="¿Qué dientes desea eliminar?",
         font=tamaño, width=44, height=2).pack(anchor="w")
        tk.Checkbutton(frame, text="Tercer Molar Derecho (48)", variable=self.diente1, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente1, 48)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Molar Derecho (47)", variable=self.diente2, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente2, 47)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Molar Derecho (46)", variable=self.diente3, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente3, 46)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Premolar Derecho (45)", variable=self.diente4, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente4, 45)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Premolar Derecho (44)", variable=self.diente5, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente5, 44)).pack(anchor="w")
        tk.Checkbutton(frame, text="Canino Derecho (43)", variable=self.diente6, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente6, 43)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Lateral Derecho (42)", variable=self.diente7, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente7, 42)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Central Derecho (41)", variable=self.diente8, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente8, 41)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Central Izquierdo (31)", variable=self.diente9, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente9, 31)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Lateral Izquierdo (32)", variable=self.diente10, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente10, 32)).pack(anchor="w")
        tk.Checkbutton(frame, text="Canino Izquierdo (33)", variable=self.diente11, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente11, 33)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Premolar Izquierdo (34)", variable=self.diente12, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente12, 34)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Premolar Izquierdo (35)", variable=self.diente13, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente13, 35)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Molar Izquierdo (36)", variable=self.diente14, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente14, 36)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Molar Izquierdo (37)", variable=self.diente15, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente15, 37)).pack(anchor="w")
        tk.Checkbutton(frame, text="Tercer Molar Izquierdo (38)", variable=self.diente16, font=opcion, padx=anchura/8, pady=etiqueta/128, selectcolor="#68EB6C",
                    onvalue=1, offvalue=0, command=lambda: self.Listener(self.diente16, 38)).pack(anchor="w")
    '''
    def tiposD(self):
        self.tipos = tk.PhotoImage(file="./src/tipos.png")
        imagen = tk.Label(var.frame2, image = self.tipos, width=353, height=240, background="white")
        imagen.pack()
    '''     
    
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
    fondo: itk.PhotoImage
    dientes: itk.PhotoImage = []

    def __init__(self):
        global var
        var = variables.VarGlo()
        self.Dientes = var.Dientes
        self.pos_x_ini = int(15*width/256) #int(width/8) #78
        self.pos_y_ini = int(height/20) #int(11*height/64) #43
        self.ancho = int(width/2)
        self.alto = int(3*height/4)
        self.tmolar_w = int(2*width/23.6)
        self.tmolar_h = int(2*height/14.4)
        self.molar_w = int(2*width/25.6)
        self.molar_h = int(2*height/14.4)
        self.s_premolar_w = int(width/9.8)
        self.s_premolar_h = int(height/7.2)
        self.p_premolar_w = int(width/14)
        self.p_premolar_h = int(height/8)
        self.canino_w = int(width/20)
        self.canino_h = int(height/10.2)
        self.lateral_w = int(width/23)
        self.lateral_h = int(height/10)
        self.incisivo_w = int(width/19)
        self.incisivo_h = int(height/8.2)
        self.d_incisivo_w = int(width/15)
        self.d_incisivo_h = int(height/9.5)
        self.d_lateral_w = int(width/15)
        self.d_lateral_h = int(height/6.5)
        self.d_canino_w = int(width/16)
        self.d_canino_h = int(height/10)
        self.dp_premolar_w = int(width/18)
        self.dp_premolar_h = int(height/9)
        self.ds_premolar_w = int(width/14)
        self.ds_premolar_h = int(height/9)
        self.d_molar_w = int(width/12.8)
        self.d_molar_h = int(height/8)
        self.ventana = var.ventana
        self.canvas = var.canvas
        global fondo
        #declarar todas las imagenes
        fondo = Image.open("./src/Base_I_res2.png")
        fondo_base = fondo.resize((self.ancho, self.alto), Image.ANTIALIAS)
        self.base = itk.PhotoImage(fondo_base)
        #----------------------------------------
        uno = Image.open("./src/dientes/TercerMolar_I_I.png")
        sm_i_diente = uno.resize((self.tmolar_w, self.tmolar_h), Image.ANTIALIAS)
        self.diente1 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente1)
        #----------------------------------------
        dos = Image.open("./src/dientes/SegundoMolar_I_I.png")
        sm_i_diente = dos.resize((self.molar_w, self.molar_h), Image.ANTIALIAS)
        self.diente2 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente2)
        #----------------------------------------
        tres = Image.open("./src/dientes/PrimerMolar_I_I.png")
        sm_i_diente = tres.resize((self.molar_w, self.molar_h), Image.ANTIALIAS)
        self.diente3 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente3)
        #----------------------------------------
        cuatro = Image.open("./src/dientes/SegundoPreMolar_I_I.png")
        sm_i_diente = cuatro.resize((self.s_premolar_w, self.s_premolar_h), Image.ANTIALIAS)
        self.diente4 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente4)
        #----------------------------------------
        cinco = Image.open("./src/dientes/PrimerPreMolar_I_I.png")
        sm_i_diente = cinco.resize((self.p_premolar_w, self.p_premolar_h), Image.ANTIALIAS)
        self.diente5 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente5)
        #----------------------------------------
        seis = Image.open("./src/dientes/Canino_I_I.png")
        sm_i_diente = seis.resize((self.canino_w, self.canino_h), Image.ANTIALIAS)
        self.diente6 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente6)
        #----------------------------------------
        siete = Image.open("./src/dientes/IncisivoLateral_I_I.png")
        sm_i_diente = siete.resize((self.lateral_w, self.lateral_h), Image.ANTIALIAS)
        self.diente7 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente7)
        #----------------------------------------
        ocho = Image.open("./src/dientes/IncisivoCentral_I_I.png")
        sm_i_diente = ocho.resize((self.incisivo_w, self.incisivo_h), Image.ANTIALIAS)
        self.diente8 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente8)
        #----------------------------------------
        nueve = Image.open("./src/dientes/IncisivoCentral_D_I.png")
        sm_i_diente = nueve.resize((self.d_incisivo_w, self.d_incisivo_h), Image.ANTIALIAS)
        self.diente9 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente9)
        #----------------------------------------
        diez = Image.open("./src/dientes/IncisivoLateral_D_I.png")
        sm_i_diente = diez.resize((self.d_lateral_w, self.d_lateral_h), Image.ANTIALIAS)
        self.diente10 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente10)
        #----------------------------------------
        once = Image.open("./src/dientes/Canino_D_I.png")
        sm_i_diente = once.resize((self.d_canino_w, self.d_canino_h), Image.ANTIALIAS)
        self.diente11 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente11)
        #----------------------------------------
        doce = Image.open("./src/dientes/PrimerPreMolar_D_I.png")
        sm_i_diente = doce.resize((self.dp_premolar_w, self.dp_premolar_h), Image.ANTIALIAS)
        self.diente12 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente12)
        #----------------------------------------
        trece = Image.open("./src/dientes/SegundoPreMolar_D_I.png")
        sm_i_diente = trece.resize((self.ds_premolar_w, self.ds_premolar_h), Image.ANTIALIAS)
        self.diente13 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente13)
        #---------------------------------------- 
        catorce = Image.open("./src/dientes/PrimerMolar_D_I.png")
        sm_i_diente = catorce.resize((self.d_molar_w, self.d_molar_h), Image.ANTIALIAS)
        self.diente14 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente14)
        #----------------------------------------
        quince = Image.open("./src/dientes/SegundoMolar_D_I.png")
        sm_i_diente = quince.resize((self.d_molar_w, self.d_molar_h), Image.ANTIALIAS)
        self.diente15 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente15)
        #----------------------------------------
        dieciseis = Image.open("./src/dientes/TercerMolar_D_I.png")
        sm_i_diente = dieciseis.resize((self.d_molar_w, self.d_molar_h), Image.ANTIALIAS)
        self.diente16 = itk.PhotoImage(sm_i_diente)
        self.dientes.append(self.diente16)
        #----------------------------------------
        self.Iniciar_Dentadura()

    def actualizar(self):
        self.canvas.delete("all")
        self.Dientes = var.Dientes
        self.Iniciar_Dentadura()

    def Iniciar_Dentadura(self):
        x=int(width/2)
        y=int(3*height/4)
        self.canvas.create_image(0, 0, image=self.base, anchor="nw")
        
        for element in self.Dientes:

            if(element == 48):

                self.canvas.create_image(
                   self.pos_x_ini-int(width/200), self.pos_y_ini+int(height/512), image=self.dientes[0], anchor="nw")

            elif(element == 47):

                self.canvas.create_image(
                    self.pos_x_ini-int(width/200), self.pos_y_ini+int(height/9), image=self.dientes[1], anchor="nw")

            elif(element == 46):

                self.canvas.create_image(
                    self.pos_x_ini, self.pos_y_ini+int(7*height/32), image=self.dientes[2], anchor="nw")

            elif(element == 45):

                self.canvas.create_image(
                    self.pos_x_ini+16, self.pos_y_ini+int(81*height/256), image=self.dientes[3], anchor="nw")

            elif(element == 44):

                self.canvas.create_image(
                    self.pos_x_ini+int(11*width/256), self.pos_y_ini+int(101*height/256), image=self.dientes[4], anchor="nw")

            elif(element == 43):

                self.canvas.create_image(
                    self.pos_x_ini+int(5*width/64), self.pos_y_ini+int(119*height/256), image=self.dientes[5], anchor="nw")

            elif(element == 42):

                self.canvas.create_image(
                    self.pos_x_ini+int(29*width/256), self.pos_y_ini+int(31*height/64), image=self.dientes[6], anchor="nw")

            elif(element == 41):

                self.canvas.create_image(
                    self.pos_x_ini+int(9*width/64), self.pos_y_ini+int(31*height/64), image=self.dientes[7], anchor="nw")

            elif(element == 31):

                self.canvas.create_image(
                    self.pos_x_ini+int(43*width/256), self.pos_y_ini+int(63*height/128), image=self.dientes[8], anchor="nw")

            elif(element == 32):

                self.canvas.create_image(
                    self.pos_x_ini+int(27*width/128), self.pos_y_ini+int(59*height/128), image=self.dientes[9], anchor="nw")

            elif(element == 33):

                self.canvas.create_image(
                    self.pos_x_ini+int(62*width/256), self.pos_y_ini+int(115*height/256), image=self.dientes[10], anchor="nw")

            elif(element == 34):

                self.canvas.create_image(
                    self.pos_x_ini+int(35*width/128), self.pos_y_ini+int(99*height/256), image=self.dientes[11], anchor="nw")

            elif(element == 35):

                self.canvas.create_image(
                    self.pos_x_ini+int(73*width/256), self.pos_y_ini+int(79*height/256), image=self.dientes[12], anchor="nw")

            elif(element == 36):

                self.canvas.create_image(
                    self.pos_x_ini+int(77*width/256), self.pos_y_ini+int(55*height/256), image=self.dientes[13], anchor="nw")

            elif(element == 37):

                self.canvas.create_image(
                    self.pos_x_ini+int(78*width/256), self.pos_y_ini+int(247*height/(9*256)), image=self.dientes[14], anchor="nw")

            elif(element == 38):

                self.canvas.create_image(
                    self.pos_x_ini+int(78*width/256), self.pos_y_ini+int(height/512), image=self.dientes[15], anchor="nw")

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