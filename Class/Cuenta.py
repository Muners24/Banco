
from datetime import datetime

class Cuenta:

    def __init__(self,saldo_inicial,propietario):
        self.numero = 0
        self.saldo = saldo_inicial
        self.fecha_creacion = self.obtenerFecha()
        self.ultima_transaccion = [self.obtenerFecha(),"Creacion Cuenta"]
        self.propietario = propietario
        
    def obtenerFecha(self):
        fecha_actual = datetime.now()
        fecha_actual = fecha_actual.strftime("%d/%m/%Y %H:%M")
        return fecha_actual
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        self.ultima_transaccion[0] = self.obtenerFecha()
        self.ultima_transaccion[1] = "Deposito " + str(cantidad)
            
    def retirar(self, cantidad):
        self.saldo -= cantidad
        self.ultima_transaccion[0] = self.obtenerFecha()
        self.ultima_transaccion[1] = "Retiro " +str(cantidad)

    
    def transferencia(self, destino ,cantidad):
        self.saldo -= cantidad
        destino.saldo += cantidad 
        self.ultima_transaccion[0] = self.obtenerFecha()
        self.ultima_transaccion[1] = "Transferencia de " + str(cantidad) + " a " + destino.numero

    def estadoCuenta(self):
        print(f'\n\tNumero de cuenta: {self.numero}')
        print(f'\tPropietario: {self.propietario.nombre}')
        print(f'\tSaldo: {self.saldo}')
        print(f'\tUlima transacción: {self.ultima_transaccion[0]} {self.ultima_transaccion[1]}')
        print(f'\tFecha de creacion: {self.fecha_creacion}')
      