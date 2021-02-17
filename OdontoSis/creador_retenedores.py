import tkinter as tk
from PIL import Image
from tkinter import ttk


class Graficador_retenedores:
    x = 0
    y = 0
    ventana: tk.Tk
    canvas: tk.Canvas
    Retenedores: tk.PhotoImage = []