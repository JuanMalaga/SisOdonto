



from tkinter import PhotoImage
from tkinter import ttk
import tkinter as tk
import prueba
import clases
import creador_dientes



Dientes = [1,4,5,2,3,10]
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
Ventana_Principal.resizable(0,0)
Ventana_Principal.iconbitmap('./odonto.ico')
Ventana_Principal.geometry("1480x800+500+100")

botonre= tk.Button(Ventana_Principal, text="Restablecer", width=14)
botonre.place(x=1305,y=600)

# TEXTO CENTRAL
brandLabel = tk.Label(Ventana_Principal, text="SISTEMA DE SIMULACIÓN ODONTOLÓGICA", font="Bahnschrift 30", bg=color["celeste"], fg="black")
brandLabel.place(x=360, y=22)

# IMAGEN GENERAL


graficador = prueba.Graficador(Ventana_Principal, Dientes)

canvas = graficador.canvas
canvas.grid(row=3, column=0)


Ventana_Principal.mainloop()