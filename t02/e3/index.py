from ..model.Hilo_Numeros import Hilo_Numeros
import time

def main():
    hilo = Hilo_Numeros("HiloSecundario")

    inicio = time.time()

    hilo.start()
    hilo.join()

    fin = time.time()
    print(f"\nTiempo total de ejecución: {fin - inicio:.2f} segundos")