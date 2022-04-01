from dbk.dbk_window_BOK import DBK_Window_BOK as DBK
from src.general import dbk_sqlite

class DeleteConfirm(DBK):

    datos = ''

    def set_datos(self, datos):
        self.datos = datos

    def function(self):
        dbk_sqlite.delete(self.datos)