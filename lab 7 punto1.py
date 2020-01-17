#Programa cuántas
#Deivid Sebastian Medina Rativa
#19/09/19

cont = 0
num = 0
valor = int(input("Ingrese el valor a buscar:"))
numeros = []
print(numeros)
while num != -1:
    num = int(input("Ingrese un numero:"))
    numeros = numeros + [num]    
    if valor == num:
        cont= cont + 1
print("El valor a buscar:", valor, "se encontro:", cont, "veces.")
