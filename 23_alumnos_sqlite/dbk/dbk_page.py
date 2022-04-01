# Copyright          2022 DBK. All rights reserved.       ####   ####   #   #
# Author: Davide P. Fragnito <davidepie90@gmail.com>      #   #  #   #  #  #
#                                                         #   #  ####   ###
# Python API (main graphics display)                      #   #  #   #  #  #
#                                                         ####   ####   #   #

import tkinter
from dbk.dbk_window import DBK_Window as DBK


class DBK_Page(DBK):
    window = ''

    def __init__(self, title='DBK', geometry='0'):
        self.window = tkinter.Tk()
        self.window.title(title)
        if geometry != '0':
            self.window.geometry(geometry)
            self.window.resizable(False, False)
        self.icon('../img/icon.ico')

    ## Cambiar de icono a la ventana
    # ejemplo: dbk_window.icon('img/icon.ico')
    def icon(self, icon):
        self.window.iconbitmap(str(icon))

    def update(self):
        pass

    def __del__(self):
        pass
