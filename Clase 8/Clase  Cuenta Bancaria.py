#Crea una clase CuentaBancaria

class CuentaBancaria: 
    def __init__ (self,numero_cuenta, titular, saldo=0.0):
         self.numero_cuenta = numero_cuenta
         self.titular = titular
         self.saldo= saldo
         
    def depositar (self,monto): 
        if monto > 0:
              self.saldo += monto
              print ("Deposito de ${monto}realizado. Nuevo Saldo: ${self.saldo}")
        else:
              print("El monto del deposito debe ser mayor que cero.")
              return f"Deposito exitoso. Saldo actual: {self.saldo}"
              
              
    def retirar (self, monto): 
        if monto > 0 and monto <= self.saldo: 
           self.saldo -= monto  
           print(f"Retiro de $ {monto} saldo actual:{self.saldo} " )  
        else:
              print("Insuficiente saldo.")
              
    def Calcular_interes(self,tasa_interes):
        if tasa_interes >= 0:
             interes = self.saldo*(tasa_interes /100)
             print("Calculo de interes: ${interes}")
        else:
             print("La tasa de interes debe ser mayor o igual a cero.")
    
    def imprimir_datos(self):
      print(f"Datos de la cuenta:")
      print(f"Numero de cuenta: {self.numero_cuenta} ")
      print(f"Titular:{self.titular}")
      print(f"Saldo actual: ${self.saldo}")


