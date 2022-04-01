# Copyright          2022 DBK. All rights reserved.       ####   ####   #   #
# Author: Davide P. Fragnito <davidepie90@gmail.com>      #   #  #   #  #  #
#                                                         #   #  ####   ###
# Python API (main graphics display)                      #   #  #   #  #  #
#	                                                      ####   ####   #   #

import tkinter
from tkinter import ttk
from dbk.dbk_window_OK import DBK_Window_OK as DBK


## Abre una ventana con un mensaje y la opción de
# volver atras
# ejecutar una función
#
## Cambiar texto del boton izquierdo
# dbk_window.botton_back('Volver')
#
## Ejecutar la ventana
# dbk_window.update(True)
#
## Definir la funcion que quiere ejecutar
# ejemplo: dbk_window.function(): print('Ok')
##
class DBK_Window_BOK(DBK):
    back_button = 'Back'

    ## Si es la unica ventana del programa establecir en True
    # ejemplo: dbk_window.update(True)
    def update(self, only_window=False):
        # Funcion
        def pulse_ok(event):
            self.function()
            self.window.destroy()

        def pulse_back(event):
            self.window.destroy()

        # Opciones del Texto
        text_lbl = tkinter.Label(self.window, text=self.text)
        text_lbl.pack(ipadx=50, ipady=15)

        # Boton BACK
        back_button = ttk.Button(self.window, text=self.back_button)
        back_button.pack(padx=35, ipady=2, side='left')
        back_button.bind('<Button-1>', pulse_back)

        # Boton OK
        ok_button = ttk.Button(self.window, text=self.ok_button)
        ok_button.pack(padx=35, ipady=2, side='right')
        ok_button.bind('<Button-1>', pulse_ok)

        # Enter Key with pad
        self.window.bind('<Return>', pulse_ok)

        if only_window:
            self.window.mainloop()

    ## Cambiar texto del boton izquierdo
    # ejemplo: dbk_window.botton_back('Entendido')
    def botton_back(self, text_botton):
        self.back_button = text_botton

    ## Definir la funcion que quiere ejecutar
    # ejemplo: dbk_window.function(): print('Ok')
    def function(self):
        pass
