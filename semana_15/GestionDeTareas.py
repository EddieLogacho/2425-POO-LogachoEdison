import tkinter as tk

def añadir_tarea():
    tarea = entrada.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)

def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        color_actual = lista_tareas.itemcget(indice, 'bg')
        nuevo_color = 'light green' if color_actual != 'light green' else 'SystemWindow'
        lista_tareas.itemconfig(indice, bg=nuevo_color)
    except IndexError:
        pass

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        pass

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Agenda")
ventana.iconbitmap("logo.ico")
ventana.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Marco para botones
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=5)

# Botones
boton_añadir = tk.Button(marco_botones, text="Añadir ", command=añadir_tarea)
boton_marcar = tk.Button(marco_botones, text="Marcar", command=marcar_completada)
boton_eliminar = tk.Button(marco_botones, text="Eliminar", command=eliminar_tarea)

boton_añadir.pack(side=tk.LEFT, padx=5)
boton_marcar.pack(side=tk.LEFT, padx=5)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15, selectbackground='#d9d9d9')
lista_tareas.pack(pady=10)

# Eventos
entrada.bind('<Return>', lambda event: añadir_tarea())
lista_tareas.bind('<Double-Button-1>', lambda event: marcar_completada())

ventana.mainloop()
