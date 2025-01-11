print("UNIVERSIDAD ESTATAL AMAZONICA")
print("Edison Logacho")
# creamos una clase Celular con sus atributos
class Celular:
    def __init__(self, marca, modelo, procesador, precio):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.venta = 0  # Inicializamos las ventas en 0
        self.repara = 0  # Inicializamos las reparaciones en 0
        self.precio = precio  # Agregamos un precio para el celular
# se crea metodos vender ya que esuna tienda de venta
    def vender(self, cantidad):
        """Venta del teléfono."""
        self.venta += cantidad
        print(f"El {self.marca} {self.modelo} se vendió {self.venta} veces hoy.")

# se crea metodos arreglar ya que tambien se repara
    def arreglar(self, cantidad):
        """Arreglar el celular."""
        self.repara += cantidad
        # se imprimira las veces que un celular se reaparado
        print(f"El {self.marca} {self.modelo} se reparó {self.repara} veces hoy.")

    def __str__(self):
        """Se va imprimir el costo del celular."""
        return f"${self.precio}"

# Ejemplo de celulares
mi_celular = Celular('Samsung', 'S23 Ultra', 'Snapdragon', 1200)
mi_celular.vender(0)
mi_celular.arreglar(1)
# se imprimira el valor del celular
print(f'El costo del celular es: {mi_celular} $')