#actividad 1
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
corrimiento = int(input("ingrese cuantas letras se correra cada letra: "))

for numero_mensaje in range(1,6):
    mensaje = input("ingrese el mensaje: ").upper()
    mensaje_encript = ""
    for letra in mensaje:
        if letra in abecedario:
            posicion = abecedario.index(letra)
            nueva_posicion = (posicion + corrimiento) % 27
            letra_nueva = abecedario[nueva_posicion]
            mensaje_encript = mensaje_encript + letra_nueva
        else:
            mensaje_encript = mensaje_encript + letra
    
    print(f"el mensaje encriptado es: {mensaje_encript}")

#actividad 2
import random
opcion = input("jugamos a piedra papel o tijeras? ").lower()
victorias = 0
derrotas = 0
empates = 0
if opcion == "si":
    while opcion == "si":
        opcion_elegida = input("elija piedra papel o tijera: ").lower()
        opciones =["piedra","papel","tijera"]
        eleccion_programa = random.choice(opciones)
        print(f"elijo {eleccion_programa}!")
        if opcion_elegida == eleccion_programa:
            print("es un empate")
            empates = empates + 1
        elif opcion_elegida == "piedra":
            if eleccion_programa == "tijera":
                print("HAS GANADO!")
                victorias = victorias + 1
            elif eleccion_programa == "papel":
                print("HAS PERDIDO")
                derrotas = derrotas + 1
        elif opcion_elegida == "tijera":
            if eleccion_programa == "papel":
                print("HAS GANADO!")
                victorias = victorias + 1
            elif eleccion_programa == "piedra":
                print("HAS PERDIDO")
                derrotas = derrotas + 1
        elif opcion_elegida == "papel":
            if eleccion_programa == "piedra":
                print("HAS GANADO!")
                victorias = victorias + 1
            elif eleccion_programa == "tijera":
                print("HAS PERDIDO")
                derrotas = derrotas + 1
        else:
            print("opcion invalida")
        opcion = input("jugamos de nuevo? (si/no) ").lower()
    print(f"el resultado final es: tienes {victorias} partidas ganadas, tienes {derrotas} partidas perdidas y {empates} empates")
elif opcion == "no":
    print("OK,Hasta luego!")
else:
    print("error,ingrese si o no")