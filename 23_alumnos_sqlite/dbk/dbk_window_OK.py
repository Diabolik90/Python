# Copyright          2022 DBK. All rights reserved.       ####   ####   #   #
# Author: Davide P. Fragnito <davidepie90@gmail.com>      #   #  #   #  #  #
#                                                         #   #  ####   ###
# Python API (main graphics display)                      #   #  #   #  #  #
#                                                         ####   ####   #   #

import tkinter
from tkinter import ttk
from dbk.dbk_window import DBK_Window as DBK


## Abre una ventana con un mensaje y la opción de cerrar
#
## Crear la ventana
# dbk_window = DBK_Window_OK('Happened successfully!', 'Successfully', '300x100')
#
## Cambiar icono
# dbk_window.icon('img/icon.ico')
#
## Cambiar texto del boton
# dbk_window.botton_ok('Entendido')
#
## Ejecutar la ventana
# dbk_window.update(True)
##
class DBK_Window_OK(DBK):
    window = ''
    text = ''
    ok_button = 'Ok'

    ## Para llamarla, crear la clase
    ## con Texto, Titulo y Dimensiones
    # ejemplo: dbk_window = DBK_Window_OK('Happened successfully!', 'Successfully', '300x100')
    def __init__(self, text, title='DBK', geometry='0'):
        self.window = tkinter.Tk()
        self.window.title(title)
        if geometry != '0':
            self.window.geometry(geometry)
            self.window.resizable(False, False)
        else:
            title_size = (len(title) * 5) + 200
            title_size = round(title_size / 10) * 10
            text_size = (len(text) * 50 / 30) + 276
            text_size = round(text_size / 10) * 10
            if text_size > title_size:
                result = str(text_size)
            else:
                result = str(title_size)
            result += "x100"
            self.window.geometry(result)
        self.text = text
        self.icon('../img/icon.ico')

    ## Cambiar de icono a la ventana
    # ejemplo: dbk_window.icon('img/icon.ico')
    def icon(self, icon):
        self.window.iconbitmap(str(icon))

    ## Si es la unica ventana del programa establecir en True
    # ejemplo: dbk_window.update(True)
    def update(self, only_window=False):
        # Funcion
        def close_window(event):
            self.window.destroy()

        # Opciones del Texto
        text_lbl = tkinter.Label(self.window, text=self.text)
        text_lbl.pack(ipadx=50, ipady=15)

        # Boton OK
        ok_button = ttk.Button(self.window, text=self.ok_button)
        ok_button.pack(ipady=2)
        ok_button.bind('<Button-1>', close_window)

        # Enter Key with pad
        self.window.bind('<Return>', close_window)

        if only_window:
            self.window.mainloop()

    def __del__(self):
        pass

    ## Cambiar texto del boton derecho
    # ejemplo: dbk_window.botton_ok('Entendido')
    def botton_ok(self, text_botton):
        self.ok_button = text_botton
