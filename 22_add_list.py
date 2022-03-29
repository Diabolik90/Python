# En este segundo ejercicio, tendréis que crear una interfaz sencilla
# la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import ttk

def open_window(w):
    # Add to list and reset entry
    def save(event):
        size = list_box.size()
        if size > 8:
            list_box.delete(0)
        list_box.insert(size, texto.get())
        list_entry.delete(0, "end")

    # reset list box
    def reset(event):
        list_box.delete(0, "end")
        result_lbl.config(text='')

    # show the selection
    def select(event):
        text = event.widget.get('anchor')
        if text == '':
            result_lbl.config(text=f'No has seleccionado nada')
        else:
            result_lbl.config(text=f'Has seleccionado\n"{text}"')

    # close window
    def close_window(event):
        w.quit()

    w.columnconfigure(0, weight=1)
    w.columnconfigure(0, weight=7)

    # Title
    title_lbl = tkinter.Label(w, text='Añadir a la lista', width=20, height=1)
    title_lbl.grid(column=0, row=0, padx=0, pady=5)

    # Entry word
    texto = tkinter.StringVar()
    list_entry = ttk.Entry(w, textvariable=texto, width=20)
    list_entry.grid(column=0, row=1, padx=0)

    # Button entry
    button_entry = tkinter.Button(w, text='Save')
    button_entry.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)
    button_entry.bind('<Button-1>', save)

    # Enter Key with pad
    w.bind('<Return>', save)

    # Button reset
    button_reset = tkinter.Button(w, text='Reset')
    button_reset.grid(column=0, row=2, sticky=tkinter.E, padx=10, pady=5)
    button_reset.bind('<Button-1>', reset)

    # List Title
    list_title_lbl = tkinter.Label(w, text='Lista:', width=20, height=1)
    list_title_lbl.grid(column=0, row=3, padx=0)

    # List
    lista_items = tkinter.StringVar()
    list_box = tkinter.Listbox(w, width=20, height=10, listvariable=lista_items)
    list_box.grid(column=0, row=4, padx=0)
    list_box.bind('<<ListboxSelect>>', select)

    # Result
    result_lbl = tkinter.Label(w)
    result_lbl.grid(column=0, row=5, padx=0, pady=10)

    # Exit
    button_exit = tkinter.Button(w, text='Close')
    button_exit.grid(column=0, row=6, pady=5)
    button_exit.bind('<Button-1>', close_window)



def main():
    # create window
    window = tkinter.Tk()

    # program
    open_window(window)

    # update
    window.mainloop()



if __name__ == '__main__':
    main()