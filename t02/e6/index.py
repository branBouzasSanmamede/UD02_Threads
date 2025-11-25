from ..model.Hilo_Factorial import Hilo_Factorial
from utils.util_simples import pedir_numero_positivo

def main():
    hilos = []

    for n in range(5, 10):
        hilos.append(Hilo_Factorial(n))

    for h in hilos:
        h.start()
        h.join()