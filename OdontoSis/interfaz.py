from variables import VarGlo


class interfaz():

    def cambiar_interfaz(self):

        var = VarGlo()

        for widget in var.frame.winfo_children():
            widget.destroy()

        for widget in var.frame2.winfo_children():
            widget.destroy()

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

    def obtener_diente(self):
        diente = -1
        global pos_x
        global pos_y
        pos_x = self.x
        pos_y = self.y

        if(pos_x < 384):
            
            if(pos_y<131):
                diente = 48
                centro_x = 136
                centro_y = 76
            elif(pos_y<235):
                diente = 47
                centro_x = 134
                centro_y = 179
            elif(13*pos_y<-3*pos_x+4958): 
                diente = 46
                centro_x = 136
                centro_y = 290
            elif(pos_y<-0.25*pos_x+470.75): 
                diente = 45
                centro_x = 166
                centro_y = 383
            elif(pos_y<-3/7*pos_x+580): 
                diente = 44 
                centro_x = 196
                centro_y = 458
            elif(pos_y<-2.4*pos_x+1171.2): 
                diente = 43
                centro_x = 246
                centro_y = 507
            elif(pos_y<-6*pos_x+2483): 
                diente = 42
                centro_x = 299
                centro_y = 524
            else: 
                diente =41   
                centro_x = 358
                centro_y = 536                             
        else:
            
            if(pos_y<126):
                diente = 38
                centro_x = 632
                centro_y = 75
            elif(pos_y < 228):
                diente = 37  
                centro_x = 641
                centro_y = 174  
            elif(23*pos_y<10*pos_x+1584): 
                diente = 36 
                centro_x = 632
                centro_y = 286
            elif(11*pos_y<4*pos_x+2204): 
                diente = 35 
                centro_x = 602
                centro_y = 375
            elif(pos_y<0.6*pos_x+142.8): 
                diente = 34 
                centro_x = 573
                centro_y = 440
            elif(7*pos_y<10*pos_x-1350): 
                diente = 33 
                centro_x = 525
                centro_y = 492
            elif(pos_y<4.8*pos_x-1585.4): 
                diente = 32 
                centro_x = 467
                centro_y = 517
            else: 
                diente = 31 
                centro_x = 414
                centro_y = 535

        

        print(self.x)
        print(self.y)
        print(diente,self.obtener_posicion(centro_x,centro_y))