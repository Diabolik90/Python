from dbk.dbk_sqlite import DBK_SQLite

directory = '../data/BD.db'
table = 'alumnos'
f_value = 'id'
s_value = 'nombre'
t_value = 'apellido'
value = f'{f_value} INTEGER PRIMARY KEY, {s_value} TEXT NOT NULL, {t_value} TEXT NOT NULL'

dbk_sqlite = DBK_SQLite(directory,table)