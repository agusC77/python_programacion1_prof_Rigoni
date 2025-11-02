#actividad 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva':
1450}
precios_frutas["naranja"] = 1200
precios_frutas["manzana"] = 1500
precios_frutas["pera" ] = 2300

print(f"los primeros precios son: {precios_frutas}")

#actividad 2

precios_frutas["Banana"] = 1330
precios_frutas["manzana"] = 1700
precios_frutas["Melon"] = 2800

print(f"los precios actualizados son: {precios_frutas}")

#actividad 3

frutas = []
frutas.extend(precios_frutas.keys())
print(f"las frutas solas son: {frutas}")

#actividad 4
def asignar_diccionario(contacto,numero):
    guia_telefonica[contacto] = numero

guia_telefonica = {}
enunciado = True
while enunciado == True:
    try:
        for i in range(5):
            contacto= str(input("ingrese el nombre del contacto: "))
            numero = int(input("ingrese el numero del contacto: "))
            asignar_diccionario(contacto,numero)
        enunciado = False
    except ValueError:
        print("error, ingrese un numero valido")

nombre_deseado = input("de que contacto desea saber el numero?:")
if nombre_deseado in guia_telefonica:
    print(f"el numero de ese contacto es {(guia_telefonica[nombre_deseado])}")
else:
    print("el contacto ingresado no se encuentra en la guia")

#actividad 5

def asignar_recuento(palabra):
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

enunciado = True
palabras_unicas = set()
recuento = {}

while enunciado == True:
    try:
        frase = str(input("ingrese una frase: "))
        for palabra in frase.split():
            palabras_unicas.add(palabra)
            asignar_recuento(palabra)
        enunciado = False
    except ValueError:
        print("error, ingrese una frase valida")

print(recuento)

#actividad 6

def notas_primer_alumno(nota_1,nota_2,nota_3):
    notas_alumno_1 = (nota_1,nota_2,nota_3)
    alumnos[alumno_1] = notas_alumno_1
    print(f"las notas del primer alumno son: {notas_alumno_1}")

def promedio_primer_alumno(nota_1,nota_2,nota_3):
    promedio = (nota_1 + nota_2 + nota_3) / 3
    print(f"el promedio de las tres notas del primer alumno es: {promedio}")

def notas_segundo_alumno(nota_1,nota_2,nota_3):
    notas_alumno_2 = (nota_1,nota_2,nota_3)
    alumnos[alumno_2] = notas_alumno_2
    print(f"las notas del segundo alumno son: {notas_alumno_2}")

def promedio_segundo_alumno(nota_1,nota_2,nota_3):
    promedio = (nota_1 + nota_2 + nota_3) / 3
    print(f"el promedio de las tres notas del segundo alumno es: {promedio}")

def notas_tercer_alumno(nota_1,nota_2,nota_3):
    notas_alumno_3 = (nota_1,nota_2,nota_3)
    alumnos[alumno_3] = notas_alumno_3
    print(f"las notas del tercer alumno son: {notas_alumno_3}")

def promedio_tercer_alumno(nota_1,nota_2,nota_3):
    promedio = (nota_1 + nota_2 + nota_3) / 3
    print(f"el promedio de las tres notas del tercer alumno es: {promedio}")
alumnos = {}
enunciado = True

while enunciado == True:
    try:
        alumno_1 = str(input("ingrese el nombre del primer alumno: "))
        alumno_2 = str(input("ingrese el nombre del segundo alumno: "))
        alumno_3 = str(input("ingrese el nombre del tercer alumno: "))
        alumnos[alumno_1] = 0
        alumnos[alumno_2] = 0
        alumnos[alumno_3] = 0
        alumnos[alumno_1]
        while enunciado == True:
            try:
                nota_1 = float(input("ingrese la primera nota del primer alumno: "))
                nota_2 = float(input("ingrese la segunda nota del primer alumno: "))
                nota_3 = float(input("ingrese la tercera nota del primer alumno: "))
                notas_primer_alumno(nota_1,nota_2,nota_3)
                promedio_primer_alumno(nota_1,nota_2,nota_3)
                alumnos[alumno_2]
                nota_1 = float(input("ingrese la primera nota del segundo alumno: "))
                nota_2 = float(input("ingrese la segunda nota del segundo alumno: "))
                nota_3 = float(input("ingrese la tercera nota del segundo alumno: "))
                notas_segundo_alumno(nota_1,nota_2,nota_3)
                promedio_segundo_alumno(nota_1,nota_2,nota_3)
                alumnos[alumno_3]
                nota_1 = float(input("ingrese la primera nota del tercer alumno: "))
                nota_2 = float(input("ingrese la segunda nota del terceralumno: "))
                nota_3 = float(input("ingrese la tercera nota del terceralumno: "))
                notas_tercer_alumno(nota_1,nota_2,nota_3)
                promedio_tercer_alumno(nota_1,nota_2,nota_3)
                enunciado = False
            except ValueError:
                print("error, ingrese un numero valido")
        enunciado = False
    except ValueError:
        print("error, ingrese nombres validos por favor")
#actividad 7

parcial_1 = set()
parcial_2 = set()

enunciado = True
while enunciado == True:
    try:
        cantidad_alumnos_1 = int(input("ingrese cuantos estudiantes aprobaron el primer parcial: "))
        for i in range(cantidad_alumnos_1):
            aprobados_1 = str(input("ingrese los nombres de los estudiantes que aprobaron el primer parcial: "))
            parcial_1.add(aprobados_1)
        cantidad_alumnos_2 = int(input("ingrese cuantos alumnos aprobaron el segundo parcial: "))
        for i in range(cantidad_alumnos_2):
            aprobados_2 = str(input("ingrese los nombres de los estudiantes que aprobaron el segundo parcial: "))
            parcial_2.add(aprobados_2)
        enunciado = False
    except ValueError:
        print("error, ingrese un valir valido")
print(f"los alumnos que aprobaron el primer parcial son: {parcial_1}")
print(f"los alumnos que aprobaron el segundo parcial son: {parcial_2}")
print(f"los alumnos que aprobaron ambos parciales son: {parcial_1.intersection(parcial_2)}")
print(f"los alumnos que aprobaron solo un parcial son: {parcial_1.symmetric_difference(parcial_2)}")
print(f"los alumnos que aprobaron al menos uno de los parciales son: {parcial_1.union(parcial_2)}")

#actividad 8
def ingresar_productos_y_stock():
    enunciado = True
    while enunciado == True:
        try:
            productos = str(input("ingrese el nombre del producto: "))
            stock = int(input(f"ingrese el stock producto {productos}: "))
            almacen[productos] = stock
            enunciado = False
        except ValueError:
            print("error, ingrese valores validos")
almacen = {}
enunciado = True
while enunciado == True:
    try:
        cantidad_productos = int(input("ingrese la cantidad de productos iniciales que desea ingresar: "))
        while cantidad_productos <= 0:
            cantidad_productos = int(input("error, ingrese un numero valido mayor a 0: "))
        for i in range(cantidad_productos):
            ingresar_productos_y_stock()
        enunciado = False
    except ValueError:
        print("error, ingrese valores validos")

while enunciado == False:
    try:
        print("opcion 1: consultar stock")
        print("opcion 2: agregar stock a un producto")
        print("opcion 3: agregar un nuevo producto")
        print("opcion 4: salir")
        opcion = int(input("que opcion desea realizar?: "))
        while opcion not in [1,2,3,4]:
            opcion = int(input("error, elija entre las opciones indicadas: "))
        if opcion == 1:
            producto_consultar = str(input("sobre que producto desea consultar?: "))
            if producto_consultar in almacen:
                print(f"el producto {producto_consultar} tiene {almacen[producto_consultar]} stock disponible")
            else:
                print("el producto no esta ingresado en el almacen")
        elif opcion == 2:
            producto_añadir = str(input("a que producto desea añadirle stock?: "))
            if producto_añadir in almacen:
                cantidad_añadir = int(input(f"cuantas unidades desea agregar al producto {producto_añadir}?: "))
                almacen[producto_añadir] += cantidad_añadir
                print(f"ahora el producto tiene {almacen[producto_añadir]} unidades")
            else:
                print("el producto no se encuentra disponible en el almacen")
        elif opcion == 3:
            producto_nuevo = str(input("ingrese el nombre del nuevo producto para almacenar: "))
            if producto_nuevo in almacen:
                print("error, el producto ya existe en el almacen")
            else:
                stock_producto_nuevo = int(input("ingrese la cantidad de unidades del nuevo producto: "))
                almacen[producto_nuevo] = stock_producto_nuevo
        elif opcion == 4:
            print("entendido")
            enunciado = True
    except ValueError:
        print("error, ingrese un valor valido")

#actividad 9
def entero_positivo_9():
    while True:
        try:
            numero = input()
            print()
            if not numero.isdigit():
                raise ValueError
            else:
                return numero
        except ValueError:
            print("Error, el valor ingresado no puede contener: ")
            print("- Coma")
            print("- Letras")
            print("- Números negativos")
            print("- Caracteres Especiales")
            print("- Tampoco puede quedar vacio")
            print()

def validar_hora_minutos():
    hora = ""
    minutos = ""
    hora_minutos = ""
    while True:
        try:
            print("Ingrese la hora:")
            hora = entero_positivo_9()
            print("Ingrese los minutos:")
            minutos = entero_positivo_9()
            hora_completa = "" 
            longitud = 0 
            numero = 0 
            longitud = len(hora)
            match longitud:
                case 2:
                    numero = int(hora)
                    if numero > 23:
                        raise Exception
                case 1:
                    hora = "0" + hora
                case _ :
                    raise Exception
            longitud = len(minutos)
            match longitud:
                case 1:
                    minutos = "0" + minutos
                case 2:
                    numero = int(minutos)
                    if numero > 59:
                        raise Exception
                case _ :
                    raise Exception
            hora_completa = hora +  ":" + minutos
            return hora_completa
        except Exception:
            print(" EL valor ingresado no puede sr mayor a 23 en caso de la hora")
            print(" El valor ingresado no puede ser mayor a 59 en caso de los minutos")

def validar_dia():
    dia = ""
    while True:
        dia = input("Ingrese el día: ").strip().capitalize()
        if dia == "":
            print("Error, no puedes dejar este campo vacío \n")
            continue
        match dia:
            case "Lunes":
                return dia
            case "Martes":
                return dia
            case "Miércoles":
                return dia
            case "Jueves":
                return dia
            case "Viernes":
                return dia
            case "Sábado":
                return dia
            case "Domigo":
                return dia
            case _ :
                print(f"{dia} no es un dia de la semana")
                print()

agenda = {("Lunes", "8:00"): "Programación", ("Lunes","10:30"): "Arquitectura", ("Miércoles", "8:30"): "Matemática"}
dia = ""
hora_minutos= ""
clave = ()

print("Ingrese un día y horario para saber si hay algún evento registrado")
dia = validar_dia()
print("El horario se mostrara en el siguiente formato 08:00, primero debes ingresar la hora y luego los minutos")
hora_minutos = validar_hora_minutos()
clave = (dia, hora_minutos)

if not clave in agenda:
    print(f"El {dia}, a las {hora_minutos} no se tienenes ningún evento")
else:
    print(f"El {dia}, a las {hora_minutos} está programado el siguiente evento: {agenda[clave]}")
print()

#actividad 10

original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}
capitales = ""
paises = ""
inversa = {}

for clave, valor in original.items():
    capitales = valor
    paises = clave
    inversa[capitales] = paises

print("Lista Original: ")
for clave, valor in original.items():
    print(f"- {clave}: {valor}")
print()
print("Lista al revez: ")
for clave, valor in inversa.items():
    print(f"- {clave}: {valor}")
print()

