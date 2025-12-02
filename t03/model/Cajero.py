import threading
import time
import random

class CuentaBancaria:
    def __init__(self, saldo_inicial=2000):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def retirar(self, nombre, cantidad):
        print(f"- {nombre} intenta retirar {cantidad}€")
        print(f"-- Saldo antes del retiro: {self.saldo}€")
        time.sleep(random.uniform(0.01, 0.1))

        if self.saldo >= cantidad:
            self.saldo -= cantidad
            time.sleep(random.uniform(0.01, 0.1))
            print(f"  ✅  {nombre} retiró {cantidad}€")
        else:
            print(f"  ❌  {nombre} NO pudo retirar {cantidad}€. Saldo insuficiente")

        print(f"-- Saldo actual: {self.saldo}\n")

    def retirar_sin_lock(self, nombre, cantidad):
        self.retirar(nombre, cantidad)

    def retirar_con_lock(self, nombre, cantidad):
        with self.lock:
            self.retirar(nombre, cantidad)