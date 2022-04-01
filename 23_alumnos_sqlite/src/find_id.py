import tkinter
from tkinter import ttk
from dbk.dbk_page import DBK_Page as DBK
from dbk.dbk_window_OK import DBK_Window_OK
from src.general import dbk_sqlite


# Devuelve la tupla del alumno buscado por ID
def find_by_id(id):
    result = dbk_sqlite.findById(id)
    return result


class FindId(DBK):

    def update(self, only_window=False):
        # Button Functions
        def find(event):
            result = find_by_id(id.get())
            list_box.delete(0, 'end')
            if result is not None:
                result = str(result)
                result = result.replace('(', '').replace(')', '').replace(", ", "\n").replace("'", '').split()
                list_box.delete(0, 'end')
                for i in range(0, 3):
                    list_box.insert(i, result[i])
            else:
                child_window = DBK_Window_OK(f'id {id.get()} no está presente en la base de datos', "No encontrado")
                child_window.update()

        def back(event):
            self.window.destroy()

        ## ID
        id_label = ttk.Label(self.window, text="Insertar ID :")
        id_label.place(x=5, y=5)
        id = tkinter.IntVar(self.window)
        id_entry = ttk.Entry(self.window, textvariable=id)
        id_entry.place(x=105, y=5)

        # Result List Title
        list_title_lbl = tkinter.Label(self.window, text='Resultado:')
        list_title_lbl.place(x=40, y=40)

        # Result List
        lista_items = tkinter.StringVar(self.window)
        list_box = tkinter.Listbox(self.window, width=22, height=3, listvariable=lista_items)
        list_box.place(x=5, y=60)

        ## Find Boton
        register_button = ttk.Button(self.window, text="Buscar")
        register_button.place(x=155, y=30)
        register_button.bind('<Button-1>', find)

        ## Back Boton
        back_button = ttk.Button(self.window, text="Atrás")
        back_button.place(x=155, y=60)
        back_button.bind('<Button-1>', back)

        # Enter Key with pad
        self.window.bind('<Return>', find)

        if only_window:
            self.window.mainloop()
