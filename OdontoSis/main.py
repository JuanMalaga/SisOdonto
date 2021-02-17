from tkinter import PhotoImage
from tkinter import ttk
import tkinter as tk
from tkinter import Frame, Button, Label
from tkinter import messagebox as mb
from tkinter.font import Font
import sys
import prueba
import clases
import creador_dientes

Dientes = [1,4,5,2,3,10,6,7,8,9,11,12,13,14,15,16]
Dientes.sort()

#arreglos
lista = [1, 2.5, 'DevCode', [5,6] ,4]


#configurar la ventana
color = {"celeste": "#88BFF3", "gris": "#93A5B6"}

Ventana_Principal = tk.Tk()

Ventana_Principal.columnconfigure(0, weight=1)
Ventana_Principal.rowconfigure(0,weight=1)
Ventana_Principal.title("SIDECO")
Ventana_Principal.config(bg="#88BFF3")
#Ventana_Principal.resizable(0,0)
Ventana_Principal.iconbitmap('./odonto.ico')
Ventana_Principal.geometry("1480x900+550+250")
Ventana_Principal.overrideredirect(True)
#botonre= tk.Button(Ventana_Principal, text="Restablecer", width=14)
#botonre.place(x=1305,y=600)

# IMAGEN GENERAL

graficador = prueba.Graficador(Ventana_Principal, Dientes)

canvas = graficador.canvas
canvas.place(x=520, y=160)

# FASES 
btn_font = Font(family="Roboto Mono", size=12)

def on_enter(e):
    botonre1["background"] = "#4dffc3"

def on_leave(e):
    botonre1["background"] = "#4dffc3"

botonre1= tk.Button(Ventana_Principal, text="FASE I\nDIENTES", font=btn_font, bd=0, width=20, overrelief="flat", cursor="hand1", background="#4dffc3",activebackground="#80ffcc")
botonre1.place(x=150,y=80)

botonre1.bind("<Enter>", on_enter)
botonre1.bind("<Leave>", on_leave)

def on_enter(e):
    botonre2["background"] = "#4dffc3"

def on_leave(e):
    botonre2["background"] = "SystemButtonFace"

botonre2= tk.Button(Ventana_Principal, text="FASE II\nAPOYOS", font=btn_font, bd=0, width=20, overrelief="flat", cursor="hand1", activebackground="#80ffcc")
botonre2.place(x=330,y=80)

botonre2.bind("<Enter>", on_enter)
botonre2.bind("<Leave>", on_leave)

def on_enter(e):
    botonre3["background"] = "#4dffc3"

def on_leave(e):
    botonre3["background"] = "SystemButtonFace"

botonre3= tk.Button(Ventana_Principal, text="FASE III\nRETENEDORES", font=btn_font, bd=0, width=20, overrelief="flat", cursor="hand1", activebackground="#80ffcc")
botonre3.place(x=510,y=80)

botonre3.bind("<Enter>", on_enter)
botonre3.bind("<Leave>", on_leave)

def on_enter(e):
    botonre4["background"] = "#4dffc3"

def on_leave(e):
    botonre4["background"] = "SystemButtonFace"

botonre4= tk.Button(Ventana_Principal, text="FASE IV\nCONECTORES MENORES", font=btn_font, bd=0, width=25, overrelief="flat", cursor="hand1", activebackground="#80ffcc")
botonre4.place(x=690,y=80)

botonre4.bind("<Enter>", on_enter)
botonre4.bind("<Leave>", on_leave)

def on_enter(e):
    botonre5["background"] = "#4dffc3"

def on_leave(e):
    botonre5["background"] = "SystemButtonFace"

botonre5= tk.Button(Ventana_Principal, text="FASE V\nCONECTOR MAYOR", font=btn_font, bd=0, width=22, overrelief="flat", cursor="hand1", activebackground="#80ffcc")
botonre5.place(x=920,y=80)

botonre5.bind("<Enter>", on_enter)
botonre5.bind("<Leave>", on_leave)

def on_enter(e):
    botonre6["background"] = "#4dffc3"

def on_leave(e):
    botonre6["background"] = "SystemButtonFace"

botonre6= tk.Button(Ventana_Principal, text="FASE VI\nBASES (REJILLAS)", font=btn_font, bd=0, width=22, overrelief="flat", cursor="hand1", activebackground="#80ffcc")
botonre6.place(x=1122,y=80)

botonre6.bind("<Enter>", on_enter)
botonre6.bind("<Leave>", on_leave)

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

# OPCIONES DE BORRADO
def Listener(variable, n):
    if variable.get():
        Dientes.append(n)
        Dientes.sort()
        print("esta agregado")
    else:
        if(Dientes.count(n) > 0):
            Dientes.remove(n)
            Dientes.sort()
            print("esta eliminando" )
    graficador.actualizar(Dientes)
    canvas = graficador.canvas

frame = Frame(Ventana_Principal)
frame.place(x=150,y=160)

tk.Label(frame, text="¿Qué dientes desea eliminar?", font="Bahnschrift 10", width=50).pack(anchor="w")
tk.Checkbutton(frame, text="Tercer Molar Izquierdo (48)", variable=diente1, onvalue=1, offvalue=0, command=lambda: Listener(diente1, 1)).pack(anchor="w")
tk.Checkbutton(frame, text="Segundo Molar Izquierdo (47)", variable=diente2, onvalue=1, offvalue=0, command=lambda: Listener(diente2, 2)).pack(anchor="w")
tk.Checkbutton(frame, text="Primer Molar Izquierdo (46)", variable=diente3, onvalue=1, offvalue=0, command=lambda: Listener(diente3, 3)).pack(anchor="w")
tk.Checkbutton(frame, text="Segundo Premolar Izquierdo (45)", variable=diente4, onvalue=1, offvalue=0, command=lambda: Listener(diente4, 4)).pack(anchor="w")
tk.Checkbutton(frame, text="Primer Premolar Izquierdo (44)", variable=diente5, onvalue=1, offvalue=0, command=lambda: Listener(diente5, 5)).pack(anchor="w")
tk.Checkbutton(frame, text="Canino (Cúspide) Izquierdo (43)", variable=diente6, onvalue=1, offvalue=0, command=lambda: Listener(diente6, 6)).pack(anchor="w")
tk.Checkbutton(frame, text="Incisivo Lateral Izquierdo (42)", variable=diente7, onvalue=1, offvalue=0, command=lambda: Listener(diente7, 7)).pack(anchor="w")
tk.Checkbutton(frame, text="Incisivo Central Izquierdo (41)", variable=diente8, onvalue=1, offvalue=0, command=lambda: Listener(diente8, 8)).pack(anchor="w")
tk.Checkbutton(frame, text="Incisivo Central Derecho (31)", variable=diente9, onvalue=1, offvalue=0, command=lambda: Listener(diente9, 9)).pack(anchor="w")
tk.Checkbutton(frame, text="Incisivo Lateral Derecho (32)", variable=diente10, onvalue=1, offvalue=0, command=lambda: Listener(diente10, 10)).pack(anchor="w")
tk.Checkbutton(frame, text="Canino (Cúspide) Derecho (33)", variable=diente11, onvalue=1, offvalue=0, command=lambda: Listener(diente11, 11)).pack(anchor="w")
tk.Checkbutton(frame, text="Primer Premolar Derecho (34)", variable=diente12, onvalue=1, offvalue=0, command=lambda: Listener(diente12, 12)).pack(anchor="w")
tk.Checkbutton(frame, text="Segundo Premolar Derecho (35)", variable=diente13, onvalue=1, offvalue=0, command=lambda: Listener(diente13, 13)).pack(anchor="w")
tk.Checkbutton(frame, text="Primer Molar Derecho (36)", variable=diente14, onvalue=1, offvalue=0, command=lambda: Listener(diente14, 14)).pack(anchor="w")
tk.Checkbutton(frame, text="Segundo Molar Derecho (37)", variable=diente15, onvalue=1, offvalue=0, command=lambda: Listener(diente15, 15)).pack(anchor="w")
tk.Checkbutton(frame, text="Tercer Molar Derecho (38)", variable=diente16, onvalue=1, offvalue=0, command=lambda: Listener(diente16, 16)).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

# IMAGEN DE TIPO DE DIENTES

tipos = tk.PhotoImage(file="./src/tipos.png")
w2 = tk.Label(Ventana_Principal, image=tipos, bg="white", width=352, height=240)
w2.place(x=150,y=619)


# BOTON ESTADO DEL NAVBAR
btnState = False

# IMAGENES
navIcon = PhotoImage(file="./src/menu.png")
closeIcon = PhotoImage(file="./src/close.png")

def switch():
    global btnState
    if btnState is True:
        # ANIMACION DE CERRADO
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # COLORES AL MOMENTO DEL CERRADO
        brandLabel.config(bg=color["celeste"], fg="black")
        homeLabel.config(bg=color["celeste"])
        topFrame.config(bg=color["celeste"])
        Ventana_Principal.config(bg=color["celeste"])

        # BOTON APAGADO
        btnState = False
    else:
        # COLORES DE LA VENTANA DESPUES DE ACCIONAR
        brandLabel.config(bg=color["celeste"], fg="black")
        homeLabel.config(bg=color["celeste"])
        topFrame.config(bg=color["celeste"])
        Ventana_Principal.config(bg=color["celeste"])

        # ANIMACION DEL NAVBAR
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()
 
        # BOTON ENCENDIDO
        btnState = True

# BARRA DE NAVEGACION SUPERIOR
topFrame = tk.Frame(Ventana_Principal, bg=color["celeste"])
topFrame.pack(side="top", fill=tk.X)

# MARCA DE AGUA FO
homeLabel = tk.Label(topFrame, text="MAXILAR INFERIOR", font="Bahnschrift 15", bg=color["celeste"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# BOTON DE MENU VERTICAL
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["celeste"], activebackground=color["celeste"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# NAVBAR VERTICAL
navRoot = tk.Frame(Ventana_Principal, bg="gray17", height=1000, width=150)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["gris"], fg="white", height=2, width=300, padx=20).place(x=0, y=0)

# INICIALIZAR Y PARA OPCIONES
y = 80
# OPCIONES
options = ["Guardar Como", "Vista Interna", "Vista Frontal", "Herramientas", "Salir"]

# BOTONES DE OPCIONES
for i in range(4):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 12", bg="gray17", fg=color["gris"], activebackground="grey17", activeforeground="white", bd=0).place(x=15, y=y)
    y += 40

# BOTON PARA CERRAR MENU VERTICAL
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["gris"], activebackground=color["gris"], bd=0, command=switch)
closeBtn.place(x=110, y=10)

# CERRAR VENTANA
def salir():
        respuesta=mb.askyesno("Alerta de Salida", "¿Está seguro que salir del programa? Los cambios no guardados serán descartados")
        if respuesta==True:
            sys.exit()

tk.Button(navRoot, text=options[4], font="BahnschriftLight 12", bg="gray17", fg=color["gris"], activebackground="grey17", activeforeground="white", bd=0, command=salir).place(x=15,y=y)
# TEXTO CENTRAL
brandLabel = tk.Label(Ventana_Principal, text="SISTEMA DE SIMULACIÓN ODONTOLÓGICA", font="Bahnschrift 30", bg=color["celeste"], fg="black")
brandLabel.place(x=340, y=8)

Ventana_Principal.mainloop()