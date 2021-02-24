import variables

var = variables.VarGlo()

class inter_1:

    # VARIABLES
    diente1 = tk.IntVar(value=1)
    diente2 = tk.IntVar(value=1)
    diente3 = tk.IntVar(value=1)
    diente4 = tk.IntVar(value=1)
    diente5 = tk.IntVar(value=1)
    diente6 = tk.IntVar(value=1)
    diente7 = tk.IntVar(value=1)
    diente8 = tk.IntVar(value=1)
    diente9 = tk.IntVar(value=1)
    diente10 = tk.IntVar(value=1)
    diente11 = tk.IntVar(value=1)
    diente12 = tk.IntVar(value=1)
    diente13 = tk.IntVar(value=1)
    diente14 = tk.IntVar(value=1)
    diente15 = tk.IntVar(value=1)
    diente16 = tk.IntVar(value=1)
    
    tipos = tk.PhotoImage(file="./src/tipos.png")
    
    def __init__: 
        pass


    def etiquetas():
        tk.Label(frame, text="¿Qué dientes desea eliminar?",
         font="Bahnschrift 10", width=50).pack(anchor="w")
        tk.Checkbutton(frame, text="Tercer Molar Izquierdo (48)", variable=diente1,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente1, 1)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Molar Izquierdo (47)", variable=diente2,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente2, 2)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Molar Izquierdo (46)", variable=diente3,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente3, 3)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Premolar Izquierdo (45)", variable=diente4,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente4, 4)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Premolar Izquierdo (44)", variable=diente5,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente5, 5)).pack(anchor="w")
        tk.Checkbutton(frame, text="Canino (Cúspide) Izquierdo (43)", variable=diente6,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente6, 6)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Lateral Izquierdo (42)", variable=diente7,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente7, 7)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Central Izquierdo (41)", variable=diente8,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente8, 8)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Central Derecho (31)", variable=diente9,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente9, 9)).pack(anchor="w")
        tk.Checkbutton(frame, text="Incisivo Lateral Derecho (32)", variable=diente10,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente10, 10)).pack(anchor="w")
        tk.Checkbutton(frame, text="Canino (Cúspide) Derecho (33)", variable=diente11,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente11, 11)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Premolar Derecho (34)", variable=diente12,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente12, 12)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Premolar Derecho (35)", variable=diente13,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente13, 13)).pack(anchor="w")
        tk.Checkbutton(frame, text="Primer Molar Derecho (36)", variable=diente14,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente14, 14)).pack(anchor="w")
        tk.Checkbutton(frame, text="Segundo Molar Derecho (37)", variable=diente15,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente15, 15)).pack(anchor="w")
        tk.Checkbutton(frame, text="Tercer Molar Derecho (38)", variable=diente16,
                    onvalue=1, offvalue=0, command=lambda: Listener(diente16, 16)).pack(anchor="w")

        monitor = Label(frame)
        monitor.pack()

    
    # OPCIONES DE BORRADO
    
    def Listener(self,variable, n):
        if variable.get():
            var.agregarDiente(n)
        
        else:
            var.eliminarDiente(n)
                
        graficador.actualizar(var.Dientes)
        canvas = graficador.canvas     