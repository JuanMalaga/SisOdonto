from variables import VarGlo
class interfaz():

    def cambiar_interfaz (self):
        
        var = VarGlo()
        
        for widget in var.frame.winfo_children():
            widget.destroy()
            
        for widget in var.frame2.winfo_children():
            widget.destroy()

    def elementos_Creados(self,arreglo):
        var= VarGlo()
        var.frame2