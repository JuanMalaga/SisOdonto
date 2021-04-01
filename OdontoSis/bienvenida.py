from tkinter import PhotoImage
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as mb
import sys
import os
import main

color = {"celeste": "#88BFF3", "gris": "#93A5B6"}
root = tk.Tk()
root.title("SIDECO")
root.state(newstate = "normal")
root.config(bg="white")
root.resizable(0,0)
root.iconbitmap('./odonto.ico')
root.geometry("679x500+920+380")

# IMAGENES
imagen=tk.PhotoImage(file="./src/caratula.png")
fondo=tk.Label(root, image=imagen).place(x=0,y=0)

# TEXTO CENTRAL
brandLabel = tk.Label(root, text="SISTEMA DE SIMULACIÓN ODONTOLÓGICA", font="Bahnschrift 18", bg="white", fg="black")
brandLabel.place(x=115, y=180)
brandLabel = tk.Label(root, text="V. 1.0", font="Roboto 10", bg="white", fg="black")
brandLabel.place(x=320, y=210)

# USUARIO

usuario=ttk.Entry(root, width=25)
usuario.place(x=170,y=250)

contraseña=ttk.Entry(root, show="*", width=25)
contraseña.place(x=430,y=250)

invitado=ttk.Entry(root, width=32)
invitado.place(x=230,y=300)

label=tk.Label(root, text = "Usuario: ", bg="white", fg="black")
label.place(x=100, y=250)
label=tk.Label(root, text = "Contraseña: ", bg="white", fg="black")
label.place(x=350, y=250)
label=tk.Label(root, text = "Código de Invitado: ", bg="white", fg="black")
label.place(x=100, y=300)
label=tk.Label(root, text = "Solicitar al Administrador", bg="yellow", fg="black")
label.place(x=450, y=300)

# COMBO
combo=ttk.Combobox(root, width=35)
combo["values"]=("Maxilar Superior", "Maxilar Inferior", "Vista Frontal")
combo.place(x=350, y=350)
#combo.current(1)

label=tk.Label(root, text = "Seleccione la vista para iniciar la simulación ", bg="white", fg="black")
label.place(x=100, y=350)

# BOTONES
def salir():
    respuesta = mb.askyesno(
        "Alerta de Salida", "¿Está seguro que salir del programa?")
    if respuesta == True:
        sys.exit()


boton=tk.Button(root, text="Ingresar al Administrador", font="BahnschriftLight 12", bg="gray17", fg="white",
          activebackground="grey17", activeforeground="white", bd=0, command=ingreso)
boton.place(x=350,y=400)

boton=tk.Button(root, text="Ingresar al Sistema", font="BahnschriftLight 12", bg="gray17", fg="white",
          activebackground="grey17", activeforeground="white", bd=0, command=vista)
boton.place(x=190,y=400)

boton=tk.Button(root, text="Salir", font="BahnschriftLight 12", bg="gray17", fg="white",
          activebackground="grey17", activeforeground="white", bd=0, command=salir)
boton.place(x=315,y=450)

root.mainloop()