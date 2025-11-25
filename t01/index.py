from .e1.index import main as e1
from .e2.index import main as e2
from .e3.index import main as e3
from utils.util_menus import ejecutar_menu

menu = [
    (1, "Ejercicio 1", e1),
    (2, "Ejercicio 2", e2),
    (3, "Ejercicio 3", e3)
]

def main():
    ejecutar_menu(menu)