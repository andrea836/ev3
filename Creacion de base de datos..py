import sys
import datetime
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("Venta.db") as conn:
        c= conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS RegistroVentas(Folio INTEGER PRIMARY KEY, Fecha timestamp NOT NULL, Descripcion TEXT NOT NULL, Cantidad INTEGER NOT NULL, PrecioIVA INTEGER NOT NULL);")
        print("Tabla creada exitosamente")
except Error as e:
    print(e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")