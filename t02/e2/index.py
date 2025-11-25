from ..model.Hilo_Durmiente_Random import Hilo_Durmiente_Random

def main():
    hilos = [Hilo_Durmiente_Random(f"Hilo{i+1}") for i in range(3)]

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()