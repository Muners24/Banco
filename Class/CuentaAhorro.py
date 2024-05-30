from Cuenta import Cuenta
import math
class CuentaAhorro(Cuenta):
    def __init__(self, saldo_inicial, propietario):
        super().__init__( saldo_inicial, propietario)
        self.ahorro = 0
        self.tasa_interes = math.log(saldo_inicial)/200
        
    def calcular_interes(self,plazo):
        self.ahorro += self.saldo * self.tasa_interes/plazo
        
    def estadoCuenta(self):
        super().estadoCuenta()
        print(f'\tTasa de intereses: {self.tasa_interes*100:.2f}%')
        print(f'\tSaldo acumulado: {self.ahorro}')
