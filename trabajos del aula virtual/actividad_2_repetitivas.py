#actividad 1: hacer un cuadrado de asteriscos
tam = int(input("ingrese el tamaño del cuadrado: "))
for i in range(tam):
    for j in range(tam):
        print("*", end = "")
    print()

#acividad 2: triangulo ascendente:
numero = int(input("ingrese un numero: "))
for i in range(1,numero + 1):
    for j in range(1, i + 1):
        print(j, end = "")
    print()

#actividad 3: tablas demultiplicar anidadas:

for i in range(1,11):
    for j in range(1,11):
        print(i ,"x", j,"=", i*j, end ="")
        print()
    
#actividad 4:cuadrado con bordes 1 e interior 0:

n = int(input("ingrese el tamaño del cuadrado:"))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n -1:
            print(1, end = "")
        else:
            print(0, end = "")
    print()

#actividad 5: combinacion de coordenadas:

for x in range(3):
    for y in range(3):
        for z in range(3):
            print(f"({x}, {y}, {z})")

#actividad 6: combinaciones con suma 10:

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i + j + k == 10:
                print(f"{i} + {j} + {k} = 10")

#actividad 7: contador regresivo 333-000:

for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        for k in range(3, -1, -1):
            print(i,j,k)

#actividad 8: reloj digital
import time
for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            print(f"{horas:02}:{minutos:02}:{segundos:02}")
            time.sleep(1)
        
#actividad 9:lanzamiento de dado:
import random

continuar = input("¿Querés jugar a sacar un 6? (s/n): ").lower()
while continuar == "s":
    print("Lanzando hasta obtener un 6…")
    lanzamiento = 0
    intentos = 0
    while lanzamiento != 6:
        lanzamiento = random.randint(1, 6)
        intentos += 1
        print(lanzamiento, end=" ")
    print(f"\n¡Salió 6 tras {intentos} lanzamientos!\n")
    continuar = input("¿Querés volver a jugar? (s/n): ").lower()
print("¡Gracias por jugar!")

#actividad 10: coordenadas,usuario:
coordenadas = False
while coordenadas == False:
    fila = int(input("ingrese la fila del 1 al 3"))
    while fila < 1 or fila > 3:
        fila = int(input("la fila ingresada esta fuera de rango, por favor ingresela nuevamente"))
    
    columna = int(input(" ingrese la columna del 1 al 4"))
    while columna < 1 or columna > 4:
            columna = int(input("ingrese una columna del 1 al 4 por favor"))
            
    coordenadas = True
print(f"las coordenadas correctas son {fila} {columna}") 