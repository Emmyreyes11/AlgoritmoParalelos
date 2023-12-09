class CajeroAutomatico: 

    def entrar (self,monto): 
        self.
    def depositar (self,monto): 
        self.sueldo +=monto 
        return f"Deposito exitoso. Saldo actual: {self.saldo}"
    def retirar (self, monto): 
        if self.saldo  >=monto: 
            self.saldo -= monto
            return f"Retiro exitoso. saldo actual:{self.saldo} "   
        else: 
            return "Saldo insuficiente"

