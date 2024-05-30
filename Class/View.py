from Banco import Banco
from Cuenta import Cuenta
from CuentaAhorro import CuentaAhorro
from Propietario import Propietario

class View:
    
    def __init__(self):
        pass
    
    def agregarPropietario(banco):
        print("Agregar Proietario\n")
        nombre = input("Ingresa su nombre: ")
        dir = input("Ingresa su dirección: ")
        tel = input("Ingresa su telefono: ")
        correo = input("Ingresa su correo: ")
        banco.registrarPropietario(Propietario(nombre,dir,tel,correo))
    
    def registrarCuenta(banco):
        print("Registrar Cuenta\n")
        nombre = input("Ingresa el nombrer del propietario: ")
        tel = input("Ingresa su telefono: ")
        
        prop = banco.obtenerPropietario(nombre,tel)
        if(prop == None):
            return
            
        print("\n1.Cuenta Normal")
        print("2.Cuenta Ahorro (Saldo inicial minimo de 2000)")
        print("3.Cancelar")
        op = input("Elige una opcion: ")

        print()
        if(op == '1'):
            saldo = float(input("Ingresa el saldo inicial: "))
            cuenta = Cuenta(saldo,prop)
        elif(op == '2'):
            saldo = 0
            while saldo < 2000:
                saldo = float(input("Ingresa el saldo inicial: "))
                if(saldo < 2000):
                    print("\nSaldo insuficiente\n")
            cuenta = CuentaAhorro(saldo,prop)
        elif(op == '3'):
            print("Operacion canelada")
            return
        else:
            print("No existe esa opcion")
            return
        
        print(banco.registrarCuenta(cuenta,prop))
        
    def depositarMenu(banco):
        print("Deposito\n")
        num = input("Ingresa el numero de cuenta: ")
        cantidad = float(input("Ingresa la cantidad: "))
        print(banco.depositar(num,cantidad))

    def transaccionMenu(banco):
        print("Transferencia\n")
        num = input("Ingresa el numero de cuenta origen: ")
        num = input("Ingresa el numero de cuenta destino: ")
        cantidad = float(input("Ingresa la cantidad: "))
        print(banco.transaccion(num,cantidad))

    def retiroMenu(banco):
        print("Retiro\n")
        num = input("Ingresa el numero de cuenta: ")
        cantidad = float(input("Ingresa la cantidad: "))
        print(banco.retirar(num,cantidad))

    def consultarCuenta(banco):
        print("Consultar Cuenta\n")
        num = input("Ingresa el numero de cuenta: ")
        cuenta = banco.obtenerCuenta(num)
        if(cuenta != None):
            cuenta.estadoCuenta()
        
    def consultarPropietario(banco):
        print("Consultar Propietario\n")
        nombre = input("Ingresa el nombrer del propietario: ")
        tel = input("Ingresa su telefono: ")
        print()
        
        prop = banco.obtenerPropietario(nombre,tel)
        if(prop == None):
            return
        
        prop.datos()
        for cuenta in prop.cuentas:
            cuenta.estadoCuenta()