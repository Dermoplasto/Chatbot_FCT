import sqlite3 as sql

def crear_conexion():
	""" Creamos una conexión con la base de datos """
	conexion = None
	try:
		conexion = sql.connect(r"bd_cerves.db")
	except sql.Error as error:
		print(error)

	return conexion

def ejecutar_sentencia(sentencia):
	conexion = crear_conexion()

	cursor = conexion.cursor()
	cursor.execute(sentencia)
	filas = cursor.fetchall()

	filas_retorno = []

	for fila in filas:
		if len(fila) == 1:
			filas_retorno.append(fila[0])
		else:
			filas_retorno.append(fila)
	conexion.close()
	
	return filas_retorno


def consultar_cervezas(tipo = None, pais = None):
    sentencia = 'SELECT DISTINCT * FROM CERVEZAS'
	
    return ejecutar_sentencia(sentencia)


'''
def consultar_cervezas():
    """ Consultamos todas las cervezas de la base de datos """

    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM CERVEZAS")
    cervezas = cursor.fetchall()
    
    return cervezas

def consultar_grad_cerves_pais(PAIS_ORIGEN):
    """ Consultamos graduación de cervezas según país de origen"""

    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT GRADUACION FROM CERVEZAS WHERE PAIS_ORIGEN = "+"{}".format(PAIS_ORIGEN))
    cervezas = cursor.fetchall()
    
    return cervezas


def consultar_categoria(CATEGORIA):
    """ Consultamos las categorías de las cervezas """

    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT CATEGORIA FROM CERVEZAS WHERE CATEGORIA = "+"{}".format(CATEGORIA))
    cervezas = cursor.fetchall()
    
    return cervezas

def consultar_graduacion(GRADUACION):
    """ Consultamos la graduación de las cervezas """

    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT GRADUACION FROM CERVEZAS WHERE GRADUACION ="+"{}".format(GRADUACION))
    cervezas = cursor.fetchall()
    
    return cervezas

def consultar_precio(PRECIO):
    """ Consultamos el precio de las cervezas """

    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT PRECIO FROM CERVEZAS WHERE PRECIO ="+"{}".format(PRECIO))
    cervezas = cursor.fetchall()
    
    return cervezas


'''




