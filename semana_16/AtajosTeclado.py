import tkinter as tk
from tkinter import messagebox
#clase padre
class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Tareas")
        self.root.geometry("400x400")

        # Lista para almacenar las tareas
        self.tareas = []

        # Campo de entrada para nueva tarea
        self.entry_tarea = tk.Entry(root, width=40)
        self.entry_tarea.pack(pady=10)
        self.entry_tarea.bind("<Return>", self.agregar_tarea)  # Atajo pulasando la tecla Enter

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.btn_agregar = tk.Button(btn_frame, text="Añadir", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(btn_frame, text="Completar", command=self.marcar_completada)
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(btn_frame, text="Eliminar", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # Asignar atajos de teclado
        self.root.bind("<c>", self.marcar_completada)
        self.root.bind("<d>", self.eliminar_tarea)
        self.root.bind("<Delete>", self.eliminar_tarea)
        self.root.bind("<Escape>", lambda event: root.quit())

    def agregar_tarea(self, event=None):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.tareas.append((tarea, False))  # False indica que no está completada
            self.listbox.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

    def marcar_completada(self, event=None):
        try:
            seleccion = self.listbox.curselection()[0]
            tarea, completada = self.tareas[seleccion]
            if not completada:
                self.tareas[seleccion] = (f"✔ {tarea}", True)
                self.listbox.delete(seleccion)
                self.listbox.insert(seleccion, f"✔ {tarea}")
            else:
                messagebox.showinfo("Info", "Esta tarea ya está completada.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para completar.")

    def eliminar_tarea(self, event=None):
        try:
            seleccion = self.listbox.curselection()[0]
            self.listbox.delete(seleccion)
            del self.tareas[seleccion]
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
