from t03.model.Cajero import CuentaBancaria
from t03.model.Persona import Persona
from utils.util_menus import mostrar_encabezado
import threading

def lanzar_hilos(hilos):
    for h in hilos: h.start()
    for h in hilos: h.join()

def main():

    cuenta_sin_lock = CuentaBancaria()
    cuenta_con_lock = CuentaBancaria()

    personas_sin = [Persona("Pepe", cuenta_sin_lock), Persona("Maria", cuenta_sin_lock)]
    personas_con = [Persona("Pepe", cuenta_con_lock), Persona("Maria", cuenta_con_lock)]

    cantidades = [300]*6 + [100]*6

    hilos_sin, hilos_con = [], []
    
    mostrar_encabezado("Sin Lock")
    
    for persona, cantidad in zip(personas_sin*5, cantidades):
        hilos_sin.append(threading.Thread(target=persona.retirar, args=(cantidad,)))        
    
    lanzar_hilos(hilos_sin)

    mostrar_encabezado("Con Lock")
    for persona, cantidad in zip(personas_con*6, cantidades):
        hilos_con.append(threading.Thread(target=persona.retirar, args=(cantidad,True)))  
    
    lanzar_hilos(hilos_con)