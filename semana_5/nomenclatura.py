# el programa trata de calcular el area del rectángulo
# creamos las variables que nos permitan almacenar la base y la altura
# se crea la funcion snake_case como se pide en el deber
def calcular_area(base, altura):
    """Calcula el área de un rectángulo"""
    return base * altura

# declaramos las variables utilizando snake_case
# con el input el usuario digitara los datos
base_rectangulo = float(input("Introduce la base del rectángulo (en metros): "))
altura_rectangulo = float(input("Introduce la altura del rectángulo (en metros): "))

# esta es la formula para calcular el área del rectángulo
area = calcular_area(base_rectangulo, altura_rectangulo)

# se mostraran en pantalla  el resultado
print(f"El área del rectángulo es: {area} metros cuadrados.")