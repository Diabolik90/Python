from tkinter import ttk
from dbk.dbk_page import DBK_Page as DBK
from src.register import Register
from src.find_id import FindId
from src.find_double import FindDouble
from src.find_all import FindAll
from src.delete_one import DeleteOne

# Open the windows
def open_register():
    page = Register('Registrar','240x120')
    page.update()

def open_find_by_id():
    page = FindId('Buscar por ID','240x120')
    page.update()

def open_find_all():
    page = FindAll('Ver Todos','260x100')
    page.update()

def delete_one():
    page = DeleteOne('Borrar','240x180')
    page.update()

def open_find_double():
    page = FindDouble('Buscar','240x145')
    page.update()

class DBK_Principal(DBK):

    def update(self, only_window=False):
        # Button Functions
        def register(event):
            open_register()

        def findId(event):
            open_find_by_id()

        def findAll(event):
            open_find_all()

        def deleteOne(event):
            delete_one()

        def findDouble(event):
            open_find_double()

        def quitProgram(event):
            self.window.destroy()

        # Texto
        title = 'Ejercicio 1 - Author : Diabolik'
        texto = 'En este ejercicio tendréis que crear una tabla llamada\n"Alumnos" que constará de tres columnas:'
        texto += '\n- la columna id de tipo entero,\n- la columna nombre que será de tipo texto\n- la columna apellido que también será de tipo texto.\n'
        texto += '\nUna vez creada la tabla, tenéis que insertarle datos,\ncomo mínimo tenéis que insertar 8 alumnos a la tabla.\n'
        texto += '\nPor último, tienes que realizar una búsqueda\nde un alumno por nombre y mostrar los datos por consola.'
        # Label
        title_lbl = ttk.Label(self.window, text=title)
        title_lbl.place(x=10, y=10)
        text_lbl = ttk.Label(self.window, text=texto)
        text_lbl.place(x=10, y=40)

        # Register Button
        register_button = ttk.Button(self.window, text="Registrar")
        register_button.place(x=30, y=220)
        register_button.bind('<Button-1>', register)

        # Find Id Button
        find_id_button = ttk.Button(self.window, text="Busca por ID")
        find_id_button.place(x=230, y=220)
        find_id_button.bind('<Button-1>', findId)

        # Find All Button
        find_all = ttk.Button(self.window, text="Ver todos")
        find_all.place(x=30, y=250)
        find_all.bind('<Button-1>', findAll)

        # Delete
        find_all = ttk.Button(self.window, text="Borrar")
        find_all.place(x=230, y=250)
        find_all.bind('<Button-1>', deleteOne)

        # Find Double Button
        find_double = ttk.Button(self.window, text="Buscar por nombre y apellido")
        find_double.place(x=30, y=280)
        find_double.bind('<Button-1>', findDouble)

        # exit Button
        exit_button = ttk.Button(self.window, text="Salir")
        exit_button.place(x=30, y=310)
        exit_button.bind('<Button-1>', quitProgram)

        if only_window:
            self.window.mainloop()