from ..model.Hilo_A import Hilo_A

def main():
    hilo = Hilo_A()
    hilo.start()

    for _ in range(30):
        print("YES")

    hilo.join()