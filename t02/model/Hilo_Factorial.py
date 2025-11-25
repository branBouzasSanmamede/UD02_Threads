from utils.util_simples import calcular_factorial
from utils.util_menus import mostrar_encabezado
import threading

class Hilo_Factorial(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.resultado = None

    def run(self):
        mostrar_encabezado(f"Cálculo del factorial de: {self.n}")
        self.resultado = calcular_factorial(self.n)
        print(f"Factorial de {self.n} = {self.resultado}")