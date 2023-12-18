
#%%
import pandas as pd   
import os 
import sys 
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

from ast import literal_eval

import mysql.connector
#%%

def creacion_bbdd_tablas(query, contraseña, nombre_bbdd=None):
    """
    Crea una conexión a la base de datos MySQL y ejecuta una consulta para crear una tabla.

    Args:
    - query (str): Consulta SQL para crear la tabla en la base de datos.
    - contraseña (str): Contraseña para acceder a la base de datos.
    - nombre_bbdd (str): Nombre de la base de datos a la que se conectará.

    Returns:
        - None

    """
    if nombre_bbdd is not None:
        cnx = mysql.connector.connect(
            user="root", 
            password=contraseña, 
            host='localhost'
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
    else:
        cnx = mysql.connector.connect(
            user="root", 
            password=contraseña,
            host="localhost", 
            database=nombre_bbdd
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)
            cnx.close()

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cnx.close()

def insertar_datos(query, contraseña, nombre_bbdd, lista_tuplas_ventas):
    cnx = mysql.connector.connect(
        user="root", 
        password=contraseña, 
        host="localhost", database=nombre_bbdd
    )

    mycursor = cnx.cursor()

    try:
        mycursor.executemany(query, lista_tuplas_ventas)
        cnx.commit()
        print(mycursor.rowcount, "registro/s insertado/s.")
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()