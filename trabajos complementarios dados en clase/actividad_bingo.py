import random
num = random.sample(range(1,51),25)
carton = [num[i:i+5]for i in range(0,25,5)]
bolillas = list(range(1,51))
random.shuffle(bolillas)

print("carton inicial:")
for fila in carton:
    print(fila)


while bolillas:
    numero_aleatorio = bolillas.pop()
    encontrado = False
    for i in range(5):
        for j in range(5):
             if carton[i][j] == numero_aleatorio:
                 carton[i][j] = 0
                 encontrado = True
    if encontrado:
        print(f"el numero {numero_aleatorio} esta en tu carton")
    else:
        print(f"el numero {numero_aleatorio} no esta en tu carton")

    for fila in carton:
        print(fila)
    
    if all(all(num_carton == 0 for num_carton in fila)for fila in carton):
        print("BINGO CARTON LLENO!!")
        break
    else:
        print("el carton aun no esta lleno")