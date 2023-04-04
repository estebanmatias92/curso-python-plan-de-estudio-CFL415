import math                                             # Libreria con funciones matematicas dentro
import random                                           # Libreria o Modulo que tiene las funciones random


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
caracter = caracter.lower()                             # Convierto a minusculas para poder comparar solo entre minusculas

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

if (num < 2):                                                   # Si es menor a 2, entonces es primo
    es_primo = False
elif (num > 2 and num % 2 == 0):                                # Si es mayor a 2 y divisible por 2, entonces no es primo
    es_primo = False
else:
    raiz_num = math.ceil(math.sqrt(num))                        # Obtengo la raiz de "num" 

    for i in range(3, raiz_num, 2):                             # Desde 3 hasta la raiz cuadrada de "num", pasando por todos los impares
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
palabra = input("Ingrese una palabra: ").lower()                # Pido por el STRING a comprobar, la convierto en minusculas tambien
palabra_invertida = "".join(reversed(palabra))                  # Ese STRING lo invierto de orden, lo cual devuelve una LISTA y a esa LISTA la vuelvo a convertir en STRING
#palabra_invertida = palabra[::-1]                              # Otro modo de invertir una cadena es usando el operador [::-1]
es_palindromo = True                                            # Asumo que puede ser True desde el principio, deja como unico camino, comprobar que sea falso y cambiar su valor en consecuencia

print("")

if (palabra != palabra_invertida):                              # Si al comparar ambos STRING, no son iguales, entonces si cambio el valor a False
    es_palindromo = False

if (es_palindromo):                                             # Ahora puedo mostrar si fue o no Palindromo
    print("La palabra es palindromo!")
else:
    print("La palabra no es palindromo :(")



#
# Ejercicio 13
#
print("\n\nAdivinar el numero entre 1 y 100")
numero_aleatorio = random.randint(1, 100)                       # Genero un numero entero random entre 1 y 100
intentos = 10                                                   # Mi juego tendra intento, como condicion para perder, los asigno

print("")

while True:                                                     # Entro en el bucle
    if (intentos <= 0):                                         # Primero compruebo de tener intentos disponibles
        print(f"Perdiste, el numero era ({numero_aleatorio})")
        break                                                   # Sino salgo
    
    print(f"\nIntentos: {intentos}\n")
    
    numero_adivinado = int(input("Ingrese un numero: "))        # Si no salio, es porque hay intentos, entonces empieza el juego
    
    if (numero_aleatorio < numero_adivinado):                   # Sera menor?
        print("El numero que buscas es menor")
    elif (numero_aleatorio > numero_adivinado):                 # Sera mayor?
        print("El numero que buscas es mayor")
    else:                                                       # Cual sera?
        print(f"Ganaste!, has acertado al numero!")
        break                                                   # Si acerto, sale

    intentos -= 1                                               # Cada iteracion del bucle (cada vez que no corta por haber ganado), es un intento menos



#
# Ejercicio 14
#
print("\n\nJuego de dados")
puntaje = 0
seguir_jugando = True                                                   # Asumo que al principio quiere empezar a jugar

print("")

while (seguir_jugando):
    print("\nTirando los dados...\n")
    
    dado_uno = random.randint(1, 6)                                     # Genero un numero entero aleatorio entre 1 y 6
    dado_dos = random.randint(1, 6)                                     # Genero otro mas
    puntaje = puntaje + (dado_uno + dado_dos)                           # Sumo los dados
    
    print(f"Primer dado: {dado_uno}")                                   # Muestro dados
    print(f"Segundo dado: {dado_dos}")
    print("")

    print(f"El puntaje acumulado hasta el momento es: {puntaje}")       # Muestro puntaje
    respuesta = input("Desea continuar jugando? (Y/N): ").lower()       # Pregunto si quiere repetir
    print("")

    if (respuesta == "n"):                                              # Si no quiere, sale con "n" o "N"
        seguir_jugando = False



#
# Ejercicio 15
#
print("\n\nPiedra, Papel o Tijera")
############
############ PRIMERA PANTALLA
############
print("\nGanar  = +1 puntos\nPerder = -1 puntos\nEmpate = 0 puntos\n")

# En mi caso yo elijo hacer toda la logica solo con numeros
# Al jugador le muestro las equivalencias para que sepa que ingresar
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
print("")

puntaje = 0

while True:
    ############
    ############ ETAPA DE ELECCION
    ############
    eleccion_computadora = random.randint(1, 3)                         # Para elegir, uso randint entre 1 y 3
    eleccion_jugador = int(input("Ingrese el numero de su jugada: "))   # Y para que el jugador elija, se lo pido directamente a el

    print("")

    ############
    ############ SEGUNDA PANTALLA
    ############
    if (eleccion_jugador < 1 or eleccion_jugador > 3):                  # Compruebo que el jugador no ingrese nada invalido
        print("Jugada invalida, saliendo...")       
        break                                                           # Si es invalido, sale del WHILE

    print("\tComputadora:\t", end = "")                                 # Empiezo a mostrar la eleccion de la computadora
    
    if (eleccion_computadora == 1):                                     # Sera una de estas 3
        print("Piedra")
    if (eleccion_computadora == 2):
        print("Papel")
    if (eleccion_computadora == 3):
        print("Tijera")

    print("\tJugador:\t", end = "")                                     # Tambien muestro la eleccion del jugador

    if (eleccion_jugador == 1):                                         # Debera ser una de estas tres
        print("Piedra")
    if (eleccion_jugador == 2):
        print("Papel")
    if (eleccion_jugador == 3):
        print("Tijera")

    print("")

    ############
    ############ ETAPA DE CALCULO
    ############
    if (eleccion_jugador == eleccion_computadora):                      # Si ambos eligieron lo mismo, hay empate
        print("\tEmpate!")
    elif (eleccion_jugador == 1 and eleccion_computadora == 3) or (eleccion_jugador == 2 and eleccion_computadora == 1) or (eleccion_jugador == 3 and eleccion_computadora == 2):
        print("\tGanaste! (+1)")                                        # Si el jugador eligio algo mejor, entonces gana la ronda
        puntaje += 1                                                    # Sumo 1 punto al puntaje
    else:   
        print("\tPerdiste! (-1)")                                       # Si la compu elegio mejor, entonces el jugador pierde la ronda
        puntaje -= 1                                                    # Resto 1 punto al puntaje acumulado 

    ############
    ############ TERCERA PANTALLA
    ############
    print(f"\nPuntaje acumulado: {puntaje}")                            # Finalizada la etapa de eleccion y la de calculo, muestro el puntaje

    ############
    ############ PANTALLA FINAL
    ############
    respuesta = input("\nDesea seguir jugando? (Y/N): ").lower()        # Compruebo si quiere seguir jugando
    
    print("\n")

    if (respuesta == "n"):                                              # En caso de no querer seguir, sale con "n" o "N"
        break