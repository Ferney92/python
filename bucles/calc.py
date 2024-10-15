def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero."

def calculadora():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        seleccion = input("Ingrese el número de la operación (1/2/3/4): ")

        if seleccion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if seleccion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif seleccion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif seleccion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif seleccion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")

            # Preguntar si desea realizar otra operación
            siguiente = input("¿Desea realizar otra operación? (si/no): ")
            if siguiente.lower() != 'si':
                break
        else:
            print("Selección inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    calculadora()
