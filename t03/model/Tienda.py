import threading
import time

class Tienda:
    def __init__(self):
        self.clientes = []
        self.sem = threading.Semaphore(3)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def cliente(self, id):
        with self.sem:
            print(f"Se ha ocupado la plaza con id {id}")
            time.sleep()