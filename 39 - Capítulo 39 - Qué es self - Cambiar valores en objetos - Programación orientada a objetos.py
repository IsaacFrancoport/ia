class Usuario:
	def __init__(self, nombre, apodos):
		self.nombre = nombre
		self.apodos = apodos
	

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApodos:', self.apodos)

usuario001 = Usuario('ISAAC EMMANUEL', 'SNUPY')

usuario002 = Usuario('ALEJANDRO', 'PRIETO')

usuario002.nombre = 'FRNACO'

usuario002.imprime_datos()