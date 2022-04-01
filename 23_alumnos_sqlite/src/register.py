import tkinter
from tkinter import ttk
from dbk.dbk_page import DBK_Page as DBK
from dbk.dbk_window_OK import DBK_Window_OK
from src.general import dbk_sqlite, s_value, t_value

# Añade un nuevo alumno en la base de datos
def register_to_database(name, surname):
    if len(name) > 0 and len(surname) > 0:
        next_id = dbk_sqlite.nextId()
        if dbk_sqlite.verified(s_value, name, t_value, surname):
            child_window = DBK_Window_OK(f'El alumno {name} {surname} ya existe en la base de datos.', "Error")
            child_window.update()
            return False
        else:
            dbk_sqlite.insert(next_id,name,surname)
            return True
    else:
        child_window = DBK_Window_OK(f'El nombre insertado no es valido', "Error")
        child_window.update()
        return False

class Register(DBK):

    def update(self, only_window=False):
        # Button Functions
        def save(event):
            if register_to_database(name.get(), surname.get()):
                self.window.destroy()

        def back(event):
            self.window.destroy()

        ## Name
        name_label = ttk.Label(self.window, text="Nombre :")
        name_label.place(x=5, y=5)
        name = tkinter.StringVar(self.window)
        name_entry = ttk.Entry(self.window, textvariable=name)
        name_entry.place(x=105, y=5)

        ## Apellido
        surname_label = ttk.Label(self.window, text="Apellido :")
        surname_label.place(x=5, y=30)
        surname = tkinter.StringVar(self.window)
        surname_entry = ttk.Entry(self.window, textvariable=surname)
        surname_entry.place(x=105, y=30)

        ## Register Boton
        register_button = ttk.Button(self.window, text="Registrar")
        register_button.place(x=155, y=60)
        register_button.bind('<Button-1>', save)

        ## Back Boton
        back_button = ttk.Button(self.window, text="Atrás")
        back_button.place(x=155, y=90)
        back_button.bind('<Button-1>', back)

        # Enter Key with pad
        self.window.bind('<Return>', save)

        if only_window:
            self.window.mainloop()