def pedir_numero_positivo(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = int(valor)
            if numero >= 0:
                return numero
            else:
                print("¡ALMENDRAO! Mete un número positivo.")
        except ValueError:
            print("¡ALMENDRAO! Mete un número válido.")

def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def calcular_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2))