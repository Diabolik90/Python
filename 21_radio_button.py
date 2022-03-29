# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
# y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.

import tkinter
from tkinter import ttk

def open_window(w):
    # result selection
    def selection():
        label.config(text=f'Has seleccionado {result.get()}')

    # reset
    def reset():
        result.set(None)
        label.config(text='')

    # columns
    w.columnconfigure(0, weight=1)
    w.columnconfigure(0, weight=4)

    # variable
    result = tkinter.IntVar()

    # result text
    label = ttk.Label(w)
    label.grid(column=0, row=0, padx=1, pady=10)

    # radio buttons
    r1 = ttk.Radiobutton(w, text="Opcion 1", value=1, variable=result, command=selection)
    r2 = ttk.Radiobutton(w, text="Opcion 2", value=2, variable=result, command=selection)
    r3 = ttk.Radiobutton(w, text="Opcion 3", value=3, variable=result, command=selection)
    r1.grid(column=0, row=1, padx=30, pady=5)
    r2.grid(column=0, row=2, padx=30, pady=5)
    r3.grid(column=0, row=3, padx=30, pady=5)

    # button for reset
    button = ttk.Button(w, text='Reiniciar', command=reset)
    button.grid(column=0, row=4, padx=20, pady=10)


def main():
    # create window
    window = tkinter.Tk()

    # program
    open_window(window)

    # update
    window.mainloop()


if __name__ == '__main__':
    main()