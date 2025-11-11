import os
import csv

#============================================================================================
#Funcion que actualiza el archivo cada vez que se la llama en base a la lista de diccionarios generada

def actualizar_archivo(catalogo):
    with open ("catalogo.csv","w",encoding="utf-8",newline="") as archivo:
                escritor = csv.DictWriter(archivo,fieldnames=["titulo","cantidad"])
                escritor.writeheader()
                escritor.writerows(catalogo)

#============================================================================================
#Funcion que genera el archivo al principio de la ejecucion

def generar_archivo():
    if not os.path.exists("catalogo.csv"):
        with open ("catalogo.csv","w",encoding="utf-8",newline="") as archivo:
            escritor = csv.DictWriter(archivo,fieldnames=["titulo","cantidad"])
            escritor.writeheader()

#============================================================================================
#Funcion que carga el catalogo con los daos guardados en el archivo de las ejecuciones anteriores

def cargar_catalogo(catalogo):
    if os.path.exists("catalogo.csv"):
        with open ("catalogo.csv","r",encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo,fieldnames= ["titulo","cantidad"])
            next(lector)
            for fila in lector:
                catalogo.append(fila)

#============================================================================================
#Funcion que agrega los titulos e inicializa la cantidad en 0

def agregar_titulos(catalogo):
    while True:
        print("ingrese el titulo: ")
        titulo_ingresado = validar_titulo()
        existe = False
        for titulos in catalogo:
            if titulos["titulo"] == titulo_ingresado:
                print("error, el titulo ya existe")
                existe = True
                break
        if existe == False:
            cantidad = 0
            contenido = {"titulo":titulo_ingresado,"cantidad":cantidad}
            catalogo.append(contenido)
            actualizar_archivo(catalogo)
            while True:
                print("desea ingresar otro titulo? ")
                print("1) si")
                print("2) no")
                opcion = input(" esperando valor: ").lower()
                match opcion:
                    case "1":
                        break
                    case "2":
                        print("entendido")
                        return catalogo
                    case _:
                        print("error, ingrese 1 o 2")

#============================================================================================
#Funcion que modifica los ejemplares del archivo

def agregar_ejemplares(catalogo):
    print("a que titulo desea agregarle los ejemplares?: ")
    titulo = validar_titulo()
    for titulos in catalogo:
        if titulos["titulo"] == titulo:
            print(f"ingrese la cantidad de ejemplares del titulo {titulo}")
            cantidad = validar_cantidad()
            titulos["cantidad"] = cantidad
            break
    actualizar_archivo(catalogo)
    while True:
        print("desea agregar ejemplares a otro titulo? ")
        print("1) si")
        print("2) no")
        opcion = input("esperando valor: ").lower()
        match opcion:
            case "1":
                break
            case "2":
                print("entendido")
                return catalogo
            case _:
                print("error, elija entre 1 o 2")

#============================================================================================
#Funcion que muestra el catalogo

def mostrar_catalogo(catalogo):
    print("===========CATALOGO===========")
    for titulo in catalogo:
        print(f"titulo: {titulo['titulo']} ejemplares: {titulo['cantidad']}")

#============================================================================================
#Funcion que permite consultar la disponibilidad de un titulo en especifico

def consultar_titulo(catalogo):
    enunciado = True
    while enunciado == True:
        print("sobre que titulo desea consultar? ")
        titulo_consultar = validar_titulo()
        existe = False
        for titulo in catalogo:
            if titulo["titulo"] == titulo_consultar:
                existe = True
                if titulo["cantidad"] > 0:
                    print(f"el titulo {titulo_consultar} tiene {titulo['cantidad']} unidades disponibles")
                else:
                    print(f"el titulo {titulo['titulo']} no tiene unidades disponibles")
                enunciado = False
        if existe == False:
            print("error, el titulo no existe")
            print("regresando al menu......")
            break

#============================================================================================
#Funcion que lista los titulos agotados

def listar_agotados(catalogo):
    agotados = False
    for titulo in catalogo:
        if titulo["cantidad"] == 0:
            agotados = True
            print(f"el titulo {titulo["titulo"]} no tiene ejemplares disponibles")
    if agotados == False:
        print("no hay titulos agotados")

#============================================================================================
#Funcion que permite agregar un nuevo titulo y su cantidad (mayor a 0)

def agregar_nuevo_titulo(catalogo):
    while True:
        print("ingrese el nombre del nuevo titulo a agregar: ")
        titulo = validar_titulo()
        existe = False
        for titulos in catalogo:
            if titulo == titulos["titulo"]:
                print("error, el titulo ya fue ingresado")
                existe = True
                break
        if existe == False:
            print("Ingrese la cantidad del nuevo titulo: ")
            cantidad = validar_cantidad()
            contenido = {"titulo":titulo,"cantidad": cantidad}
            catalogo.append(contenido)
            actualizar_archivo(catalogo)
            print("desea ingresar otro titulo?: ")
            print("1) si")
            print("2) no")
            opcion = input("ingrese la opcion elegida: ")
            match opcion:
                case "1":
                    continue
                case "2":
                    print("entendido")
                    return catalogo
                case _:
                    print("error, elija entre 1) si o 2) no")

#============================================================================================
#Funcion que permite modificar los ejemplares ya sea sumando 1 (devolviendo un titulo) o restando 1 (prestando un titulo)

def modificar_ejemplares(catalogo,opcion_elegida):
    if opcion_elegida == "prestar":
        print("ingrese que titulo desea prestar: ")
        titulo_prestar = validar_titulo()
        encontrado = False
        for titulo in catalogo:
            if titulo["titulo"] == titulo_prestar:
                encontrado = True
                if titulo["cantidad"] == 0:
                    print(f"el titulo que desea prestar no tiene unidades disponibles")
                else:
                    titulo["cantidad"] -= 1
                    print("actualizado")
                    print(f"el titulo {titulo_prestar} tiene {titulo["cantidad"]} unidades disponibles")
                    actualizar_archivo(catalogo)
                    break
        if encontrado == False:
            print("el titulo no existe o no ha sido agregado")
    elif opcion_elegida == "devolver":
        print("ingrese el titulo que desea devolver: ")
        titulo_devolver = validar_titulo()
        encontrado = False
        for titulo in catalogo:
            if titulo["titulo"] == titulo_devolver:
                encontrado = True
                titulo["cantidad"] += 1
                print("actualizado")
                print(f"el titulo {titulo_devolver} tiene {titulo["cantidad"]} unidades disponibles")
                actualizar_archivo(catalogo)
        if encontrado == False:
            print("el titulo no existe o no ha sido agregado")

#============================================================================================
#Funcion que permite eliminar un titulo de la lista y del archivo

def eliminar_titulo(catalogo):
    print("ingrese el titulo a eliminar del catalogo: ")
    titulo_eliminar = validar_titulo()
    for titulos in catalogo:
        if titulos["titulo"] == titulo_eliminar:
            catalogo.remove(titulos)
            actualizar_archivo(catalogo)
            print("titulo eliminado con exito.")
            break

#============================================================================================
#Funciones que sirven para validar el titulo y la cantidad

def validar_titulo():
    valor = input("esperando valor: ").lower().strip()
    while not valor:
        valor = ("error, ingrese un valor valido: ").lower().strip()
    return valor
def validar_cantidad():
    while True:
        try:
            valor = int(input("esperando valor: "))
            if valor <= 0:
                raise ValueError
            else:
                return valor
        except ValueError:
            print("error, ingrese un numero entero valido mayor a 0")

#============================================================================================
#Funcion que ejecuta el menu

def menu(catalogo):
    while True:
        print ("==================MENU==================")
        print("1) ingresar titulos")
        print("2) ingresar ejemplares (reemplaza el numero ya existente de ejemplares)")
        print("3) mostrar catalogo")
        print("4) consultar disponibilidad")
        print("5) listar agotados")
        print("6) agregar titulo")
        print("7) actualizar ejemplares: prestamo o devolucion (modifica el numero existente de ejemplares mas no lo elimina)")
        print("8) eliminar titulo")
        print("9) salir")
        opcion = input("que desea realizar?: ")
        match opcion:
            case "1":
                agregar_titulos(catalogo)
            case "2":
                if not catalogo:
                    print("error, el catalogo esta vacio, ingrese titulos primero e intente nuevamente")
                else:
                    agregar_ejemplares(catalogo)
                    print(catalogo)
            case "3":
                if not catalogo:
                    print("error, el catalogo esta vacio, ingrese titulos primero e intente nuevamente")
                else:
                    mostrar_catalogo(catalogo)
            case "4":
                if not catalogo:
                    print("error, el catalogo esta vacio, ingrese titulos primero e intente nuevamente")
                else:
                    consultar_titulo(catalogo)
            case "5":
                if not catalogo:
                    print("error, el catalogo esta vacio, ingrese titulos primero e intente nuevamente")
                else:
                    listar_agotados(catalogo)
            case "6":
                if not catalogo:
                    print("error, el catalogo esta vacio, ingrese titulos primero e intente nuevamente")
                else:
                    agregar_nuevo_titulo(catalogo)
            case "7":
                if not catalogo:
                    print("error, el catalogo esta vacio, ingrese titulos primero e intente nuevamente")
                else:
                    while True:
                        opcion = input("desea prestar o devolver algun ejemplar?: ").lower().strip()
                        match opcion:
                            case "prestar":
                                modificar_ejemplares(catalogo,opcion)
                                break
                            case "devolver":
                                modificar_ejemplares(catalogo,opcion)
                                break
                            case _:
                                print("Error, elija entre prestar o devolver")
            case "8":
                if not catalogo:
                    print("error, el catalogo esta vacio, ingrese titulos primero e intente nuevamente")
                else:
                    eliminar_titulo(catalogo)
            case "9":
                print("entendido, gracias por usar este menu interactivo de libros!!")
                print("cerrando menu....")
                break
            case _:
                print("error, elija una de las opciones del menu")

#============================================================================================
#Fragmento del codigo que genera el archivo, la lista, carga la lista y llama la funcion del menu

if __name__ == "__main__":
    generar_archivo()
    catalogo = []
    cargar_catalogo(catalogo)
    menu(catalogo)