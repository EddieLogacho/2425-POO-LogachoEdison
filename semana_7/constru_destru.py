
class Menu:
    # METODOS CONSTRUCTOR
    def __init__(self, platos , bebidas):
        self.platos = platos
        self.bebidas = bebidas

class Desayuno(Menu):
    def __init__(self,platos , bebidas ,frutas):
        super().__init__(platos , bebidas)
        self.frutas = frutas

    def mostrarInfo(self):
        print(f"Su desayuno es", self.platos)
        print(f"La bebida selecciona es:", self.bebidas)
        print(f"La fruta selecciona es:", self.frutas)

class Almuerzo(Menu):
    def __init__(self,platos , bebidas , postre):
        super().__init__(platos , bebidas)
        self.postre = postre

    def mostrarInfo(self):
        print(f"Su almuerzo  es", self.platos)
        print(f"La bebida seleccionado es:", self.bebidas)
        print(f"El postre seleccionado es:", self.postre)

class Merienda(Menu):
    def __init__(self,platos , bebidas ,  comidaLight):
        super().__init__(platos , bebidas )
        self.comidaLight = comidaLight

    def mostrarInfo(self):
        print(f"Su almuerzo  es", self.platos)
        print(f"La bebida seleccionado es:", self.bebidas)
        print(f"le comida light seleccionada es:", self.comidaLight)

    # METODOS DESTRUCTOR

    def __del__(self):
        print(f"El objeto merienda ha sido eliminado")


plato2=Almuerzo("Encebollado","Jugo de Limón","Flan")
plato2.mostrarInfo()
plato3=Merienda("Sandwich con pan integral","yugur con granola","Manzana con crema de maní")
plato3.mostrarInfo()
plato1=Desayuno("Continental","Jugo de Mora","Papaya")
plato1.mostrarInfo()
plato3.__del__()



