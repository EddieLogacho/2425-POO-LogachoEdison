import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar  # Necesitas instalar tkcalendar: pip install tkcalendar

class EventManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Eventos")

        # Frame para la lista de eventos
        self.event_frame = ttk.Frame(root)
        self.event_frame.pack(padx=10, pady=10)

        # TreeView para mostrar los eventos
        self.event_tree = ttk.Treeview(self.event_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.event_tree.heading("Fecha", text="Fecha")
        self.event_tree.heading("Hora", text="Hora")
        self.event_tree.heading("Descripción", text="Descripción")
        self.event_tree.pack()

        # Frame para la entrada de datos
        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(padx=10, pady=10)

        # Calendario para seleccionar la fecha
        ttk.Label(self.input_frame, text="Seleccione la fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.cal = Calendar(self.input_frame, selectmode="day", year=2025, month=3, day=19)
        self.cal.grid(row=1, column=0, padx=5, pady=5)

        # Campo de entrada para la hora
        ttk.Label(self.input_frame, text="Hora:").grid(row=2, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.input_frame)
        self.time_entry.grid(row=3, column=0, padx=5, pady=5)

        # Campo de entrada para la descripción
        ttk.Label(self.input_frame, text="Descripción:").grid(row=4, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.input_frame)
        self.desc_entry.grid(row=5, column=0, padx=5, pady=5)

        # Frame para los botones
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(padx=10, pady=10)

        # Botones para agregar, eliminar y salir
        ttk.Button(self.button_frame, text="Agregar Evento", command=self.add_event).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(self.button_frame, text="Eliminar Evento Seleccionado", command=self.delete_event).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.button_frame, text="Salir", command=root.quit).grid(row=0, column=2, padx=5, pady=5)

    def add_event(self):
        # Obtener la fecha seleccionada del calendario
        date = self.cal.get_date()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        # Validar que todos los campos estén completos
        if date and time and desc:
            # Agregar el evento a la lista (TreeView)
            self.event_tree.insert("", "end", values=(date, time, desc))
            # Limpiar los campos de entrada después de agregar el evento
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            # Mostrar un mensaje de advertencia si algún campo está vacío
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")

    def delete_event(self):
        # Obtener el evento seleccionado en la lista
        selected_item = self.event_tree.selection()
        if selected_item:
            # Eliminar el evento seleccionado
            self.event_tree.delete(selected_item)
        else:
            # Mostrar un mensaje de advertencia si no hay ningún evento seleccionado
            messagebox.showwarning("Nada Seleccionado", "Por favor, seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagerApp(root)
    root.mainloop()