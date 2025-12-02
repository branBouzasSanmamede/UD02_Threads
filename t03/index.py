from .e1.index import main as e1
from .e2.index import main as e2
from .e3.index import main as e3
from .e4.index import main as e4
from .e5.index import main as e5
from .e6.index import main as e6
from .e7.index import main as e7
from .e8.index import main as e8
from .e9.index import main as e9
from .e10.index import main as e10
from utils.util_menus import ejecutar_menu

menu = [
    (1, "Ejercicio 1", e1),
    (2, "Ejercicio 2", e2),
    (3, "Ejercicio 3", e3),
    (4, "Ejercicio 4", e4),
    (5, "Ejercicio 5", e5),
    (6, "Ejercicio 6", e6),
    (7, "Ejercicio 6", e7),
    (8, "Ejercicio 6", e8),
    (9, "Ejercicio 6", e9),
    (10, "Ejercicio 6", e10),
]

def main():
    ejecutar_menu(menu)