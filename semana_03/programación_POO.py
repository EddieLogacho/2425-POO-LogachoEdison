print(f"UNIVERSIDAD ESTATAL AMAZÓNICA")
print(f"Carrera de tecnologías de la información")
print(f"Tema: programación POO")
# nombre de la clase clima
class Clima:
    def __init__(self, dia, temperatura):
        self.dia = dia  # Día de la semana (1-7)
        self.temperatura = temperatura  # Temperatura del día

 # Método para mostrar la información del clima de un día específico
    def mostrar_info(self):
        print(f"Día {self.dia}: {self.temperatura}°C")

# Clase que maneja los datos semanales del clima
class SemanaClima:
    def __init__(self):
        self.climas = []  # Lista para almacenar los objetos de Clima

# Método para agregar un día de clima
    def agregar_clima(self, dia, temperatura):
        clima = Clima(dia, temperatura)
        self.climas.append(clima)

    # Método para calcular el promedio semanal de las temperaturas
    def calcular_promedio(self):
        suma_temperaturas = sum([clima.temperatura for clima in self.climas])
        promedio = suma_temperaturas / len(self.climas)
        return promedio

    # Método para mostrar la información de toda la semana
    def mostrar_semana(self):
        for clima in self.climas:
            clima.mostrar_info()


# Función principal
def programa_principal():
    semana = SemanaClima()  # Crear un objeto de la clase SemanaClima

    # Pedir las temperaturas para cada día de la semana
    for i in range(1, 8):
        temperatura = float(input(f"Introduce la temperatura del día {i}: "))
        semana.agregar_clima(i, temperatura)  # Agregar la temperatura al objeto de SemanaClima

    # Mostrar la información de la semana
    print("\nInformación semanal:")
    semana.mostrar_semana()

    # Calcular y mostrar el promedio semanal
    promedio = semana.calcular_promedio()
    print(f"\nEl promedio de temperatura de la semana es: {promedio:.2f} grados.")


# Llamar a la función principal para ejecutar el programa
programa_principal()

