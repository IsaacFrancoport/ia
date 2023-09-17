cursos = ['Python', 'JavaScript', 'COBOL', 'HTML']

for x in cursos:
	print(x)
	# A QUI PODEMOS NOTAR QUE SE IMPRIMRN TODOS LOS CURSOS EN FORMA ORDENADA 
cursos = ['gato', 'perro', 'chango', 'raton']

for x in cursos:
	if x == "chango":
		break
	print(x)
	# A QUI PODEMOS VER QUE SOLAMNETE SE IMPRIME HASTA PERRO YA QUE CHANGO NO SE IMPRIME 