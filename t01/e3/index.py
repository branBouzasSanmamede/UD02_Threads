from ..model.Hilo_Contador import Hilo_Contador

def main():
    Hilo_Contador.contador = 0

    h1 = Hilo_Contador("SI")
    h2 = Hilo_Contador("NO")

    h1.start()
    h2.start()

    h1.join()
    h2.join()

    print("\nValor final del contador:", Hilo_Contador.contador)