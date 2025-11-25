from ..model.Hilo_Concurrente import Hilo_Concurrente
from utils.util_menus import mostrar_encabezado

def main():
    hiloA = Hilo_Concurrente(1, 10, "ThreadA")
    hiloB = Hilo_Concurrente(20, 30, "ThreadB")

    mostrar_encabezado("Hilos inicializados")

    hiloA.start()
    hiloB.start()

    hiloA.join()
    hiloB.join()