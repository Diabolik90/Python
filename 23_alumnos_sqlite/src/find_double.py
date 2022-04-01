import tkinter
from tkinter import ttk
from dbk.dbk_page import DBK_Page as DBK
from dbk.dbk_window_OK import DBK_Window_OK
from src.general import dbk_sqlite, s_value, t_value

# Devuelve la tupla del alumno buscado por nombre y apellido
def find_double(name, surname):
    result = dbk_sqlite.findDouble(s_value,name,t_value, surname)
    return result

class FindDouble(DBK):

    def update(self, only_window=False):
        # Button Functions
        def find(event):
            result = find_double(name.get(), surname.get())
            list_box.delete(0, 'end')
            if result != None:
                result = str(result)
                result = result.replace('(', '').replace(')', '').replace(", ", "\n").replace("'", '').split()
                list_box.delete(0, 'end')
                for i in range(0,3):
                    list_box.insert(i,result[i])
            else:
                child_window = DBK_Window_OK(f'{name.get()} {surname.get()} no está presente en la base de datos',"No encontrado")
                child_window.update()

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

        # Result List Title
        list_title_lbl = tkinter.Label(self.window, text='Resultado:')
        list_title_lbl.place(x=40, y=60)

        # Result List
        lista_items = tkinter.StringVar(self.window)
        list_box = tkinter.Listbox(self.window, width=22, height=3, listvariable=lista_items)
        list_box.place(x=5, y=85)

        ## Find Boton
        register_button = ttk.Button(self.window, text="Buscar")
        register_button.place(x=155, y=80)
        register_button.bind('<Button-1>', find)

        ## Back Boton
        back_button = ttk.Button(self.window, text="Atrás")
        back_button.place(x=155, y=110)
        back_button.bind('<Button-1>', back)

        # Enter Key with pad
        self.window.bind('<Return>', find)

        if only_window:
            self.window.mainloop()