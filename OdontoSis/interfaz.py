from variables import VarGlo
from PIL import Image
from tkinter import ttk
import ctypes
from PIL import ImageTk as itk
from tkinter.font import Font

resolucion = ctypes.windll.user32 
width = resolucion.GetSystemMetrics(0)
height = resolucion.GetSystemMetrics(1)

#locaciones
mitad_x = 470
primer_diente_y = 182
segundo_diente_iz_y = 305
segundo_diente_de_y = 289

#Terceros
tercero_primer_iz = (188,426)
tercero_segundo_iz = (206,421)
tercero_primer_de = (732,405)
tercero_segundo_de = (758,410)
#cuartos 
cuarto_primer_iz = (221,523)
cuarto_segundo_iz = (244,506)
cuarto_primer_de = (702,485)
cuarto_segundo_de = (723,496)
#quintos
quinto_primer_iz = (266,598)
quinto_segundo_iz = (297,577)
quinto_primer_de = (674,573)
quinto_segundo_de = (662,566)
#sextos
sexto_primer_iz = (337,642)
sexto_segundo_iz = (344,625)
sexto_primer_de = (613,629)
sexto_segundo_de = (608,617)
#septimos
septimo_primer_iz = (401,659)
septimo_segundo_iz = (403,648)
septimo_primer_de = (543,663)
septimo_segundo_de = (538,634)


class interfaz():

    global var
    var = VarGlo()
    botonActual = 1
    cuadricula = False
    Botones = []
    Imagenes = []

    def cuadriculas(self):
        self.cuadricula = True
        self.canvas.create_line(mitad_x,0,mitad_x,1000)
        self.canvas.create_line(0,primer_diente_y,1000,primer_diente_y)
        self.canvas.create_line(0,segundo_diente_iz_y,mitad_x,segundo_diente_iz_y)
        self.canvas.create_line(940,segundo_diente_de_y,mitad_x,segundo_diente_de_y)
        self.canvas.create_line(tercero_primer_iz,tercero_segundo_iz)

    def cambiar_interfaz(self):
        var = VarGlo()
        for widget in var.frame.winfo_children():
            widget.destroy()
        for widget in var.frame2.winfo_children():
            widget.destroy()
        self.botonActual = 1
        self.opcion = 0

    def elementos_Creados(self, arreglo):
        var = VarGlo()
        var.frame2

    def obtener_posicion(self,centro_x,centro_y):
        if(centro_x<pos_x):
            derecha = True
        else:
            derecha = False
        if(centro_y>pos_y):
            arriba = True
        else:
            arriba = False

        return arriba,derecha

    def existe_diente(self,numero):
        var = VarGlo()
        if(var.Dientes.count(numero)>0):
            return True
        return False

    def no_existe_diente(self,numero):
        var = VarGlo()
        if(var.Dientes.count(numero)>0):
            return False
        return True

    def conf_imagen(self, apoyoa : Image, X, Y,  ancho = -1, alto = -1,rotacion = 0, flip = False,extra :Image = None, separado = 0, vertical = False, Ampliar_separacion = False, crop = (-1,-1,-1,-1)):
        crecimiento = 1
        if(apoyoa.filename == "./src/apoyos/apoyo_oclusal_superior.png"):
            crecimiento = 4/3
        self.permitido = True 
        if(crop != (-1,-1,-1,-1)):    
            apoyoa = apoyoa.crop(crop) 
        if(ancho == -1):
            ancho = apoyoa.width
            
        if(alto == -1):    
            alto = apoyoa.height

        

        medidas = (int(ancho*width*crecimiento/1920),int(alto*height*crecimiento/1080))
        apoyoa = apoyoa.resize(medidas)   
        self.x= int((X)*width/1920)
        self.y= int((Y)*height/1080)
        if(extra is not None):
            extra = extra.resize(medidas)
            apoyoa = self.get_concat_h_cut_center(apoyoa,extra,separacion = separado, ampliar= Ampliar_separacion)
        if (flip):
            apoyoa = apoyoa.transpose(Image.FLIP_LEFT_RIGHT)
        if ( vertical):
            apoyoa = apoyoa.transpose(Image.FLIP_TOP_BOTTOM)     
        dst = apoyoa.rotate(rotacion)
        
        self.tkimage = itk.PhotoImage(dst)
        
    def obtener_diente(self):
        self.diente = -1
        global pos_x
        global pos_y
        pos_x = self.x*1920/width
        pos_y = self.y*1080/height
        var = VarGlo()
        canvas = var.canvas
        if(pos_x < mitad_x):
            if(pos_y<primer_diente_y):
                self.asignar(48,185 ,121)
            elif(pos_y<segundo_diente_iz_y):
                self.asignar(47,184 ,240)
            elif(self.pertenece_cuadrante(tercero_primer_iz,tercero_segundo_iz)): 
                self.asignar(46,190 ,363)
            elif(self.pertenece_cuadrante(cuarto_primer_iz,cuarto_segundo_iz)): 
                self.asignar(45,215 ,467)
            elif(self.pertenece_cuadrante(quinto_primer_iz,quinto_segundo_iz)): 
                self.asignar(44,261 ,545)
            elif(self.pertenece_cuadrante(sexto_primer_iz,sexto_segundo_iz)): 
                self.asignar(43,318 ,606)
            elif(self.pertenece_cuadrante(septimo_primer_iz,septimo_segundo_iz)): 
                self.asignar(42,386 ,637)
            else: 
                self.asignar(41,449 ,648)
        else:
            if(pos_y<primer_diente_y):
                self.asignar(38,769 ,117)
            elif(pos_y < segundo_diente_de_y):
                self.asignar(37,772 ,230)  
            elif(self.pertenece_cuadrante(tercero_primer_de,tercero_segundo_de)): 
                self.asignar(36,752 ,351)
            elif(self.pertenece_cuadrante(cuarto_primer_de,cuarto_segundo_de)): 
                self.asignar(35,726 ,442)
            elif(self.pertenece_cuadrante(quinto_primer_de,quinto_segundo_de)): 
                self.asignar(34,689 ,523) 
            elif(self.pertenece_cuadrante(sexto_primer_de,sexto_segundo_de)): 
                self.asignar(33,635 ,593) 
            elif(self.pertenece_cuadrante(septimo_primer_de,septimo_segundo_de)): 
                self.asignar(32,587 ,625)
            else: 
                self.asignar(31,511 ,640)
        return self.diente,self.obtener_posicion(self.centro_x,self.centro_y)

    def get_concat_h_cut_center(self,im1, im2, separacion = 0, ampliar = False):
        if(ampliar):
            dimensiones = (im1.width + im2.width, max(im1.height, im2.height))
        
        print(im1.width + im2.width)
        if(not ampliar):
            im1 = im1.crop((0,0,im1.width/2+separacion,im1.height))
            im2 = im2.crop((im2.width/2,0,im2.width,im2.height))
            dimensiones = (im1.width + im2.width, max(im1.height, im2.height))
        dst = Image.new("RGBA", dimensiones)
        dst.paste(im1,(0,0))
        dst.paste(im2, (im1.width, (im1.height - im2.height) // 2))
        return dst        

    def pertenece_cuadrante(self,v1,v2):
        x1 = v1[0]
        y1 = v1[1]
        x2 = v2[0]
        y2 = v2[1]
        m = (y2-y1)/(x2-x1)
        b = y2-m*x2
        if(self.cuadricula):
            if(x1< mitad_x):
                self.canvas.create_line(0,b,mitad_x,mitad_x*m+b)
            else:
                self.canvas.create_line(mitad_x,mitad_x*m+b,2*mitad_x,(2*mitad_x)*m+b)
        if(pos_y<m*pos_x+b):
            return True
        else:
            return False    

    def asignar(self,diente,x,y):
        self.diente = diente
        dist = 20
        self.centro_y = y
        self.centro_x = x         
        if(self.cuadricula):
            self.canvas.create_line(x-dist,y,x+dist,y,width=5,fill="green")
            self.canvas.create_line(x,y-dist,x,y+dist,width=5,fill="green")


    def crearImagenBoton(self,imagen,imagen_teoria = None,titulo_teoria = None,mensaje = None):
        posicion = self.botonActual
        im1 = Image.open(self.direccionBase+imagen)
        im1 = im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.Imagenes.append(itk.PhotoImage(im1))
        self.Botones.append(ttk.Button())
        self.Botones[self.botonActual-1] = ttk.Button(
            self.frame, image = self.Imagenes[-1], command= lambda : self.Actualizar(posicion,imagen_teoria,titulo_teoria,mensaje))
        self.Botones[self.botonActual-1].grid(column=self.botonActual, row=1, padx=5)
        self.botonActual+=1

    def crear_Borrador_(self):
        im1 = Image.open('./src/borrador.png')
        im1 = im1.resize((var.size, var.size), Image.ANTIALIAS)
        self.Imagenes.append(itk.PhotoImage(im1))
        self.Botones.append(ttk.Button())
        self.Botones[self.botonActual-1] = ttk.Button(
            self.frame, image = self.Imagenes[-1], command= lambda : self.limpiar())
        self.Botones[self.botonActual-1].grid(column=self.botonActual, row=1, padx=5)


    def Actualizar(self,num,imagen_teoria,titulo_teoria,mensaje):
        self.opcion = num
        if(imagen_teoria is not None and titulo_teoria is not None and mensaje is not None):
            self.crear_teoria(imagen_teoria,titulo_teoria,mensaje)

    def crear_teoria(self,imagen,titulo,mensaje):
        self.ancho=int(width/4)
        self.largo=int(3*height/4)
        self.img = Image.open(imagen)
        self.img = self.img.resize((self.ancho, int(13*self.largo/64)), Image.ANTIALIAS)
        self.img = itk.PhotoImage(self.img) 
        self.label = ttk.Label(self.frame, image = self.img).place(x=0,y=int(5*self.largo/8))
        self.tamaño=Font(family="Bahnschrift", size = int(width/100))
        self.fuente=Font(family="Roboto Mono", size = int(width/196))
        self.titulo = ttk.Label(self.frame, font=self.tamaño, text=titulo, width=self.ancho).place(x=19*self.ancho/64,y=55*self.largo/64)
        self.descripcion = ttk.Label(self.frame, font=self.fuente, wraplength= int(13*self.ancho/16), width=self.ancho,justify="center",
        text=mensaje).place(x=11*self.ancho/128,y=58*self.largo/64)    