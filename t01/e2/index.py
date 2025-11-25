from ..model.Hilo_A import Hilo_A
from ..model.Hilo_B import Hilo_B
from utils.util_menus import mostrar_encabezado

def main():
    
    hilo_a = Hilo_A()
    hilo_b = Hilo_B()

    mostrar_encabezado("Ejecucion en HiloA")
    hilo_a.start()

    mostrar_encabezado("Ejecucion en HiloB")
    hilo_b.start()

    mostrar_encabezado("Ejecucion en main")
    for _ in range(10):
        print("MAIN")

    hilo_a.join()
    hilo_b.join()