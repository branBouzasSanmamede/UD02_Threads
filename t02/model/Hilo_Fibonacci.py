from utils.util_simples import calcular_fibonacci
from utils.util_menus import mostrar_encabezado
import threading

class Hilo_Fibonacci(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.resultado = None

    def run(self):
        mostrar_encabezado(f"Cálculo del fibonacci de: {self.n}")
        self.resultado = calcular_fibonacci(self.n)
        print(f"Fibonacci de {self.n} = {self.resultado}")