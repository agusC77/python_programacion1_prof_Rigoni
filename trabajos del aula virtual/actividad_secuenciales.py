#actividad 1
print("Hola Mundo!")
#actividad 2
nombre = input("ingrese su nombre: ")
print (f"Hola {nombre}!")
#actividad 3
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad =int(input("ingrese su edad: "))
residencia = input("ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {residencia}")
#actividad 4
import math
radio = int(input("ingrese el radio de un circulo: "))
perimetro = radio * math.pi * 2
area = math.pi * (radio ** 2)
print(f"el perimetro del circulo es {perimetro} y el area es: {area}")
#actividad 5
segundos = int(input("ingrese una cantidad de segundos: "))
horas = segundos /3600
print(f"{segundos} segundos serian: {horas} hora/s")
#actividad 6
numero = int(input("ingrese un numero: "))
tabla = numero * 1
print(f"{numero} * 1 = {tabla}")
tabla = numero * 2
print(f"{numero} * 2 = {tabla}")
tabla = numero * 3
print(f"{numero} * 3 = {tabla}")
tabla = numero * 4
print(f"{numero} * 4 = {tabla}")
tabla = numero * 5
print(f"{numero} * 5 = {tabla}")
tabla = numero * 6
print(f"{numero} * 6 = {tabla}")
tabla = numero * 7
print(f"{numero} * 7 = {tabla}")
tabla = numero * 8
print(f"{numero} * 8 = {tabla}")
tabla = numero * 9
print(f"{numero} * 9 = {tabla}")
tabla = numero * 10
print(f"{numero} * 10 = {tabla}")
#actividad 7
numero1 =int(input("ingrese un numero distinto a 0: "))
numero2 = int(input("ingrese un segundo numero distinto a 0: "))
if numero1 and numero2 !=0:
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2
    print(f"la suma de los numeros es: {suma}, la resta es: {resta}, la multiplicacion es: {multi} y la division es: {div}")
else:
    print("los numeros deben ser distinos a 0")
#actividad 8
altura =float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kg: "))
imc = peso / (altura**2)
print (f"su indice de masa corporal es {imc}")
#actividad 9
temperatura = float(input("ingrese una temperatura en grados celsius: "))
temperatura_fahrenheit = 9/5 * temperatura + 32
print (f"la temperatura en fahrenheit es: {temperatura_fahrenheit}")
#actividad 10
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f" el promedio de los numeros es: {promedio}")
