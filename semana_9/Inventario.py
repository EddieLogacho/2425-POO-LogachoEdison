print("UNIVERSIDAD ESTATAL AMAZÓNICA".center(50,'-'))
print(' Eddie Logacho --> POO '.center(50,'*'))
#creamos la clase Padre
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
#con el getter vamos a acceder a los atributos
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio
#con el Setter nos permite modificar el valor de un atributo de manera controlada.
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# se crea la clase hija
class Inventario:
    def __init__(self):
        self.productos = []

    # se crea una función para agregar los productos
    def agregar_producto(self, producto):
        # 'any' sirbe para verificar si ya existe un producto en el inventario con el mismo
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            #con 'append' agrega un nuevo elemento a la lista.
            self.productos.append(producto)
            print("Producto agregado exitosamente.")

    # se crea una función para eliminar los productos
    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado exitosamente.")

    # se crea una función para actualizar los productos
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

# Se crea el menu de opciones que va mostrar en pantalla
def menu():
    inventario = Inventario()
    while True:
        print("""
        Menu de inventario:
        (1) Añadir producto
        (2) Eliminar producto
        (3) Actualizar producto
        (4) Buscar producto por nombre
        (5) Mostrar todos los productos
        (6) Salir
        """)
# aqui el usuario va a seleccionar la opcion requerida
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
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
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

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

#asegura que el código dentro de ese bloque se ejecute solo cuando el archivo se ejecute directamente, no cuando se importe como módulo en otro archivo
if __name__ == "__main__":
    menu()
