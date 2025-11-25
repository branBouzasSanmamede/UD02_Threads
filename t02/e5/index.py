from ..model.Hilo_Factorial import Hilo_Factorial
from ..model.Hilo_Fibonacci import Hilo_Fibonacci
from utils.util_simples import pedir_numero_positivo

def main():

    hilo_factorial = Hilo_Factorial(pedir_numero_positivo("Introduce el número para calcular el factorial: "))
    hilo_fibonacci = Hilo_Fibonacci(pedir_numero_positivo("Introduce el número para calcular Fibonacci: "))

    hilo_factorial.start()
    hilo_fibonacci.start()

    hilo_factorial.join()
    hilo_fibonacci.join()