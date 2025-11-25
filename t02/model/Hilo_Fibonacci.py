from utils.util_simples import calcular_fibonacci
import threading

class Hilo_Fibonacci(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.resultado = None

    def run(self):
        self.resultado = calcular_fibonacci(self.n)
        print(f"Fibonacci de {self.n} = {self.resultado}")