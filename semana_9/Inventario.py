#se a importado eta libreria para verificar si el archivo .txt exixte
import os
#se crea la clase padre
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

    def to_file_string(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_file_string(line):
      #try y except sirbe para manejar errores y evitar que el problema se detenga
        try:
            id_producto, nombre, cantidad, precio = line.strip().split(',')
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            return None

#esta es la clase hija
class Inventario:
    FILE_NAME = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
          # con with open se usa para abrir el archivo de manera eficiente y segura
            with open(self.FILE_NAME, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_file_string())
        except PermissionError:# se utiliza para capturar y manejar un error
            print("Error: No tienes permiso para escribir en el archivo.")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.FILE_NAME):
            return
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    producto = Producto.from_file_string(line)
                    if producto:
                        self.productos.append(producto)
        except FileNotFoundError:# se utiliza para manejar el error que ocurre cuando se intenta accedera un archivo q no exixte
            print("Archivo de inventario no encontrado, iniciando con un inventario vacío.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if any(p.get_id() == id_producto for p in self.productos):
            self.productos = [p for p in self.productos if p.get_id() != id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        nombre = nombre.strip().lower()
        return [p for p in self.productos if nombre in p.get_nombre().strip().lower()]

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    inventario = Inventario()
    while True:
        print("""
        MENU DE INVENTARIO:
        (1) Añadir producto
        (2) Eliminar producto
        (3) Actualizar producto
        (4) Buscar producto por nombre
        (5) Mostrar todos los productos
        (6) Salir
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: ").replace(",", "."))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos en cantidad y precio.")
                continue
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            try:
                nuevo_precio = float(nuevo_precio.replace(",", ".")) if nuevo_precio else None
            except ValueError:
                nuevo_precio = None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            encontrados = inventario.buscar_por_nombre(nombre)
            if encontrados:
                for p in encontrados:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
