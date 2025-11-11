# ============================================
#   TRABAJO PRÁCTICO DE RECURSIVIDAD
# ============================================

# ============================================
# EJERCICIO 1: Factorial de un número
# ============================================

def factorial(n):
    #Calcula el factorial de un número
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número para calcular su factorial: "))
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")
print()


# ============================================
# EJERCICIO 2: Serie de Fibonacci
# ============================================

def fibonacci(pos):
    #Devuelve el número en la posición dada de la serie de Fibonacci
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingrese hasta qué posición desea mostrar la serie de Fibonacci: "))
for i in range(n):
    print(fibonacci(i), end=" ")
print("\n")


# ============================================
# EJERCICIO 3: Potencia recursiva
# ============================================

def potencia(base, exponente):
    #Calcula base^exponente
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))
print(f"{b} elevado a la {e} es: {potencia(b, e)}\n")


# ============================================
# EJERCICIO 4: Conversión decimal a binario
# ============================================

def decimal_a_binario(num):
    #Convierte un número decimal a binario
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

numero = int(input("Ingrese un número decimal para convertir a binario: "))
resultado = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {resultado}\n")


# ============================================
# EJERCICIO 5: Palíndromo
# ============================================

def es_palindromo(palabra):
    #Verifica si una palabra es palindroma
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
print(f"¿'{texto}' es palíndromo?: {es_palindromo(texto)}\n")


# ============================================
# EJERCICIO 6: Suma de dígitos
# ============================================

def suma_digitos(n):
    #Suma los dígitos de un número entero
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número para sumar sus dígitos: "))
print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}\n")


# ============================================
# EJERCICIO 7: Pirámide de bloques
# ============================================

def contar_bloques(n):
    #Calcula el total de bloques en una pirámide
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}\n")


# ============================================
# EJERCICIO 8: Contar dígito
# ============================================

def contar_digito(numero, digito):
    #Cuenta cuántas veces aparece un dígito en un número
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
d = int(input("Ingrese el dígito que desea contar: "))
print(f"El dígito {d} aparece {contar_digito(numero, d)} veces en {numero}")