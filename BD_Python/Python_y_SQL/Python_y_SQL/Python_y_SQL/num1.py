import mysql.connector
from mysql.connector import Error

try:
	conexion = mysql.connector.connect(host = 'localhost',
	user = 'root',
	#si no pide contrasña (como XAMPP) se puede quitar la passwd
	#passwd = 'root',
	db = 'bdpendientes')
except Error as ex:
	print('La conexion ha tenido un error: ', ex)


#Un cursor nos sirve para hacer consultas en SQL

cursor = conexion.cursor()
#cursor.execute('select id from entradasalidadinero')
#cursor.execute('select id, montoie, fechaes from entradasalidadinero')
cursor.execute('select id, montoie, fechaes from entradasalidadinero where id = 5')
consulta = cursor.fetchall()

#for i in consulta:
    #Se puede imprimir de estas dos formas:
	#print(i)
	#print(i[0])

for id, montoie, fechaes in consulta:
	print('El id es: ', id, ' con un monto ', montoie, 'y con fecha: ', fechaes)
#Una de las dos para salir: (el exit me da error por alguna razón)
#conexion.exit()
conexion.close()