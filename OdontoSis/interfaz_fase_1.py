import variables
import tkinter as tk
import creador_dientes as crea
from interfaz import interfaz

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
        graficador  =  crea.Graficador()
        graficador_sup = crea.Graficador_Superior()
        var.Iniciar_Dentadura()
        var.Iniciar_Dentadura_Sup()
        graficador.actualizar()
        graficador_sup.actualizar()
        var.canvas = graficador.canvas
        var.canvas = graficador_sup.canvas      

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
        graficador  =  crea.Graficador()
        graficador.actualizar()
        var.canvas = graficador.canvas     