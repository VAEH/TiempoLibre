import sqlite3
import hashlib
#Conecxión a la base de datos

conn = sqlite3.connect(':memory:')

#cursor
cursor = conn.cursor()

#Creo la tabla
cursor.execute("""CREATE TABLE currency
                    (ID integer primary key, name text, symbol text)""" )

#Guardo cambios 
conn.commit()

#Inserto datos de monedas
cursor.execute("INSERT INTO currency VALUES (1, 'Peso (ARG)', '$')")
cursor.execute("INSERT INTO currency VALUES (2, 'Dolar', 'U$S') ")

# Revierto los cambios
# Las dos inserciones anteriores no se van a ver efectuadas 
conn.rollback()

#Consulto todas las monedas
query = "SELECT * FROM currency"

#Busco el resultado 
#Y con fetchall vamos a obtener todas las filas
currencies = cursor.execute(query).fetchall()

print(currencies)

#Cierro la conexión a la Base de datos
conn.close()

# Crear funcion
def md5sum(t):
    return hashlib.md5(t).hexdigest()

conn = sqlite3.connect(':memory:')
conn.create_function("md5", 1, md5sum)
cursor = conn.cursor()
cursor.execute("select md5(?)", (b"foo",))
print(cursor.fetchone()[0])

# cierro la conexión a la base de datos  
conn.close()


class Mysum:
    def __init__(self):
        self.count = 0
    def step(self, value):
        self.count +=value
    def finalize(self):
        return self.count

conn = sqlite3.connect(':memory:')
conn.create_aggregate("mysum", 1, Mysum)
cursor = conn.cursor()
# Se crea la tabla test
cursor.execute("create table test(i)")
# Inserto en "test" el valor  '1' y '2'
cursor.execute("insert into test(i) values (1)")
cursor.execute("insert into test(i) values (2)")
# Luego se hace el select
cursor.execute("select mysum(i) from test")
print(cursor.fetchone()[0])