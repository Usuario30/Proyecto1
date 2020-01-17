#Programa cuántas
#Deivid Sebastian Medina Rativa
#19/09/19

bandera = False
num = 0
valor = int(input("Ingrese el valor a buscar:"))
numeros = []
print(numeros)
while num != -1:
    num = int(input("Ingrese un numero:"))
    numeros = numeros + [num]    
    if valor == num:
        bandera = True
print("El valor a buscar:", valor, "se encontro:", bandera)
