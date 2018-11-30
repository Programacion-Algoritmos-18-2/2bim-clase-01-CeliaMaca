"""
	Importamos la libreria codecs para evitar conflictos pro caracteres especiales
"""
import codecs

"""
creamos una clase Archivo para leer el archivo
"""
class MiArchivo:
	"""
	Contructor de la clase que abre el archivo
	"""
	def __init__(self):
		"""
		"""
		self.archivo=codecs.open("data\informacion.csv", "r")#abrimos el archivo en su ubicacion y con el comando r de lectura
	"""
	Obtener la informacion del archivo como un arreglo (cada posicion uan linea del archivo)
	"""
	def obtener_informacion(self):
		return self.archivo.readlines()
	"""
	Cerramso el archivo
	"""	
	def cerrar_archivo(self):
		self.archivo.close()
"""
	Creamos una clase para crear o escribir al final de un archivo definido
"""
class MiArchivoEscribir:
	"""
	Constructor que al iniciarse abre el archivo
	"""
	def __init__(self):
		"""
        """
		self.archivo = codecs.open("data/info_resumida.csv", "a")#Direccion del archivo y con el comando a para agregar al final
	
	"""
	Funcion que escribe una linea al final en el archivo sleccionado
	"""
	def agregar_informacion(self, a):
		self.archivo.write("%s|%2.f\n" % (a.nombre, a.obtener_promedio()))
	"""
	Funcion para cerrar el archivo y guardar lso cmabios 
	"""
	def cerrar_archivo(self):
		self.archivo.close()