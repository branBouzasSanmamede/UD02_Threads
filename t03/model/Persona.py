class Persona:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta

    def retirar(self, cantidad, usar_lock=False):
        if usar_lock:
            self.cuenta.retirar_con_lock(self.nombre, cantidad)
        else:
            self.cuenta.retirar_sin_lock(self.nombre, cantidad)