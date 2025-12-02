from utils.util_menus import mostrar_encabezado
from t03.model.Tienda import Tienda
from t03.model.Cliente import Cliente

tienda = Tienda()

def main():
    mostrar_encabezado("Tienda")
    nombre = "Pepe"

    for i in range(8):
        c = Cliente(i, nombre + f"_{i}")
        tienda.agregar_cliente(c)

