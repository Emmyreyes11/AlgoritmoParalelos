#Crea una clase Empleado

class persona1: 
    def __init__(self,nombre="", apellidos="", edad=0, sexo=0,  direccion="", email="", sueldo=0):
       self.nombre = nombre 
       self.apellidos = apellidos 
       self.edad = edad 
       self.sexo = sexo
       self.direccion = direccion 
       self.email = email
       self.sueldo = sueldo 

    def Asignar_Sueldo(self,sueldo):
        self.sueldo = sueldo
        
    def calcular_Afp(self):      
    #El Afp es el 2.87% del suueldo afp=0.02287 * self.sueldo
    
     def Calcular_Sfs(self):
    #El SFS es el 3.04% del sueldo Sfs= 0.0304 * self.sueldo return Sfs

      def calcular_impuesto_renta(self):
    # Deducciones de TSS sfs= self.sueldo * 0.0304, afp = self.sueldo * 0.0287, total_deducciones = sfs + afp

    #Base Imponible
        base_imponible = self.sueldo - total_deducciones

    #Multiplicar por 12 
    base_anual = base_imponible * 12

    #Verificar en que rango cae 
    if base_anual <=416220.00:
       impuesto_mensual = 0
    elif 416220.00 <base_anual<=624329.00:
      excedente= base_anual - 416220.00
      impuesto_anual = excedente * 0.15
      impuesto_mensual = impuesto_anual / 12
    elif 624329.00 <base_anual<=867123.00:
      excedente = base_anual - 624329.00
      impuesto_anual = excedente * 0.20 + 31216.00 #Sumar monto fijo adicional

      impuesto_mensual= impuesto_anual /12
    elif base_anual > 867123.00:
      excedente = base_anual - 867123.00
      impuesto_anual = excedente * 0.25 + 6516.00
      impuesto_mensual = impuesto_anual/12
    else:
       impuesto_mensual = 0
    return impuesto_mensual
    
def imprimir_datos(self):
      print(f"Nombre:{self.nombre}")
      print(f"Apellidos: {self.apellidos}")
      print(f"Edad: {self.edad}")
      print(f"Sexo: {self.sexo}")
      print(f"Direccion: {self.direccion}")
      print(f"Email: {self.email}")
      print(f"Sueldo: {self.sueldo}")
      print(f"AFP:  {self.calcular_Afp()}")
      print(f"SFS: {self.calcular_Sfs()}")
      print(f"IRS:  {self.calcular_impuesto_renta():.2f}")

    
#Obtener datos del usuario 
nombre = input ("Ingrese el nombre:")
apellidos = input ("Ingrese los apellidos:")
edad = int (input ("Ingrese la edad:"))
sexo = input("Ingrese el sexo:")
direccion = input ("Ingrese la direccion")
email = input ("Inngrese su correo electronico")
sueldo = float (input ("ingrese el sueldo:"))

#Ejemplode uso con datos ingresados por el usuario 
persona1 =Persona (nombre=nombre,apellidos=apellidos, edad=edad,direccion=direccion,email= email,sueldo= sueldo)

persona1.imprimir_datos ()


    
    