import tkinter
from tkinter import ttk
from dbk.dbk_page import DBK_Page as DBK
from dbk.dbk_window_OK import DBK_Window_OK
from src.delete_confirm import DeleteConfirm
from src.general import dbk_sqlite, s_value, t_value

def delete_one(name, surname):
    if len(name) > 0 and len(surname) > 0:
        if dbk_sqlite.verified(s_value, name, t_value, surname):
            confirm_window = DeleteConfirm(f'Quieres eliminar {name} {surname} del la base de datos?','Confirmar')
            datos = dbk_sqlite.findDouble(s_value,name,t_value, surname)
            confirm_window.set_datos(datos)
            confirm_window.update()
        else:
            child_window = DBK_Window_OK(f'El alumno {name} {surname} no está presente en la base de datos.', "Error")
            child_window.update()
    else:
        child_window = DBK_Window_OK(f'El nombre insertado no es valido', "Error")
        child_window.update()

class DeleteOne(DBK):

    def update(self, only_window=False):
        def deleteOne(event):
            delete_one(name.get(), surname.get())

        def back(event):
            self.window.destroy()

        # Texto
        title = f'Insertar los datos del alumno\nque quieres borrar de la base de datos'
        title_lbl = ttk.Label(self.window, text=title)
        title_lbl.place(x=10, y=10)

        ## Name
        name_label = ttk.Label(self.window, text="Nombre :")
        name_label.place(x=5, y=60)
        name = tkinter.StringVar(self.window)
        name_entry = ttk.Entry(self.window, textvariable=name)
        name_entry.place(x=105, y=60)

        ## Apellido
        surname_label = ttk.Label(self.window, text="Apellido :")
        surname_label.place(x=5, y=90)
        surname = tkinter.StringVar(self.window)
        surname_entry = ttk.Entry(self.window, textvariable=surname)
        surname_entry.place(x=105, y=90)

        ## Register Boton
        delete_button = ttk.Button(self.window, text="Borrar")
        delete_button.place(x=155, y=120)
        delete_button.bind('<Button-1>', deleteOne)

        ## Back Boton
        back_button = ttk.Button(self.window, text="Atrás")
        back_button.place(x=155, y=150)
        back_button.bind('<Button-1>', back)

        # Enter Key with pad
        self.window.bind('<Return>', deleteOne)

        if only_window:
            self.window.mainloop()