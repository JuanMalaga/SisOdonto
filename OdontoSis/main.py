from tkinter import PhotoImage
from tkinter import ttk
import tkinter as tk
from tkinter import Frame, Button, Label
from tkinter import messagebox as mb
from tkinter.font import Font
import sys
import variables  
from interfaz_fase_1 import inter_1
import orquestador_fases
import interfaz_fase_1
import ctypes
from PIL import ImageTk, Image

resolucion = ctypes.windll.user32 
global var
var = variables.VarGlo()

# configurar la ventana
color = {"celeste": "#88BFF3", "gris": "#93A5B6"}
Ventana_Principal = tk.Tk()
Ventana_Principal.title("SIDECO")
#Ventana_Principal.resizable(0,0)
Ventana_Principal.config(bg="#88BFF3")
Ventana_Principal.iconbitmap('./odonto.ico')
# CENTRALIZANDO VENTANA
width = resolucion.GetSystemMetrics(0)
height = resolucion.GetSystemMetrics(1)
#Ventana_Principal.geometry("600x900+550+150")
Ventana_Principal.geometry(f"{int(9*width/32)}x{int(height/2.9)}+{int(3*width/8)}+{int(height/4)}")
print(width,height)
#imagenes 
navIcon = PhotoImage(file="./src/menu.png")
closeIcon = PhotoImage(file="./src/close.png")
img = Image.open("./src/caratula.png")
original=img.size
nuevo=(width/3.79, height/9.06)

factor = min(float(nuevo[1])/original[1], float(nuevo[0])/original[0])
w = int(original[0] * factor)
h = int(original[1] * factor)

banners= img.resize((w, h), Image.ANTIALIAS)
banners = ImageTk.PhotoImage(banners)

canvas = tk.Canvas(Ventana_Principal, width=nuevo[0], height= nuevo[1])
canvas.create_image(nuevo[0]/2, nuevo[1]/2, anchor=tk.CENTER, image=banners, tags="img")
canvas.pack(fill=None, expand=False)
#banners=tk.PhotoImage(file="./src/caratula.png")

# BOTON ESTADO DEL NAVBAR
btnState = False
combo=ttk.Combobox(Ventana_Principal, width=28)
combo.set("Maxilar Inferior")
# BIENVENIDA
def vista():
    if combo.get() == 'Maxilar Inferior':
        iniciar()
        
    elif combo.get() == 'Maxilar Superior':
       pass
    
def ingreso():
      Ventana_Principal.state(newstate = "normal")
      root.state(newstate = "withdraw")

# CERRAR VENTANA
def salir():
    respuesta = mb.askyesno(
        "Alerta de Salida", "¿Está seguro que salir del programa? Los cambios no guardados serán descartados")
    if respuesta == True:
        sys.exit()


    # BOTONES
def salirP():
    respuesta = mb.askyesno(
        "Alerta de Salida", "¿Está seguro que salir del programa?")
    if respuesta == True:
        sys.exit()

# guardar
def guardar():
    var.Guardar_archivo()

def precarga():
    # TEXTO CENTRAL
    tamaño=Font(family="Bahnschrift", size = int(width/142.23))
    version=Font(family="Roboto", size = int(width/220))
    brandLabel = tk.Label(Ventana_Principal, text="SISTEMA DE SIMULACIÓN ODONTOLÓGICA", font=tamaño, bg="#88BFF3", fg="black")
    brandLabel.place(x=int(width/22.26), y=int(height/8))
    brandLabel = tk.Label(Ventana_Principal, text="V. 1.0", font=version, bg="#88BFF3", fg="black")
    brandLabel.place(x=int(width/8), y=int(height/6.86))

    # USUARIO
    letra=Font(family="Bahnschrift", size = int(width/213.3))
    solicitud=Font(family="Bahnschrift", size = int(width/284.5))

    usuario=ttk.Entry(Ventana_Principal, width=int(width/140), font=letra)
    usuario.place(x=int(width/15),y=int(height/5.76), height=int(height/65.46))

    contraseña=ttk.Entry(Ventana_Principal, show="*", width=int(width/161), font=letra)
    contraseña.place(x=int(width/5.7),y=int(height/5.76), height=int(height/65.46))

    invitado=ttk.Entry(Ventana_Principal, width=int(width/120), font=letra)
    invitado.place(x=int(width/10.24),y=int(height/4.8), height=int(height/65.46))

    label=tk.Label(Ventana_Principal, text = "Usuario: ", bg="#88BFF3", fg="black", font=letra)
    label.place(x=int(width/25.6), y=int(height/5.83))
    label=tk.Label(Ventana_Principal, text = "Contraseña: ", bg="#88BFF3", fg="black", font=letra)
    label.place(x=int(width/7.53), y=int(height/5.83))
    label=tk.Label(Ventana_Principal, text = "Código de Invitado: ", bg="#88BFF3", fg="black", font=letra)
    label.place(x=int(width/25.6), y=int(height/4.85))
    label=tk.Label(Ventana_Principal, text = "Solicitar al Administrador", bg="yellow", fg="black", font=solicitud)
    label.place(x=int(width/5.6), y=int(height/4.8))

    # COMBO
    combo["values"]=("Maxilar Superior", "Maxilar Inferior", "Vista Frontal")
    combo.place(x=int(width/6.43), y=int(height/4.11), height=int(height/65.46))
    #combo.current(1)

    label=tk.Label(Ventana_Principal, text = "Seleccione la vista inicial para simular: ", bg="#88BFF3", fg="black"
            , font=letra)
    label.place(x=int(width/25.6), y=int(height/4.15))

    boton=tk.Button(Ventana_Principal, text="Ingresar al Administrador", font=letra, bg="gray17", fg="white",
            activebackground="grey17", activeforeground="white", bd=0, command=ingreso)
    boton.place(x=int(width/7.32),y=int(height/3.6))

    boton=tk.Button(Ventana_Principal, text="Ingresar al Sistema", font=letra, bg="gray17", fg="white",
            activebackground="grey17", activeforeground="white", bd=0, command=vista)
    boton.place(x=int(width/13.48),y=int(height/3.6))

    boton=tk.Button(Ventana_Principal, text="Salir", font=letra, bg="gray17", fg="white",
            activebackground="grey17", activeforeground="white", bd=0, command=salirP)
    boton.place(x=int(width/8.13),y=int(height/3.2))

def iniciar():
    for widget in Ventana_Principal.winfo_children():
        widget.destroy()
    Ventana_Principal.geometry(f"1365x900+{int(width/4)}+{int(height/8)}")
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
    options = ["Guardar Como", "Maxilar Superior",
            "Maxilar Inferior", "Herramientas", "Salir"]

    # BOTONES DE OPCIONES

    for i in range(4):
        tk.Button(navRoot, text=options[i], font="BahnschriftLight 12" , bg="gray17", fg=color["gris"],
                activebackground="grey17", activeforeground="white", bd=0).place(x=15, y=y)
        y += 40


        
    # BOTON PARA CERRAR MENU VERTICAL
    closeBtn = tk.Button(navRoot, image=closeIcon,
                        bg=color["gris"], activebackground=color["gris"], bd=0, command=switch)
    closeBtn.place(x=110, y=10)

    tk.Button(navRoot, text=options[4], font="BahnschriftLight 12", bg="gray17", fg=color["gris"],
          activebackground="grey17", activeforeground="white", bd=0, command=salir).place(x=15, y=y)


    tk.Button(navRoot, text=options[0], font="BahnschriftLight 12", bg="gray17", fg=color["gris"],
            activebackground="grey17", activeforeground="white", bd=0, command= guardar).place(x=15, y=80)

    # TEXTO CENTRAL
    brandLabel = tk.Label(Ventana_Principal, text="SISTEMA DE SIMULACIÓN ODONTOLÓGICA",
                        font="Bahnschrift 30", bg=color["celeste"], fg="black")
    brandLabel.place(x=340, y=8)
    graficador = interfaz_fase_1.Graficador()

    tk.Button(navRoot, text=options[1], font="BahnschriftLight 12", bg="gray17", fg=color["gris"],
          activebackground="grey17", activeforeground="white", bd=0).place(x=15, y=120)
    

precarga()
Ventana_Principal.mainloop()



