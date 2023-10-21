nota= int(input("Digite Su Nota"))
carrera = input("Carrera")

if nota >=90 and carrera.upper() == "ISC":
   print("Aplica para beca en la MIT")
else:
   print("Lo sentimos no tenemos becas disponibles")