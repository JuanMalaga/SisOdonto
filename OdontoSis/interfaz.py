from variables import VarGlo
from PIL import Image
import ctypes
from PIL import ImageTk as itk

resolucion = ctypes.windll.user32 
width = resolucion.GetSystemMetrics(0)
height = resolucion.GetSystemMetrics(1)

#locaciones
mitad_x = 485
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
quinto_primer_de = (665,558)
quinto_segundo_de = (676,562)
#sextos
sexto_primer_iz = (342,645)
sexto_segundo_iz = (352,625)
sexto_primer_de = (622,619)
sexto_segundo_de = (631,627)
#septimos
septimo_primer_iz = (412,674)
septimo_segundo_iz = (414,629)
septimo_primer_de = (555,646)
septimo_segundo_de = (558,661)


class interfaz():

    def cuadriculas(self):
        canvas.create_line(mitad_x,0,mitad_x,1000)
        canvas.create_line(0,primer_diente_y,1000,primer_diente_y)
        canvas.create_line(0,segundo_diente_iz_y,mitad_x,segundo_diente_iz_y)
        canvas.create_line(940,segundo_diente_de_y,mitad_x,segundo_diente_de_y)
        canvas.create_line(tercero_primer_iz,tercero_segundo_iz)

    def cambiar_interfaz(self):
        var = VarGlo()
        for widget in var.frame.winfo_children():
            widget.destroy()
        for widget in var.frame2.winfo_children():
            widget.destroy()
        self.actual = "ninguno"

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

    def conf_imagen(self, apoyoa : Image, X, Y,  ancho = -1, alto = -1,rotacion = 0, flip = False,extra :Image = None, separado = 0):
        crecimiento = 1
        if(apoyoa.filename == "./src/apoyos/apoyo_oclusal_superior.png"):
            crecimiento = 4/3
        self.permitido = True 
        if(ancho == -1 and alto == -1):
            ancho = apoyoa.width
            alto = apoyoa.height
        medidas = (int(ancho*width*crecimiento/1920),int(alto*height*crecimiento/1080))
        apoyoa = apoyoa.resize(medidas)   
        self.x= int((X)*width/1920)
        self.y= int((Y)*height/1080)
        if(extra is not None):
            extra = extra.resize(medidas)
            apoyoa = self.get_concat_h_cut_center(apoyoa,extra,separacion = separado)
        if (flip):
            apoyoa = apoyoa.transpose(Image.FLIP_LEFT_RIGHT)
        dst = apoyoa.rotate(rotacion)
        self.tkimage = itk.PhotoImage(dst)
        
    def obtener_diente(self):
        self.diente = -1
        global pos_x
        global pos_y
        print(self.x)
        print(self.y)
        pos_x = self.x*1980/width
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
                self.asignar(42,376 ,637)
            else: 
                self.asignar(41,439 ,648)
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
                self.asignar(32,572 ,630)
            else: 
                self.asignar(31,501 ,640)
  
        print(self.diente)
        
        return self.diente,self.obtener_posicion(self.centro_x,self.centro_y)

    def get_concat_h_cut_center(self,im1, im2, separacion = 0):
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
        if(pos_y<m*pos_x+b):
            return True
        else:
            return False    

    def asignar(self,diente,x,y):
        self.diente = diente
        self.centro_y = y
        self.centro_x = x         