#actividad 1
numeros = list(range(0,101,4))
print(numeros)

#actividad 2
lista = ["hola",123,"agustin",True,"2007"]
print(f"el penultimo elemento de la lista es {lista[-2]}")

#actividad 3

lista = []
for i in range(3):
    palabras = input("ingrese las palabras a añadir a la lista: ")
    lista.append(palabras)

print(lista)

#actividad 4

lista = ["perro", "gato", "conejo", "pez"]
print(f"la lista original es: {lista}")
lista[1] = "loro"
lista[3] = "oso"

print(f"la lista de animales cambiada es: {lista}")

#actividad 5
#EXPLICACION CON MIS PALABRAS: 
numeros = [9,15,3,22,7] # el programa crea una lista de 5 numeros desordenados
numeros.remove(max(numeros)) # le aplica el comando remove y el comando max a esa lista, lo que remueve el numero mas grande
print(numeros) # imprime la lista modificada, se imprimira [9,15,3,7]

#actividad 6

numeros = list(range(10,31,5))

print(F"los primeros dos numeros de la lista son: {numeros[0]} y {numeros[1]}")

#actividad 7

autos = ["sedan", "polo", "suran", "gol"]
print(f"la lista original es: {autos}")
autos[1] = "corvette"
autos[2] = "renault"
print(f"la lista modificada es: {autos}")

#actividad 8:

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(f"la fila con el doble de 5, de 10 y de 15 es: {dobles}")

#actividad 9: 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras.remove(compras[0][0])

print(f"la lista de compras modificada es: {compras}")

#actividad 10:

lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(lista_anidada)

