# Copyright          2022 DBK. All rights reserved.       ####   ####   #   #
# Author: Davide P. Fragnito <davidepie90@gmail.com>      #   #  #   #  #  #
#                                                         #   #  ####   ###
# Python API (main graphics display)                      #   #  #   #  #  #
#                                                         ####   ####   #   #

import sqlite3 as sql


## Inicializar la clase con la ruta de la Base de datos y el nombre de la tabla
# ejemplo: dbk_sqlite = DBK_SQLite('data/mydatabase.db','users')
#
## Cambiar el primer valor que por defecto es 'id'
# ejemplo: dbk_sqlite.changeFirstValor('year')
#
## Crea la base de datos si no existe
# Pasar los valores en un unico str y el numero de datos
# 'id, username, password' = 3
# ejemplo: dbk_sqlite.create('id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL', 3)
#
## Comprueba la existencia y devuelve un bool
# ejemplo: if dbk_sqlite.exist(1,'id'): print('id=1 exist')
#
## Verifica la comparación de dos datos y devuelve un bool
# ejemplo: if dbk_sqlite.verified('username','admin','password','123456'): print('Login')
#
## Insertar nuevo elemento en la Base de datos
# Pasar los argumentos en tuple
# ejemplo: dbk_sqlite.insert(1,'admin','123456')
#
## Elimina un elemento del registro
# Pasar los argumentos en tuple como los devuelven los find
# ejemplo: dbk_sqlite.delete(dbk_sqlite.findById(1))
#
## Busca en la Base de datos por columna y devuelve una list
# ejemplo: lista = dbk_sqlite.findBy('username', 'admin')
#
## Busca en la Base de datos por columna y devuelve una list
# ejemplo: lista = dbk_sqlite.findDouble('id', 1, 'username', 'admin')
#
## Busca en la Base de datos por id y devuelve una list
# ejemplo: lista = dbk_sqlite.findById(1)
#
## Devuelve el primer Id libre de la tabla
# ejemplo: next_id = dbk_sqlite.nextId()
#
## Devuelve el número de datos guardados
# ejemplo: all_users = dbk_sqlite.size()
##
class DBK_SQLite:
    directory = ''
    table = ''
    first_valor = 'id'

    ## Inicializar la clase con la ruta de la Base de datos y el nombre de la tabla
    # ejemplo: dbk_sqlite = DBK_SQLite('data/mydatabase.db','users')
    def __init__(self, directory, table):
        self.directory = directory
        self.table = table

    ## Cambiar el primer valor que por defecto es 'id'
    # ejemplo: dbk_sqlite.changeFirstValor('year')
    def changeFirstValor(self, valor):
        self.first_valor = valor

    ## Crea la base de datos si no existe
    # Pasar los valores en un unico str y el numero de datos
    # 'id, username, password' = 3
    # ejemplo: dbk_sqlite.create('id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL', 3)
    def create(self, scalar_valued):
        function = f""" CREATE TABLE {self.table} ({scalar_valued})"""
        position = scalar_valued.find(' ')
        if position > 0:
            tmp_str = ''
            for i in range(0, position):
                tmp_str += scalar_valued[i]
            self.changeFirstValor(tmp_str)
        conexion = sql.connect(self.directory)
        try:
            cursor = conexion.cursor()
            cursor.execute(function)
            conexion.commit()
        except sql.OperationalError:
            print()
        conexion.close()

    ## Comprueba la existencia y devuelve un bool
    # ejemplo: if dbk_sqlite.exist(1,'id'): print('id=1 exist')
    def exist(self, valor, value='id'):
        function = f'SELECT * FROM {self.table} WHERE {value}={valor}'
        conexion = sql.connect(self.directory)
        cursor = conexion.cursor()
        cursor.execute(function)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        if datos:
            return True
        else:
            return False

    ## Verifica la comparación de dos datos y devuelve un bool
    # ejemplo: if dbk_sqlite.verified('username','admin','password','123456'): print('Login')
    def verified(self, value1, valor1, value2, valor2):
        function = f"SELECT {self.first_valor} FROM {self.table} WHERE {value1}='{valor1}' AND {value2}='{valor2}'"
        conexion = sql.connect(self.directory)
        cursor = conexion.cursor()
        cursor.execute(function)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        if datos:
            return True
        else:
            return False

    ## Insertar nuevo elemento en la Base de datos
    # Pasar los argumentos en tuple
    # ejemplo: dbk_sqlite.insert(1,'admin','123456')
    def insert(self, *args):
        if self.exist(args[0]):
            print(f"insert Error: the {self.first_valor}='{args[0]}' already exists.")
            return
        function = f"INSERT INTO {self.table} VALUES ("
        scalar_valued = len(args)
        for i in range(0, scalar_valued):
            if type(args[i]) == str:
                tmp_args = f"'{args[i]}'"
            else:
                tmp_args = args[i]
            function += str(tmp_args)
            if i < (scalar_valued - 1):
                function += ','
            else:
                function += ')'
        conexion = sql.connect(self.directory)
        cursor = conexion.cursor()
        cursor.execute(function)
        conexion.commit()
        conexion.close()

    ## Elimina un elemento del registro
    # Pasar los argumentos en tuple como los devuelven los find
    # ejemplo: dbk_sqlite.delete(dbk_sqlite.findById(1))
    def delete(self, data):
        if not self.exist(data[0]):
            print(f"insert Error: the {self.first_valor}='{data[0]}' not exists.")
            return
        function = f"DELETE FROM {self.table} WHERE {self.first_valor}={data[0]}"
        conexion = sql.connect(self.directory)
        cursor = conexion.cursor()
        cursor.execute(function)
        conexion.commit()
        conexion.close()

    ## Busca en la Base de datos por columna y devuelve una list
    # ejemplo: lista = dbk_sqlite.findBy('username', 'admin')
    def findBy(self, value, valor):
        function = f'SELECT * FROM {self.table} WHERE {value}="{valor}"'
        conexion = sql.connect(self.directory)
        cursor = conexion.cursor()
        cursor.execute(function)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return datos

    ## Busca en la Base de datos por columna y devuelve una tupla
    # ejemplo: lista = dbk_sqlite.findDouble('id', 1, 'username', 'admin')
    def findDouble(self, value1, valor1, value2, valor2):
        if self.verified(value1, valor1, value2, valor2) == False:
            return None
        function = f"SELECT * FROM {self.table} WHERE {value1}='{valor1}' AND {value2}='{valor2}'"
        conexion = sql.connect(self.directory)
        cursor = conexion.cursor()
        cursor.execute(function)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return datos

    ## Busca en la Base de datos por id y devuelve una list
    # ejemplo: lista = dbk_sqlite.findById(1)
    def findById(self, id):
        return self.findBy(self.first_valor, id)

    ## Devuelve el primer Id libre de la tabla
    # ejemplo: next_id = dbk_sqlite.nextId()
    def nextId(self):
        result = 0
        data = ''
        while data is not None:
            result += 1
            data = self.findById(result)
        return result

    ## Devuelve el número de datos guardados
    # ejemplo: all_users = dbk_sqlite.size()
    def size(self):
        function = f"SELECT count({self.first_valor}) FROM {self.table}"
        conexion = sql.connect(self.directory)
        cursor = conexion.cursor()
        cursor.execute(function)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        datos = str(datos)
        datos = datos.replace('(', '').replace(",)", '')
        return int(datos)
