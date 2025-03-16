import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
app = tk.Tk()
app.title('U.E.A')
app.iconbitmap("logo.ico")
app.geometry('500x500')
app.configure(background='gray')
app.config(bd=20)
app.config(relief='ridge')
app.config(cursor='hand2')

# Función para agregar datos a la lista
def agregar_dato():
    dato = campo_texto.get()  # Obtener el texto del campo de entrada
    if dato:  # Verificar que el campo no esté vacío
        lista_datos.insert(tk.END, dato)  # Agregar el dato a la lista
        campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un dato antes de agregar.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Eliminar todos los elementos de la lista


# Etiqueta de instrucción
etiqueta = tk.Label(app, text="Ingresa un dato y presiona 'Agregar':")
etiqueta.pack(pady=10)

# Campo de texto para ingresar datos
campo_texto = tk.Entry(app, width=40)
campo_texto.pack(pady=10)

# Lista para mostrar los datos
lista_datos = tk.Listbox(app, width=50, height=10,)
lista_datos.config(background="#556B2F")
lista_datos.pack(pady=10)

# Botón para agregar datos
boton1 = tk.Button(app, text="Agregar", command=agregar_dato)
boton1.pack(pady=5)

# Botón para limpiar la lista
boton2 = tk.Button(app, text="Limpiar", command=limpiar_lista)
boton2.pack(pady=5)
#ubicacion de los botones
boton1.pack(side=tk.RIGHT, padx=100, pady=50)
boton2.pack(side=tk.LEFT, padx=80, pady=50)

# Iniciar el bucle principal de la aplicación
app.mainloop()
