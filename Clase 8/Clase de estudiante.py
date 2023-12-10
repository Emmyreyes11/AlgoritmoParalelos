#Crea una clase estudiante que tenga los siguientes atributos: nombre,apellido,edad,sexo,direccion,carrera,email,telefono. 

class estudiante: 
    nombre =""
    apellidos = ""
    edad = ""
    sexo = ""
    direccion= ""
    carrera = ""
    email = ""
    telefono = ""



    def estudiante2 (self, nombre, apellidos,edad, sexo, direccion, carrera, email,telefono):
        return self.nombre + "" + self. apellidos  + "" + self.edad  + "" + self.sexo  + "" + self.direccion + "" + self.carrera + "" + self.email + "" + self.telefono
        
Estud = estudiante ()
nombre = input ("Nombre..:")
apellidos = input ("Apellido..:")
edad = input ("Edad..:")
sexo = input ("Sexo..:")
direccion = input ("Direccion..:")
carrera = input ("Carrera..:")
email = input ("Email..:")
telefono = input ("Telefono..:") 
       
print(Estud.estudiante())
