#actividad 1

edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("es mayor de edad")
elif edad < 18 and edad > 0:
    print("es menor de edad")
else:
    print("error en la edad")

#actividad 2

nota = int(input("ingrese su nota del 1 al 10: "))
if nota >= 6 and nota < 11:
    print("aprobado")
elif nota < 6 and nota > 1:
    print("desaprobado")
else:
    print("error en las notas, intente nuevamente")

#actividad 3

numero = int(input("ingrese un numero par: "))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("por favor ingrese un numero par")

#actividad 4

edad = int(input("ingrese su edad: "))

if edad < 12:
    print("es un niño")
elif edad >= 12 and edad < 18:
    print("es un adolescente")
elif edad >= 18 and edad < 30:
    print("es un adulto joven")
elif edad > 30:
    print("es un adulto")

#actividad 5

clave = str(input("ingrese una contraseña de entre 8 y 14 caracteres: "))
if len(clave) >= 8 and len(clave) <= 14:
    print("la contraseña es correcta")
else:
    print("por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#actividad 6

from statistics import median, mode, mean
import random
numeros = [random.randint(1, 100) for i in range(10)]

mediana = median(numeros)
moda = mode(numeros)
media = mean(numeros)
print("la media es: ",media)
print("la mediana es: ", mediana)
print("la moda es: ", moda)

if media > mediana > moda:
    print("tiene un sesgo positivo")
elif media < mediana < moda:
    print("tiene un sesgo negativo")
elif media == mediana == moda:
    print("no tiene sesgo")
else:
    print("no pertenecea ninguna de las 3 opciones anteriores")

#actividad 7

texto = str(input("ingrese una frase o palabra: "))
ultima_letra = texto[-1].lower()
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{texto}!")
else:
    print(texto)

#actividad 8

nombre = input("ingrese su nombre: ")
opcion = int(input("ingrese el numero 1 si quiere su nombre en minusculas,el numero 2 si lo desea en mayusculas o el numero 3 si lo desea con la primera letra en mayuscula: "))

if opcion == 1:
    nombre = nombre.lower()
    print(nombre)
elif opcion == 2:
    nombre = nombre.upper()
    print(nombre)
elif opcion == 3:
    nombre = nombre.title()
    print(nombre)
else:
    print("error, seleccione una opcion correcta")

#actividad 9

magnitud = float(input("ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("es un temblor muy leve,imperceptible")
elif magnitud >= 3 and magnitud < 4:
    print("es un temblor leve,ligeramente perceptible")
elif magnitud >= 4 and magnitud < 5:
    print("es un temblor moderado,sentido por las personas pero sin daños")
elif magnitud >= 5 and magnitud < 6:
    print("es un temblor fuerte, puede provocar daños en estructuras leves")
elif magnitud >= 6 and magnitud < 7:
   print("es un terremoto muy fuerte,puede provocar grandes daños") 
elif magnitud >= 7:
    print("es un terremoto practicamente extremo, puede provocar daños a gran escala")

#actividad 10

hemisferio = input("ingrese el hemisferio en el que se encuentra (norte o sur): ")
mes = str(input("ingrese el mes (en palabras): "))
dia = int(input("ingrese el dia (numero): "))
hemisferio = hemisferio.lower()
mes = mes.lower()
if mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
    if dia > 31 or dia < 1:
        print("error en la fecha")
        exit()
elif mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre":
    if dia > 30 or dia < 1:
        print("error en la fecha")
        exit()
elif mes == "febrero":
    if dia > 28 or dia < 1:
        print("error en la fecha")
        exit()
else:
    print("fecha invalida")
    exit()
if hemisferio == "norte":
    if (mes == "marzo" and dia > 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
        print(" es primavera")
    elif (mes == "junio" and dia > 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
        print("es verano")
    elif (mes == "septiembre" and dia > 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
        print("es otoño")
    elif (mes == "diciembre" and dia > 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
        print("es invierno")

elif hemisferio == "sur":
    if (mes == "marzo" and dia > 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
        print(" es otoño")
    elif (mes == "junio" and dia > 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
        print("es invierno")
    elif (mes == "septiembre" and dia > 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
        print("es primavera")
    elif (mes == "diciembre" and dia > 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
        print("es verano")
else:
    print("error en la fecha")