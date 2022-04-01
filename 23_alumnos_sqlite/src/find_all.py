import tkinter
from tkinter import ttk
from dbk.dbk_page import DBK_Page as DBK
from src.general import dbk_sqlite, table


def get_list(id):
    return dbk_sqlite.findById(id)


# Devuelve el numero de alumnos
def list_size():
    return dbk_sqlite.size()


class FindAll(DBK):

    def update(self, only_window=False):
        def back(event):
            self.window.destroy()

        # Texto
        title = f'Ver todos los {table}'
        title_lbl = ttk.Label(self.window, text=title)
        title_lbl.place(x=10, y=10)

        # Result List Title
        list_title_lbl = tkinter.Label(self.window, text='Resultado:')
        list_title_lbl.place(x=40, y=40)

        # Page Geometry
        height_size = list_size()
        geometry = height_size * 10 + 90
        for i in range(1, height_size):
            geometry += 5
        geometry = '260x' + str(geometry)
        self.window.geometry(geometry)

        # Result List
        lista_items = tkinter.StringVar(self.window)
        list_box = tkinter.Listbox(self.window, width=40, height=height_size, listvariable=lista_items)
        list_box.place(x=5, y=60)

        # Fill List
        result = 1
        limit = height_size
        while result <= limit:
            datos = get_list(result)
            if datos is not None:
                datos = str(datos)
                datos = datos.replace('(', '').replace(')', '').replace(',', "\n").replace("'", '')
                number = datos.split()
                number = int(number[0])
                list_box.insert(number, datos)
            else:
                limit += 1
            result += 1

        ## Back Boton
        back_button = ttk.Button(self.window, text="Atrás")
        back_button.place(x=175, y=10)
        back_button.bind('<Button-1>', back)

        # Enter Key with pad
        self.window.bind('<Return>', back)

        if only_window:
            self.window.mainloop()
