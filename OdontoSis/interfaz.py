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

    def obtener_diente(self):
        diente = -1
        
        if(self.y < 490):
            if(self.y<130):
                if (self.x<205):
                    diente = 48
                elif (self.x>536):
                    diente = 38    
            elif(self.y<230):
                if (self.x<205):
                    diente = 47
                elif (self.x>536):
                    diente = 37 
            elif(self.y<345):
                if (self.x<205):
                    diente = 46
                elif (self.x>536):
                    diente = 36 
            elif(self.y<430):
                if (self.x<233):
                    diente = 45
                elif (self.x>536):
                    diente = 35 
            else:
                if(self.x<260):
                    if (self.y-490>-12*self.x/25):
                        diente = 44
                if(self.x>530):
                    if (self.y-463<17*self.x/22):     
                        diente = 34     
                
                    
        else:
            pass

        print(self.x)
        print(self.y)
        print(diente)