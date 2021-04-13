import tkinter as tk
from PIL import ImageTk, Image
import ctypes

resolucion = ctypes.windll.user32 

root = tk.Tk()

img = Image.open("./src/caratula.png")

w = resolucion.GetSystemMetrics(0)
h = resolucion.GetSystemMetrics(1)

o_size = img.size   #Tamaño original de la imagen
f_size = (w/4, h/4) #Tamaño del canvas donde se mostrará la imagen

factor = min(float(f_size[1])/o_size[1], float(f_size[0])/o_size[0])
width = int(o_size[0] * factor)
height = int(o_size[1] * factor)

rImg= img.resize((width, height), Image.ANTIALIAS)
rImg = ImageTk.PhotoImage(rImg)

canvas = tk.Canvas(root, width=f_size[0], height= f_size[1])
canvas.create_image(f_size[0]/2, f_size[1]/2, anchor=tk.CENTER, image=rImg, tags="img")
canvas.pack(fill=None, expand=False)

root.mainloop()