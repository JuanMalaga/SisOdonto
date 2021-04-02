from tkinter import PhotoImage
from tkinter import messagebox as mb
import tkinter as tk
from tkinter import ttk
import sys

import tkinter as tk

color = {"celeste": "#88BFF3", "gris": "#93A5B6"}
root = tk.Tk()
root.title("SIDECO")
root.config(bg="white")
root.resizable(0,0)
root.iconbitmap('./odonto.ico')
root.geometry("679x500+920+380")
#root.overrideredirect(True)

# IMAGENES
imagen=tk.PhotoImage(file="./src/caratula.png")
fondo=tk.Label(root, image=imagen).place(x=0,y=0)

# TEXTO CENTRAL
brandLabel = tk.Label(root, text="SISTEMA DE SIMULACIÓN ODONTOLÓGICA", font="Bahnschrift 18", bg="white", fg="black")
brandLabel.place(x=115, y=180)
brandLabel = tk.Label(root, text="V. 1.0", font="Roboto 10", bg="white", fg="black")
brandLabel.place(x=320, y=210)

# COMBO
combo=ttk.Combobox(root, width=30)
combo["values"]=("Maxilar Superior", "Maxilar Inferior", "Vista Frontal")
combo.place(x=260, y=250)

label=tk.Label(root, text = "Seleccione la vista para al simulación  ", bg="white", fg="black")
label.place(x=50, y=250)

# BOTONES
    
def salir():
    respuesta = mb.askyesno(
        "Alerta de Salida", "¿Está seguro que salir del programa?")
    if respuesta == True:
        sys.exit()


boton=tk.Button(root, text="Ingresar al Sistema", font="BahnschriftLight 12", bg="gray17", fg="white",
          activebackground="grey17", activeforeground="white", bd=0)
boton.place(x=250,y=300)

boton=tk.Button(root, text="Salir", font="BahnschriftLight 12", bg="gray17", fg="white",
          activebackground="grey17", activeforeground="white", bd=0, command=salir)
boton.place(x=315,y=400)

root.mainloop()