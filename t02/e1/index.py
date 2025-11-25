from ..model.Hilo_Durmiente import Hilo_Durmiente

def main():
    hilo = Hilo_Durmiente()

    print("Estado antes de start:", hilo.is_alive())

    hilo.start()
    print("Estado justo después de start:", hilo.is_alive())

    hilo.join()
    print("Estado después de join:", hilo.is_alive())