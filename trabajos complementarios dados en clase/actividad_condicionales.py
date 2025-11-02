fechas = input("ingrese el dia(texto), ingrese el numero del dia (numero) / ingrese el mes: ")
fechas =fechas.split(",")
dia = fechas[0]
aux = fechas[1].strip().split("/")
DD = int(aux[0])
MM = int(aux[1])

if MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12:
    if DD > 31 or DD < 1:
        print("error en la fecha")
    else:
        print(f"hoy es {dia}, {DD} del {MM}")
elif MM == 4 or MM == 6 or MM == 9 or MM == 11:
    if DD > 30 or DD < 1:
        print("error en la fecha")
    else:
        print(f"hoy es {dia}, {DD} del {MM}")
elif MM == 2:
     if DD > 28 or DD < 1:
        print("error en la fecha")
     else:
        print(f"hoy es {dia}, {DD} del {MM}")

if dia == "lunes" or dia == "martes" or dia == "miercoles":
    examenes = input("se tomaron examenes? ")
    if examenes == "si" or examenes == "SI":
        cant_aprobados = int(input("ingrese la cantidad de aprobados: "))
        cant_desaprobados = int(input("ingrese la cantidad de desaprobados: "))
        total_alumnos = cant_aprobados + cant_desaprobados
        porcentaje_aprobados = (cant_aprobados/total_alumnos) * 100
        print(f"el porcentaje de aprobados es: {porcentaje_aprobados}")
    elif examenes =="no" or examenes == "NO":
        print("no hay examenes evaluados")
    else:
        print("error, la respuesta debe ser si o no")
elif dia == "jueves":
    porcentaje_asistencia = int(input("ingrese el porcentaje de alumnos q asistio a la clase: "))
    if porcentaje_asistencia > 50 and porcentaje_asistencia < 101:
        print("asistio la mayoria de los alumnos")
    elif porcentaje_asistencia < 50 and porcentaje_asistencia > 0:
        print("no asistio la mayoria de los alumnos")
    else:
        print("error")
elif dia  == "viernes":
    if DD == 1 and (MM == 1 or MM == 7):
        print("Comienzo de nuevo ciclo")
        cant_alumnos = int(input("ingrese la cantidad de alumnos "))
        arancel = int(input("ingrese el arancel en $ a pagar de cada alumno "))
        ingreso_total = cant_alumnos * arancel
        print(f"el ingreso total recibido es: {ingreso_total} $")


    