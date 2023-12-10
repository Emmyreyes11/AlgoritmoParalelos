#Crea una clase persona que tenga los siguientes atributos: nombre,apellido,edad,sexo,direccion.

class persona: 
    nombre =""
    apellidos = ""
    edad = ""
    sexo = ""
    direccion = ""



    def Persona1 (self, nombre, apellidos,edad, sexo, direccion):
        return self.nombre + "" + self. apellidos  + "" + self.edad  + "" + self.sexo  + "" + self.direccion
        
        
pers =  persona()
nombre = input ("Nombre..:")
apellidos = input ("Apellidos..:")
edad = input ("Edad..:")
sexo = input ("Sexo..:")
direccion = input ("Direccion..:")

print(pers.Persona())
