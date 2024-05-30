
from Cuenta import Cuenta


class Banco:
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.prop_cont = 0
        self.cuenta_cont = 0
        self.propietarios = {}
        self.cuentas = {}
    
    def registrarPropietario(self,nuevo_propietario):
        self.propietarios[self.prop_cont] = nuevo_propietario
        self.prop_cont += 1
        
    def registrarCuenta(self,cuenta,propietario):
        cuenta.numero = str(self.cuenta_cont)
        propietario.registrarCuenta(cuenta)
        self.cuentas[self.cuenta_cont] = cuenta
        self.cuenta_cont += 1
        return f'Cuenta registrada correctamente\nNumero de cuenta: {self.cuenta_cont-1}'
            
    def obtenerCuenta(self,numero_cuenta):
        for i in range(self.cuenta_cont):
            if(self.cuentas[i].numero == numero_cuenta):
                return self.cuentas[i]
        print("Cuenta no encontrada")
        return None
        
    def obtenerPropietario(self,nombre,telefono):
        for i in range(self.prop_cont):
            if self.propietarios[i].nombre == nombre and self.propietarios[i].telefono == telefono:
                return self.propietarios[i]
        print("Propietario no encontrado\n")
        return None
    
    def imprimirReporte(self):
        print("Reporte de cuentas\n")
        for i in range(self.prop_cont):
            print()
            self.propietarios[i].datos()
            print()
            for cuenta in self.propietarios[i].cuentas:
                cuenta.estadoCuenta()
    
    def depositar(self,numero_cuenta,cantidad):
        invalido = ""
        if(cantidad < 0):
            invalido += "Cantidad invalida\n"
        
        cuenta = self.obtenerCuenta(numero_cuenta)
        if cuenta == None:
            invalido += "No existe una cuenta con ese numero\n"
        
        if(invalido == ""):
            cuenta.depositar(cantidad)
            return "Deposito exitoso\n"
        
        return invalido

    def retirar(self,numero_cuenta,cantidad):
        invalido = ""
        cuenta = self.obtenerCuenta(numero_cuenta)
        if cuenta == None:
            invalido += "No existe una cuenta con ese numero\n"
        if(cantidad < 0 or cantidad > cuenta.saldo):
            invalido += "Cantidad invalida\n"
            
        if(invalido == ""):
            cuenta.retirar(cantidad)
            return "Retiro exitoso"
        return invalido
    
    def transferencia(self,num_cuenta_origen,num_cuenta_destino,cantidad):
        invalido = ""
        origen = self.obtenerCuenta(num_cuenta_origen)
        destino = self.obtenerCuenta(num_cuenta_destino)
        if origen == None and destino == None:
            invalido += "Alguna de las cuentas no existe\n"
        
        if(cantidad < 0 or cantidad > origen.saldo):
            invalido += "Cantidad invalida\n"
        
        if invalido == "":
            origen.transferencia(destino,cantidad)
            return "Transferencia exitosa\n"
        
        return invalido

        
        
