from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
from tkinter import PhotoImage
import tkinter as tk
from tkinter import ttk

import tkinter as tk

color = {"celeste": "#88BFF3", "gris": "#93A5B6"}

root = tk.Tk()
root.title("SIDECO")
root.config(bg="#88BFF3")
root.resizable(0,0)
root.iconbitmap('./odonto.ico')
root.geometry("1480x800+500+100")


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
        root.config(bg=color["celeste"])

        # BOTON APAGADO
        btnState = False
    else:
        # COLORES DE LA VENTANA DESPUES DE ACCIONAR
        brandLabel.config(bg=color["celeste"], fg="black")
        homeLabel.config(bg=color["celeste"])
        topFrame.config(bg=color["celeste"])
        root.config(bg=color["celeste"])

        # ANIMACION DEL NAVBAR
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # BOTON ENCENDIDO
        btnState = True

# BARRA DE NAVEGACION SUPERIOR
topFrame = tk.Frame(root, bg=color["celeste"])
topFrame.pack(side="top", fill=tk.X)

# MARCA DE AGUA FO
homeLabel = tk.Label(topFrame, text="FO - UNMSM", font="Bahnschrift 15", bg=color["celeste"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# TEXTO CENTRAL
brandLabel = tk.Label(root, text="SISTEMA DE SIMULACIÓN ODONTOLÓGICA", font="Bahnschrift 30", bg=color["celeste"], fg="black")
brandLabel.place(x=360, y=22)

# CAMBIAR FASES


# BOTON DE MENU VERTICAL
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["celeste"], activebackground=color["celeste"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# NAVBAR VERTICAL
navRoot = tk.Frame(root, bg="gray17", height=1000, width=180)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["gris"], fg="white", height=2, width=300, padx=20).place(x=0, y=0)

# INICIALIZAR Y PARA OPCIONES
y = 80
# OPCIONES
options = ["Guardar Como", "Vista Interna", "Vista Frontal", "Herramientas", "Salir"]

# BOTONES DE OPCIONES
for i in range(5):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 12", bg="gray17", fg=color["gris"], activebackground="grey17", activeforeground="white", bd=0).place(x=20, y=y)
    y += 40

# BOTON PARA CERRAR MENU VERTICAL
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["gris"], activebackground=color["gris"], bd=0, command=switch)
closeBtn.place(x=140, y=10)

root.mainloop()