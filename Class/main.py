import os

from Banco import Banco
from Cuenta import Cuenta
from CuentaAhorro import CuentaAhorro
from Propietario import Propietario
from View import View
#from Class.Banco import Banco 

banco = Banco("Banco")
view = View()
propietario1 = Propietario("Juan Pérez", "Av. Principal 123", "123456789", "juan@gmail.com")
propietario2 = Propietario("María Gómez", "Calle Secundaria 456", "987654321", "maria@gmail.com")
banco.registrarPropietario(propietario1)
banco.registrarPropietario(propietario2)
cuenta1 = Cuenta( 1000, propietario1)
cuenta2 = Cuenta( 2000, propietario2)
cuenta3 = CuentaAhorro( 2000, propietario1)
cuenta4 = CuentaAhorro( 2000, propietario2)
banco.registrarCuenta(cuenta1,propietario1)
banco.registrarCuenta(cuenta2,propietario2)
banco.registrarCuenta(cuenta3,propietario1)
banco.registrarCuenta(cuenta4,propietario2)

cuenta1.depositar(500)
cuenta2.retirar(300)


op = 0
while(op != 9):
    os.system("cls")
             
    print("Banco\n\n")
    print("1. Agregar Propietario")
    print("2. Registrar Cuenta")
    print("3. Depositar")
    print("4. Transaccion")
    print("5. Retiro")
    print("6. Reporte de propietarios")
    print("7. Consultar cuenta")
    print("8. Consultar propietario")
    print("9. Salir")
    op = int(input("Elige una opcion: "))
    
    
    os.system("cls")
    if(op == 1):
        view.agregarPropietario(banco)
    elif(op == 2):
        view.registrarCuenta(banco)
    elif(op == 3):
        view.depositarMenu(banco)
    elif(op == 4):
        view.transaccionMenu(banco)
    elif(op == 5):
        view.retiroMenu(banco)
    elif(op == 6):
        banco.imprimirReporte()
    elif(op == 7):
        view.consultarCuenta(banco)
    elif(op == 8):
        view.consultarPropietario(banco)
    elif(op == 9):
        print("Saliendo del programa")
    else:
        print("No existe esa opcion")
        
    print()
    os.system("pause")
    
