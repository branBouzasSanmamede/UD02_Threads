from t01.index import main as t01
from t02.index import main as t02
from utils.util_menus import ejecutar_menu

menu = [
    (1, "Boletin 1 Hilos", t01)
    (2, "Boletin 2 Hilos", t02)
]

def main():
    ejecutar_menu(menu)

if __name__ == "__main__":
    main()