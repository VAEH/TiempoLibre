import sqlite3

#Conecxión a la base de datos

conn = sqlite3.connect(':memory:')

#cursor
cursor = conn.cursor()

#Creo la tabla
cursor.execute("""CREATE TABLE currency
                    (ID integer primary key, name text, symbol text)""" )

#Inserto datos de monedas
cursor.execute("INSERT INTO currency VALUES (1, 'Peso (ARG)', '$')")
cursor.execute("INSERT INTO currency VALUES (2, 'Dolar', 'U$S') ")

#Guardo cambios 
conn.commit()

#Consulto todas las monedas
query = "SELECT * FROM currency"

#Busco el resultado 
#Y con fetchall vamos a obtener todas las filas
currencies = cursor.execute(query).fetchall()

print(currencies)

#Cierro la conexión a la Base de datos
conn.close()