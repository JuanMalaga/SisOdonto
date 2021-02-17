import tkinter as tk
from PIL import Image
from tkinter import ttk


class Graficador:
    
    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo : tk.PhotoImage
    dientes: tk.PhotoImage = []
    Retenedores: tk.PhotoImage = []
    actual = "retenedor_Vert_inf_iz"

    def __init__(self, ventana, Dientes):
        self.Dientes = Dientes
        self.pos_x_ini = 78
        self.pos_y_ini = 43
        self.ventana = ventana
        self.canvas = tk.Canvas(self.ventana, width=800, height=700)

        self.Iniciar_Dentadura()

        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)

    def crear_botones(self):
        self.labelframe = ttk.LabelFrame(self.ventana, text="Opciones")
        self.labelframe.grid(column=1, row=0, sticky="w", padx=5, pady=5)
        self.boton1 = ttk.Button(self.labelframe, text="Borrar", command=self.borrar_linea)
        self.boton1.grid(column=0, row=0, padx=5)

        self.boton7 = ttk.Button(self.labelframe, text="Agregar", command=self.Iniciar_Dentadura)
        self.boton7.grid(column=1, row=0, padx=5)

        self.boton2 = ttk.Button(self.labelframe, text="1", command=self.Escoger_retenedor_circular)
        self.boton2.grid(column=0, row=1, padx=5)

        self.boton3 = ttk.Button(self.labelframe, text="2", command=self.Escoger_retenedor_vertical_sup_iz)
        self.boton3.grid(column=0, row=2, padx=5)

        self.boton4 = ttk.Button(self.labelframe, text="3", command=self.Escoger_retenedor_vertical_sup_der)
        self.boton4.grid(column=0, row=3, padx=5)

        self.boton5 = ttk.Button(self.labelframe, text="4", command=self.Escoger_retenedor_vertical_inf_iz)
        self.boton5.grid(column=0, row=4, padx=5)

        self.boton6 = ttk.Button(self.labelframe, text="5", command=self.Escoger_retenedor_vertical_inf_der)
        self.boton6.grid(column=0, row=5, padx=5)

    def borrar_linea(self):
       
        self.canvas.delete("diente1")

    def actualizar(self, Dientes):
        self.Dientes = Dientes
        self.Iniciar_Dentadura()

    def Escoger_retenedor_circular(self):
        self.actual="retenedor_circular"

    def Escoger_retenedor_vertical_sup_iz(self):
        self.actual="retenedor_Vert_sup_iz"

    def Escoger_retenedor_vertical_sup_der(self):
        self.actual="retenedor_Vert_sup_der"

    def Escoger_retenedor_vertical_inf_iz(self):
        self.actual="retenedor_Vert_inf_iz"

    def Escoger_retenedor_vertical_inf_der(self):
        self.actual="retenedor_Vert_inf_der"            

    def left_but_down(self, evento):
            self.x = evento.x
            self.y = evento.y

            if(self.actual == "retenedor_circular"):
                Retenedor = tk.PhotoImage(file="./src/retenedores.png")
                
            elif(self.actual == "retenedor_Vert_sup_iz"):
                Retenedor = tk.PhotoImage(file="./src/Retenedor_Vertica_sup_iz.png")
                
            elif(self.actual == "retenedor_Vert_sup_der"):
                Retenedor = tk.PhotoImage(file="./src/Retenedor_Vertica_sup_der.png")
                
            elif(self.actual == "retenedor_Vert_inf_iz"):
                Retenedor = tk.PhotoImage(file="./src/Retenedor_Vertical_inf_izq.png")

            elif(self.actual == "retenedor_Vert_inf_der"):
                Retenedor = tk.PhotoImage(file="./src/Retenedor_Vertica_inf_der.png")
                        
            self.Retenedores.append(Retenedor) 
            self.canvas.create_image(evento.x-40, evento.y-35, image=self.Retenedores[len(self.Retenedores)-1], anchor="nw", tag="baston")


    def left_but_up(self, evento):
        return

    def Iniciar_Dentadura(self):
        self.canvas.delete("all")

        self.fondo = tk.PhotoImage(file="./src/Base_I_res.png")
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")

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



        for element in self.Dientes:

            if(element == 1):
                
                self.canvas.create_image(self.pos_x_ini, self.pos_y_ini, image=self.dientes[0], anchor="nw")

            elif(element == 2):
                
                self.canvas.create_image(self.pos_x_ini, self.pos_y_ini+100, image=self.dientes[1], anchor="nw")

            elif(element == 3):
                
                self.canvas.create_image(self.pos_x_ini, self.pos_y_ini+200, image=self.dientes[2], anchor="nw")

            elif(element == 4):
                
                self.canvas.create_image(self.pos_x_ini+25, self.pos_y_ini+300, image=self.dientes[3], anchor="nw")

            elif(element == 5):
                
                self.canvas.create_image(self.pos_x_ini+72, self.pos_y_ini+377, image=self.dientes[4], anchor="nw")

            elif(element == 6):
                
                self.canvas.create_image(self.pos_x_ini+127, self.pos_y_ini+437, image=self.dientes[5], anchor="nw")

            elif(element == 7):
                
                self.canvas.create_image(self.pos_x_ini+192, self.pos_y_ini+454, image=self.dientes[6], anchor="nw")

            elif(element == 8):
                
                self.canvas.create_image(self.pos_x_ini+237, self.pos_y_ini+454, image=self.dientes[7], anchor="nw")

            elif(element == 9):
                
                self.canvas.create_image(self.pos_x_ini+287, self.pos_y_ini+462, image=self.dientes[8], anchor="nw")

            elif(element == 10):
                
                self.canvas.create_image(self.pos_x_ini+357, self.pos_y_ini+437, image=self.dientes[9], anchor="nw")

            elif(element == 11):
                
                self.canvas.create_image(self.pos_x_ini+402, self.pos_y_ini+427, image=self.dientes[10], anchor="nw")

            elif(element == 12):
                
                self.canvas.create_image(self.pos_x_ini+462, self.pos_y_ini+377, image=self.dientes[11], anchor="nw")

            elif(element == 13):
                
                self.canvas.create_image(self.pos_x_ini+473, self.pos_y_ini+299, image=self.dientes[12], anchor="nw")

            elif(element == 14):
                
                self.canvas.create_image(self.pos_x_ini+498, self.pos_y_ini+200, image=self.dientes[13], anchor="nw")

            elif(element == 15):
                
                self.canvas.create_image(self.pos_x_ini+508, self.pos_y_ini+92, image=self.dientes[14], anchor="nw")

            elif(element == 16):
                
                self.canvas.create_image(self.pos_x_ini+504, self.pos_y_ini-5, image=self.dientes[15], anchor="nw")
