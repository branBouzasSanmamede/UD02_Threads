from .e1.index import main as e1
from .e2.index import main as e2
from .e3.index import main as e3
from .e4.index import main as e4
from .e5.index import main as e5
from .e6.index import main as e6
from utils.util_menus import ejecutar_menu

menu = [
    (1, "Ejercicio 1", e1),
    (2, "Ejercicio 2", e2),
    (3, "Ejercicio 3", e3),
    (4, "Ejercicio 4", e4),
    (5, "Ejercicio 5", e5),
    (6, "Ejercicio 6", e6)
]

def main():
    ejecutar_menu(menu)