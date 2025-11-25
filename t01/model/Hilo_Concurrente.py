import threading

class Hilo_Concurrente(threading.Thread):
    def __init__(self, inicio, fin, nombre):
        super().__init__()
        self.inicio = inicio
        self.fin = fin
        self.nombre = nombre

    def run(self):
        print(f"{self.nombre} comienza")
        for i in range(self.inicio, self.fin + 1):
            print(f"{self.nombre} dice: {i}")
        print(f"{self.nombre} termina")