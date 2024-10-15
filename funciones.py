supermercado = float(input("Cantidad de productos"))
print(supermercado)
def multiplicacion(x,y):
    return x * y
subtotal = 0
cantidad = 1

while cantidad !=0:
    print("Cantidad de productos")
    cantidad = float(input())
    if cantidad==0:
        break

precio = float(input("ingresar precio del producto"))
resultado = multiplicacion(supermercado, precio)
print(resultado)