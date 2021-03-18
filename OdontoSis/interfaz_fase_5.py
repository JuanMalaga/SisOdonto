import tkinter as tk
from PIL import Image
from tkinter import ttk
from creador_conectores_mayores import Graficador_conectores_mayores
from interfaz import interfaz
from variables import VarGlo
class interfaz_fase_5(interfaz):

    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo : tk.PhotoImage
    conectores : tk.PhotoImage = []


    def __init__ (self):
        global graficador 
        global var
        var = VarGlo()
        graficador = Graficador_conectores_mayores()

    def iniciar_interfaz(self):
        self.cambiar_interfaz()
        graficador.crear_botones()
        
    def limpiar(self):
        graficador.limpiar()
        