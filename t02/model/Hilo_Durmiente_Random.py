import threading, time, random

class Hilo_Durmiente_Random(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.tiempo_ms = random.randint(0, 10000)

    def run(self):
        try:
            print(f"{self.nombre} va a estar dormido durante {self.tiempo_ms} milisegundos.")
            time.sleep(self.tiempo_ms / 1000)
        except Exception as e:
            print(f"Excepción en {self.nombre}: {e}")
        print(f"{self.nombre} ha despertado.")