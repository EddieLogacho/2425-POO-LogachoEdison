print(f"UNIVERSIDAD ESTATAL AMAZÓNICA")
print(f"Carrera de tecnologías de la información")
print(f"Tema: programación tradicional")
# Función para pedir la temperatura de un día específico
def pedir_temperatura(dia):
    temperatura = float(input(f"Introduce la temperatura del día {dia}: "))
    return temperatura
# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio
# Función principal que organiza la ejecución del programa
def programa_principal():
    # Lista para almacenar las temperaturas de la semana
    temperaturas = []

    # Pedir las temperaturas de cada día de la semana (7 días)
    for i in range(1, 8):
        temp = pedir_temperatura(i)
        temperaturas.append(temp)

    # Calcular el promedio de la semana
    promedio = calcular_promedio(temperaturas)

    # Mostrar el resultado
    print(f"Este es el promedio de las temperatura de la semana  {promedio:.2f} grados.")


# esta es la función para ejecutar el programa
programa_principal()