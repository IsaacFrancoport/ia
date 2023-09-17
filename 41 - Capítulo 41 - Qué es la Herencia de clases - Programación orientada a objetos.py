

class Usuario:
	def __init__(self, nombre, apodos):
		self.nombre = nombre
		self.apodos = apodos
	

	def muestra_datos(self):
		print("el nombre del usuario es: " + self.nombre, "y tirne", self.apodos)

usuario1 = Usuario("isaac", "snupy")

usuario1.muestra_datos()

class Usuario_Premium(Usuario):
 pass
usuario2 = Usuario("Emmanuel", "raton")

usuario2.muestra_datos()
	

