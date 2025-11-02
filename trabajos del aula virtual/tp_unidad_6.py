#actividad 1
def imprimir_hola_mundo(frase):
    print(frase)

frase = "Hola mundo!"
imprimir_hola_mundo(frase)

#actividad 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("ingrese su nombre: ")
print(saludar_usuario(nombre))

#actividad 3
def informacion_personal(nombre, apellido,edad, residencia):
    return f"Hola!, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
residencia = input("ingrese el lugar donde vive: ")
edad = int(input("ingrese su edad: "))
print(informacion_personal(nombre,apellido,edad,residencia))

#actividad 4
import math
def calcular_area_circulo(radio):
    area = math.pi * (radio**2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("ingrese el radio del circulo: "))
print(f"el area del circulo es {calcular_area_circulo(radio)}")
print(f"el perimetro del circulo es {calcular_perimetro_circulo(radio)}")

#actividad 5
def segundos_a_horas(segundos):
    horas = segundos/3600
    return horas
segundos = int(input("ingrese la cantidad de segundos: "))
print(f"la cantidad de {segundos} segundos es equivalente a {segundos_a_horas(segundos)} hora/s")

#actividad 6

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("ingrese un numero: "))
tabla_multiplicar(numero)

#actividad 7

#actividad 7
def operaciones_basicas(a, b):
    res_suma = a + b
    res_resta = a - b
    res_multiplicacion = a * b
    if b != 0:
        res_division = a/b
    else:
        res_division = "no se puede dividir por 0"
    tupla_resultados = (res_suma,res_resta,res_multiplicacion,res_division)
    return tupla_resultados
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
res = operaciones_basicas(num1,num2)
print(f"el resultado de la suma es {res[0]}")
print(f"el resultado de la resta es {res[1]}")
print(f"el resultado de la multiplicacion es {res[2]}")
print(f"el resultado de la division es {res[3]}")

#actividad 8

def calcular_imc(peso, altura):
    indice_masa_corporal = peso / (altura ** 2)
    return indice_masa_corporal

peso = float(input("ingrese su peso en kilogramos: "))
altura = float(input("ingrese su altura en metros: "))
print(f"el indice de masa corporal en base al peso y altura dadas es {calcular_imc(peso,altura):.2f}")

#actividad 9

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celsius = float(input("ingrese la temperatura en grados celsius: "))
print(f"la temperatura {celsius} en grados fahrenheit es {celsius_a_fahrenheit(celsius)}")

#actividad 10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un segundo numero: "))
num3 = int(input("ingrese un tercer numero: "))
print(f"el promedio es {calcular_promedio(num1,num2,num3):.2f}")