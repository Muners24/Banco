
class Propietario:

    def __init__(self, nombre, direccion, telefono, correo):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.cuentas = []
        
    def registrarCuenta(self,cuenta):
        self.cuentas.append(cuenta)

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def actualizar_correo(self, nuevo_correo):
        self.correo = nuevo_correo
        
    def datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Direccion: {self.direccion}')
        print(f'Telefono: {self.telefono}')
        print(f'Correo: {self.correo}')
