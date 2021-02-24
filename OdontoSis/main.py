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
import creador_retenedores
import variables  
from interfaz_fase_1 import inter_1
import orquestador_fases

# configurar la ventana
color = {"celeste": "#88BFF3", "gris": "#93A5B6"}
Ventana_Principal = tk.Tk()
Ventana_Principal.columnconfigure(0, weight=1)
Ventana_Principal.rowconfigure(0, weight=1)
Ventana_Principal.title("SIDECO")
Ventana_Principal.config(bg="#88BFF3")
Ventana_Principal.iconbitmap('./odonto.ico')
Ventana_Principal.geometry("1480x900+550+250")


# Declaracion Elementos de la GUI

canvas = tk.Canvas(Ventana_Principal, width=800, height=700)
canvas.place(x=520, y=160)
frame = Frame(Ventana_Principal)
frame.place(x=150, y=160)
frame2 = Frame(Ventana_Principal, width=352, height=240)
frame2.place(x=150, y=619)

#globalizando para todos los archivos

var = variables.VarGlo()
var.agregar_Interfaz(Ventana_Principal,canvas,frame,frame2)
var.Iniciar_Dentadura()

# Inicializacion de la primera fase
interfaz1 = inter_1()
interfaz1.iniciar_interfaz()

# FASES
fases = orquestador_fases.orquestador()
fases.cambiar()

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
homeLabel = tk.Label(topFrame, text="MAXILAR INFERIOR", font="Bahnschrift 15",
                     bg=color["celeste"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# BOTON DE MENU VERTICAL
navbarBtn = tk.Button(topFrame, image=navIcon,
                      bg=color["celeste"], activebackground=color["celeste"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# NAVBAR VERTICAL
navRoot = tk.Frame(Ventana_Principal, bg="gray17", height=1000, width=150)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15",
         bg=color["gris"], fg="white", height=2, width=300, padx=20).place(x=0, y=0)

# INICIALIZAR Y PARA OPCIONES
y = 80
# OPCIONES
options = ["Guardar Como", "Vista Interna",
           "Vista Frontal", "Herramientas", "Salir"]

# BOTONES DE OPCIONES
for i in range(4):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 12", bg="gray17", fg=color["gris"],
              activebackground="grey17", activeforeground="white", bd=0).place(x=15, y=y)
    y += 40

# BOTON PARA CERRAR MENU VERTICAL
closeBtn = tk.Button(navRoot, image=closeIcon,
                     bg=color["gris"], activebackground=color["gris"], bd=0, command=switch)
closeBtn.place(x=110, y=10)

# CERRAR VENTANA
def salir():
    respuesta = mb.askyesno(
        "Alerta de Salida", "¿Está seguro que salir del programa? Los cambios no guardados serán descartados")
    if respuesta == True:
        sys.exit()


tk.Button(navRoot, text=options[4], font="BahnschriftLight 12", bg="gray17", fg=color["gris"],
          activebackground="grey17", activeforeground="white", bd=0, command=salir).place(x=15, y=y)
# TEXTO CENTRAL
brandLabel = tk.Label(Ventana_Principal, text="SISTEMA DE SIMULACIÓN ODONTOLÓGICA",
                      font="Bahnschrift 30", bg=color["celeste"], fg="black")
brandLabel.place(x=340, y=8)
graficador = creador_dientes.Graficador()
Ventana_Principal.mainloop()


