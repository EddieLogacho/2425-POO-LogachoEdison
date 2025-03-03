import json


# Importamos la librería json para manejar la carga y guardado del inventario en un archivo
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario para almacenar los productos
        self.cargar_inventario()  # Cargar productos al iniciar

    def cargar_inventario(self):
        """Carga los productos desde un archivo JSON"""
        try:
            with open(self.archivo, "r") as f:
                self.productos = json.load(f)
        except FileNotFoundError:
            print("Inventario no encontrado. Se creará un nuevo archivo.")
            self.productos = {}
        except json.decoder.JSONDecodeError:
            print("Error: El archivo JSON está corrupto. Se creará uno nuevo.")
            self.productos = {}

    def guardar_inventario(self):
        """Guarda los productos en un archivo JSON"""
        try:
            with open(self.archivo, "w") as f:
                json.dump(self.productos, f, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario"""
        if producto.id_producto in self.productos:
            print(f"El producto con ID {producto.id_producto} ya existe.")
        else:
            self.productos[producto.id_producto] = {
                "nombre": producto.nombre,
                "cantidad": producto.cantidad,
                "precio": producto.precio
            }
            print(f"Producto {producto.id_producto} agregado.")
            self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario"""
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto {id_producto} eliminado.")
            self.guardar_inventario()
        else:
            print(f"El producto {id_producto} no existe en el inventario.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto"""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto]["cantidad"] = cantidad
            if precio is not None:
                self.productos[id_producto]["precio"] = precio
            print(f"Producto {id_producto} actualizado.")
            self.guardar_inventario()
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario"""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for id_producto, info in self.productos.items():
                print(f"ID: {id_producto}, Nombre: {info['nombre']}, Cantidad: {info['cantidad']}, Precio: {info['precio']}")

    def menu(self):
        """Muestra el menú de opciones para gestionar el inventario"""
        while True:
            print("\n1_ Agregar producto\n2_ Eliminar producto\n3_ Actualizar producto\n4_ Mostrar inventario\n5_ Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_producto = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad del producto: "))
                precio = float(input("Precio del producto: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                self.agregar_producto(producto)

            elif opcion == "2":
                id_producto = input("ID del producto que desea eliminar: ")
                self.eliminar_producto(id_producto)

            elif opcion == "3":
                id_producto = input("ID del producto que desea actualizar: ")
                cantidad = input("Nueva cantidad del producto (dejar en blanco si no desea cambiar): ")
                precio = input("Nuevo precio del producto (dejar en blanco si no desea cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                self.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == "4":
                self.mostrar_inventario()

            elif opcion == "5":
                print("Guardando inventario y saliendo...")
                self.guardar_inventario()
                break

if __name__ == "__main__":
    inventario = Inventario()
    inventario.menu()