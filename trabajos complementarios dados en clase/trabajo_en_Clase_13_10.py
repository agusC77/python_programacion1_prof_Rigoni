import csv
with open("archivo.csv","w",newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre","precio"])
enunciado = True
while enunciado == True:
    try:
        print("bienvenido!")
        print("1) mostrar productos")
        print("2) agregar productos")
        print("3) eliminar productos")
        print("4) salir")
        opcion = int(input("que opcion desea realizar?: "))
        while opcion not in [1,2,3,4]:
            opcion = int(input("error, ingrese una opcion entre el 1 y el 4: "))
        if opcion == 1:
            with open("archivo.csv","r") as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    print(fila)
        elif opcion == 2:
            pass
    except ValueError:
        print("error, elija un numero valido")
    