import math
import random


#
# Ejercicio 1
#
print("\nComprobar si un numero es PAR o IMPAR")
numero_del_usuario = input("Ingrese un numero: ")       # Pido primero al usuario un numero (es devuelto como string)
numero_del_usuario = int(numero_del_usuario)            # Convierto el valor alfanumerico que me dio el usuario, a numero

print("")

if ((numero_del_usuario % 2) == 0):                     # Primero compruebo SI es par
    print("El numero que ingresaste fue par")           # Si es par, entra aca
else:                                                   
    print("El numero que ingresaste no fue par")        # Si no es par, entra aca



#
# Ejercicio 2
#
print("\n\nEncontrar el mayor de DOS numeros")
numero1 = int(input("Te pido que me des un numero: "))
numero2 = int(input("Te pido que me des otro numero: "))

print("")

if (numero1 > numero2):
    print(f"El numero {numero1} es mayor al numero {numero2}")
elif (numero1 == numero2):
    print(f"El numero {numero1} es igual al numero {numero2}")
else:
    print(f"El numero {numero1} es menor al numero {numero2}")



#
# Ejercicio 3
#
print("\n\nEncontrar el mayor de TRES numeros")
numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))
numero3 = int(input("Ingrese el tercer numero entero: "))

mayor = numero1

print("")

if (numero1 > numero2 and numero1 > numero3):               # Si numero1 es mayor que el resto
    mayor = numero1
elif (numero2 > numero1 and numero2 > numero3):             # Sino, si el numero2 es mayor que el resto
    mayor = numero2
else:                                                       # Por descarte si ninguno de los anteriores es mayor, queda como mayor el numero3
    mayor = numero3

print(f"El numero mayor: {mayor}")



#
# Ejercicio 4
#
print("\n\nComprobar si eres mayor de 18")
edad = int(input("Ingrese su edad: "))

print("")

if (edad > 18):
    print("Usted es mayor de edad!")
else:
    print("Usted es menor")



#
# Ejercicio 5
# 
print("\n\nComprobar vocales o consonantes")
caracter = input("Ingrese una vocal o consonante: ")    # Primero pido el dato

print("")

if (len(caracter) > 1):                                 # Compruebo que sea solo un caracter el ingresado
    print("Ingresaste mal, volve a intentar")
else:                                                   # Si esta bien, compruebo vocal y consonante
    if (caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"):
        print("El caracter ingresado es vocal!")
    elif (caracter.isalpha()):
        print("El caracter ingresado es consonante!")
    else:
        print("El caracter ingresado es simbolo o numero :(")



#
# Ejercicio 6
#
print("\n\nConvertir calificacion del 'Sistema Numerico' al 'Sistema Alfabetico'")
nota = float(input("Ingrese su calificacion (1 - 10): "))
nota_alfabetica = ""

print("")

if (nota < 1 or nota > 10):
    print("La calificacion esta fuera del rango valido.")
elif (nota >= 9 and nota <= 10):
    nota_alfabetica = "A"
elif (nota >= 8):
    nota_alfabetica = "B"
elif (nota >= 7):
    nota_alfabetica = "C"
elif (nota >= 6):
    nota_alfabetica = "D"
else:
    nota_alfabetica = "F"

if (nota_alfabetica != ""):                                 # Si nota_alfabetica no esta vacia
    print(f"Su nota es: {nota_alfabetica}")



#
# Ejercicio 7
#
print("\n\nTabla Multiplicar (FOR)")
num = int(input("Ingrese el numero para generar la tabla: "))

print("")

for i in range(1, 11):                                      # Iterando
    multiplo = i * num                                      # Calculando
    print(f"{num} x {i} = {multiplo}")                      # Mostrando


print("\nTabla Multiplicar (WHILE)")
num = int(input("Ingrese el numero para generar la tabla: "))

print("")

i = 1
while (i < 11):                                             # Iterando
    multiplo = i * num                                      # Calculando
    print(f"{num} x {i} = {multiplo}")                      # Mostrando
    i = i + 1                                               # Actualizando "i"



#
# Ejercicio 8
#
print("\n\nSumar los primeros n numeros naturales")
n = int(input("Ingrese el valor de n: "))
suma = 0
maximo = n + 1

print("")

for i in range(1, maximo):
    suma += i                                               # Acumular cada suma en una variable

print(f"La suma de los primeros {n} números naturales es: {suma}")



#
# Ejercicio 9
#
print("\n\nCalcular Factorial de un numero")
num = int(input("Ingrese un numero entero positivo: "))
factorial = 1                                               # Factorial empieza desde 1

print("")

if (num <= 0):                                              # Si no se corresponde, no se calcula y se muestra el error
    print("El numero no puede ser ni 0 ni negativo.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print(f"El factorial de {num} es: {factorial}")



#
# Ejercicio 10
#
print("\n\nCalcular serie Fibonacci para un numero")
num = int(input("Ingrese un numero entero positivo: "))

print("")

if (num < 0):                                                   # Compruebo valores incorrectos
    print("El numero no puede ser negativo.")                   # Muestro error
else:
    a = 0                                                       # Preparo los primeros valores de la serie Fib
    b = 1
    #print(f"Serie Fibonacci de {num}: [ ", end="")

    for i in range(num):                                        # Arranco la serie hasta "num"
        temp = a                                                # Salvo el ultimo valor "a", aparte
        a = b                                                   # Actualizo el valor de "a" por el de "b"
        b = temp + b                                            # Ahora sumo el viejo valor de "a" + "b" y actualizo "b"
        print(temp)                                             # Muestro el valor "a" previamente salvado
        #print(f"{temp}", end=" , ")                             # Muestro el valor "a" previamente salvado
    
    #print("\b\b ]")



#
# Ejercicio 11
#
print("\n\nDeterminar si un numero ingresado es primo")
num = int(input("Ingrese un numero natural: "))
es_primo = True                                                 # Asumir que el numero puede ser primo, comprobar lo contrario

print("")

if (num < 2 or num % 2 == 0):                                   # Si es menor o divisible por 2, entonces no es primo
    es_primo = False
else:
    raiz_num = int(math.sqrt(num))

    for i in range(3, raiz_num + 1, 2):                         # Desde 3 hasta la raiz cuadrada de "num", pasando por todos los impares
        if (num % i == 0):                                      # Comprobar si "num" es divisible por alguno de los impares
            es_primo = False                                    # Si lo es, entonces no era primo
            break

if (es_primo):                                                  # Si llegamos hasta aca, sin caer en las anteriores condiciones, entonces es primo
    print("El numero es primo!")
else:
    print("El numero no es primo :(")



#
# Ejercicio 12
#
print("\n\nComprobar palindromo")
palabra = input("Ingrese una palabra: ").lower()
palabra_invertida = "".join(reversed(palabra))
es_palindromo = True

print("")

if (palabra != palabra_invertida):
    es_palindromo = False

if (es_palindromo):
    print("La palabra es palindromo!")
else:
    print("La palabra no es palindromo :(")



#
# Ejercicio 13
#
print("\n\nAdivinar el numero entre 1 y 100")
numero_aleatorio = random.randint(1, 100)
intentos = 10

print("")

while True:
    if (intentos <= 0):
        print(f"Perdiste, el numero era ({numero_aleatorio})")
        break
    
    print(f"\nIntentos: {intentos}\n")
    
    numero_adivinado = int(input("Ingrese un numero: "))
    
    if (numero_aleatorio < numero_adivinado):
        print("El numero que buscas es menor")
    elif (numero_aleatorio > numero_adivinado):
        print("El numero que buscas es mayor")
    else:
        print(f"Ganaste!, has acertado al numero!")
        break

    intentos -= 1



#
# Ejercicio 14
#
print("\n\nJuego de dados")
puntaje = 0
seguir_jugando = True

print("")

while (seguir_jugando):
    print("\nTirando los dados...\n")
    
    dado_uno = random.randint(1, 6)
    dado_dos = random.randint(1, 6)
    puntaje = puntaje + (dado_uno + dado_dos)
    
    print(f"Primer dado: {dado_uno}")
    print(f"Segundo dado: {dado_dos}")
    print("")

    print(f"El puntaje acumulado hasta el momento es: {puntaje}")
    respuesta = input("Desea continuar jugando? (Y/N): ").lower()
    print("")

    if (respuesta == "n"):
        seguir_jugando = False



#
# Ejercicio 15
#
print("\n\nPiedra, Papel o Tijera")
print("\nGanar  = +1 puntos\nPerder = -1 puntos\nEmpate = 0 puntos\n")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
print("")

puntaje = 0

while True:
    eleccion_computadora = random.randint(1, 3)
    eleccion_jugador = int(input("Ingrese el numero de su jugada: "))

    print("")

    if (eleccion_jugador < 1 or eleccion_jugador > 3):
        print("Jugada invalida, saliendo...")
        break

    print("\tComputadora:\t", end = "")
    
    if (eleccion_computadora == 1):
        print("Piedra")
    if (eleccion_computadora == 2):
        print("Papel")
    if (eleccion_computadora == 3):
        print("Tijera")

    print("\tJugador:\t", end = "")

    if (eleccion_jugador == 1):
        print("Piedra")
    if (eleccion_jugador == 2):
        print("Papel")
    if (eleccion_jugador == 3):
        print("Tijera")

    print("")

    if (eleccion_jugador == eleccion_computadora):
        print("\tEmpate!")
    elif (eleccion_jugador == 1 and eleccion_computadora == 3) or (eleccion_jugador == 2 and eleccion_computadora == 1) or (eleccion_jugador == 3 and eleccion_computadora == 2):
        print("\tGanaste! (+1)")
        puntaje += 1
    else:
        print("\tPerdiste! (-1)")
        puntaje -= 1

    print(f"\nPuntaje acumulado: {puntaje}")

    respuesta = input("\nDesea seguir jugando? (Y/N): ").lower()
    
    print("\n")

    if (respuesta == "n"):
        break