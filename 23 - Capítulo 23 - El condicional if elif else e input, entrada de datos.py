edad = int (input(" QUE EDAD TIENES?   .....     "))

if edad <= 5:
    print("no puedes entrar a este lugar")


elif edad >= 10 and edad <= 16:
    print("te falta poco para entrar a este lugar")


elif edad >= 18 and edad <= 60: 
    print("puedes entra al lugar")

else:
    print("edad ya no valida")
