print(f"UNIVERSIDAD ESTATAL AMAZONICA")
print(f"Edison Logacho")
# se crea la clase padre
class Persona:
    def __init__(self, nombre,edad,sexo):#metodo constructor
        self.__nombre = nombre #definir atributos agregando"__"no se va acceder directamente
        self.edad = edad #definir atributos.
        self.sexo = sexo #definir atributos
        #encapsulamiento
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre

        #creamos los metodos
    def mostrarInfo(self):
        print("El nombre es: ",self.get_nombre())
        print("El edad es: ",self.edad)
        print("El sexo es: ",self.sexo)
class Empleado(Persona):#esta es la clase hija y heredara de la clase padre
    def __init__(self, nombre,edad,sexo,cargo, hijos):#heredo todos los atributos de la clase padre y se agrego cargo y telefono
        super().__init__(nombre,edad,sexo)
        self.cargo = cargo
        self.hijos = hijos
    #creamos el metodo
    def mostrarInfo(self):
        super().mostrarInfo()
        print("El cargo es: ",self.cargo)
        print("Cuantos hijos tiene: ",self.hijos)

class Cliente(Persona):  # Clase hija que hereda de Persona
    def __init__(self, nombre, edad, sexo, descuentos):
        super().__init__(nombre, edad, sexo)  # Llama al constructor de Persona
        self.descuentos = descuentos

    def mostrarInfo(self):
        super().mostrarInfo()  # Llama al metodo de la clase padre Persona
        print("Su descuento es: ", self.descuentos)
    

persona1=Empleado("Edison",40,"hombre","Jefe de proyecto",2)
persona1.mostrarInfo()
#creamos un objeto de la clase padre
persona2=Persona("Cristina",37,"femenino")
persona2.mostrarInfo()
persona3=Cliente("Christian",20,"masculino","30%")
persona3.mostrarInfo()








