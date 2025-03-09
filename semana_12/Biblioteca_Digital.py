import json
import os

class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }

class Usuario:
    def __init__(self, user_id, nombre, libros_prestados=None):
        self.user_id = user_id
        self.nombre = nombre
        self.libros_prestados = libros_prestados if libros_prestados else []

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "nombre": self.nombre,
            "libros_prestados": self.libros_prestados
        }

class Biblioteca:
    def __init__(self, archivo_libros='biblioteca.json', archivo_usuarios='usuarios.json'):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.libros = self.cargar_libros()
        self.usuarios = self.cargar_usuarios()

    def cargar_libros(self):
        try:
            if os.path.exists(self.archivo_libros):
                with open(self.archivo_libros, 'r', encoding='utf-8') as archivo:
                    datos_libros = json.load(archivo)
                    return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
            else:
                print("No se encontró el archivo de libros, creando uno nuevo.")
                return {}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al cargar los libros: {e}")
            return {}

    def guardar_libros(self):
        try:
            with open(self.archivo_libros, 'w', encoding='utf-8') as archivo:
                json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4, ensure_ascii=False)
            print(f"Libros guardados correctamente en {self.archivo_libros}.")
        except Exception as e:
            print(f"Error al guardar los libros: {e}")

    def cargar_usuarios(self):
        try:
            if os.path.exists(self.archivo_usuarios):
                with open(self.archivo_usuarios, 'r', encoding='utf-8') as archivo:
                    datos_usuarios = json.load(archivo)
                    usuarios = {}
                    for user_data in datos_usuarios.values():
                        if 'user_id' in user_data and 'nombre' in user_data:
                            usuarios[user_data['user_id']] = Usuario(user_data['user_id'], user_data['nombre'], user_data.get('libros_prestados', []))
                        else:
                            print(f"Datos incompletos para el usuario: {user_data}")
                    return usuarios
            else:
                print("No se encontró el archivo de usuarios, creando uno nuevo.")
                return {}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al cargar los usuarios: {e}")
            return {}

    def guardar_usuarios(self):
        try:
            with open(self.archivo_usuarios, 'w', encoding='utf-8') as archivo:
                json.dump({usuario.user_id: usuario.to_dict() for usuario in self.usuarios.values()}, archivo, indent=4, ensure_ascii=False)
            print(f"Usuarios guardados correctamente en {self.archivo_usuarios}.")
        except Exception as e:
            print(f"Error al guardar los usuarios: {e}")

    def guardar(self):
        self.guardar_libros()
        self.guardar_usuarios()

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar()

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.user_id] = usuario
        self.guardar()
        print(f"Usuario {usuario.nombre} registrado con éxito.")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for usuario in self.usuarios.values():
                print(f"ID: {usuario.user_id}, Nombre: {usuario.nombre}, Libros Prestados: {', '.join(usuario.libros_prestados) or 'Ninguno'}")

    def prestar_libro(self, user_id, isbn):
        usuario = self.usuarios.get(user_id)
        libro = self.libros.get(isbn)
        if usuario and libro and not libro.prestado:
            libro.prestado = True
            usuario.libros_prestados.append(isbn)
            self.guardar()
            print(f"Libro {isbn} prestado a {usuario.nombre} con éxito.")
        else:
            print("Libro no disponible o usuario no encontrado.")

    def devolver_libro(self, user_id, isbn):
        usuario = self.usuarios.get(user_id)
        libro = self.libros.get(isbn)
        if usuario and libro and libro.prestado and isbn in usuario.libros_prestados:
            libro.prestado = False
            usuario.libros_prestados.remove(isbn)
            self.guardar()
            print(f"Libro {isbn} devuelto por {usuario.nombre} con éxito.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Mostrar Libros\n3. Registrar Usuario\n4. Mostrar Usuarios\n5. Prestar Libro\n6. Devolver Libro\n7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            biblioteca.mostrar_libros()
        elif opcion == '3':
            user_id = input("ID de usuario: ")
            nombre = input("Nombre: ")
            usuario = Usuario(user_id, nombre)
            biblioteca.registrar_usuario(usuario)
        elif opcion == '4':
            biblioteca.mostrar_usuarios()
        elif opcion == '5':
            user_id = input("ID de usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(user_id, isbn)
        elif opcion == '6':
            user_id = input("ID de usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(user_id, isbn)
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()