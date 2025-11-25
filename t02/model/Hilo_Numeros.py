import threading, time

class Hilo_Numeros(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        for i in range(1, 101):
            print(f"[{self.ident}] {self.nombre}: {i}")
            time.sleep(0.1)