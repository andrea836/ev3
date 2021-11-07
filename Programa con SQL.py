import datetime
import sys
import sqlite3
from sqlite3 import Error

precioFinal=0
respuestaWhile=1
respuesta=1
clave_venta=0

while respuesta==1:
    print("***MENU***")
    print("")
    print("1.Registrar venta")
    print("2.Consulta de venta")
    print("3.Reporte de fechas")
    print("4.Salir")
    print("")
    
    opcion=int(input("Ingrese una accion:\n"))
    
    if opcion==1:
        try:
            with sqlite3.connect("Venta.db") as conn:
                while respuestaWhile==1:
                    print("Conexion establecida")
                    mi_cursor = conn.cursor()
                    clave_venta=input("Que folio de venta se ingreso: \n")
                    FechaActual=datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
                    Articulo=input("Que articulo se vendió: \n")
                    Pcs=int(input("Cuantas piezas fueron vendidas: \n"))
                    precio=int(input(f"A que precio fue vendido {Articulo}: \n"))
                    precioTotal=precio*Pcs
                    PrecioMulti=precioTotal*.16
                    precioIVAF=precioTotal+PrecioMulti
                    print(f"La cantidad a pagar es: {precioIVAF}")
                    valores = {"Folio": clave_venta, "Fecha": FechaActual, "Articulo":Articulo, "Cantidad":Pcs, "PrecioIVA":precioIVAF}
                    mi_cursor.execute("INSERT INTO RegistroVentas VALUES(:Folio, :Fecha, :Articulo, :Cantidad, :PrecioIVA)",valores)
                    print("Registro agregado exitosamente")
                    respuestaWhile=int(input("Desea registrar otra venta? [1] SI [0] NO?: "))
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
                conn.close()
                print("Se ha cerrado la conexión")
                
    if opcion==2:
        try:
            with sqlite3.connect("Venta.db") as conn:
                mi_cursor = conn.cursor()
                claveConsulta=int(input("Dime que clave quieres consultar: \n"))
                criterios = {"Folio":claveConsulta}
                mi_cursor.execute("SELECT Folio,Fecha,Descripcion,Cantidad,PrecioIVA FROM RegistroVentas WHERE Folio = :Folio;", criterios)
                registros = mi_cursor.fetchall()
   
                for Folio, Fecha, Articulo, Cantidad, Precio in registros:
                    print(f"Folio = {Folio}")
                    print(f"Fecha de registro = {Fecha}")
                    print(f"Descripcion = {Articulo}")
                    print(f"Cantidad = {Cantidad}")
                    print(f"Precio con IVA = {Precio}")
                respuestaWhile=int(input("Desea consultar otro dato? [1] SI [0] NO "))
        except sqlite3.Error as e:
            print (e)
        except Exception:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
                conn.close()
                print("Se ha cerrado la conexión")
                    
    if opcion==3:
        fecha_consultar = input("Dime una fecha (dd/mm/aaaa): ")
        fecha_consultar = datetime.datetime.strptime(fecha_consultar, "%d/%m/%Y").date()
        try:
            with sqlite3.connect("Venta.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
                mi_cursor = conn.cursor()
                criterios = {"fecha":fecha_consultar}
                mi_cursor.execute("SELECT Folio, Fecha, Descripcion, Cantidad, PrecioIVA FROM RegistroVentas WHERE DATE(Fecha) = :fecha;", criterios)
                registros = mi_cursor.fetchall()
   
                for Folio, Fecha, Articulo, Cantidad, Precio in registros:
                    print(f"Folio = {Folio}")
                    print(f"Fecha de registro = {Fecha}")
                    print(f"Descripcion = {Articulo}")
                    print(f"Cantidad = {Cantidad}")
                    print(f"Precio con IVA = {Precio}")
                    print("*"*5)
            respuestaW=int(input("Desea consultar otro dato? [1] SI [0] NO "))
        except sqlite3.Error as e:
            print (e)
        except Exception:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
                conn.close()
                print("Se ha cerrado la conexión")
                
                
    if opcion==4:
        print("Ha cerrado el programa con exito")
        break