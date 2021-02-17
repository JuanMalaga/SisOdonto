import tkinter as tk
from PIL import Image
from tkinter import ttk


class interfaz_fase_3:

    x = 0
    y = 0
    pos_x_ini = 0
    pos_y_ini = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    fondo : tk.PhotoImage
    Retenedores : tk.PhotoImage = []


    def __init__ (self, ventana, canvas, frame, actual):
        self.ventana = ventana
        self.canvas = canvas


    
        