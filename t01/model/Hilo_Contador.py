import threading

contador = 0

class Hilo_Contador(threading.Thread):
    def __init__(self, palabra):
        super().__init__()
        self.palabra = palabra

    def run(self):
        for _ in range(10):
            Hilo_Contador.contador += 1
            print(self.palabra, " - ", Hilo_Contador.contador)