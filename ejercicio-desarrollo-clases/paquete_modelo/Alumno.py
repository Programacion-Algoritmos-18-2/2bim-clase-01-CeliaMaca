"""
"""
class Alumno(object):
	"""
	"""
	def __init__(self, n, n1, n2, n3):
		"""
		"""
		self.nombre=n
		self.nota1=int(n1)
		self.nota2=int(n2)
		self.nota3=int(n3)

	def agregar_nombre(self, n):
		"""
		agregar el nombre
		"""
		self.nombre = n
	def obtener_nombre(self):
		"""
		devolver el nombre
		"""
		return self.nombre

	def agregar_nota1(self,n1):#agregar nota 1
		self.nota1=int(n1)


	def obtener_nota1(self):# devolver nota 1
		"""
		"""
		return self.nota1
		
	def agregar_nota2(self, n2):# agregar nota 2
		"""
		"""
		self.nota2=int(n2)
	def obtener_nota2(self,):# devolver nota 2
		"""
		"""
		return self.nota2
	
	def agregar_nota3(self, n3):#agregaar nota 3
		"""
		"""
		self.nota3=int(n3)
	def obtener_nota3(self,):# devolver nota 3
		"""
		"""
		return self.nota3
	def obtener_promedio(self):# Calcular el promedio usando los obtener notas
		return (self.obtener_nota1()+self.obtener_nota2()+self.obtener_nota3())/3
	
	def __str__(self):#metodo para imprimir el pbjeto homologo al toString de JAVA
		"""
		"""
		return "%20s\t%10d "%(self.nombre, self.obtener_promedio())
		
		