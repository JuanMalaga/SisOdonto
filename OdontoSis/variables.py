import clases
class VarGlo:
    Dientes = []
    Apoyos : clases.componente_odontologico = []
    Retenedores : clases.componente_odontologico = []
    Conectores_menores : clases.componente_odontologico = []
    Conectores_mayores : clases.componente_odontologico = []
    Bases : clases.componente_odontologico = []
    
    def __init__(self):
        self.Dientes = [1, 4, 5, 2, 3, 10, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
        self.Dientes.sort()
        

    def agregarDiente(self,elemento):
        self.Dientes.append(elemento)
        self.Dientes.sort()

    def agregarRetenedor(self, elemento):
        aux = clases.componente_odontologico(x,y)
        self.Retenedores.append(aux)   

    def agregarApoyo(self, x,y):
        aux = clases.componente_odontologico(x,y)
        self.Apoyos.append(aux)
    
    def agregarConec_Menor(self, x,y):
        aux = clases.componente_odontologico(x,y)
        self.Conectores_menores.append(aux)

    def agregarConec_Mayor(self, x,y):
        aux = clases.componente_odontologico(x,y)
        self.Conectores_mayores.append(aux)

    def agregarBase(self, x,y):
        aux = clases.componente_odontologico(x,y)
        self.Bases.append(aux)
    