# listas = [3,4,6,7,8,9,1,2,3,5]
# elemento = input("ingresar la cantidad de datos en la lista")
# print(elemento)
# for  in range()
# print()

tamano = input("ingrese el tamano de la lista")
listas = []
for i in range(int(tamano)):
    print(f'el valor a ingresar es: {i} ')
    valor = input()
    listas.append(valor)
print(listas)

contador = input("ingrese el tamano de la lista")
listas = []
while i in range(int(contador)):
    print(f'el valor a ingresar es: {i} ')
    valor = input()
    listas.append(valor)
print(listas)

def saludar():
    print("Hola, mundo!")
    
#llamar a la funcion
saludar() #imprime ""

def multiplicacion(x,y):
    return x * y
