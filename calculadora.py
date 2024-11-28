def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero!"
    return a / b

def mostrar_menu():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

def main():
    while True:
        mostrar_menu()
        try:
            operacion = int(input("Selecciona una operación (1/2/3/4) o 0 para salir: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if operacion == 0:
            print("Saliendo de la calculadora.")
            break

        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, ingresa un valor numérico válido.")
            continue

        if operacion == 1:
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif operacion == 2:
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif operacion == 3:
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif operacion == 4:
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Opción no válida, por favor elige una operación entre 1 y 4.")

if __name__ == "__main__":
    main()
