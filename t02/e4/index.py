from ..model.Hilo_Numeros import Hilo_Numeros
from utils.util_menus import mostrar_encabezado
import time

def main():
    hilos = []

    for n in range(1, 6):
        hilos.append(Hilo_Numeros(f"miHilo-{n}"))

    mostrar_encabezado("Lanzando los hilos")
    t0 = time.time()

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    t1 = time.time()
    print(f"Tiempo total de ejecución: {t1 - t0:.5f} segundos")