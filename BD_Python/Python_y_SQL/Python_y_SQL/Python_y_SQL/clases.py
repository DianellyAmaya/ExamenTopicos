import mysql.connector
from mysql.connector import Error

class BD():
	def __innit__(self):
		try:
			conexion = mysql.connector.connect(host = 'localhost', user = 'root',	passwd = 'root',	db = 'bdpendientes')
			print('Se ha conectado la base de datos')
		except Error as ex:
			print('la conexión ha tenido un error: ', ex)

	def imprimir_personas(self):
		if self.conexion.is_connected():
				try:
					cursor = self.conexion.cursor()
					cursor.execute('slect nombre from personas')
					consulta = cursor.fetchall()
					return consulta
				except Error as ex:
					print('La conexion ha tenido un error: ', ex)

	def select(self, tabla):
		if self.conexion.is_connected():
				try:
					script = 'select * from ' + tabla
					cursor = self.conexion.cursor()
					cursor.execute(script)
					consulta = cursor.fetchall()
					return consulta
				except Error as ex:
					print('La conexion ha tenido un error: ', ex)

#Imprimirá el monto, fecha y nombre de la persona que realizo la esd
	def imprimir_esd(self): 
		if self.conexion.is_connected():
				try:
					cursor = self.conexion.cursor()
					cursor.execute('select esd.fechaES, esd.montoIE, pe.nombre,'					
					'from entradasalidadinero esd from entradasalidadinero esd inner join personas pe'
					'on esd.idPersonas = pe.id')
					consulta = cursor.fetchall()
					return consulta
				except Error as ex:
					print('La conexion ha tenido un error: ', ex)

#Imprimirá el pendiente, nombre de quien lo asignó
	def imprimir_pendientes(self): 
		if self.conexion.is_connected():
				try:
					cursor = self.conexion.cursor()
					cursor.execute('select per.nombre, pen.id from pendientes pen'
					'inner join personas per on per.id = pen.idPersonaQueAsigno')
					consulta = cursor.fetchall()
					return consulta
				except Error as ex:
					print('La conexion ha tenido un error: ', ex)


#base = BD()
#impresion = base.imprimir_personas()
#for nombre in impresion:
	#print(nombre[0])

b = BD()
print(b.select('usuarios'))